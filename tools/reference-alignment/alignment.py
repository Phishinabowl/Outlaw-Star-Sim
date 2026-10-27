"""Bounded gallery/local-frame candidate search. No authored table or model writes."""
import argparse
import csv
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import uuid

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat
from PIL import __version__ as PILLOW_VERSION

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/reference-context'))
from core import safe_path, writer, atomic, encode

VERSION = 'alignment-prototype-v1'
MAX_FRAMES = 900
MAX_BYTES = 600 * 1024**2
MAX_SECONDS = 900
PROTOTYPE = {'846774', '846776', '846800', '846823', '846843'}
STAGE3_ROLES = dict.fromkeys(['846782','846844','846916','846988','847060','847120'],'FIT')
STAGE3_ROLES.update(dict.fromkeys(['846790','846880','847024','847102'],'HOLDOUT'))
STAGE3_ROLES.update(dict.fromkeys(['846856','846859','846976','846980','847029','847031','847100'],'FIT'))
STAGE3_ROLES.update(dict.fromkeys(['846985','847030','847093'],'HOLDOUT'))


def ratio(value):
    value = F(str(value))
    return f'{value.numerator}/{value.denominator}'


def seconds(value):
    return f'{float(value):.9f}'


def digest(path, budget=None):
    h = hashlib.sha256()
    before = signature(path)
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024**2), b''):
            h.update(block)
            if budget is not None:
                budget.check()
    if signature(path) != before:
        raise ValueError('Input changed while hashing')
    return h.hexdigest()


def signature(path):
    st = Path(path).stat()
    return st.st_size, st.st_mtime_ns, st.st_ctime_ns, st.st_ino


def read_json(path):
    return json.loads(Path(path).read_text('utf-8'))


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def input_id(identity):
    return hashlib.sha256(canonical(identity)).hexdigest()


class Budget:
    def __init__(self, path, frames=MAX_FRAMES, size=MAX_BYTES, wall=MAX_SECONDS):
        self.path, self.frames, self.size = Path(path), frames, size
        self.deadline = time.monotonic() + wall

    def check(self):
        files = list(self.path.rglob('*'))
        total = sum(p.stat().st_size for p in files if p.is_file())
        count = sum(p.suffix == '.png' and p.name.startswith('frame-') for p in files)
        if count > self.frames or total > self.size or time.monotonic() >= self.deadline:
            raise ValueError('Run frame/disk/time budget exceeded')
        return count, total


def run_process(command, budget, log=None):
    """Bounded subprocess, killed and reaped on timeout/resource failure; never use a shell."""
    budget.check()
    timeout = max(0.01, budget.deadline - time.monotonic())
    if log is None:
        result = subprocess.run(command, capture_output=True, timeout=timeout, check=True)
        budget.check()
        if len(result.stdout) + len(result.stderr) > 8 * 1024**2:
            raise ValueError('Oversized probe output')
        return result.stdout
    with Path(log).open('wb') as stream:
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=stream)
        try:
            while process.poll() is None:
                budget.check()
                time.sleep(0.05)
            budget.check()
            if process.returncode:
                raise ValueError(f'FFmpeg failed ({process.returncode}); see local log')
        finally:
            if process.poll() is None:
                process.kill()
            process.wait()


def masks_checked(rectangles):
    mask = Image.new('L', (320, 240), 255)
    draw = ImageDraw.Draw(mask)
    for box in rectangles:
        if len(box) != 4 or not (0 <= box[0] < box[2] <= 320 and 0 <= box[1] < box[3] <= 240):
            raise ValueError('Mask must be x0,y0,x1,y1 inside 320x240')
        draw.rectangle((box[0], box[1], box[2]-1, box[3]-1), fill=0)
    retained = int(ImageStat.Stat(mask).sum[0]) // 255
    if retained * 10 < 320 * 240 * 7:
        raise ValueError('Mask leaves less than 70 percent of picture')
    return mask, retained


def normalized(path, expected_aspect=None):
    with Image.open(path) as image:
        image.load()
        aspect = F(image.width, image.height)
        if expected_aspect is not None and abs(aspect / expected_aspect - 1) > F(1, 50):
            raise ValueError('Picture aspect mismatch; explicit normalization review required')
        return image.convert('L').resize((320, 240), Image.Resampling.LANCZOS), aspect


def score(a, b, mask, retained):
    delta = ImageChops.multiply(ImageChops.difference(a, b), mask)
    return 1 - F(int(ImageStat.Stat(delta).sum[0]), 255 * retained)


def clusters(records):
    if not records:
        return []
    best = max(r['score'] for r in records)
    threshold = max(F(9, 10), best-F(1, 100))
    selected = [r for r in records if r['score'] >= threshold]
    if not selected:
        selected = [r for r in records if r['score'] >= best-F(1, 100)]
    groups = []
    for record in sorted(selected, key=lambda r: r['local']):
        if not groups or record['local']-groups[-1][-1]['local'] > F(1, 2):
            groups.append([])
        groups[-1].append(record)
    return sorted(groups, key=lambda g: (-max(r['score'] for r in g), g[0]['local']))


def candidate_state(groups):
    if not groups:
        return 'NO_CANDIDATES', None
    scores = sorted((max(r['score'] for r in g) for g in groups), reverse=True)
    gap = scores[0]-scores[1] if len(scores) > 1 else None
    if scores[0] < F(9, 10):
        return 'LOW_SCORE_REVIEW', gap
    if gap is not None and gap < F(1, 100):
        return 'AMBIGUOUS_CLUSTERS', gap
    if groups[0][-1]['local']-groups[0][0]['local'] > F(1, 2):
        return 'BROAD_SCORE_REGION', gap
    return 'CANDIDATE_REQUIRES_VISUAL_REVIEW', gap


def parse_frames(log, paths, expected_base, origin, start, end):
    text = Path(log).read_text('utf-8', errors='replace')
    bases = set(re.findall(r'config in time_base:\s*(\d+/\d+)', text))
    if bases != {str(expected_base)}:
        # Fraction prints integral time bases as integers; normalize strings before comparison.
        if not bases or {F(b) for b in bases} != {expected_base}:
            raise ValueError('Cannot establish source filter time base')
    logged = [(int(n), int(pts)) for n, pts in re.findall(r'n:\s*(\d+)\s+pts:\s*(-?\d+)\s+pts_time:', text)]
    if len({n for n, _ in logged}) != len(logged):
        raise ValueError('Duplicate decoded frame ordinals')
    points = dict(logged)
    output = []
    previous = None
    for n, path in enumerate(paths):
        if n not in points:
            raise ValueError('Output frame has no decoded PTS')
        pts = points[n]
        local = pts * expected_base-origin
        if previous is not None and pts <= previous:
            raise ValueError('Duplicate/nonmonotonic decoded PTS')
        if not start <= local < end:
            raise ValueError('Decoded frame outside requested local interval')
        with Image.open(path) as image:
            image.verify()
        output.append({'pts': pts, 'local': local, 'path': Path(path)})
        previous = pts
    return output


def decode(ffmpeg, source, stream, base, origin, start, end, destination, budget, coarse):
    if not 0 <= start < end or end-start > 12:
        raise ValueError('Invalid bounded decode interval')
    if destination.exists():
        raise ValueError('Decode destination already exists')
    destination.mkdir()
    count, size = budget.check()
    cap = min(budget.frames-count+1, 52 if coarse else 180)
    if cap < 2:
        raise ValueError('Insufficient remaining frame budget')
    absolute_start, absolute_end = start+origin, end+origin
    expression = f'gte(t,{seconds(absolute_start)})*lt(t,{seconds(absolute_end)})'
    if coarse:
        expression += '*if(isnan(prev_selected_t),1,gte(t-prev_selected_t,0.25))'
    command = [ffmpeg, '-hide_banner', '-nostdin', '-n', '-loglevel', 'info', '-copyts',
               '-ss', seconds(start), '-t', seconds(end-start), '-i', str(source),
               '-map', f'0:{stream}', '-an', '-sn', '-dn', '-vf', f"select='{expression}',showinfo",
               '-fps_mode', 'passthrough', '-frames:v', str(cap), '-start_number', '0',
               str(destination / 'frame-%05d.png')]
    log = destination / 'decode.log'
    run_process(command, budget, log)
    paths = sorted(destination.glob('frame-*.png'))
    if len(paths) >= cap:
        raise ValueError('Decode hit sentinel frame cap; incomplete output refused')
    records = parse_frames(log, paths, base, origin, start, end)
    return records, [Path(ffmpeg).name, *command[1:]]


def packet_text(value):
    h, m, sec = value.split(':')
    return int(h)*3600+int(m)*60+F(sec)


def inspect_inputs(root, episode, selected, ffprobe, budget):
    coverage = read_json(root/'reference/indexes/performance-subtitle-coverage.json')
    episode_id = f'EP-{episode:02d}'
    entry = next(r for r in coverage['episodes'] if r['episode_id'] == episode_id)
    source = safe_path(root, entry['source'])
    source_before = signature(source)
    if not source.is_relative_to(root/'_source_episodes'):
        raise ValueError('Video outside immutable source directory')
    if source.stat().st_size != entry['source_bytes']:
        raise ValueError('Video size differs from indexed source')
    probe = json.loads(run_process([ffprobe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(source)], budget))
    videos = [r for r in probe['streams'] if r['codec_type'] == 'video']
    if len(videos) != 1:
        raise ValueError('Ambiguous video stream')
    video = videos[0]
    if F(video.get('sample_aspect_ratio', '1:1').replace(':','/')) != 1:
        raise ValueError('Non-square video pixels require explicit normalization support')
    if video['width']*video['height'] > 1920*1080:
        raise ValueError('Prototype picture dimensions exceed budgeted scope')
    if 'start_time' not in probe['format'] or 'duration' not in probe['format']:
        raise ValueError('Missing container time origin/duration')
    origin, duration, base = F(probe['format']['start_time']), F(probe['format']['duration']), F(video['time_base'])
    if origin != 0:
        raise ValueError('Nonzero container origin needs a separately validated seek policy; prototype refuses it')
    subtitle = safe_path(root, entry['local_subtitle'])
    if digest(subtitle) != entry['subtitle_sha256']:
        raise ValueError('Subtitle digest differs from registered copy')
    substream = next((s for s in probe['streams'] if s['index'] == entry['subtitle_stream']), None)
    if not substream or substream['codec_type'] != 'subtitle' or substream['codec_name'] != entry['subtitle_codec']:
        raise ValueError('Subtitle stream mismatch')
    # Establish only a bounded packet/cue comparison; never infer speaker/text verification.
    ass = [packet_text(line.split(',', 3)[1]) for line in subtitle.read_text('utf-8-sig').splitlines() if line.startswith('Dialogue:')]
    packets = json.loads(run_process([ffprobe, '-v', 'error', '-read_intervals', '0%+30', '-select_streams', str(entry['subtitle_stream']), '-show_packets', '-show_entries', 'packet=pts_time', '-of', 'json', str(source)], budget))
    times = [F(p['pts_time'])-origin for p in packets.get('packets', []) if 'pts_time' in p]
    comparison = min(3, len(times), len(ass))
    verified = comparison == 3 and all(abs(times[i]-ass[i]) <= F(1,1000) for i in range(3)) and origin == 0
    locator_path = root/f'reference/indexes/animehistory/CSVs/episode-{episode:02d}.csv'
    locators = read_csv(locator_path)
    cache = root/f'reference/cache/animehistory-review/{episode_id}'
    manifest = read_json(cache/'manifest.json')
    locator_hash = digest(locator_path)
    if manifest['csv_sha256'] != locator_hash:
        raise ValueError('Stale gallery manifest')
    images = []
    for image_id in selected:
        row = next((r for r in locators if r['image_id'] == image_id), None)
        if row is None or row['episode_id'] != episode_id:
            raise ValueError('Image outside episode locator baseline')
        item = manifest['images'].get(image_id)
        if not item or item['state'] != 'cached':
            raise ValueError('Selected image not cached; use gallery preparation separately')
        path = safe_path(cache, item['file'])
        if digest(path) != item['sha256']:
            raise ValueError('Gallery image digest mismatch')
        images.append({'image_id': image_id, 'web_seconds': int(row['web_seconds']), 'path': path, 'image_sha256': item['sha256']})
    identity = dict(episode_id=episode_id, video_source=entry['source'], video_sha256=digest(source, budget),
                    video_stream_index=video['index'], video_time_base=ratio(base), media_origin_seconds=ratio(origin),
                    subtitle_stream_index=entry['subtitle_stream'], subtitle_sha256=entry['subtitle_sha256'],
                    subtitle_time_basis='MEDIA_RELATIVE' if verified else 'UNVERIFIED',
                    subtitle_shift_seconds='0/1' if verified else '', locator_sha256=locator_hash)
    if signature(source) != source_before:
        raise ValueError('Source changed during input inspection')
    return source, images, identity, probe, {'compared_cues': comparison, 'packet_seconds': [ratio(t) for t in times[:3]], 'ass_seconds': [ratio(t) for t in ass[:3]], 'scope': 'first three cues in bounded probe; not whole-track dialogue verification'}, duration


def comparison_sheet(gallery, records, groups, destination, label, rectangles):
    canvas = Image.new('RGB', (1500, 1350), '#17202b')
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)
    except OSError:
        font = ImageFont.load_default(size=20)
    def tile(path, x, y, width, height, caption):
        with Image.open(path) as image:
            image.thumbnail((width, height))
            canvas.paste(image.convert('RGB'), (x+(width-image.width)//2, y))
        draw.text((x+5, y+height+4), caption, fill='white', font=font)
    draw.text((15,10), f'{label} | CANDIDATES ONLY | 320x240 greyscale scoring; masks {rectangles}', fill='white', font=font)
    tile(gallery, 0,45,750,500,'Gallery reference')
    if groups:
        best = max(groups[0], key=lambda r: (r['score'], -r['local']))
        tile(best['path'],750,45,750,500,f"Best: local {float(best['local']):.3f}s | PTS {best['pts']}")
        for index, group in enumerate(groups[:3]):
            record = max(group, key=lambda r: (r['score'], -r['local']))
            tile(record['path'],index*500,590,500,300,f"Cluster {index+1}: {float(record['local']):.3f}s score {float(record['score']):.5f}")
        ordered = sorted(records, key=lambda r:r['local'])
        i = ordered.index(best)
        for index, record in enumerate(ordered[max(0,i-1):i+2]):
            tile(record['path'],index*500,965,500,300,f"Decoded neighbor: {float(record['local']):.3f}s PTS {record['pts']}")
    canvas.save(destination)


def search(root, episode, selected, ffmpeg, ffprobe, rectangles, pilot_stage=2):
    root = Path(root).absolute()
    if not 1 <= episode <= 26 or not 1 <= len(selected) <= 5 or len(set(selected)) != len(selected):
        raise ValueError('Select one episode and 1-5 unique image IDs')
    allowed = PROTOTYPE if pilot_stage==2 else set(STAGE3_ROLES) if pilot_stage==3 else set()
    if episode != 1 or not set(selected) <= allowed:
        raise ValueError('Selection outside the declared Episode 1 pilot stage')
    mask, retained = masks_checked(rectangles)
    base = safe_path(root, f'reference/working/alignment/EP-{episode:02d}')
    with writer(base):
        run_id = 'ALNRUN-'+uuid.uuid4().hex
        stage = safe_path(base, run_id)
        stage.mkdir()
        budget = Budget(stage)
        started = time.monotonic()
        manifest = {'owner': VERSION, 'run_id': run_id, 'pilot_stage':pilot_stage, 'declared_roles':{i:STAGE3_ROLES[i] if pilot_stage==3 else 'LEAD' for i in selected}, 'created_utc': datetime.now(timezone.utc).isoformat(), 'status': 'RUNNING', 'results': []}
        tracked = []
        try:
            source, images, identity, probe, subtitle_check, duration = inspect_inputs(root, episode, selected, ffprobe, budget)
            tracked = [(source, signature(source))] + [(r['path'], signature(r['path'])) for r in images]
            # Pin smaller inputs again after inspection to detect changes during decoding too.
            small_inputs = [root/f'reference/indexes/animehistory/CSVs/episode-{episode:02d}.csv',
                            root/f'reference/cache/animehistory-review/EP-{episode:02d}/manifest.json',
                            root/'reference/indexes/performance-subtitle-coverage.json']
            coverage = read_json(small_inputs[-1])
            entry = next(r for r in coverage['episodes'] if r['episode_id']==f'EP-{episode:02d}')
            small_inputs.append(safe_path(root,entry['local_subtitle']))
            small_hashes = [(p,digest(p)) for p in small_inputs]
            if small_hashes[0][1] != identity['locator_sha256'] or small_hashes[-1][1] != identity['subtitle_sha256']:
                raise ValueError('Inputs changed after inspection')
            versions = {name:run_process([exe,'-version'],budget).decode('utf-8',errors='replace').splitlines()[0] for name,exe in [('ffmpeg',ffmpeg),('ffprobe',ffprobe)]}
            manifest.update(identity=identity, input_id=input_id(identity), probe=probe, subtitle_check=subtitle_check,
                            recipe={'version': VERSION, 'implementation_sha256': digest(Path(__file__)), 'python':sys.version.split()[0], 'pillow':PILLOW_VERSION, 'tools': versions, 'size': [320,240], 'masks':rectangles, 'retained_pixels':retained, 'score':'1-MAE/255', 'coarse_interval':'1/4', 'cluster_gap_seconds':'1/2', 'cluster_score_band':'1/100', 'refinement_windows':2, 'refinement_width':'1/1', 'caps':{'frames':MAX_FRAMES,'bytes':MAX_BYTES,'seconds':MAX_SECONDS}, 'commands':[]})
            atomic(stage/'run.json',encode(manifest))
            base_time, origin = F(identity['video_time_base']), F(identity['media_origin_seconds'])
            total_windows = F(0)
            for image in images:
                target, aspect = normalized(image['path'])
                center = F(image['web_seconds']-2 if image['image_id'] in {'846774','846776'} else image['web_seconds'])
                start, end = max(F(0),center-6), min(duration,center+6)
                folder = stage/image['image_id']; folder.mkdir()
                records, command = decode(ffmpeg,source,identity['video_stream_index'],base_time,origin,start,end,folder/'coarse',budget,True)
                total_windows += end-start
                def rank(values):
                    for record in values:
                        normalized_frame,_ = normalized(record['path'],aspect)
                        record['score'] = score(target,normalized_frame,mask,retained)
                def remember(command):
                    manifest['recipe']['commands'].append([identity['video_source'] if v==str(source) else str(Path(v).relative_to(root)).replace('\\','/') if str(v).startswith(str(root)) else v for v in command])
                remember(command); rank(records)
                coarse_groups = clusters(records)
                for number, group in enumerate(coarse_groups[:2]):
                    top=max(group,key=lambda r:(r['score'],-r['local']))
                    fine_start, fine_end = max(start,top['local']-F(1,2)),min(end,top['local']+F(1,2))
                    refined,command=decode(ffmpeg,source,identity['video_stream_index'],base_time,origin,fine_start,fine_end,folder/f'fine-{number}',budget,False)
                    total_windows += fine_end-fine_start
                    remember(command); rank(refined)
                    by_pts={r['pts']:r for r in records}
                    for record in refined:
                        if record['pts'] in by_pts and digest(record['path']) != digest(by_pts[record['pts']]['path']):
                            raise ValueError('Same PTS decoded inconsistently')
                        by_pts[record['pts']]=record
                    records=sorted(by_pts.values(),key=lambda r:r['local'])
                if total_windows>70:
                    raise ValueError('Media-window coverage budget exceeded')
                groups=clusters(records); state,gap=candidate_state(groups)
                comparison_sheet(image['path'],records,groups,folder/'comparison.png',image['image_id'],rectangles)
                output=[]
                for record in records:
                    output.append(dict(pts=record['pts'],local_seconds=ratio(record['local']),score=ratio(record['score']),image=record['path'].relative_to(stage).as_posix(),sha256=digest(record['path'])))
                group_data=[]
                for group in groups[:3]:
                    top=max(group,key=lambda r:(r['score'],-r['local']))
                    group_data.append(dict(start=ratio(group[0]['local']),end=ratio(group[-1]['local']),best_pts=top['pts'],best_local=ratio(top['local']),score=ratio(top['score'])))
                result=dict(image_id=image['image_id'],web_seconds=image['web_seconds'],image_sha256=image['image_sha256'],search_start=ratio(start),search_end=ratio(end),role=manifest['declared_roles'][image['image_id']],status='CANDIDATE',diagnostic=state,runner_up_gap=ratio(gap) if gap is not None else None,clusters=group_data,frames=output)
                manifest['results'].append(result)
                atomic(stage/'run.json',encode(manifest)); budget.check()
                print(json.dumps({'image_id':image['image_id'],'diagnostic':state,'top':group_data[:1]}),flush=True)
            if any(signature(path)!=before for path,before in tracked):
                raise ValueError('Input changed during candidate search')
            if any(digest(path)!=before for path,before in small_hashes):
                raise ValueError('Metadata/subtitle changed during candidate search')
            manifest.update(status='COMPLETE_CANDIDATES',window_seconds=ratio(total_windows),elapsed_seconds=round(time.monotonic()-started,3),resources=dict(zip(['frames','bytes'],budget.check())))
            atomic(stage/'run.json',encode(manifest))
            budget.check()
            return stage
        except BaseException as exc:
            manifest.update(status='FAILED',diagnostic=f'{type(exc).__name__}: {exc}')
            atomic(stage/'run.json',encode(manifest))
            raise


def cleanup(root, run_id, episode):
    if not re.fullmatch(r'ALNRUN-[a-f0-9]{32}',run_id) or not 1<=episode<=26:
        raise ValueError('Invalid explicit run identity')
    base=safe_path(root,f'reference/working/alignment/EP-{episode:02d}')
    with writer(base):
        path=safe_path(base,run_id)
        manifest=read_json(path/'run.json')
        if manifest.get('owner')!=VERSION or manifest.get('run_id')!=run_id:
            raise ValueError('Unowned run')
        for item in path.rglob('*'):
            safe_path(path,item.relative_to(path))
        shutil.rmtree(path)
        if path.exists():raise ValueError('Run cleanup incomplete')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    sub=commands.add_parser('search')
    sub.add_argument('--episode',type=int,required=True)
    sub.add_argument('--image-id',action='append',required=True)
    sub.add_argument('--pilot-stage',type=int,choices=(2,3),default=2)
    sub.add_argument('--ffmpeg',default=shutil.which('ffmpeg'))
    sub.add_argument('--ffprobe',default=shutil.which('ffprobe'))
    sub.add_argument('--mask',action='append',default=[],help='Explicit normalized rectangle x0,y0,x1,y1; maximum 30 percent union')
    sub=commands.add_parser('cleanup');sub.add_argument('--episode',type=int,required=True);sub.add_argument('--run-id',required=True)
    args=parser.parse_args()
    try:
        if args.command=='search':
            if not args.ffmpeg or not args.ffprobe:raise ValueError('Locate installed FFmpeg/FFprobe explicitly; no automatic installation')
            path=search(ROOT,args.episode,args.image_id,args.ffmpeg,args.ffprobe,[list(map(int,box.split(','))) for box in args.mask],args.pilot_stage)
            print(json.dumps({'run':str(path),'status':'COMPLETE_CANDIDATES','authored_tables_changed':False}))
        else:
            cleanup(ROOT,args.run_id,args.episode);print(json.dumps({'removed_run':args.run_id}))
    except (ValueError,OSError,KeyError,StopIteration,subprocess.SubprocessError) as exc:
        print(json.dumps({'error':str(exc)}),file=sys.stderr);return 1
    return 0


if __name__=='__main__':sys.exit(main())
