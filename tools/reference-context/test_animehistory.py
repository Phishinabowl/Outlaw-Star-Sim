"""Bounded HTML/discovery/robots and shared-core compatibility regression fixtures."""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch

import animehistory as ah
import context_tool
import core
from test_context import sample, receipt, tempdir
import test_context

CHAR = ah.HUB + 'characters/1050/'
LORE = ah.HUB + 'lore/ships-casters-tao/'


def document(body, url=CHAR):
    return '<!DOCTYPE html><html><head><title>Test | AnimeHistory.org</title><link rel="canonical" href="' + url + '"></head><body>' + body + '</body></html>'


def character():
    return document('<div class="main-content"><article class="char-dossier">'
                    '<h1 class="char-dossier-title">Pilot <span class="anime-char-spoiler-pill">SPOILER!</span></h1>'
                    '<p class="char-dossier-meta">Ship operator</p><div class="char-dossier-bio">'
                    'First sentence.<br>Second sentence &amp; context. <a href="/anime/outlaw-star/lore/ships-casters-tao/#lore-entry-7">Related source</a>'
                    '</div><nav><a href="/login/">Login bait</a></nav>'
                    '<script>Never include this text.</script></article></div>')


def lore():
    return document('<div class="main-content"><section class="lore-section">'
                    '<h3 class="lore-section-label">Ship controls</h3>'
                    '<article class="lore-entry" id="lore-entry-7"><h4 class="lore-entry-title">Mechanism</h4>'
                    '<div class="lore-entry-body">A sourced description.</div>'
                    '<div class="lore-entry-tell lore-entry-tell--analysis"><div class="lore-entry-tell-label">Why it matters</div>'
                    '<div class="lore-entry-tell-body">An editorial interpretation.</div></div>'
                    '<p class="lore-entry-debut"><a href="/anime/outlaw-star/#ep-4247">Episode 4</a></p></article>'
                    '<article class="lore-entry" id="lore-entry-8"><h4 class="lore-entry-title">Mechanism</h4>'
                    '<div class="lore-entry-body">A separate mechanism.</div></article></section></div>', LORE)


def response(text, url, media='text/html; charset=UTF-8', status=200):
    return status, {'Content-Type': media}, text.encode('utf-8'), url


class HTMLTests(unittest.TestCase):
    def test_character_boundaries_entities_and_no_scripts_navigation(self):
        value = ah.capture(character(), CHAR)
        core.check_capture(value)
        self.assertEqual(value['parse_status'], 'COMPLETE')
        text = value['sections'][0]['text']
        self.assertIn('First sentence. Second sentence & context.', text)
        self.assertNotIn('Never include', text)
        self.assertNotIn('Login bait', str(value['sections']))
        self.assertNotIn('SPOILER!', str(value['sections']))
        self.assertEqual(value['remote_revision_id'], '')
        self.assertEqual(value['version_url'], '')
        self.assertEqual(value['source_text'], character())

    def test_lore_analysis_and_repeated_title_boundaries(self):
        value = ah.capture(lore(), LORE)
        sections = value['sections']
        self.assertEqual(len(sections), 2)
        self.assertEqual(sections[0]['heading_path'], sections[1]['heading_path'])
        self.assertNotEqual(sections[0]['locator'], sections[1]['locator'])
        self.assertEqual(sections[0]['blocks'][1]['source_role'], 'SOURCE_INTERPRETATION')
        self.assertEqual(ah.selection(value, LORE + '#lore-entry-8'), ['LORE:lore-entry-8'])
        with self.assertRaises(ValueError): ah.selection(value, LORE + '#missing')

    def test_missing_layout_and_challenge_never_become_success(self):
        for text in ('<html><title>Just a moment</title></html>', document('<div class="navigation">No article</div>')):
            with self.assertRaises(ValueError): ah.capture(text, CHAR)
        value = character().replace('class="char-dossier-bio"', 'class="changed-bio"')
        parsed = ah.parse(value, CHAR)
        self.assertIn(parsed['parse_status'], ('PARTIAL', 'FAILED'))
        self.assertTrue(parsed['parse_warnings'])

    def test_duplicate_ids_and_wrong_canonical_refused(self):
        with self.assertRaises(ValueError): ah.capture(lore().replace('lore-entry-8', 'lore-entry-7'), LORE)
        with self.assertRaises(ValueError): ah.capture(character(), LORE)

    def test_urls_are_bounded_and_anchors_share_identity(self):
        self.assertEqual(ah.canonical(ah.HUB + '#characters'), ah.canonical(ah.HUB + '#lore'))
        self.assertEqual(ah.canonical('https://www.animehistory.org/anime/outlaw-star/'), ah.HUB)
        for url in ('http://animehistory.org/anime/outlaw-star/', ah.BASE + '/php/internal.php',
                    ah.BASE + '/anime/other/', ah.HUB + '?token=secret', ah.HUB + '%2e%2e/',
                    'https://animehistory.org.evil.invalid/anime/outlaw-star/'):
            with self.assertRaises(ValueError): ah.canonical(url)

    def test_cached_hub_structure_and_episode_candidates(self):
        path = core.ROOT / 'reference/cache/animehistory/series.html'
        if not path.exists(): self.skipTest('Local-only hub fixture unavailable')
        result = ah.capture(path.read_text('utf-8'), ah.HUB)
        sections = result['sections']
        self.assertEqual(len([item for item in sections if item['locator'].startswith('EPISODE:')]), 26)
        self.assertEqual(len(ah.selection(result, ah.HUB + '#characters')), 24)
        self.assertEqual(ah.selection(result, ah.HUB + '#ep-4247'), ['EPISODE:04'])
        episode = next(item for item in sections if item['locator'] == 'EPISODE:04')
        self.assertEqual(episode['episode_id_hint'], 'EP-04')
        self.assertTrue(any('/lore/' in link['url'] for link in episode['outbound_links']))


class ClientTests(unittest.TestCase):
    def make(self, replies, robots='User-agent: *\nAllow: /\nDisallow: /php/\n'):
        self.calls, self.waits = [], []
        queue = [response(robots, ah.BASE + '/robots.txt', 'text/plain')] + replies
        def send(url, policy):
            self.calls.append(url)
            return queue.pop(0)
        return ah.Client(send=send, sleep=self.waits.append, clock=lambda: 0)

    def test_robots_first_and_html_response_contract(self):
        client = self.make([response(character(), CHAR)])
        value, raw, info = client.query(CHAR + '#anything')
        self.assertEqual(self.calls, [ah.BASE + '/robots.txt', CHAR])
        self.assertEqual(core.sha(raw), info['raw_sha256'])
        self.assertEqual(info['encoding'], 'UTF-8')
        self.assertIn('robots', info)
        self.assertEqual(value['site'], 'ANIMEHISTORY')

    def test_robots_denial_stops_before_article(self):
        client = self.make([], 'User-agent: *\nDisallow: /anime/\n')
        with self.assertRaises(core.AccessError) as caught: client.query(CHAR)
        self.assertEqual(caught.exception.outcome, 'DENIED')
        self.assertEqual(len(self.calls), 1)

    def test_invalid_robots_or_html_media_stops(self):
        client = self.make([], '<html>Challenge</html>')
        with self.assertRaises(core.AccessError): client.query(CHAR)
        self.assertEqual(len(self.calls), 1)
        client = self.make([response('{}', CHAR, 'application/json')])
        with self.assertRaises(core.AccessError): client.query(CHAR)

    def test_missing_denied_and_retry_boundaries(self):
        for status, expected in ((404, 'NOT_FOUND'), (403, 'DENIED')):
            client = self.make([response('', CHAR, status=status)])
            with self.assertRaises(core.AccessError) as caught: client.query(CHAR)
            self.assertEqual(caught.exception.outcome, expected)
        client = self.make([response('', CHAR, status=503)] * 3)
        with self.assertRaises(core.AccessError) as caught: client.query(CHAR)
        self.assertEqual(caught.exception.outcome, 'RETRY_EXHAUSTED')
        self.assertEqual(len(self.calls), 4)
        self.assertIn(4, self.waits)

    def test_encoding_and_backoff_success(self):
        encoded = character().encode('utf-16')
        client = self.make([(429, {'Retry-After': '3'}, b'', CHAR),
                            (200, {'Content-Type': 'text/html; charset=UTF-16'}, encoded, CHAR)])
        value, raw, info = client.query(CHAR)
        self.assertEqual(value['source_text'], character())
        self.assertEqual(raw, encoded)
        self.assertIn(3, self.waits)
        self.assertEqual(info['encoding'], 'UTF-16')
        client = self.make([(200, {'Content-Type': 'text/html; charset=UTF-8'}, b'\xff', CHAR)])
        with self.assertRaises(core.AccessError): client.query(CHAR)

    def test_redirect_policy(self):
        guard = ah.GuardedRedirect(None)
        with self.assertRaises(core.AccessError):
            guard.redirect_request(None, None, 302, '', {}, ah.BASE + '/login/')
        policy = ah.RobotFileParser()
        policy.parse(['User-agent: *', 'Disallow: /anime/'])
        with self.assertRaises(core.AccessError):
            ah.GuardedRedirect(policy).redirect_request(None, None, 302, '', {}, CHAR)

    def test_discovery_deduplicates_only_url_inventory(self):
        prefix = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        character_map = prefix + '<url><loc>' + CHAR + '</loc></url></urlset>'
        lore_map = prefix + ''.join('<url><loc>' + LORE + '</loc></url>' for _ in range(3)) + '</urlset>'
        client = self.make([response(character_map, ah.BASE + '/sitemap-characters.php', 'application/xml'),
                            response(lore_map, ah.BASE + '/sitemap-lore.php', 'application/xml')])
        result = client.discover()
        self.assertEqual(result['articles'], sorted([CHAR, LORE]))
        self.assertEqual(result['sitemaps'][1]['selected_entries'], 3)
        self.assertEqual(len(self.calls), 3)
        self.assertFalse(any('/anime/outlaw-star/' in url for url in self.calls))
        with self.assertRaises(core.AccessError): ah.sitemap_urls('<!DOCTYPE x><urlset/>')


class IntegrationTests(unittest.TestCase):
    def test_anchor_cli_requests_fetch_one_document(self):
        with tempdir() as directory:
            from argparse import Namespace
            value = ah.capture(lore(), LORE)
            raw = lore().encode('utf-8')
            args = Namespace(command='animehistory-fetch', url=[LORE + '#lore-entry-7', LORE + '#lore-entry-8'], refresh=False)
            with patch.object(context_tool, 'ANIME_CACHE', Path(directory) / 'cache'), \
                    patch.object(ah.Client, 'query', return_value=(value, raw, receipt(raw) | {'requested': [LORE]})) as query, \
                    patch('builtins.print'):
                self.assertEqual(context_tool.run(args), 0)
                self.assertEqual(query.call_count, 1)
                self.assertEqual(context_tool.run(args), 0)
                self.assertEqual(query.call_count, 1)

    def test_shared_site_caches_and_changed_html_retention(self):
        with tempdir() as directory:
            fandom_store = core.Store(Path(directory) / 'fandom')
            html_store = core.Store(Path(directory) / 'animehistory')
            fandom_store.put(sample(), b'api', receipt(b'api'))
            html = character()
            first = ah.capture(html, CHAR)
            old = html_store.put(first, html.encode(), receipt(html.encode()))
            new_html = html.replace('First sentence.', 'A changed sentence.')
            second = ah.capture(new_html, CHAR)
            html_store.put(second, new_html.encode(), receipt(new_html.encode()))
            caches = core.CacheSet([fandom_store, html_store])
            self.assertEqual(caches.verify(), 3)
            self.assertEqual(caches.load(old)['content_sha256'], first['content_sha256'])
            self.assertEqual(caches.load(core.Store.key(second['document_key'], second['version_key']))['site'], 'ANIMEHISTORY')
            self.assertNotEqual(first['version_key'], second['version_key'])
            self.assertEqual(first['document_key'], second['document_key'])

    def test_wrong_url_digest_is_refused(self):
        value = ah.capture(character(), CHAR)
        value['document_key'] = 'animehistory:url:' + '0' * 64
        with self.assertRaises(ValueError): core.check_capture(value)

    def test_offline_show_uses_selected_locator_and_preserves_cache(self):
        from argparse import Namespace
        with tempdir() as directory:
            base = Path(directory) / 'cache'
            store = core.Store(base)
            text = lore()
            value = ah.capture(text, LORE)
            store.put(value, text.encode(), receipt(text.encode()) | {'requested': [LORE]})
            before = (base / 'manifest.json').read_bytes()
            args = Namespace(command='show', site='animehistory', article=LORE, locator=['LORE:lore-entry-7'])
            with patch.object(context_tool, 'ANIME_CACHE', base), patch('builtins.print') as printer, \
                    patch.object(ah.Client, 'query', side_effect=AssertionError('No network permitted')):
                self.assertEqual(context_tool.run(args), 0)
                import json
                output = json.loads(printer.call_args[0][0])
                self.assertEqual(output['content'][0]['locator'], 'LORE:lore-entry-7')
                args.locator = ['absent']
                with self.assertRaises(ValueError): context_tool.run(args)
            self.assertEqual((base / 'manifest.json').read_bytes(), before)

    def test_mixed_site_source_rows_validate_and_preserve_authored_values(self):
        fixtures = test_context.TableTests()
        fixtures.setUp()
        tables = fixtures.tables
        with tempdir() as directory:
            fandom_store = core.Store(Path(directory) / 'fandom')
            html_store = core.Store(Path(directory) / 'animehistory')
            fandom_store.put(sample(), b'api', receipt(b'api'))
            html = character()
            value = ah.capture(html, CHAR)
            html_store.put(value, html.encode(), receipt(html.encode()))
            source = {field: '' for field in core.FIELDS['sources']}
            source.update({key: ('; '.join(value[key]) if isinstance(value[key], list) else value[key])
                           for key in source if key in value})
            source.update(source_id='CTXSRC-000002', notes='No license declared in this fixture.')
            tables['sources'].append(source)
            tables['context'].append(dict(tables['context'][0], context_id='CTX-000002',
                                           source_id='CTXSRC-000002', source_locator='CHARACTER:PROFILE'))
            before = copy.deepcopy(tables)
            errors = core.validate_tables(tables, store=core.CacheSet([fandom_store, html_store]))
            self.assertEqual(errors, [])
            self.assertEqual(tables, before)


if __name__ == '__main__': unittest.main()
