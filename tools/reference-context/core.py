"""Shared, local-only context contracts and immutable source cache. Standard library only."""
from contextlib import contextmanager
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = 1


class AccessError(Exception):
    def __init__(self, outcome, diagnostic):
        super().__init__(diagnostic)
        self.outcome = outcome


FIELDS = {
    'subjects': 'subject_id display_name subject_type aliases identity_status identification_cues notes'.split(),
    'sources': ('source_id site document_key version_key title canonical_url version_url remote_page_id '
                'remote_revision_id remote_modified_utc captured_utc content_sha256 capture_method '
                'parse_status parse_warnings license_name license_url attribution_url notes').split(),
    'context': ('context_id source_id source_locator summary claim_kind continuity review_status '
                'evidence_status research_priority revisit_reason uncertainties authored_by authored_utc '
                'source_checked_by source_checked_utc primary_checked_by primary_checked_utc').split(),
    'links': 'link_id context_id relation target_type target_id notes'.split(),
}
ENUMS = {
    'subject_type': 'CHARACTER SHIP EQUIPMENT WEAPON MACHINERY LOCATION FACTION EVENT CONCEPT PRESENTATION UNKNOWN',
    'identity_status': 'PROVISIONAL ESTABLISHED AGGREGATE',
    'site': 'FANDOM ANIMEHISTORY', 'capture_method': 'FANDOM_API FANDOM_XML ANIMEHISTORY_HTML',
    'parse_status': 'COMPLETE PARTIAL FAILED',
    'claim_kind': 'IDENTIFICATION DESCRIPTION RELATIONSHIP EVENT_CONTEXT INTERPRETATION',
    'continuity': 'ANIME MANGA ANGEL_LINKS_ANIME ANGEL_LINKS_MANGA OTHER MIXED UNKNOWN',
    'review_status': 'DRAFT SOURCE_CHECKED NEEDS_RECHECK',
    'evidence_status': 'SECONDARY_ONLY PRIMARY_CORROBORATED PRIMARY_CONFLICT NOT_ASSESSED',
    'research_priority': 'UNASSESSED HIGH NORMAL LOW',
}
RELATIONS = {'ABOUT': 'SUBJECT', 'MENTIONS': 'SUBJECT', 'APPLIES_TO_EPISODE': 'EPISODE',
             'CONTEXT_FOR_IMAGE': 'IMAGE', 'SAME_ASSERTION_AS': 'CONTEXT',
             'CONTRADICTS': 'CONTEXT', 'CHECKED_AGAINST': 'EVIDENCE'}
REQUIRED = {
    'subjects': 'subject_id display_name subject_type identity_status',
    'sources': ('source_id site document_key version_key title canonical_url captured_utc content_sha256 '
                'capture_method parse_status attribution_url'),
    'context': ('context_id source_id source_locator summary claim_kind continuity review_status '
                'evidence_status research_priority authored_by authored_utc'),
    'links': 'link_id context_id relation target_type target_id',
}


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def safe_path(base, relative):
    """Reject absolute paths, escapes and existing symlinks/Windows reparse points."""
    base = Path(base).absolute()
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts or not relative.parts:
        raise ValueError('Unsafe relative cache/evidence path')
    target = base / relative
    for item in (target, *target.parents):
        if item.exists() or item.is_symlink():
            info = item.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
                raise ValueError('Symlink/reparse point refused')
    if not target.resolve().is_relative_to(base.resolve()):
        raise ValueError('Resolved path escapes base')
    return target


def atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, name = tempfile.mkstemp(prefix='.pending-', dir=path.parent)
    try:
        with os.fdopen(handle, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


@contextmanager
def writer(base):
    """Non-blocking OS lock; OS releases on process exit, no stale-PID lock deletion."""
    lock = safe_path(base, 'writer.lock')
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open('a+b') as stream:
        stream.seek(0, 2)
        if stream.tell() == 0:
            stream.write(b'0')
            stream.flush()
        stream.seek(0)
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == 'nt':
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def utc(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.utcoffset() is None or parsed.utcoffset().total_seconds() != 0:
        raise ValueError('Timestamp must have a UTC offset')


def https_url(value, hosts=None, canonical=False):
    try:
        parts = urlsplit(value)
        return (parts.scheme == 'https' and bool(parts.hostname) and not parts.username and
                parts.port in (None, 443) and (hosts is None or parts.hostname in hosts) and
                (not canonical or not parts.fragment))
    except ValueError:
        return False


def check_capture(capture):
    if capture.get('schema_version') != SCHEMA or capture.get('outcome') != 'OK':
        raise ValueError('Not a successful schema-v1 capture')
    if capture.get('site') not in ENUMS['site'].split():
        raise ValueError('Unknown site')
    for key in ('document_key', 'version_key', 'title', 'canonical_url', 'capture_method',
                'captured_utc', 'parser_version'):
        if not isinstance(capture.get(key), str) or not capture[key]:
            raise ValueError('Missing capture field: ' + key)
    if capture.get('parse_status') not in ENUMS['parse_status'].split():
        raise ValueError('Invalid parser status')
    if capture['parse_status'] != 'COMPLETE' and not capture.get('parse_warnings'):
        raise ValueError('Missing parse warnings')
    if not isinstance(capture.get('source_text'), str):
        raise ValueError('Missing source text')
    if sha(capture['source_text'].encode('utf-8')) != capture.get('content_sha256'):
        raise ValueError('Source content hash mismatch')
    utc(capture['captured_utc'])
    hosts = {'FANDOM': {'outlawstar.fandom.com'}, 'ANIMEHISTORY': {'animehistory.org', 'www.animehistory.org'}}
    if not https_url(capture['canonical_url'], hosts[capture['site']], canonical=True):
        raise ValueError('Invalid canonical URL')
    if capture['site'] == 'FANDOM':
        page, revision = capture.get('remote_page_id'), capture.get('remote_revision_id')
        if not re.fullmatch(r'[1-9]\d*', str(page)) or not re.fullmatch(r'[1-9]\d*', str(revision)):
            raise ValueError('Invalid remote IDs')
        if capture['document_key'] != f'fandom:outlawstar:page:{page}' or capture['version_key'] != f'revision:{revision}':
            raise ValueError('Fandom identity mismatch')
        if capture['capture_method'] not in ('FANDOM_API', 'FANDOM_XML'):
            raise ValueError('Capture method mismatch')
    else:
        if capture['document_key'] != 'animehistory:url:' + sha(capture['canonical_url'].encode('utf-8')):
            raise ValueError('AnimeHistory identity mismatch')
        if capture['version_key'] != 'sha256:' + capture['content_sha256'] or capture['capture_method'] != 'ANIMEHISTORY_HTML':
            raise ValueError('AnimeHistory version/method mismatch')
    if capture.get('remote_modified_utc'):
        utc(capture['remote_modified_utc'])
    locators = set()
    for section in capture.get('sections', []):
        for item in (section, *section.get('blocks', [])):
            locator = item.get('locator')
            if not locator or locator in locators:
                raise ValueError('Missing/duplicate source locator')
            locators.add(locator)
        if not isinstance(section.get('text'), str) or not isinstance(section.get('heading_path'), list):
            raise ValueError('Invalid section')
    if not locators:
        raise ValueError('No parsed section representation')


class Store:
    """Append-only snapshots/receipts; manifest is the only mutable cache catalogue.

    Snapshot identity is document+version. Nothing here initializes or edits authored CSVs.
    There is deliberately no snapshot deletion command in Stage 2.
    """
    def __init__(self, base):
        self.base = Path(base).absolute()

    def path(self, relative):
        return safe_path(self.base, relative)

    def manifest(self):
        path = self.path('manifest.json')
        if not path.exists():
            return {'schema_version': SCHEMA, 'snapshots': {}, 'aliases': {}}
        result = json.loads(path.read_text('utf-8'))
        if result.get('schema_version') != SCHEMA or not isinstance(result.get('snapshots'), dict) or not isinstance(result.get('aliases'), dict):
            raise ValueError('Invalid cache manifest')
        return result

    @staticmethod
    def key(document, version):
        return sha(encode([document, version]))

    def load(self, key):
        if not re.fullmatch(r'[0-9a-f]{64}', key):
            raise ValueError('Invalid cache key')
        directory = self.path('snapshots/' + key)
        registry = json.loads(safe_path(directory, 'files.json').read_text('utf-8'))
        if set(registry) != {'capture.json', 'source.txt'}:
            raise ValueError('Invalid snapshot file registry')
        for relative, expected in registry.items():
            if sha(safe_path(directory, relative).read_bytes()) != expected:
                raise ValueError('Snapshot file hash mismatch')
        capture = json.loads(safe_path(directory, 'capture.json').read_text('utf-8'))
        check_capture(capture)
        if self.key(capture['document_key'], capture['version_key']) != key:
            raise ValueError('Snapshot identity mismatch')
        if safe_path(directory, 'source.txt').read_bytes() != capture['source_text'].encode('utf-8'):
            raise ValueError('Source file mismatch')
        entry = self.manifest()['snapshots'].get(key, {})
        if entry.get('current_parse'):
            capture.update(self.load_parse(entry['current_parse']))
            check_capture(capture)
        return capture

    def load_parse(self, relative):
        if not re.fullmatch(r'normalized/[0-9a-f]{64}\.json', relative):
            raise ValueError('Invalid normalized-result path')
        data = self.path(relative).read_bytes()
        if sha(data) != Path(relative).stem:
            raise ValueError('Normalized-result hash mismatch')
        return json.loads(data)

    def save_parse(self, capture, entry):
        result = {key: capture[key] for key in ('parser_version', 'sections', 'parse_status', 'parse_warnings')}
        payload = encode(result)
        name = 'normalized/' + sha(payload) + '.json'
        versions = entry.setdefault('parses', {})
        if capture['parser_version'] in versions and versions[capture['parser_version']] != name:
            raise ValueError('Parser output changed without a parser-version increment')
        path = self.path(name)
        if path.exists():
            if path.read_bytes() != payload:
                raise ValueError('Normalized-result collision/corruption')
        else:
            atomic(path, payload)
        versions[capture['parser_version']] = name
        entry['current_parse'] = name

    def reparse(self, key, parser):
        capture = self.load(key)
        capture.update(parser(capture['source_text']))
        check_capture(capture)
        with writer(self.base):
            manifest = self.manifest()
            self.save_parse(capture, manifest['snapshots'][key])
            atomic(self.path('manifest.json'), encode(manifest))
        return capture

    def lookup(self, alias):
        key = self.manifest()['aliases'].get(alias)
        return self.load(key) if key else None

    def put(self, capture, raw, receipt):
        check_capture(capture)
        if not isinstance(raw, bytes) or receipt.get('raw_sha256') != sha(raw):
            raise ValueError('Invalid raw receipt')
        key = self.key(capture['document_key'], capture['version_key'])
        receipt = dict(receipt, schema_version=SCHEMA, snapshot_key=key)
        with writer(self.base):
            manifest = self.manifest()
            target = self.path('snapshots/' + key)
            if target.exists():
                previous = self.load(key)
                if previous['content_sha256'] != capture['content_sha256']:
                    raise ValueError('Content changed for same remote version; preserving prior snapshot')
            else:
                stage = Path(tempfile.mkdtemp(prefix='.pending-', dir=self.base))
                try:
                    files = {'capture.json': encode(capture), 'source.txt': capture['source_text'].encode('utf-8')}
                    for name, data in files.items():
                        safe_path(stage, name).write_bytes(data)
                    safe_path(stage, 'files.json').write_bytes(encode({name: sha(data) for name, data in files.items()}))
                    target.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(stage, target)
                finally:
                    # Only this call's freshly created, contained temporary directory.
                    if stage.exists():
                        shutil.rmtree(safe_path(self.base, stage.name))
            raw_name = 'payloads/' + sha(raw) + '.bin'
            raw_path = self.path(raw_name)
            if raw_path.exists():
                if raw_path.read_bytes() != raw:
                    raise ValueError('Raw payload collision/corruption')
            else:
                atomic(raw_path, raw)
            receipt['raw_path'] = raw_name
            receipt_name = 'receipts/' + sha(encode(receipt)) + '.json'
            receipt_path = self.path(receipt_name)
            if not receipt_path.exists():
                atomic(receipt_path, encode(receipt))
            entry = manifest['snapshots'].setdefault(key, {'document_key': capture['document_key'],
                                                         'version_key': capture['version_key'], 'receipts': []})
            self.save_parse(capture, entry)
            if receipt_name not in entry['receipts']:
                entry['receipts'].append(receipt_name)
            for alias in receipt.get('requested', []):
                previous_key = manifest['aliases'].get(alias)
                previous_capture = self.load(previous_key) if previous_key else None
                older_same_page = (previous_capture and capture['site'] == 'FANDOM' and
                                   previous_capture['document_key'] == capture['document_key'] and
                                   int(previous_capture['remote_revision_id']) > int(capture['remote_revision_id']))
                if not older_same_page:
                    manifest['aliases'][alias] = key
            atomic(self.path('manifest.json'), encode(manifest))
        return key

    def attempt(self, outcome, requested, diagnostic):
        # Only controlled diagnostics, never response bodies or cookie headers.
        entry = {'utc': now(), 'outcome': outcome, 'requested': requested, 'diagnostic': diagnostic}
        with writer(self.base):
            path = self.path('attempts.jsonl')
            with path.open('ab') as stream:
                stream.write(json.dumps(entry, ensure_ascii=False).encode('utf-8') + b'\n')

    def verify(self):
        manifest = self.manifest()
        for key, entry in manifest['snapshots'].items():
            capture = self.load(key)
            if (entry['document_key'], entry['version_key']) != (capture['document_key'], capture['version_key']):
                raise ValueError('Manifest identity mismatch')
            for relative in entry.get('parses', {}).values():
                self.load_parse(relative)
            for name in entry['receipts']:
                receipt_bytes = self.path(name).read_bytes()
                if not re.fullmatch(r'receipts/[0-9a-f]{64}\.json', name) or sha(receipt_bytes) != Path(name).stem:
                    raise ValueError('Receipt hash/path mismatch')
                receipt = json.loads(receipt_bytes)
                if receipt['snapshot_key'] != key or sha(self.path(receipt['raw_path']).read_bytes()) != receipt['raw_sha256']:
                    raise ValueError('Receipt/payload mismatch')
        for key in manifest['aliases'].values():
            if key not in manifest['snapshots']:
                raise ValueError('Dangling cache alias')
        return len(manifest['snapshots'])


class CacheSet:
    """Read-only routing across independent site caches; no combined mutable manifest."""
    key = staticmethod(Store.key)

    def __init__(self, stores):
        self.stores = list(stores)

    def load(self, key):
        matches = [store for store in self.stores if key in store.manifest()['snapshots']]
        if len(matches) != 1:
            raise ValueError('Missing or ambiguous cross-site snapshot')
        return matches[0].load(key)

    def verify(self):
        return sum(store.verify() for store in self.stores)


def read_tables(directory):
    tables = {}
    for name, fields in FIELDS.items():
        with (Path(directory) / (name + '.csv')).open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != fields:
                raise ValueError('Header/order mismatch: ' + name)
            tables[name] = list(reader)
    return tables


def source_row(capture, source_id):
    """Propose captured metadata only; does not create a claim or review any prose."""
    check_capture(capture)
    if not re.fullmatch(r'CTXSRC-\d{6,}', source_id):
        raise ValueError('Invalid explicit source ID')
    row = {field: capture.get(field, '') for field in FIELDS['sources']}
    row['source_id'] = source_id
    row['parse_warnings'] = '; '.join(capture['parse_warnings'])
    row['notes'] = ('Structural parser only; article claims require separate review. '
                    + ('No source-declared license captured; verify reuse terms. ' if not row['license_name'] else '')
                    + 'Source text remains in the ignored local cache.')
    return row


def validate_tables(tables, root=ROOT, store=None, image_keys=None, episode_ids=None):
    """Read-only contract validation. No authored data is rewritten or auto-reviewed."""
    errors = []
    indices = {}
    for name, fields in FIELDS.items():
        if name not in tables:
            errors.append('Missing table: ' + name)
        index = indices[name] = {}
        for row in tables.get(name, []):
            ident = row.get(fields[0], '')
            label = name + ':' + ident
            if set(row) != set(fields) or any(not isinstance(value, str) for value in row.values()):
                errors.append(label + ': invalid fields/row width')
                continue
            pattern = {'subjects': r'[a-z][a-z0-9]*(?:_[a-z0-9]+)*', 'sources': r'CTXSRC-\d{6,}',
                       'context': r'CTX-\d{6,}', 'links': r'CTXLINK-\d{6,}'}[name]
            if not re.fullmatch(pattern, ident) or ident in index:
                errors.append(label + ': duplicate/invalid ID')
            index[ident] = row
            for field in REQUIRED[name].split():
                if not row[field].strip():
                    errors.append(label + ': required ' + field)
            for field, values in ENUMS.items():
                if field in row and row[field] not in values.split():
                    errors.append(label + ': invalid ' + field)
            for field, value in row.items():
                if value and field.endswith('_utc'):
                    try:
                        utc(value)
                    except ValueError:
                        errors.append(label + ': invalid UTC ' + field)
            for prefix in ('source_checked', 'primary_checked'):
                if prefix + '_by' in row and bool(row[prefix + '_by']) != bool(row[prefix + '_utc']):
                    errors.append(label + ': unpaired provenance ' + prefix)
    sources, contexts, subjects = indices['sources'], indices['context'], indices['subjects']
    seen_sources, seen_links, subject_links = set(), set(), set()
    cached = {}
    if store:
        try:
            store.verify()
        except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
            errors.append('Cache health: ' + str(exc))
    for row in sources.values():
        label = row['source_id']
        grain = row['document_key'], row['version_key']
        if grain in seen_sources:
            errors.append(label + ': duplicate source version')
        seen_sources.add(grain)
        if not re.fullmatch('[0-9a-f]{64}', row['content_sha256']):
            errors.append(label + ': invalid content hash')
        for field in ('canonical_url', 'version_url', 'license_url', 'attribution_url'):
            if row[field] and not https_url(row[field]):
                errors.append(label + ': invalid HTTPS ' + field)
        hosts = {'FANDOM': {'outlawstar.fandom.com'}, 'ANIMEHISTORY': {'animehistory.org', 'www.animehistory.org'}}
        if not https_url(row['canonical_url'], hosts.get(row['site'], set()), canonical=True):
            errors.append(label + ': invalid canonical source URL')
        if row['parse_status'] != 'COMPLETE' and not row['parse_warnings']:
            errors.append(label + ': missing parse warnings')
        if not row['license_name'] and not row['notes']:
            errors.append(label + ': unknown license needs notes')
        if row['site'] == 'FANDOM':
            if grain != (f"fandom:outlawstar:page:{row['remote_page_id']}", f"revision:{row['remote_revision_id']}"):
                errors.append(label + ': inconsistent Fandom identity')
            if (not re.fullmatch(r'[1-9]\d*', row['remote_page_id']) or not re.fullmatch(r'[1-9]\d*', row['remote_revision_id'])
                    or row['capture_method'] not in ('FANDOM_API', 'FANDOM_XML')):
                errors.append(label + ': invalid Fandom IDs/method')
        elif row['site'] == 'ANIMEHISTORY':
            if (row['document_key'] != 'animehistory:url:' + sha(row['canonical_url'].encode('utf-8')) or
                    row['version_key'] != 'sha256:' + row['content_sha256'] or
                    row['capture_method'] != 'ANIMEHISTORY_HTML'):
                errors.append(label + ': invalid AnimeHistory identity/method')
        if store:
            try:
                capture = store.load(store.key(*grain))
                cached[label] = capture
                if capture['content_sha256'] != row['content_sha256']:
                    errors.append(label + ': pinned hash differs')
            except (ValueError, OSError, KeyError, json.JSONDecodeError):
                errors.append(label + ': pinned snapshot missing/corrupt')
    for row in indices['links'].values():
        origin, relation, kind, target = (row[key] for key in ('context_id', 'relation', 'target_type', 'target_id'))
        label = row['link_id']
        grain = origin, relation, kind, target
        if grain in seen_links or RELATIONS.get(relation) != kind or origin not in contexts:
            errors.append(label + ': duplicate/invalid link')
        seen_links.add(grain)
        if kind == 'SUBJECT':
            if target not in subjects:
                errors.append(label + ': unknown subject')
            if relation in ('ABOUT', 'MENTIONS'):
                pair = origin, target
                if pair in subject_links:
                    errors.append(label + ': repeated ABOUT/MENTIONS subject')
                subject_links.add(pair)
        elif kind == 'CONTEXT':
            if target not in contexts or origin == target or not origin.startswith('CTX-') or not target.startswith('CTX-'):
                errors.append(label + ': invalid context target')
            elif not re.fullmatch(r'CTX-\d{6,}', origin) or not re.fullmatch(r'CTX-\d{6,}', target) or int(origin[4:]) >= int(target[4:]):
                errors.append(label + ': context pair must be ascending')
        elif kind == 'IMAGE' and (image_keys is None or target not in image_keys):
            errors.append(label + ': unknown/unvalidated image')
        elif kind == 'EPISODE' and (episode_ids is None or target not in episode_ids):
            errors.append(label + ': unknown/unvalidated episode')
        elif kind == 'EVIDENCE':
            try:
                file, _, anchor = target.partition('#')
                evidence = safe_path(root, file)
                if not evidence.is_file() or evidence.suffix.lower() != '.md':
                    raise ValueError('Evidence must be an existing Markdown assessment')
                if anchor:
                    text = evidence.read_text('utf-8')
                    headings = re.findall(r'^#+\s+(.+?)\s*#*$', text, re.M)
                    counts, anchors = {}, set()
                    for heading in headings:
                        slug = re.sub(r'[^\w\- ]', '', heading.lower().replace('`', '')).replace(' ', '-')
                        number = counts.get(slug, 0)
                        counts[slug] = number + 1
                        anchors.add(slug + (f'-{number}' if number else ''))
                    anchors.update(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
                    if anchor not in anchors:
                        raise ValueError('Evidence anchor missing')
            except (ValueError, OSError):
                errors.append(label + ': unsafe/missing evidence pointer or anchor')
        if relation in ('CONTRADICTS', 'CHECKED_AGAINST') and not row['notes']:
            errors.append(label + ': missing relation limits')
    for row in contexts.values():
        label = row['context_id']
        source = sources.get(row['source_id'])
        related = [link for link in indices['links'].values() if link['context_id'] == label]
        if not source:
            errors.append(label + ': missing source')
        if row['review_status'] == 'SOURCE_CHECKED':
            if not row['source_checked_by'] or not any(link['relation'] == 'ABOUT' for link in related):
                errors.append(label + ': checked claim needs reviewer and ABOUT link')
            if source and (source['parse_status'] == 'FAILED' or (source['parse_status'] == 'PARTIAL' and not row['uncertainties'])):
                errors.append(label + ': unresolved parse limits')
        if row['evidence_status'] in ('PRIMARY_CORROBORATED', 'PRIMARY_CONFLICT'):
            if not row['primary_checked_by'] or not any(link['relation'] == 'CHECKED_AGAINST' for link in related):
                errors.append(label + ': primary state needs scoped assessment')
        if ((row['research_priority'] == 'HIGH' and not row['revisit_reason']) or
            ((row['review_status'] == 'NEEDS_RECHECK' or row['evidence_status'] == 'PRIMARY_CONFLICT'
              or row['continuity'] in ('MIXED', 'UNKNOWN')) and not row['uncertainties'])):
            errors.append(label + ': missing uncertainty/revisit reason')
        capture = cached.get(row['source_id'])
        if capture and row['source_locator'] != 'DOCUMENT':
            locations = {part['locator'] for section in capture['sections'] for part in (section, *section['blocks'])}
            if row['source_locator'] not in locations:
                errors.append(label + ': source locator missing from capture')
    for row in subjects.values():
        aliases = row['aliases'].split(';') if row['aliases'] else []
        if any(not alias.strip() or alias != alias.strip() for alias in aliases) or len(set(aliases)) != len(aliases):
            errors.append(row['subject_id'] + ': invalid duplicate/empty aliases')
        if row['identification_cues'] and not any(link['relation'] == 'ABOUT' and link['target_id'] == row['subject_id']
                                                  for link in indices['links'].values()):
            errors.append(row['subject_id'] + ': cues require ABOUT-linked basis')
    return errors
