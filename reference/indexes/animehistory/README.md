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

## Authored category index and future Power BI view

**Planning requirement — 2026-10-26:** design the authored category index for later Power BI
reporting. Complete the all-episode category survey, then prepare and validate a research report
before collaborative cross-episode detail reviews. The authored index and generated category
workbook were initialized on 2026-10-26. Power BI implementation, page design and image display
remain future work.

Retain one authoritative authored CSV across episodes, with exactly one row per gallery image.
The initial field contract and vocabulary are defined below. Its data contract must support:

- Stable text identifiers: retain `episode_id` and `image_id`, and derive a deterministic
  `image_key` from both for report relationships. Keep numeric episode order, locator order and
  web seconds available from the locator join for sorting; do not sort timestamp labels as prose.
- A single header row, stable snake_case field names, UTF-8 CSV with standard quoting, and no
  merged cells, decorative rows or spreadsheet formulas. Set types explicitly during import:
  identifiers and timestamp labels are text, ordering fields are whole numbers, and review times
  use ISO 8601 UTC. Empty optional values mean unknown/not recorded, not zero or a negative finding.
- Controlled category, subject, detail, review-status, confidence and priority vocabularies.
  Use canonical tag values with documented meanings; keep synonyms in display labels or notes.
  Distinguish preliminary identification from verified observations and canon classification.
- Overlapping tags stored as semicolon-delimited values, without semicolons inside a tag.
  The report transformation derives separate image-to-category, image-to-subject and
  image-to-detail association tables, one image key/tag per row, plus unique tag lookup tables.
  These are generated views, not competing authored CSVs. Do not expand independent tag lists
  together into multiplied rows or infer that a detail belongs to a particular subject from
  their co-occurrence; subject-specific relationships require separately supported records.
- Scene-group identities scoped by episode, separate screening/detail states, concise visible
  descriptions, uncertainties, revisit reasons, review provenance and later evidence pointers.
  Preserve unreviewed records so coverage reports include pending work.
- Locator joins for web time, source image/page links and alignment status; do not maintain
  duplicate editable locator metadata. Local cache paths and availability are machine-specific
  operational data and cannot serve as stable report identities.

Power BI and the generated ImportExcel workbook are projections of these textual sources.
Refresh must preserve authored notes and stable identities. Validate key uniqueness, join
coverage, controlled values, types and before/after row counts; count distinct image keys for
image totals after tag expansion. Category totals overlap and must not be added as an image total.
Report coverage describes sampled gallery locators, not complete episode footage.

Candidate report pages include survey coverage, cross-episode XGP references, other subject
browsing and an uncertainty/rewatch queue. Final pages and filters will be agreed after the survey.
Image preview feasibility must be tested in the intended report environment; retain source links
as a fallback without assuming that ignored local cache files are accessible to a published report.
No cloud publication, media upload, new service or installation is authorized by this requirement.

### Category-index field contract — version 1

The authored file is `category-index.csv` in this folder. Establish all locator rows as
unreviewed when the file is created; initial population is not screening. The 21 columns below
are ordered as shown. Initialization and screening evidence is recorded below.

| Field | Type / rule |
| --- | --- |
| `episode_id` | Required text matching a locator episode, e.g. `EP-04`. |
| `image_id` | Required text matching that episode's locator image ID. The pair is unique. |
| `scene_group_id` | Optional text `EP-04-S001` style identity for a contiguous chronological group. Retain assigned IDs when boundaries are revised; numbers are identities, not a sort key. |
| `scene_summary` | Short preliminary context for the group. Repeat consistently across group members; validate consistency. Grouping describes sampled shots, not verified edit boundaries. |
| `categories` | Zero or more broad category tags from the vocabulary below. |
| `subjects` | Zero or more canonical subject identifiers from the subject register below. |
| `subject_details` | Zero or more visible feature/area tags from the vocabulary below. These are image-level tags, not subject-to-feature assertions. |
| `presentation` | Required single value: `UNKNOWN`, `STORY`, `OPENING`, `ENDING`, `RECAP`, `PREVIEW`, `EYECATCH`, `TITLE_CARD`, `END_CARD`, `OTHER`. Classify the sampled presentation, not an assumed source episode for reused footage. |
| `screening_status` | Required: `UNREVIEWED`, `SCREENED`, `NEEDS_RECHECK`, `UNAVAILABLE`. |
| `detail_status` | Required: `NOT_REVIEWED`, `PARTIAL`, `REVIEWED`. Independent of preliminary screening. |
| `identification_confidence` | Required: `NOT_ASSESSED`, `HIGH`, `MEDIUM`, `LOW`. Applies to subject identification only, not canon/timing/detail accuracy. Where identities differ in confidence, use the lowest assessed confidence and identify the uncertain subject in `uncertainties`. |
| `visual_summary` | Concise visible content; do not copy generated captions as observations or place recollections here. |
| `research_priority` | Required: `UNASSESSED`, `HIGH`, `NORMAL`, `LOW`. Priority for further reference work, not canonical authority. |
| `revisit_reason` | Specific reason to return, such as a useful rear view, uncertain doorway relationship or mechanism endpoint. Required for `HIGH` priority. |
| `uncertainties` | Identification doubts, illegible text, contradictions and questions for closer inspection/video. Required for `NEEDS_RECHECK` or assessed `LOW` confidence. For `UNAVAILABLE`, record the inspection/access obstacle. |
| `reported_context` | Attributed recollections or supplied interpretations, distinguished from visible observations. Include who supplied the context; blank when none. |
| `screened_by` | Reviewer identity for the latest screening/recheck attempt, including unavailable outcomes. A name here does not imply maintainer acceptance. |
| `screened_utc` | ISO 8601 UTC timestamp for that attempt; blank for untouched records. |
| `detail_reviewed_by` | Reviewer identity for the latest substantive detailed review; blank until partial/reviewed. |
| `detail_reviewed_utc` | ISO 8601 UTC timestamp for that detailed review. |
| `detail_references` | Semicolon-separated repository-relative evidence links/anchors for later detailed findings. Required when `detail_status` is `PARTIAL` or `REVIEWED`; do not store detailed canon claims solely in this screening table. |

`SCREENED` means sufficient visual inspection to assign preliminary tags, including images with
no current research value. `NEEDS_RECHECK` means inspected but a material classification remains
unresolved; retain candidate tags so uncertain XGP references stay discoverable. `UNAVAILABLE`
means not visually inspected because the image could not be accessed/decoded; retain previous
notes if any. These are mutually exclusive current states, not an audit history. The workbook/report
must show them separately. Detail review does not automatically resolve uncertain classifications.
Git retains published annotation history; do not add a Markdown record for each screening batch.

The generated view derives `image_key` as `episode_id + ':' + image_id`, numeric episode order,
locator ordinal, web timestamp/seconds, episode title, source URLs and alignment status. It may
also derive scene start/end web seconds from group membership. Do not add these as duplicate
editable columns. Unassigned groups and blank tag lists remain unknown/unassigned, not exclusions.

### Initial tag vocabulary

Tag lists use unique lowercase snake_case tokens, sorted alphabetically and joined with `;`
without surrounding spaces. Empty means unassigned; do not use `none`, free-form synonyms or
comma-separated values. New tokens are permitted only with a definition added here in the same
reviewable change. Existing tokens must not silently change meaning. This initial vocabulary is
extensible across all episodes; unknown identities must not be guessed to fit the register.

| `categories` token | Meaning |
| --- | --- |
| `ships_vehicles` | Spacecraft, ground vehicles and their exterior forms. |
| `interiors_rooms` | Interior spaces and room arrangements. |
| `machinery_controls` | Mechanisms, engines, consoles, switches and operational equipment. |
| `characters_creatures` | People, aliens, animals and visible character appearance. |
| `costumes_accessories` | Clothing, wearable equipment and accessories. |
| `weapons` | Personal or mounted weapons, ammunition and weapon effects when identifiable. |
| `props_equipment` | Portable objects, tools, containers and other equipment. |
| `locations_infrastructure` | Buildings, settlements, stations, hangars and built environments. |
| `celestial_environment` | Space, celestial bodies, terrain and natural environments. |
| `graphics_signage` | Text, emblems, interface graphics, signs and transition/title designs. |
| `lighting_effects` | Useful lighting, atmosphere, energy or other visual effects. |

Apply categories for useful visible content, not every incidental background object. Multiple
categories may apply to the same image. A failed identification is expressed by subject/confidence
and uncertainty fields, not a category that hides the image from other groups.

The `subjects` register starts with:

| Tokens | Identity |
| --- | --- |
| `xgp` | XGP-15AII / Outlaw Star; operating states remain details/notes, not different ship identities. |
| `gene_starwind`, `jim_hawking`, `melfina`, `hilda`, `aisha_clanclan`, `suzuka`, `gilliam` | Named character/system identities. Gilliam's displayed body/interface can also receive graphics or machinery tags. |
| `caster` | Gene's caster weapon; do not use for an unidentified gun. |
| `ron_macdougall`, `harry_macdougall` | MacDougall brothers; first-batch identifications supplied by the maintainer, with cropped visibility recorded per image. |
| `space_pirate_foot_soldier` | Recurring mechanical space-pirate foot soldiers, identified by the maintainer; no specific unit/faction identity implied. |
| `horus` | Hilda's spacecraft, identified by the maintainer in Episode 4 exterior/cockpit views. |
| `xgp_hangar_asteroid` | Asteroid containing the Outlaw Star's storage hangar and awakening setting, identified by the maintainer; door motion and transfer context remain reported until checked in video. |
| `starwind_hawking_hq` | Starwind & Hawking premises; identification does not establish a planet/location without supporting evidence. |
| `unknown_character`, `unknown_creature`, `unknown_ship`, `unknown_vehicle`, `unknown_location`, `unknown_equipment` | Visible but unidentified subjects; describe distinguishing appearance in the summary. These are unresolved identity buckets, not assertions that different images depict the same subject. |

Register additional named ships, locations, characters and recurring props as encountered. For
possible XGP content, retain `xgp` as a candidate with `NEEDS_RECHECK`, qualified confidence and
an explicit uncertainty. The subject table is preliminary identification metadata, not canon proof.

Initial `subject_details` tokens are:

| Group | Tokens / meaning |
| --- | --- |
| Exterior views | `exterior`, `front_view`, `rear_view`, `side_view`, `top_view`, `underside_view`, `wide_view`, `close_up`; orientations are relative to the depicted subject. |
| Ship areas | `cockpit`, `engineering`, `corridor`, `galley`, `dining`, `lounge`, `quarters`, `cargo`, `boarding_access`, `hangar`; uncertain room identities must be qualified, and co-occurrence does not establish adjacency. |
| Assemblies/features | `hatch_door`, `window`, `seat`, `console`, `display`, `control`, `engine`, `landing_gear`, `grappler_arm`, `boarding_device`, `melfina_apparatus`, `gilliam_body`. |
| Appearance/content | `face_expression`, `body_pose`, `clothing`, `accessory`, `handheld_object`, `weapon_detail`, `signage_text`, `material_surface`, `lighting`, `energy_effect`. |
| Visible configuration | `deployed`, `stowed`, `open`, `closed`; identify the affected object in the summary. Static images establish visible endpoints only, not motion, direction or a complete operating sequence. |

Do not tag a room `engineering` merely because it contains machinery, or label a feature
`sub_ether_drive` without support. Add specific technical terms when supported, retaining unknown
identities otherwise. These lists describe observable retrieval features; gameplay plans and
reconstruction proposals belong in linked evidence/design records.

### Initial validation and review operation

Before Episode 4 screening, create and validate the authored rows and generated browsing view.
Check all locator keys join exactly once, all 9,204 baseline rows remain represented, mandatory
defaults are explicit, and no records are marked reviewed by initialization. Save screening
progress after each contact-sheet group; resume by image identity and state, never workbook row
number. A 24-image sheet is a navigation batch, not an assumed scene group.

Validate controlled values, canonical tag membership, duplicate tags, scene-group consistency,
reviewer/time pairs and conditional requirements above. Treat `UNREVIEWED` rows as blank authored
content with default enums; `SCREENED`/`NEEDS_RECHECK` require a visual summary and screening
provenance. `UNAVAILABLE` requires an obstacle and attempt provenance. Detail states require their
own provenance and evidence pointers. Schema version 1 is owned here; any future migration must
preserve notes, IDs and existing review states. ImportExcel/report regeneration must never write
back over authored annotations. No screening or Phase 3.2A execution occurs through this specification.

### Category-index initialization and first screening — 2026-10-26

- [category-index.csv](category-index.csv) is the authoritative authored table: 9,204 unique
  episode/image pairs, 21 fields, joined exactly once to the existing locators. Initialization
  set every row to `UNREVIEWED` / `NOT_REVIEWED`; it did not assign categories or scene groups.
- [category-review.xlsx](category-review.xlsx) is the ignored generated browsing view: Overview
  plus 26 episode tabs with filters, frozen identifiers/headers, image hyperlinks and all authored
  fields plus joined locator context. It is separate from the existing locator workbook.
- `category_index.py initialize` refuses an existing authored CSV. `validate` checks the full
  baseline, field contract, documented vocabulary, conditional requirements, UTC provenance and
  scene-group consistency/contiguity. `view-data` produces only a disposable join under `.tmp/`.
  The field/tag definitions above remain authoritative; the validator reads their controlled values.
- Refresh with `powershell -File tools/reference-extraction/build_category_workbook.ps1 -Python <python-executable>`.
  The Python environment needs no additional packages for category validation; workbook authoring
  uses installed ImportExcel 7.8.10. Reopening the saved workbook verified 285,324 displayed cells,
  9,204 image links and all episode summaries. The build checks that the authored CSV hash is
  unchanged before replacing the browsing view. No CSV notes are read back from the workbook.
- The first Episode 4 sheet, locators 1–24 / IDs 847835–847858, was visually screened as an
  integration trial. Opening presentation covers the first 17 sampled images; story presentation
  begins at locator 18 in this batch. Fourteen records are `SCREENED`, ten `NEEDS_RECHECK` and
  330 Episode 4 records remained `UNREVIEWED` at that initial checkpoint. Subsequent maintainer
  corrections below update the current counts. All 9,204 detailed-review states remain `NOT_REVIEWED`.
  Selected ambiguous subjects were inspected at full cached-image size; this remains category
  screening, without fine transcription, local timing alignment or completed mechanism analysis.
- High-priority revisit records in this batch are the opening XGP exterior (847840), caster and
  ammunition (847843), and asteroid-facility door (847857). Initial unresolved spacecraft/facility
  identities are superseded by the attributed corrections below; none of these views is relabeled
  as an XGP cockpit.

**Maintainer identification corrections — 2026-10-26:** locator 10 depicts Ron MacDougall, with
only the top of Harry's head at the bottom edge; the red background figures appear generic rather
than individually identified. Locator 14's mechanical figures are recurring space-pirate foot
soldiers. Locator 19 is Hilda's ship Horus; 20–21 show its cockpit with Hilda piloting. Locator 23
is the asteroid containing the XGP storage/awakening hangar, with large front bay doors reported
to open for ship passage. Locator 24 shows Horus approaching that asteroid before the crew transfer.
These supplied identities/context are attributed in `reported_context`; static observations remain
separate from reported movement and future actions. A subsequent maintainer clarification identifies
locator 22 as Gene, Jim and Melfina in Horus's passenger seats while Hilda flies them to the
asteroid; its identity recheck is resolved, with travel context retained as attributed information.
Current Episode 4 counts are **22 SCREENED / 2 NEEDS_RECHECK / 330 UNREVIEWED**. The remaining
recheck records are locators 7 and 8. No detailed-review state changed.

Five category-validator tests cover initialization refusal, stable-ID resume despite reordered
rows, overlapping tags, key/value failures, distinct recheck/unavailable/detail states and scene
groups. The gallery regression suite includes authored-status integration without annotation
mutation. Rendered workbook previews support layout checks; native Excel/VS Code viewer behavior
for this new workbook remains an owner-run check, not established by data verification alone.
All progress stays in this CSV/documentation pair, without a Markdown file per batch. Phase 3.2A
remains unstarted. The next Episode 4 navigation batch starts at locator 25 / image ID 847859.

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
