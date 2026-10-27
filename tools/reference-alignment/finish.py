"""Preview and explicitly apply episode alignment-output cleanup after durable evidence checks."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

import alignment as a
import models as m


def inventory(root, episode, discard=()):
    if not 1 <= episode <= 26:
        raise ValueError('Invalid episode')
    if len(set(discard)) != len(discard) or any(not re.fullmatch(r'ALNRUN-[a-f0-9]{32}', x) for x in discard):
        raise ValueError('Invalid explicit discard run IDs')
    anchors, mappings = m.load(root)
    m.validate(anchors, mappings, m.locators(root))
    base = a.safe_path(root, f'reference/working/alignment/EP-{episode:02d}')
    runs = []
    seen = set()
    for path in sorted(base.iterdir()) if base.exists() else []:
        a.safe_path(base, path.name)
        if path.name == 'writer.lock' and path.is_file():
            continue
        if not path.is_dir() or not re.fullmatch(r'ALNRUN-[a-f0-9]{32}', path.name):
            raise ValueError('Unexpected episode workspace entry: ' + path.name)
        manifest_path = a.safe_path(path, 'run.json')
        manifest = a.read_json(manifest_path)
        if manifest.get('owner') != a.VERSION or manifest.get('run_id') != path.name:
            raise ValueError('Unowned run: ' + path.name)
        if manifest.get('status') not in ['COMPLETE_CANDIDATES', 'FAILED']:
            raise ValueError('Active/incomplete run: ' + path.name)
        files = []
        for item in sorted(path.rglob('*')):
            a.safe_path(path, item.relative_to(path))
            if item.is_file():
                files.append(dict(path=item.relative_to(path).as_posix(), bytes=item.stat().st_size,
                                  sha256=a.digest(item)))
        records = [r for r in anchors if r['run_id'] == path.name]
        reason = ''
        disposition = 'VALIDATED_RESULT_CLEANUP'
        if path.name in discard:
            seen.add(path.name)
            if records:
                raise ValueError('Discard cannot bypass registered evidence: ' + path.name)
            disposition = 'EXPLICIT_UNREGISTERED_DISCARD'
        else:
            results = manifest.get('results', [])
            if manifest['status'] != 'COMPLETE_CANDIDATES' or not results:
                reason = 'Failed/empty run requires explicit unregistered discard'
            elif len({r['image_id'] for r in results}) != len(results) or len(records) != len(results):
                reason = 'Every run image needs a durable assessment'
            else:
                by_image = {r['image_id']: r for r in records}
                for result in results:
                    row = by_image.get(result['image_id'])
                    if row is None or row['status'] == 'CANDIDATE':
                        reason = 'Unresolved candidate needs review or explicit keep-output'
                        break
                    recipe = json.loads(row['recipe_json'])
                    if (row['episode_id'] != f'EP-{episode:02d}' or row['input_id'] != manifest.get('input_id')
                            or row['image_sha256'] != result['image_sha256']
                            or row['role'] != result['role']
                            or row['search_start_seconds'] != result['search_start']
                            or row['search_end_seconds'] != result['search_end']
                            or recipe.get('run_manifest_sha256') != a.digest(manifest_path)
                            or any(recipe.get(k) != v for k, v in manifest['recipe'].items())):
                        reason = 'Retained provenance differs from run manifest'
                        break
                    if row['status'] == 'MATCHED':
                        frames = {str(f['pts']): f for f in result['frames']}
                        for pts, digest in recipe['reviewed_frame_hashes'].items():
                            frame = frames.get(pts)
                            if not frame or digest != frame['sha256'] or a.digest(a.safe_path(path, frame['image'])) != digest:
                                reason = 'Reviewed frame bytes differ from retained provenance'
                                break
                    if reason:
                        break
        if any(Path(item['path']).name not in ['run.json', 'comparison.png', 'decode.log']
               and not re.fullmatch(r'frame-[0-9]+\.png', Path(item['path']).name) for item in files):
            reason = 'Unexpected file may contain unique evidence; retain or relocate it before cleanup'
        runs.append(dict(run_id=path.name, eligible=not reason, reason=reason,
                         disposition=disposition, files=files, bytes=sum(f['bytes'] for f in files)))
    if set(discard) != seen:
        raise ValueError('Explicit discard run is absent')
    registers = {name: a.digest(a.safe_path(root, 'reference/indexes/animehistory/' + name))
                 for name in ['alignment-anchors.csv', 'alignment-mappings.csv']
                 if (Path(root)/'reference/indexes/animehistory'/name).exists()}
    plan = dict(episode_id=f'EP-{episode:02d}', runs=runs, register_hashes=registers,
                locator_hashes={p.name: a.digest(p) for p in sorted((Path(root)/'reference/indexes/animehistory/CSVs').glob('episode-*.csv'))})
    token = hashlib.sha256(a.canonical(plan)).hexdigest()
    return dict(**plan, preview_sha256=token, removable_bytes=sum(r['bytes'] for r in runs if r['eligible']))


def finish(root, episode, discard=(), apply=False, preview_sha256=None, keep_output=False):
    if not 1 <= episode <= 26:
        raise ValueError('Invalid episode')
    if apply and keep_output:
        raise ValueError('Choose apply or keep-output')
    base = a.safe_path(root, f'reference/working/alignment/EP-{episode:02d}')
    # Share registry and search locks with their writers throughout recheck/deletion.
    with a.writer(a.safe_path(root, 'reference/working/alignment/registry')), a.writer(base):
        plan = inventory(root, episode, discard)
        if not apply:
            return dict(**plan, action='KEEP_OUTPUT' if keep_output else 'PREVIEW', removed_runs=[])
        if preview_sha256 != plan['preview_sha256']:
            raise ValueError('Preview missing/stale; inspect a fresh preview before applying')
        if any(not r['eligible'] for r in plan['runs']):
            raise ValueError('Unresolved runs block episode cleanup; review or keep output')
        removed = []
        for run in plan['runs']:
            path = a.safe_path(base, run['run_id'])
            for item in path.rglob('*'):
                a.safe_path(path, item.relative_to(path))
            shutil.rmtree(path)
            if path.exists():
                raise ValueError('Run cleanup incomplete')
            removed.append(run['run_id'])
        remaining = inventory(root, episode)
        if remaining['runs']:
            raise ValueError('Episode cleanup incomplete')
        return dict(**plan, action='REMOVED', removed_runs=removed)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--episode', type=int, required=True)
    p.add_argument('--discard-run', action='append', default=[])
    choice = p.add_mutually_exclusive_group()
    choice.add_argument('--apply', action='store_true')
    choice.add_argument('--keep-output', action='store_true')
    p.add_argument('--preview-sha256')
    args = p.parse_args()
    try:
        report = finish(a.ROOT, args.episode, args.discard_run, args.apply,
                        args.preview_sha256, args.keep_output)
        for run in report['runs']:
            run['file_count'] = len(run.pop('files'))
        print(json.dumps(report, indent=2))
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps(dict(error=str(exc))), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
