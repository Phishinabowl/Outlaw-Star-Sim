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
   Routine matching now accepts an explicit one-episode selection plan for any of the 26
   episodes; retain the existing 1–5-image command bound. See the
   [all-episode extension](../../../tools/reference-alignment/README.md#all-episode-extension--2026-10-28)
   for plan fields and episode-scoped assessment/current-verification commands. Tool support
   does not imply that an episode already has validated timing coverage.
   The pinned Episode 1 release has a validated navigation offset of -1.388 s only for whole-second
   web labels 06:40–20:40. The pinned Episode 2 release has independently validated navigation
   coverage of web labels 01:43–22:39 with offset -1.286 s; its
   [alignment review](../episode-02-alignment-review.md) records the limits. Episode 3 now has
   separately validated navigation coverage for web labels 01:47–23:00 at offset -1.4845 s;
   its [alignment review](../episode-03-alignment-review.md) retains the checks and unmapped edges.
   Episode 4 has independently validated navigation coverage for web labels 01:54–22:30 at
   offset -1.2415 s; its [alignment review](../episode-04-alignment-review.md) retains nine direct
   intervals, 330 estimates and 15 unmapped edge images. The maintainer accepted this checkpoint
   on 2026-10-29.
   Other unsupported
   regions remain unmapped. The tool doc owns the
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
| `suzuka_bokken` | Suzuka's wooden sword, identified through selected secondary context and Episode 6 dialogue. A dark surface in a still does not establish material, cutting physics or universal immunity to weapon sensors. |
| `light_shield` | Portable light-shield equipment/effect identified in Episode 6 dialogue. Record the depicted holder and visible field separately; no common power rating, full activation mechanism or identical hardware across users is established. |
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
| `gene_father`, `gene_father_ship` | Descriptive IDs for Gene's father and the yellow family spacecraft in his childhood flashback, supported by Episode 2 father/son dialogue and rescue continuity. No primary proper name, ship model or legal ownership established; keep hostile surrounding craft separate. |
| `pirate_landing_craft` | Green pirate landing/dropship units identified by the maintainer in Episode 4 locator 167; reported landing-foot action is retained separately from still-image observations. |
| `xgp_hangar_asteroid` | Asteroid containing the Outlaw Star's storage hangar and awakening setting, identified by the maintainer; door motion and transfer context remain reported until checked in video. |
| `starwind_hawking_hq` | Starwind & Hawking premises; identification does not establish a planet/location without supporting evidence. |
| `guugaku` | Bald Kei pirate with large neck bolts; Episode 1 identification uses the cached secondary appearance description and visible features. |
| `pirate_fighter`, `pirate_fighter_pilot` | Episode 1 pursuing fighter craft and goggled pilot, identified through the bounded subtitle/scene check. The pilot's personal name and exact readiness-call attribution remain unassigned; do not equate the craft with Episode 4's landing units automatically. |
| `sentinel_iii` | Planet named by the Episode 1 establishing narration, corroborated against local globe/city views; does not identify the separate pre-title launch facility. |
| `gene_modular_blaster` | Descriptive Episode 1 ID for the purple revolver-style blaster and fitted component kit, supported by short-barrel-blaster dialogue. Distinct from the gold caster; no model/caliber or full modification mechanism established. |
| `melfina_transport_case` | Reinforced transport trunk revealing Melfina in Episode 1; distinct from the XGP pod/apparatus and Hilda's laptop. No complete life-support specification implied. |
| `hilda_prosthetic_arm` | Descriptive continuity ID for Hilda's artificial arm, exposed mechanisms and repair/hand-test views in Episode 2. Distinct from her wrist controller; no complete engineering design or manufacturer identification implied. |
| `blue_heaven` | Asteroid free town identified in secondary Episode 2 preparation and local dialogue; distinct from the XGP storage asteroid. No image match or measured layout established by preparation. |
| `swanzo` | Corbonite mechanic associated with Blue Heaven in selected secondary context; image identification and containment-suit details require scoped review. |
| `mikey` | Catalogue identity established through Episode 5's named video call (018/020), translated dialogue and matching dock appearance. Matching Episode 2/3 mechanic rows are reconciled; cropped and distant views retain scene-continuity limits. Independent appearance-article confirmation remains unavailable. See [current identification scope](#cross-episode-mikey-identification--2026-10-30). |
| `mccoy_combat_machine` | Descriptive ID for the yellow articulated machine with McCoy visible above/behind its opened shell in Episode 3 gallery 027–030. No canonical model or autonomous capability established; earlier Episode 2 annotations remain unchanged. |
| `blue_heaven_hotel_attacker` | Descriptive ID for the orange-clad man interrogated by Hilda in Episode 3 gallery 037–047. Proper name unresolved; distinct from McCoy. |
| `blue_heaven_grappler_ship` | Descriptive collective ID for the compact class-C craft pursuing Horus from Blue Heaven in Episode 3. The dialogue count is five; exact vessel names and individual pilot assignments are unverified. Distinct from Episode 1 pirate fighters and Episode 4 landing units. |
| `mccoy` | Episode 2 bearded bar antagonist with curly hair, green sleeves, dark vest and wrist wraps, identified in gallery 299–316 through translated dialogue, scene continuity and CTX-000042. Standalone wiki lookup returned NOT_FOUND; no operator identity is assigned to the later yellow mechanical opponent. |
| `orta_honehone` | Ctarl-Ctarl ship named in secondary Episode 3 context; distinct from Horus and the XGP. No image match or measured dimensions established in preparation. |
| `ctarl_ctarl` | Humanoid species identity, distinct from the Ctarl-Ctarl Empire as a political faction. Secondary catalogue context does not establish biological capabilities. |
| `ctarl_governor` | Descriptive role ID for the elderly pointed-eared official displayed in Episode 3's recorded reprimand. Translated dialogue addresses him as Governor and identifies the Comm Cube message as a recording; personal name and physical recording-device design remain unverified. |
| `farfallas` | Destination-system identity; Farfallus retained as an AnimeHistory spelling variant. Original-language spelling and image associations remain unverified. |
| `starwind_hawking_car` | Descriptive continuity ID for the red open-top classic-style car used by Gene and Jim in Episode 1. No verified model designation, legal ownership or complete propulsion mechanism implied. |
| `sentinel_rental_car` | Pale-green enclosed rental car used by Gene, Jim and Melfina during Episode 6's trip to Hugo. Descriptive continuity ID, distinct from the earlier red car; make/model and propulsion remain unverified. |
| `fred_luo`, `fred_luo_premises` | Fred Luo and his Episode 6 weapons showroom/office, identified through the named greeting, visit continuity and selected secondary context. Premises identity does not establish a complete building layout or equate it with Luo-family headquarters on Heifong. |
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
| Repair references | `prosthetic_arm` for an identified artificial limb or its exposed mechanisms; `repair_tool` for visible repair implements, without assigning brand, exact process or specifications from dialogue alone. |
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

## Episode 2 bounded alignment — 2026-10-28

The [alignment review](../episode-02-alignment-review.md) records 18 attempts: eight precise
matches and ten retained ambiguities. Four FIT coefficients were frozen before HOLDOUT searches;
four independent matches, including both sides of the break, validated local = web - 1.286 s
for whole-second web labels [103,1360). Gallery 001–348 receives navigation coverage;
349–354 remains unmapped. Maximum HOLDOUT interval error is 0.400 s. Actual scene/cue inspection
is still required; sparse sampling is not full-runtime verification.

Current Episode 2 input verification, two bounded hash reproductions and early/late subtitle
context checks passed. The ImportExcel view is refreshed. Provenance-gated cleanup removed
five search runs (1,396 files / 1,008,059,897 bytes). Image annotations and Episode 1 records
remain unchanged. The maintainer accepted this checkpoint on 2026-10-28; the first Episode 2 survey
batch and Phase 3.2A have not advanced.

## Episode 2 annotated survey — batch 01, 2026-10-28

The [first batch](../episode-02-review-batch-01.md) covers gallery 001–072 with accepted
alignment, translated subtitle context and selected full-size checks. All 72 rows are
INITIAL_REVIEW_COMPLETE: 71 SCREENED and one NEEDS_RECHECK (003 launch-site/craft identity).
Maintainer clarification identifies 012 as an opening fight vignette between XGP and El Dorado,
including El Dorado's foreground grappler arm; its identification recheck is resolved.
The remaining 282 rows are untouched.
Ten scene groups preserve opening/story separation, case state changes and prosthetic repair
references. Selected secondary Harry appearance and repair context is registered separately
from primary observations. Generated ImportExcel views are refreshed and validated.
The maintainer accepted batch 01 and its clarification follow-ups on 2026-10-28;
Phase 3.2A remains unstarted.

## Episode 2 annotated survey — batch 02, 2026-10-28

The [second batch](../episode-02-review-batch-02.md) covers gallery 073–144 with aligned
English subtitle context, eleven full-size original checks and eighteen explicit local frame
samples. Fourteen scene groups preserve the farm siege, ammunition/pond retrieval, Tao/caster
exchange, dropship intervention and Melfina's awakening. Maintainer clarification resolves 097–098
as Gene/Jim's prepared two-rocket attack blocked by pirate magic, and identifies 107–110 as the
elderly pirate's dragon attack canceled by Gene's caster shot. Combined Episode 2 coverage is
144 INITIAL_REVIEW_COMPLETE: 143 SCREENED and one NEEDS_RECHECK (003); 210 gallery rows remain
untouched. Existing secondary assertions
supply 49 new image links without merging pirate role IDs into candidate proper names.
The maintainer accepted batch 02 and its clarification follow-ups on 2026-10-28;
no later batch or Phase 3.2A work is included.

## Episode 2 annotated survey — batch 03, 2026-10-28

The [third batch](../episode-02-review-batch-03.md) covers gallery 145–216 with aligned
translated subtitle context, eighteen full-size original checks and thirty explicit local samples.
Seventeen scene groups distinguish dropship boarding/rendezvous, main-Horus sub-ether imagery,
the bumper, childhood memory/dream and Blue Heaven approach. Descriptive father/family-ship IDs
retain the unnamed yellow ship separately from purple attackers in 185–186. Maintainer context
identifies those attackers as hired support brought by the MacDougalls; El Dorado's recalled
position and later recognition remain follow-up leads. It also identifies the father's hand at
188 and corrects 189–190 to a view through the closed escape-pod door/window rather than a screen.
Combined coverage is 216 INITIAL_REVIEW_COMPLETE: 215 SCREENED, one NEEDS_RECHECK
(003), with 138 gallery rows untouched at that checkpoint. The maintainer accepted this batch
and its clarification follow-ups on 2026-10-28 during Episode 2 closeout;
no later batch or Phase 3.2A work is included.

## Episode 2 annotated survey — batch 04, 2026-10-28

The [fourth batch](../episode-02-review-batch-04.md) covers gallery 217–288 with aligned
English subtitle context and 21 full-size checks. Fifteen scene groups distinguish Horus's
overhead docking support and boarding stairs, Swanzo's greeting, Gene's gun bluff, Jim's
reflection, ship-detail inserts, station corridors/market, Melfina's clothing fitting and the
bar. Static support views and dialogue warnings do not establish full docking or pressure-system
specifications. The tall human companion remains unnamed in image tags; Mikey is a secondary
lead without an appearance match. Existing secondary context supplies 89 new image links.
Combined coverage is 288 INITIAL_REVIEW_COMPLETE: 287 SCREENED and one NEEDS_RECHECK
(003), with 66 gallery rows untouched. No new decoded frames were created. Gallery originals
and contact sheets remained until the subsequent episode-level archive cleanup. The maintainer
accepted this batch on 2026-10-28 during Episode 2 closeout;
no later batch or Phase 3.2A work is included.

## Episode 2 annotated survey — batch 05, 2026-10-28

The [final batch](../episode-02-review-batch-05.md) covers gallery 289–354 with translated
subtitle context, 26 full-size checks and 18 explicit local samples. Fifteen scene groups
preserve the bar confrontation, hotel/reception, clothing change, sleeping, intrusion and yellow
mechanical opponent. McCoy's image cues are recorded; the machine's operator, model and exact
blue-tool function remain unassigned. Gallery 349–354 remains unmapped; local scene samples
do not extend ALNMAP-000004. Existing context supplies 69 new image links.

All 354 Episode 2 rows are INITIAL_REVIEW_COMPLETE: 353 SCREENED and one NEEDS_RECHECK
(003 opening ship). This is initial-survey completion, not full identity or design verification.
The maintainer accepted the final review and authorized episode-level RAR cleanup on 2026-10-28.
The [retention checkpoint](../episode-02-retention-checkpoint.md) owns the resulting archive,
recovery and pruning evidence. No next episode or Phase 3.2A work is included.

### Episode 2 retention checkpoint — 2026-10-28

The complete format-2 EP-02.rar contains 354 gallery originals and recovery metadata; no manual
supplements are registered for this episode. Native integrity and staged recovery passed during
archive creation, and prune independently repeated recovery/inventory/hash checks before removing
the expanded cache. Final status: cached 0, archived 354, contact sheets 15, unpacked bytes 0,
archive hash valid. The RAR is 61,505,246 bytes; removing redundant expanded data reclaimed
61,969,457 bytes. All 20 preserved CSV/sheet/registry hashes matched. No temporary media runs or
archive staging directories remain. Both generated views are refreshed and validated.

The initial survey is closed with locator 003 unresolved and 349–354 unmapped. Restore originals
from the verified RAR when a later full-size check is needed. The maintained retention record
above owns commands, hashes, recovery details and limits. The maintainer confirmed this checkpoint
on 2026-10-28; no next episode or Phase 3.2A work starts here.

## Episode 3 gallery preparation — 2026-10-28

All 354 Into Burning Space gallery images (847481–847834, web labels 00:01:43–00:23:07)
downloaded through the established paced gallery tool. Image decoding, original-byte SHA-256,
manifest identity and locator order checks passed; zero failed or missing images remain.
JPEG bytes total 63,789,662; expanded cache including manifest totals 64,204,169 bytes.

The same prepare command generated 15 chronological 4-by-6 contact sheets under
`reference/contact-sheets/animehistory-review/EP-03/`. All sheet hashes, 1600×2056 dimensions,
354 ordered ID/time/image-hash associations and the final sheet's 18-image population passed
verification. Sheet PNGs total 52,844,982 bytes, or 52,914,693 including the registry. First,
middle and last sheet layouts were visually checked for readable labels and image placement;
this is preparation QA, not content classification or annotated image review.

Original JPEGs and their recovery manifest are local-only under
`reference/cache/animehistory-review/EP-03/`; no RAR exists yet. All 354 annotation rows remain
UNREVIEWED / NOT_REVIEWED. No subtitle/context preparation, accepted Episode 3 timing mapping,
local video extraction or category annotation was added in this increment. Existing episodes,
source media and authored tables are unchanged. Next scope is subtitle/website preparation and
episode-specific alignment before substantive timed batch review. The maintainer accepted this
gallery preparation together with the subsequent subtitle/context preparation on 2026-10-28.
No Phase 3.2A work is included.

## Episode 3 subtitle/context preparation — 2026-10-28

The [preparation record](../episode-03-context-preparation.md) documents a full read of the 372
English ASS events, pinned media/subtitle hashes, bounded packet checks and local-time navigation
notes. Four selected Fandom captures and the cached AnimeHistory Episode 3 synopsis supply nine
new source-checked secondary assertions; later-episode biography and route/performance limits
remain explicit. The generated context workbook is refreshed after validation.

All 354 Episode 3 image rows remain UNREVIEWED / NOT_REVIEWED. No gallery annotations,
context-to-image links, video-frame extraction or alignment mappings were added. Episode 3
alignment remains the next separate step before timed batch review. The maintainer accepted
this preparation checkpoint on 2026-10-28; no Phase 3.2A work is included.

## Episode 3 bounded alignment — 2026-10-28

The [alignment review](../episode-03-alignment-review.md) records 16 assessed attempts, ten
supported direct intervals and six retained ambiguities. ALNMAP-000006 supersedes the frozen
FIT proposal with unchanged coefficients after independent validation: local = web -1.4845 s,
web-label domain [107,1381). Gallery 002–352 has ten direct intervals and 341 estimates;
001 and 353–354 remain unmapped. The measured maximum HOLDOUT interval error is 0.3755 s,
not an error guarantee for untested images.

Current Episode 3 input verification, two accepted-frame hash reproductions and two separated
subtitle/scene checks passed. The category workbook is refreshed and owned alignment outputs
are cleaned after durable-provenance checks. Gallery originals/contact sheets remain available
for review. All Episode 3 annotations remain UNREVIEWED / NOT_REVIEWED. The maintainer accepted
this alignment checkpoint on 2026-10-28.
The first three-sheet survey and Phase 3.2A have not started.

## Episode 3 annotated survey — batch 01, 2026-10-29

The [batch record](../episode-03-review-batch-01.md) documents the subsequent review of
gallery 001–072, three contact sheets and 19 selected originals including the follow-up
inspection of 013, with translated subtitle
cues 34–91 and the accepted alignment. All 72 rows are INITIAL_REVIEW_COMPLETE:
71 SCREENED and one NEEDS_RECHECK (005, recurring opening launch-site/vessel identity).
The remaining 282 Episode 3 rows are untouched. McCoy's machine operator reveal, the
separate hotel attacker, paint-round pistol and Horus dock/service views are indexed.
Mikey's name-to-face association remains provisional, with the tentative maintainer identification
retained. Image 013 is corrected to opening XGP–El Dorado combat. The maintainer accepted
the batch and follow-up corrections on 2026-10-29. This is not a targeted modeling deep dive.
Phase 3.2A remains unstarted.

## Episode 3 annotated survey — batch 02, 2026-10-29

The [batch record](../episode-03-review-batch-02.md) documents gallery 073–144 using three
contact sheets, 25 selected originals, translated subtitle cues 92–161 and the accepted
alignment. All 72 new rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 3 now has
144 initially reviewed rows (143 SCREENED, one NEEDS_RECHECK at 005); 210 remain untouched.
The survey preserves Horus dock-release configurations, passenger and operating stations,
class-C pursuit, turret and anti-laser imagery, and Orta-Honehone's exterior and command-space
views. Mechanism specifications, unnamed pilot identity and environmental construction remain
qualified. The maintainer accepted this batch on 2026-10-29; no Phase 3.2A work is included.

## Episode 3 annotated survey — batch 03, 2026-10-29

The [batch record](../episode-03-review-batch-03.md) documents gallery 145–216 using three
contact sheets, 22 selected originals, translated subtitle cues 159–225 and accepted alignment.
All 72 new rows are SCREENED / INITIAL_REVIEW_COMPLETE, including three EYECATCH graphics.
Episode 3 now has 216 initially reviewed rows (215 SCREENED, one NEEDS_RECHECK at 005);
138 remain untouched. Orta-Honehone maneuver context, bridge displays, Aisha costume/poses,
Horus passage/escape, Blue Heaven exterior and McCoy questioning are indexed. Maintainer
clarification identifies 196–197 as Horus's continuous sub-ether activation/disappearance
sequence; exact effect timing and mechanics remain for targeted review.
The maintainer accepted this batch and clarification on 2026-10-29; no Phase 3.2A work is included.

## Episode 3 annotated survey — batch 04, 2026-10-29

The [batch record](../episode-03-review-batch-04.md) documents gallery 217–288 using three
contact sheets, 25 selected originals, translated subtitle cues and accepted alignment.
All 72 new rows are SCREENED / INITIAL_REVIEW_COMPLETE; 275 is a childhood FLASHBACK.
Episode 3 now has 288 initially reviewed rows (287 SCREENED, one NEEDS_RECHECK at 005);
66 remain untouched. Horus cockpit access, gunner handoff, exterior angles and missile
bank are indexed alongside pirate command-space, launch-tube and fighter references.
Leprechaun/Purgatory wreckage is jointly identified by dialogue without assigning each
fragment. Pirate leaders retain descriptive identities with provisional name leads.
The maintainer accepted this batch on 2026-10-29; no Phase 3.2A work is included.

## Episode 3 annotated survey — batch 05, 2026-10-29

The [final batch record](../episode-03-review-batch-05.md) documents gallery 289–354 using
three contact sheets, 26 selected originals, translated subtitle cues, cached website
context and accepted alignment. All 66 new rows are SCREENED / INITIAL_REVIEW_COMPLETE.
All 354 Episode 3 gallery images now have completed initial reviews: 353 SCREENED and
one NEEDS_RECHECK at 005. No targeted deep-dive completion is implied.
Horus's glowing brand, fighter underside, El Dorado/pirate hull details, recorded governor
message, Aisha's demotion and the hiding-asteroid display are indexed with mechanism,
identity and timing limits. The two final portraits remain unmapped. At survey acceptance,
episode cleanup had not run. The maintainer accepted the
remaining Episode 3 survey batches and clarifications on 2026-10-29, including image 347's
future reference value. No next episode or Phase 3.2A work is included.

### Episode 3 retention checkpoint — 2026-10-29

The [retention record](../episode-03-retention-checkpoint.md) documents the subsequently
authorized archive and cleanup. The complete format-2 EP-03.rar contains 354 gallery
originals and recovery metadata; no manual supplements are registered for this episode.
Native integrity and staged recovery passed during creation; prune independently repeated
recovery/inventory/hash checks before removing the expanded cache. Final status: cached 0,
archived 354, contact sheets 15, unpacked bytes 0, archive hash valid. The archive is
63,800,869 bytes; removing duplicate expanded data reclaimed 64,204,169 bytes. All 53
protected CSV/sheet/registry hashes and sizes matched. No temporary media or archive staging
directories remain. Both generated workbooks are refreshed and verified. Restore originals
from the RAR for later full-size checks; retained contact sheets remain available for browsing.
The maintainer confirmed this retention checkpoint for publication on 2026-10-29.
No next episode or Phase 3.2A work starts here.

## Episode 4 retrospective subtitle/context preparation — 2026-10-29

The [preparation record](../episode-04-context-preparation.md) adds a full read of the 355
ordered English ASS events and pinned local-media/subtitle provenance to the accepted earlier
Episode 4 survey. It reuses the existing Episode 4 context pilot, adds selected Fandom episode
summary/Gilliam captures and five secondary assertions, and records startup, navigation-role,
vehicle/weapon and naming leads. Subtitle halcyon versus wiki Helicon wording remains a
documented discrepancy; earlier annotations and attributed notes are preserved.

Implemented, verified and accepted by the maintainer on 2026-10-29. During this preparation,
no gallery/supplement annotation, image link, historical timing
or alignment table was revised, and the verified Episode 4 archive remains pruned. Episode 4
alignment is the next separate step before the existing annotation/documentation sweep.
No next episode or Phase 3.2A work is included.

The subsequent [Episode 4 alignment](../episode-04-alignment-review.md), implemented and verified
2026-10-29 and accepted by the maintainer on the same date, adds bounded navigation timing without changing earlier annotations
or historical time leads. Reproduction and current-media checks passed; 1,111,216,828 bytes of
temporary alignment output were removed. The verified gallery and nine supplements were restored
for this work and remain available for the next annotation/documentation reconciliation sweep.
The unchanged RAR remains the archive; repeat its established prune procedure after that sweep.

## Episode 4 retrospective reconciliation — 2026-10-29

The [reconciliation record](../episode-04-reconciliation-review.md), implemented, verified and accepted by the maintainer on 2026-10-29,
audits all 354 gallery rows and nine supplements against all 15 retained sheets, selected originals,
translated subtitle windows and cached context. Images 145–146 now correctly describe partly open
eyes; 254 is a present-day STORY reaction rather than a childhood FLASHBACK sample. Attributed
notes, keys, groups, tags, review depth and the one identity recheck (007) are preserved.
Selected rows gain source/subtitle limits, including Gilliam versus Melfina, Horus intercuts,
individual versus installed-engine testing, dock intrusion, ignition/power and weapon distinctions.
Forty-eight secondary image-context links are added; CTX-000014 retains the halcyon/Helicon question.
Manual player times and UNRECONCILED status remain explicit. The accepted alignment registers and
all generated locator CSVs are unchanged. Initial-survey evidence pointers belong in uncertainty
notes; targeted detailed-review fields remain empty. This does not promote review depth or start 3.2A.

After the sweep, the existing RAR passed fresh staged recovery/hash/recovery-metadata checks and
the normal prune removed all 354 expanded gallery images and nine supplemental originals again.
All 15 sheets remain; the unchanged archive retains 354 images and nine supplements. No alignment
candidate output or temporary restore/packing folders remain. Both ImportExcel views are refreshed
and verified; manual links require restoration. The reconciliation record owns the preservation
checks, exact counts and remaining research questions. No next episode starts automatically.

The subsequent broader documentation audit is recorded in the same reconciliation record. It
updates related room/component evidence, operational vocabulary, open questions, roadmap and
historical reference pointers without changing accepted design decisions. CSVs and both generated
workbooks remain byte-identical to the post-sweep versions, so another refresh is unnecessary.
The maintainer accepted the documentation and cleanup checkpoint on 2026-10-29; Phase 3.2A remains unstarted.

## Episode 5 gallery and subtitle/context preparation — 2026-10-30

The [preparation record](../episode-05-context-preparation.md) records the preceding verified
354-image download and 15 chronological sheets, followed by a full read of all 379 English ASS
events and selected website context. Local subtitle intervals remain separate from web labels.
One selected Fandom episode-summary capture and existing AnimeHistory/Aisha/Swanzo/Melfina/ship
sources supply seven new secondary assertions and reuse of earlier scoped records. The unavailable
standalone Mikey lookup remains explicit. No image associations or primary promotions are added.

Context/cache/category validation, preservation checks and the refreshed five-tab ImportExcel
context view passed. All 354 Episode 5 image records remain UNREVIEWED / NOT_REVIEWED; gallery
originals and contact sheets remain local for the upcoming survey. No Episode 5 RAR or timing
mapping was created during preparation. The maintainer accepted this preparation on 2026-10-30;
the subsequent alignment results follow. No Phase 3.2A work is included.

## Episode 5 bounded alignment — 2026-10-30

The [alignment record](../episode-05-alignment-review.md) documents 13 predeclared attempts:
seven matched intervals and six ambiguous held/repeated drawings. Three FIT anchors froze the
offset before four independent HOLDOUT matches validated ALNMAP-000010. Navigation coverage is
web labels 01:43–22:58 inclusive, with `local = web - 1.232 s`: all 354 gallery rows, seven direct
intervals and 347 estimates. No entire-runtime alignment or exact subtitle association is implied.

Current-input validation and early/late frame-hash reproduction passed. The category workbook
refreshed and passed saved-data/link and visual checks. All four owned search runs were removed
through the inspected cleanup preview, releasing 776,723,199 bytes; gallery originals and 15
sheets remain. Earlier episodes, context data and image annotations are unchanged. The maintainer
accepted this alignment checkpoint on 2026-10-30; the first three-sheet image review is the next
separate step. No Phase 3.2A work is included.

## Episode 5 annotated survey — batch 01, 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Gallery 001–072
(848189–848260) received individual descriptions, overlapping tags, priorities, uncertainty
notes and 20 contiguous scene groups. All three contact sheets were visually reviewed;
full-size originals inspected were 002, 006, 007, 014, 015, 018, 025, 026, 033, 035,
036, 055, 067 and 071. No new video extraction was performed. The accepted alignment's
temporary frames remain removed and are not claimed as newly inspected survey evidence.

ALNMAP-000010 supplies `local = web - 1.232 s` navigation coverage for all 72 labels,
with two direct matches at 001/011 and estimates elsewhere. The two-second search half-window
does not establish an exact subtitle/frame association. Translated English ASS cues 30–105
were reread: video-call/docking discussion (02:30.02–02:57.14), Hilda's death and Gene's plans
(03:05.99–03:33.94), registration/paint/supplies negotiation (03:34.02–04:28.13), Swanzo's
backstory and limited knowledge (04:32.68–05:25.79), Ctarl inquiry/work arrangements
(05:25.93–05:48.58), and hull-color choice/Gilliam farewell (05:48.65–06:01.49).
Speaker/subject associations use visual continuity and selected secondary context, not empty
subtitle Name fields or the numerically closest web label.

Opening 001–013 remains separate from story action: XGP exterior, the unresolved launch-site
view, Gene's gun framing, caster still life, portraits, Suzuka clothing, the three-woman
composition, the XGP/El Dorado vignette and crew montage. Japanese title 024 is not independently
transcribed. Image 002 remains NEEDS_RECHECK for the craft/facility identity; no XGP planetary
launch or Sentinel III location is inferred. Other cropped montage identities remain qualified
in row notes without promoting the scene to present-day narrative evidence.

Images 014–021 show green Swanzo outside his suit, reclining in a pink support inside a transparent
chamber, with tea service, headset and Mikey's video call. Chamber contents, pressure, gravity,
dimensions and life-support operation remain unverified. The name Mikey in cue 31, call continuity,
selected Swanzo biography and later matching goggled mechanic support the initial-survey association
in 018/020 and dock views. Its independent appearance-source confirmation remains limited;
the batch checkpoint retained PROVISIONAL identity and left earlier Episode 3 rows unchanged.
The subsequent [cross-episode identification update](#cross-episode-mikey-identification--2026-10-30)
records the current catalogue identity and retrospective corrections.

The rounded teal figure in 027–028 and later dock conversations is Swanzo in his suit, not Gilliam.
Plain and patterned yellow visor lights, side headset, red trim, gloves, belt and pale side fittings
are useful appearance references. Their changes do not establish a display/emotion algorithm.
Gilliam is addressed in the final dialogue but that does not identify a visible Gilliam body.

Images 025–026 and 033–035 are high-priority unpainted XGP exterior/service references: underside
motifs, seams, recessed equipment, circular assemblies, forward silhouette, hanging connections
and articulated dock work arms. Do not relabel surrounding service arms as the ship's grapplers,
assign exact service-line functions or infer internal rooms from exposed external panels.
Registration and repaint are promised; the dialogue explicitly excludes obtaining grappler weapons
locally. The remaining portraits preserve Gene/Jim/Melfina/Mikey/Swanzo expressions and costume
details through that negotiation, Hilda backstory, Ctarl warning and color discussion.

CTX-000073 adds only Swanzo's readable unsuited appearance description from CTXSRC-000016,
SECTION:0007, as SOURCE_CHECKED / SECONDARY_ONLY. Existing partner, Blue Heaven, registration
and backstory assertions are reused. Thirty links are added, including selected image associations;
these are contextual, not exact timing links or primary-evidence promotions. No new website
retrieval, manual supplement or targeted deep-review status is introduced.

All 72 rows are INITIAL_REVIEW_COMPLETE: 71 SCREENED and one NEEDS_RECHECK (002).
The remaining 282 Episode 5 rows and all other episodes are untouched. Maintained records validate;
9,132 out-of-batch category rows, prior context claims/links/sources and 403 protected input hashes
are preserved. The only existing context-subject edit updates the scoped Mikey association note.
The refreshed ImportExcel category view retains 30 tabs, with 432,588 gallery cells, 9,204 image
links, 510 manual cells and 3,819 alignment cells verified. The five-tab context view verifies
10,599 cells and 1,969 links; both builders confirm authored-data equality. Rendered recheck,
chamber, XGP service, dock, overview, new claim and Mikey-note views passed visual inspection.
No fresh native Office Viewer test is claimed. Disposable helpers/previews are removed. Media and cited
source caches remain local-only. Next separate batch: 073–144. No Phase 3.2A work is included.

## Cross-episode Mikey identification — 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Thirty previously unnamed mechanic rows
are identified as Mikey using Episode 5's named video call (018/020, translated English ASS
cue 31), matching dock appearance and the existing CTX-000060 partner context. The retained
Episode 2 sheets 0217–0240 and 0241–0264 and Episode 3 sheets 0049–0072 and 0073–0096
were visually rechecked. No originals were restored and no new media or website retrieval occurred.

- Episode 2: 228, 229, 232, 234–244, 249–251 and 254 (18 rows).
- Episode 3: 054, 058–059, 066–069, 071–072, 074–075 and 079 (12 rows).

Clear views match brown hair, yellow goggles, blue tank top, pink trousers and white gloves.
Episode 2's cropped trouser/boot views (232, 234–235, 239, 242–244) retain MEDIUM confidence
and explicit adjacent-shot continuity limits. Distant overhead views (Episode 2: 228–229,
240–241, 254; Episode 3: 058–059, 079) also retain MEDIUM confidence. Clearer views use HIGH.
The subject registry's ESTABLISHED status applies to this scoped catalogue identity; it does not
establish a complete biography or independently sourced appearance article.

Visible descriptions, attributed earlier tentative notes, scene groups, review statuses/depths
and priorities are preserved. Earlier review records below and in the linked batch documents
describe their original evidence state; this section owns the subsequent identification scope.
CTX-000060 remains SOURCE_CHECKED / SECONDARY_ONLY. Thirty contextual image links
(CTXLINK-000903–000932) reuse that assertion without primary-evidence or exact-timing promotion.
The context tables contain 44 subjects, 26 sources, 73 assertions and 932 links.

Category/context validation passes. Preservation checks confirm the other 9,174 category rows,
prior context assertions/sources/links and 84 protected input, archive and contact-sheet hashes
are unchanged. Episode 5's pending batch 01 annotations remain intact. No Phase 3.2A work is included.
Both ImportExcel workbooks refreshed with authored-data equality verified: category view retains
30 tabs, 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819 alignment cells;
context view retains five tabs with 10,869 cells and 2,029 links verified. Rendered Episode 2/3
tags, cropped-view qualification and the subject registry passed visual inspection. No new
native Office Viewer test is claimed. Temporary reconciliation helpers and previews are removed.

## Episode 5 annotated survey — batch 02, 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Gallery 073–144
(848261–848332) received individual visible descriptions, overlapping tags, priorities,
qualified context and 14 contiguous groups, EP-05-S021–S034. All three sheets were visually
reviewed. Full-size originals inspected: 073, 074, 075, 078, 085, 086, 088, 094, 095,
101, 103, 106, 111, 117, 119, 126, 132, 134, 139, 140, 141 and 143. No new media
extraction, source retrieval, manual supplement or targeted deep review was performed.

ALNMAP-000010 supplies navigation estimates (`local = web - 1.232 s`) for all 72 labels;
none has an accepted direct matched interval. Ambiguous anchor attempts at 078 and 094
remain ambiguous. Translated English ASS cues 106–183 were reread: grief/memory disagreement
(06:12.21–06:42.90), memory and spaceflight discussion (06:58.36–07:41.93), food/interruption
(07:45.04–07:56.31), Aisha introduction/Hilda inquiry (07:58.55–08:51.83), Leyline demands
(08:53.70–09:18.46), threats and flight (09:18.53–09:41.35), and pursuit/fight context
(09:49.06–10:21.16). These local intervals bracket narrative action; they do not identify
every speaker or assign a subtitle to its numerically nearest web label. Silent alley action
remains distinct from spoken context. The pinned preparation record owns track/hash provenance.

073 is a high-priority unpainted XGP underside/service reference, continuing the earlier hull
views. Surrounding articulated service arms are not relabeled as XGP grapplers. 074 shows
colored spherical lights/fixtures, not identified planets. The two-bed room, mirror-shaving
view and green hinged door in 075–085 are retained as Blue Heaven scene references without
assigning the room to the ship, a named hotel or a measured floor plan. 086 is a brief Hilda
final-confrontation recollection, not a new present-day event; small figures retain MEDIUM
identity confidence and no new explosive-mechanism claim. 087 records Gene's visible reaction.

088, 101, 113 and 143 are high-priority station environment references: multiple levels,
shopfronts, illuminated signs, railings, drains, rough alley walls and service pipes. Sign text
is not independently transcribed. The crew's discussion in 089–100 names the Physical Navigation
System and contrasts Gene's subjective ship-piloting experience with his space anxiety; it does
not establish technical architecture, sensor placement or numerical performance. The blue-gloved
hand at Gene's shoulder in 094 is his own, not Melfina's.

Aisha's hooded and cropped views use her named introduction, subsequent face reveal, existing
CTX-000057 appearance context and local continuity. The hand/cloak-only views remain MEDIUM.
117 and 132 are high-value face/headband/cheek-mark references. Collar-grip, angry/comic reactions,
clenched fists, evasive crew poses and the broken-pavement view in 134 preserve useful action
endpoints without inventing a complete animation or power scale. 139 is a raised boot/defensive
pose, not a newly identified weapon. 140 is a dark motion/impact insert with no resolved object
or contact point. No actual Galactic Leyline coordinates are supplied.

Cached CTXSRC-000026 SECTION:0002 and CTXSRC-000021 SECTION:0004 were reread for encounter
context. Nineteen links, CTXLINK-000933–000951, reuse CTX-000043, CTX-000057 and CTX-000067
for selected station, appearance and Leyline-demand views. All assertions retain their prior
status; no duplicate assertion, source refresh or primary-evidence promotion is added.

All 72 rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 5 now has 144 initial-review
rows (143 SCREENED, one NEEDS_RECHECK at 002) and 210 unreviewed rows. Validation and preservation
checks confirm the other 9,132 category rows, all previous context links, subject/source/assertion
tables and 406 protected input/media/timing hashes are unchanged. Next separate batch: 145–216.
Phase 3.2A remains unstarted.

Both ImportExcel projections refreshed with authored-data equality verified. Category view retains
30 tabs, 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819 alignment cells.
Context view retains five tabs with 11,040 cells and 2,067 links verified. Rendered hull tags,
room qualification, Aisha portrait, pavement action and added context-link views passed visual
inspection. No new native Office Viewer test is claimed. Disposable batch helpers and previews
are removed; gallery originals and contact sheets remain available for the continuing survey.

## Episode 5 annotated survey — batch 03, 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Gallery 145–216
(848333–848404) received individual descriptions, overlapping tags, priorities and qualified
context in 15 contiguous groups, EP-05-S035–S049. All three sheets were visually reviewed.
Full-size originals inspected: 145, 149, 150, 151, 157, 161, 165, 171, 173, 175, 177,
181, 182, 183, 187, 195, 201, 202, 212 and 216. No new extraction, source retrieval,
manual supplement or targeted deep review was performed.

ALNMAP-000010 covers all 72 labels. 163 and 181 have accepted direct intervals at
686.811–686.853 s and 751.459–751.793 s; the other 70 receive navigation estimates using
`local = web - 1.232 s`. The ambiguous 154 attempt remains estimate-only. English ASS cues
181–244 were reread, spanning 10:11.35–14:59.37 local: attempted beast-power/moon-phase
discussion (184–196), pursuit/caster-shell errand (197–207), garden arrival and Gene's strain
(208–211), artificial flowers and Melfina's origin questions (212–218), android discussion
and cheek touch/pinch (219–225), and Gene's promise/invitation (226–243). Cue 244 brackets
the subsequent Jim contact. These are scene-navigation ranges, not automatic nearest-label
speaker assignments or universal exact subtitle/frame matches. Prepared track/hash provenance
and earlier alignment evidence remain unchanged.

145–164 retain Aisha's cloak changes, braid, pointed nails, gold bangles, face, outfit, tail,
stance and running pose. 149, 157–158 and 163 are high-priority future character/action references.
Tight hand/shoulder crops retain MEDIUM identity confidence from continuity. The pink blush
patches in 161 are a comic drawing state. The dialogue's inherited-power and moon-phase claims
remain translated character statements; no complete beast transformation, claw-extension
mechanism, universal moon rule or numerical power specification is verified. This attempted
transformation is distinct from the later exhaustion scene described in secondary context.

165–170 preserve Blue Heaven shop-walkway staging, doors, shutters, signs, drain and Jim's
satchel/clothing. The instruction to buy caster shells is an errand, not a visible purchase
or a newly identified ammunition prop. 168 provides a high-priority unobstructed environment
view. 171–173 are EYECATCH graphics, separate from story action and the proposed end-sequence
To Be Continued motif. 173 is a useful outlined emblem/yin-yang/star reference; no animation
timing, audio synchronization or interface implementation is established.

174–184 show Gene and Melfina reaching the green-lit station garden, Gene's visible strain,
Melfina assisting him and the bench. 182's framed star-speckled panels are seen through his
fingers, supported by the adjacent 183 eye/glove shot. No display technology, optical design,
clinical diagnosis or gravity measurement is inferred. 175, 181, 186, 201, 212 and 216 are
high-priority environment/staging views, not XGP interiors or a measured station floor plan.

187–188 retain blossom shapes and colors. The English dialogue explicitly identifies the
flowers as artificial; their appearance alone does not establish material, manufacturing
process, botanical species or that every surrounding shrub is artificial. Melfina's tears,
cheek touch/pinch reactions and later smiles remain useful performance references, especially
195. Gene calls her an android and promises to find her past; those translated statements
do not identify her creator, specify her physiology or record a completed search. 205–216
retain that promise and the lighter bench conversation without changing its future-intent status.

Cached CTXSRC-000021 SECTION:0004 and CTXSRC-000003 SECTION:0004/BLOCK:0009 were reread.
Seventeen links, CTXLINK-000952–000968, reuse CTX-000057, CTX-000043 and CTX-000072 for
selected appearance, station and promise-context images. No new source/assertion or primary
promotion is added. Existing context counts remain 44 subjects, 26 sources and 73 assertions,
with 968 links after this increment.

All 72 rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 5 now has 216 initial-review
rows (215 SCREENED, one NEEDS_RECHECK at 002) and 138 unreviewed rows. Validation and
preservation checks confirm the other 9,132 category rows, earlier pending batch, prior
context links/tables and 406 protected input/media/timing hashes are unchanged.
Next separate batch: 217–288. Phase 3.2A remains unstarted.

Both ImportExcel projections refreshed with authored-data equality verified. Category view retains
30 tabs, 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819 alignment cells.
Context view retains five tabs with 11,193 cells and 2,101 links verified. Rendered Aisha outfit,
eyecatch classification, overhead garden, artificial-flower qualification and added context-link
views passed visual inspection. No new native Office Viewer test is claimed. Disposable batch
helpers and previews are removed; originals and contact sheets remain for the continuing survey.

## Episode 5 annotated survey — batch 04, 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Gallery 217–288
(848405–848476) received individual visible descriptions, overlapping tags, priorities and
qualified context in 13 contiguous groups, EP-05-S050–S062. All three sheets were visually
reviewed. Full-size originals inspected: 222, 223, 224, 228, 229, 230, 232, 233, 240,
241, 243, 244, 248, 250, 259, 262, 266, 270, 272, 287 and 288. No new video extraction,
website retrieval, manual supplement or targeted deep review was performed.

ALNMAP-000010 covers all 72 labels. 228 and 235 have accepted direct intervals at
921.546–921.587 s and 946.737–946.821 s; the other 70 receive navigation estimates using
`local = web - 1.232 s`. English ASS cues 238–310 were reread: invitation/radio rendezvous
(238–249, 14:37.85–15:12.68 local), renewed confrontation and power claims (250–257,
15:12.88–16:12.10), officer/pay and meal discussion (258–280, 16:26.39–17:46.86), renewed
arrest and beast-power threats (281–298, 17:55.51–18:55.40), and the shell offer (299–303,
18:55.60–19:04.98). The remaining cues through 310 provide bounded lookahead for the later
caster/restaurant aftermath and transition; they do not extend this batch's image review
or establish a firing action in 288. Subtitle proximity alone does not assign speakers or
exact image/dialogue synchronization. The pinned track/hash and earlier alignment remain unchanged.

217–221 continue the garden invitation and contact with Jim. 222 is a high-priority street-art
reference. 223 shows Jim's small blue ear fitting and communication pose without establishing
its internal design or radio range. 224–225 are high-priority weapons/equipment-shop interiors:
long guns, dense shelves, floor bins, overhead claw-ended hardware and an upright armored
figure/display. Equipment models and the shop's proper name remain unassigned; the upright
form is not labeled Gilliam or Swanzo. The dialogue initially reports poor shell prospects;
these images do not show the eventual purchase. Signs are not independently translated.

226–242 retain Aisha's return, Gene's crossed-arm blocking pose, uncoated harness/holster views,
Aisha's braid, tail, rear pouch, power-claim poses and collapse. 232–234 are high-priority
costume references. The red/pink 230 insert remains qualified by adjacent Gene costume/action
continuity; it does not establish a resolved face, exact strike contact or equipment damage.
Aisha's half-power/full-beast statements are boasts, not measured force or skin durability.
240–242 visibly show the kneeling/floor endpoints; cue 257 supplies the calorie-exhaustion
explanation without establishing an energy budget or completed beast transformation.

243 is a high-priority crowded restaurant-facade reference, with unnamed pedestrians and no
verified business-name translation. 244–268 retain red chairs, lattice walls, tableware, food,
eating poses, the white-jacketed unnamed server and growing used-bowl stacks. 244, 248, 250
and 266 are high-priority food/prop references. 250 pours red liquid from a brown bottle;
neither an alcoholic drink nor a sauce type is independently identified. Appetite, Resident
Officer claims and lack of imperial money remain scene dialogue, not general biological or
payroll rules. Comic bowl/crew movements do not establish a measured impact sequence.

269–286 preserve Aisha's gestures, expressions, renewed arrest demand and transformation
threats, plus Gene/Jim's responses. 270 and 272 are useful future character-performance views.
287–288 introduce Jim's offered caster shell. 288 is high priority for the future caster work:
rounded end, cylindrical casing, ring seams, collar and surface wear. Cue 301 identifies the
offered shell as number 12 and reports an excessive price; no printed number is read on the
image. No caliber, internal mechanism, measured price, effect, loading or firing sequence is
established in this batch. The cropped gloved hand is linked to Jim through scene continuity.

Cached CTXSRC-000021 SECTION:0004 and CTXSRC-000026 SECTION:0002 were reread. Eighteen links,
CTXLINK-000969–000986, reuse CTX-000043, CTX-000057, CTX-000071 and CTX-000072 for selected
station, appearance, exhaustion and invitation views. No new source/assertion or primary
promotion is added. Context counts remain 44 subjects, 26 sources and 73 assertions, with
986 links after this increment.

All 72 rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 5 now has 288 initial-review
rows (287 SCREENED, one NEEDS_RECHECK at 002) and 66 unreviewed rows. Validation and preservation
checks confirm the other 9,132 category rows, earlier pending batches, previous context links
and 406 protected input/media/timing hashes are unchanged. Next separate batch: 289–354.
Phase 3.2A remains unstarted.

Both ImportExcel projections refreshed with authored-data equality verified. Category view retains
30 tabs, 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819 alignment cells.
Context view retains five tabs with 11,355 cells and 2,137 links verified. Rendered shop,
rear-costume, shell appearance, shell qualification and added context-link views passed visual
inspection. No new native Office Viewer test is claimed. Disposable batch helpers and previews
are removed; originals and contact sheets remain available for the final Episode 5 batch.

## Episode 5 annotated survey — batch 05, 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Gallery 289–354
(848477–848542) received individual visible descriptions, overlapping tags, priorities and
qualified context in 16 contiguous groups, EP-05-S063–S078. All three final sheets were
visually reviewed. Full-size originals inspected: 289, 290, 292, 293, 295, 301, 302, 307,
313, 314, 324, 333, 334, 336–339, 342, 348, 352 and 354. No source-video extraction,
website retrieval, new manual image or targeted deep-review completion is claimed.

ALNMAP-000010 covers all 66 labels. 354 retains its accepted direct interval at
1376.500–1376.542 local seconds; the other 65 are navigation estimates using
`local = web - 1.232 s`. Earlier ambiguous attempts at 328, 334 and 353 remain estimates.
English ASS cues 299–366 were reread: shell number 12, caster confrontation and bill
(18:55.60–19:35.30), repaint/registration and Gilliam integration discussion
(19:43.25–20:24.39), pirate territories, Fred Luo and farewell (20:27.73–21:39.19),
clearance/beacons and launch call (21:46.91–22:26.40), and Aisha's dishwashing aftermath
(22:34.69–22:58.65). These are translated scene-navigation intervals, not exact matches
between every sampled image and subtitle line. Ending lyrics and Episode 6 preview remain
outside this gallery batch's narrative attribution.

289–295 retain the silver-gray shell, caster rear opening/linkage and side fitting, upright
handling pose, comic eye insert and Aisha's spiral-eyed, ragged, smoke-wreathed aftermath.
289, 290, 292 and 295 are high-priority caster references. Number 12 comes from cue 301,
not a readable shell marking. 293 is a stylized reaction insert, not a resolved projectile
or beam diagram. The sampled images do not cover the complete loading, closure, aiming,
firing and impact sequence. The planned maintainer-supplied screenshots between 289 and 295
remain pending and will receive separate manual IDs and observed player-time provenance.
No caliber, effect measurement, universal shell behavior, lethality or internal mechanism
is inferred. 296–298 preserve Gene's departure and the unnamed restaurant personnel;
dialogue assigns Aisha the bill without establishing its amount or payment completion.

299–312 retain the station return, repainted XGP and dock conversation. 301–302 are
high-priority upper-hull/nose references: red finish, blue perforated trim, gold tip,
cockpit window, fins, panel seams and external service connections. 307–308 provide
companion underside views; dark shading does not establish a permanent black belly finish.
Articulated dock tools are separate from ship grappler arms. Dialogue confirms registration
and paint, not complete weapons outfitting; no written registration number is read.
Mikey and suited Swanzo remain distinct from Gilliam. 312 preserves Swanzo's suit/eye
drawing and side fitting. The translated AI-integration statement does not establish
permanent inseparability or a complete control architecture. Sentinel III remains the
intended destination, not a completed arrival.

313–332 preserve the station meeting-room chart, sofa, separate chair, small computer,
closed door and character performance. 313–315 and 324 are high-priority chart/environment
and Swanzo-suit references. This is not assigned as an XGP interior. Translated dialogue
names Tempa Empire, Kei/Ban territory, Heifong and the Fred Luo procurement lead; the
unlabeled chart does not establish measured borders, coordinates or a plotted route.
Fred remains an absent dialogue referent. Jim's alarm, coat pulling and Gene's farewell
gestures are performance references, not measured fabric behavior or completed procurement.

333–345 retain Blue Heaven's exterior and dock platform, then the XGP cockpit. 333–334
are high-priority station references, including readable BLUEHEAVEN, WELCOME! and Private
signs. 335–339 and 342 are high-priority cockpit references: the pilot seat and ceiling,
overhead circular Gilliam unit, curved grips, Melfina's red-framed display/controls, Jim
leaning behind a seat, and the upright lever in a slotted base beside rings and round
controls. Screen symbols, control command mappings and exact clearances remain unverified.
Melfina is clothed in a cockpit seat, not visibly in her apparatus. Surrounding starfield
presentation alone does not distinguish windows from projected display. Clearance, beacon
confirmation, following beacons and Gene's later launch call remain separate statements;
no complete flight checklist, ignition cycle or autonomous-navigation algorithm is established.
346–347 show an asteroid field with no resolved ship, not a verified sub-ether effect.

348–354 retain Aisha's yellow apron, foamy sink, crockery stacks, cleaning props, tiled
restaurant kitchen, extractor hood and comic expressions. 348 and 354 are high priority
for environment/prop and facial-performance work. Restaurant labor follows the bill
aftermath, but no wage, debt amount or precise employment arrangement is established.
This is Blue Heaven restaurant space, not an XGP galley.

Cached CTXSRC-000026 SECTION:0002, CTXSRC-000021 SECTION:0004,
CTXSRC-000016 SECTION:0001/BLOCK:0027 and CTXSRC-000025 SECTION:0001 were reread.
Thirty-nine links, CTXLINK-000987–001025, reuse CTX-000043, CTX-000060,
CTX-000065, CTX-000066, CTX-000068 and CTX-000069 for selected station, mechanic,
AI, repaint, caster/bill and destination-context images. No source/assertion or primary
promotion is added. Context totals are 44 subjects, 26 sources, 73 assertions and 1,025 links.

All 66 rows are SCREENED / INITIAL_REVIEW_COMPLETE. Episode 5's complete sampled gallery
now has 354 initial-review rows: 353 SCREENED and one NEEDS_RECHECK at 002. No gallery
row remains unreviewed in this episode. Global counts are 1,758 SCREENED, 12 NEEDS_RECHECK
and 7,434 UNREVIEWED; depth counts are 1,712 INITIAL_REVIEW_COMPLETE, 58 PARTIAL and
7,434 NOT_REVIEWED. Validation and preservation checks passed for all other 9,138 category
rows, existing context-link prefixes, reported notes and 406 protected media/input/timing
hashes. This is initial gallery coverage, not complete episode-footage or mechanism analysis.

Next: add the planned caster supplements, then verify/archive and prune through the accepted
episode cleanup procedure when authorized. Originals and contact sheets remain available;
no Episode 5 archive or media cleanup is performed in this increment. No later episode or
Phase 3.2A work is included.

Both ImportExcel projections refreshed with authored-data equality verified. The category
view retains 30 tabs, 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819
alignment cells. The context view retains five tabs with 11,706 cells and 2,215 links
verified. Changed shell, hull, cockpit-control, uncertainty and context-link ranges were
rendered and visually inspected. No fresh native Office Viewer test is claimed. Disposable
batch authoring helpers, baseline and preview images are removed after verification;
episode media are retained for the planned supplements.

## Episode 5 caster supplements — 2026-10-30

Status: implemented, verified and accepted by the maintainer on 2026-10-30. Sixteen supplied screenshots
are preserved byte-for-byte as EP-05-MAN-001–016 under
`reference/working/manual-supplements/EP-05/`. Their total size is 45,577,793 bytes.
The supplemental CSV retains individual SHA-256s, sizes, original attachment filenames,
whole-second VLC labels, contextual gallery links and supplied sequence order. No cropping,
recompression, deduplication, video extraction or source-media modification was performed.
Near-repeat flare states remain separate records. Player chrome, black bars, pause symbols
and Next frame overlays are capture artifacts, not anime artwork.

| Manual IDs | Visible player labels | Observed reference content |
| --- | --- | --- |
| 001–005 | 19:04, 19:05, 19:06, 19:06, 19:07 | Gene handling the open/displaced caster rear assembly beside Jim, fingers at the opening, changing linkage positions and a later seated/closed appearance. |
| 006–010 | 19:13 for all five | Caster held upright beside Gene's head; small pink flare, broadened pink shapes, a large jagged lateral flare, a smaller pink state, then yellow-white flare/streaks with pink remaining around the weapon. |
| 011 | 19:14 | Forward-facing circular muzzle and front fittings surrounded by a broken pink ring. |
| 012 | 19:15 | Blue-white luminous ball-like form at the forward-facing muzzle with pale ribbon-like tendrils and detached spots. |
| 013–014 | 19:15 for both | Aisha's raised fists and subsequent exaggerated reaction amid blue-white luminous forms and crossing/curving streaks. |
| 015–016 | 19:17 for both | Aisha leaning back with arms spread under cyan illumination, then inverted with wrapped lower legs/soles raised, ragged costume and tail visible beside a curved bright streak. |

All sixteen are HIGH priority and SCREENED / INITIAL_REVIEW_COMPLETE. The sequence is useful
for future caster modeling, handling animation and visual-effect work, with a revisit pointer
to SET-136. It does not authorize weapon implementation. Visible loading/closure states are
recorded without claiming a fully established insertion path, latch identity, internal feed
mechanism, joint axis or dimensions. Colored flare and discharge shapes are observations;
charge physics, projectile material/speed, continuous-beam behavior, damage, lethality and
universal number-12 behavior remain unverified. Shell number 12 retains its prior translated
dialogue basis rather than a newly read marking. Partial finger/weapon occlusion remains explicit.

Manual IDs preserve supplied order where player labels repeat. Every record retains
PLAYER_UI_WHOLE_SECONDS / UNRECONCILED: no decoded frame PTS, consecutive-frame guarantee,
exact duration or independent gallery match is claimed. The visible release title identifies
Episode 5 and the CA71B58C label, but does not supply a binary source identity or subsecond
alignment proof. Contextual associations bracket gallery 289–290, 292–293 and 292/295;
they do not rewrite the accepted mapping or its direct-versus-estimated distinctions.

Only gallery 289–295 receive follow-up uncertainty wording and attributed supplied-context
notes linking the new states. Their original visible summaries, tags, priorities, review
provenance and detail depth remain unchanged. The other 9,197 gallery rows and all ten earlier
manual records are unchanged. Sixteen links, CTXLINK-001026–001041, associate the supplements
with existing CTX-000068's caster/incapacitation/bill narrative. No new source/assertion or
primary-status promotion is added. Context totals remain 44 subjects, 26 sources and 73 assertions,
with 1,041 links. Gallery coverage/status counts are unchanged; manual-reference count is 26.

Validation passed, including present-file hashes/sizes for all sixteen new originals,
exact preservation of existing manual/context prefixes, bounded gallery-field changes and
405 protected input/media/timing hashes. The supplements will join the Episode 5 RAR through
the accepted archive-and-prune procedure during authorized episode cleanup. They remain
expanded with gallery originals for now. No cleanup, next episode, commit or Phase 3.2A work
is included in this supplement increment.

Both ImportExcel workbooks refreshed with source-data equality verified. The category
projection retains 30 tabs, 432,588 gallery cells, 9,204 gallery image links and 3,819
alignment cells; its expanded manual view has 1,326 verified cells for 26 records.
The context projection retains five tabs with 11,850 verified cells and 2,247 links.
Changed manual identity/time/availability, loading, flare, discharge/reaction and context-link
ranges were rendered and visually inspected. No fresh native Office Viewer test is claimed.
Disposable authoring helpers, baseline and preview images are removed; the sixteen reference
originals remain available for review and later archive inclusion.

## Episode 5 retention checkpoint — 2026-10-30

Status: cleanup authorized, implemented, verified and accepted by the maintainer on
2026-10-30. The initial survey covers all 354 sampled gallery images
(353 SCREENED, one NEEDS_RECHECK at 002), plus sixteen HIGH-priority initial-review caster
supplements. Initial coverage does not settle the unidentified recurring opening craft at 002,
internal caster mechanics, exact manual-image timing or other retained detail questions.

Before pruning, `models.py validate --current --episode 5` with the installed FFprobe passed
VERIFIED_CURRENT_EP05. The alignment finish preview found no runs and zero removable bytes;
the earlier four-run cleanup remains intact. No new search/reproduction frames were created.
Durable anchor/mapping records and their timing distinctions remain unchanged.

The first complete format-2 archive was created with `episode_gallery.py archive --episode 5
--compression 3`, using WinRAR 7.13 x64, non-solid compression. It includes 354 gallery JPGs,
their manifest, all sixteen EP-05-MAN PNG originals and the supplemental recovery metadata.
Native RAR integrity, staged restoration, decoding, exact inventory and image/hash comparisons
passed before promotion. Observed creation/recovery verification time was 90.328 s.

| Retained artifact / size | Result |
| --- | --- |
| `reference/cache/animehistory-review/archives/EP-05.rar` | 107,537,634 bytes |
| Archive SHA-256 | `8373923f7887c3166f9b42b0b5b89060d2b20081b342de10d286e7d15155285f` |
| Packing inputs including recovery metadata | 108,062,011 bytes |
| Compression saving against packing inputs | 524,377 bytes, approximately 0.49% |
| Receipt | `reference/cache/animehistory-review/archives/EP-05.json`; complete, archive format 2, gallery 354, supplements 16 |
| Contact sheets retained | All 15 PNGs, 52,773,132 bytes, plus unchanged `sheets.json` registry |

`episode_gallery.py prune --episode 5 --progress-saved` independently restored and checked
the archive again, compared its manifest and current supplemental recovery snapshot, then
removed the expanded gallery cache and all sixteen registered supplemental PNGs. Both emptied
episode media directories are absent. Removed expanded data totals 108,047,676 bytes:
62,469,883 bytes of gallery cache/manifest and 45,577,793 bytes of manual PNGs. This removal
is measured separately from the newly retained RAR; it is not a claim of that amount of net
compression saving. Contact sheets, research records, cited context captures and existing
subtitle copies remain available under their separate retention rules.

Final gallery status: cached 0, archived images 354, archived supplements 16, contact sheets 15,
unpacked bytes 0 and archive hash valid. All 63 protected CSV, sheet/registry, earlier archive
and subtitle-provenance hashes match the pre-cleanup baseline. Authored annotations, manual
player labels/hashes/order and context records are unchanged. No archive packing, verification,
prune-verification or restore staging directories remain. The empty manual folder was removed
by the tool; no unrelated working-directory cleanup was performed.

Both generated ImportExcel views are refreshed after pruning. Supplemental availability is
NOT_LOCAL and paths/IDs remain available for later verified restoration; this does not reduce
review coverage. Later full-size work uses `episode_gallery.py restore --episode 5`, or
`restore --episode 5 --supplements-only` for the manual PNGs alone, followed by normal verified
prune after use. Current-media timing verification requires restoring its gallery inputs.

Episode 6 is the next episode in the adopted sequence, but is not started automatically.
No source media, archive, screenshot or workbook is published, and no Phase 3.2A work is included.

Post-prune workbook checks passed: 30 category tabs, 432,588 gallery cells, 9,204 gallery
links, 1,326 manual cells and 3,819 alignment cells; five context tabs, 11,850 cells and
2,247 links. Authored-source equality passed for both builds. All sixteen Episode 5 manuals
are NOT_LOCAL; the context overview now counts 21 linked archived manual images globally.
Changed availability and overview ranges were rendered and visually inspected, without a
fresh native Office Viewer claim. Disposable cleanup-baseline, check and preview files are
removed after verification; contact sheets, archive/receipt and durable evidence remain.

## Episode 6 gallery preparation — 2026-10-30

Download and contact-sheet preparation are complete for **The Beautiful Assassin**;
the maintainer accepted this checkpoint on 2026-10-30. The existing gallery tool prepared all 354 indexed
images, IDs 848543–848896, with web labels 00:01:43–00:23:07. All originals decoded and
passed manifest hash/inventory verification: 354 cached, zero failed or missing. JPEG
payload totals 62,202,827 bytes; the expanded cache including its manifest is 62,623,017 bytes.

All 15 chronological contact sheets remain under
`reference/contact-sheets/animehistory-review/EP-06/`. Their registry hashes, 1600 × 2056
dimensions and complete ordered image-ID/web-time/source-hash mapping passed verification.
The final sheet contains 18 images. The first, middle (169–192) and final sheets were
visually inspected for layout, readable labels and image presentation. Sheet PNGs total
52,085,220 bytes, excluding the registry.

Command: `python tools/reference-extraction/episode_gallery.py prepare --episode 6`.
Status and independent registry checks passed afterward. Originals and recovery manifest
remain under `reference/cache/animehistory-review/EP-06/`; no Episode 6 RAR exists yet.
All 354 annotation rows remain UNREVIEWED / NOT_REVIEWED. Website/subtitle preparation,
alignment and annotated review remain subsequent steps; web labels are not local-video
times. No source media was modified, no media is published and no Phase 3.2A work is included.

## Episode 6 subtitle and website context — 2026-10-30

The [preparation record](../episode-06-context-preparation.md) pins the local media/subtitle
identity and records a full read of all 365 ordered English ASS events. Landing roles and strut
warnings, Fred's equipment bargain, Suzuka's wooden sword, shields and conditional challenge
are indexed by local subtitle intervals. West Virginia and Locus spaceport labels remain
unreconciled; subtitle times are not assigned to the unaligned gallery labels.

Three selected Fandom captures and cached AnimeHistory episode/character prose supply eight
new secondary assertions, four catalogue subjects and 34 typed links, including background reuse.
The standalone Light shield lookup was NOT_FOUND. Novel/manga backstory, later episodes,
infobox statistics and universal mechanism claims are excluded. No image association or
primary-status promotion is added.

Context/cache validation and preservation checks passed. The five-tab ImportExcel context view
refreshed and passed saved-data/link and affected visual checks. All 354 Episode 6 image rows
remain UNREVIEWED / NOT_REVIEWED at this preparation checkpoint. The maintainer accepted
the preparation on 2026-10-30; subsequent alignment is recorded below. No Phase 3.2A work is included.

## Episode 6 bounded alignment — 2026-10-30

The [alignment record](../episode-06-alignment-review.md) documents 14 declared attempts:
seven reviewed matches and seven ambiguous holds/repeated or unclear drawings. Four FIT
matches froze ALNMAP-000011 before independent HOLDOUT searches; three HOLDOUT matches
validated identical coefficients in ALNMAP-000012. Navigation is `local = web - 1.5185 s`
for web labels 01:47–21:18 inclusive: ordinals 002–324, seven direct intervals and 316
estimates. Ordinal 001 and final 325–354 remain unmapped; late ambiguous checks do not
extend coverage. No entire-runtime or exact subtitle association is implied.

Current-input and early/late hash reproduction checks passed. The category workbook refreshed
with direct intervals, estimates and unmapped boundaries kept separate; saved-data/link and
visual checks passed. All five temporary search runs were removed through the inspected
cleanup preview, releasing 769,808,022 bytes. Gallery originals, all 15 contact sheets,
context records/workbook and earlier alignment rows remain unchanged. All 354 Episode 6
annotation rows remain UNREVIEWED / NOT_REVIEWED at acceptance on 2026-10-30;
the first three-sheet review is the next separate step. No Phase 3.2A work is included.

## Episode 6 annotated survey — batch 01, 2026-10-30

Status: initial survey implemented, verified and accepted by the maintainer on 2026-10-30. Images
001–072 (IDs 848543–848614), sheets 0001–0024, 0025–0048 and 0049–0072, are annotated.
Thirty originals were additionally inspected full-size: 001, 008–010, 012, 019, 026, 029,
032–035, 037, 041–044, 046, 048–049, 053, 055, 061, 063, 065, 067–068 and 070–072.
The three sheets were inspected in full; sampled imagery is not continuous-video coverage.

The accepted [context preparation](../episode-06-context-preparation.md) and
[alignment review](../episode-06-alignment-review.md) supply navigation and source limits.
Local English ASS cues 34–105 were reread, including the surrounding named Fred greeting.
Within this batch, 002, 030 and 036 have direct intervals; 68 rows have mapping estimates
and 001 is unmapped. Estimates remain navigation aids. No new alignment run or website
retrieval was needed. The cached Fred/Suzuka context remains secondary, with no primary promotion.

Images 001–015 are opening material. Suzuka's cup/veranda illustration, Gene's jump, XGP
exterior, caster still life, MacDougall portraits, seated trio, mechanical pirate foot soldier,
El Dorado/XGP vignette and cast lineup retain that presentation. Image 005 is the recurring
unidentified launch craft/facility and remains NEEDS_RECHECK. Cropped montage figures in 009
and the tentative Aisha eye in 010 retain their identity limits. No cast-lineup membership,
literal montage spatial arrangement or present-day combat is inferred.

Images 016–051 establish the Sentinel approach and landing. High-priority references include:

- 019, 029–030, 032 and 035–036: underside silhouette, gold stepped nozzle, dark rear
  structure, side housings, exhaust and pad approach. Red atmospheric/cockpit illumination
  is a visible state, without a thermal, alarm or damage algorithm.
- 020, 026–028, 033–034 and 037–040: paired controls, Gilliam's segmented circular interface,
  Jim forward/lower than Gene, Melfina's occupied slatted apparatus behind them and a hand
  lifted near the pilot's circular side control. Dialogue assigns Melfina beacon alignment
  and calls for strut deployment; still endpoints do not establish complete control/motion logic.
- 041–043: pale cup-shaped landing foot, central gold tapered component, rods/split supports,
  nose band/oval apertures and the nearly vertical ship over a circular yellow-marked pad.
  The sampled apparatus state does not prove the full deployment path, a broken strut,
  exact load paths or correspondence to the reported strut three.
- 044–051: brighter post-landing cockpit, two forward/pilot seat levels, flared side stations,
  looping cables, floor fittings, Gilliam overhead and cyan-lit Melfina apparatus. Empty side
  seating/display structures remain distinct from the occupied forward and pilot stations.
  These views do not measure room dimensions or prove shutdown/retraction behavior.

ASS cues 34–61 (156.87–245.88 s) cover approach, fuel/speed concerns, beacon help, engine
cut request and strut-three yellow warning. Cues 62–69 (257.47–285.96 s) welcome the ship
to West Virginia Spaceport on Sentinel III and discuss cheap docking/Blue Heaven registration.
This port identification is dialogue/scene continuity; it does not resolve the later Locus
spaceport wording or identify the unnamed binocular-using port observer in 021–022.

Image 052 is the episode title card, with Japanese wording left untranscribed. Images 053–060
show the port frontage, E-7 arrow sign, canopy/tube lights, steps, traffic signals, sculpture
and crew's travel discussion. The sculpture is not tagged as a ship. Melfina's outfit and the
three standing figures provide useful costume/pose references without calibrated height claims.

Images 061–065 introduce a pale-green enclosed rental car, distinct from the earlier red
Starwind/Hawking car. Visible features include round lamps, fan-like grille, curved glazing,
roof loop/fin, steering wheel, front seats, Melfina's diagonal belt and Jim in the rear.
The visible underside gap/shadow and grille do not establish its lift/propulsion mechanism.
Gene drives; Jim's hand near Gene's head is associated through rear-seat continuity. Images
066–067 retain road/gantry/rocky-outskirts references without a measured route to Hugo.
Translated cues 70–81 (299.25–336.08 s) provide the rental plan, Hugo destination, original
car in the silo and roughly three-hour estimate; no vehicle make/model or speed is derived.

Images 068–072 move into Fred's weapons showroom/office. The gold-trimmed display case contains
an unidentified large cylindrical weapon with a pink pointed end, not an established caster,
engine or verified XGP purchase. Blade racks, hanging weapon panels, cabinets, doors and
articulated desk lamps are retained for later environment work. Fred's red headband/dark bangs,
named greeting in cues 82–88 (344.86–366.07 s) and CTX-000077 support the preliminary survey
identity in 070–072. This premises is not a ship interior or the stated Heifong headquarters.

The vocabulary adds fred_luo from the existing context catalogue, sentinel_rental_car and
fred_luo_premises as scoped descriptive survey identities. Thirty contextual image links
(CTXLINK-001076–001105) reuse CTX-000008, 000009, 000065, 000076–000078. These do not establish
exact subtitle timing or change evidence status. No new source, assertion or manual supplement
is added. All 72 rows have INITIAL_REVIEW_COMPLETE depth: 71 SCREENED, one NEEDS_RECHECK;
32 chronological scene groups and 35 high-priority rows. The remaining 282 Episode 6 rows
are untouched and unreviewed.

Category/context validation passed. All 9,132 out-of-batch annotation rows, prior context
links and 381 protected input hashes are unchanged, including gallery originals/sheets,
alignment registers, subtitle provenance/copy and existing context subjects/sources/claims.
The refreshed ImportExcel category view retains 30 tabs, 432,588 verified gallery cells,
9,204 image links, 1,326 manual cells and 4,419 alignment cells. The context view retains
five tabs with 12,695 verified cells and 2,390 links; 666 distinct images have context links.
Both builders confirm authored-data equality. Changed recheck, landing-gear, cockpit,
showroom, new-link and overview ranges were rendered and visually inspected. No fresh
native Office Viewer check is claimed. Disposable batch/preview helpers are removed after
verification. Next separate batch: 073–144. No Phase 3.2A work is included.

## Episode 6 annotated survey — batch 02, 2026-10-30

Status: initial survey implemented, verified and accepted by the maintainer on 2026-10-30. Images
073–144 (IDs 848615–848686), sheets 0073–0096, 0097–0120 and 0121–0144, are annotated.
All three sheets were inspected. Thirty-two originals were additionally inspected full-size:
074–075, 078, 084, 086, 089–091, 093, 098, 100, 114, 116, 119, 123–126, 129–140 and
143–144. These sampled views are not continuous-video coverage.

The accepted [context preparation](../episode-06-context-preparation.md) and
[alignment review](../episode-06-alignment-review.md) remain the timing/source basis.
All 72 rows use ALNMAP-000012 navigation estimates (`local = web - 1.5185 s`), without a
direct matched frame in this batch. Local English ASS cues 88–169 were reread for the
greeting, business negotiation, false referral and threat; cues 195–211 were reread only
to check the later wooden-sword explanation. Cached Suzuka SECTION:0005/0014 and Fred Luo
SECTION:0001/0007 were reused offline. No website retrieval or new alignment run was needed.

Images 073–088 continue Fred's greeting and establish the seated office conversation.
Jim's uneasy reactions, Melfina's cape/tie, Fred's pale coat and gray shoulder panels,
Gene's yellow cape, facing seating, low table, ceiling lights and guards beside the paneled
door provide character, costume and environment references. Translated cues 99–105
(396.21–418.92 s) distinguish the present Sentinel visit from the company's Heifong
headquarters and mention frontier expansion. They do not locate this room on Heifong.

Images 089–097 show Fred leaning close, Gene pointing a twin-muzzle gray-purple pistol,
and their return to the equipment discussion. The gun in 090–091 is visibly unlike the
gold caster; its exact model and correspondence to the earlier modular blaster are not
established. No firing occurs in these sampled stills. Cues 107–123 (421.90–470.21 s)
identify Gene's request for ship equipment and the grappler-ship complication. They are
not a verified loadout inventory, installation record or generic price specification.

Images 098–118 retain unusually useful office references: mounted swords, knives and
axes, gold-bordered hanging panels, gray columns, suspended and track lights, dark seating,
curved desk and lamp. Repeated conversational portraits retain their individual locators.
The negotiation in cues 123–141 (467.81–528.83 s) concerns costly grappler equipment,
non-legitimate supply routes, payment assurance and preparing an estimate. Fred's low bend
in 116 is a cropped pose; it does not identify hidden storage or a floor hatch.

Images 119–128 move Gene, Jim and Melfina into the adjacent blue-floored gun-display area.
The open doorway in 119 and reverse view in 123 establish a local connection to Fred's
office; 124 records the closed-door endpoint. Glazed handgun cabinets, the framed dragon
picture, an angular counter/workstation and its green overhead frame are useful later
environment references, without a complete building plan. The suited guard remains unnamed.
The red-hooded visitor in 126 is associated with Suzuka through the subsequent reveal.
The placard visibly reads `New Tipe`; this lettering is preserved rather than corrected
or used to assign a firearm model. The cloak's paired gold diamonds are visible motifs,
without a verified faction meaning.

Images 129–136 show the office's blade displays, hooded arrival, Fred's decorated envelope,
guards drawing guns, cloak movement and Suzuka standing with a long dark sword as the guards
fall/slump around her. Their death or exact injuries are not established. The sampled endpoints
do not reproduce the full attack trajectory. The sword's wooden-bokken identification uses
CTX-000079 and the later translated explanation, not a material inference from dark shading.
The subjects vocabulary adds the existing context-catalogue identity `suzuka_bokken`; no new
context subject or assertion is created. The costume/grip view in 136 is a high-priority reference.

Images 137–144 retain Suzuka's ponytail, headband, layered collars, red sash/wrist guards,
orange-purple shoulder wrap, tassels and profile, plus Fred's worried response. A small hinged
gold watch-like item in 139–140 accompanies the time-limit exchange; its type, dial reading and
mechanism remain unverified. The overlapping profiles in 144 are a transition composition,
not a literal spatial measurement or magic effect. Cues 152–169 (566.15–647.82 s) provide
the false referral, five-minute threat, market-rival explanation and later Twilight Suzuka name.
The ASS spelling `Mr. Oh` and secondary `Mr. O` remain unreconciled. Fred's suggested rivals
do not establish the employer's identity. No later crew membership is inferred.

Thirty-nine image associations (CTXLINK-001106–001144) reuse CTX-000076–000079 and 000081.
They remain contextual links, without exact subtitle matches or primary-status promotion.
All 72 rows are SCREENED / INITIAL_REVIEW_COMPLETE, with 12 new chronological groups
(EP-06-S033–S044) and 29 high-priority references. There are no new NEEDS_RECHECK rows;
weapon models, guard outcomes, timepiece details and referral spelling remain explicit limits.
Combined Episode 6 coverage is 144 initial reviews: 143 SCREENED and the prior opening craft
at 005 NEEDS_RECHECK. The remaining 210 Episode 6 rows are untouched.

Category/context validation and preservation checks passed: 9,132 out-of-batch annotation
rows, all prior 1,105 context links and 383 protected input hashes remain unchanged.
The refreshed ImportExcel category view retains 30 tabs, 432,588 verified gallery cells,
9,204 image links, 1,326 manual cells and 4,419 alignment cells. The context view retains
five tabs, 13,046 verified cells and 2,468 links, covering 697 distinct linked images.
Authored-data equality and changed showroom, entrance, new-link and overview visual checks
passed. No fresh native Office Viewer check is claimed. Disposable batch helpers/previews
are removed after verification. Next separate batch: 145–216. No Phase 3.2A work is included.

## Episode 6 annotated survey — batch 03, 2026-10-30

Status: initial survey implemented, verified and accepted by the maintainer on 2026-10-30. Images
145–216 (IDs 848687–848758), sheets 0145–0168, 0169–0192 and 0193–0216, are annotated.
All three sheets were inspected. Forty originals were additionally inspected full-size:
153, 155–156, 158, 160–161, 163, 165–170, 172–173, 175–183, 186, 188, 190, 192–194,
197, 199–201, 203, 205–208 and 210. Sampled stills do not establish continuous attack trajectories.

The accepted [context preparation](../episode-06-context-preparation.md) and
[alignment review](../episode-06-alignment-review.md) remain authoritative for source identity
and timing limits. Local English ASS cues 164–238 were reread, including surrounding dialogue
beyond the batch boundary. Image 180 has direct correspondence ALNANC-000100 at local
752.752 s; the other 71 rows use ALNMAP-000012 estimates. Image 165's shield pose and 192's
held city panorama remain ambiguous anchor attempts, without losing their bounded estimates.
No new alignment run, media extraction or website retrieval was needed. Existing selected
Suzuka context and CTX-000074/000076–000080 were reused without primary-status promotion.

Images 145–159 continue Suzuka's time limit and Gene's intervention. The overhead office
view in 153 records the facing sofas, low table, circular carpet border, separate rounded
desk, columns, wall displays, discarded cloak and prone guards. Gene's crouch behind the
sofa in 155–156 is useful cover/pose evidence, without a ballistic-material specification.
Fred ducks behind the desk. Close views retain individual expressions, hair and clothing.
The small gold object later seen in 177 has a crown/loop consistent with a timepiece,
but no readable dial establishes its displayed time or exact type.

Images 160–169 provide Gene's twin-muzzle pistol, trigger/finger close-up and the bright
white-blue oval field meeting Suzuka's wooden sword. Cues 171 and 175 (662.78–664.00 s
and 698.58–700.98 s) explicitly name light shields. The wider view at 165 associates the
field with Gene; the close field overlapping Suzuka in 166–167 is not reassigned to her.
The subjects vocabulary adds the existing context identity `light_shield`. Visible arcs,
transparency, hair highlights and recoil are effects/poses, without verified field capacity,
electrical/magic physics, activation mechanism, impulse or shield-failure specification.
The pistol's exact model remains unassigned, distinct from the gold caster.

Images 170–179 show Gene without his coat, a displayed broad silver sword, fighting poses,
a different slim dark pistol and pale falling fragments. Image 170 retains white back straps
and the red upper-arm star; 172 is a useful full-body outfit, belts, holster and boot reference
with the yellow coat on the floor. No complete blade-breaking sequence, firearm model,
caliber or ammunition type is established. The trigger view at 163 and aiming pose at 178
do not themselves show a muzzle flash or completed shot trajectory.

Images 180–191 show debris and the protection/equipment bargain. The direct frame at 180
captures tumbling fragments/chair before the dragon artwork; 182 retains Fred behind the
rubble-covered desk and bent lamps. Cues 181–194 (754.70–792.90 s) supply Suzuka's next-sunset
reprieve, Fred's request for continued protection, Gene's equipment condition and added
missiles. The blue handheld item's rear housing is visible in 186, and Gene manipulates it
in 190. Dialogue/continuity associates it with the list, without a readable screen, itemized
bill, exact device class, printing mechanism or missile count. No installation is verified.
Fred's assassin-ranking/survival statement remains attributed dialogue, not a verified
exhaustive kill record or numeric capability specification.

Images 192–195 show Suzuka above the city and her bodyguard remark in cue 195
(805.49–807.75 s). Rooflines, towers, lights, two celestial discs and distant beams are
useful environment references without exact district, astronomical identities, calibrated
scale or a continuous roof-to-office route. Images 196–198 are EYECATCH graphics, including
the partial lettering transition and completed yin-yang/logo composition; they are not
in-world displays or story locations.

Images 199–206 return to the premises' weapon-sensor check and visible office damage.
The screen in 199 visibly reads MODE THERMOGRAPHY and contains a colored armed silhouette,
color bar, seven-bar chart and trace graph. Association with Gene is tentative from pose,
coat outline and scene continuity. No temperatures, thresholds, sensor algorithm or live-feed
specification are derived. Image 200 records a red translucent cylindrical housing on a
ringed column; 201 places the fixture/frame, counter, cabinets, doorway and standing figures.
The still does not prove alarm activation, rotation or the fixture's exact sensing function.
Cues 196–202 (827.81–852.53 s) explain the failure to detect Suzuka's wooden sword at this
premises. This is not universal immunity to weapon sensors. The matching green- and
purple-glasses guards are standing again in 202, 204 and 206, clarifying the earlier down
poses without assigning names or injuries. Image 205 preserves the damaged ceiling,
doorway edges, furniture and rubble, without calculating damage energy or cutting physics.

Images 203 and 207–216 retain Gene handling unidentified shop guns, the back of his restored
yellow coat, display supports/labels and the group discussing the next deadline. The
caster-shell request and no-demand/antique response in cues 203–205 (857.04–864.57 s)
are dialogue context; the displayed gun in Gene's hand is not identified as a caster and
no caster shell is visible. Later conversation does not establish a new purchase or loadout.

Thirty-eight image associations (CTXLINK-001145–001182) reuse CTX-000074 and 000076–000080.
No source, assertion, context-catalogue subject or manual supplement is added. All 72 rows
are SCREENED / INITIAL_REVIEW_COMPLETE, with 17 new groups (EP-06-S045–S061) and 37
high-priority references. No new NEEDS_RECHECK row is introduced. Combined Episode 6 coverage
is 216 initial reviews: 215 SCREENED and the earlier opening craft at 005 NEEDS_RECHECK.
The remaining 138 Episode 6 rows are untouched.

Category/context validation and preservation checks passed: all 9,132 out-of-batch rows,
prior 1,144 context links and 383 protected hashes are unchanged, preserving batch 02's
uncommitted work. Refreshed ImportExcel views retain 30 category tabs with 432,588 verified
gallery cells, 9,204 image links, 1,326 manual cells and 4,419 alignment cells; the five-tab
context view has 13,388 verified cells and 2,544 links, covering 732 distinct linked images.
Authored-data equality and affected shield, security, direct-timing, new-link and overview
visual checks passed. No fresh native Office Viewer check is claimed. Disposable batch
helpers/previews are removed after verification. Next separate batch: 217–288. No Phase 3.2A
work is included.

## Episode 6 annotated survey — batch 04, 2026-10-30

Status: initial survey implemented, verified and accepted by the maintainer on 2026-10-30. Images
217–288 (IDs 848759–848830), sheets 0217–0240, 0241–0264 and 0265–0288, are annotated.
All three sheets were inspected, with 34 full-size original checks: 227, 234, 237,
241–248, 254, 256, 260–263, 267, 272–275 and 277–288. The accepted
[context preparation](../episode-06-context-preparation.md) and
[alignment review](../episode-06-alignment-review.md) retain source and timing authority.
Local English ASS cues 213–300 were reread, including neighboring dialogue outside the batch.
Image 277 retains direct frame ALNANC-000095 at 1105.521 s; 280 retains direct interval
ALNANC-000102 at 1116.324–1116.407 s. The other 70 rows use ALNMAP-000012 navigation
estimates, not exact subtitle associations. No new search, media extraction or website
retrieval was needed. Cached Suzuka SECTION:0005 was reread; later events remain separate.

Images 217–226 continue the shop conversation. Fred proposes finding Suzuka's employer;
Gene wants a hotel, declines Fred's offer to stay together and leaves with a promise to
call. Cues 214–227 (885.43–919.83 s) provide that translated context. Portraits, gestures,
the facing group and display-room doorway retain individual descriptions. The suggested
employer search does not establish an employer identity or an action completed offscreen.

Images 227–240 establish Fred's arched storefront, the parked rounded pale-green rental
car, neighboring lit entrances and the renewed street challenge. The full-length Suzuka
view at 234 records her white robe, red sash, orange-purple wrap and dark wooden sword
among signs, overhead cables and street covers. The lettering is not comprehensively
transcribed or used to invent a district map. Cues 228–243 (923.44–969.64 s) explain the
ship-supplies motivation, mutual introductions, renewed duel, Gene directing Melfina back
to Fred and asking Jim for backup. Gene's defensive crouch beside the car at 237 is a
pose reference without a reconstructed incoming attack path.

Images 241–248 follow the alley chase and traffic encounter. Gene carries the slim dark
pistol, distinct from the gold caster; cue 244 (978.36–980.62 s) calls it useless without
identifying its precise failure. Boots/puddle splashes, wall vents, pipes, refuse and
the narrow alley's opening onto the lit main road are useful environment references.
The passing pale-blue car at 244 is distinct from the rental car. Images 245–248 show
a tilting/scraping truck, Suzuka facing its front with her wooden sword, an overhead
sword pose and exposed box cargo/underbody with sparks beside another car. The sampled
stills do not show every strike or establish exact vehicle division geometry, mass,
speed, stopping force or cutting physics. Suzuka calls the feat strength in cue 247
(1008.49–1010.29 s); this is attributed dialogue, not a measured capability or separate
spell specification. Drivers and bystanders remain unnamed.

Images 249–258 retain the post-encounter exchange, Jim arriving at the rental car's
controls, Suzuka's pursuit in its rectangular mirror and Gene speaking inside the car.
Cues 245–256 (1005.05–1038.48 s) supply the taunt, pickup, pursuit and Gene asking Jim to
do something while traveling. The requested preparation is not visually established
by these stills. Mirror perspective and vehicle fittings do not identify propulsion,
pursuit speed or distance. The car seating is recorded for this scene without assuming
a universal arrangement.

Images 259–271 move to the outskirts: stars, two small crescents, a distant illuminated
city strip, a field of eroded-looking rock spires, Jim watching behind a rock, Suzuka
balanced on a spire and Gene challenging her below. Image 263 provides an especially
useful costume silhouette against the huge cratered celestial disc. No geological
composition, astronomical identities, calibrated scale, travel distance, jump capability
or levitation is derived. Cues 257–265 (1052.33–1080.89 s) provide their motivation and
challenge. Gene's raised gloves at 267 are a preparatory pose, without a verified
electronic activation gesture. Image 271 records Suzuka raising her wooden sword.

Images 272–279 show Gene, now without his yellow coat, meeting Suzuka's sword with a
small bright blue-white field near his gloves. Cues 266–269 (1092.57–1103.58 s) name the
shield and explain focusing shields at a single point. This supports the concentrated
shield interpretation rather than a shield belonging to Suzuka. Close views preserve
two braced gloves, sword contact, thin arcs and irregular dark glove patches; the direct
wide frame at 277 preserves their stance and radiating streaks. These are valuable
effect references without emitter count, energy units, electrical/magic physics or
precise capacity. Dark patches and secondary power-exhaustion prose do not independently
verify burning, destroyed hardware, a battery model or the exact failure instant.

Images 280–282 show the disarming exchange, an upright dark sword shape in the foreground
and an overhead chase. The direct interval at 280 fixes a pose, not the complete grip,
kick or sword-transfer path. Images 283–286 preserve Suzuka's red bow, the sash extending
sideways and her gathering the loosened robe closed. Image 284 crops out the pulling
hand, so continuity supplies the removal interpretation without reproducing every motion.
Images 287–288 clearly show Gene holding the wooden sword and long red sash as separate
objects. Cues 272–275 (1141.45–1146.26 s) identify the demand for both. Later bargaining,
symbolic death and target-priority agreement belong to the next batch; no fatal outcome
or crew membership is inferred here.

Forty-three contextual image links (CTXLINK-001183–001225) reuse CTX-000077–000080.
No source, assertion, subject vocabulary or manual supplement is added, and no assertion
is promoted to primary status. All 72 rows are SCREENED / INITIAL_REVIEW_COMPLETE, with
15 chronological groups (EP-06-S062–S076) and 35 high-priority references. No new
NEEDS_RECHECK row is introduced. Combined Episode 6 coverage is 288 initial reviews:
287 SCREENED and the prior opening craft at 005 NEEDS_RECHECK. The final 66 rows remain
untouched. No Phase 3.2A work is included.

Validation preserves all 9,132 out-of-batch annotation rows, all prior 1,182 context
links and 379 protected input hashes, including every Episode 6 gallery original,
contact sheet, subtitle copy and protected timing/context record. The refreshed category
view retains 30 tabs, 432,588 gallery cells, 9,204 image links, 1,326 manual cells and
4,419 alignment cells. The context view retains five tabs with 13,775 verified cells
and 2,630 links, covering 768 distinct linked images. Authored-data equality and affected
shield, direct-timing and overview visual checks passed. Cached-source verification passed
for all 30 snapshots. Disposable batch helpers/previews were removed after verification.
No fresh native Office Viewer check is claimed. Next separate batch: 289–354.

## Episode 6 annotated survey — batch 05, 2026-10-30

Status: initial survey implemented, verified and accepted by the maintainer on 2026-10-30. Images
289–354 (IDs 848831–848896), sheets 0289–0312, 0313–0336 and 0337–0354, are annotated.
All three sheets were inspected, including the final sheet's 18 images. Thirty-two originals
were inspected full-size: 289, 291, 295, 297, 302, 304, 306, 310–314, 316, 320, 322, 324,
327–328, 330–332, 335–336, 340–341, 343, 346–348, 351–352 and 354. Existing batch 04
annotations and links are preserved. No new extraction, alignment search or website fetch
was required. The accepted [context preparation](../episode-06-context-preparation.md) and
[alignment review](../episode-06-alignment-review.md) remain authoritative.

Local English ASS cues 272–365 were reread to distinguish the duel, negotiation and closing
story from ending lyrics and the Episode 7 preview. Image 324 retains direct correspondence
ALNANC-000096 at local 1276.442 s. Images 289–323 have 35 ALNMAP-000012 navigation estimates;
325–354 remain UNMAPPED. Those final 30 annotations use visible content and scene order for
dialogue context without extrapolating the offset or claiming exact subtitle matches.
Earlier ambiguous attempts at held-car image 350 and closing-tableau image 354 remain
ambiguous; completing their visual review does not upgrade timing evidence.

Images 289–296 continue the captured-sash exchange. Gene holds the red cloth near his nose,
then bargains with seated Suzuka over the sash and wooden sword. The scent remark is
translated dialogue rather than a property established visually. Low views between Gene's
legs and reverse views record their positions and Suzuka gathering her loosened robe.
Image 295 separately shows the slim pistol, wooden sword and red sash. No sword breaking,
completed firing cycle or measured separation is established.

Images 297–305 retain Gene's slim dark pistol, long side ridge, top sights, small red
circular detail and broad muzzle rim, plus individual portraits. The weapon is distinct
from the gold caster; the red detail's function, model, ammunition and caliber remain
unassigned. Suzuka's chest wrap, loosened robe and low shoulder cloth are costume references
without a complete dressing/construction sequence. Cues 287–299 (1178.02–1215.39 s) propose
a draw and distinguish Gene's personal duel from protecting Fred indefinitely. They do not
prove superior lethal ability or a permanent bodyguard commitment.

Images 306–313 retain Gene extending the pistol, Suzuka remaining seated and a wider view
of their separation. Cues 300–305 (1217.26–1235.90 s) discuss contract, pride and Gene's
symbolic declaration that Twilight Suzuka has died. No muzzle flash or bullet path is
visible in the selected pistol still at 310. The cached Suzuka SECTION:0005 describes shots
at the ground, but sampled images do not independently reconstruct every shot. Suzuka is
visibly alive afterward; the language is not an actual death, resurrection or fatal injury.
Image 310 is useful for Gene's white back straps, wrist guard, belt and thigh holster.

Images 314–321 show the sword/sash on the ground, Gene turning away, Suzuka objecting and
Gene giving a thumbs-up. Cues 306–318 (1236.22–1270.18 s) offer the items as payment for
Fred's life, then resolve the pride objection by making Gene the target before Fred.
This is the particular negotiated agreement, not a universal assassination-contract rule,
an unconditional abandonment of the contract or formal crew membership. Images 322–324
retain Gene's coat spread on the ground, a cropped pickup transition and his departure with
the coat over his shoulder beside Jim. Jim's green satchel, cargo trousers and outfit are
useful references. Images 325–329 continue their departure and Suzuka's response, with
rock spires and celestial-disc compositions retained without scale or astronomical claims.

Images 330–336 return to Fred's showroom. Image 330 preserves the large segmented weapon
with pink pointed tip on a three-legged stand inside a lit gold-framed cabinet. It resembles
the earlier display in 068; model, ammunition, installation and purchase of this particular
item remain unverified. Image 331 locates the green counter frame, cabinets, damaged office
doorway and two guards. Image 332 shows the blue handheld item's rear label and fittings,
without readable account details, verified device class or printing mechanism. The handshake
in 335–336 concludes the exchange visually without an itemized contract or shipment receipt.

Cues 325–343 (1297.41–1355.33 s) arrange delivery to dock 26 at Locus' spaceport, discuss
the remaining employer problem, refer to a 750,000-wong difference and a 30% discount, and
comment on maintaining a grappler ship. Preserve the dialogue's subtraction wording rather
than inventing an itemized ledger, debt direction, standard hiring fee or general maintenance
tariff. Earlier West Virginia Spaceport wording remains unreconciled with Locus. Arranged
delivery is distinct from equipment visibly delivered or installed.

Images 337–345 retain Fred's embraces, Gene's frustration, two matching unnamed guards and
the discount explanation. Image 340 frames Gene and Fred through the guards' silhouettes
below the green crossbar and pink dome light. The light does not establish alarm activation
or a new security state. Image 341 is a useful paired outfit/eyewear reference, without
names, injury diagnoses or inferred visor functions. The recurring embrace compositions
remain distinct individual locators rather than being discarded as duplicates.

Images 346–351 return to the rental car outside Fred's storefront. The frontal views show
the initially empty driver seat, Gene entering and then holding the steering wheel on the
viewer's left, Jim front-right and Melfina behind. Mirror, seats, dashboard fitting, roof
and glazing are useful interior references, without measured dimensions, propulsion or a
general seating rule. Melfina's rear-seat portrait preserves her white collar, purple tie
and dark vest. Images 352–354 are the closing story tableau: Suzuka has restored her robe
and carries the wooden sword over her shoulder against the large pale disc. Scene continuity
and cue 349 (1380.79–1386.03 s) preserve the continuing challenge; these are not ending-credit
images, an exact subtitle match or an Episode 6 crew-joining event.

Fifty-three image links (CTXLINK-001226–001278) reuse CTX-000075–000078. No source, assertion,
subject vocabulary or manual supplement is added; no primary-status promotion is made.
All 66 new rows are SCREENED / INITIAL_REVIEW_COMPLETE, in 13 groups (EP-06-S077–S089),
with 27 high-priority references and no new NEEDS_RECHECK rows. Episode 6 now has initial
survey coverage for all 354 images: 353 SCREENED and 005 NEEDS_RECHECK for the recurring
unknown opening craft. All 354 are INITIAL_REVIEW_COMPLETE; targeted mechanism review is
not implied. Archive verification and pruning are a separate pending closeout step.

Validation passed with all 9,138 out-of-batch annotation rows, all prior 1,225 context links
and 379 protected input hashes unchanged, preserving batch 04's uncommitted work. All 30
cached snapshots verified. The category workbook retains 30 tabs, 432,588 verified gallery
cells, 9,204 image links, 1,326 manual cells and 4,419 alignment cells. The context workbook
retains five tabs, 14,252 verified cells and 2,736 links, covering 809 distinct linked images.
Authored-data equality and affected display-weapon, car-interior, mapping-boundary and
overview visual checks passed. No fresh native Office Viewer check is claimed. Disposable
batch helpers/previews were removed after verification; gallery originals and contact sheets
remain available for the separate episode closeout. No Phase 3.2A work is included.

## Episode 6 retention checkpoint — 2026-10-30

Status: cleanup authorized, implemented, verified and accepted by the maintainer on 2026-10-30.
All 354 gallery images retain INITIAL_REVIEW_COMPLETE: 353 SCREENED and the recurring
unknown opening craft at 005 NEEDS_RECHECK. There are no registered Episode 6 manual
supplements. This closeout preserves the recheck and all mechanism, identity and timing limits.

Before pruning, `models.py validate --current --episode 6` with the installed FFprobe passed
VERIFIED_CURRENT_EP06. The alignment finish preview found no runs and zero removable bytes,
confirming that the earlier five-run cleanup remains intact. No new search/reproduction
frames were created. The fresh no-run preview digest is
`0282b42c74d8bbf933d6dcf0a243c0255dcc63519b0c82f917531353a65c0f8f`.

The first complete format-2 archive was created with `episode_gallery.py archive --episode 6
--compression 3`, using WinRAR 7.13 x64, non-solid compression. It contains all 354 gallery
JPGs, their manifest and an empty supplemental recovery snapshot. Native RAR integrity,
staged restoration, decoding, exact inventory and hash comparisons passed before promotion.
Creation and round-trip verification took 85.860 seconds.

| Retained artifact / size | Result |
| --- | --- |
| `reference/cache/animehistory-review/archives/EP-06.rar` | 62,187,300 bytes |
| Archive SHA-256 | `7fcb881253f8fd7d460455d71b5f62473d267c090cf832102fab5ab34590bbcc` |
| Packing inputs including recovery metadata | 62,623,125 bytes |
| Compression saving against packing inputs | 435,825 bytes, approximately 0.70% |
| Receipt | `reference/cache/animehistory-review/archives/EP-06.json`; complete, format 2, gallery 354, supplements 0 |
| Contact sheets retained | All 15 PNGs, 52,085,220 bytes, plus unchanged registry |

`episode_gallery.py prune --episode 6 --progress-saved` independently restored and checked
the archive again, compared its manifest and current supplemental recovery snapshot, then
removed the expanded gallery cache. Removed cache/manifest data totaled 62,623,017 bytes;
this is separate from net compression saving because the RAR remains. No manual PNGs needed
removal. Final status: cached 0, archived images 354, archived supplements 0, contact sheets
15, unpacked bytes 0 and archive hash valid. The Episode 6 cache directory is absent. No
packing, verification, prune-verification, restore or candidate-archive leftovers remain.

All 55 protected annotation/context/locator CSV, contact-sheet/registry, alignment-plan/review
and subtitle/provenance hashes match the pre-cleanup baseline. Source media remain immutable.
No review status, association, manual-image record or timing mapping changed. Cited website
captures and existing subtitle copies retain their separate retention rules. Unrelated working
files and application attachments were not swept.

Both ImportExcel views were refreshed after pruning. The category view retains 30 tabs,
432,588 verified gallery cells, 9,204 image links, 1,326 manual cells and 4,419 alignment cells.
The context view retains five tabs, 14,252 verified cells and 2,736 links. Authored-data equality
passed. Post-refresh timing-boundary and context-overview visual checks passed;
no fresh native Office Viewer acceptance test is claimed. Routine RECORDED_UNCHECKED timing
availability is distinct from the explicit pre-prune current-media verification above.

Later full-size work uses `episode_gallery.py restore --episode 6`, followed by normal verified
prune after use. Restore gallery inputs before a fresh current-media timing verification.
Episode 7 is next in the adopted sequence and is not started automatically. Phase 3.2A
remains unstarted.
