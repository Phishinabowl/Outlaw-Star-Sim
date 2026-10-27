"""Selected public source capture/cache and read-only CSV validation; no authored writes."""
import argparse
import csv
import json
import sys

from core import ROOT, Store, CacheSet, read_tables, sha, validate_tables, source_row, safe_path, atomic, encode
from fandom import AccessError, Client, MAX_TITLES, from_xml, parse, title_check
import animehistory

CACHE = ROOT / 'reference/cache/context/fandom'
ANIME_CACHE = ROOT / 'reference/cache/context/animehistory'


def brief(capture, reused=False):
    return {key: capture[key] for key in ('title', 'document_key', 'version_key', 'content_sha256', 'parse_status')} | {
        'text_characters': len(capture['source_text']), 'sections': len(capture['sections']),
        'parse_warnings': capture['parse_warnings'], 'cache_reused': reused}


def run(args):
    store = Store(CACHE)
    if args.command in ('animehistory-fetch', 'animehistory-reparse'):
        store = Store(ANIME_CACHE)
        if not 1 <= len(args.url) <= animehistory.MAX_URLS:
            raise ValueError('Select 1–10 explicit URLs')
        requested = {}
        for url in args.url:
            document = animehistory.canonical(url)
            requested.setdefault(document, []).append(url)
        client, output = animehistory.Client(), []
        for document, selections in requested.items():
            cached = store.lookup(document)
            if args.command == 'animehistory-reparse':
                if not cached:
                    raise ValueError('Document not in cache: ' + document)
                capture = store.reparse(store.key(cached['document_key'], cached['version_key']),
                                        lambda text: animehistory.parse(text, cached['canonical_url']))
                reused = True
            elif cached and not args.refresh:
                capture, reused = cached, True
            else:
                try:
                    capture, raw, receipt = client.query(document)
                    store.put(capture, raw, receipt)
                    reused = False
                except AccessError as exc:
                    store.attempt(exc.outcome, [document], str(exc))
                    raise
            item = brief(capture, reused)
            item['selections'] = {url: animehistory.selection(capture, url) for url in selections}
            output.append(item)
        print(json.dumps(output, indent=2, ensure_ascii=False))
    elif args.command == 'animehistory-discover':
        print(json.dumps(animehistory.Client().discover(), indent=2))
    elif args.command in ('show', 'source-row'):
        store = Store(ANIME_CACHE if args.site == 'animehistory' else CACHE)
        article = animehistory.canonical(args.article) if args.site == 'animehistory' else title_check(args.article)
        capture = store.lookup(article)
        if not capture:
            raise ValueError('Selected article is not cached; no network request made')
        if args.command == 'source-row':
            print(json.dumps(source_row(capture, args.source_id), indent=2, ensure_ascii=False))
            return 0
        output = brief(capture, True)
        if args.locator:
            if len(args.locator) > 5 or len(set(args.locator)) != len(args.locator):
                raise ValueError('Select 1–5 unique explicit section/block locators')
            found = {part['locator']: part for section in capture['sections'] for part in (section, *section['blocks'])}
            if any(locator not in found for locator in args.locator):
                raise ValueError('Selected locator is absent from this source version')
            output['content'] = [found[locator] for locator in args.locator]
        else:
            output['section_index'] = [{key: section.get(key) for key in ('locator', 'heading_path', 'source_anchor', 'episode_id_hint')}
                                       for section in capture['sections']]
        print(json.dumps(output, indent=2, ensure_ascii=False))
    elif args.command in ('fetch', 'reparse'):
        titles = args.title
        if not 1 <= len(titles) <= MAX_TITLES or len(set(titles)) != len(titles):
            raise ValueError('Select 1–10 unique explicit titles')
        for title in titles:
            title_check(title)
        client = Client()
        output = []
        for title in titles:
            cached = store.lookup(title)
            if args.command == 'reparse':
                if not cached:
                    raise ValueError('Article not in cache: ' + title)
                output.append(brief(store.reparse(store.key(cached['document_key'], cached['version_key']), parse), True))
                continue
            if cached and not args.refresh:
                output.append(brief(cached, True))
                continue
            try:
                capture, raw, receipt = client.query(title)
                store.put(capture, raw, receipt)
                output.append(brief(capture))
            except AccessError as exc:
                store.attempt(exc.outcome, [title], str(exc))
                raise
        print(json.dumps(output, indent=2, ensure_ascii=False))
    elif args.command == 'import-xml':
        path = args.path.resolve()
        if path.stat().st_size > 8 * 1024 * 1024:
            raise ValueError('XML size limit exceeded')
        raw = path.read_bytes()
        captures = from_xml(raw)
        for capture in captures:
            receipt = {'requested': [capture['title']], 'capture_method': 'FANDOM_XML',
                       'captured_utc': capture['captured_utc'], 'raw_sha256': sha(raw),
                       'raw_bytes': len(raw), 'media_type': 'application/xml', 'input_filename': path.name}
            store.put(capture, raw, receipt)
        print(json.dumps([brief(item) for item in captures], indent=2, ensure_ascii=False))
    elif args.command == 'verify':
        stores = {'fandom': store, 'animehistory': Store(ANIME_CACHE)}
        selected = stores if args.site == 'all' else {args.site: stores[args.site]}
        print(json.dumps({'verified_snapshots': {site: item.verify() for site, item in selected.items()}}))
    elif args.command == 'compare-xml':
        if args.path.stat().st_size > 8 * 1024 * 1024:
            raise ValueError('XML size limit exceeded')
        comparisons = []
        for expected in from_xml(args.path.read_bytes()):
            actual = store.load(store.key(expected['document_key'], expected['version_key']))
            match = actual['source_text'] == expected['source_text']
            comparisons.append({'title': expected['title'], 'version_key': expected['version_key'], 'exact_text_match': match})
            if not match:
                raise ValueError('XML text differs from cached revision')
        print(json.dumps(comparisons, indent=2))
    elif args.command == 'validate':
        images, episodes = set(), set()
        for name in ('category-index.csv', 'supplemental-index.csv'):
            with (ROOT / 'reference/indexes/animehistory' / name).open(encoding='utf-8-sig', newline='') as stream:
                for row in csv.DictReader(stream):
                    images.add(row['episode_id'] + ':' + row['image_id'])
                    episodes.add(row['episode_id'])
        errors = validate_tables(read_tables(ROOT / 'reference/indexes/context'),
                                 store=CacheSet([store, Store(ANIME_CACHE)]), image_keys=images, episode_ids=episodes)
        print(json.dumps({'valid': not errors, 'errors': errors}, indent=2))
        return 1 if errors else 0
    elif args.command == 'view-data':
        from views import build_view
        data = build_view()
        destination = args.output.absolute()
        relative = destination.relative_to(ROOT)
        path = safe_path(ROOT, relative)
        if path.suffix != '.json' or not (path.is_relative_to(ROOT / '.tmp') or path.is_relative_to(ROOT / 'reference/working/context')):
            raise ValueError('Generated view data must be JSON in workspace temporary/context working storage')
        atomic(path, encode(data))
        print(json.dumps({'output': str(path), 'metrics': data['metrics']}))
    return 0


def main():
    from pathlib import Path
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    fetch = commands.add_parser('fetch', help='Fetch selected public articles; reuse cache unless --refresh')
    fetch.add_argument('--title', action='append', required=True)
    fetch.add_argument('--refresh', action='store_true')
    commands.add_parser('reparse', help='Reparse retained source text offline; preserve raw snapshots').add_argument('--title', action='append', required=True)
    for command in ('import-xml', 'compare-xml'):
        commands.add_parser(command).add_argument('path', type=Path)
    for command in ('animehistory-fetch', 'animehistory-reparse'):
        subparser = commands.add_parser(command)
        subparser.add_argument('--url', action='append', required=True)
        if command.endswith('fetch'):
            subparser.add_argument('--refresh', action='store_true')
    commands.add_parser('animehistory-discover', help='List selected public sitemap URLs; download no articles')
    show = commands.add_parser('show', help='Offline section index or selected cached source text; never writes research')
    show.add_argument('--site', choices=('fandom', 'animehistory'), required=True)
    show.add_argument('--article', required=True)
    show.add_argument('--locator', action='append')
    source = commands.add_parser('source-row', help='Propose cached source metadata for an explicit stable ID; write no CSVs')
    source.add_argument('--site', choices=('fandom', 'animehistory'), required=True)
    source.add_argument('--article', required=True)
    source.add_argument('--source-id', required=True)
    commands.add_parser('view-data', help='Validate maintained tables and write a generated workbook/bridge projection').add_argument('--output', type=Path, required=True)
    commands.add_parser('verify').add_argument('--site', choices=('fandom', 'animehistory', 'all'), default='fandom')
    commands.add_parser('validate', help='Validate existing maintained CSVs; never initialize/rewrite them')
    try:
        return run(parser.parse_args())
    except (AccessError, ValueError, OSError, KeyError) as exc:
        print(json.dumps({'outcome': getattr(exc, 'outcome', 'ERROR'), 'diagnostic': str(exc)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
