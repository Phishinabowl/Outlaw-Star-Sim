"""Extract up to 32 explicitly requested episode frames, recording decoded PTS.

Generated PNGs/logs are local-only. No scaling or subtitle burn-in is applied.
"""
import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def seconds(value):
    try:
        number = Decimal(value)
    except InvalidOperation:
        raise argparse.ArgumentTypeError('Time must be seconds')
    if not number.is_finite() or number < 0:
        raise argparse.ArgumentTypeError('Time must be finite and nonnegative')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('episode', type=int, choices=range(1, 27))
    parser.add_argument('--batch', required=True)
    parser.add_argument('--time', type=seconds, action='append', required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z][a-z0-9-]{0,47}', args.batch):
        parser.error('Batch must be a lowercase letter followed by letters/digits/hyphens')
    if len(args.time) > 32 or len(set(args.time)) != len(args.time):
        parser.error('Supply at most 32 distinct explicit times')
    matches = sorted((ROOT / '_source_episodes').glob(f'*_-_{args.episode:02}_-_*.mkv'))
    if len(matches) != 1:
        parser.error(f'Expected one source episode; found {len(matches)}')
    ffmpeg, ffprobe = shutil.which('ffmpeg'), shutil.which('ffprobe')
    if not ffmpeg or not ffprobe:
        parser.error('FFmpeg and FFprobe must be on PATH')
    source = matches[0]
    probe = json.loads(subprocess.run(
        [ffprobe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(source)],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout)
    duration = Decimal(probe['format']['duration'])
    if any(t >= duration for t in args.time):
        parser.error('Requested time exceeds source duration')
    video = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    destination = ROOT / 'reference' / 'extracted-frames' / f'episode{args.episode:02}' / args.batch
    index = ROOT / 'reference' / 'indexes' / f'episode-{args.episode:02}-{args.batch}-frames.json'
    for path in (destination, index):
        resolved = path.resolve()
        if not resolved.is_relative_to((ROOT / 'reference').resolve()):
            parser.error('Output resolves outside reference directory')
        if any(resolved.is_relative_to((ROOT / folder).resolve())
               for folder in ('_source_settei', '_source_episodes')):
            parser.error('Output resolves into an immutable source directory')
    if destination.exists() or index.exists():
        parser.error('Batch already exists; choose a new name (no overwrites)')
    version = subprocess.run([ffmpeg, '-version'], capture_output=True,
                             text=True, check=True).stdout.splitlines()[0]
    destination.mkdir(parents=True)
    records = []
    for number, requested in enumerate(args.time, 1):
        output = destination / f'frame-{number:02}.png'
        command = [ffmpeg, '-hide_banner', '-nostdin', '-n', '-loglevel', 'info',
                   '-copyts', '-ss', str(requested), '-i', str(source),
                   '-map', f'0:{video["index"]}', '-an', '-sn', '-dn',
                   '-vf', 'showinfo', '-frames:v', '1', '-fps_mode', 'passthrough',
                   '-update', '1', str(output)]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        log = output.with_suffix('.log')
        log.write_text(result.stderr, encoding='utf-8')
        result.check_returncode()
        # showinfo may log a second buffered frame. The PNG uses the first (n=0).
        match = re.search(r'n:\s*0\s+pts:\s*(-?\d+)\s+pts_time:([\d.eE+-]+)', result.stderr)
        base = re.search(r'config in time_base:\s*(\d+/\d+)', result.stderr)
        if not match or not base or not output.is_file():
            raise ValueError(f'Cannot establish frame PTS: {output.name}')
        relative_command = [Path(ffmpeg).name, *command[1:]]
        relative_command[relative_command.index(str(source))] = source.relative_to(ROOT).as_posix()
        relative_command[-1] = output.relative_to(ROOT).as_posix()
        records.append(dict(frame_id=f'EP-{args.episode:02}-{args.batch}-{number:02}',
                            requested_seconds=str(requested), decoded_pts=int(match[1]),
                            decoded_pts_seconds=match[2], time_base=base[1],
                            video_stream=video['index'], width=video['width'], height=video['height'],
                            image=output.relative_to(ROOT).as_posix(),
                            image_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
                            log=log.relative_to(ROOT).as_posix(), command=relative_command,
                            observation_status='UNREVIEWED'))
        print(f'{output.name}: requested {requested}s; decoded {match[2]}s', flush=True)
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(json.dumps(dict(episode_id=f'EP-{args.episode:02}',
                                     source=source.relative_to(ROOT).as_posix(),
                                     source_bytes=source.stat().st_size, tool_version=version,
                                     records=records), indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
