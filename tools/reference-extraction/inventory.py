"""Read-only source inventory and local settei screening sheets."""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[2]


def main():
    index = ROOT / 'reference' / 'indexes'
    sheets = ROOT / 'reference' / 'contact-sheets'
    index.mkdir(parents=True, exist_ok=True)
    sheets.mkdir(parents=True, exist_ok=True)
    rows = []
    scans = sorted((ROOT / '_source_settei').glob('*.jpg'))
    for n, path in enumerate(scans, 1):
        with Image.open(path) as im:
            size = list(im.size)
        rows.append(dict(id=f'SET-{n:03}', path=path.relative_to(ROOT).as_posix(),
                         bytes=path.stat().st_size, dimensions=size,
                         sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    episodes = [dict(path=p.relative_to(ROOT).as_posix(), bytes=p.stat().st_size)
                for p in sorted((ROOT / '_source_episodes').iterdir()) if p.is_file()]
    (index / 'source-manifest.json').write_text(json.dumps(dict(settei=rows, episodes=episodes), indent=2) + '\n', encoding='utf-8')
    for start in range(0, len(scans), 30):
        batch = scans[start:start + 30]
        canvas = Image.new('RGB', (1500, 6 * 230), 'white')
        draw = ImageDraw.Draw(canvas)
        for i, path in enumerate(batch):
            x, y = (i % 5) * 300, (i // 5) * 230
            with Image.open(path) as im:
                thumb = ImageOps.contain(ImageOps.exif_transpose(im).convert('RGB'), (292, 204))
                canvas.paste(thumb, (x + (300 - thumb.width) // 2, y + 20))
            draw.text((x + 8, y + 4), path.name, fill='black')
        canvas.save(sheets / f'settei-{start + 1:03}-{start + len(batch):03}.jpg', quality=90)
    print(f'Inventoried {len(scans)} scans and {len(episodes)} episode-folder files; generated {(len(scans)+29)//30} sheets.')


if __name__ == '__main__':
    main()
