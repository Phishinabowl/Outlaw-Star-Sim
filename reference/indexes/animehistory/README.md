# Local AnimeHistory timestamp index

Source: [AnimeHistory Outlaw Star galleries](https://animehistory.org/anime/outlaw-star/) (EXT-001). These are sampled web screencap locator records, not annotated scene breakdowns or verified local-video times.

Initial cache completed October 6, 2026 (America/New_York): **26 episodes, 104 gallery pages, 9,204 records**, plus the series hub and robots guidance. All episodes have 354 unique records across four pages. Episode 4 covers 00:01:43–00:23:14. The combined index and all per-episode counts/IDs/cache hashes were verified. Retrieval timestamps in the records use UTC.

- [animehistory-review.xlsx](animehistory-review.xlsx) is the generated local browsing workbook: Overview plus EP-01 through EP-26 tabs, filters, frozen identifiers/headers and image hyperlinks. It contains locators only; no images or visual subject annotations are embedded. Open this for routine review.
- [all-episodes.csv](all-episodes.csv) combines the complete successfully parsed galleries and remains in this folder.
- `CSVs/episode-01.csv` through `CSVs/episode-26.csv` provide the authoritative individual episode records. Start with [Episode 4](CSVs/episode-04.csv).
- manifest.json records expected/actual counts, page URLs, retrieval timestamps, raw-HTML hashes, and coverage ranges.
- Original HTML and per-page retrieval sidecars live under ignored reference/cache/animehistory/. They can be reparsed without visiting the site. No screenshots, CSS, scripts, or other linked assets are downloaded.

## Using the records

Search/filter CSVs by episode_id or web_seconds/web_timestamp. Each row has the source caption, image ID/URL, gallery/page URL, retrieval time, and source HTML digest. Image links still require internet access; caching the HTML does not make the images available offline. Opening cached HTML in a browser may load remote resources, so use the CSV index for offline lookup.

All alignment_status values initially read UNVERIFIED and local_timestamp is empty. Web times are second-resolution locator labels, not frame-accurate PTS. Validate recognizable matching shots against the local source before using them for extraction. Record confirmed matches in authored scene/evidence records rather than editing these generated CSVs; rerunning the generator replaces its outputs.

A gallery's 354 records do not guarantee every scene or the full episode runtime is covered. Review the first/last timestamp in the manifest; gaps/openings/endings can be excluded by sampling. Counts verify the records against the website's declared count, not the authenticity, timing accuracy, resolution, or completeness of the underlying anime footage.

## Reproducing the cache/index

Run python tools/reference-extraction/cache_timestamp_index.py from the repository root. Requires Python's standard library and network access for pages not cached. No new packages are needed. The script discovers episode gallery links from the hub, checks robots guidance, follows gallery pagination, paces requests, and validates captions/IDs/counts/order. It reuses caches only when their SHA-256 matches the sidecar. HTTP failures or unexpected content stop the run; completed page caches can be reused on the next run. It does not bypass login or access restrictions.

Textual metadata is Git-trackable; raw website HTML remains local-only. Source episode/settei folders are neither read nor modified by this tool.

## Workbook refresh and ownership

The 2026-10-26 organization change places individual episode CSVs in `CSVs/`; their contents are
unchanged. The workbook is a generated, ignored local convenience view, not a second editable
source. Rebuilding replaces it. Keep source corrections and future authored annotations in their
own authoritative textual data; do not keep unique edits only in the workbook.

`tools/reference-extraction/build_animehistory_workbook.ps1` reads the 26 episode CSVs, verifies all
fields against `all-episodes.csv`, and writes `animehistory-review.xlsx` in this folder. It retains
all 14 source fields and adds a View image hyperlink column. Image IDs and timestamp labels remain
text; seconds and page numbers are numeric. The overview links to episode tabs and totals records.
The builder performs no network requests or media extraction. Web/local alignment remains unverified.

Use PowerShell with the installed ImportExcel module (tested with 7.8.10). The script checks for
the module and does not install dependencies or start Excel. Run from the repository root:

```text
powershell -File tools/reference-extraction/build_animehistory_workbook.ps1
```

The script builds under ignored `.tmp/animehistory-workbook/`, reopens the result to verify every
source field and image link, and replaces the generated workbook only after validation succeeds.
Close the workbook before refreshing if Excel holds a file lock. CSV regeneration and workbook
refresh are separate operations; refresh after regenerating the locator CSVs.

The ImportExcel test opened directly in VS Code Office Viewer on 2026-10-26, as reported by the
maintainer. The earlier artifact-tool export required an Excel resave for that viewer; the exact
incompatible XML feature was not isolated. ImportExcel is the retained authoring path. No XLSX/LFS
publication rule is introduced.
