"""Disposable contract, cache, transport and structural-parser regression tests."""
import copy
import csv
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import core
import fandom


def tempdir():
    base = core.safe_path(core.ROOT, 'reference/working/context/tests')
    base.mkdir(parents=True, exist_ok=True)
    return tempfile.TemporaryDirectory(dir=base)


def api_data(text='A short article.', title='Horus', revision=9335, page=2691):
    return {'query': {'pages': [{'ns': 0, 'title': title, 'pageid': page, 'revisions': [
        {'revid': revision, 'timestamp': '2024-06-24T05:37:56Z',
         'slots': {'main': {'contentmodel': 'wikitext', 'content': text}}}]}]}}


def sample(text='A short article.', revision=9335):
    return fandom.from_api(api_data(text, revision=revision), 'Horus')


def receipt(raw=b'payload', method='FANDOM_API'):
    return {'requested': ['Horus'], 'raw_sha256': core.sha(raw), 'capture_method': method,
            'raw_bytes': len(raw), 'media_type': 'application/json', 'captured_utc': '2026-10-26T00:00:00Z'}


class ParserTests(unittest.TestCase):
    def test_nested_infobox_and_reference_preserved(self):
        text = '{{Infobox ship|name={{PAGENAME}}|ship=[[Horus|Horus ship]]|other={{x|a|b}}}}\n' \
               'Intro<ref name="ep">[[Episode 4]]</ref>\n==Anime==\nA.\n==Manga==\nB.'
        result = fandom.parse(text)
        self.assertEqual(result['parse_status'], 'PARTIAL')
        blocks = result['sections'][0]['blocks']
        fields = {item['name']: item['value'] for item in blocks if item['kind'] == 'INFOBOX_FIELD'}
        self.assertEqual(fields['name'], '{{PAGENAME}}')
        self.assertEqual(fields['ship'], '[[Horus|Horus ship]]')
        self.assertEqual(fields['other'], '{{x|a|b}}')
        self.assertTrue(any(item['kind'] == 'REFERENCE' and 'Episode 4' in item['raw'] for item in blocks))
        self.assertEqual([item['heading_path'] for item in result['sections']], [[], ['Anime'], ['Manga']])
        self.assertNotIn('Unbalanced template/parameter delimiter', result['parse_warnings'])

    def test_repeated_headings_and_hidden_headings(self):
        text = '<!--\n==not a section==\n-->\n{{x|\n==also hidden==\n}}\n==Gallery==\nA\n==Gallery==\nB'
        result = fandom.parse(text)
        self.assertEqual(len(result['sections']), 3)
        self.assertNotEqual(result['sections'][1]['locator'], result['sections'][2]['locator'])
        self.assertEqual(result['sections'][2]['heading_path'], ['Gallery'])

    def test_self_closing_reference_cannot_swallow_sections(self):
        text = 'A<ref name="ep"/>\n==Biography==\nB\n==Manga==\nC<ref name="ep">citation</ref>'
        result = fandom.parse(text)
        self.assertEqual([item['heading_path'] for item in result['sections']], [[], ['Biography'], ['Manga']])
        refs = [block for section in result['sections'] for block in section['blocks'] if block['kind'] == 'REFERENCE']
        self.assertEqual(len(refs), 2)
        self.assertEqual(refs[0]['raw'], '<ref name="ep"/>')
        self.assertFalse(result['parse_warnings'])

    def test_unclosed_markup_visible(self):
        result = fandom.parse('Text {{unclosed\n<ref>missing ending')
        self.assertEqual(result['parse_status'], 'PARTIAL')
        self.assertTrue(any('Unclosed template' in item for item in result['parse_warnings']))
        self.assertTrue(any('Unclosed reference' in item for item in result['parse_warnings']))
        self.assertIn('{{unclosed', result['sections'][0]['text'])

    def test_source_retained_exactly_unicode_and_line_endings(self):
        text = '日本語\r\n[[Hilda]] &amp; text\n'
        value = sample(text)
        self.assertEqual(value['source_text'], text)
        self.assertEqual(value['content_sha256'], core.sha(text.encode('utf-8')))

    def test_live_xml_fixture(self):
        fixture = core.ROOT / 'reference/working/fandom-export-test/Outlaw+Star+Wiki-20261026234357.xml'
        if not fixture.exists():
            fixture = core.ROOT / 'reference/cache/context/fandom/payloads/d1bec92374e524b1928121a86beb4b31d812ee789effcd7408e18d5aa11b89e5.bin'
        if not fixture.exists():
            self.skipTest('Local-only pilot XML unavailable; synthetic tests still run')
        raw = fixture.read_bytes()
        self.assertEqual(core.sha(raw), 'd1bec92374e524b1928121a86beb4b31d812ee789effcd7408e18d5aa11b89e5')
        captures = fandom.from_xml(raw)
        self.assertEqual({item['title']: len(item['source_text']) for item in captures},
                         {'Horus': 452, 'Hilda': 18661, 'Outlaw Star (ship)': 12281})
        for item in captures:
            core.check_capture(item)
            api = fandom.from_api(api_data(item['source_text'], item['title'], int(item['remote_revision_id']),
                                          int(item['remote_page_id'])), item['title'])
            self.assertEqual(item['content_sha256'], api['content_sha256'])
        hilda = next(item for item in captures if item['title'] == 'Hilda')
        self.assertTrue(any('Manga' in '/'.join(section['heading_path']) for section in hilda['sections']))

    def test_xml_rejects_entities_wrong_site_and_history(self):
        for raw in (b'<!DOCTYPE x [<!ENTITY y "x">]><mediawiki/>',
                    '<!DOCTYPE x [<!ENTITY y "x">]><mediawiki/>'.encode('utf-16'),
                    b'<html>Challenge</html>',
                    b'<mediawiki><siteinfo><base>https://other.invalid/wiki/Main</base></siteinfo></mediawiki>'):
            with self.assertRaises(ValueError): fandom.from_xml(raw)
        raw = b'<mediawiki><siteinfo><base>https://outlawstar.fandom.com/wiki/Main</base></siteinfo><page><title>Horus</title><ns>0</ns><revision/><revision/></page></mediawiki>'
        with self.assertRaises(ValueError): fandom.from_xml(raw)


class TransportTests(unittest.TestCase):
    def client(self, responses):
        self.calls, self.waits = [], []
        def send(url):
            self.calls.append(url)
            value = responses.pop(0)
            if isinstance(value, Exception): raise value
            return value
        return fandom.Client(send=send, sleep=self.waits.append, clock=lambda: 0)

    @staticmethod
    def response(data):
        return 200, {'Content-Type': 'application/json'}, json.dumps(data).encode()

    def test_selected_api_request_and_redirect_identity(self):
        data = api_data()
        data['query']['redirects'] = [{'from': 'Horus alias', 'to': 'Horus'}]
        client = self.client([self.response(data)])
        capture, raw, info = client.query('Horus alias')
        self.assertEqual(capture['document_key'], 'fandom:outlawstar:page:2691')
        self.assertEqual(capture['requested'], ['Horus alias'])
        self.assertIn('rvslots=main', self.calls[0])
        self.assertEqual(info['raw_sha256'], core.sha(raw))

    def test_denial_stops_without_retry_or_alternate(self):
        client = self.client([(403, {}, b'')])
        with self.assertRaises(fandom.AccessError) as caught: client.query('Horus')
        self.assertEqual(caught.exception.outcome, 'DENIED')
        self.assertEqual(len(self.calls), 1)

    def test_html_and_malformed_json_are_not_articles(self):
        for response in ((200, {'content-type': 'text/html'}, b'<html>challenge</html>'),
                         (200, {'content-type': 'application/json'}, b'<html>challenge</html>'),
                         self.response({'error': 'bad shape'}),
                         self.response({'query': {'pages': []}})):
            client = self.client([response])
            with self.assertRaises(fandom.AccessError) as caught: client.query('Horus')
            self.assertEqual(caught.exception.outcome, 'INVALID_RESPONSE')

    def test_maxlag_and_rate_limit_backoff_is_bounded(self):
        client = self.client([self.response({'error': {'code': 'maxlag'}}),
                              (429, {'Retry-After': '4'}, b''), self.response(api_data())])
        self.assertEqual(client.query('Horus')[0]['title'], 'Horus')
        self.assertEqual(len(self.calls), 3)
        self.assertIn(4, self.waits)
        client = self.client([(503, {}, b'')] * 3)
        with self.assertRaises(fandom.AccessError) as caught: client.query('Horus')
        self.assertEqual(caught.exception.outcome, 'RETRY_EXHAUSTED')
        client = self.client([(429, {'Retry-After': '600'}, b'')])
        with self.assertRaises(fandom.AccessError): client.query('Horus')
        self.assertEqual(len(self.calls), 1)

    def test_network_failure_retry_and_missing_title(self):
        client = self.client([fandom.AccessError('RETRY_EXHAUSTED', 'network'), self.response(api_data())])
        self.assertEqual(client.query('Horus')[0]['title'], 'Horus')
        client = self.client([self.response({'query': {'pages': [{'title': 'Absent', 'missing': True}]}})])
        with self.assertRaises(fandom.AccessError) as caught: client.query('Absent')
        self.assertEqual(caught.exception.outcome, 'NOT_FOUND')

    def test_explicit_titles_and_endpoint_boundary(self):
        for title in ('', '../x|Hilda', 'Special:AllPages', 'Horus#Heading', 'Horus\nHilda'):
            with self.assertRaises(ValueError): fandom.title_check(title)
        with self.assertRaises(ValueError): fandom.transport('https://other.invalid/api.php')
        with self.assertRaises(fandom.AccessError):
            fandom.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.invalid')


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempdir()
        self.base = Path(self.temp.name) / 'cache'
        self.store = core.Store(self.base)

    def tearDown(self): self.temp.cleanup()

    def put(self, value=None, raw=b'payload'):
        return self.store.put(value or sample(), raw, receipt(raw))

    def test_repeat_api_xml_capture_deduplicates_snapshot(self):
        key = self.put()
        value = sample()
        value['capture_method'] = 'FANDOM_XML'
        self.store.put(value, b'xml', receipt(b'xml', 'FANDOM_XML'))
        self.assertEqual(self.store.verify(), 1)
        self.assertEqual(len(self.store.manifest()['snapshots'][key]['receipts']), 2)
        self.assertEqual(len(list((self.base / 'snapshots').iterdir())), 1)

    def test_changed_revision_retains_pinned_snapshot(self):
        old = self.put()
        newer = self.put(sample('New article.', revision=9440))
        self.assertNotEqual(old, newer)
        self.assertEqual(self.store.verify(), 2)
        self.assertEqual(self.store.load(old)['source_text'], 'A short article.')
        self.assertEqual(self.store.lookup('Horus')['version_key'], 'revision:9440')
        self.put(sample())
        self.assertEqual(self.store.lookup('Horus')['version_key'], 'revision:9440')

    def test_same_revision_changed_text_refused(self):
        self.put()
        before = (self.base / 'manifest.json').read_bytes()
        with self.assertRaises(ValueError): self.put(sample('Changed revision text.'))
        self.assertEqual((self.base / 'manifest.json').read_bytes(), before)
        self.assertEqual(self.store.lookup('Horus')['source_text'], 'A short article.')

    def test_reparse_preserves_raw_snapshot_and_prior_parser_result(self):
        key = self.put()
        snapshot = self.base / 'snapshots' / key
        before = {path.name: path.read_bytes() for path in snapshot.iterdir()}
        def updated(text): return fandom.parse(text) | {'parser_version': 'test-v2'}
        self.store.reparse(key, updated)
        self.assertEqual({path.name: path.read_bytes() for path in snapshot.iterdir()}, before)
        self.assertEqual(len(self.store.manifest()['snapshots'][key]['parses']), 2)
        self.assertEqual(self.store.lookup('Horus')['parser_version'], 'test-v2')
        self.assertEqual(self.store.verify(), 1)
        def changed(text): return updated(text) | {'parse_status': 'PARTIAL', 'parse_warnings': ['changed']}
        with self.assertRaises(ValueError): self.store.reparse(key, changed)

    def test_denied_attempt_does_not_replace_success(self):
        self.put()
        before = (self.base / 'manifest.json').read_bytes()
        self.store.attempt('DENIED', ['Horus'], 'API HTTP 403')
        self.assertEqual((self.base / 'manifest.json').read_bytes(), before)
        self.assertEqual(self.store.verify(), 1)

    def test_corrupt_snapshot_or_payload_rejected(self):
        key = self.put()
        source = self.base / 'snapshots' / key / 'source.txt'
        source.write_text('corrupt', encoding='utf-8')
        with self.assertRaises(ValueError): self.store.verify()
        source.write_text('A short article.', encoding='utf-8')
        raw = next((self.base / 'payloads').iterdir())
        raw.write_bytes(b'bad')
        with self.assertRaises(ValueError): self.store.verify()

    def test_interrupted_promotion_cleans_only_owned_temp(self):
        sentinel = self.base / 'keep.txt'
        self.base.mkdir()
        sentinel.write_text('keep')
        original = core.os.replace
        def fail_stage(source, destination):
            if Path(source).is_dir(): raise OSError('simulated interruption')
            return original(source, destination)
        with patch('core.os.replace', side_effect=fail_stage):
            with self.assertRaises(OSError): self.put()
        self.assertEqual(sentinel.read_text(), 'keep')
        self.assertFalse(list(self.base.glob('.pending-*')))
        self.assertFalse((self.base / 'manifest.json').exists())

    def test_lock_and_paths(self):
        for path in ('../outside', '/absolute'):
            with self.assertRaises(ValueError): self.store.path(path)
        with core.writer(self.base):
            with self.assertRaises(OSError):
                with core.writer(self.base): pass
        self.put()
        self.assertEqual(self.store.verify(), 1)


class TableTests(unittest.TestCase):
    def setUp(self):
        self.tables = {name: [] for name in core.FIELDS}
        def row(name, **values): return dict.fromkeys(core.FIELDS[name], '') | values
        self.tables['subjects'] = [row('subjects', subject_id='horus', display_name='Horus', subject_type='SHIP', identity_status='ESTABLISHED')]
        source = sample()
        self.tables['sources'] = [row('sources', source_id='CTXSRC-000001', **{key: str(source[key]) if not isinstance(source[key], list) else '; '.join(source[key]) for key in core.FIELDS['sources'] if key in source},
                                      notes='License not declared in synthetic response.')]
        self.tables['context'] = [row('context', context_id='CTX-000001', source_id='CTXSRC-000001', source_locator='DOCUMENT',
                                      summary='A proposed source paraphrase.', claim_kind='DESCRIPTION', continuity='ANIME',
                                      review_status='DRAFT', evidence_status='SECONDARY_ONLY', research_priority='NORMAL',
                                      authored_by='Test', authored_utc='2026-10-26T00:00:00Z')]
        self.tables['links'] = [row('links', link_id='CTXLINK-000001', context_id='CTX-000001', relation='ABOUT', target_type='SUBJECT', target_id='horus')]

    def validate(self): return core.validate_tables(self.tables, image_keys={'EP-04:847840'}, episode_ids={'EP-04'})

    def test_valid_draft_is_not_auto_checked(self):
        self.assertEqual(self.validate(), [])
        self.assertEqual(self.tables['context'][0]['review_status'], 'DRAFT')

    def test_checked_and_primary_states_require_provenance(self):
        item = self.tables['context'][0]
        item.update(review_status='SOURCE_CHECKED', evidence_status='PRIMARY_CORROBORATED')
        errors = self.validate()
        self.assertTrue(any('reviewer' in error for error in errors))
        self.assertTrue(any('assessment' in error for error in errors))
        item.update(source_checked_by='Test', source_checked_utc='2026-10-26T00:00:00Z', evidence_status='SECONDARY_ONLY')
        self.assertEqual(self.validate(), [])

    def test_unknown_continuity_priority_and_utc(self):
        self.tables['context'][0].update(continuity='UNKNOWN', research_priority='HIGH', authored_utc='2026-10-26T00:00:00')
        self.assertTrue(any('UTC' in error for error in self.validate()))
        self.assertTrue(any('uncertainty' in error for error in self.validate()))

    def test_wrong_grain_and_dangling_targets(self):
        self.tables['sources'].append(dict(self.tables['sources'][0], source_id='CTXSRC-000002'))
        self.tables['links'].append(dict(self.tables['links'][0], link_id='CTXLINK-000002', relation='MENTIONS', target_id='horus'))
        self.tables['links'].append(dict(self.tables['links'][0], link_id='CTXLINK-000003', relation='CONTEXT_FOR_IMAGE', target_type='IMAGE', target_id='EP-04:missing'))
        errors = self.validate()
        self.assertTrue(any('duplicate source' in error for error in errors))
        self.assertTrue(any('ABOUT/MENTIONS' in error for error in errors))
        self.assertTrue(any('unvalidated image' in error for error in errors))

    def test_headers_match_document_and_wrong_csv_headers_fail(self):
        import re
        contract = (core.ROOT / 'reference/indexes/context/README.md').read_text('utf-8')
        for name, fields in core.FIELDS.items():
            section = re.search(r'### ' + name + r'\.csv\n(.*?)(?=\n### |\n## |\Z)', contract, re.S)[1]
            documented = re.findall(r'^\| `([a-z_0-9]+)` \|', section, re.M)
            self.assertEqual(documented, fields)
        with tempdir() as directory:
            for name, fields in core.FIELDS.items():
                with (Path(directory) / (name + '.csv')).open('w', encoding='utf-8', newline='') as stream:
                    writer = csv.DictWriter(stream, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(self.tables[name])
            self.assertEqual(core.read_tables(directory), self.tables)
            (Path(directory) / 'links.csv').write_text('wrong,header\n')
            with self.assertRaises(ValueError): core.read_tables(directory)

    def test_missing_pinned_snapshot_and_invalid_evidence_anchor(self):
        with tempdir() as directory:
            errors = core.validate_tables(self.tables, store=core.Store(Path(directory) / 'cache'))
            self.assertTrue(any('pinned snapshot' in error for error in errors))
        self.tables['links'].append(dict(self.tables['links'][0], link_id='CTXLINK-000002', relation='CHECKED_AGAINST',
                                         target_type='EVIDENCE', target_id='docs/canon-policy.md#missing', notes='test limit'))
        self.assertTrue(any('anchor' in error for error in self.validate()))

    def test_wrong_source_method_and_failed_parser_cannot_be_checked(self):
        self.tables['sources'][0].update(capture_method='ANIMEHISTORY_HTML', parse_status='FAILED', parse_warnings='unreadable')
        self.tables['context'][0].update(review_status='SOURCE_CHECKED', source_checked_by='Test', source_checked_utc='2026-10-26T00:00:00Z')
        errors = self.validate()
        self.assertTrue(any('IDs/method' in error for error in errors))
        self.assertTrue(any('parse limits' in error for error in errors))

    def test_invalid_context_id_is_diagnostic_not_crash(self):
        self.tables['context'][0]['context_id'] = 'CTX-bad'
        self.tables['context'].append(dict(self.tables['context'][0], context_id='CTX-000002'))
        self.tables['links'] = [dict.fromkeys(core.FIELDS['links'], '') | {
            'link_id': 'CTXLINK-000001', 'context_id': 'CTX-bad', 'relation': 'SAME_ASSERTION_AS',
            'target_type': 'CONTEXT', 'target_id': 'CTX-000002'}]
        self.assertTrue(self.validate())

    def test_source_locator_and_pinned_snapshot_validation(self):
        with tempdir() as directory:
            store = core.Store(Path(directory) / 'cache')
            store.put(sample(), b'payload', receipt())
            self.assertEqual(core.validate_tables(self.tables, store=store), [])
            self.tables['context'][0]['source_locator'] = 'SECTION:9999'
            self.assertTrue(any('locator' in error for error in core.validate_tables(self.tables, store=store)))


if __name__ == '__main__': unittest.main()
