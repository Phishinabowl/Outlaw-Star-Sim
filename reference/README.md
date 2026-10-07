# Local reference workflow

Original source folders are read-only and ignored. Generated frames, contact sheets, caches, and working images are ignored. Authored indexes and textual evidence are trackable.

Run tools/reference-extraction/inventory.py using Python with Pillow. It inventories both source folders, hashes scans, records image dimensions, writes reference/indexes/source-manifest.json, and generates labeled settei contact sheets under reference/contact-sheets/. Episode videos are listed but not decoded or hashed by default.

Index fields: source ID, filename, visible sheet number, Japanese title, English translation, subject, category, verification status, reconstruction relevance, region/system, measurements/callouts, questions. Unknown fields remain blank; unreviewed is explicit.

Episode extraction is deferred. Future frame records must identify the exact source filename, requested time, actual decoded presentation timestamp, stream, extraction command/version, and observation. Do not infer timestamps from another release.

The user's [image map](image-map.md) is preserved as original review notes. [Image map reconciliation](indexes/image-map-reconciliation.md) records resolved sheet identities, corrections, and episode-verification leads; use the screening CSV for collection-wide status.

[Local AnimeHistory timestamp indexes](indexes/animehistory/README.md) cover all 26 episodes. HTML and timestamp metadata are cached; screencap images remain online, and gallery times still need alignment to local media.
