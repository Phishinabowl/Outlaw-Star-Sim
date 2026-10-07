"""Inspect one local episode with FFprobe; never decode or modify video."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('episode', type=int, choices=range(1, 27))
    args = parser.parse_args()
    matches = sorted((ROOT / '_source_episodes').glob(f'*_-_{args.episode:02}_-_*'))
    if len(matches) != 1:
        parser.error(f'Expected exactly one episode file; found {len(matches)}')
    probe = shutil.which('ffprobe')
    if not probe:
        parser.error('FFprobe not found on PATH')
    source = matches[0]
    version = subprocess.run([probe, '-version'], check=True, capture_output=True, text=True).stdout.splitlines()[0]
    flags = ['-v', 'error', '-show_format', '-show_streams', '-show_chapters', '-of', 'json']
    result = subprocess.run([probe, *flags, str(source)], check=True, capture_output=True, text=True, encoding='utf-8')
    metadata = json.loads(result.stdout)
    relative = source.relative_to(ROOT).as_posix()
    metadata['format']['filename'] = relative
    record = dict(episode_id=f'EP-{args.episode:02}', source=relative,
                  source_bytes=source.stat().st_size, tool_version=version,
                  probe_arguments=flags, metadata=metadata)
    output = ROOT / 'reference' / 'indexes' / f'episode-{args.episode:02}-metadata.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Wrote {output.relative_to(ROOT).as_posix()}')
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
