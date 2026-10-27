"""Reproduce one accepted anchor's bounded decoded PNG hashes, without restoring old runs."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import tempfile

import alignment as a
import models as m


def reproduce(root, anchor_id, ffmpeg, ffprobe):
    anchors, mappings = m.load(root)
    m.validate(anchors, mappings, m.locators(root))
    selected = [r for r in anchors if r['anchor_id'] == anchor_id and r['status'] == 'MATCHED']
    if len(selected) != 1:
        raise ValueError('Select exactly one accepted anchor')
    row = selected[0]
    source = a.safe_path(root, row['video_source'])
    source_signature = a.signature(source)
    m.verify_current(root, [row], ffprobe)
    recipe = json.loads(row['recipe_json'])
    scratch = a.safe_path(root, '.tmp/alignment-reproduction')
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='reproduce-', dir=scratch) as name:
        stage = a.safe_path(scratch, Path(name).name)
        budget = a.Budget(stage, frames=180, size=200*1024**2, wall=120)
        version = a.run_process([ffmpeg, '-version'], budget).decode('utf-8').splitlines()[0]
        if version != recipe['tools']['ffmpeg']:
            raise ValueError('FFmpeg version differs from retained recipe; byte reproduction not claimed')
        # Parse bounded seek/duration only. Never execute stored command text or arbitrary flags.
        windows = set()
        for command in recipe['commands']:
            output = Path(command[-1]).parts
            if row['image_id'] not in output or not any(part.startswith('fine-') for part in output):
                continue
            start = F(command[command.index('-ss')+1])
            end = start + F(command[command.index('-t')+1])
            lo, hi = m.interval(row)
            if start <= lo <= hi < end:
                windows.add((start, end))
        if not windows:
            raise ValueError('No retained native-frame window covers this anchor')
        start, end = sorted(windows)[0]
        if end-start > 1:
            raise ValueError('Reproduction exceeds one-second pilot bound')
        frames, _ = a.decode(ffmpeg, source,
            int(row['video_stream_index']), F(row['video_time_base']), F(row['media_origin_seconds']),
            start, end, stage/'decode', budget, False)
        actual = {str(r['pts']): a.digest(r['path']) for r in frames}
        expected = recipe['reviewed_frame_hashes']
        if not expected or any(actual.get(pts) != digest for pts,digest in expected.items()):
            raise ValueError('Reproduced frame hashes differ from retained accepted evidence')
        if a.signature(source) != source_signature:
            raise ValueError('Source changed during reproduction')
        result = dict(anchor_id=anchor_id, status='REPRODUCED', decoded_frames=len(frames),
                      matched_frame_hashes=len(expected), window_start_seconds=a.ratio(start),
                      window_end_seconds=a.ratio(end), source_sha256=row['video_sha256'],
                      input_id=row['input_id'], temporary_output_removed=True)
    if stage.exists():
        raise ValueError('Reproduction output cleanup incomplete')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--anchor-id',required=True)
    p.add_argument('--ffmpeg',required=True)
    p.add_argument('--ffprobe',required=True)
    args=p.parse_args()
    print(json.dumps(reproduce(a.ROOT,args.anchor_id,args.ffmpeg,args.ffprobe)))


if __name__=='__main__':main()
