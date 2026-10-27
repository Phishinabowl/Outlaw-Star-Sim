"""Selected public AnimeHistory text; explicit URLs, robots checks, no internal endpoints/media."""
from dataclasses import dataclass, field
from html.parser import HTMLParser
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urldefrag, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

from core import AccessError, SCHEMA, check_capture, now, sha

BASE = 'https://animehistory.org'
HUB = BASE + '/anime/outlaw-star/'
AGENT = 'OutlawStarReferenceContext/0.1 (bounded read-only research; no media)'
PARSER = 'animehistory-html-2'
MAX_BYTES = 8 * 1024 * 1024
MAX_URLS = 10
META_PATHS = {'/robots.txt', '/sitemap-characters.php', '/sitemap-lore.php'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
SKIP = {'script', 'style', 'nav', 'form', 'aside', 'footer', 'svg', 'noscript'}


def canonical(url, metadata=False):
    parts = urlsplit(url)
    if (parts.scheme != 'https' or parts.hostname not in ('animehistory.org', 'www.animehistory.org')
            or parts.username or parts.password or parts.port not in (None, 443) or parts.query):
        raise ValueError('Only selected public AnimeHistory HTTPS URLs without queries are allowed')
    path = parts.path
    if path != unquote(path) or re.search(r'[\x00-\x20\\]', path):
        raise ValueError('Encoded/unsafe article path refused')
    article = re.fullmatch(r'/anime/outlaw-star/(?:characters/[1-9]\d*/|lore/[a-z0-9]+(?:-[a-z0-9]+)*/)?', path)
    if not article and not (metadata and path in META_PATHS):
        raise ValueError('URL is outside selected Outlaw Star articles/discovery metadata')
    if parts.fragment and not re.fullmatch(r'[A-Za-z0-9_-]{1,120}', parts.fragment):
        raise ValueError('Unsupported source anchor')
    # Both host spellings publish the same bare-host canonical links.
    return BASE + path


def kind(url):
    path = urlsplit(canonical(url)).path
    return 'CHARACTER' if '/characters/' in path else 'LORE' if '/lore/' in path else 'HUB'


class GuardedRedirect(HTTPRedirectHandler):
    max_redirections = 2
    max_repeats = 1

    def __init__(self, robots):
        super().__init__()
        self.robots = robots

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        try:
            destination = canonical(newurl, metadata=True)
        except ValueError as exc:
            raise AccessError('DENIED', 'Redirect outside selected public paths refused') from exc
        if req and urlsplit(req.full_url).path == '/robots.txt' and urlsplit(destination).path != '/robots.txt':
            raise AccessError('DENIED', 'Robots request redirected outside robots guidance')
        if self.robots and not self.robots.can_fetch(AGENT, destination):
            raise AccessError('DENIED', 'Redirect disallowed by robots guidance')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def transport(url, robots=None):
    canonical(url, metadata=True)
    request = Request(url, headers={'User-Agent': AGENT, 'Accept': 'text/html,application/xml,text/plain'})
    try:
        with build_opener(GuardedRedirect(robots)).open(request, timeout=30) as response:
            final = canonical(response.url, metadata=True)
            raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise AccessError('INVALID_RESPONSE', 'Response exceeds 8 MiB bound')
            return response.status, dict(response.headers), raw, final
    except HTTPError as exc:
        return exc.code, dict(exc.headers), b'', url
    except (URLError, TimeoutError, OSError) as exc:
        raise AccessError('RETRY_EXHAUSTED', 'Network/timeout failure') from exc


class Client:
    def __init__(self, send=transport, sleep=time.sleep, clock=time.monotonic):
        self.send, self.sleep, self.clock = send, sleep, clock
        self.last, self.robots, self.robots_receipt = None, None, None

    def request(self, url):
        for attempt in range(3):
            if self.last is not None:
                self.sleep(max(0, 1 - (self.clock() - self.last)))
            self.last = self.clock()
            try:
                status, headers, raw, final = self.send(url, self.robots)
            except AccessError as exc:
                if exc.outcome != 'RETRY_EXHAUSTED' or attempt == 2:
                    raise
                self.sleep(2 ** (attempt + 1))
                continue
            canonical(final, metadata=True)
            if self.robots and not self.robots.can_fetch(AGENT, final):
                raise AccessError('DENIED', 'Final URL disallowed by robots guidance')
            if status in (401, 402, 403) or 300 <= status < 400:
                raise AccessError('DENIED', f'HTTP {status}; no alternate route attempted')
            if status == 404:
                raise AccessError('NOT_FOUND', 'Selected public page not found')
            if status == 429 or 500 <= status <= 599:
                if attempt == 2:
                    raise AccessError('RETRY_EXHAUSTED', f'HTTP {status}; retry bound reached')
                delay = next((value for key, value in headers.items() if key.lower() == 'retry-after'), '')
                if delay and (not str(delay).isdigit() or int(delay) > 60):
                    raise AccessError('RETRY_EXHAUSTED', 'Unsupported Retry-After; retry later')
                self.sleep(max(2 ** (attempt + 1), int(delay or 0)))
                continue
            if status != 200 or len(raw) > MAX_BYTES:
                raise AccessError('INVALID_RESPONSE', 'Unexpected status or oversized response')
            media = next((value for key, value in headers.items() if key.lower() == 'content-type'), '')
            match = re.search(r'charset\s*=\s*["\']?([\w-]+)', media, re.I)
            encoding = match[1] if match else 'utf-8'
            try:
                text = raw.decode(encoding, errors='strict')
            except (LookupError, UnicodeError) as exc:
                raise AccessError('INVALID_RESPONSE', 'Unknown encoding or undecodable response') from exc
            return text, raw, {'requested': [url], 'requested_url': url, 'final_url': final,
                               'raw_sha256': sha(raw), 'raw_bytes': len(raw), 'encoding': encoding,
                               'media_type': media, 'captured_utc': now(), 'capture_method': 'ANIMEHISTORY_HTML'}
        raise AccessError('RETRY_EXHAUSTED', 'Retry bound reached')

    def check_robots(self):
        if self.robots:
            return
        text, raw, info = self.request(BASE + '/robots.txt')
        if 'text/plain' not in info['media_type'].lower() or len(raw) > 65536 or not re.search(r'^User-agent:', text, re.M | re.I):
            raise AccessError('INVALID_RESPONSE', 'Robots guidance missing/malformed; no article requested')
        robots = RobotFileParser()
        robots.parse(text.splitlines())
        self.robots = robots
        self.robots_receipt = {'url': info['final_url'], 'raw_sha256': info['raw_sha256'],
                               'checked_utc': info['captured_utc'], 'text': text}

    def query(self, url):
        document = canonical(url)
        self.check_robots()
        if not self.robots.can_fetch(AGENT, document):
            raise AccessError('DENIED', 'Selected page disallowed by robots guidance')
        text, raw, info = self.request(document)
        if 'text/html' not in info['media_type'].lower():
            raise AccessError('INVALID_RESPONSE', 'Expected public HTML document')
        try:
            result = capture(text, info['final_url'])
        except (ValueError, KeyError) as exc:
            raise AccessError('INVALID_RESPONSE', 'Missing/mismatched public article identity') from exc
        info['requested'] = list(dict.fromkeys([document, result['canonical_url']]))
        info['requested_with_anchor'] = url
        info['robots'] = self.robots_receipt
        return result, raw, info

    def discover(self):
        """Read only the two advertised URL inventories. Never follow their articles."""
        self.check_robots()
        result = {'site': 'ANIMEHISTORY', 'articles': [], 'sitemaps': []}
        for path in ('/sitemap-characters.php', '/sitemap-lore.php'):
            url = BASE + path
            if not self.robots.can_fetch(AGENT, url):
                raise AccessError('DENIED', 'Sitemap disallowed by robots guidance')
            text, raw, info = self.request(url)
            if not any(value in info['media_type'].lower() for value in ('application/xml', 'text/xml')):
                raise AccessError('INVALID_RESPONSE', 'Expected XML sitemap')
            urls, count = sitemap_urls(text)
            result['articles'].extend(urls)
            result['sitemaps'].append({'url': url, 'sha256': sha(raw), 'selected_entries': count,
                                        'unique_selected_documents': len(urls)})
        result['articles'] = sorted(set(result['articles']))
        return result


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)
    parent: object = field(default=None, repr=False)

    def has(self, name):
        return name in self.attrs.get('class', '').split()

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def find(self, name):
        return next((node for node in self.walk() if node.has(name)), None)

    def text(self):
        if self.tag in SKIP or self.attrs.get('aria-hidden') == 'true' or self.has('anime-char-spoiler-pill'):
            return ''
        pieces = []
        for child in self.children:
            if isinstance(child, str):
                pieces.append(child)
            else:
                value = child.text()
                pieces.append(('\n' if child.tag in ('br', 'p', 'div', 'li', 'section', 'article') else '') + value)
        return re.sub(r'\s+', ' ', ''.join(pieces)).strip()


class Tree(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.root = Node('ROOT')
        self.stack = [self.root]
        self.mismatches = 0
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), parent=self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        match = next((index for index in range(len(self.stack) - 1, 0, -1) if self.stack[index].tag == tag), None)
        if match is not None:
            if match != len(self.stack) - 1:
                self.mismatches += 1
            del self.stack[match:]
        elif tag not in VOID:
            self.mismatches += 1

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def links(node, url):
    result, seen = [], set()
    for item in node.walk():
        if item.tag != 'a' or not item.attrs.get('href'):
            continue
        parent = item.parent
        hidden = False
        while parent and parent is not node:
            if parent.tag in SKIP:
                hidden = True
                break
            parent = parent.parent
        if hidden:
            continue
        target = urljoin(url, item.attrs['href'])
        parts = urlsplit(target)
        if parts.scheme not in ('https', 'http') or not parts.hostname or target in seen:
            continue
        seen.add(target)
        result.append({'kind': 'SOURCE_LINK', 'url': target, 'target': target,
                       'label': item.text(), 'source_href': item.attrs['href']})
    return result


def parse(text, url):
    """Known content containers only. Fail visibly rather than summarize navigation."""
    url = canonical(url)
    page_kind = kind(url)
    tree = Tree(text)
    main = tree.root.find('main-content')
    warnings, sections = [], []

    def add(node, locator, heading_path, content_nodes, anchor='', episode=''):
        if not node:
            return
        blocks = []
        for label, content, role in content_nodes:
            if not content:
                continue
            value = content.text()
            if not value:
                continue
            blocks.append({'kind': 'PROSE', 'locator': locator + f'/BLOCK:{len(blocks)+1:04d}',
                           'label': label, 'text': value, 'source_role': role})
        if not blocks:
            warnings.append('Empty expected content: ' + locator)
        sections.append({'locator': locator, 'heading_path': heading_path,
                         'text': '\n\n'.join((block['label'] + ': ' if block['label'] else '') + block['text'] for block in blocks),
                         'blocks': blocks, 'outbound_links': links(node, url),
                         'source_anchor': anchor, 'episode_id_hint': episode})

    if main:
        if page_kind == 'HUB':
            synopsis = main.find('anime-detail-dual-synopsis')
            add(synopsis, 'HUB:SYNOPSIS', ['Outlaw Star', 'Synopsis'], [('', synopsis, 'SOURCE_DESCRIPTION')])
            episodes = [node for node in main.walk() if node.has('ep-row')]
            for node in episodes:
                number = node.attrs.get('data-num', '')
                title = node.find('ep-title')
                if not re.fullmatch(r'[1-9]\d?', number) or not title:
                    warnings.append('Unrecognized episode identity')
                    continue
                add(node, 'EPISODE:' + number.zfill(2), ['Episodes', title.text()],
                    [('Synopsis', node.find('ep-synopsis'), 'SOURCE_DESCRIPTION')],
                    node.attrs.get('id', ''), 'EP-' + number.zfill(2))
                if not node.find('ep-synopsis') or not node.find('ep-synopsis').text():
                    warnings.append('Episode synopsis missing: ' + number)
            characters = [node for node in main.walk() if node.has('anime-char-row')]
            for index, node in enumerate(characters, 1):
                name = node.find('anime-char-name')
                profile = next((link['url'] for link in links(node, url) if '/characters/' in link['url']), '')
                character_id = re.search(r'/characters/(\d+)/', profile)
                locator = 'CHARACTER:' + character_id[1] if character_id else f'CHARACTER:ORDER:{index:04d}'
                if not name or not character_id:
                    warnings.append('Character identity/layout incomplete')
                if not node.find('anime-char-bio') or not node.find('anime-char-bio').text():
                    warnings.append('Character biography missing: ' + locator)
                add(node, locator, ['Characters', name.text() if name else 'Unknown'],
                    [('Role', node.find('anime-char-role'), 'SOURCE_LABEL'),
                     ('Biography', node.find('anime-char-bio'), 'SOURCE_DESCRIPTION')])
            lore_index = next((node for node in main.walk() if node.attrs.get('id') == 'lore'), None)
            add(lore_index, 'HUB:LORE_INDEX', ['Lore', 'Page index'],
                [('Available pages', lore_index.find('lore-page-list') if lore_index else None, 'SOURCE_INDEX')], 'lore')
            if not lore_index or not lore_index.find('lore-page-list'):
                warnings.append('Lore page index structure missing')
            if len(episodes) != 26 or len(characters) != 24:
                warnings.append('Hub coverage differs from pilot baseline (26 episodes / 24 characters)')
        elif page_kind == 'CHARACTER':
            dossier = main.find('char-dossier')
            bio = main.find('char-dossier-bio')
            title = main.find('char-dossier-title')
            add(dossier, 'CHARACTER:PROFILE', ['Character profile', title.text() if title else 'Unknown'],
                [('Role', main.find('char-dossier-meta'), 'SOURCE_LABEL'),
                 ('Biography', bio, 'SOURCE_DESCRIPTION')])
            if not dossier or not bio or not title:
                warnings.append('Character profile structure missing')

        if page_kind in ('CHARACTER', 'LORE'):
            entries = [node for node in main.walk() if node.has('lore-entry')]
            for node in entries:
                anchor = node.attrs.get('id', '')
                if not re.fullmatch(r'lore-entry-[1-9]\d*', anchor):
                    warnings.append('Lore entry anchor missing/changed')
                    anchor = f'unanchored-{len(sections)+1}'
                title = node.find('lore-entry-title')
                parent = node.parent
                while parent and not parent.has('lore-section') and not parent.has('char-mod--lore'):
                    parent = parent.parent
                group = parent.find('lore-section-label') if parent else None
                if group is None and parent:
                    group = parent.find('char-mod-head-title')
                content = [('Description', node.find('lore-entry-body'), 'SOURCE_DESCRIPTION')]
                for tell in [item for item in node.walk() if item.has('lore-entry-tell')]:
                    label = tell.find('lore-entry-tell-label')
                    if not label or not tell.find('lore-entry-tell-body'):
                        warnings.append('Lore commentary label/body missing: ' + anchor)
                    content.append((label.text() if label else 'Commentary', tell.find('lore-entry-tell-body'),
                                    'SOURCE_INTERPRETATION' if tell.has('lore-entry-tell--analysis') else
                                    'SOURCE_BREAKDOWN' if tell.has('lore-entry-tell--breakdown') else 'SOURCE_COMMENTARY'))
                content.append(('Episode pointer', node.find('lore-entry-debut'), 'SOURCE_EPISODE_POINTER'))
                add(node, 'LORE:' + anchor, [group.text() if group else 'Lore', title.text() if title else 'Unknown'],
                    content, anchor)
                if not title or not node.find('lore-entry-body'):
                    warnings.append('Lore entry title/body missing')
            if page_kind == 'LORE' and not entries:
                warnings.append('No expected lore entries found')
    else:
        warnings.append('Expected main-content container missing')

    locators = [section['locator'] for section in sections]
    if len(set(locators)) != len(locators):
        raise ValueError('Duplicate content locator; ambiguous source structure')
    if tree.mismatches or len(tree.stack) != 1:
        warnings.append('HTML nesting repaired; inspect source boundaries')
    if not sections:
        sections = [{'locator': 'DOCUMENT', 'heading_path': [], 'text': '', 'blocks': [], 'outbound_links': []}]
    failed = not main or not any(section['text'] for section in sections)
    return {'parser_version': PARSER, 'sections': sections, 'parse_status': 'FAILED' if failed else 'PARTIAL' if warnings else 'COMPLETE',
            'parse_warnings': list(dict.fromkeys(warnings))}


def capture(text, url):
    document = canonical(url)
    tree = Tree(text)
    expected = [node for node in tree.root.walk() if node.tag == 'link' and node.attrs.get('rel') == 'canonical']
    if len(expected) != 1 or canonical(urljoin(document, expected[0].attrs.get('href', ''))) != document:
        raise ValueError('Missing/mismatched canonical article URL')
    title_node = next((node for node in tree.root.walk() if node.tag == 'title'), None)
    if not title_node or not title_node.text():
        raise ValueError('Article title missing')
    digest = sha(text.encode('utf-8'))
    result = {'schema_version': SCHEMA, 'site': 'ANIMEHISTORY', 'outcome': 'OK',
              'title': title_node.text(), 'canonical_url': document,
              'document_key': 'animehistory:url:' + sha(document.encode('utf-8')),
              'version_key': 'sha256:' + digest, 'content_sha256': digest,
              'remote_page_id': '', 'remote_revision_id': '', 'remote_modified_utc': '',
              'version_url': '', 'captured_utc': now(), 'source_text': text,
              'capture_method': 'ANIMEHISTORY_HTML', 'license_name': '', 'license_url': '',
              'attribution_url': document, **parse(text, document)}
    if result['parse_status'] == 'FAILED':
        raise ValueError('Recognized article content missing; possible layout change or challenge')
    check_capture(result)
    return result


def sitemap_urls(text):
    if '\x00' in text or re.search(r'<!\s*(DOCTYPE|ENTITY)', text, re.I):
        raise AccessError('INVALID_RESPONSE', 'DTD/entities refused in sitemap')
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise AccessError('INVALID_RESPONSE', 'Invalid sitemap XML') from exc
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    if root.tag != ns + 'urlset':
        raise AccessError('INVALID_RESPONSE', 'Expected sitemap URL inventory')
    selected = []
    for item in root.findall(ns + 'url/' + ns + 'loc'):
        if item.text and '/anime/outlaw-star/' in item.text:
            try:
                selected.append(canonical(item.text))
            except ValueError as exc:
                raise AccessError('INVALID_RESPONSE', 'Unexpected selected sitemap URL') from exc
    return sorted(set(selected)), len(selected)


def selection(capture, requested_url):
    """Anchors select normalized sections; never create another cached document."""
    fragment = urlsplit(requested_url).fragment
    sections = capture['sections']
    if fragment == 'characters' and kind(capture['canonical_url']) == 'HUB':
        selected = [section for section in sections if section['locator'].startswith('CHARACTER:')]
    elif fragment == 'episodes' and kind(capture['canonical_url']) == 'HUB':
        selected = [section for section in sections if section['locator'].startswith('EPISODE:')]
    elif fragment == 'lore' and kind(capture['canonical_url']) == 'HUB':
        selected = [section for section in sections if section['locator'] == 'HUB:LORE_INDEX']
    elif fragment:
        selected = [section for section in sections if section.get('source_anchor') == fragment]
    else:
        selected = sections
    if not selected:
        raise ValueError('Requested anchor has no recognized content section; inspect the layout')
    return [section['locator'] for section in selected]
