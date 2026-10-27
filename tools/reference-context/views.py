"""Validated reader/Power BI projections. Never rewrite the maintained research tables."""
import csv
from pathlib import Path
from urllib.parse import quote

from core import ROOT, FIELDS, CacheSet, Store, read_tables, sha, validate_tables

INDEX = ROOT / 'reference/indexes/context'


def caches():
    return CacheSet([Store(ROOT / 'reference/cache/context' / site) for site in ('fandom', 'animehistory')])


def image_inventory():
    inventory, episodes = {}, set()
    base = ROOT / 'reference/indexes/animehistory'
    with (base / 'all-episodes.csv').open(encoding='utf-8-sig', newline='') as stream:
        for row in csv.DictReader(stream):
            key = row['episode_id'] + ':' + row['image_id']
            if key in inventory:
                raise ValueError('Duplicate gallery image key')
            inventory[key] = {'url': row['image_url'], 'availability': 'ONLINE_REFERENCE',
                              'episode_id': row['episode_id'], 'web_timestamp': row['web_timestamp']}
            episodes.add(row['episode_id'])
    with (base / 'supplemental-index.csv').open(encoding='utf-8-sig', newline='') as stream:
        for row in csv.DictReader(stream):
            key = row['episode_id'] + ':' + row['image_id']
            if key in inventory:
                raise ValueError('Duplicate manual/gallery image key')
            from core import safe_path
            path = safe_path(ROOT, row['media_path'])
            availability = 'NOT_LOCAL'
            if path.exists():
                if sha(path.read_bytes()) != row['media_sha256']:
                    raise ValueError('Supplement media differs from registered hash')
                availability = 'LOCAL_VERIFIED'
            inventory[key] = {'url': path.as_uri(), 'availability': availability,
                              'episode_id': row['episode_id'], 'web_timestamp': ''}
            episodes.add(row['episode_id'])
    return inventory, episodes


def bridge_tables(tables):
    output = {name: [] for name in ('context_subjects', 'context_episodes', 'context_images',
                                    'context_contexts', 'context_evidence')}
    names = {'SUBJECT': 'context_subjects', 'EPISODE': 'context_episodes', 'IMAGE': 'context_images',
             'CONTEXT': 'context_contexts', 'EVIDENCE': 'context_evidence'}
    for link in tables['links']:
        output[names[link['target_type']]].append({key: link[key] for key in ('context_id', 'relation', 'target_id', 'notes')})
    return output


def build_view(index=INDEX):
    tables = read_tables(index)
    images, episodes = image_inventory()
    errors = validate_tables(tables, root=ROOT, store=caches(), image_keys=set(images), episode_ids=episodes)
    if errors:
        raise ValueError('Context validation failed: ' + '; '.join(errors))
    subjects = {row['subject_id']: row for row in tables['subjects']}
    sources = {row['source_id']: row for row in tables['sources']}
    contexts = {row['context_id']: row for row in tables['context']}
    rows = {'Subjects': tables['subjects'], 'Sources': tables['sources'], 'Context': [], 'Links': []}
    for record in tables['context']:
        links = [link for link in tables['links'] if link['context_id'] == record['context_id']]
        source = sources[record['source_id']]
        capture = caches().load(Store.key(source['document_key'], source['version_key']))
        section = next((section for section in capture['sections'] if section['locator'] == record['source_locator']
                        or any(block['locator'] == record['source_locator'] for block in section['blocks'])), None)
        source_url = source['version_url'] or source['canonical_url']
        if source['site'] == 'ANIMEHISTORY' and section and section.get('source_anchor'):
            source_url += '#' + quote(section['source_anchor'])
        scoped_subjects = sorted({subjects[link['target_id']]['display_name'] for link in links if link['relation'] == 'ABOUT'})
        image_links = [link for link in links if link['relation'] == 'CONTEXT_FOR_IMAGE']
        rows['Context'].append({
            'context_id': record['context_id'], 'summary': record['summary'],
            'about_subjects': '; '.join(scoped_subjects), 'review_status': record['review_status'],
            'evidence_status': record['evidence_status'], 'continuity': record['continuity'],
            'source_title': source['title'], 'source_url': source_url,
            **{field: record[field] for field in FIELDS['context'] if field not in ('context_id', 'summary', 'review_status', 'evidence_status', 'continuity')},
            'source_site': source['site'], 'linked_images': len(image_links),
            'section_heading': ' / '.join(section['heading_path']) if section else '',
        })
    for link in tables['links']:
        kind, target = link['target_type'], link['target_id']
        url, availability = '', ''
        if kind == 'IMAGE':
            url, availability = images[target]['url'], images[target]['availability']
        elif kind == 'EVIDENCE':
            path, _, anchor = target.partition('#')
            url = (ROOT / path).as_uri() + ('#' + anchor if anchor else '')
        label = subjects[target]['display_name'] if kind == 'SUBJECT' else contexts[target]['summary'] if kind == 'CONTEXT' else target
        rows['Links'].append(dict(link, target_label=label, target_url=url, media_availability=availability))
    bridges = bridge_tables(tables)
    linked_images = {row['target_id'] for row in bridges['context_images']}
    metrics = {
        'Subjects': len(subjects), 'Captured source versions': len(sources), 'Context records': len(contexts),
        'Source checked': sum(row['review_status'] == 'SOURCE_CHECKED' for row in contexts.values()),
        'Needs recheck': sum(row['review_status'] == 'NEEDS_RECHECK' for row in contexts.values()),
        'Draft': sum(row['review_status'] == 'DRAFT' for row in contexts.values()),
        'Primary corroborated': sum(row['evidence_status'] == 'PRIMARY_CORROBORATED' for row in contexts.values()),
        'Distinct linked images': len(linked_images),
        'Linked manual images not local': sum(images[key]['availability'] == 'NOT_LOCAL' for key in linked_images),
    }
    return {'schema_version': 1, 'sheets': rows, 'metrics': metrics, 'bridges': bridges,
            'input_hashes': {name: sha((Path(index) / (name + '.csv')).read_bytes()) for name in FIELDS},
            'image_index_hashes': {name: sha((ROOT / 'reference/indexes/animehistory' / name).read_bytes())
                                   for name in ('category-index.csv', 'supplemental-index.csv', 'all-episodes.csv')}}
