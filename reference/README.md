# Local reference workflow

Original source folders are read-only and ignored. Generated frames, contact sheets, caches, and working images are ignored. Authored indexes and textual evidence are trackable.

Run tools/reference-extraction/inventory.py using Python with Pillow. It inventories both source folders, hashes scans, records image dimensions, writes reference/indexes/source-manifest.json, and generates labeled settei contact sheets under reference/contact-sheets/. Episode videos are listed but not decoded or hashed by default.

Index fields: source ID, filename, visible sheet number, Japanese title, English translation, subject, category, verification status, reconstruction relevance, region/system, measurements/callouts, questions. Unknown fields remain blank; unreviewed is explicit.

Episode extraction is deferred. Future frame records must identify the exact source filename, requested time, actual decoded presentation timestamp, stream, extraction command/version, and observation. Do not infer timestamps from another release.

The user's [image map](image-map.md) is preserved as original review notes. [Image map reconciliation](indexes/image-map-reconciliation.md) records resolved sheet identities, corrections, and episode-verification leads; use the screening CSV for collection-wide status.

[Local AnimeHistory timestamp indexes](indexes/animehistory/README.md) cover all 26 episodes. HTML and timestamp metadata are cached; screencap images remain online, and gallery times still need alignment to local media.

[Repeated-sheet comparison](indexes/settei-variant-review.md) covers the first eight bridge/engineering variants. [Episode 4 startup evidence](indexes/episode-04-startup-review.md) records focused local frame PTS and observations separately from English-subtitle leads. Frame PNGs/logs and the working subtitle copy remain ignored; textual manifests are trackable.

[Startup open-item follow-up](indexes/startup-open-items-followup.md) tracks the six priority questions, closer handle/hatch evidence, six further geometry-critical variants and selected Japanese propulsion labels. It also records which questions still need remembered episode leads or original-language audio review.

The user's [episode-time notes](episode-times.md) are retained unchanged; the corrected Episode 7 endpoint and verified scene findings are in [the Episodes 4/7/8 startup comparison](indexes/startup-sequence-comparison.md). This separates commissioning, simulated fault practice and actual standby-to-launch operation.

[Episode 26 entry evidence](indexes/episode-26-platform-review.md) verifies occupant descent. [Episode 11 sub-ether/recovery evidence](indexes/episode-11-subether-review.md) records transition effects, disrupted entry, auxiliary operation and physical key shutdown/restart, with English subtitle findings separated from visuals.
