# Local AnimeHistory timestamp index

Selected character/lore/article context from AnimeHistory and Fandom is maintained in a separate
shared register, not additional editable columns in the generated locators. The
[context tool](../../../tools/reference-context/README.md) owns its accepted bounded workflow,
layout and validation. Reuse the authored image index's subject IDs and link sources without
overwriting survey observations or review status. The maintained context register and generated
workbook supplement the image survey; they do not mark images reviewed.

Source: [AnimeHistory Outlaw Star galleries](https://animehistory.org/anime/outlaw-star/) (EXT-001). These are sampled web screencap locator records, not annotated scene breakdowns or verified local-video times.

Initial cache completed October 6, 2026 (America/New_York): **26 episodes, 104 gallery pages, 9,204 records**, plus the series hub and robots guidance. All episodes have 354 unique records across four pages. Episode 4 covers 00:01:43–00:23:14. The combined index and all per-episode counts/IDs/cache hashes were verified. Retrieval timestamps in the records use UTC.

- [animehistory-review.xlsx](animehistory-review.xlsx) is the generated local browsing workbook: Overview plus EP-01 through EP-26 tabs, filters, frozen identifiers/headers and image hyperlinks. It contains locators only; no images or visual subject annotations are embedded. Open this for routine review.
- [all-episodes.csv](all-episodes.csv) combines the complete successfully parsed galleries and remains in this folder.
- `CSVs/episode-01.csv` through `CSVs/episode-26.csv` provide the authoritative individual episode records. Start with [Episode 4](CSVs/episode-04.csv).
- manifest.json records expected/actual counts, page URLs, retrieval timestamps, raw-HTML hashes, and coverage ranges.
- Original HTML and per-page retrieval sidecars live under ignored reference/cache/animehistory/. They can be reparsed without visiting the site. No screenshots, CSS, scripts, or other linked assets are downloaded.

## Ordered episode-review workflow

**Adopted — 2026-10-27:** this section owns the end-to-end sequence. The
[implementation plan](../../../docs/implementation/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research)
owns episode order and phase authorization; tool documents own commands and their validation.
The subtitle-context step is newly integrated here. Earlier batches are not retrospectively
described as subtitle-assisted; revisit their specific open questions when this step is applied.
Timing preparation and alignment-output cleanup were accepted with alignment-tool Stages 4–5
on 2026-10-27. Alignment occurs within each episode review, rather than as a full-show prerequisite.
These additions do not authorize later episodes or Phase 3.2A.

1. **Select the episode and resume point.** Follow the planned episode order: Episode 4 first,
   then 1–3 and 5–26. Read existing annotation/context records, unresolved questions and the last
   reviewed image key. Preserve completed work and stable IDs. Confirm available gallery locators,
   source caches and episode archive state; preparation does not mark images reviewed.

2. **Download or restore the gallery images.** Use the existing
   [gallery tool](../../../tools/reference-extraction/README.md#episode-gallery-review-tool--proposal)
   to prepare the selected episode, resuming verified cache entries. Restore an existing verified
   RAR when appropriate instead of downloading duplicates. Verify expected/cached/failed/missing
   counts, decoding and hashes. Keep unavailable images explicit; sampled gallery coverage is not
   full-video coverage. Source episodes remain immutable.

3. **Generate and verify contact sheets.** Use chronological 24-image sheets with stable image
   IDs, ordinals and web timestamp labels. Check the sheet registry, hashes, dimensions and ordered
   mapping to the locators; visually inspect representative layouts. Keep sheets in the episode's
   folder under `reference/contact-sheets/animehistory-review/`. Do not infer local-video timing
   or detailed machinery motion from the sheet labels or sampled endpoints.

4. **Prepare the website context.** Read the episode summary and reuse relevant existing context
   records. Retrieve only selected character, ship, location, equipment or lore pages needed for
   the episode through the [context tool](../../../tools/reference-context/README.md#proposed-routine).
   Inspect source sections and warnings, retain version/hash and attribution, and record concise
   useful assertions in the context register. Keep episode boundaries, continuity, interpretation,
   conflicting claims and uncertain identity matches explicit. Website assertions remain secondary
   unless separately corroborated within a stated primary-evidence scope.

5. **Prepare the subtitle context.** Reuse the full English dialogue ASS copy at
   `reference/working/performance-subtitles/episode-NN.ass`. Verify its hash, episode/source
   filename and selected track against the existing [subtitle coverage/provenance index](../performance-subtitle-coverage.json).
   Read the episode's full ordered dialogue, not just the earlier performance-keyword candidates,
   to understand names, speakers where supported, commands, action context and scene progression.
   Revisit surrounding lines while reviewing ambiguous images. These are translated English
   subtitles, not a verified English-dub transcript or original-Japanese transcription; formatting
   or an empty speaker field must not be turned into a guessed speaker identity. Preserve source,
   track/hash and local start/end intervals for substantive subtitle-based findings, using existing
   annotation/evidence fields and linked reviews. Full subtitle text remains ignored/local-only.
   Missing or mismatched copies are a recorded preparation gap; do not silently rerun the
   all-episode extraction or treat the performance-audit status as dialogue verification.

6. **Relate dialogue to scenes carefully.** Subtitle times follow the indexed local release;
   website times remain unaligned until matching shots are checked. Use narrative context to form
   identification leads, but do not automatically attach a subtitle to the numerically nearest
   gallery timestamp or assume a constant episode-wide offset. Record verified matches with their
   provenance; retain unverified associations as such. Dialogue can clarify a reported command or
   name without establishing which mechanism is visible, its dimensions or its complete motion.
   **Timing preparation, before timed dialogue/image associations:** follow the
   [accepted alignment procedure](../../../tools/reference-alignment/README.md#episode-alignment-procedure--accepted-2026-10-27).
   Validate existing anchor/mapping records and check current input identity where available.
   Reuse a supported direct interval or bounded mapping for navigation; when coverage is missing,
   record the gap or obtain scoped authorization for bounded matching rather than extrapolating.
   Declare FIT/HOLDOUT roles before searches, visually assess candidates, retain durable
   provenance and independently validate a proposed mapping before using estimates. Refresh the
   category workbook and distinguish direct, estimated, player-lead and unmapped timing.
   The pinned Episode 1 release has a validated navigation offset of -1.388 s only for whole-second
   web labels 06:40–20:40; other regions/episodes remain unmapped. The tool doc owns the
   [measured limits](../../../tools/reference-alignment/README.md#stage-3-validation-results--2026-10-27).
   A two-second navigation search window is not a verified subtitle-to-frame association.
   Generated locator fields and existing review states remain unchanged.

7. **Review a bounded image batch.** Normally inspect three sheets (up to 72 images) together,
   with selected full-size checks for ambiguous identities or valuable details. Record individual
   visible summaries, overlapping category/subject/detail tags, presentation, chronological scene
   groups, confidence, priority, revisit reasons and screening provenance. Use the websites and
   subtitles during the review rather than deferring every ambiguity to maintainer recollection.
   Keep visible content, translated dialogue, secondary claims and attributed maintainer context
   distinguishable. INITIAL_REVIEW_COMPLETE records annotated-survey depth; NEEDS_RECHECK can
   remain for a material identity or interpretation question. Do not promote to targeted
   PARTIAL/REVIEWED without the required scoped evidence record.

8. **Report findings and incorporate corrections.** Present a bulleted batch review with image
   ordinals/ranges, distinctive per-image callouts, valuable references and remaining questions.
   Incorporate supplied corrections with attribution. Register supplemental manual screenshots
   with stable episode-specific IDs, original hashes, local-player times, provenance and relevant
   gallery associations; do not fabricate archive alignment or drop unsupported uncertainty.
   Reuse existing context records and add justified links rather than duplicating claims or
   overwriting existing observations.

9. **Validate, refresh and repeat.** Validate image/supplement annotations, context records,
   source caches, link targets and review-state requirements. Check that out-of-batch records,
   stable IDs and the full locator inventory are preserved. Refresh the generated ImportExcel
   category/context workbooks, verify saved values/links and inspect affected views. Authoritative
   edits remain in the textual records. Continue from the next pending image key within the
   authorized episode, repeating steps 6–9; no batch download or workbook refresh counts as review.

10. **Check episode coverage and unresolved work.** Account for every sampled locator and
    registered supplement, preserving unavailable/unreviewed states and named recheck queues.
    Reconcile corrections and useful source/subtitle context; retain targeted full-size/video,
    translation and design questions for later work. Do not call incomplete coverage complete or
    require every reconstruction question to be settled before finishing an initial survey.

11. **Archive and remove expanded episode images.** Follow the accepted
    [retention/recovery procedure](../../../tools/reference-extraction/README.md#episode-retention-and-supplement-recovery--accepted-2026-10-26):
    package gallery originals and all registered episode supplements in the episode RAR; verify
    integrity, staged restoration, inventory and hashes before promotion or pruning. Then remove
    both expanded gallery images and registered supplemental originals. Retain contact sheets,
    sheet registry, RAR/recovery receipt, maintained records and generated workbooks. Verify final
    status and refresh availability displays. Cited website caches and existing subtitle copies
    have separate provenance/retention and are not deleted by episode-image pruning. Remove only
    identified disposable preparation/preview artifacts; do not sweep unrelated working files.
    **Before gallery pruning**, run the alignment tool's Stage 5 episode-finish preview. Check
    durable assessments/provenance, explicitly retain unresolved runs with `--keep-output`, or
    apply the inspected preview token to eligible owned runs. Failed/abandoned unregistered runs
    require explicit discard; no candidate is accepted merely to enable cleanup. Verify that no
    unnecessary alignment PNGs, comparison sheets or run directories remain. These reproducible
    search outputs do not enter the episode RAR; gallery originals and registered supplements do.
    Finish current-media/reproduction checks while required gallery inputs are available; after
    pruning, restore verified inputs before requesting a fresh source/gallery verification.

12. **Record the checkpoint and next scope.** Summarize coverage, retained artifacts, cleanup
    evidence and unresolved questions. Leave changes uncommitted until confirmation through the
    existing Git workflow; confirmation may cover several batches rather than require a commit
    after each one. Advance to the next episode only within explicit scoped authorization.
    The later Power BI/cross-episode synthesis and Phase 3.2A boundaries remain unchanged.

## Episode 1 preparation — 2026-10-26

Authorized preparation downloaded all 354 sampled gallery images (IDs 846773–847126,
web locators 01:43–22:03) and generated 15 chronological 24-image contact sheets; the final
sheet contains 18 images. Cache decoding/hashes, all sheet hashes/dimensions (1600×2056),
and all 354 ordered ID/time mappings passed. Early, middle and final layouts were inspected.
Gallery originals occupy 60,722,405 bytes and sheets 51,022,124 bytes. No Episode 1 RAR exists
yet; expanded images remain available during review, with verified archive/prune at episode end.

The source-context preparation reuses the cached AnimeHistory Episode 1 synopsis and Hilda
biography and adds selected Fandom Outlaw World and Starwind and Hawking articles. Six concise
SECONDARY_ONLY records (CTX-000019–000024) preserve disguise, opening-Horus, case/computer,
caster and headquarters context. The biography's Episode 1/2 boundary and the headquarters
article's Sentinel III/Heifong distinction remain explicit. No context-to-image links were
inferred, and all 354 Episode 1 annotation rows remain UNREVIEWED/NOT_REVIEWED pending the
annotated survey. The context workbook was refreshed and checked; existing image/supplement
annotations are unchanged. The next review batch is sheets 1–3, locators 001–072.

### Episode 1 annotated survey — sheets 1–3

Locators 001–072 (846773–846844; web labels 01:43–05:48) received individual descriptions,
overlapping tags, 15 chronological scene groups and INITIAL_REVIEW_COMPLETE status. Fifty-one
are SCREENED and 21 retain NEEDS_RECHECK; remaining 282 locators are unreviewed. All three sheets
and full-size locators 028, 045, 054 and 058 were inspected. Opening/title material is distinguished
from story footage. Launch-site craft/location, goggled pilot/craft, certain display/emitter views
and the glass imagery remain explicit rechecks. Horus identity uses the previously identified
Episode 4 form plus secondary Episode 1 context; no complete chase action or propulsion model
was verified. A shorter cone configuration is visible across 055–056, without assigning its function.

The bounded lookup added cached Roi Fong, Guugaku and Soi Len appearance descriptions, four
SECONDARY_ONLY context records (CTX-000025–000028) and selected image associations. Proper-name
matches to the existing pirate-leader IDs remain candidates; no earlier Episode 4 IDs were renamed.
Guugaku's neck-bolt description and Clyde's Bar signage support preliminary subject tags. The
city/globe remains a Sentinel III context lead rather than a verified location match. No new manual
supplements, primary source-video inspection, translation or timing alignment occurred.

Workbook refresh preserves ISO UTC review timestamps as text, using the same date-conversion
guard as the context builder. Maintained annotation validation, saved workbook equality and
preservation of all out-of-batch rows are checked before reporting the batch. Next: 073–144.

### Episode 1 subtitle-context follow-up — 2026-10-27

The complete 293-event English ASS track was read and its registered hash/source identity verified.
The [scoped review](../episode-01-subtitle-context-review.md) and
[bounded decode provenance](../episode-01-subtitle-context-frames.json) record the first-batch
follow-up. All three sheets and selected full-size images were revisited; 19 three-second local
windows supplied scene checks without extending the validated timing mapping or assigning exact
gallery-frame timestamps. No later gallery annotations or secondary context records were changed.

The launch sequence in 011–019 is corrected from OPENING to pre-title STORY. Pirate fighter/pilot
roles, pursuit commands, damaged-Horus/sub-ether context and Sentinel III's establishing identity
are clearer. The maintainer identifies Horus's four yellow rear-pylon units as sub-ether drives;
the wider local view corroborates four assemblies, with spin-up/configuration details and limits
in the linked review. The glass in 071 repeats the visitor's face, distinct from the bartender;
its precise optical treatment remains open.

Only 58 rows changed: 011–019 and 024–072 have PARTIAL status for this targeted context check,
not completed mechanism/translation verification. First-batch totals are now 60 SCREENED and
12 NEEDS_RECHECK, with 58 PARTIAL and 14 INITIAL_REVIEW_COMPLETE. All remaining 282 Episode 1
locators and every other episode/supplement remain unchanged. Next: 073–144 after this follow-up;
the full subtitle read does not mark those later images reviewed.

**Subsequent maintainer clarifications:** figure 007 is Gene; 034 is the fighter launch tunnel,
037 the fighter targeting screen, 038 the incoming missile salvo, 042 Horus's return-fire missile
launchers, and 045–046 a deployed defensive pod described tentatively as laser-based. The faceted
glass's physical implementation is deferred rather than an unresolved scene identity. The
Sentinel launch-site attribution remains tentative. Current first-batch counts are **65 SCREENED /
7 NEEDS_RECHECK**, with 58 PARTIAL and 14 INITIAL_REVIEW_COMPLETE. Only launch-scene locators
011–014 and 016–018 remain flagged. A total of 59 first-batch gallery rows changed across the
follow-up and clarifications; later rows remain untouched.

**EP-01-MAN-001** preserves the supplied Horus salvo screenshot at player label 04:05, linked
contextually to locator 042. Its ten-record supplemental register retains the original hash,
player-time basis and uncertainty. Likely at least four launchers remains a tentative estimate,
separate from the visibly four yellow drive assemblies. The screenshot remains local and will
be bundled into Episode 1's RAR at completion through the accepted retention procedure.

## Using the records

Search/filter CSVs by episode_id or web_seconds/web_timestamp. Each row has the source caption, image ID/URL, gallery/page URL, retrieval time, and source HTML digest. Image links still require internet access; caching the HTML does not make the images available offline. Opening cached HTML in a browser may load remote resources, so use the CSV index for offline lookup.

All alignment_status values initially read UNVERIFIED and local_timestamp is empty. Web times are second-resolution locator labels, not frame-accurate PTS. Validate recognizable matching shots against the local source before using them for extraction. Record confirmed matches in authored scene/evidence records rather than editing these generated CSVs; rerunning the generator replaces its outputs.

A gallery's 354 records do not guarantee every scene or the full episode runtime is covered. Review the first/last timestamp in the manifest; gaps/openings/endings can be excluded by sampling. Counts verify the records against the website's declared count, not the authenticity, timing accuracy, resolution, or completeness of the underlying anime footage.

## Authored category index and future Power BI view

**Planning requirement — 2026-10-26:** design the authored category index for later Power BI
reporting. Complete the all-episode annotated survey, then prepare and validate a research report
before question-driven cross-episode deep dives. The authored index and generated category
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
| `presentation` | Required single value: `UNKNOWN`, `STORY`, `FLASHBACK`, `OPENING`, `ENDING`, `RECAP`, `PREVIEW`, `EYECATCH`, `TITLE_CARD`, `END_CARD`, `OTHER`. Classify the sampled presentation, not an assumed source episode for reused footage. `FLASHBACK` identifies an embedded memory/past-event sequence; it is distinct from an episode recap. |
| `screening_status` | Required: `UNREVIEWED`, `SCREENED`, `NEEDS_RECHECK`, `UNAVAILABLE`. |
| `detail_status` | Required: `NOT_REVIEWED`, `INITIAL_REVIEW_COMPLETE`, `PARTIAL`, `REVIEWED`. Review depth independent of screening/identity status. Initial means the annotated survey is complete; partial/reviewed refer to a documented targeted deep dive, not universal verification of every visible detail. |
| `identification_confidence` | Required: `NOT_ASSESSED`, `HIGH`, `MEDIUM`, `LOW`. Applies to subject identification only, not canon/timing/detail accuracy. Where identities differ in confidence, use the lowest assessed confidence and identify the uncertain subject in `uncertainties`. |
| `visual_summary` | Concise visible content; do not copy generated captions as observations or place recollections here. |
| `research_priority` | Required: `UNASSESSED`, `HIGH`, `NORMAL`, `LOW`. Priority for further reference work, not canonical authority. |
| `revisit_reason` | Specific reason to return, such as a useful rear view, uncertain doorway relationship or mechanism endpoint. Required for `HIGH` priority. |
| `uncertainties` | Identification doubts, illegible text, contradictions and questions for closer inspection/video. Required for `NEEDS_RECHECK` or assessed `LOW` confidence. For `UNAVAILABLE`, record the inspection/access obstacle. |
| `reported_context` | Attributed recollections or supplied interpretations, distinguished from visible observations. Include who supplied the context; blank when none. |
| `screened_by` | Reviewer identity for the latest screening/recheck attempt, including unavailable outcomes. A name here does not imply maintainer acceptance. |
| `screened_utc` | ISO 8601 UTC timestamp for that attempt; blank for untouched records. |
| `detail_reviewed_by` | Reviewer identity for the latest targeted deep dive; blank for not-reviewed/initial-review-complete. Initial survey provenance stays in screened_by/screened_utc. |
| `detail_reviewed_utc` | ISO 8601 UTC timestamp for that targeted deep dive. |
| `detail_references` | Semicolon-separated repository-relative evidence links/anchors for later detailed findings. Required when `detail_status` is `PARTIAL` or `REVIEWED`; do not store detailed canon claims solely in this screening table. |

`SCREENED` means sufficient visual inspection to assign preliminary tags, including images with
no current research value. `NEEDS_RECHECK` means inspected but a material classification remains
unresolved; retain candidate tags so uncertain XGP references stay discoverable. `UNAVAILABLE`
means not visually inspected because the image could not be accessed/decoded; retain previous
notes if any. These are mutually exclusive current states, not an audit history. The workbook/report
must show them separately. Detail review does not automatically resolve uncertain classifications.
Git retains published annotation history; do not add a Markdown record for each screening batch.

### Annotated survey and targeted review depth — accepted 2026-10-26

The episode survey is the main initial review, not merely automated sorting. Record individual
visible descriptions, useful overlapping tags, scene/state context, selected full-size checks,
research priorities, uncertainties, maintainer corrections and supplemental references as needed.
Preserve these findings for reuse; a later pass must not repeat already-answered descriptions.
Survey in bounded contact-sheet batches, with concise grouped reports and image-specific callouts.

Use `INITIAL_REVIEW_COMPLETE` when that annotated review is complete for the image. This is an
explicit assessment, not an automatic consequence of downloading a cache or setting SCREENED.
An image may be INITIAL_REVIEW_COMPLETE while still NEEDS_RECHECK for an unresolved identity:
review depth and open questions are separate. UNREVIEWED/UNAVAILABLE images cannot carry this
completed initial-review status. NOT_REVIEWED remains the default for unreviewed images and
limited preliminary sorting that has not reached the annotated-survey level.

PARTIAL and REVIEWED are reserved for question-driven deep dives with their own reviewer/time
and evidence references. Evidence must state the question, findings and remaining limits; REVIEWED
means the stated review scope is complete, not that dimensions, dialogue and animation are all
verified. Deep dives are triggered by modeling/design needs or material uncertainties: compare
full-resolution views for shape/fit, inspect continuous footage for motion, verify specific text
or dialogue, reconcile conflicting evidence or align missing shots/timestamps. There is no required
second review of every image, XGP candidate or non-XGP category. A high revisit priority is a
research lead, not an automatic task or blocker to 3.2A.

The all-episode survey still precedes the planned Power BI report; targeted XGP evidence synthesis
and only the deep dives necessary for the first increment follow it. Research-readiness acceptance
and separate 3.2A authorization remain required. The implementation plan owns those gates.

**Initial-status adoption — 2026-10-26:** the completed Episode 4 annotated survey (354 gallery
records, including unresolved locator 007) and nine manual supplements are assessed as
INITIAL_REVIEW_COMPLETE. Existing annotations, screening states, source/timing limits and initial
review provenance are preserved. No targeted-review dates, reviewers or evidence claims are
manufactured. The other 8,850 gallery records remain NOT_REVIEWED. The additive enum preserves
the 21-column schema, stable IDs and existing PARTIAL/REVIEWED meanings; projections must refresh.

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
| `horus_dropship` | Detachable crew-transfer craft carried by Horus; maintainer identification distinguishes it from the parent vessel in the asteroid-entry sequence. |
| `ship_anchor` | Ship-launched tethered anchor hardware, identified by the maintainer; common equipment class does not imply identical mechanisms on every vessel. |
| `jim_satchel` | Jim's carried satchel; contents and recurring inventory are not established. |
| `xgp_maintenance_robot` | Small blue rail-mounted maintenance unit seen in the XGP passage/cockpit; physical unit identity does not establish its full capabilities or a ship-wide rail route. |
| `hilda_laptop` | Hilda's folding portable computer used at the XGP cockpit station; keep distinct from Melfina's transport case. |
| `hilda_wrist_controller` | Hilda's wrist controller/communicator, identified by the maintainer; reported uses include contacting Horus's AI and remotely commanding the ship/dropship. |
| `hilda_grappling_device` | Hilda's handheld hook/line device used during the Episode 4 tether traversal and final confrontation, identified by maintainer action context; distinct from ship-launched anchors. |
| `pirate_attack_ship` | Blue/orange spacecraft attacking the crew at the asteroid in Episode 4, identified by the maintainer; proper vessel name remains unassigned. |
| `pirate_away_team_leader` | Bald, mustached pirate leader portrait in Episode 4 locator 115; maintainer identifies his away-team leadership role, without a confirmed proper name. |
| `pirate_shipboard_leader` | Dark-haired female pirate leader with pink hair ribbons in Episode 4 locator 182; maintainer identifies her as directing the attack from the blue/orange vessel, separately from the asteroid away-team leader. Proper name remains unassigned. |
| `pirate_main_section` | Main section of the blue/orange pirate attack ship, reported to separate from its grappler section and block the asteroid hangar exit. Component role is maintainer-supplied context. |
| `pirate_grappler_section` | Detached grappler section of the blue/orange pirate attack ship, reported and visibly shown gripping Horus in Episode 4 locators 216–217. Keep distinct from the main section blocking XGP. |
| `el_dorado` | MacDougall brothers' gold spacecraft, identified by the maintainer in Episode 4 locators 230 and 234–239; compare SET-107/112 for exterior and launcher references. |
| `halcyon_missile` | Large El Dorado underside missile identified by the maintainer in supplemental references EP-04-MAN-003–007; compare SET-112's ハルシオン・ミサイル. Halcyon is a provisional Latin rendering, distinct from El Dorado's smaller nose-launched missiles. |
| `gene_escape_pod` | Escape pod associated with Gene's childhood rescue in the Episode 4 flashback, identified from maintainer sequence context; do not transfer its design to Horus's dropship or other escape craft. |
| `pirate_landing_craft` | Green pirate landing/dropship units identified by the maintainer in Episode 4 locator 167; reported landing-foot action is retained separately from still-image observations. |
| `xgp_hangar_asteroid` | Asteroid containing the Outlaw Star's storage hangar and awakening setting, identified by the maintainer; door motion and transfer context remain reported until checked in video. |
| `starwind_hawking_hq` | Starwind & Hawking premises; identification does not establish a planet/location without supporting evidence. |
| `guugaku` | Bald Kei pirate with large neck bolts; Episode 1 identification uses the cached secondary appearance description and visible features. |
| `pirate_fighter`, `pirate_fighter_pilot` | Episode 1 pursuing fighter craft and goggled pilot, identified through the bounded subtitle/scene check. The pilot's personal name and exact readiness-call attribution remain unassigned; do not equate the craft with Episode 4's landing units automatically. |
| `sentinel_iii` | Planet named by the Episode 1 establishing narration, corroborated against local globe/city views; does not identify the separate pre-title launch facility. |
| `gene_modular_blaster` | Descriptive Episode 1 ID for the purple revolver-style blaster and fitted component kit, supported by short-barrel-blaster dialogue. Distinct from the gold caster; no model/caliber or full modification mechanism established. |
| `melfina_transport_case` | Reinforced transport trunk revealing Melfina in Episode 1; distinct from the XGP pod/apparatus and Hilda's laptop. No complete life-support specification implied. |
| `blue_heaven` | Asteroid free town identified in secondary Episode 2 preparation and local dialogue; distinct from the XGP storage asteroid. No image match or measured layout established by preparation. |
| `swanzo` | Corbonite mechanic associated with Blue Heaven in selected secondary context; image identification and containment-suit details require scoped review. |
| `mccoy` | Named Episode 2 bar antagonist in the captured synopsis; standalone wiki lookup returned NOT_FOUND. No appearance or individual attacker identification assigned during preparation. |
| `starwind_hawking_car` | Descriptive continuity ID for the red open-top classic-style car used by Gene and Jim in Episode 1. No verified model designation, legal ownership or complete propulsion mechanism implied. |
| `club_temptation` | Club identified by the visible Episode 1 sign and secondary scene context CTX-000034; its private-room companion remains unnamed. |
| `clydes_bar` | Clyde's Bar exterior/interior in Episode 1; visible entrance sign and secondary episode context support identification. |
| `rob_cain`, `clyde` | Rob Cain / Death Rob and Clyde, identified through the Episode 1 confrontation and aftermath subtitles. Secondary Rob Kane spelling is an alias, not a separate person. |
| `iris` | Green-haired woman at Clyde's Bar, identified by the maintainer; cached summary caption CTX-000029 and Iris biography CTX-000032–033 provide separately attributed secondary context. |
| `jim_pda` | Jim's dark blue hinged handheld device; PDA/diagnostic role is secondary context (CTX-000030). Its rear-facing image does not verify a readable interface. |
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
| Identified drive hardware | `sub_ether_drive` for supported sub-ether-drive component references; Horus's yellow cone units are identified by the maintainer with Episode 1 escape-dialogue corroboration. Keep component motion and other ships' designs separately qualified. |
| Access and equipment details | `tether_cable` for a visible cable/tether without an assumed anchoring mechanism; `thruster` for visible propulsion nozzle/jet imagery; `entry_control` for local access-control hardware; `portable_computer` for folding/portable computing equipment; `instrument_panel` for grouped gauges and indicators. |
| Anchor and carried bag | `anchor` for identified anchoring hardware; `satchel` for a carried soft-sided bag, without an assumed contents list. |
| Graphic framing | `circular_view` for circular-masked images without asserting a camera technology; `registration_overlay` for portrait/status graphics associated with the established registration sequence, without inferring a biometric algorithm. |
| Systems and action retrieval | `wraparound_display` for enclosing cockpit screen surfaces; `instruction_graphic` for onboard instructional imagery; `schematic` for line/diagram depictions rather than physical geometry; `wrist_device` for worn electronic hardware without assumed function; `maintenance_robot` and `guide_rail` for the observed maintenance-unit assembly; `projectile` for visible ammunition/rocket-like objects without identifying an ether weapon. |
| Appearance/content | `face_expression`, `body_pose`, `clothing`, `accessory`, `handheld_object`, `weapon_detail`, `signage_text`, `material_surface`, `lighting`, `energy_effect`. |
| Reported magic imagery | `magic_effect` for imagery associated with an identified magic action in supplied or verified context; describe the visible light/field separately, without assuming a full magic system or treating every transparent helmet as magic. |
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
provenance. `UNAVAILABLE` requires an obstacle and attempt provenance. INITIAL_REVIEW_COMPLETE
uses the recorded initial-survey provenance; PARTIAL/REVIEWED require separate targeted-review
provenance and evidence pointers. Schema version 1 is owned here; any future migration must
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
At the end of the first-sheet checkpoint, Episode 4 counts were **22 SCREENED / 2 NEEDS_RECHECK /
330 UNREVIEWED**, with locators 7 and 8 needing recheck. No detailed-review state changed.

Five category-validator tests cover initialization refusal, stable-ID resume despite reordered
rows, overlapping tags, key/value failures, distinct recheck/unavailable/detail states and scene
groups. The gallery regression suite includes authored-status integration without annotation
mutation. Rendered workbook previews support layout checks; native Excel/VS Code viewer behavior
for this new workbook remains an owner-run check, not established by data verification alone.
All progress stays in this CSV/documentation pair, without a Markdown file per batch. Phase 3.2A
remains unstarted. Subsequent screening progress is recorded below and in the authored CSV.

### Episode 4 category survey progress

**Sheets 2–4 — 2026-10-26:** locators 25–96 / image IDs 847859–847930, web labels
00:03:11–00:07:31. All 72 received individual visible-content summaries, overlapping tags and
chronological shot/group membership; the pre-existing first-sheet annotations and other episodes
were preserved. Three contact sheets and selected full-size cached images were visually inspected.
No new downloads, video extraction, timing alignment, Japanese transcription or detailed-review
completion occurred. Existing bootstrap/cockpit reviews supply contextual identity comparisons,
not exact web-to-local timestamp matches.

| Range | Preliminary grouping / revisit value |
| --- | --- |
| 25–32 | Horus anchors outside the asteroid; its detachable dropship transfers the crew through a smaller side gate. Maintainer corrections identify anchor use (25), dropship detachment/flight (28), side entrance (29), gate opening (31) and dropship entry (32); action context is attributed rather than established from static samples. Nearby passenger/pilot views are grouped with this dropship sequence. |
| 33–40 | Episode title card; crew at an entry doorway; grey-green XGP exterior components and hangar reveal. High-value hull detailing (35–37) and ship/truss/crew compositions (39–40). No paint history, support load path or scale measurement established. |
| 41–50 | Hangar crew, handled computer case, Jim's green satchel (44; maintainer identification, contents unknown), Melfina outfit views, circular entry-button array, boarding hatch and passage. Key access references are 47–49; no complete pressure cycle, door trajectory or measured corridor route inferred. |
| 51–60 | Dim cockpit, seat backs/hoses/hand controls, Hilda's laptop staging and overhead seating views. Especially useful for cockpit spatial and operator-reach review; retain per-image visible subjects rather than copying the entire crew to every reaction crop. |
| 61–66 | Laptop graphical bootstrap endpoints, analog-style gauge cluster and brightened cockpit compositions. Intermediate countdown states are absent from these gallery samples; no exact protocol, keystroke sequence or numeric gauge reading assigned. |
| 67–84 | Gilliam overhead housing, contrasting illuminated/dark sectors, crew reactions and cockpit overview. Locator 78's circular-framed overhead composition is a high-value spatial reference; circular masking does not identify a camera technology. |
| 85–96 | Hilda, Gene, Jim and Melfina portrait/reaction views, portrait/status cards, isolated Hilda card, wide cockpit/headroom views and further Gilliam samples. No biometric algorithm or exact animation timing inferred. |

**Maintainer corrections — 2026-10-26:** Horus uses fired tethered anchors to secure itself to the
asteroid, later turning it to shield Horus from pirate fire. The maintainer also recalls XGP anchors
used on the advertisement ship in the bomb-threat/heist episode; retain this as an unverified
cross-episode retrieval lead, without assigning an episode number or treating that sequence as
reviewed. The smaller side gate admits Horus's detachable dropship while the parent vessel remains
anchored outside; this is distinct from the large ship-exit bay doors. Locators 28–32 retain the
supplied detachment, gate-opening and entry context in their attributed notes. Jim's satchel is
identified in locator 44; its contents remain unknown rather than labeled as tools or normal inventory.

**Sheets 5–7 — 2026-10-26:** locators 97–168 / image IDs 847931–848002, web labels
00:07:34–00:11:54. All 72 were individually described and tagged after contact-sheet inspection;
selected full-size images resolved hardware/scene distinctions. Earlier annotations, the two manual
references and untouched episode/gallery records were preserved. Existing startup/cockpit/robot
reviews provided identity comparisons without declaring exact gallery-to-local timing alignment.

| Range | Preliminary grouping / revisit value |
| --- | --- |
| 97–110 | Cockpit crew exchange and wraparound information display. Locators 105–107 are strong central-field/side-screen/Gilliam composition references; decorative display wording is not technical specification. |
| 111–117 | Hilda's wrist controller/communicator, exterior vessel context, blue/orange pirate attack ship (114), pirate away-team leader (115) and dark Horus hull/markings. Maintainer supplies the controller/AI/remote-command roles; proper ship and leader names remain unassigned. |
| 118–130 | Hilda at the cockpit exit; remaining crew; Melfina beside the apparatus floor cap; Jim climbing into a seat; Gene seated without his coat; forward instructional display. Useful doorway/seat/cap references at 125–130. |
| 131–140 | Low/short-raised apparatus states, Gene/Jim seat layout, then Hilda back in the main Horus cockpit (maintainer clarification) and a twin-bodied vessel schematic. Locator 137's drawing remains an onboard representation, not measured hull geometry. |
| 141–148 | Asteroid/space attack context followed by Melfina inside the blue-green apparatus, including relaxed and crossed-arm poses and closed/open eyes. No fluid composition or biological mechanism established. |
| 149–162 | Tall apparatus shell behind the seats, shielding/aperture views, seated character/control relations, small blue maintenance unit and its rail, and Gilliam housing. Major later-detail candidates include 149, 152, 154–155 and 161–162. Rail continuity, shell travel and numerical clearances remain unmeasured. |
| 163–168 | Gene reaction, Horus exterior amid bursts, Hilda in the main Horus cockpit, green pirate landing-craft designs (167; maintainer identification) and Hilda reaction. Landing-foot operation remains attributed context pending video review. |

**Maintainer corrections — 2026-10-26:** locators 111–112 show Hilda's controller/communicator
used to contact Horus's AI, issue remote ship commands and summon/control its dropship. The
maintainer describes the AI as similar in role to Gilliam; this does not identify a shared technical
implementation or establish a complete command set. Locator 114 is the attacking pirate ship,
retained as a later awakening-expansion reference. The pirate-leader description supplied with
the number 116 is attached to the actual portrait at locator 115; locator 116 remains a Horus hull
view. The leader is reported to command the pirate away team entering the asteroid to seize XGP.
Hilda's later cockpit views are identified as the main Horus cockpit, resolving the parent-versus-
dropship rechecks. Locator 167 shows pirate landing craft reported to descend and plant a foot
against the asteroid; preserve this as a later landing/boarding animation research lead. These
future-use notes do not expand the accepted awakening slice or authorize implementation.

**Sheets 8–10 — 2026-10-26:** locators 169–240 / image IDs 848003–848074. All 72 received
individual descriptions and tags after contact-sheet inspection, with selected full-size checks.
The pass adds 72 `SCREENED` records after the maintainer's El Dorado identification. Earlier annotations, manual
supplements and untouched gallery rows remain unchanged.

| Range | Preliminary grouping / revisit value |
| --- | --- |
| 169–175 | Jim and the passage maintenance unit, engineering cylinder faces/manual access (170–171), closed doorway, XGP inside the hangar and the pirate away team. No measured clearances or complete route inferred. |
| 176–179 | Mid-episode eyecatch (176–178), followed by the XGP intrusion warning (179). Presentation and warning role follow maintainer context; unclear Japanese is not guessed. |
| 180–188 | Horus under fire, shipboard female pirate leader, Hilda at the main Horus controls, reported anchor-assisted asteroid pivot (185–186), and separated pirate-vessel assemblies (188). |
| 189–199 | Pirates in the hangar, Gene firing through/standing at the XGP hull hatch, passage Gilliam, and main-gate venting (198). Gun model remains unassigned; the gate timing, command and purpose are attributed action context. |
| 200–211 | Pilot/apparatus relationship, key/socket control (201), extended engineering cylinders (202), startup graphic (203), low cockpit layout (204), Melfina shell framing and the main pirate section blocking the gate (208). |
| 212–221 | Pirate main section firing, close Horus hull/contact views, detached grappler gripping Horus (216–217), enemy through the XGP forward view, Gilliam and joystick detail (221). The tight crop at 214 does not establish an attacker or mechanism. |
| 222–229 | Away-team leader among hangar beams, cockpit reactions and incoming glare; body poses, seat/control relations and lighting references. |
| 230–240 | El Dorado gold craft (maintainer identification), asteroid explosions, Ron portrait, Hilda reaction, El Dorado/projectiles and grappled Horus beside the blast. The maintainer identifies 239 as the initial smaller nose-launched missiles, distinct from the large underside Halcyon missile. Compare SET-107/112. |

**Maintainer action context — 2026-10-26:** the female leader in 182 directs the attack from the
blue/orange pirate ship while the male leader commands the asteroid assault. Horus uses anchors
to pivot the asteroid for protection at 185–186. Gene has Gilliam briefly open the main hangar
gate to vent invading pirates at 198. At 208, the detached main pirate section blocks the exit;
the separate grappler section attacks and grips Horus at 216–217. These descriptions are retained
in `reported_context` separately from visible still observations; they are not a timed video
verification or approval to expand implementation. Main section, grappler section and shipboard
leader have separate retrieval tokens; their proper names remain unassigned.

**El Dorado clarification — 2026-10-26:** the maintainer identifies the gold craft as El Dorado,
operated by the MacDougall brothers. Reported story context: pirates previously hired them to find
Hilda and XGP; after that contract ended, another client hired them and they double-cross the
pirates in this encounter. The maintainer associates the attack with the large underside missile
depicted in SET-112. That sheet's existing reading is `ハルシオン・ミサイル`, provisionally rendered
**Halcyon missile**; official Latin spelling remains unverified. This resolves the gold-craft
identity rechecks. A subsequent maintainer clarification identifies 239 as the initial smaller
missiles fired from El Dorado's nose launchers, distinct from the large underside Halcyon missile.
Contract history, firing sequence and exact launcher-to-shot matches still require video/dialogue
verification in a later detailed pass. SET-107/112 are cross-references, not new detailed reviews.

**Sheets 11–13 — 2026-10-26:** locators 241–312 / image IDs 848075–848146, web labels
00:16:21–00:20:40. Contact sheets and selected full-size images support 72 individual annotations:
67 `SCREENED`, five `NEEDS_RECHECK`. Previous annotations and all seven manual supplements are
unchanged. `FLASHBACK` is added to the presentation vocabulary for embedded memory/past-event
sequences; no existing presentation values are remapped.

| Range | Preliminary grouping / revisit value |
| --- | --- |
| 241–249 | Ron at the El Dorado station, asteroid damage, pirate leaders, XGP in the hangar and Gilliam over the circular forward display/interference. The clear camera feed after 249 is supplied context, not a sampled frame here. |
| 250–254 | Gene recognition/memory sequence, classified FLASHBACK from maintainer context: white transition, pod-related hardware, burning ship/pod/El Dorado staging and young Gene. Locator 254 is a present-day-looking reaction associated with the memory sequence, not a childhood-design assertion. |
| 255–264 | Reported missile order, Harry reaction, Ron monologue, pirate vessel/glow, Hilda and El Dorado against the star. MAN-003–007 retain deployment/firing/flight inserts. The glow at 260 is not identified as a shield or physical gravity contour. |
| 265–279 | MacDougall portraits, stellar exterior, pirate grappler, trajectory graphic (270–271), pirate/Hilda reactions and debris. Display/voiceover ownership follows maintainer context; selected Japanese labels are separate from unverified dialogue and physics. |
| 280–289 | Reported asteroid breakout at 280, 281 and 283, excluding 282. Major XGP hull/arm-root and broken-rock exit references; raised Gene/Jim seat/control relationships at 284–287. |
| 290–299 | Pirate leaders, grappler section during escape, Hilda/craft views, XGP cockpit, pirate green-hatched boarding hand (297), XGP hand/wrist (298) and leader reaction (299). Crushing/death and throwing action remain attributed context. |
| 300–312 | Powered pirate anchor (302), tether across XGP wrist (303), thrust/tether staging, dropship exterior (307), Melfina behind the slotted shell (308), crew reactions and suit equipment (312). Later Hilda/anchor outcome is deferred to the final set. |

**Maintainer sequence context — 2026-10-26:** Gene recognizes El Dorado on Gilliam's camera feed,
recalling his father's contract killing by the MacDougalls and escape-pod rescue. Pirate-ship
voiceover at 270–271 explains the stellar gravity-well danger. XGP breaks through damaged rock
because the main gate is unusable. During escape, damaged Horus prompts Hilda's planned dropship
abandonment and XGP-grappler catch. The pirate grappler section turns back; its green-hatched
boarding hand carries the male leader. XGP's hand crushes it, killing the leader, and Gene throws
the pirate vessel behind. The anchor at 302 reportedly diverts the dropship and restrains XGP's
arm. These action/backstory reports remain in `reported_context`, distinct from visible stills,
verified dialogue, measured mechanics and implementation scope. No final rescue/fate interpretation
is assigned by this pass.

**Shot-ownership corrections — 2026-10-26:** the maintainer confirms Hilda's main Horus cockpit
at 293 and the main Horus ship in the background of 294. Locators 301 and 306 show the dropship
cockpit. Locator 312 shows Hilda putting on her space suit in the dropship cockpit before her
reported attempt to abandon it and reach XGP in the following gallery set. These five ownership
rechecks are resolved; the later sequence remains unreviewed. Locators 298–299 link to new manual
crushing-contact/boarding-interior references below without changing their detailed-review status.

**Sheets 14–15 — 2026-10-26:** locators 313–354 / image IDs 848147–848188, web labels
00:20:44–00:23:14. All 42 have individual category-screening descriptions and tags, supported by
contact sheets and selected full-size hardware/contact checks. Earlier gallery annotations and
all nine manual records are preserved. Handheld grappling-device and magic-associated imagery
tokens distinguish personal equipment, ship anchors and reported magical actions.

| Range | Preliminary grouping / revisit value |
| --- | --- |
| 313–319 | Dropship access crop, Hilda in her suit, handheld grappling device and clamp on the pirate tether, cable grips, Gene reaction and extended-arm XGP exterior. Major equipment/attachment references at 314–316; XGP exterior at 318. |
| 320–323 | Pirate tether pursuit/zipline-like equipment, female leader's raised-hand defensive imagery, Hilda above the approaching pursuer and handgun aim. Magic/bullet-blocking function follows maintainer context rather than a complete effect/weapon analysis. |
| 324–329 | Frayed tether beside the pirate anchor and XGP wrist (324), Hilda reaching after departing XGP, crew reactions and separation. Full-size 324 shows damaged cable sections; complete failure timing and escape constraints remain reported context. |
| 330–337 | Final Hilda/pirate confrontation, large translucent field and smaller orb, handheld hook contact at the leader's foot (334), Hilda expressions. No identifiable dental device is exposed in the close-ups. |
| 338–341 | Bright sphere and distant flashes against the star, associated by maintainer context with the explosion killing both characters. These effect samples do not independently establish a trigger mechanism or visible occupant deaths. |
| 342–346 | XGP beyond the stellar limb, clear underside/pod exterior (343), cockpit side/rear pan with pale seat/console shells, gauges and partial Gilliam. Strong later exterior and cockpit-modeling references. |
| 347–354 | Jim turning toward Gene with Melfina's slotted apparatus behind, Gene portraits, Gilliam face/mount (351) and closing nebula view. The tiny form at 354 is not resolved as detailed vessel geometry. |

**Final-sequence context — 2026-10-26:** the maintainer describes Hilda leaving the dropship,
hooking the pirate tether attached to XGP's arm, reeling/climbing toward XGP, and being pursued
by pirates on a faster tether transport. The female leader uses magic to counter Hilda's gunfire.
The tether breaks and XGP accelerates away; returning for Hilda would reportedly prevent escape
from the gravity well. Hilda hooks the leader's foot, speaks and bites down on a suspected
tooth-carried explosive/trigger, causing an explosion that kills both. This narrative is retained
as attributed context. Trigger construction, exact dialogue, continuous choreography, final
effect identification and quantitative gravity/propulsion constraints are not independently
verified by the category pass. No new gameplay or later-phase implementation is authorized.

**Current gallery coverage:** all **354 Episode 4 baseline images inspected**, comprising
**353 SCREENED / 1 NEEDS_RECHECK / 0 UNREVIEWED**, zero unavailable. Recheck locator: **7**;
the ship/launchpad and planet identity remain unresolved. This completes baseline screening
coverage with that retained question, not detailed review or every-frame episode coverage.
All 354 Episode 4 gallery records and nine manual supplements are `INITIAL_REVIEW_COMPLETE`;
the other 8,850 gallery records remain `NOT_REVIEWED`. No targeted deep dive is marked complete.
All nine manual supplements remain category-screened
and unreconciled in timing. Episode 4's gallery baseline is exhausted. The planned next episode
is Episode 1; its screening remains unstarted, as do Episodes 2–3 and 5–26. Locator 7 can be
revisited independently without reopening completed image descriptions. Per-image descriptions,
priorities and questions live in `category-index.csv`; these
group summaries do not replace them. The generated browsing workbook is refreshed from that CSV.

**Post-review storage — 2026-10-26:** Episode 4's verified format-2 RAR contains all 354 gallery
originals and nine supplemental PNGs with recovery metadata. Both expanded image sets are pruned;
all 15 contact sheets and their registry remain available. Full gallery restore and identical
sheet regeneration passed before final pruning. CSV annotations are unchanged by cleanup;
supplement rows show NOT_LOCAL in the refreshed workbook until restored. Detailed commands,
retention rules and recovery evidence are owned by the
[tool record](../../../tools/reference-extraction/README.md#episode-retention-and-supplement-recovery--accepted-2026-10-26).

### Manual supplemental references

Maintainer-supplied images outside the gallery baseline are indexed in
[supplemental-index.csv](supplemental-index.csv) and displayed on **Manual references** in the same
`category-review.xlsx`. They are a separate source table for future Power BI joins, not additional
gallery locators. The authored gallery table remains exactly 9,204 rows / 354 per episode.
Manual rows use the same 21 annotation fields/vocabulary, with `image_id` formatted
`EP-04-MAN-001` and the following nine provenance fields. IDs never depend on later timing matches.

| Field | Meaning / initial validation |
| --- | --- |
| `media_path` | Repository-relative PNG path under ignored `reference/working/manual-supplements/`; images are retained locally, outside gallery cache cleanup/prune ownership. |
| `media_sha256` | SHA-256 of the original supplied screenshot bytes, not of the source video. |
| `media_bytes` | Original screenshot byte count, imported as a whole number. |
| `local_timestamp` | Exact visible VLC `mm:ss` label; this is a player-display observation, not a verified decoded frame PTS. |
| `local_seconds` | Whole-number seconds parsed from that label; must agree with it. |
| `timestamp_basis` | Initially `PLAYER_UI_WHOLE_SECONDS`. No frame accuracy or fixed gallery offset implied. |
| `alignment_status` | Initially `UNRECONCILED`. A later verified alignment requires an explicit contract update; preserve the original player label and ID. |
| `related_gallery_ids` | Semicolon-separated same-episode gallery IDs used as contextual associations. These do not declare exact image matches or replace gallery timing. |
| `source_description` | Supplied-image provenance and visible source/player context. Do not assert that a title-bar filename establishes the archive's exact edition/hash or timing. |

The manual sheet is sorted by episode, observed local seconds and stable ID. It has local image
links, source notes, tags, timing status and derived media availability. Its counts are shown
separately on Overview; unaligned local seconds are never interleaved with gallery web seconds as
if they shared a clock. File links require a local restored image. The cleanup refinement bundles selected-episode
supplemental PNGs and recovery metadata into that episode's RAR alongside gallery originals.
Normal verified pruning removes gallery originals and supplemental PNGs, retaining contact sheets.
The workbook marks absent supplemental images `NOT_LOCAL`; restore them from the RAR for full-size
inspection or to use the local link. This availability is generated host-local state, not an authored
review/timing status or proof of archive completeness. Authored CSVs remain outside the archive as working records; recovery
metadata inside the archive is a snapshot, not a competing annotation source. No image publication
is authorized. See the [archive/retention contract](../../../tools/reference-extraction/README.md#episode-retention-and-supplement-recovery--accepted-2026-10-26).

**Initial manual batch — 2026-10-26:** two full VLC screenshots were copied byte-for-byte and
hash-checked, preserving UI, pillarboxing, opening text and original PNG quality:

- **EP-04-MAN-001**, VLC **01:56** (116 s): oblique rear XGP view with bright exhaust and visible
  pods/connecting structures. Stored at `reference/working/manual-supplements/EP-04/EP-04-MAN-001.png`.
- **EP-04-MAN-002**, VLC **01:57** (117 s): oblique forward XGP view with pointed hull, pods and
  colored exterior bands. Stored alongside the first image under its own stable ID.

Both are `SCREENED`, high priority, `OPENING`, and associated contextually with gallery locator
006 / ID 847840. Their detailed-review states remain `NOT_REVIEWED`; no temporal offset or exact
gallery match was assigned. The workbook now has 28 tabs (Overview, 26 gallery tabs and Manual
references); saved-file checks cover 285,324 gallery cells, 9,204 gallery image links, 68 manual
cells, both local media links and the separate manual count. Source CSV hashes remain unchanged
by workbook generation. Eight validator tests include manual timing, identity/association/path
refusals and media-integrity checks.

**Opening corrections from maintainer context:** locator 008 / ID 847842 is the back of Gene's
head. The maintainer describes him subsequently turning toward the camera and firing, followed by
the cut to the caster on the table in locator 009; this surrounding action remains attributed, not
independently viewed in this pass. Its identity recheck is resolved. Locator 007 remains uncertain:
the maintainer proposes a ship/launchpad scene, possibly XGP or another ship on Gene's planet
(possibly Sentinel), without confirming either identity. Preserve those alternatives in the index;
do not promote the planet, vessel or launchpad interpretation to verified fact.

**Halcyon deployment supplements — 2026-10-26:** five additional full VLC screenshots are
retained byte-for-byte under `reference/working/manual-supplements/EP-04/`, with separate stable
IDs, hashes and visible player-time labels:

| Manual ID | VLC label | Visible state / supplied sequence association |
| --- | --- | --- |
| EP-04-MAN-003 | 17:15 | El Dorado underside panel partly separated with a narrow dark opening; maintainer places the deployment inserts between gallery 256–257. |
| EP-04-MAN-004 | 17:16 | Large purple/white missile exposed on a lowered yellow carrier beneath the open bay, with extended support struts. Same reported interval. |
| EP-04-MAN-005 | 17:17 | Missile remains on the carrier with a long forward guide member and aft plate structure visible. Same reported interval; compare SET-112 guide catapult/blast-reflector design. |
| EP-04-MAN-006 | 17:25 | Closer underside view with missile still visible and a bright plume extending aft; maintainer identifies firing between gallery 259–260. A departed/free-flight missile is not shown in this still. |
| EP-04-MAN-007 | 17:27 | Detached purple missile with a large white exhaust plume, seen near a dark asteroid silhouette and bright orange/white background. Maintainer places this post-launch travel shot before the cut to gallery 260. |

The maintainer reports Ron orders firing at gallery 255, Harry becomes excited and triggers
deployment, the deployment inserts occur between 256–257, and the sequence returns to Ron's
monologue at 257. Firing is reported between 259–260. These gallery-relative intervals and
dialogue/action descriptions remain attributed associations, not verified frame matching or a
shared timestamp clock. At supplemental ingestion, gallery rows 241 onward were unreviewed;
supplemental indexing itself did not screen them. The later sheets 11–13 pass is recorded above.
All five supplements are `STORY`, `SCREENED`, high priority and `NOT_REVIEWED` for detailed
evidence. SET-112 is a research cross-reference; exact continuous motion, timing and official
Latin weapon spelling remain open. MAN-007 adds the visible free-flight state missing from MAN-006;
the maintainer reports a few seconds of travel toward the asteroid/ships before gallery 260.
This does not establish a measured trajectory, speed or exact duration. Current manual coverage
at this checkpoint was seven records, with 238 saved-cell checks and seven local image links;
the subsequent grappler supplements below extend manual coverage without changing gallery counts.

**Grappler contact and boarding-area supplements — 2026-10-26:** two original full VLC PNGs
are saved byte-for-byte alongside the earlier supplements, with hash/size verification:

| Manual ID | VLC label | Visible state / supplied sequence association |
| --- | --- | --- |
| EP-04-MAN-008 | 19:49 | XGP fingers enclose the red pirate hand near its green hatch, with white jagged marks across the hub; the cream arm connects back to the blue spherical pirate grappler section. |
| EP-04-MAN-009 | 19:49 | Low interior view of the male leader and blue/white foot soldiers beneath curved purple boarding-area panels, loose fragments and exposed cables. |

Both are associated with the reported interval between gallery 298–299. The maintainer describes
the XGP crush leading to an explosion that kills the leader in that landing/boarding area. Visible
contact and interior states are separated from this subsequent action/outcome; neither still is
marked as a continuous-motion or death verification. Both share a whole-second player label;
attachment order is preserved by stable IDs without inventing subsecond timing. Detailed review
remains `NOT_REVIEWED`, timing remains `UNRECONCILED`, and priority is high. Current manual
coverage is nine records; generated workbook checks cover 306 manual cells and nine image links.

`category_index.py supplement-data` validates manual metadata, checks hashes/sizes for present
local images, and adds derived `media_availability` (`LOCAL_VERIFIED` or `NOT_LOCAL`) to its
disposable workbook join. Missing media after pruning does not prevent refresh. Normal `validate`
checks metadata without requiring a host to possess local-only screenshots. Refresh uses the existing
ImportExcel builder; it refuses a stale build if either authored CSV changes during generation.

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
The builder performs no network requests or media extraction. This locator-only workbook retains
the original unverified timing fields; bounded derived alignment is available separately in the
existing category workbook as described below.

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

### Category workbook alignment view

The existing `category-review.xlsx` now includes **Alignment anchors** and **Alignment mappings**
tabs and derived timing fields on episode/manual tabs. The [alignment tool's Stage 4 results](../../../tools/reference-alignment/README.md#stage-4-integration-results--2026-10-27)
own the field contracts, availability modes, report bridge grains and validation evidence.
All 9,204 gallery locators and nine supplements retain their original data and review states.
This integration passed saved-value/link checks, visual inspection and maintainer-reported native
viewer checks on 2026-10-27; the maintainer confirmed the integration on that date.

Refresh with PowerShell 7 and installed ImportExcel:

```powershell
./tools/reference-extraction/build_category_workbook.ps1 -Python <python.exe-path>
./tools/reference-extraction/build_category_workbook.ps1 -Python <python.exe-path> -VerifyAlignmentMedia -FFprobe <ffprobe.exe-path>
```

The default labels available alignment records `RECORDED_UNCHECKED`; explicit media verification
can establish `VERIFIED_CURRENT` at refresh time within the current pilot contract. Missing or
mismatched inputs suppress derived timings. Direct intervals and model estimates remain separate;
unsupported times are blank. The original generated `alignment_status` is unchanged. Episode 1's
bounded mapping does not apply to other episodes or its uncovered opening/ending regions.
The workbook remains generated and ignored; record durable evidence in the maintained CSVs.

### Episode 1 annotated survey — sheets 4–6 (2026-10-27)

Locators 073–144 now have individual initial-review annotations, covering the bar confrontation,
cyborg fight, aftermath, nighttime walkway and industrial landing transition. All three contact
sheets and ten ambiguous full-size gallery images were inspected. Subtitle cues 57–116 and eleven
bounded scene windows support the context; the [batch evidence record](../episode-01-review-batch-02.md)
distinguishes primary observations, secondary names and timing limits. No alignment mapping changed.

Episode 1 now has 144 reviewed gallery records: 137 SCREENED and seven NEEDS_RECHECK, with
86 INITIAL_REVIEW_COMPLETE and 58 PARTIAL. The remaining 210 records remain UNREVIEWED/NOT_REVIEWED.
Maintainer clarifications resolve 084 as boot detailing and 140–144 as the pirate ship from the
opening chase; exact facility geography remains unknown. The seven earlier tentative launch-site
rechecks remain. Iris is maintainer-identified, with separate secondary biography context in
CTX-000032–033. PDA attribution and Hilda's crowd appearance retain their secondary-source limits.

The owned 132-frame temporary decode set and two previews are removed after recording hashes,
timestamps and inspection selections. Gallery originals, contact sheets and EP-01-MAN-001 remain
under the existing episode retention policy; no episode-completion archive or cleanup is implied.

### Episode 1 annotated survey — sheets 7–9 (2026-10-27)

Locators 145–216 have individual initial-review annotations: pirate deployment, Club Temptation,
an alley cutaway, daytime city views, the early Starwind & Hawking premises, Rachel's call,
mid-episode break graphics and an identity-search screen. The [batch record](../episode-01-review-batch-03.md)
owns selected full-size checks, subtitle scope, secondary associations and temporary-decode evidence.

All 72 new rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 1 totals are 216 reviewed:
209 SCREENED and seven earlier launch-site NEEDS_RECHECK; 158 INITIAL_REVIEW_COMPLETE and
58 PARTIAL. The remaining 138 rows are UNREVIEWED/NOT_REVIEWED. No previous rows or other
episodes changed. The private-room woman remains unidentified; Hilda's Rachel cover-profile
fields are not treated as true biography. HQ views concern Sentinel, not the later Heifong branch.
The four break-graphic rows are EYECATCH, not ship references or the episode-ending card.

Eight bounded local windows produced 100 temporary frames over 25 requested seconds; the selected
preview was inspected. Hash/PTS provenance is retained and the owned decode set is pruned after
verification. Original gallery images, contact sheets and the manual supplement remain under the
existing episode-completion RAR policy. No alignment mapping or 3.2A status changes.

### Episode 1 annotated survey — sheets 10–12 (2026-10-27)

Locators 217–288 have individual initial-review annotations, covering HQ departure, the bodyguard
agreement at Clyde's Bar, alley ambush, red car and controls, roadside repair and pirate roadblock.
The [batch record](../episode-01-review-batch-04.md) distinguishes subtitle context, secondary
associations, selected full-size imagery and bounded local scene checks. The ordinary pistol is
kept distinct from the later caster; the red-car subject is a descriptive continuity ID.

All 72 new rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 1 now has 288 reviewed:
281 SCREENED and seven earlier launch-site NEEDS_RECHECK; 230 INITIAL_REVIEW_COMPLETE and
58 PARTIAL. The remaining 66 rows are UNREVIEWED/NOT_REVIEWED. No earlier annotations or other
episodes changed. Locator 225 is an OTHER scene-change flash, not an asserted physical gunshot;
285's obscured occupants do not establish an empty car. Exact car model, propulsion, control
labels and repair procedure remain unverified; no layout or gameplay implementation is implied.

Seven bounded windows produced 132 temporary frames over 33 requested seconds. Selected preview
frames were visually inspected, provenance retained and the owned temporary set pruned after hash
verification. Cached gallery originals, contact sheets and the manual supplement remain under the
existing episode-completion RAR policy. Alignment records are unchanged; Phase 3.2A is unstarted.

### Episode 1 annotated survey — sheets 13–15

The [final batch](../episode-01-review-batch-05.md) annotates locators 289–354 with individual
descriptions, eight scene groups and bounded subtitle/video context. All 354 sampled Episode 1
gallery records now have an initial survey: **346 SCREENED / eight NEEDS_RECHECK**, with
296 INITIAL_REVIEW_COMPLETE and 58 prior targeted PARTIAL records. Seven flags concern the
earlier tentative launch-site identity; locator 350 adds the case-code O/0 transcription question.
This is complete sampled-gallery survey coverage, not full-video or targeted design verification.

High-value references include the purple modular blaster kit, the distinct gold caster loading
and aiming views, and Melfina's transport-case exterior, access panel and interior reveal.
Existing CTX-000020/022/024 records are reused with new image links; no new secondary claims,
source captures, mapping anchors or prior annotations were introduced. Locators 331–354 are
outside the validated mapping: scene context does not provide estimated gallery timestamps.

Both generated ImportExcel views are refreshed and checked. Own bounded-decode outputs are
pruned after frame-hash verification, retaining provenance. Contact sheets, gallery originals
and EP-01-MAN-001 were retained for corrections until the subsequent cleanup below.
No next episode or Phase 3.2A work starts here. Changes remain uncommitted pending confirmation.

### Episode 1 retention checkpoint — 2026-10-28

The [retention record](../episode-01-retention-checkpoint.md) documents the completed archive
and cleanup. EP-01.rar contains all 354 gallery originals and EP-01-MAN-001 plus recovery metadata;
native integrity, staged restoration, exact inventory and image hashes passed. Prune repeated
recovery verification before removing both expanded image sets. Final status: cached 0, archived
gallery 354, archived supplement 1, all 15 contact sheets retained and archive hash valid.

The archive is 62,978,197 bytes; pruning reclaimed 63,495,276 bytes of redundant expanded data.
All 20 preserved CSV/sheet/registry hashes matched. No temporary alignment image runs or archive
staging directories remain. Generated views are refreshed with the supplement marked NOT_LOCAL;
the eight rechecks, authored review states and bounded alignment remain unchanged. Restore from
the verified RAR for future full-size checks. No next episode or Phase 3.2A work starts here.

The maintainer accepted pending batches 04–05, the tentative case-code follow-up and the verified
Episode 1 retention checkpoint on 2026-10-28. The eight rechecks remain open.

## Episode 2 preparation — 2026-10-28

All 354 gallery images (847127–847480) downloaded and passed decoding/hash validation; the
existing prepare command also generated 15 contact sheets. JPEG bytes total 61,557,786, with
61,969,457 bytes in the expanded cache including its manifest. No archive exists yet.

The [context preparation record](../episode-02-context-preparation.md) documents the full read
of all 387 registered English ASS events, verified source/track/hash and first-three-packet
timing checks. Five selected Fandom articles and cached AnimeHistory Episode 2/Hilda/Horus
context supply eleven new concise secondary assertions. Blue Heaven, Swanzo and McCoy receive
catalogue IDs without assigning them to images. The failed standalone McCoy lookup is explicit.
The narrow Horus two-jump route claim is now corroborated against the translated local dialogue;
no XGP performance or completed travel measurement is inferred.

All 354 Episode 2 image records remain UNREVIEWED / NOT_REVIEWED. No sheets or gallery originals
were visually inspected during context preparation; no context-image links or alignment records
were added. Episode 2 remains unmapped, and Episode 1's offset must not be reused. Context views
are refreshed and validated; further timing/image review and Phase 3.2A remain separate scope.

The maintainer accepted this Episode 2 download/subtitle/context preparation on 2026-10-28.
