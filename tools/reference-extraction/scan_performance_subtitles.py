"""Copy English full-dialogue ASS from all 26 numbered episodes and index leads.

Read-only sources; no audio/video decoding. Complete text/candidate excerpts stay
in ignored working storage. Coverage/provenance metadata are trackable.
Keyword hits are search leads, never automatically verified performance evidence.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PATTERN = re.compile(
    r'\d|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|'
    r'twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|'
    r'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|'
    r'million|billion|half|quarter|double|twice|degrees?|tons?|tonnes?|'
    r'parsecs?|mass|g|inertia\w*|speed|velocity|accelerat\w*|decelerat\w*|kilomet\w*|km|meters?|'
    r'miles?|light.?years?|light.?speed|distance|range|seconds?|minutes?|hours?|'
    r'days?|weeks?|months?|years?|percent|output|propulsion|thrust|reactors?|'
    r'ether|fuel|energy|power|gravity|gravitational|orbit\w*|trajectory|'
    r'coordinates|capacity|temperature|pressure|oxygen|life support|stress|'
    r'overload|critical|threshold|overheat\w*|engines?|verniers?|standby|'
    r'stand.by|cool\w*|stabiliz\w*|landing|launch|countdown|hyperspace)\b', re.I)


def main():
    ffmpeg, ffprobe = shutil.which('ffmpeg'), shutil.which('ffprobe')
    if not ffmpeg or not ffprobe:
        raise RuntimeError('FFmpeg and FFprobe must be on PATH')
    destination = ROOT / 'reference/working/performance-subtitles'
    coverage_path = ROOT / 'reference/indexes/performance-subtitle-coverage.json'
    if destination.exists() or coverage_path.exists():
        raise FileExistsError('Audit outputs already exist; no overwrites')
    destination.mkdir(parents=True)
    version = subprocess.run([ffmpeg, '-version'], capture_output=True, text=True,
                             check=True).stdout.splitlines()[0]
    records = []
    for episode in range(1, 27):
        sources = sorted((ROOT / '_source_episodes').glob(f'*_-_{episode:02}_-_*.mkv'))
        if len(sources) != 1:
            raise ValueError(f'EP-{episode:02}: expected one numbered source')
        source = sources[0]
        probe = json.loads(subprocess.run(
            [ffprobe, '-v', 'error', '-show_streams', '-of', 'json', str(source)],
            capture_output=True, text=True, encoding='utf-8', check=True).stdout)
        matches = [s for s in probe['streams'] if s['codec_type'] == 'subtitle'
                   and s['codec_name'] == 'ass'
                   and s.get('tags', {}).get('language') == 'eng'
                   and 'sign' not in s.get('tags', {}).get('title', '').lower()
                   and 'song' not in s.get('tags', {}).get('title', '').lower()]
        if len(matches) != 1:
            raise ValueError(f'EP-{episode:02}: ambiguous English dialogue track')
        stream = matches[0]
        output = destination / f'episode-{episode:02}.ass'
        command = [ffmpeg, '-v', 'error', '-n', '-i', str(source), '-map',
                   f'0:{stream["index"]}', '-c:s', 'copy', str(output)]
        subprocess.run(command, check=True, capture_output=True)
        dialogue = []
        for line in output.read_text(encoding='utf-8-sig').splitlines():
            if not line.startswith('Dialogue:'):
                continue
            fields = line.split(',', 9)
            if len(fields) != 10:
                raise ValueError(f'Malformed dialogue in {output.name}')
            text = re.sub(r'\{[^}]*\}', '', fields[9]).replace('\\N', ' ').replace('\\n', ' ')
            dialogue.append(dict(index=len(dialogue) + 1, start=fields[1],
                                 end=fields[2], text=text))
        hits = [d for d in dialogue if PATTERN.search(d['text'])]
        candidate_path = output.with_name(f'episode-{episode:02}-candidates.json')
        candidate_path.write_text(json.dumps(dict(dialogue=dialogue, hits=hits),
                                 ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        relative_command = [Path(ffmpeg).name, *command[1:]]
        relative_command[relative_command.index(str(source))] = source.relative_to(ROOT).as_posix()
        relative_command[-1] = output.relative_to(ROOT).as_posix()
        records.append(dict(episode_id=f'EP-{episode:02}',
                            source=source.relative_to(ROOT).as_posix(), source_bytes=source.stat().st_size,
                            subtitle_stream=stream['index'], subtitle_codec=stream['codec_name'],
                            subtitle_tags=stream.get('tags', {}),
                            local_subtitle=output.relative_to(ROOT).as_posix(),
                            subtitle_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
                            command=relative_command, dialogue_records=len(dialogue),
                            keyword_candidates=len(hits), review_status='SEARCH_LEADS_ONLY'))
        print(f'EP-{episode:02}: stream {stream["index"]}; {len(dialogue)} dialogue records; {len(hits)} leads', flush=True)
    coverage_path.write_text(json.dumps(dict(tool_version=version,
                              search_pattern=PATTERN.pattern, episodes=records),
                              ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
