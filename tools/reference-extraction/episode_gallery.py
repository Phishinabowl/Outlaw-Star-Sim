"""Bounded AnimeHistory cache/contact sheets and verified RAR recovery. No video decoding.

Generated media and recovery state stay in ignored directories. Commands do not mark
images visually reviewed or create the future authored category index.
"""
import argparse
from contextlib import contextmanager
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import time
import uuid
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener
from urllib.robotparser import RobotFileParser

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[2]
OWNER = 'animehistory-review-v1'
AGENT = 'OutlawStarReferenceReview/1.0 (paced episode image research)'
HOSTS = {'animehistory.org', 'www.animehistory.org'}
MAX_IMAGE = 20 * 1024 * 1024


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_path(path, base):
    """Validate lexical/resolved containment and reject Windows junctions/symlinks."""
    path, base = Path(path).absolute(), Path(base).absolute()
    if path == base or not path.is_relative_to(base):
        raise ValueError(f'Expected child of {base}: {path}')
    for part in (path, *path.parents):
        if part.exists() or part.is_symlink():
            attrs = part.lstat()
            if stat.S_ISLNK(attrs.st_mode) or getattr(attrs, 'st_file_attributes', 0) & 0x400:
                raise ValueError(f'Reparse point/link refused: {part}')
        if part == base:
            break
    if not path.resolve().is_relative_to(base.resolve()):
        raise ValueError(f'Resolved path escapes {base}: {path}')
    return path


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        temporary.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def image_info(data):
    if not data or len(data) > MAX_IMAGE:
        raise ValueError('Empty or oversized image')
    with Image.open(io.BytesIO(data)) as image:
        if image.format not in ('JPEG', 'PNG'):
            raise ValueError(f'Unexpected image format: {image.format}')
        image.verify()
    with Image.open(io.BytesIO(data)) as image:
        image.load()
        width, height = image.size
    return {'bytes': len(data), 'sha256': digest(data), 'width': width, 'height': height}


def allowed_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in HOSTS or parsed.port not in (None, 443):
        raise ValueError(f'Unexpected URL: {url}')
    if parsed.username or parsed.password:
        raise ValueError('URL credentials refused')
    return url


class RestrictedRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        allowed_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class Downloader:
    def __init__(self, interval=1.0):
        self.interval = max(1.0, interval)
        self.last = 0
        self.opener = build_opener(RestrictedRedirect())
        self.robots = None

    def fetch(self, url, maximum):
        allowed_url(url)
        time.sleep(max(0, self.interval - (time.monotonic() - self.last)))
        self.last = time.monotonic()
        with self.opener.open(Request(url, headers={'User-Agent': AGENT}), timeout=30) as response:
            allowed_url(response.url)
            data = response.read(maximum + 1)
            if len(data) > maximum:
                raise ValueError('Response exceeds size limit')
            return data, response.headers.get_content_type(), response.url

    def load_robots(self):
        data, kind, _ = self.fetch('https://animehistory.org/robots.txt', 1024 * 1024)
        if kind not in ('text/plain', 'text/html'):
            raise ValueError('Unexpected robots response')
        self.robots = RobotFileParser()
        self.robots.parse(data.decode('utf-8').splitlines())
        delay = self.robots.crawl_delay(AGENT) or self.robots.crawl_delay('*')
        if delay:
            self.interval = max(self.interval, delay)

    def image(self, url):
        if self.robots is None:
            self.load_robots()
        if not self.robots.can_fetch(AGENT, url):
            raise PermissionError(f'Robots guidance disallows {url}')
        for attempt in range(3):
            try:
                data, kind, final = self.fetch(url, MAX_IMAGE)
                if kind not in ('image/jpeg', 'image/png'):
                    raise ValueError(f'Unexpected response type: {kind}')
                image_info(data)
                return data, final
            except HTTPError as error:
                if error.code in (401, 403, 429) or error.code < 500:
                    raise
                if attempt == 2:
                    raise
            except (URLError, TimeoutError):
                if attempt == 2:
                    raise
            time.sleep(2 ** attempt)


class Gallery:
    def __init__(self, episode, root=ROOT):
        if not 1 <= episode <= 26:
            raise ValueError('Episode must be 1–26')
        self.root = Path(root).absolute()
        self.episode = episode
        self.id = f'EP-{episode:02}'
        self.cache_base = checked_path(self.root / 'reference/cache/animehistory-review', self.root)
        self.folder = checked_path(self.cache_base / self.id, self.cache_base)
        self.manifest_path = checked_path(self.folder / 'manifest.json', self.folder)
        self.sheet_base = checked_path(self.root / 'reference/contact-sheets/animehistory-review', self.root)
        self.sheets = checked_path(self.sheet_base / self.id, self.sheet_base)
        self.archives = checked_path(self.cache_base / 'archives', self.cache_base)
        self.archive_path = checked_path(self.archives / f'{self.id}.rar', self.archives)
        self.receipt_path = checked_path(self.archives / f'{self.id}.json', self.archives)
        csv_path = checked_path(self.root / f'reference/indexes/animehistory/CSVs/episode-{episode:02}.csv', self.root)
        raw = csv_path.read_bytes()
        self.csv_hash = digest(raw)
        self.rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
        if not self.rows or len({r['image_id'] for r in self.rows}) != len(self.rows):
            raise ValueError('Empty locator list or duplicate IDs')
        times = []
        for row in self.rows:
            if row['episode_id'] != self.id or not re.fullmatch(r'\d+', row['image_id']):
                raise ValueError('Locator identity mismatch')
            allowed_url(row['image_url'])
            if not urlparse(row['image_url']).path.startswith('/uploads/screencaps/'):
                raise ValueError('Unexpected image URL path')
            times.append(int(row['web_seconds']))
        if times != sorted(times):
            raise ValueError('Locator timestamps are not chronological')
        self.by_id = {r['image_id']: r for r in self.rows}

    def new_manifest(self):
        return {'owner': OWNER, 'episode': self.id, 'csv_sha256': self.csv_hash,
                'expected': len(self.rows), 'updated_utc': now(), 'images': {}}

    def load(self, required=True):
        if not self.manifest_path.exists():
            if self.folder.exists() and any(self.folder.iterdir()):
                raise ValueError('Unowned/nonempty episode cache without manifest')
            if required:
                raise ValueError('No unpacked cache; prepare or restore first')
            return self.new_manifest()
        manifest = json.loads(self.manifest_path.read_text(encoding='utf-8'))
        self.validate_manifest(manifest)
        return manifest

    def validate_manifest(self, manifest):
        if (manifest.get('owner'), manifest.get('episode'), manifest.get('csv_sha256'), manifest.get('expected')) != (OWNER, self.id, self.csv_hash, len(self.rows)):
            raise ValueError('Manifest ownership/locator version mismatch')
        for image_id, record in manifest['images'].items():
            if image_id not in self.by_id or record['image_url'] != self.by_id[image_id]['image_url']:
                raise ValueError('Manifest image identity mismatch')
            if record['state'] not in ('cached', 'failed'):
                raise ValueError('Unexpected cache state')
            if record['state'] == 'cached' and record['file'] != f'images/{image_id}.jpg':
                raise ValueError('Unexpected cache filename')

    def save(self, manifest):
        checked_path(self.manifest_path, self.root)
        manifest['updated_utc'] = now()
        write_json(self.manifest_path, manifest)

    def selection(self, start=1, limit=None):
        if start < 1 or start > len(self.rows) or (limit is not None and limit < 1):
            raise ValueError('Invalid start/limit')
        return self.rows[start-1:None if limit is None else start-1+limit]

    def validate_cache(self, folder, manifest, extra_files=()):
        self.validate_manifest(manifest)
        expected = {'manifest.json', *extra_files}
        for image_id, record in manifest['images'].items():
            if record['state'] != 'cached':
                continue
            target = checked_path(folder / record['file'], folder)
            data = target.read_bytes()
            info = image_info(data)
            if any(info[k] != record[k] for k in info):
                raise ValueError(f'Cached image changed: {image_id}')
            expected.add(record['file'])
        actual = set()
        for target in folder.rglob('*'):
            checked_path(target, folder)
            if target.is_file():
                actual.add(target.relative_to(folder).as_posix())
        if actual != expected:
            raise ValueError(f'Unexpected/missing cache files: {actual ^ expected}')
        return expected

    def prepare(self, start=1, limit=None, offline=False, downloader=None):
        manifest = self.load(required=False)
        self.save(manifest)
        # Recover only our known interrupted-transfer filename; no original image is replaced.
        for row in self.selection(start, limit):
            image_id = row['image_id']
            target = checked_path(self.folder / f'images/{image_id}.jpg', self.folder)
            temporary = checked_path(target.with_suffix('.jpg.part'), self.folder)
            record = manifest['images'].get(image_id)
            if record and record['state'] == 'cached':
                if not target.exists() and temporary.exists():
                    info = image_info(temporary.read_bytes())
                    if any(info[k] != record[k] for k in info):
                        raise ValueError('Interrupted transfer hash mismatch')
                    temporary.replace(target)
                info = image_info(target.read_bytes())
                if any(info[k] != record[k] for k in info):
                    raise ValueError(f'Cached image changed: {image_id}')
                temporary.unlink(missing_ok=True)
                continue
            temporary.unlink(missing_ok=True)
            if target.exists():
                raise ValueError(f'Unregistered image refused: {target}')
            if offline:
                continue
            try:
                if downloader is None:
                    downloader = Downloader()
                data, final_url = downloader.image(row['image_url'])
                info = image_info(data)
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary.write_bytes(data)
                # Persist the hash before promotion so an interrupted rename is recoverable.
                record = {**row, **info, 'state': 'cached', 'file': f'images/{image_id}.jpg',
                          'retrieved_utc': now(), 'final_url': final_url}
                manifest['images'][image_id] = record
                self.save(manifest)
                temporary.replace(target)
                print(f'{self.id} cached {image_id}', flush=True)
            except Exception as error:
                if not target.exists():
                    manifest['images'][image_id] = {**row, 'state': 'failed', 'error': str(error), 'attempted_utc': now()}
                    self.save(manifest)
                raise
            finally:
                if target.exists() or manifest['images'].get(image_id, {}).get('state') != 'cached':
                    temporary.unlink(missing_ok=True)
        return self.make_sheets(start, limit)

    def sheet_registry(self):
        target = checked_path(self.sheets / 'sheets.json', self.sheets)
        if target.exists():
            registry = json.loads(target.read_text(encoding='utf-8'))
            if (registry.get('owner'), registry.get('episode'), registry.get('csv_sha256')) != (OWNER, self.id, self.csv_hash):
                raise ValueError('Contact-sheet ownership mismatch')
            return registry
        if self.sheets.exists() and any(self.sheets.iterdir()):
            raise ValueError('Nonempty unowned contact-sheet directory')
        return {'owner': OWNER, 'episode': self.id, 'csv_sha256': self.csv_hash, 'sheets': {}}

    def make_sheets(self, start=1, limit=None):
        manifest = self.load()
        self.validate_cache(self.folder, manifest)
        registry = self.sheet_registry()
        selected = self.selection(start, limit)
        try:
            font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18)
        except OSError:
            font = ImageFont.load_default(size=18)
        made = []
        for offset in range(0, len(selected), 24):
            rows = selected[offset:offset+24]
            first, last = start+offset, start+offset+len(rows)-1
            name = f'sheet-{first:04}-{last:04}.png'
            target = checked_path(self.sheets / name, self.sheets)
            canvas = Image.new('RGB', (1600, 6*336+40), '#171b22')
            draw = ImageDraw.Draw(canvas)
            draw.text((12, 8), f'{self.id} | locators {first}–{last} | CATEGORY SCREENING ONLY | web times unaligned', font=font, fill='white')
            identities = []
            for index, row in enumerate(rows):
                x, y = index % 4 * 400, index // 4 * 336 + 40
                record = manifest['images'].get(row['image_id'], {})
                if record.get('state') == 'cached':
                    with Image.open(self.folder / record['file']) as original:
                        thumb = ImageOps.contain(original.convert('RGB'), (392, 294))
                        canvas.paste(thumb, (x+4+(392-thumb.width)//2, y+(294-thumb.height)//2))
                else:
                    draw.text((x+12, y+125), 'UNAVAILABLE / NOT CACHED', font=font, fill='#ffad66')
                draw.text((x+8, y+300), f'{first+index:03} | {row["image_id"]} | {row["web_timestamp"]}', font=font, fill='white')
                identities.append({'image_id': row['image_id'], 'web_timestamp': row['web_timestamp'], 'image_sha256': record.get('sha256')})
            buffer = io.BytesIO()
            canvas.save(buffer, format='PNG')
            data = buffer.getvalue()
            if target.exists():
                previous = registry['sheets'].get(name)
                if not previous or digest(target.read_bytes()) != previous['sha256']:
                    raise ValueError('Changed/unregistered contact sheet refused')
            self.sheets.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            registry['sheets'][name] = {'sha256': digest(data), 'locators': identities}
            write_json(self.sheets / 'sheets.json', registry)
            made.append(str(target))
        return {'episode': self.id, 'sheets': made}

    def cleanup(self, progress_saved=False):
        if not progress_saved:
            raise ValueError('Cleanup requires --progress-saved acknowledgement; annotations are never inferred')
        registry = self.sheet_registry()
        if not self.sheets.exists():
            return {'removed_sheets': 0}
        expected = {'sheets.json', *registry['sheets']}
        actual = set()
        for target in self.sheets.iterdir():
            checked_path(target, self.sheets)
            if not target.is_file():
                raise ValueError('Unexpected contact-sheet directory entry')
            actual.add(target.name)
        if actual != expected:
            raise ValueError('Unregistered contact-sheet files; cleanup refused')
        for name, item in registry['sheets'].items():
            target = checked_path(self.sheets / name, self.sheets)
            if digest(target.read_bytes()) != item['sha256']:
                raise ValueError('Changed contact sheet; cleanup refused')
        for name in expected:
            checked_path(self.sheets / name, self.sheets).unlink()
        self.sheets.rmdir()
        return {'removed_sheets': len(registry['sheets'])}

    def status(self):
        manifest = self.load(required=False)
        cached = sum(r['state'] == 'cached' for r in manifest['images'].values())
        failed = sum(r['state'] == 'failed' for r in manifest['images'].values())
        if self.manifest_path.exists():
            self.validate_cache(self.folder, manifest)
        receipt = json.loads(self.receipt_path.read_text()) if self.receipt_path.exists() else None
        archive_valid = bool(receipt and self.archive_path.exists() and receipt['archive_sha256'] == digest(self.archive_path.read_bytes()))
        review = {'category_screened': None, 'initial_review_complete': None, 'detail_reviewed': None,
                  'review_status_note': 'No authored category index available.'}
        category_path = self.root / 'reference/indexes/animehistory/category-index.csv'
        if category_path.exists():
            import category_index
            fields, annotations = category_index.read_csv(category_path)
            if fields != category_index.FIELDS:
                raise ValueError('Category index header mismatch')
            _, sources = category_index.read_csv(self.root / 'reference/indexes/animehistory/all-episodes.csv')
            category_index.validate(annotations, sources)
            selected = [r for r in annotations if r['episode_id'] == self.id]
            review = {'category_screened': sum(r['screening_status'] == 'SCREENED' for r in selected),
                      'category_needs_recheck': sum(r['screening_status'] == 'NEEDS_RECHECK' for r in selected),
                      'category_unavailable': sum(r['screening_status'] == 'UNAVAILABLE' for r in selected),
                      'category_unreviewed': sum(r['screening_status'] == 'UNREVIEWED' for r in selected),
                      'initial_review_complete': sum(r['detail_status'] == 'INITIAL_REVIEW_COMPLETE' for r in selected),
                      'detail_reviewed': sum(r['detail_status'] == 'REVIEWED' for r in selected),
                      'detail_partial': sum(r['detail_status'] == 'PARTIAL' for r in selected),
                      'review_status_note': 'Counts from validated authored annotations; cache does not imply review.'}
        return {'episode': self.id, 'expected': len(self.rows), 'cached': cached,
                'failed': failed, 'not_cached': len(self.rows)-cached-failed,
                **review,
                'contact_sheets': len(self.sheet_registry()['sheets']),
                'archive_hash_valid': archive_valid, 'archived_images': receipt['cached'] if archive_valid else 0,
                'archive_bytes': self.archive_path.stat().st_size if self.archive_path.exists() else 0,
                'archived_supplements': receipt.get('supplements', 0) if archive_valid else 0,
                'unpacked_bytes': sum(p.stat().st_size for p in self.folder.rglob('*') if p.is_file()) if self.folder.exists() else 0}


def rar_path():
    candidates = [shutil.which('rar'), Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'WinRAR/Rar.exe']
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(candidate)
    raise ValueError('RAR command-line executable unavailable; install/setup is not automatic')


def rar(executable, args, cwd=None):
    result = subprocess.run([executable, *args], cwd=cwd, capture_output=True, timeout=300)
    if result.returncode:
        raise ValueError(f'RAR failed ({result.returncode}): {result.stderr[-2000:]!r} {result.stdout[-2000:]!r}')
    return result.stdout


def member_name(name):
    name = name.replace('\\', '/')
    path = PurePosixPath(name)
    if path.is_absolute() or any(p in ('..', '.') or ':' in p for p in path.parts) or not name:
        raise ValueError(f'Unsafe archive member: {name}')
    if not (name in ('manifest.json', 'supplements.json') or re.fullmatch(r'images/\d+\.jpg', name)
            or re.fullmatch(r'supplements/EP-\d{2}-MAN-\d{3}\.png', name)):
        raise ValueError(f'Unexpected archive member: {name}')
    return name


def empty_supplements(gallery):
    return {'owner': OWNER, 'format_version': 1, 'episode': gallery.id, 'records': []}


def validate_supplement_snapshot(gallery, snapshot):
    """Recovery metadata has a fixed episode-owned path contract, independent of review enums."""
    if (snapshot.get('owner'), snapshot.get('format_version'), snapshot.get('episode')) != (OWNER, 1, gallery.id):
        raise ValueError('Supplement archive ownership/version mismatch')
    records = snapshot.get('records')
    if not isinstance(records, list) or len(records) > 1000:
        raise ValueError('Invalid supplemental archive inventory')
    seen = set()
    for item in records:
        identity = item.get('image_id', '')
        if not re.fullmatch(re.escape(gallery.id) + r'-MAN-\d{3}', identity) or identity in seen:
            raise ValueError('Invalid/duplicate supplemental archive identity')
        seen.add(identity)
        if (item.get('file') != f'supplements/{identity}.png'
                or item.get('media_path') != f'reference/working/manual-supplements/{gallery.id}/{identity}.png'
                or not re.fullmatch('[0-9a-f]{64}', item.get('sha256', ''))
                or type(item.get('bytes')) is not int or not 0 < item['bytes'] <= MAX_IMAGE):
            raise ValueError('Invalid supplemental archive path/hash/size')
    return snapshot


def current_supplements(gallery, require_media=True):
    """Read only the selected episode's authored media records; never modify review CSVs."""
    import category_index
    index = checked_path(gallery.root / 'reference/indexes/animehistory/supplemental-index.csv', gallery.root)
    snapshot = empty_supplements(gallery)
    if not index.exists():
        return snapshot
    fields, rows = category_index.read_csv(index)
    if fields != category_index.SUPPLEMENT_FIELDS:
        raise ValueError('Supplemental index header mismatch')
    selected = [r for r in rows if r['episode_id'] == gallery.id]
    category_index.validate_supplements(selected, gallery.rows)
    for row in sorted(selected, key=lambda r: r['image_id']):
        target = checked_path(gallery.root / row['media_path'], gallery.root)
        info = {'sha256': row['media_sha256'], 'bytes': int(row['media_bytes'])}
        if target.exists() or require_media:
            actual = image_info(target.read_bytes())
            if actual['sha256'] != info['sha256'] or actual['bytes'] != info['bytes']:
                raise ValueError(f'Supplement differs from authored hash: {row["image_id"]}')
        snapshot['records'].append(dict(image_id=row['image_id'], file=f'supplements/{row["image_id"]}.png',
            media_path=row['media_path'], sha256=info['sha256'], bytes=info['bytes'],
            local_timestamp=row['local_timestamp'], local_seconds=row['local_seconds'],
            timestamp_basis=row['timestamp_basis'], alignment_status=row['alignment_status'],
            related_gallery_ids=row['related_gallery_ids'], source_description=row['source_description']))
    return validate_supplement_snapshot(gallery, snapshot)


def staged_supplements(gallery, folder):
    path = checked_path(folder / 'supplements.json', folder)
    return validate_supplement_snapshot(gallery, json.loads(path.read_text(encoding='utf-8'))) if path.exists() else empty_supplements(gallery)


def unpack_verified(gallery, archive, destination, executable):
    """Stream validated members to explicit files; never trust archive extraction paths."""
    output = rar(executable, ['lb', '-cfg-', '-p-', '-scf', str(archive)])
    names = [member_name(line) for line in output.decode('utf-8-sig').splitlines() if line]
    if len(names) != len(set(names)) or 'manifest.json' not in names:
        raise ValueError('Missing/duplicate archive manifest or member')
    raw = rar(executable, ['p', '-inul', '-cfg-', '-p-', str(archive), 'manifest.json'])
    if len(raw) > 2*1024*1024:
        raise ValueError('Oversized manifest')
    manifest = json.loads(raw)
    gallery.validate_manifest(manifest)
    supplement_raw = None
    snapshot = empty_supplements(gallery)
    if 'supplements.json' in names:
        supplement_raw = rar(executable, ['p', '-inul', '-cfg-', '-p-', str(archive), 'supplements.json'])
        if len(supplement_raw) > 2*1024*1024:
            raise ValueError('Oversized supplemental manifest')
        snapshot = validate_supplement_snapshot(gallery, json.loads(supplement_raw))
    extra_files = {r['file'] for r in snapshot['records']}
    if supplement_raw is not None:
        extra_files.add('supplements.json')
    expected = {'manifest.json', *extra_files, *(r['file'] for r in manifest['images'].values() if r['state'] == 'cached')}
    if set(names) != expected:
        raise ValueError('Archive inventory differs from manifest')
    destination.mkdir(parents=True, exist_ok=False)
    (destination / 'manifest.json').write_bytes(raw)
    if supplement_raw is not None:
        (destination / 'supplements.json').write_bytes(supplement_raw)
    supplement_by_file = {r['file']: r for r in snapshot['records']}
    for name in sorted(expected - {'manifest.json', 'supplements.json'}):
        target = checked_path(destination / name, destination)
        argument = name.replace('/', '\\') if os.name == 'nt' else name
        data = rar(executable, ['p', '-inul', '-cfg-', '-p-', str(archive), argument])
        info = image_info(data)
        if name in supplement_by_file:
            item = supplement_by_file[name]
            if info['sha256'] != item['sha256'] or info['bytes'] != item['bytes']:
                raise ValueError(f'Archived supplement hash/size mismatch: {name}')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    gallery.validate_cache(destination, manifest, extra_files)
    return manifest


def restore_supplements(gallery, staging):
    """Preflight every destination, then recover only missing original PNGs. Never edit indexes."""
    snapshot = staged_supplements(gallery, staging)
    pending = []
    for item in snapshot['records']:
        target = checked_path(gallery.root / item['media_path'], gallery.root)
        if target.exists():
            data = target.read_bytes()
            if digest(data) != item['sha256'] or len(data) != item['bytes']:
                raise ValueError(f'Conflicting supplemental restore destination: {target}')
        else:
            pending.append((target, checked_path(staging / item['file'], staging)))
    for target, source in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive create protects against changes after preflight. Source was hash-verified.
        with target.open('xb') as output:
            output.write(source.read_bytes())
    for item in snapshot['records']:
        checked_path(staging / item['file'], staging).unlink()
    extras = checked_path(staging / 'supplements', staging)
    if extras.exists():
        extras.rmdir()
    checked_path(staging / 'supplements.json', staging).unlink(missing_ok=True)
    return len(pending)


def remove_owned(folder, base):
    """Validate every member before recursive deletion of a tool-created staging/cache dir."""
    checked_path(folder, base)
    for child in folder.rglob('*'):
        checked_path(child, folder)
    shutil.rmtree(folder)


@contextmanager
def episode_lock(gallery):
    """OS lock is released on process exit; a leftover file is not a stale lock."""
    gallery.cache_base.mkdir(parents=True, exist_ok=True)
    lock_path = checked_path(gallery.cache_base / f'.{gallery.id}.lock', gallery.cache_base)
    with lock_path.open('a+b') as handle:
        handle.seek(0, 2)
        if not handle.tell():
            handle.write(b'0')
            handle.flush()
        handle.seek(0)
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == 'nt':
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)


def archive(gallery, compression=3, allow_partial=False, replace=False):
    manifest = gallery.load()
    members = gallery.validate_cache(gallery.folder, manifest)
    cached = sum(r['state'] == 'cached' for r in manifest['images'].values())
    if not cached or (cached != len(gallery.rows) and not allow_partial):
        raise ValueError('Incomplete cache; --allow-partial is required for a trial archive')
    executable = rar_path()
    if gallery.archive_path.exists():
        read_receipt(gallery)
        if not replace:
            raise ValueError('Verified archive exists; use --replace-archive to replace it after a new verified round trip')
    gallery.archives.mkdir(parents=True, exist_ok=True)
    candidate = checked_path(gallery.archives / f'{gallery.id}-{uuid.uuid4().hex}.candidate.rar', gallery.archives)
    staging = checked_path(gallery.cache_base / f'verify-{uuid.uuid4().hex}', gallery.cache_base)
    packing = checked_path(gallery.cache_base / f'pack-{uuid.uuid4().hex}', gallery.cache_base)
    supplements = current_supplements(gallery)
    started = time.monotonic()
    try:
        packing.mkdir(parents=True, exist_ok=False)
        for name in members:
            target = checked_path(packing / name, packing)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(checked_path(gallery.folder / name, gallery.folder), target)
        extra_files = {'supplements.json'}
        write_json(packing / 'supplements.json', supplements)
        for item in supplements['records']:
            target = checked_path(packing / item['file'], packing)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(checked_path(gallery.root / item['media_path'], gallery.root), target)
            info = image_info(target.read_bytes())
            if info['sha256'] != item['sha256'] or info['bytes'] != item['bytes']:
                raise ValueError('Supplement changed during archive preparation')
            extra_files.add(item['file'])
        gallery.validate_cache(packing, manifest, extra_files)
        members = members | extra_files
        args = ['a', '-cfg-', '-idq', '-p-', '-r-', '-ol-', f'-m{compression}', '-s-', str(candidate), *sorted(members)]
        rar(executable, args, cwd=packing)
        rar(executable, ['t', '-cfg-', '-idq', '-p-', str(candidate)])
        unpack_verified(gallery, candidate, staging, executable)
        if staged_supplements(gallery, staging) != supplements:
            raise ValueError('Supplement recovery metadata mismatch')
        if current_supplements(gallery) != supplements:
            raise ValueError('Supplemental sources changed during archive verification')
        source_bytes = sum((packing / name).stat().st_size for name in members)
        archive_bytes = candidate.stat().st_size
        receipt = {'owner': OWNER, 'episode': gallery.id, 'csv_sha256': gallery.csv_hash,
                   'archive_sha256': digest(candidate.read_bytes()), 'cached': cached,
                   'expected': len(gallery.rows), 'complete': cached == len(gallery.rows),
                   'archive_format': 2, 'supplements': len(supplements['records']),
                   'input_bytes': source_bytes, 'archive_bytes': archive_bytes,
                   'saved_bytes': source_bytes-archive_bytes,
                   'compression_level': compression, 'solid': False,
                   'roundtrip_verified_utc': now(), 'elapsed_seconds': round(time.monotonic()-started, 3),
                   'rar_version': rar(executable, ['-iver']).decode(errors='replace').strip()}
        candidate.replace(gallery.archive_path)
        write_json(gallery.receipt_path, receipt)
        return receipt
    finally:
        candidate.unlink(missing_ok=True)
        if staging.exists():
            remove_owned(staging, gallery.cache_base)
        if packing.exists():
            remove_owned(packing, gallery.cache_base)


def read_receipt(gallery):
    item = json.loads(gallery.receipt_path.read_text())
    if (item.get('owner'), item.get('episode'), item.get('csv_sha256')) != (OWNER, gallery.id, gallery.csv_hash):
        raise ValueError('Archive receipt identity mismatch')
    if digest(gallery.archive_path.read_bytes()) != item['archive_sha256']:
        raise ValueError('Archive differs from verified receipt')
    return item


def restore(gallery, supplements_only=False):
    read_receipt(gallery)
    if gallery.folder.exists() and not supplements_only:
        raise ValueError('Unpacked cache already exists; refusing restore conflict')
    staging = checked_path(gallery.cache_base / f'restore-{uuid.uuid4().hex}', gallery.cache_base)
    try:
        unpack_verified(gallery, gallery.archive_path, staging, rar_path())
        restore_supplements(gallery, staging)
        if not supplements_only:
            staging.replace(gallery.folder)
    finally:
        if staging.exists():
            remove_owned(staging, gallery.cache_base)
    return gallery.status()


def prune(gallery, progress_saved=False, remove_sheets=False):
    if not progress_saved:
        raise ValueError('Prune requires --progress-saved acknowledgement')
    read_receipt(gallery)
    current = gallery.load() if gallery.folder.exists() else None
    if current is not None:
        gallery.validate_cache(gallery.folder, current)
    staging = checked_path(gallery.cache_base / f'prune-verify-{uuid.uuid4().hex}', gallery.cache_base)
    try:
        archived = unpack_verified(gallery, gallery.archive_path, staging, rar_path())
        if current is not None and current != archived:
            raise ValueError('Archive does not match current manifest; prune refused')
        supplements = current_supplements(gallery, require_media=False)
        if staged_supplements(gallery, staging) != supplements:
            raise ValueError('Archive does not include the current supplements; refresh archive before pruning')
        if remove_sheets:
            gallery.cleanup(progress_saved)
        removed_supplements = 0
        # Every present original was preflighted against the authored and restored hashes above.
        for item in supplements['records']:
            target = checked_path(gallery.root / item['media_path'], gallery.root)
            if target.exists():
                target.unlink()
                removed_supplements += 1
        manual_folder = checked_path(gallery.root / f'reference/working/manual-supplements/{gallery.id}', gallery.root)
        if manual_folder.exists() and not any(manual_folder.iterdir()):
            manual_folder.rmdir()
        if gallery.folder.exists():
            remove_owned(gallery.folder, gallery.cache_base)
    finally:
        if staging.exists():
            remove_owned(staging, gallery.cache_base)
    return {**gallery.status(), 'removed_supplements': removed_supplements}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('prepare', 'sheets', 'status', 'cleanup', 'archive', 'restore', 'prune'))
    parser.add_argument('--episode', type=int, required=True)
    parser.add_argument('--start', type=int, default=1, help='1-based locator position')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--progress-saved', action='store_true', help='Acknowledge review notes saved, or that trial sheets contain no unique annotations')
    parser.add_argument('--allow-partial', action='store_true')
    parser.add_argument('--replace-archive', action='store_true')
    parser.add_argument('--compression', type=int, choices=range(6), default=3)
    parser.add_argument('--remove-sheets', action='store_true', help='Prune only: also remove registered contact sheets; default retains them')
    parser.add_argument('--supplements-only', action='store_true', help='Restore only: recover missing supplemental PNGs without replacing the gallery cache')
    args = parser.parse_args()
    if args.remove_sheets and args.operation != 'prune':
        parser.error('--remove-sheets is only valid with prune')
    if args.supplements_only and args.operation != 'restore':
        parser.error('--supplements-only is only valid with restore')
    gallery = Gallery(args.episode)
    with episode_lock(gallery):
        if args.operation == 'prepare':
            result = gallery.prepare(args.start, args.limit, args.offline)
        elif args.operation == 'sheets':
            result = gallery.make_sheets(args.start, args.limit)
        elif args.operation == 'status':
            result = gallery.status()
        elif args.operation == 'cleanup':
            result = gallery.cleanup(args.progress_saved)
        elif args.operation == 'archive':
            result = archive(gallery, args.compression, args.allow_partial, args.replace_archive)
        elif args.operation == 'restore':
            result = restore(gallery, args.supplements_only)
        else:
            result = prune(gallery, args.progress_saved, args.remove_sheets)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        sys.exit(f'ERROR: {error}')
