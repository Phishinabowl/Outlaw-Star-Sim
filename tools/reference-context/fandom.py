"""Bounded anonymous MediaWiki reader and conservative wikitext structural adapter.

No browser automation, credentials, rendered-HTML scraping or template evaluation.
"""
import json
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET

from core import AccessError, SCHEMA, check_capture, now, sha

BASE = 'https://outlawstar.fandom.com'
API = BASE + '/api.php'
AGENT = 'OutlawStarReferenceContext/0.1 (bounded read-only research; no media)'
PARSER = 'fandom-wikitext-2'
MAX_BYTES = 8 * 1024 * 1024
MAX_TITLES = 10


def title_check(title):
    if (not isinstance(title, str) or not title.strip() or title != title.strip()
            or len(title) > 255 or re.search(r'[\x00-\x1f\x7f|#<>\[\]{}]', title)):
        raise ValueError('Invalid explicit article title')
    if ':' in title:
        raise ValueError('Only main-namespace articles are selected in Stage 2')
    return title


def article_url(title):
    return BASE + '/wiki/' + quote(title.replace(' ', '_'), safe='()')


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise AccessError('DENIED', 'HTTP redirect refused; only the documented API endpoint is permitted')


def transport(url):
    parts = urlsplit(url)
    if parts.scheme != 'https' or parts.netloc != 'outlawstar.fandom.com' or parts.path != '/api.php':
        raise ValueError('Unexpected network endpoint')
    request = Request(url, headers={'User-Agent': AGENT, 'Accept': 'application/json'})
    try:
        with build_opener(NoRedirect()).open(request, timeout=30) as response:
            raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise AccessError('INVALID_RESPONSE', 'API response exceeds size bound')
            return response.status, dict(response.headers), raw
    except HTTPError as exc:
        # Never log challenge/cookie/error bodies.
        return exc.code, dict(exc.headers), b''
    except (URLError, TimeoutError, OSError) as exc:
        raise AccessError('RETRY_EXHAUSTED', 'Network/timeout failure') from exc


class Client:
    def __init__(self, send=transport, sleep=time.sleep, clock=time.monotonic):
        self.send, self.sleep, self.clock = send, sleep, clock
        self.last = None

    def query(self, title):
        title_check(title)
        params = dict(action='query', prop='revisions', titles=title,
                      rvprop='ids|timestamp|content', rvslots='main', format='json',
                      formatversion=2, redirects=1, maxlag=5, meta='siteinfo', siprop='rightsinfo')
        url = API + '?' + urlencode(params)
        for attempt in range(3):
            if self.last is not None:
                self.sleep(max(0, 1.0 - (self.clock() - self.last)))
            self.last = self.clock()
            try:
                status, headers, raw = self.send(url)
            except AccessError as exc:
                if exc.outcome != 'RETRY_EXHAUSTED' or attempt == 2:
                    raise
                self.sleep(2 ** (attempt + 1))
                continue
            if status in (401, 403, 402) or 300 <= status < 400:
                raise AccessError('DENIED', f'API HTTP {status}; no alternate route attempted')
            if status == 429 or 500 <= status <= 599:
                if attempt == 2:
                    raise AccessError('RETRY_EXHAUSTED', f'API HTTP {status}; retry bound reached')
                retry_after = next((value for key, value in headers.items() if key.lower() == 'retry-after'), '')
                if retry_after and (not str(retry_after).isdigit() or int(retry_after) > 60):
                    raise AccessError('RETRY_EXHAUSTED', 'Retry-After exceeds bounded wait; retry later')
                self.sleep(max(2 ** (attempt + 1), int(retry_after or 0)))
                continue
            if status != 200:
                raise AccessError('INVALID_RESPONSE', f'Unexpected API HTTP {status}')
            media_type = next((value for key, value in headers.items() if key.lower() == 'content-type'), '')
            if len(raw) > MAX_BYTES or 'application/json' not in media_type.lower():
                raise AccessError('INVALID_RESPONSE', 'Expected bounded JSON response, not HTML/challenge')
            try:
                data = json.loads(raw.decode('utf-8'))
            except (UnicodeError, ValueError) as exc:
                raise AccessError('INVALID_RESPONSE', 'Invalid JSON payload') from exc
            if not isinstance(data, dict):
                raise AccessError('INVALID_RESPONSE', 'JSON root is not an object')
            if data.get('error'):
                if not isinstance(data['error'], dict):
                    raise AccessError('INVALID_RESPONSE', 'Malformed API error object')
                code = data['error'].get('code', 'unknown')
                if code in ('maxlag', 'ratelimited') and attempt < 2:
                    self.sleep(2 ** (attempt + 1))
                    continue
                outcome = 'RETRY_EXHAUSTED' if code in ('maxlag', 'ratelimited') else 'INVALID_RESPONSE'
                if code in ('readapidenied', 'permissiondenied', 'blocked'):
                    outcome = 'DENIED'
                raise AccessError(outcome, 'API error: ' + str(code))
            try:
                captures = from_api(data, title)
            except (ValueError, KeyError, TypeError, IndexError) as exc:
                raise AccessError('INVALID_RESPONSE', 'Missing/invalid article revision structure') from exc
            return captures, raw, {'requested': [title], 'requested_url': url, 'final_url': url,
                                   'media_type': media_type, 'raw_sha256': sha(raw),
                                   'raw_bytes': len(raw), 'captured_utc': now(), 'capture_method': 'FANDOM_API'}
        raise AccessError('RETRY_EXHAUSTED', 'Retry bound reached')


def template_spans(text):
    """Top-level template spans; nested arguments remain intact, never evaluated."""
    stack, spans, warnings, position = [], [], [], 0
    while position < len(text):
        protected = re.match(r'<!--.*?-->|<nowiki\b[^>]*>.*?</nowiki\s*>', text[position:], re.S | re.I) if text[position] == '<' else None
        if protected:
            position += protected.end()
            continue
        if text.startswith('{{', position):
            width = 3 if text.startswith('{{{', position) else 2
            stack.append((width, position))
            position += width
        elif text.startswith('}}', position):
            if stack:
                width, start = stack.pop()
                if not text.startswith('}' * width, position):
                    warnings.append('Unbalanced template/parameter delimiter')
                    width = 2
                position += width
                if not stack:
                    spans.append((start, position))
            else:
                warnings.append('Unmatched template closing delimiter')
                position += 2
        else:
            position += 1
    if stack:
        warnings.append('Unclosed template/parameter; original source retained')
    return spans, warnings


def split_fields(text):
    """Split a template only at top-level pipes, preserving nested wiki constructs."""
    depth, links, start, output = 0, 0, 0, []
    for token in re.finditer(r'\{\{|\}\}|\[\[|\]\]|\|', text):
        value = token.group()
        if value == '{{': depth += 1
        elif value == '}}': depth = max(0, depth - 1)
        elif value == '[[': links += 1
        elif value == ']]': links = max(0, links - 1)
        elif not depth and not links:
            output.append(text[start:token.start()])
            start = token.end()
    output.append(text[start:])
    return output


def parse(text):
    spans, warnings = template_spans(text)
    masked = list(text)
    protected = spans + [(match.start(), match.end()) for match in re.finditer(
        r'<!--.*?-->|<nowiki\b[^>]*>.*?</nowiki\s*>|<ref\b[^>]*?(?:/\s*>|>.*?</ref\s*>)', text, re.S | re.I)]
    for start, end in protected:
        for pos in range(start, end):
            if masked[pos] != '\n': masked[pos] = ' '
    headings = list(re.finditer(r'^(={2,6})\s*(.*?)\s*\1\s*$', ''.join(masked), re.M))
    bounds = [(0, headings[0].start() if headings else len(text), [], '')]
    hierarchy = []
    for index, match in enumerate(headings):
        level = len(match[1])
        hierarchy = [(old_level, title) for old_level, title in hierarchy if old_level < level]
        hierarchy.append((level, match[2].strip()))
        bounds.append((match.end(), headings[index + 1].start() if index + 1 < len(headings) else len(text),
                       [title for _, title in hierarchy], text[match.start():match.end()]))
    sections = []
    for number, (start, end, heading_path, heading_raw) in enumerate(bounds, 1):
        locator = f'SECTION:{number:04d}'
        body = text[start:end]
        blocks = []
        for template_start, template_end in spans:
            if not start <= template_start < end:
                continue
            raw = text[template_start:template_end]
            parts = split_fields(raw[2:-2])
            name = parts[0].strip()
            blocks.append({'kind': 'TEMPLATE', 'start': template_start, 'end': template_end,
                           'name': name, 'raw': raw, 'resolved': False})
            warnings.append('Unresolved template: ' + name)
            if name.lower().startswith('infobox'):
                for part in parts[1:]:
                    if '=' in part:
                        field, value = part.split('=', 1)
                        blocks.append({'kind': 'INFOBOX_FIELD', 'start': template_start, 'end': template_end,
                                       'name': field.strip(), 'value': value.strip(), 'raw': part})
        ref_matches = list(re.finditer(r'<ref\b[^>]*?(?:/\s*>|>.*?</ref\s*>)', body, re.S | re.I))
        for match in ref_matches:
            blocks.append({'kind': 'REFERENCE', 'start': start + match.start(), 'end': start + match.end(), 'raw': match.group()})
        if len(list(re.finditer(r'<ref\b', body, re.I))) != len(ref_matches):
            warnings.append('Unclosed reference tag; original source retained')
        occupied = sorted((block['start'], block['end']) for block in blocks)
        cursor = start
        for left, right in occupied + [(end, end)]:
            if left > cursor:
                blocks.append({'kind': 'PROSE', 'start': cursor, 'end': left, 'raw': text[cursor:left]})
            cursor = max(cursor, right)
        blocks.sort(key=lambda block: (block['start'], -block['end']))
        for index, block in enumerate(blocks, 1):
            block['locator'] = locator + f'/BLOCK:{index:04d}'
        outbound = []
        for match in re.finditer(r'\[\[([^\]\n]+)\]\]', body):
            destination = match[1].split('|', 1)[0].strip()
            outbound.append({'kind': 'WIKI', 'target': destination,
                             'url': BASE + '/wiki/' + quote(destination.replace(' ', '_'), safe='():#'),
                             'raw': match.group()})
        for match in re.finditer(r'\[(https?://[^\s\]]+)(?:\s+[^\]]*)?\]', body):
            outbound.append({'kind': 'EXTERNAL', 'target': match[1], 'url': match[1], 'raw': match.group()})
        sections.append({'locator': locator, 'heading_path': heading_path, 'heading_raw': heading_raw,
                         'start': start, 'end': end, 'text': body, 'blocks': blocks, 'outbound_links': outbound})
    warnings = list(dict.fromkeys(warnings))
    return {'parser_version': PARSER, 'sections': sections,
            'parse_status': 'PARTIAL' if warnings else 'COMPLETE', 'parse_warnings': warnings}


def capture(title, page, revision, timestamp, text, method, rights=None):
    if not isinstance(text, str):
        raise ValueError('Missing wikitext')
    rights = rights or {}
    url = article_url(title)
    result = {'schema_version': SCHEMA, 'site': 'FANDOM', 'outcome': 'OK', 'title': title,
              'document_key': f'fandom:outlawstar:page:{page}', 'version_key': f'revision:{revision}',
              'canonical_url': url, 'version_url': url + '?oldid=' + str(revision),
              'remote_page_id': str(page), 'remote_revision_id': str(revision),
              'remote_modified_utc': timestamp, 'source_text': text,
              'content_sha256': sha(text.encode('utf-8')), 'captured_utc': now(),
              'capture_method': method, 'license_name': rights.get('text', ''),
              'license_url': rights.get('url', ''), 'attribution_url': url + '?action=history',
              **parse(text)}
    check_capture(result)
    return result


def from_api(data, requested):
    query = data['query']
    pages = query['pages']
    if not isinstance(pages, list) or len(pages) != 1:
        raise ValueError('Expected one selected article')
    page = pages[0]
    if 'missing' in page or 'invalid' in page:
        raise AccessError('NOT_FOUND', 'Selected article missing or invalid')
    if page.get('ns') != 0:
        raise ValueError('Unexpected namespace')
    revisions = page['revisions']
    if len(revisions) != 1:
        raise ValueError('Expected exactly one latest revision')
    revision = revisions[0]
    slot = revision['slots']['main']
    if slot.get('contentmodel') not in (None, 'wikitext'):
        raise ValueError('Unexpected content model')
    result = capture(page['title'], page['pageid'], revision['revid'], revision['timestamp'],
                     slot['content'], 'FANDOM_API', query.get('rightsinfo'))
    result['requested'] = [requested]
    result['redirects'] = query.get('redirects', [])
    result['normalized_titles'] = query.get('normalized', [])
    return result


def from_xml(raw):
    if len(raw) > MAX_BYTES:
        raise ValueError('Oversize XML refused')
    decoded = raw.decode('utf-8-sig')
    if '\x00' in decoded or re.search(r'<!\s*(DOCTYPE|ENTITY)', decoded, re.I):
        raise ValueError('Oversize XML or DTD/entities refused')
    root = ET.fromstring(decoded)
    namespace = root.tag.rsplit('}', 1)[0] + '}' if '}' in root.tag else ''
    if root.tag != namespace + 'mediawiki':
        raise ValueError('Not a MediaWiki export')
    site = root.find(namespace + 'siteinfo')
    if site is None or site.findtext(namespace + 'base', '').split('/wiki/')[0] != BASE:
        raise ValueError('Wrong export site')
    output, seen = [], set()
    for page in root.findall(namespace + 'page'):
        title = page.findtext(namespace + 'title')
        title_check(title)
        if title in seen or page.findtext(namespace + 'ns') != '0':
            raise ValueError('Duplicate page or unexpected namespace')
        seen.add(title)
        revisions = page.findall(namespace + 'revision')
        if len(revisions) != 1:
            raise ValueError('Only current-revision XML fixtures are supported')
        revision = revisions[0]
        text = revision.find(namespace + 'text')
        if text is None or 'deleted' in text.attrib:
            raise ValueError('Missing/deleted revision content')
        output.append(capture(title, page.findtext(namespace + 'id'), revision.findtext(namespace + 'id'),
                              revision.findtext(namespace + 'timestamp'), text.text or '', 'FANDOM_XML'))
    if not output or len(output) > MAX_TITLES:
        raise ValueError('Select 1–10 articles per XML import')
    return output
