"""Cache AnimeHistory gallery HTML and index caption timestamps; no image downloads."""
import csv
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

ROOT = Path(__file__).resolve().parents[2]
BASE = 'https://animehistory.org'
CACHE = ROOT / 'reference' / 'cache' / 'animehistory'
INDEX = ROOT / 'reference' / 'indexes' / 'animehistory'
AGENT = 'OutlawStarReferenceIndexer/1.0 (HTML metadata cache; no images)'


def fetch(url, name):
    path = CACHE / name
    sidecar = path.with_suffix(path.suffix + '.json')
    if path.exists() and sidecar.exists():
        data = path.read_bytes()
        info = json.loads(sidecar.read_text(encoding='utf-8'))
        if hashlib.sha256(data).hexdigest() != info['sha256']:
            raise ValueError(f'Cache hash mismatch: {path}')
        return data.decode('utf-8', errors='replace'), info
    time.sleep(0.5)
    request = Request(url, headers={'User-Agent': AGENT})
    with urlopen(request, timeout=30) as response:
        data = response.read()
        final_url = response.url
        if urlparse(final_url).hostname not in ('animehistory.org', 'www.animehistory.org'):
            raise ValueError(f'Unexpected redirect: {final_url}')
    info = dict(requested_url=url, final_url=final_url,
                retrieved_utc=datetime.now(timezone.utc).isoformat(),
                sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                cache_path=path.relative_to(ROOT).as_posix())
    path.write_bytes(data)
    sidecar.write_text(json.dumps(info, indent=2) + '\n', encoding='utf-8')
    return data.decode('utf-8', errors='replace'), info


class GalleryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.items = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'div' and 'gallery-item' in a.get('class', '').split():
            if a.get('data-type') == 'screencap':
                self.items.append(a)


def parse(text):
    parser = GalleryParser()
    parser.feed(text)
    return parser


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    INDEX.mkdir(parents=True, exist_ok=True)
    robots_text, robots_info = fetch(BASE + '/robots.txt', 'robots.txt')
    robots = RobotFileParser()
    robots.parse(robots_text.splitlines())
    hub_url = BASE + '/anime/outlaw-star/'
    if not robots.can_fetch(AGENT, hub_url):
        raise ValueError('Robots guidance disallows series hub')
    hub, hub_info = fetch(hub_url, 'series.html')
    episodes = {}
    for link in parse(hub).links:
        url = urljoin(hub_url, link)
        match = re.fullmatch(r'/gallery/screencaps/outlaw-star/episode-(\d+)/', urlparse(url).path)
        if match and urlparse(url).hostname in ('animehistory.org', 'www.animehistory.org'):
            episodes[int(match[1])] = url.split('?')[0]
    if set(episodes) != set(range(1, 27)):
        raise ValueError(f'Expected episode links 1–26; got {sorted(episodes)}')
    all_rows, summaries, cache_records = [], [], [robots_info, hub_info]
    for episode, gallery_url in sorted(episodes.items()):
        if not robots.can_fetch(AGENT, gallery_url):
            raise ValueError(f'Robots guidance disallows {gallery_url}')
        first, first_info = fetch(gallery_url, f'episode-{episode:02}-page-01.html')
        page_match = re.search(r'Page\s+1\s+of\s+(\d+)', first)
        count_match = re.search(r'name="description"\s+content="(\d+) screencaps', first)
        if not page_match or not count_match:
            raise ValueError(f'Cannot establish pagination/count: episode {episode}')
        pages, expected = int(page_match[1]), int(count_match[1])
        if not 1 <= pages <= 20:
            raise ValueError(f'Unexpected pagination: {pages}')
        rows, ids = [], set()
        for page in range(1, pages + 1):
            page_url = gallery_url if page == 1 else gallery_url + f'?page={page}'
            if not robots.can_fetch(AGENT, page_url):
                raise ValueError(f'Robots guidance disallows {page_url}')
            text, info = (first, first_info) if page == 1 else fetch(page_url, f'episode-{episode:02}-page-{page:02}.html')
            cache_records.append(info)
            parsed = parse(text)
            if not parsed.items:
                raise ValueError(f'Empty gallery page: {page_url}')
            for item in parsed.items:
                caption = item['data-caption']
                match = re.fullmatch(r'Outlaw Star Ep (\d+): (.+) @ (\d{2}:\d{2}:\d{2})', caption)
                if not match or int(match[1]) != episode:
                    raise ValueError(f'Unexpected caption: {caption}')
                timestamp = match[3]
                h, m, s = map(int, timestamp.split(':'))
                if m >= 60 or s >= 60:
                    raise ValueError(f'Invalid time: {timestamp}')
                if item['data-id'] in ids:
                    raise ValueError(f'Duplicate image ID: {item["data-id"]}')
                ids.add(item['data-id'])
                image_url = BASE + '/uploads/screencaps/' + item['data-filename']
                rows.append(dict(episode_id=f'EP-{episode:02}', episode_title=match[2],
                                 web_timestamp=timestamp, web_seconds=h*3600+m*60+s,
                                 image_id=item['data-id'], image_url=image_url, caption=caption,
                                 gallery_url=gallery_url, source_page_url=info['final_url'],
                                 source_page=page, retrieved_utc=info['retrieved_utc'],
                                 html_sha256=info['sha256'], local_timestamp='',
                                 alignment_status='UNVERIFIED'))
        if len(rows) != expected:
            raise ValueError(f'Count mismatch EP-{episode:02}: {len(rows)} != {expected}')
        if [r['web_seconds'] for r in rows] != sorted(r['web_seconds'] for r in rows):
            raise ValueError(f'Non-monotonic gallery timestamps: episode {episode}')
        with (INDEX / f'episode-{episode:02}.csv').open('w', newline='', encoding='utf-8') as output:
            writer = csv.DictWriter(output, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        all_rows.extend(rows)
        summaries.append(dict(episode_id=f'EP-{episode:02}', title=rows[0]['episode_title'],
                              pages=pages, expected_count=expected, actual_count=len(rows),
                              first_timestamp=rows[0]['web_timestamp'], last_timestamp=rows[-1]['web_timestamp'],
                              gallery_url=gallery_url, alignment_status='UNVERIFIED'))
        print(f'EP-{episode:02}: {len(rows)} timestamps, {pages} pages, {rows[0]["web_timestamp"]}–{rows[-1]["web_timestamp"]}', flush=True)
    with (INDEX / 'all-episodes.csv').open('w', newline='', encoding='utf-8') as output:
        writer = csv.DictWriter(output, fieldnames=list(all_rows[0]))
        writer.writeheader()
        writer.writerows(all_rows)
    manifest = dict(source_id='EXT-001', source=hub_url, generated_utc=datetime.now(timezone.utc).isoformat(),
                    cache_policy='Reuse verified cache; remove/refresh only by explicit choice',
                    image_downloads=0, total_records=len(all_rows), episodes=summaries, pages=cache_records)
    (INDEX / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'Complete: {len(summaries)} episodes, {len(all_rows)} records, no screenshots downloaded.', flush=True)


if __name__ == '__main__':
    main()
