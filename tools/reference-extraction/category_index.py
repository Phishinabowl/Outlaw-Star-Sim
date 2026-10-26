"""Initialize/validate authored gallery annotations and prepare a disposable browsing join."""
import argparse
from collections import Counter
import csv
import hashlib
from datetime import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / 'reference/indexes/animehistory'
FIELDS = ('episode_id image_id scene_group_id scene_summary categories subjects subject_details '
          'presentation screening_status detail_status identification_confidence visual_summary '
          'research_priority revisit_reason uncertainties reported_context screened_by screened_utc '
          'detail_reviewed_by detail_reviewed_utc detail_references').split()
DEFAULTS = dict(presentation='UNKNOWN', screening_status='UNREVIEWED', detail_status='NOT_REVIEWED',
                identification_confidence='NOT_ASSESSED', research_priority='UNASSESSED')
SUPPLEMENT_FIELDS = FIELDS + ['media_path', 'media_sha256', 'media_bytes', 'local_timestamp',
                              'local_seconds', 'timestamp_basis', 'alignment_status',
                              'related_gallery_ids', 'source_description']


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as source:
        reader = csv.DictReader(source)
        return reader.fieldnames, list(reader)


def contract():
    """Read controlled values from their single authoritative documentation register."""
    doc = (INDEX / 'README.md').read_text(encoding='utf-8')
    field_section = doc.split('### Category-index field contract — version 1', 1)[1].split('### Initial tag vocabulary', 1)[0]
    lines = [line for line in field_section.splitlines() if line.startswith('| `')]
    if [re.findall(r'`([^`]+)`', line)[0] for line in lines] != FIELDS:
        raise ValueError('Documented field contract differs from validator version 1')
    enums = {}
    for line in lines:
        tokens = re.findall(r'`([^`]+)`', line)
        if tokens[0] in DEFAULTS:
            enums[tokens[0]] = {v for v in tokens[1:] if re.fullmatch('[A-Z_]+', v)}
    section = doc.split('### Initial tag vocabulary', 1)[1].split('### Initial validation', 1)[0]
    category, rest = section.split('The `subjects` register starts with:', 1)
    subject, detail = rest.split('Initial `subject_details` tokens are:', 1)
    def table_tokens(text):
        return {token for line in text.splitlines() if line.startswith('| ')
                for token in re.findall(r'`([a-z][a-z_]+)`', line)}
    return enums, dict(categories=table_tokens(category), subjects=table_tokens(subject),
                       subject_details=table_tokens(detail))


def key(row):
    return row['episode_id'] + ':' + row['image_id']


def locators():
    _, rows = read_csv(INDEX / 'all-episodes.csv')
    counts = Counter(row['episode_id'] for row in rows)
    if len(rows) != 9204 or counts != {f'EP-{n:02}': 354 for n in range(1, 27)}:
        raise ValueError('Unexpected locator baseline')
    if len({key(row) for row in rows}) != len(rows):
        raise ValueError('Duplicate locator keys')
    return rows


def initialize(path, sources):
    rows = [{**dict.fromkeys(FIELDS, ''), **DEFAULTS,
             'episode_id': source['episode_id'], 'image_id': source['image_id']} for source in sources]
    with path.open('x', encoding='utf-8', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def validate(rows, sources, enums=None, vocabulary=None):
    if enums is None:
        enums, vocabulary = contract()
    expected = {key(row) for row in sources}
    if len(rows) != len(expected) or {key(row) for row in rows} != expected:
        raise ValueError('Annotation keys missing, duplicated or outside locator baseline')
    by_key = {key(row): row for row in rows}
    group_summary, group_positions = {}, {}
    for ordinal, source in enumerate(sources):
        row = by_key[key(source)]
        def require(condition, message):
            if not condition:
                raise ValueError(f'{key(row)}: {message}')
        require(list(row) == FIELDS and all(isinstance(v, str) for v in row.values()), 'Invalid fields or missing values')
        for field, values in enums.items():
            require(row[field] in values, f'Invalid {field}: {row[field]}')
        for field, values in vocabulary.items():
            tags = row[field].split(';') if row[field] else []
            require(tags == sorted(set(tags)) and set(tags) <= values, f'Invalid/duplicate/unsorted {field}')
        for who, when in [('screened_by', 'screened_utc'), ('detail_reviewed_by', 'detail_reviewed_utc')]:
            require(bool(row[who]) == bool(row[when]), f'Incomplete {who}/{when}')
            if row[when]:
                try:
                    parsed = datetime.fromisoformat(row[when].replace('Z', '+00:00'))
                    require(parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0, 'Review time must be UTC')
                except ValueError:
                    raise ValueError(f'{key(row)}: Invalid UTC timestamp') from None
        status = row['screening_status']
        if status == 'UNREVIEWED':
            require(all(row[f] == DEFAULTS.get(f, '') for f in FIELDS if f not in ('episode_id', 'image_id')), 'Untouched row contains authored content')
        else:
            require(bool(row['screened_by']), 'Screening attempt needs provenance')
        if status in ('SCREENED', 'NEEDS_RECHECK'):
            require(bool(row['visual_summary']), 'Inspected image needs visual summary')
        if status in ('NEEDS_RECHECK', 'UNAVAILABLE') or row['identification_confidence'] == 'LOW':
            require(bool(row['uncertainties']), 'Missing uncertainty/access obstacle')
        if row['subjects'] and status != 'UNAVAILABLE':
            require(row['identification_confidence'] != 'NOT_ASSESSED', 'Named/candidate subjects need confidence')
        if row['research_priority'] == 'HIGH':
            require(bool(row['revisit_reason']), 'High priority needs revisit reason')
        if row['detail_status'] != 'NOT_REVIEWED':
            require(bool(row['detail_reviewed_by'] and row['detail_references']), 'Detailed review needs provenance/evidence')
        else:
            require(not row['detail_reviewed_by'] and not row['detail_references'], 'Unexpected detailed-review data')
        for reference in filter(None, row['detail_references'].split(';')):
            relative = Path(reference.split('#', 1)[0])
            require(not relative.is_absolute() and '..' not in relative.parts and (ROOT / relative).is_file(), 'Invalid evidence reference')
        group = row['scene_group_id']
        require(bool(group) == bool(row['scene_summary']), 'Group identity/summary must be paired')
        if group:
            require(bool(re.fullmatch(re.escape(row['episode_id']) + r'-S\d{3}', group)), 'Invalid episode-scoped group')
            require(group_summary.setdefault(group, row['scene_summary']) == row['scene_summary'], 'Group summary mismatch')
            group_positions.setdefault(group, []).append(ordinal)
    for group, positions in group_positions.items():
        if positions != list(range(positions[0], positions[-1] + 1)):
            raise ValueError(f'Noncontiguous scene group: {group}')
    return by_key


def browsing_data(rows, sources):
    by_key = validate(rows, sources)
    ordinals, joined = Counter(), []
    for source in sources:
        ordinals[source['episode_id']] += 1
        joined.append({**by_key[key(source)], 'image_key': key(source),
                       'episode_number': int(source['episode_id'][3:]),
                       'locator_ordinal': ordinals[source['episode_id']],
                       **{f: source[f] for f in ('episode_title', 'web_timestamp', 'web_seconds',
                                                'image_url', 'source_page_url', 'alignment_status')}})
    return joined


def validate_supplements(rows, sources, verify_media=False):
    """Separate manual records retain their own time basis and never enlarge gallery coverage."""
    related = {(r['episode_id'], r['image_id']) for r in sources}
    episodes = {r['episode_id'] for r in sources}
    annotations = []
    for row in rows:
        if list(row) != SUPPLEMENT_FIELDS or any(not isinstance(v, str) for v in row.values()):
            raise ValueError('Supplement header/values mismatch')
        if row['episode_id'] not in episodes or not re.fullmatch(re.escape(row['episode_id']) + r'-MAN-\d{3}', row['image_id']):
            raise ValueError('Invalid manual reference identity')
        if row['timestamp_basis'] != 'PLAYER_UI_WHOLE_SECONDS' or row['alignment_status'] != 'UNRECONCILED':
            raise ValueError('Manual timing must remain explicitly unreconciled under version 1')
        if not re.fullmatch(r'\d{2}:\d{2}', row['local_timestamp']):
            raise ValueError('Expected observed mm:ss player label')
        minutes, seconds = map(int, row['local_timestamp'].split(':'))
        if seconds >= 60 or str(minutes * 60 + seconds) != row['local_seconds']:
            raise ValueError('Player label/seconds mismatch')
        if not re.fullmatch('[0-9a-f]{64}', row['media_sha256']) or not row['media_bytes'].isdigit() or int(row['media_bytes']) < 1:
            raise ValueError('Invalid manual media hash/size')
        relative = Path(row['media_path'])
        base = (ROOT / 'reference/working/manual-supplements').resolve()
        target = (ROOT / relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or not target.is_relative_to(base):
            raise ValueError('Supplement path outside owned manual-media folder')
        if not row['source_description']:
            raise ValueError('Missing manual source provenance')
        ids = row['related_gallery_ids'].split(';') if row['related_gallery_ids'] else []
        if len(ids) != len(set(ids)) or any((row['episode_id'], value) not in related for value in ids):
            raise ValueError('Unknown/duplicate associated gallery image')
        if verify_media:
            data = target.read_bytes()
            if len(data) != int(row['media_bytes']) or hashlib.sha256(data).hexdigest() != row['media_sha256']:
                raise ValueError('Manual media hash/size mismatch')
        annotations.append({field: row[field] for field in FIELDS})
    validate(annotations, annotations)
    return rows


def supplements(sources, verify_media=False):
    path = INDEX / 'supplemental-index.csv'
    if not path.exists():
        return []
    fields, rows = read_csv(path)
    if fields != SUPPLEMENT_FIELDS:
        raise ValueError('Supplement CSV header mismatch')
    return validate_supplements(rows, sources, verify_media)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('initialize', 'validate', 'view-data', 'supplement-data'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    sources = locators()
    path = INDEX / 'category-index.csv'
    if args.operation == 'initialize':
        initialize(path, sources)
    fields, rows = read_csv(path)
    if fields != FIELDS:
        raise ValueError('Annotation CSV header mismatch')
    validate(rows, sources)
    manual = supplements(sources, verify_media=args.operation == 'supplement-data')
    if args.operation in ('view-data', 'supplement-data'):
        output = args.output.resolve() if args.output else None
        if output is None or not output.is_relative_to((ROOT / '.tmp').resolve()):
            raise ValueError('Browsing intermediate must be under repository .tmp')
        output.parent.mkdir(parents=True, exist_ok=True)
        if args.operation == 'view-data':
            data = browsing_data(rows, sources)
        else:
            data = [{**r, 'image_key': key(r), 'episode_number': int(r['episode_id'][3:]),
                     'media_uri': (ROOT / r['media_path']).resolve().as_uri()}
                    for r in sorted(manual, key=lambda r: (r['episode_id'], int(r['local_seconds']), r['image_id']))]
        output.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({'records': len(rows), 'screening': dict(Counter(r['screening_status'] for r in rows)),
                      'detail': dict(Counter(r['detail_status'] for r in rows)),
                      'episode_04': dict(Counter(r['screening_status'] for r in rows if r['episode_id'] == 'EP-04')),
                      'manual_supplements': len(manual)}))


if __name__ == '__main__':
    main()
