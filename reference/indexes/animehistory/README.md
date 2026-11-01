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
   filename and selected track against the existing [subtitle coverage/provenance index](../performance/performance-subtitle-coverage.json).
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
   [alignment review](../episodes/EP-02/alignment/episode-02-alignment-review.md) records the limits. Episode 3 now has
   separately validated navigation coverage for web labels 01:47–23:00 at offset -1.4845 s;
   its [alignment review](../episodes/EP-03/alignment/episode-03-alignment-review.md) retains the checks and unmapped edges.
   Episode 4 has independently validated navigation coverage for web labels 01:54–22:30 at
   offset -1.2415 s; its [alignment review](../episodes/EP-04/alignment/episode-04-alignment-review.md) retains nine direct
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

Historical episode observations: [Episode 4 record](../episodes/EP-04/survey/episode-04-survey-history.md).


Five category-validator tests cover initialization refusal, stable-ID resume despite reordered
rows, overlapping tags, key/value failures, distinct recheck/unavailable/detail states and scene
groups. The gallery regression suite includes authored-status integration without annotation
mutation. Rendered workbook previews support layout checks; native Excel/VS Code viewer behavior
for this new workbook remains an owner-run check, not established by data verification alone.
All progress stays in this CSV/documentation pair, without a Markdown file per batch. Phase 3.2A
remains unstarted. Subsequent screening progress is recorded below and in the authored CSV.

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


Historical episode observations: [Episode 4 record](../episodes/EP-04/evidence/episode-04-supplement-history.md).

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


## Episode review records

Episode-specific history now lives in the [episode directory](../episodes/README.md).
The retained schema and workflow sections above remain authoritative. Earlier statements about
keeping all progress in this README describe their dated checkpoints and are superseded by this layout.

### Historical link destinations

<a id="episode-1-preparation--2026-10-26"></a>
[Episode 1 preparation — 2026-10-26](../episodes/EP-01/preparation/episode-01-preparation-history.md#episode-1-preparation--2026-10-26)

<a id="episode-1-annotated-survey--sheets-13"></a>
[Episode 1 annotated survey — sheets 1–3](../episodes/EP-01/survey/episode-01-survey-history.md#episode-1-annotated-survey--sheets-13)

<a id="episode-1-subtitle-context-follow-up--2026-10-27"></a>
[Episode 1 subtitle-context follow-up — 2026-10-27](../episodes/EP-01/evidence/episode-01-subtitle-context-history.md#episode-1-subtitle-context-follow-up--2026-10-27)

<a id="episode-4-category-survey-progress"></a>
[Episode 4 category survey progress](../episodes/EP-04/survey/episode-04-survey-history.md#episode-4-category-survey-progress)

<a id="episode-1-annotated-survey--sheets-46-2026-10-27"></a>
[Episode 1 annotated survey — sheets 4–6 (2026-10-27)](../episodes/EP-01/survey/episode-01-survey-history.md#episode-1-annotated-survey--sheets-46-2026-10-27)

<a id="episode-1-annotated-survey--sheets-79-2026-10-27"></a>
[Episode 1 annotated survey — sheets 7–9 (2026-10-27)](../episodes/EP-01/survey/episode-01-survey-history.md#episode-1-annotated-survey--sheets-79-2026-10-27)

<a id="episode-1-annotated-survey--sheets-1012-2026-10-27"></a>
[Episode 1 annotated survey — sheets 10–12 (2026-10-27)](../episodes/EP-01/survey/episode-01-survey-history.md#episode-1-annotated-survey--sheets-1012-2026-10-27)

<a id="episode-1-annotated-survey--sheets-1315"></a>
[Episode 1 annotated survey — sheets 13–15](../episodes/EP-01/survey/episode-01-survey-history.md#episode-1-annotated-survey--sheets-1315)

<a id="episode-1-retention-checkpoint--2026-10-28"></a>
[Episode 1 retention checkpoint — 2026-10-28](../episodes/EP-01/survey/episode-01-retention-checkpoint.md#episode-1-retention-checkpoint--2026-10-28)

<a id="episode-2-preparation--2026-10-28"></a>
[Episode 2 preparation — 2026-10-28](../episodes/EP-02/preparation/episode-02-preparation-history.md#episode-2-preparation--2026-10-28)

<a id="episode-2-bounded-alignment--2026-10-28"></a>
[Episode 2 bounded alignment — 2026-10-28](../episodes/EP-02/alignment/episode-02-alignment-history.md#episode-2-bounded-alignment--2026-10-28)

<a id="episode-2-annotated-survey--batch-01-2026-10-28"></a>
[Episode 2 annotated survey — batch 01, 2026-10-28](../episodes/EP-02/survey/episode-02-survey-history.md#episode-2-annotated-survey--batch-01-2026-10-28)

<a id="episode-2-annotated-survey--batch-02-2026-10-28"></a>
[Episode 2 annotated survey — batch 02, 2026-10-28](../episodes/EP-02/survey/episode-02-survey-history.md#episode-2-annotated-survey--batch-02-2026-10-28)

<a id="episode-2-annotated-survey--batch-03-2026-10-28"></a>
[Episode 2 annotated survey — batch 03, 2026-10-28](../episodes/EP-02/survey/episode-02-survey-history.md#episode-2-annotated-survey--batch-03-2026-10-28)

<a id="episode-2-annotated-survey--batch-04-2026-10-28"></a>
[Episode 2 annotated survey — batch 04, 2026-10-28](../episodes/EP-02/survey/episode-02-survey-history.md#episode-2-annotated-survey--batch-04-2026-10-28)

<a id="episode-2-annotated-survey--batch-05-2026-10-28"></a>
[Episode 2 annotated survey — batch 05, 2026-10-28](../episodes/EP-02/survey/episode-02-survey-history.md#episode-2-annotated-survey--batch-05-2026-10-28)

<a id="episode-2-retention-checkpoint--2026-10-28"></a>
[Episode 2 retention checkpoint — 2026-10-28](../episodes/EP-02/survey/episode-02-retention-checkpoint.md#episode-2-retention-checkpoint--2026-10-28)

<a id="episode-3-gallery-preparation--2026-10-28"></a>
[Episode 3 gallery preparation — 2026-10-28](../episodes/EP-03/preparation/episode-03-preparation-history.md#episode-3-gallery-preparation--2026-10-28)

<a id="episode-3-subtitlecontext-preparation--2026-10-28"></a>
[Episode 3 subtitle/context preparation — 2026-10-28](../episodes/EP-03/preparation/episode-03-preparation-history.md#episode-3-subtitlecontext-preparation--2026-10-28)

<a id="episode-3-bounded-alignment--2026-10-28"></a>
[Episode 3 bounded alignment — 2026-10-28](../episodes/EP-03/alignment/episode-03-alignment-history.md#episode-3-bounded-alignment--2026-10-28)

<a id="episode-3-annotated-survey--batch-01-2026-10-29"></a>
[Episode 3 annotated survey — batch 01, 2026-10-29](../episodes/EP-03/survey/episode-03-survey-history.md#episode-3-annotated-survey--batch-01-2026-10-29)

<a id="episode-3-annotated-survey--batch-02-2026-10-29"></a>
[Episode 3 annotated survey — batch 02, 2026-10-29](../episodes/EP-03/survey/episode-03-survey-history.md#episode-3-annotated-survey--batch-02-2026-10-29)

<a id="episode-3-annotated-survey--batch-03-2026-10-29"></a>
[Episode 3 annotated survey — batch 03, 2026-10-29](../episodes/EP-03/survey/episode-03-survey-history.md#episode-3-annotated-survey--batch-03-2026-10-29)

<a id="episode-3-annotated-survey--batch-04-2026-10-29"></a>
[Episode 3 annotated survey — batch 04, 2026-10-29](../episodes/EP-03/survey/episode-03-survey-history.md#episode-3-annotated-survey--batch-04-2026-10-29)

<a id="episode-3-annotated-survey--batch-05-2026-10-29"></a>
[Episode 3 annotated survey — batch 05, 2026-10-29](../episodes/EP-03/survey/episode-03-survey-history.md#episode-3-annotated-survey--batch-05-2026-10-29)

<a id="episode-3-retention-checkpoint--2026-10-29"></a>
[Episode 3 retention checkpoint — 2026-10-29](../episodes/EP-03/survey/episode-03-retention-checkpoint.md#episode-3-retention-checkpoint--2026-10-29)

<a id="episode-4-retrospective-subtitlecontext-preparation--2026-10-29"></a>
[Episode 4 retrospective subtitle/context preparation — 2026-10-29](../episodes/EP-04/preparation/episode-04-preparation-history.md#episode-4-retrospective-subtitlecontext-preparation--2026-10-29)

<a id="episode-4-retrospective-reconciliation--2026-10-29"></a>
[Episode 4 retrospective reconciliation — 2026-10-29](../episodes/EP-04/evidence/episode-04-reconciliation-history.md#episode-4-retrospective-reconciliation--2026-10-29)

<a id="episode-5-gallery-and-subtitlecontext-preparation--2026-10-30"></a>
[Episode 5 gallery and subtitle/context preparation — 2026-10-30](../episodes/EP-05/preparation/episode-05-preparation-history.md#episode-5-gallery-and-subtitlecontext-preparation--2026-10-30)

<a id="episode-5-bounded-alignment--2026-10-30"></a>
[Episode 5 bounded alignment — 2026-10-30](../episodes/EP-05/alignment/episode-05-alignment-history.md#episode-5-bounded-alignment--2026-10-30)

<a id="episode-5-annotated-survey--batch-01-2026-10-30"></a>
[Episode 5 annotated survey — batch 01, 2026-10-30](../episodes/EP-05/survey/episode-05-survey-history.md#episode-5-annotated-survey--batch-01-2026-10-30)

<a id="cross-episode-mikey-identification--2026-10-30"></a>
[Cross-episode Mikey identification — 2026-10-30](../comparisons/mikey-identification.md#cross-episode-mikey-identification--2026-10-30)

<a id="episode-5-annotated-survey--batch-02-2026-10-30"></a>
[Episode 5 annotated survey — batch 02, 2026-10-30](../episodes/EP-05/survey/episode-05-survey-history.md#episode-5-annotated-survey--batch-02-2026-10-30)

<a id="episode-5-annotated-survey--batch-03-2026-10-30"></a>
[Episode 5 annotated survey — batch 03, 2026-10-30](../episodes/EP-05/survey/episode-05-survey-history.md#episode-5-annotated-survey--batch-03-2026-10-30)

<a id="episode-5-annotated-survey--batch-04-2026-10-30"></a>
[Episode 5 annotated survey — batch 04, 2026-10-30](../episodes/EP-05/survey/episode-05-survey-history.md#episode-5-annotated-survey--batch-04-2026-10-30)

<a id="episode-5-annotated-survey--batch-05-2026-10-30"></a>
[Episode 5 annotated survey — batch 05, 2026-10-30](../episodes/EP-05/survey/episode-05-survey-history.md#episode-5-annotated-survey--batch-05-2026-10-30)

<a id="episode-5-caster-supplements--2026-10-30"></a>
[Episode 5 caster supplements — 2026-10-30](../episodes/EP-05/evidence/episode-05-supplement-history.md#episode-5-caster-supplements--2026-10-30)

<a id="episode-5-retention-checkpoint--2026-10-30"></a>
[Episode 5 retention checkpoint — 2026-10-30](../episodes/EP-05/survey/episode-05-retention-checkpoint.md#episode-5-retention-checkpoint--2026-10-30)

<a id="episode-6-gallery-preparation--2026-10-30"></a>
[Episode 6 gallery preparation — 2026-10-30](../episodes/EP-06/preparation/episode-06-preparation-history.md#episode-6-gallery-preparation--2026-10-30)

<a id="episode-6-subtitle-and-website-context--2026-10-30"></a>
[Episode 6 subtitle and website context — 2026-10-30](../episodes/EP-06/preparation/episode-06-preparation-history.md#episode-6-subtitle-and-website-context--2026-10-30)

<a id="episode-6-bounded-alignment--2026-10-30"></a>
[Episode 6 bounded alignment — 2026-10-30](../episodes/EP-06/alignment/episode-06-alignment-history.md#episode-6-bounded-alignment--2026-10-30)

<a id="episode-6-annotated-survey--batch-01-2026-10-30"></a>
[Episode 6 annotated survey — batch 01, 2026-10-30](../episodes/EP-06/survey/episode-06-survey-history.md#episode-6-annotated-survey--batch-01-2026-10-30)

<a id="episode-6-annotated-survey--batch-02-2026-10-30"></a>
[Episode 6 annotated survey — batch 02, 2026-10-30](../episodes/EP-06/survey/episode-06-survey-history.md#episode-6-annotated-survey--batch-02-2026-10-30)

<a id="episode-6-annotated-survey--batch-03-2026-10-30"></a>
[Episode 6 annotated survey — batch 03, 2026-10-30](../episodes/EP-06/survey/episode-06-survey-history.md#episode-6-annotated-survey--batch-03-2026-10-30)

<a id="episode-6-annotated-survey--batch-04-2026-10-30"></a>
[Episode 6 annotated survey — batch 04, 2026-10-30](../episodes/EP-06/survey/episode-06-survey-history.md#episode-6-annotated-survey--batch-04-2026-10-30)

<a id="episode-6-annotated-survey--batch-05-2026-10-30"></a>
[Episode 6 annotated survey — batch 05, 2026-10-30](../episodes/EP-06/survey/episode-06-survey-history.md#episode-6-annotated-survey--batch-05-2026-10-30)

<a id="episode-6-retention-checkpoint--2026-10-30"></a>
[Episode 6 retention checkpoint — 2026-10-30](../episodes/EP-06/survey/episode-06-retention-checkpoint.md#episode-6-retention-checkpoint--2026-10-30)
