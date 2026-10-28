# Episode alignment tool

**Status — 2026-10-27:** proposal published as `10678c8`; Stages 1–2 and the cleanup amendment
were confirmed and published in checkpoint `2c31b99`. Stage 3's bounded Episode 1 validation was
confirmed and published as `2be404f`. Stages 4–5 and the episode-review integration procedure were
accepted by the maintainer on 2026-10-27 after workbook, cleanup and reproduction validation.
The two maintained alignment CSVs are initialized. No all-episode extraction or whole-runtime timing
claim is implied.

**Extension — 2026-10-28:** explicit episode selection plans now support Episodes 1–26 through
search, assessment registration, current-input verification, modeling, report projection,
reproduction and cleanup. The [extension results](#all-episode-extension--2026-10-28) distinguish
synthetic coverage from the bounded live Episode 2 tool check. This extension is implemented and
tested, and accepted by the maintainer on 2026-10-28; it does not establish Episode 2 timing alignment.

## Purpose and ownership

Relate sampled AnimeHistory gallery images to the indexed local episode release so subtitle
context and later targeted visual inspection can use traceable local times. Automate bounded
candidate-frame searches and comparison preparation while retaining visual review, uncertainty
and source identity. Avoid repeated manual VLC seeking and full-episode frame dumps.

This document owns the proposed tool, storage, stages and technical validation. The
[image-index README](../../reference/indexes/animehistory/README.md#ordered-episode-review-workflow)
owns the end-to-end episode-review sequence and existing annotation contracts. The
[implementation plan](../../docs/implementation/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research)
owns execution scope and acceptance. The [canon policy](../../docs/canon-policy.md) remains in force:
timing alignment does not establish character identity, mechanism behavior or canonical terminology.

## Initial evidence and limits

The maintainer supplied two Episode 1 VLC screenshots from the indexed CBM release. Comparison
with cached gallery images supports the following same-shot leads:

| Gallery locator / image ID | Web label | Supplied VLC label | Preliminary difference |
| --- | --- | --- | --- |
| 002 / 846774 — caster still life | 01:46 | 01:44 | Local appears about 2 s earlier |
| 004 / 846776 — Melfina opening close-up | 01:53 | 01:51 | Local appears about 2 s earlier |

The screenshots are deliberately approximate, not exact-frame captures. The caster credit overlay
differs; Melfina's hair/petals differ in animation position. Both clocks show whole seconds, and
both comparisons are within the opening. `local ≈ web − 2 s` is a search seed for that region,
not a validated Episode 1 mapping or a rule for other episodes. The existing generated locator
alignment fields remain unchanged. Screenshot registration, hashes and any retained copies belong
to an authorized pilot step; this proposal does not create supplemental-image records or copy media.

## Proposed storage and data ownership

Use two maintained UTF-8 CSVs across all episodes, with stable keys and no per-episode table files.
The exact ordered fields and vocabulary are defined in [Stage 1's contract](#stage-1-data-contract-v1).
Initialization remains later implementation work.

| Location | Proposed role |
| --- | --- |
| `tools/reference-alignment/` | This proposal, later bounded matching/model/validation commands and tests. Reuse existing gallery/source helpers where appropriate; do not duplicate episode download or RAR tools. |
| `reference/indexes/animehistory/alignment-anchors.csv` | Authored alignment evidence: selected gallery image keys and visually checked local frame/shot matches, including ambiguity and failed attempts. |
| `reference/indexes/animehistory/alignment-mappings.csv` | Authored episode/release/segment mappings, supporting and independent validation anchors, fitted parameters, applicability and verification limits. |
| `reference/indexes/animehistory/category-review.xlsx` | Existing generated ImportExcel workbook; later alignment-anchor/mapping tabs and joined timing fields. No additional workbook or editable spreadsheet authority. |
| `reference/working/alignment/EP-NN/<run-id>/` | Ignored, owned temporary search frames, comparison sheets, candidate scores and execution metadata. Bounded by selected images/windows and recorded resource limits. |
| Existing gallery cache / RAR and subtitle copies | Read-only inputs at their existing locations. Restore selected gallery inputs through the gallery tool when needed; do not reorganize or duplicate collections. |

### Temporary-output retention and episode cleanup

`reference/working/alignment/` is disposable processing space, not a permanent image collection.
Routine episode completion must include alignment-output cleanup after results are validated and
their durable records are checked. Keeping search outputs is an explicit temporary option for
debugging or an unresolved review, rather than the default end state for every episode.

- Retain the authored anchor/mapping records, including ambiguity/failure decisions, source hashes,
  actual PTS/time bases, search bounds, scoring/mask recipe, tool versions, review rationale and
  validation results. Preserve sufficient reproducibility metadata in the maintained records
  before removing the run manifest; references to disposable frame paths alone are insufficient.
- Remove decoded coarse/refinement PNGs, comparison sheets, transient logs and the owned run
  directory once that prerequisite passes. Do not archive these reproducible search outputs into
  each episode RAR by default. Existing gallery images and manual supplements retain their
  separate archive/cleanup rules.
- Keep cleanup available as an explicit tool operation. Stage 5 must validate an episode-finish
  path that previews eligible runs, checks retained provenance and cleans only those owned runs,
  with a keep-output option for unresolved work. Search itself must not delete review material
  before inspection or silently resolve an ambiguous candidate in order to permit cleanup.
- Failed or abandoned disposable runs may be explicitly discarded without promoting their
  candidates to accepted evidence. Such disposal must remain distinct from validated-result
  cleanup; the latter requires durable accepted-result provenance first.

Stage 5 implements the preview/provenance gate in `finish.py`, with explicit keep-output and
unregistered-discard modes. The earlier `alignment.py cleanup` command now requires
`--discard-unregistered` and refuses any run referenced by the anchor register. Registered-result
cleanup must use `finish.py`. Stage 3's historical cleanup used the earlier command after manual
provenance checks; the [Stage 5 results](#stage-5-cleanup-and-reproduction-results--2026-10-27)
record the subsequent automated validation.

Stage 1's contract implements these record requirements:

- **Anchor grain and identity:** one stable anchor ID per selected image/release matching attempt
  or assessment; permit multiple candidates and revised assessments without silent replacement.
  Join the existing episode/image key rather than maintaining another editable copy of web times.
  Preserve failed/ambiguous attempts, reviewer/time, method and concise rationale.
- **Input identity:** gallery image digest and locator snapshot digest; exact source-relative video
  filename, selected video stream, source identity/digest and relevant timing metadata. Reuse
  existing subtitle provenance and verify the subtitle hash/track belongs to that local release.
  Filename/size alone must not silently validate a changed source. Finalize an affordable full-file
  digest/reuse strategy and invalidation rules before treating results as reproducible.
- **Time basis and precision:** retain the observed player label separately from decoded frame PTS
  (presentation timestamp). Define the conversion between stream/container PTS and media-relative
  time used by the player/subtitle track, including nonzero or negative start times. Preserve
  rational time-base precision internally; a decimal display must not imply measured precision.
- **Match scope:** distinguish exact corresponding frame content, visually matching shot interval,
  approximate player observation, machine-proposed candidate and unresolved/no-match results.
  Identical held frames can support an interval rather than a unique instant. Overlay-masked
  similarity is not pixel equality and must be labeled accordingly.
- **Mapping grain:** one stable mapping ID per episode, local release, gallery snapshot and
  bounded segment. Record model, parameters, time range, supporting/holdout anchor IDs, observed
  validation error, uncertainty, reviewer/time and status. Define boundary inclusivity and forbid
  conflicting active mappings for the same inputs/range. Missing coverage stays explicitly unmapped.
- **Status separation:** proposed/reviewed anchors and proposed/validated/rejected/superseded
  mappings must not be confused with image screening, detailed review or canon evidence states.
  Define acceptance thresholds and ambiguity criteria before evaluating the live pilot.

Keep `all-episodes.csv` and `CSVs/episode-NN.csv` as source locators. Do not hand-edit their
generated `local_timestamp` or `alignment_status` columns. Workbook/Power BI joins may derive
matched and estimated local times from the maintained alignment tables, with explicit provenance.
Do not overwrite original web labels, manual-player timestamps or existing annotation records.

## Proposed bounded matching behavior

1. Select an episode, explicit gallery image keys, candidate search windows and run limits. Reuse
   verified cached images and the indexed local video. No network fetch, whole-video frame dump,
   source modification, new installation or desktop automation is implicit in a matching command.
2. Use installed FFprobe/FFmpeg capabilities to inspect timing and decode only the selected
   windows. Record commands, versions, actual frame timestamps and seek/decode behavior. A requested
   seek time is not proof of the timestamp of the returned frame. Honor a frame/disk/time budget;
   widen a failed search only explicitly and within an agreed bound.
3. Normalize comparison size/aspect ratio and deal explicitly with player borders, letterboxing,
   credits/subtitles, color differences and compression. Keep transformations/masks reproducible;
   do not hide a mismatch by aggressively cropping away distinguishing content. A perceptual
   similarity method may rank candidates, with coarse-to-fine search if justified by the pilot.
   Algorithm/dependency choice is deferred to Stage 1/2 inspection of installed capabilities.
4. Present candidate frames with nearby temporal neighbors, original gallery image, actual local
   timestamps and scores. Retain competing matches. A top score alone cannot accept an anchor;
   black frames, repeated opening imagery, held drawings and repeated shots need explicit handling.
5. Visually review and record the supported result, including a time interval when a unique frame
   is not identifiable. Do not assign dialogue speakers from matching scores or infer names/actions
   solely from temporal proximity. Full local text/frames stay ignored; maintained records contain
   concise findings and source-relative provenance.
6. Fit the simplest supported timing relationship and test it on independent images not used to
   choose the parameters. Refuse unsupported extrapolation, insufficient anchors and stale inputs.
   Keep a candidate model separate from any accepted mapping and from calculated browsing fields.

Candidate equations, using seconds on explicitly defined time axes:

- Constant offset: `local_time = web_time + b`. Episode 1's opening seed is approximately `b = −2`.
- Linear drift: `local_time = a × web_time + b`, only if independent checks support a changing
  timing relationship. Do not assume a frame-rate explanation without evidence.
- Piecewise mapping: separate validated segments around edit/cut/timing discontinuities. Do not
  fit one line through a jump or mark a missing local shot as matched.

Web labels have whole-second precision. Exact local frame identification does not upgrade the
precision of every web timestamp or guarantee exact-frame estimates for intervening images.
Observed holdout residuals are measured validation results, not a universal error bound. Sparse
anchors cannot prove the absence of every unobserved edit; monitor mismatches during later review.

## Staged development and acceptance

Build in focused increments and resolve failures before advancing. Record commands, results,
evidence limits and cleanup after each stage. No stage is completed merely by authorizing it.

### Stage 1 — data contract and bounded test design

**Defined — 2026-10-27:** [contract v1 and test plan](#stage-1-data-contract-v1) below. This is a
design checkpoint, not executable-test, live matching or timing-validation evidence.

Define the two CSV contracts, identities, time axes, status vocabulary, mapping boundaries,
input invalidation, temporary-storage limits and reproducibility strategy. Specify numeric
acceptance criteria, holdout selection and independent validation before fitting results.
Plan anchors across the opening, early story, around any eyecatch/commercial-break boundary,
and late story. The supplied opening screenshots remain approximate leads. Use synthetic fixtures
to design tests for fixed offset, drift, discontinuity, ambiguous holds and absent matches.
Do not initialize CSVs, decode video or modify workbook behavior in this stage.

### Stage 2 — matching prototype

Implement read-only source inspection and bounded candidate matching for a few explicit Episode 1
images. Validate normalization, real returned PTS, ranking, repeated/ambiguous shots, overlay
differences, no-match outcomes and budget enforcement. Visually inspect comparison output.
Test interrupted/failed runs, source containment, conflicts, safe cleanup and preservation of
existing inputs. Confirm useful precision and resource use before expanding the pilot. Candidate
search success does not validate an episode-wide model or automatically populate reviewed anchors.

### Stage 3 — Episode 1 timing validation

Select separated anchors through Episode 1, including checks before/after known sequence breaks
and near the end, plus independent holdouts. Record visually reviewed anchors and fit/test the
simplest supported mapping. Exercise model changes and boundaries using synthetic fixtures even
if the live episode needs only an offset. Check an actual subtitle interval against aligned scene
context without declaring the subtitle an exact spoken-language transcript. Record inspected
coverage, failed/ambiguous shots, observed error and remaining uncertainty. No all-episode mapping
is inferred from one release/episode. Stop if pilot criteria fail; retain valid earlier records.

### Stage 4 — workbook and report-ready integration

Extend the existing category workbook using installed ImportExcel, adding anchor/mapping browsing
and clearly separated directly matched versus estimated local times. Display mapping ID, method,
range, status and uncertainty; leave unsupported/stale/out-of-range times blank rather than zero.
Join on stable episode/image/release keys. Validate source/table uniqueness, interval boundaries,
row counts, overlap refusal, hyperlinks, precision and unchanged authored data. Preserve all
9,204 gallery rows, supplements, original timing labels, annotations and review statuses.
Reopen/check saved values and visually inspect affected views; obtain native-viewer feedback.
Test a report-ready projection without building or publishing Power BI yet. No unrequested
schema migration or cloud/media publication is part of this stage.

### Stage 5 — cleanup, procedure acceptance and workflow integration

Record combined results and limits. Remove owned disposable search frames/comparison output
after retaining sufficient source/command/time/method provenance to reproduce accepted results;
implement and test the [episode cleanup boundary](#temporary-output-retention-and-episode-cleanup),
including preview/provenance checks, an explicit keep-output option and refusal while required
review evidence exists only in temporary output. Verify that completed episode processing leaves
no unnecessary decoded alignment frames, comparison sheets or duplicate runs.
Do not delete gallery originals, registered supplements, source videos, subtitle copies or cited
website caches as incidental cleanup. Identified supplemental screenshots follow the existing
episode RAR retention rules. Refuse recursive deletion outside the resolved owned workspace or
through reparse points. Verify cleanup and revalidation after temporary outputs are absent.

Obtain maintainer acceptance before calling this an established procedure. Only then update the
ordered episode workflow to establish/verify timing after gallery preparation and before timed
subtitle-to-image use. Later episode pilots run with explicit scoped authorization and reuse
the accepted procedure; they do not inherit Episode 1's parameters. Installation, bulk processing,
new episode surveys, modeling and Phase 3.2A do not begin automatically. Publication follows the
existing confirmation workflow and never includes source or derivative media implicitly.

## Current completion boundary

Stages 1–3 are technically complete within their recorded pilot scopes. Stage 3 adds reviewed
anchor records, exact-rational model/registry validation and a measured navigation mapping for
part of Episode 1. Unsupported regions and ambiguous/sampled no-match attempts remain explicit.
No generated locator timing fields or existing survey annotations change. Stage 4's derived
workbook/report projections are validated, including native-viewer feedback.
Stage 5's cleanup/reproduction implementation and integrated procedure are validated and accepted
on 2026-10-27; no later episode or Phase 3.2A work is authorized by these results.

## Stage 1 data contract v1

This section is authoritative for the new alignment records; the existing image-index README
continues to own survey fields. Stage 3 implements decoded-search records and model validation;
player-only observation authoring and future workbook projections are not implemented commands.
Maintain exactly two cross-episode CSVs with UTF-8, one header, standard CSV quoting and no formulas.
Identifiers, digests, rational numbers, player labels and UTC values are text; numeric ordering
fields are explicitly typed on import. Empty optional values mean unrecorded, never zero.
Rationals use reduced signed `numerator/positive-denominator` form, including `0/1` and `1/1`.
Use exact rational arithmetic for calculations; format decimal seconds only in generated views.

### Input identity and time axis

`video_source` is the exact repository-relative path under immutable `_source_episodes/`, resolved
with containment/reparse checks. Stream indices are absolute container indices, as in the existing
subtitle coverage record. Before the first Stage 2 run, compute a streaming SHA-256 of only the
selected episode file, checking size/stat stability before and after reading. Verify the registered
ASS and selected gallery image hashes; reuse the per-episode locator CSV digest from the gallery
manifest after checking its bytes. No whole-collection media hashing is authorized by this design.

For later commands, recompute the selected video digest before accepting a new reviewed anchor
or mapping. Reuse that verified digest only within the same locked run while file stat checks
remain unchanged; stat equality alone is never proof across separate acceptance runs. Rendering
an existing workbook does not scan videos; it shows the recorded identity and distinguishes
unavailable/unverified-current-media from observed mismatch. Missing inputs are not invalid records,
but new matching/validation cannot proceed without them. Changed input bytes require a new
`input_id`; preserve earlier rows rather than silently rebinding their source.

`input_id` is SHA-256 of canonical UTF-8 JSON containing the episode ID, video path/hash/stream,
video time base, media origin, subtitle stream/hash/time-basis/shift and locator digest. Use sorted
keys, no insignificant whitespace and no absolute host paths. Every anchor for one input ID must
agree on that tuple. The mapping table joins to this identity through its anchors; do not maintain
a third release table. Gallery image hashes are anchor-specific and checked against the locator key.

Define local media time as `frame_pts × video_time_base − media_origin_seconds`. The rational
origin must be established from probe/decode behavior, including container start and edit offsets;
it is not automatically the first displayed video frame or the first subtitle cue. A negative raw
PTS is permitted when documented; usable playback targets must fall within the local media domain.
Do not compute frame time as frame-number divided by nominal FPS or substitute requested seek time.

The extracted ASS time axis must be checked against the registered extraction command/container
timing. `subtitle_time_basis` is `UNVERIFIED`, `MEDIA_RELATIVE` or `SHIFTED_TO_MEDIA`.
`subtitle_shift_seconds` is blank for UNVERIFIED, `0/1` for MEDIA_RELATIVE, otherwise the verified
rational shift in `local_time = ASS_time + subtitle_shift_seconds`. Video alignment can be studied
with an unverified subtitle basis, but automatic subtitle joins must remain disabled until verified.
Changing that basis/shift changes input ID and requires explicit reconciliation of affected rows.

### alignment-anchors.csv

One row is one candidate/assessment for one gallery image and exact input identity. Allocate
`ALNANC-000001` style IDs once; never derive them from row position or reuse deleted IDs. Multiple
attempts/candidates for the same image are allowed. A revised assessment receives a new ID with
`supersedes_anchor_id`; preserve the earlier evidence and mark it SUPERSEDED explicitly. Refuse
cycles, cross-image/input supersession and competing active accepted matches unless reconciled.

Exact ordered header:

```text
anchor_id,episode_id,image_id,input_id,video_source,video_sha256,video_stream_index,video_time_base,media_origin_seconds,subtitle_stream_index,subtitle_sha256,subtitle_time_basis,subtitle_shift_seconds,locator_sha256,image_sha256,run_id,role,method,recipe_json,search_start_seconds,search_end_seconds,match_kind,status,local_start_pts,local_end_pts,player_timestamp,player_precision_seconds,candidate_score,runner_up_gap,reviewer,reviewed_utc,supersedes_anchor_id,notes
```

| Fields | Contract |
| --- | --- |
| `anchor_id`, `episode_id`, `image_id` | Stable anchor ID and existing gallery episode/image key. Manual screenshots are leads associated with a gallery key, not invented gallery IDs. |
| `input_id` through `image_sha256` | Required identity/time fields as specified above; lowercase 64-character SHA-256s. UNVERIFIED subtitle shift is the only optional member of this identity tuple. |
| `run_id` | Stable `ALNRUN-` plus UUID hex for a bounded attempt. Shared by candidates generated in the same run; not a filesystem path. |
| `role` | `LEAD`, `FIT` or `HOLDOUT`, frozen before the attempt is evaluated. The two supplied opening observations are LEAD. |
| `method` | `PLAYER_SCREENSHOT` or `BOUNDED_FRAME_SEARCH_V1`. Method describes acquisition, not verification. |
| `recipe_json` | Compact reproducibility JSON: tool/code versions, actual executable versions, search sampling/refinement, normalization, mask rectangles, score definition, budgets and requested seek/decode arguments. No tokens/cookies/absolute host paths. Retain all parameters needed to regenerate candidates after disposable outputs are removed; a deleted log path alone is insufficient. |
| `search_start_seconds`, `search_end_seconds` | Rational local-media search interval `[start,end)`, required for frame search; blank for screenshot-only observations. Must be bounded, within the inspected source duration and recorded before processing. |
| `match_kind` | `UNASSESSED`, `CORRESPONDING_FRAME`, `SHOT_INTERVAL`, `PLAYER_OBSERVATION` or `NONE`. CORRESPONDING_FRAME means visually corresponding animation/composition within stated overlay/encoding differences, not byte-identical source imagery. |
| `status` | `CANDIDATE`, `MATCHED`, `AMBIGUOUS`, `NO_MATCH`, `REJECTED` or `SUPERSEDED`. Machine output starts CANDIDATE or a non-match diagnostic; only a documented visual assessment can set MATCHED. |
| `local_start_pts`, `local_end_pts` | Integer source-stream frame PTS, inclusive endpoints of a contiguous visually supported set of matching frames. Equal for a unique corresponding frame. Required for MATCHED decoded matches; blank for player-only observations and no-match results. Do not compress disjoint candidate intervals into one range. |
| `player_timestamp`, `player_precision_seconds` | Preserve the exact supplied VLC label and its display resolution separately; `01:44` and `1/1` are valid. This is not decoded PTS. Whole-second display alone does not establish a rounding rule or an exact instant; no automatic ±0.5 s precision claim. |
| `candidate_score`, `runner_up_gap` | Optional rational values in `[0,1]`, interpreted only with the recipe. Compare against the next distinct temporal candidate cluster, not the adjacent duplicate frame. Scores never establish review or correctness. |
| `reviewer`, `reviewed_utc` | Paired assessment provenance; UTC ISO 8601 with Z or +00:00. Required for MATCHED/AMBIGUOUS/REJECTED/SUPERSEDED and reviewed NO_MATCH; machine diagnostics without review remain explicit in notes. |
| `supersedes_anchor_id`, `notes` | Optional supersession target; notes required for ambiguity, no match, rejection, supersession, player observations and any masking/precision limitation. Include supplied-image provenance/registered supplement pointer if retained later. |

PLAYER_OBSERVATION may be MATCHED at same-shot precision with reviewer attribution, but never
participates in fitting or holdout acceptance. A MATCHED SHOT_INTERVAL is useful evidence without
being a unique timestamp. No-match rows use NONE; CANDIDATE/AMBIGUOUS rows must not become direct
local-time projections. MATCHED decoded anchors project a local interval and method, not a
fabricated single frame when the interval is nonzero.

### alignment-mappings.csv

One row is a model for one episode/input and one half-open integer-web-second segment. Allocate
`ALNMAP-000001` IDs once. Piecewise alignment uses multiple non-overlapping rows, not another
formula type. `supersedes_mapping_ids` lists earlier IDs separated by semicolons; preserve history,
forbid cycles and reconcile replaced ranges explicitly. No two active VALIDATED mappings may
overlap for the same episode/input; unresolved conflicts disable derived timing for that overlap.

Exact ordered header:

```text
mapping_id,episode_id,input_id,segment_label,web_start_seconds,web_end_seconds,model,scale,offset_seconds,fit_anchor_ids,holdout_anchor_ids,status,max_fit_interval_error_seconds,median_holdout_interval_error_seconds,max_holdout_interval_error_seconds,max_anchor_width_seconds,estimated_half_window_seconds,method_version,reviewer,reviewed_utc,supersedes_mapping_ids,limitations
```

| Fields | Contract |
| --- | --- |
| `mapping_id`, `episode_id`, `input_id`, `segment_label` | Stable mapping identity, existing episode/input and concise scope, e.g. opening or post-eyecatch. A label does not prove that an edit boundary exists. |
| `web_start_seconds`, `web_end_seconds` | Whole-number interval `[start,end)` on the existing web-label axis. No default coverage outside checked anchors: start at the earliest accepted anchor label and end at the latest +1 second. This last bin admits that whole-second locator, not extrapolation to arbitrary fractional web times. Narrow/split coverage at observed discontinuities. |
| `model`, `scale`, `offset_seconds` | `OFFSET` or `LINEAR`; rational parameters of `local = scale × web + offset`. OFFSET requires scale `1/1`. No parameters copied to another episode/input. |
| `fit_anchor_ids`, `holdout_anchor_ids` | Sorted unique semicolon-separated IDs, disjoint and on the same episode/input. All must be active MATCHED decoded anchors of the declared role, within the segment. At most one independent vote per image key. |
| `status` | `PROPOSED`, `VALIDATED`, `REJECTED` or `SUPERSEDED`. Validation requires all criteria below plus reviewer/time. Availability/staleness of local inputs is a separate derived condition, not silent record rewriting. |
| `max_fit_interval_error_seconds`, `median_holdout_interval_error_seconds`, `max_holdout_interval_error_seconds` | Rational observed errors computed by the stated method, required for validation. Preserve failed measured values on a rejected model. Empty is untested, never zero error. |
| `max_anchor_width_seconds` | Largest supported local-time interval width among included anchors, for precision visibility and eligibility checks. |
| `estimated_half_window_seconds` | Rational suggested navigation/search half-window; baseline `2/1`. This is a practical search setting, not a guaranteed uncertainty bound or frame accuracy. |
| `method_version` | `ALIGNMENT_MODEL_V1` for the criteria below. Changing criteria requires an explicit version/review, not overwriting prior validation under the same label. |
| `reviewer`, `reviewed_utc`, `supersedes_mapping_ids`, `limitations` | Paired UTC review provenance, optional replacement IDs and required scope/error/continuity limitations. An empty model is not evidence of zero offset. |

Fitting uses midpoints of eligible decoded anchor intervals. OFFSET uses the median of
`local_midpoint − web_label`; LINEAR uses ordinary least squares of those midpoints. Retain
rationals and deterministic tie behavior (median averages the two central values for even counts).
For a prediction p and supported local interval [L,U], interval error is `max(L−p,0,p−U)`.
These residuals describe agreement with reviewed anchors. Do not enlarge anchor intervals, masks
or thresholds after fitting to turn a failure into a pass. Test alternatives as new proposed rows.

### Predetermined pilot and acceptance criteria

These are Stage 1 design requirements, not measured pilot results or promised achievable accuracy.
Failure must remain reportable; revised limits require a versioned design decision before a new run.

| Area | V1 gate |
| --- | --- |
| Stage 2 scope | Explicit Episode 1 locators 002, 004, 028, 051 and 071 (IDs 846774, 846776, 846800, 846823, 846843). These exercise overlay differences, moving animation, a seated pilot, ship exterior and a potentially ambiguous glass effect. These prototype images are not Stage 3 fit/holdout images. |
| Search bounds | Maximum five images per command; initial 12 s window per image. For 002/004 only, center the search on web time −2 s; for others use the unverified web-time seed without assuming the opening offset. No automatic widening or additional images. |
| Resource caps | At most 60 s initial media-window coverage per run, 900 saved candidate frames, 600 MiB run storage and 15 min processing wall time. Coarse sampling target 4 frames/s, then native-PTS refinement within at most two 1 s candidate windows per image. At most 70 s union coverage after refinement. Keyframe preroll is still bounded by the process timeout. Stop gracefully on any cap; do not resample timestamps to pretend to have decoded different source frames. |
| Ranking gate | Prototype comparison uses normalized greyscale mean absolute difference at 320×240, score `1 − MAE/255`, with explicit aspect normalization and optional recorded rectangular masks. At least 70% of picture pixels must remain. Scores ≥0.90 and distinct-cluster gap ≥0.01 are candidate-review aids only; lower/close results stay ambiguous unless a reviewer documents an independent visual resolution. No score sets MATCHED automatically. |
| Review packet | Show original uncropped gallery/candidate views, transformations/masks, top three distinct temporal clusters where available, and neighboring native frames. Low-texture/black frames, repeated drawings and missing shots are not accepted by score alone. |
| Anchor eligibility | A fitted/tested anchor must have a visually supported decoded interval width ≤0.5 s and be distinguishable from competing shots. Wider shot matches/player screenshots remain evidence leads but cannot validate model accuracy. No unreviewed candidate or superseded row participates. |
| Stage 3 initial partition | FIT ordinals 010, 072, 144, 216, 288, 348; HOLDOUT 018, 108, 252, 330. Freeze roles before matching/fitting. The two supplied screenshots are LEAD only. Holdouts are never used for coefficients, mask tuning or favorable point selection. |
| Coverage | Inspect the opening, early/middle/late story and both sides of any identified eyecatch/edit boundary. The ordinal list is an initial spread, not proof that every boundary is bracketed. Add explicitly predeclared anchors/holdouts if needed; retain failed original selections rather than replacing them invisibly. No whole-runtime claim outside supported web-label ranges. |
| OFFSET acceptance | At least three independent FIT and two independent HOLDOUT images per segment; all included anchors meet the width/review gate. Max fit interval error ≤1.0 s; median holdout interval error ≤0.5 s; max holdout interval error ≤1.0 s. No unexplained boundary mismatch, competing active mapping or stale input. |
| LINEAR acceptance | Consider only if OFFSET fails. At least five FIT and three HOLDOUT images spanning ≥300 s; the same residual limits must pass. Require a positive scale within [0.95,1.05], predicted drift ≥1.0 s over the segment and median holdout-error improvement ≥0.25 s over the rejected OFFSET. A result outside these bounds requires investigation/revised design, not silent clipping. |
| Segment changes | A discontinuity cannot be concealed by widening error limits or fitting across a jump. Split at a checked boundary and meet the minimum fit/holdout gate independently in each segment; under-supported regions stay unmapped. |
| Subtitle check | After verifying the subtitle time basis, check at least two dialogue windows against reviewed scene context in separated covered regions. Preserve source/track/hash and local cue intervals; a search window or textual match alone cannot verify speaker identity or original language. |

Candidate ranking thresholds are intentionally conservative heuristics for this prototype, not
calibrated probabilities. Stage 2 reports ranking success/failure and resource observations; a
poor heuristic is revised explicitly before further matching rather than reinterpreted as truth.
The minimum segment counts can require extra anchors beyond the initial ten-image partition;
insufficient regions remain unsupported instead of relaxing counts after inspection.

### Required regression scenarios and integration checks

Stage 1 defines these fixtures conceptually. Matcher, timestamp parsing, input-preservation,
resource and cleanup fixtures are Stage 2 work. Model/holdout/domain fixtures accompany Stage 3's
model implementation; later projection fixtures accompany Stage 4. They are not passed tests
merely because the bounded matcher passes its own tests.

| Scenario | Required behavior |
| --- | --- |
| Known offset / sign | Synthetic `local=web−2` recovers negative offset and passes independent holdouts; the inverse conversion is not mistaken for the forward equation. |
| Drift | Synthetic positive linear drift that fails OFFSET but meets LINEAR criteria recovers the supported relationship; inadequate span or a nonpositive/out-of-range scale is rejected. |
| Cut / missing scene | A planted step change cannot validate as one smooth model. Correctly split segments must pass independently; absent local content yields NO_MATCH and no estimated match for that image. |
| Held or repeated imagery | Identical neighboring frames produce a supported interval; distant repeats produce separate competing clusters. An interval wider than 0.5 s cannot become a precise fitting point. |
| Overlays / normalization | Credit/subtitle/border differences retain reproducible masks and full comparison views. Excessive crop/mask fails the retained-area gate. Different scene content is not rescued by hiding it. |
| Actual timestamps | Synthetic nonzero/negative starts, variable frame intervals, duplicate/nonmonotonic PTS and seeking preroll test actual returned PTS handling. Refuse unresolved/disordered timing; do not substitute nominal FPS or request time. |
| Source/subtitle change | Wrong source/stream/hash, changed gallery/locator bytes, inconsistent input tuple and unknown subtitle basis prevent the affected acceptance/join without destroying prior records. |
| Independence / precision | Role leakage, duplicate-image votes, reused holdouts, insufficient counts, interval inflation and rounding that hides an error are refused. Exact threshold edges are tested with rational values. |
| Domain and identity | Enforce half-open mapping boundaries, unique stable IDs, no cycles, no conflicting validated ranges and no automatic extrapolation. Unsupported browsing values are blank with an explicit reason, never zero. |
| Recovery and cleanup | Test interrupted decoding/output promotion, caps, missing inputs, locked/conflicting destinations and reparse/traversal paths. Preserve source files and earlier valid tables/workbooks; delete only the resolved owned run outputs. |
| Later projection | Preserve all 9,204 locators, manual supplements, annotations and original web/player labels. Verify direct-match intervals versus mapping estimates, input/status/method display and separate Power BI bridge grains; do not multiply image counts. |

Stage 4 must publish the two alignment tabs and joined derived fields in the existing category
workbook only. Required derived columns are `matched_local_start`, `matched_local_end`,
`estimated_local_time`, `timing_basis`, `mapping_id`, `alignment_availability` and
`suggested_search_half_window_seconds`. `timing_basis` distinguishes DIRECT_MATCH,
MAPPING_ESTIMATE, PLAYER_LEAD and UNMAPPED; availability distinguishes verified-current,
recorded-but-unchecked-current, missing and mismatch. These are derived projections, not a
migration of generated locator or authored survey fields. Pinned direct evidence can coexist
with a model estimate for comparison, but neither overwrites the other.

### Stage 1 design-check result

The existing per-episode gallery metadata provides stable image keys/web seconds and a locator
digest; cached images provide separate byte hashes. Existing subtitle coverage pins episode/source,
stream and ASS digest. Existing extraction records distinguish requested seek time from decoded
PTS and time base. These satisfy the planned join/provenance inputs, while full video digest,
media origin, current executable paths and subtitle-axis verification remain Stage 2 obligations.

The planned Stage 3 image ordinals resolve in Episode 1's existing 354-row locator list and span
02:14–21:42; holdouts are 02:42, 07:53, 16:10 and 20:40. This is metadata selection only, not a
visual review of future batches or proof of a constant offset. No synthetic/live test has run,
no anchor/mapping is initialized and no existing review/timing status changes as part of Stage 1.

## Stage 3 execution selection — 2026-10-27

The initial FIT/HOLDOUT partition remains unchanged. Initial FIT searches flagged five broad
score regions; visual inspection does not justify precise points for those held/similar drawings.
Preserve them as ambiguous attempts. Before additional matching or model fitting, declare
supplementary FIT ordinals **084, 087, 204, 208, 257, 259, 328** (IDs 846856, 846859, 846976,
846980, 847029, 847031, 847100). They target visible action, the spinning mid-episode graphic,
the following display shot, combat and the caster effect. Selection uses existing gallery sheets,
not measured residuals; no original HOLDOUT changes role. Gallery-sheet inspection also exposed
the holdout thumbnails at 252/330 incidentally; their local matches remain unmeasured at this point
and do not influence fitting-image selection or coefficients. Eyecatch graphics appear at
204–207, between web 13:25 and 13:35; check both sides explicitly rather than assuming continuity.
Before freezing coefficients or searching any holdout, add HOLDOUT ordinals **213, 258, 321**
(IDs 846985, 847030, 847093), selected from visible hand/combat/projectile motion in the existing
sheets. These supplement rather than replace the four original holdouts. They provide an explicit
post-eyecatch check and additional moving shots if original samples are held or missed by coarse
sampling. Keep every attempted result; do not discard a failed precise holdout to improve acceptance.

## Stage 2 prototype validation — 2026-10-27

### Implemented boundary

`alignment.py` implements local-only `search` and explicit owned-run `cleanup`. The prototype
accepts only Episode 1 and the five predeclared IDs; it refuses other episodes, future fit/holdout
images, duplicate selections and more than five images. It writes only ignored run outputs.
There are no network requests, automatic installations, model fits, accepted-anchor writes,
spreadsheet updates or episode-review status changes.

The implementation uses installed Python 3.12.14, Pillow 12.3.0 and FFmpeg/FFprobe
9.0.1-essentials_build-www.gyan.dev. The run records the implementation digest, runtime versions,
full selected-video SHA-256, locator/gallery/subtitle hashes, selected streams, probe metadata,
commands, masks, rational PTS-derived local times and per-frame hashes. Subprocesses are bounded
by the run deadline; decoding children are killed and reaped on interruption/failure. Failed
runs retain a FAILED manifest and local diagnostics instead of appearing complete.

Live searches used the predetermined 12 s windows, 4 frames/s target coarse sampling and at most
two native-frame 1 s refinement windows per image. The explicit mask `(0,204,320,240)` excludes
the bottom 15% of the normalized picture from scoring; 85% remains. Full uncropped color images
are shown for visual review. No threshold, mask or search window was tuned after seeing results.

### Live candidate results

Both five-image runs produced identical input identities, candidate records, PTS, scores,
ambiguity diagnostics and saved decoded-frame hashes. The final run is
`reference/working/alignment/EP-01/ALNRUN-d2d2dd0402a34d4bac74f3a6c058b8cd/`.
Its five `comparison.png` files were inspected against the gallery views and decoded neighbors.

| Locator / ID | Web label | Best decoded local candidate | Score | Visual inspection and timing limit |
| --- | --- | --- | --- | --- |
| 002 / 846774 | 01:46 | 01:45.147 / PTS 105147 | 0.99355 | Corresponding caster/table composition; small pan and release/compression differences remain. |
| 004 / 846776 | 01:53 | 01:52.070 / PTS 112070 | 0.99260 | Corresponding Melfina hair/petal drawing; following decoded frame crosses into the next character shot. |
| 028 / 846800 | 03:16 | 03:15.028 / PTS 195028 | 0.99283 | Corresponding seated-pilot composition, but similar drawings at 03:18.865 and 03:20.784 compete. AMBIGUOUS_CLUSTERS; no precise anchor accepted. |
| 051 / 846823 | 04:36 | 04:34.524 / PTS 274524 | 0.99343 | Corresponding ship/green-line composition; neighboring frames show changing bright effects. |
| 071 / 846843 | 05:45 | 05:43.635 / PTS 343635 | 0.99127 | Corresponding hands/glass/reflections composition; neighboring frames differ in motion. |

These are visually corroborated candidate shots, not pixel-equal frames, accepted MATCHED
anchors or fitted timing points. The printed milliseconds are source PTS precision, not a claim
of millisecond alignment accuracy. The gallery's whole-second labels and differing animation
drawings still matter. Differences of approximately −0.85 to −1.48 s in this small early-episode
selection do not establish an episode-wide constant offset or drift model.

The selected release has video stream 0, time base `1/1000` and container origin `0/1`.
Its full video digest is
`05f4bfbe5e0d84d0e03a854699f2cc14bdcb8ded74f7ea4f6fef0ec3d0182e48`.
The input ID is `cbc30c1dd4fe0666b3dacb4d7448b35d2237f7e4922ef17ae04a2f2a5c0c9ea0`.
Subtitle stream 4 and the registered ASS digest matched; the first three ASS cue starts
(10.98, 13.02 and 21.73 s) equal the source subtitle-packet times. MEDIA_RELATIVE records this
bounded time-axis check only. Whole-track synchronization, dialogue interpretation and separated
subtitle-context checks remain Stage 3 work.

The final Stage 2 run took **13.344 s**, saved **381 decoded PNGs**, and occupied **285,988,256 bytes**
(about **272.74 MiB**) after final manifest writing. Initial search coverage was 60 s; the sum
of initial/refinement window widths was 66 s, a conservative upper bound on their union and
within the 70 s cap. The duplicate earlier run was removed through `cleanup`; the retained
run remained local and ignored for review at Stage 2 completion. Stage 3 subsequently retained
its five leads in the anchor CSV and removed its disposable outputs. Synthetic fixtures are
removed automatically.

### Regression evidence and remaining limits

`test_alignment.py` passed **22 tests**, including an actual FFmpeg synthetic-video decode.
Covered cases include exact rational arithmetic and canonical identity, mask union/70% boundary,
different-content and overlay scores, aspect mismatch, held/repeated imagery, score-threshold
edges, variable/negative/nonzero PTS parsing, duplicate/disordered/missing/out-of-window PTS,
corrupt output, changed gallery/locator/subtitle inputs, wrong video size, ambiguous video stream,
wrong subtitle stream, unknown subtitle
axis, full-file hash change, missing source, frame/disk/deadline limits, subprocess failure,
timeout/interruption, writer conflicts, failed-run preservation, scope guards and owned cleanup.
The Windows reparse guard uses a mocked reparse attribute, not a live junction fixture.
No source fixture or preexisting authored table is changed by these tests.

Material prototype limits:

- Live decoding is validated only for this zero-origin release. Nonzero/negative container
  origins are refused until their seek policy has separate integration evidence; parser tests
  alone do not establish full decode support for those sources.
- Coarse sampling can miss a very brief shot, and refinement examines only two selected regions.
  A low/empty result stays unresolved; there is no automatic wider extraction or NO_MATCH proof.
- Temporal groups contain samples within the configured near-best score band. A missing runner-up
  gap means no second qualifying group, not proof of independent separation. Group extents are
  score regions, not reviewed held-frame intervals. Low-texture/repeated shots still need review.
- Original dimensions and square pixels are checked; aspect differences over 2%, non-square pixels
  and pictures larger than 1920×1080 are refused. The heuristic is not calibrated across releases.
- Budget checks poll decoding and can leave partial output on failure. Completion requires the
  final checks; partial outputs must be inspected or removed using the owned cleanup command.
- Offset/drift/cut fitting, independent holdout gates, accepted-anchor precision, mapping-domain
  validation and workbook preservation/projection tests have not run. Those belong to Stages 3–4.

### Prototype commands

Run from the repository root using the installed Python runtime and explicit installed FFmpeg
paths where they are absent from PATH. No package installation is part of these commands.

```powershell
python tools/reference-alignment/alignment.py search --episode 1 --image-id 846774 --image-id 846776 --image-id 846800 --image-id 846823 --image-id 846843 --ffmpeg <ffmpeg.exe-path> --ffprobe <ffprobe.exe-path> --mask 0,204,320,240
$env:ALIGNMENT_TEST_FFMPEG = '<ffmpeg.exe-path>'
python -m unittest discover -s tools/reference-alignment -p 'test_*.py' -v
python tools/reference-alignment/alignment.py cleanup --episode 1 --run-id <exact-ALNRUN-id>
```

The cleanup example above records the historical Stage 2 command. Current cleanup uses the
Stage 5 preview/apply procedure; direct unregistered discard requires its explicit flag.

Cleanup validates the explicit resolved run path, run ID, owner manifest and descendants before
recursive removal. It cannot delete a gallery cache, source directory or arbitrary path. This
section records prototype behavior and validation; it is not yet the accepted integrated procedure.

## Stage 3 validation results — 2026-10-27

### Records, independence and visual assessments

`models.py` adds reviewed-run registration, exact-rational OFFSET/LINEAR calculations, proposal
freezing and register validation. It uses the ordered schemas above and initializes only
`alignment-anchors.csv` and `alignment-mappings.csv`. Registration/model acceptance recomputes
the full selected-video digest and checks source/gallery/subtitle/locator identities before
writing. Changed input, invalid schema, stale votes or failed validation preserve existing files.
Registry `validate` checks recorded evidence and calculations without assuming current media
availability; its output explicitly reports `current_media_check=NOT_PERFORMED`.

Each new Stage 3 image was searched only after its role was declared, with the unchanged scoring
mask, thresholds and 12 s bounds. All 20 comparison packets were visually inspected. High scores
were not sufficient for precise acceptance: held dialogue/credit drawings remain ambiguous,
and the smoke/caster-effect searches did not establish corresponding drawings in sampled output.
NO_MATCH here describes that bounded sampled attempt, not absence from the underlying episode.

| Role | Ordinals accepted at decoded-frame/short-interval precision | Ambiguous | Sampled no-match |
| --- | --- | --- | --- |
| FIT | 087, 204, 257, 288 | 010, 072, 084, 144, 208, 216, 259, 348 | 328 |
| HOLDOUT | 252, 258, 321, 330 | 108, 213 | 018 |

No unresolved image was relabeled as a passing holdout or a precise failed holdout. Individual
notes explain the visible mismatch/ambiguity; no original attempt was deleted from the register.
The additional selections and incidental holdout-thumbnail exposure are recorded in the execution
selection above. Selection was based on gallery content, not residuals, and no masks, thresholds,
intervals or coefficients were tuned using holdout errors.

`ALNMAP-000001` froze the OFFSET coefficients using FIT anchors 000005, 000008, 000009 and
000011 **before any local holdout search**. It was PROPOSED and unvalidated at that point.
After independent holdout inspection, `ALNMAP-000002` retained the exact same fit IDs and
coefficients; the initial proposal is preserved as SUPERSEDED. Accepted holdouts are 000016,
000017, 000019 and 000020. The remaining original/supplementary assessments retain their states.
The five historical Stage 2 leads are also retained as four CANDIDATE and one AMBIGUOUS LEAD,
without promotion or fitting votes. Final totals: **25 anchors; 8 MATCHED, 11 AMBIGUOUS,
2 NO_MATCH, 4 CANDIDATE; 2 mapping-history rows, 1 VALIDATED**.

### Validated mapping and coverage limits

For the pinned Episode 1 CBM release/input identity recorded in Stage 2:

`local_seconds = web_seconds − 347/250` (−1.388 s).

| Measure | Observed result | Gate |
| --- | --- | --- |
| Independent FIT / HOLDOUT count | 4 / 4 | At least 3 / 2 for OFFSET |
| Maximum fit interval error | 41/125 s = 0.328 s | ≤1 s |
| Median holdout interval error | 471/2000 s = 0.2355 s | ≤0.5 s |
| Maximum holdout interval error | 81/125 s = 0.648 s | ≤1 s |
| Maximum accepted anchor interval width | 63/500 s = 0.126 s | ≤0.5 s |
| Web-label applicability | `[400,1241)`, whole-second labels 06:40 through 20:40 | Checked-label envelope only |

OFFSET passes; no live LINEAR model is justified under the predetermined simpler-model rule.
The mapping is sampled navigation guidance with a suggested ±2 s search window, not exact
frame synchronization or a bound on every uninspected instant. The opening, early story before
06:40, and ending after 20:40 remain **unmapped**. Held original samples near the beginning/end
are not converted into precise endpoints. No parameter is copied to another episode/release.

The eyecatch is sampled at the spinning graphic (204) and following display/face shots (208/213).
The latter corroborate the far-side scene at shot precision but are not model votes. Later precise
holdouts pass without a coefficient change; no discontinuity was demonstrated at the inspected
resolution. Sparse checks cannot prove uninterrupted frame correspondence through the break or
exclude an unobserved short edit. More precise boundary/full-runtime coverage remains separate
research when needed, not an implicit expansion of this validation.

### Subtitle-context checks

The registered ASS digest remains
`edbb42674cf707b51122ddd54b132d16ffde7fe981b54f24170c155810d0b0f3`, stream 4, with the
MEDIA_RELATIVE basis established by the bounded packet check. Two separated local intervals
inside the supported navigation region were inspected:

| ASS dialogue ordinal / local interval | Visual/context check |
| --- | --- |
| Cue 76, 396.64–402.84 s | The subtitle challenges Gene about the earlier Butch confrontation. Accepted local frame 398.940 s shows the coat/hand/torso bar confrontation; adjoining gallery/candidate views establish that scene context. |
| Cue 198, 969.84–972.97 s | The subtitle demands that the woman be left behind. Saved local frame PTS 971012 (971.012 s) shows the blue-clad attacker's close-up in the alley, following the group composition at holdout 252. |

These checks support scene-level dialogue lookup on the recorded local time axis. They do not
verify the original Japanese wording, speaker identity from timing alone, continuous whole-track
sync or an exact dialogue-to-gallery-frame match. Cue text was summarized rather than used to
override the visible evidence or assign new survey tags. No existing annotation is retrospectively
marked subtitle-reviewed by this pilot.

### Tests, resources and disposable-output cleanup

**38 tests pass**: the 22 matcher regressions plus 16 model/registry tests. Added cases cover
negative offset sign, even-count medians, exact residual edges, holdout coefficient independence,
recoverable drift, insufficient span/counts, invalid scale, unnecessary LINEAR fits, inadequate
holdout improvement, planted step changes with separately passing segments, wide intervals,
duplicate votes/IDs, identity/role/state mismatches, stored metric/coefficient corruption,
half-open domain/extrapolation checks, conflicting validated coverage, supersession cycles,
CSV round trips, stale-input refusal before registry writes and changed gallery bytes with an
otherwise unchanged video/input identity. Synthetic step/drift tests do not
assert those features exist in Episode 1. Current media availability is separate from record validity.

Six Stage 3 runs searched 20 declared images and saved 1,478 decoded frames, occupying
1,141,293,360 bytes in total; recorded processing time summed to 53.251 s. Each run stayed below
the existing per-run 900-frame / 600 MiB / 15-minute cap; the largest used 359 frames and
325,371,616 bytes. No automatic widening or full-episode frame dump occurred.

After recording the complete methods/identities, actual accepted PTS/frame hashes, review notes,
ambiguous/no-match attempts and model history, the six Stage 3 runs and retained Stage 2 run
were removed with the existing explicit owned-run cleanup command. This removed **1,427,281,616
bytes** (about 1.33 GiB), including 1,859 decoded PNGs and comparison/log output. Seven disposable
assessment JSON inputs were also removed after their notes were retained in the CSV. No ALNRUN
directory remains under the Episode 1 alignment workspace. Ten maintained-input/register/subtitle
files have identical pre/post-cleanup hashes, and the 25-anchor / 2-mapping register validates
after removal. Gallery images, contact sheets, source videos and subtitle files are preserved.
An explicit `validate --current --ffprobe ...` check also rehashes the Episode 1 video, selected
gallery inputs, registered subtitle and locator baseline after cleanup; logical `validate` alone
does not make that current-media claim.

At Stage 3 completion, this manually checked cleanup used the already tested command; it did not
implement Stage 5's episode-finish preview/provenance gate or regeneration-from-durable-records test.
Stages 4–5 were then unstarted. No workbook, generated locator, category/context annotation,
other episode or Phase 3.2A change is included in Stage 3.

### Stage 3 commands

```powershell
python tools/reference-alignment/alignment.py search --pilot-stage 3 --episode 1 --image-id <declared-image-id> --ffmpeg <ffmpeg.exe-path> --ffprobe <ffprobe.exe-path> --mask 0,204,320,240
python tools/reference-alignment/models.py record --run-id <exact-ALNRUN-id> --assessments <local-reviewed-assessment.json> --ffprobe <ffprobe.exe-path>
python tools/reference-alignment/models.py propose --fit <FIT-anchor-ids> --label <scope-label> --limitations <recorded-limits> --ffprobe <ffprobe.exe-path>
python tools/reference-alignment/models.py propose --fit <same-FIT-ids> --holdout <reviewed-HOLDOUT-ids> --label <scope-label> --limitations <recorded-limits> --ffprobe <ffprobe.exe-path> --assess --supersedes <frozen-proposal-id>
python tools/reference-alignment/models.py validate
python tools/reference-alignment/models.py validate --current --ffprobe <ffprobe.exe-path>
```

Assessment inputs explicitly name image ID, status, match kind, supported start/end PTS for a
MATCHED result, reviewer and rationale. Registration never chooses those values from scores.
Revision of an existing anchor assessment requires explicit supersession; that authoring command
is not implemented yet, so repeated registration of the same run/image is refused. Model proposals
are recorded before independent testing; final assessment refuses changed frozen coefficients.

## Stage 4 integration results — 2026-10-27

**Status:** implemented, validated and confirmed by the maintainer on 2026-10-27. The maintainer reported that
the new tabs open correctly in the native viewer and that EP-01 row 92 displays the direct time
`00:06:38.940` separately from the mapping estimate `00:06:38.612`. Stage 5 was then unstarted;
its subsequent results are recorded below.

`projection.py` derives read-only timing views from the existing locator, supplement and alignment
registers. `build_category_workbook.ps1` uses ImportExcel 7.8.10 to refresh the existing ignored
`category-review.xlsx`. Its 30 worksheets include the original overview, 26 episode tabs and
manual-supplement tab, plus **Alignment anchors** and **Alignment mappings**. All 9,204 gallery
rows, nine supplements, 25 anchor assessments and two mapping-history records are preserved.
Authored CSVs, original web/player labels, annotations and review statuses remain unchanged.

### Derived fields and availability

The seven required timing fields are implemented. Additional provenance columns are `anchor_id`,
`anchor_status`, `alignment_input_id`, `alignment_method`, `alignment_reason` and
`alignment_checked_utc`. Three numeric companions, `matched_local_start_seconds`,
`matched_local_end_seconds` and `estimated_local_seconds`, support report calculations without
parsing display labels. These values and the suggested search half-window are numeric or null;
unavailable times are blank, never zero. IDs and `HH:MM:SS.mmm` display labels remain text.
Exact rational values and decoded PTS remain authoritative in the alignment registers;
millisecond display rounding does not establish millisecond accuracy.

- `DIRECT_MATCH` supplies the accepted anchor interval. A bounded mapping estimate can coexist
  in its separate column; neither replaces the other.
- `MAPPING_ESTIMATE` requires a validated mapping with matching identity and a web label inside
  its half-open domain. Ambiguous/candidate/no-match assessments never become direct matches.
- `UNMAPPED` leaves unsupported times blank. Other episodes do not inherit Episode 1's mapping.
- `PLAYER_LEAD` preserves manual supplements' unreconciled player labels in their original fields,
  without inventing gallery associations or local timing.

Default refresh checks locally available registration metadata and small-input digests, without
rehashing the source video. Its available records read `RECORDED_UNCHECKED`. Explicit
`-VerifyAlignmentMedia` performs the current pilot's source/input verification and records
`VERIFIED_CURRENT` with a UTC check time. Missing or mismatched inputs read `MISSING` or
`MISMATCH` and suppress derived image timings; historical raw evidence remains visible in the
alignment tabs. An episode row can be `VERIFIED_CURRENT` and `UNMAPPED`: source identity passed,
but no timing match or mapping covers that image. Availability is not a precision/confidence score.
The original locator `alignment_status` remains `UNVERIFIED`; use the new derived fields for
bounded timing provenance. Fresh verification currently follows the Episode 1 pilot contract.

The verified pilot projection contains eight directly matched rows, 236 estimate-only rows and
8,960 unmapped rows. The 244 rows with mapping coverage are limited to Episode 1 web labels
06:40–20:40; the recommended search half-window remains two seconds.

### Report-ready grains

The disposable JSON projection provides separate arrays rather than expanding the gallery table:

| Array | Grain / relationship | Pilot count |
| --- | --- | ---: |
| `gallery_timing` | One `image_key` (`episode_id:image_id`) per gallery locator | 9,204 |
| `manual_timing` | One manual supplement key; separate from gallery counts | 9 |
| `anchors` | One `anchor_id`; includes raw history and input identity | 25 |
| `mappings` | One `mapping_id`; includes superseded and validated history | 2 |
| `image_anchors` | Image key to anchor ID and input ID | 25 |
| `image_mappings` | Image key to applicable validated mapping ID and input ID | 244 |
| `mapping_anchors` | Mapping ID to anchor ID with FIT/HOLDOUT role and mapping status | 12 |

Join bridges to their unique image/anchor/mapping keys. Filter mapping status explicitly when
reporting current accepted coverage: the 12 mapping-anchor links include four superseded-proposal
FIT links and eight validated FIT/HOLDOUT links. Do not flatten the bridges into the image fact
table or count their rows as images. Conflicting identities, duplicate keys or overlapping active
mapping coverage fail refresh instead of selecting an arbitrary record. No Power BI model or
dashboard is built or published in this stage; JSON is a generated projection, not another authority.

### Validation evidence

The alignment suite passed **49 tests**, including 11 projection tests; the existing category suite
passed **10 tests**. Projection fixtures cover interval/estimate separation, half-open boundaries,
unaccepted history, missing/mismatched inputs, manual leads, unchanged source data, bridge grains,
identity conflicts, blank versus zero, timestamp rounding and verification modes.

The production workbook was saved and reopened with ImportExcel. Checks compared **432,588
gallery cells**, **459 manual cells**, **1,029 alignment cells**, all **9,204 image links**, nine
manual links and 25 anchor-to-gallery links. Overview totals and all 30 worksheet names passed.
OpenXML inspection independently confirmed timestamp/ID string types, numeric second values and
physically blank unsupported timing cells. No formulas are introduced. Input digest checks guard
promotion; an intentionally invalid FFprobe path failed refresh and left the existing XLSX
byte-identical. Temporary staging from that negative test was removed.

Read-only rendering of the saved ImportExcel workbook covered the overview alignment summary,
direct/estimated/unsupported Episode 1 rows, both alignment tabs, manual supplements and headers
plus initial rows for all 26 episode tabs. Visual inspection found readable labels and distinct
timing/availability states. Native-viewer feedback subsequently passed as recorded above.
No source-video extraction, new image survey, CSV migration or Phase 3.2A work occurred.

### Stage 4 commands

Run with PowerShell 7 and installed ImportExcel; close Excel's workbook before refresh if locked.
Use executable paths appropriate to the current host. No dependencies are installed automatically.

```powershell
./tools/reference-extraction/build_category_workbook.ps1 -Python <python.exe-path>
./tools/reference-extraction/build_category_workbook.ps1 -Python <python.exe-path> -VerifyAlignmentMedia -FFprobe <ffprobe.exe-path>
python tools/reference-alignment/projection.py --output .tmp/alignment-report.json
python tools/reference-alignment/projection.py --output .tmp/alignment-report.json --verify-current --ffprobe <ffprobe.exe-path>
```

Projection outputs must remain inside repository `.tmp/`. Routine refresh neither decodes media
nor downloads/restores archived galleries. Explicit verification needs its registered inputs
available; failure preserves the existing workbook. Workbook values represent the last refresh,
not continuous monitoring. No additional permanent workbook or projection CSV is created.

## Stage 5 cleanup and reproduction results — 2026-10-27

**Status:** implementation and bounded pilot validation passed; Stages 4–5 and the integrated
procedure were accepted and confirmed by the maintainer on 2026-10-27. No episode review or
Phase 3.2A work was started by Stage 5.

`finish.py` adds a default read-only deletion preview for one episode. It validates the maintained
registers and inventories only owned `ALNRUN-<32 lowercase hex digits>` directories beneath the
resolved `reference/working/alignment/EP-NN/` boundary. Unknown entries, active runs, symlinks,
Windows reparse points and unsafe paths are refused. Nonstandard files inside a run block removal
because they may contain unique review material. Source media, gallery originals, supplements,
contact sheets, caches and workbooks are outside this deletion boundary.

Registered-result eligibility requires a durable assessed row for every run image, matching run
manifest digest, input/image identity, role, search bounds and the complete retained recipe.
Accepted frame hashes must also match the decoded files. Unresolved CANDIDATE rows block routine
cleanup. AMBIGUOUS/NO_MATCH/REJECTED assessments remain legitimate durable outcomes; cleanup does
not promote them or require a passing model. Registry validation checks referenced model history
and votes independently. Missing source media does not destroy historical record validity.

`--keep-output` explicitly retains output and reports eligibility/blockers. An unregistered failed
or abandoned completed run can be named with `--discard-run`; that decision is distinct from
validated-result cleanup. Discard refuses registered evidence and cannot bypass unexpected-file
checks. Apply requires the exact inspected preview SHA-256. That digest covers run inventories,
file bytes, register bytes and locator bytes; changes require a fresh preview. Search and registry
writer locks are held during recheck/deletion. All runs are preflighted before deletion begins.
Deletion is sequential rather than a filesystem transaction: an OS/lock failure is reported and
remaining output is retained; inspect a fresh preview before retrying. A successful rerun on an
empty episode is harmless. Preview creates only the existing one-byte writer lock files.

`reproduce.py` verifies one accepted anchor against current registered inputs, checks the retained
FFmpeg version, and regenerates its recorded native-frame seek window (at most one second).
It parses the saved seek/duration rather than executing stored command text. Every retained
accepted PNG hash must match; source modification during the operation is refused. Its private
`.tmp/alignment-reproduction/` child directory is removed after success or failure. This proves
decoded-frame reproducibility with the pinned decoder; it does not repeat visual interpretation
or claim another FFmpeg build will produce byte-identical PNGs.

### Validation evidence

The complete alignment suite passed **64 tests**, with the actual FFmpeg synthetic decode enabled.
The 15 added Stage 5 tests cover preview/keep/apply, idempotence, unchanged evidence/out-of-boundary
media, stale file/register tokens, missing/unresolved assessments, changed manifests/frames,
registered-discard refusal, explicit failed/abandoned discard, invalid/unknown paths and states,
reparse-guard refusal, OS deletion failure/retry, unexpected unique files, decoder-version mismatch,
bounded reproduction, frame-hash mismatch and cleanup after interrupted decoding. Reparse refusal
is simulated at the path guard; these tests do not claim elevated Windows junction creation.

Live validation ran after the original seven search runs had already been removed. All eight
accepted Episode 1 anchors reproduced successfully: **188 decoded frames across eight one-second
windows matched all 16 retained accepted-frame hashes**. Each window's temporary images/logs were
removed immediately. Anchor IDs were `ALNANC-000005`, `000008`, `000009`, `000011`, `000016`,
`000017`, `000019` and `000020` (all with the `ALNANC-` prefix).

A fresh bounded single-image search for image `846859` created disposable run
`ALNRUN-68a2f73af1304c0e8ff80c04693c7764`. Its unregistered candidate was correctly ineligible for
routine result cleanup. Keep-output retained it; explicit unregistered-discard preview/apply then
removed **75 files / 50,214,352 bytes**. No assessment or mapping was added. Registered-result
deletion was exercised by deterministic fixtures; the live new run exercised unregistered discard.
An empty-episode apply also passed. The final workspace contains no ALNRUN directories or
reproduction child outputs. **33 index/register/subtitle inputs were byte-identical** before and
after the pilot. The 25-anchor/two-mapping register still validates, and the explicit current-media
check passed as `VERIFIED_CURRENT_EP01` after cleanup. The bounded mapping and uncertainty did not change.

### Episode alignment procedure — accepted 2026-10-27

1. Prepare the authorized episode's verified gallery inputs/contact sheets, website context and
   pinned subtitle copy through the owning episode workflow. Read existing anchors, model limits
   and unresolved work. Do not reuse another release's or episode's timing parameters.
2. Validate maintained records. Request an explicit current-input verification before treating a
   saved mapping as current; absent archived inputs require verified restoration, not silent reuse.
   Unsupported regions stay unmapped. Narrative-only context can still be reviewed without a match.
3. Where authorized and necessary, declare FIT/HOLDOUT roles before bounded searches. Visually
   assess candidates, retain identities, PTS, recipes, rationale and unsuccessful/ambiguous results.
   Freeze model coefficients before independent validation. Do not widen extraction automatically.
4. Refresh the existing category workbook, checking direct intervals separately from estimates
   and original player/web labels. Use estimates only to navigate; verify the actual scene and
   surrounding subtitle intervals before making substantive dialogue/image associations.
5. Before pruning gallery originals at episode completion, validate durable records and perform
   any required current-media/reproduction checks. Preview alignment cleanup. Resolve missing
   provenance or explicitly keep output for open review; discard unregistered runs only deliberately.
6. Inspect the preview's exact runs, eligibility and byte counts, then apply its digest. Check that
   eligible outputs are gone and records still validate. Do not put reproducible alignment frames
   in the episode RAR. Archive gallery originals/supplements and retain contact sheets through the
   separately accepted gallery retention procedure; then record the checkpoint and unresolved scope.

```powershell
python tools/reference-alignment/models.py validate --current --ffprobe <ffprobe.exe-path>
python tools/reference-alignment/reproduce.py --anchor-id <accepted-anchor-id> --ffmpeg <ffmpeg.exe-path> --ffprobe <ffprobe.exe-path>
python tools/reference-alignment/finish.py --episode 1
python tools/reference-alignment/finish.py --episode 1 --keep-output
python tools/reference-alignment/finish.py --episode 1 --apply --preview-sha256 <inspected-preview-digest>
# Unregistered discard: include the same exact run selection in preview and apply.
python tools/reference-alignment/finish.py --episode 1 --discard-run <exact-unregistered-ALNRUN-id>
python tools/reference-alignment/finish.py --episode 1 --discard-run <exact-unregistered-ALNRUN-id> --apply --preview-sha256 <inspected-preview-digest>
```

The ordered episode workflow integrates timing preparation and cleanup per episode, rather than
requiring full-show alignment before reviews resume. No additional batch, episode,
installation, modeling or phase execution follows automatically. At Stage 5 acceptance, search,
registration, source verification and reproduction retained the bounded Episode 1 pilot restriction.
The explicit all-episode extension below replaces that execution restriction; historical pilot
evidence and episode-specific validation limits remain unchanged.

## All-episode extension — 2026-10-28

Status: implemented and tested; accepted by the maintainer on 2026-10-28. The historical Episode 1 pilot
commands remain available for reproduction. Routine episode work uses an explicit `--plan`.
Supporting another episode does not authorize extracting it or establish its alignment.

### Declared selection plan

One JSON plan names exactly one `episode_id` from EP-01 through EP-26. It contains 1–354 distinct
gallery image IDs with predeclared LEAD/FIT/HOLDOUT roles and explicit local search bounds.
A command selects **1–5 IDs from that plan**. A plan is metadata, not an instruction to decode
every entry. Unknown fields, duplicate IDs, invalid roles, episode disagreement, undeclared
selections and invalid bounds are rejected. Gallery membership and source identity are checked
against the selected episode's existing inputs before decoding. Each window is positive,
at most 12 seconds and inside the local media duration; windows are never silently widened.

Example from the live Episode 2 tool check, using LEAD roles only:

```json
{
  "schema_version": 1,
  "episode_id": "EP-02",
  "selections": [
    {"image_id": "847151", "role": "LEAD", "search_start_seconds": "184", "search_end_seconds": "196"},
    {"image_id": "847191", "role": "LEAD", "search_start_seconds": "329", "search_end_seconds": "341"}
  ]
}
```

Bounds accept rational strings or decimal strings and are retained as exact rationals.
The run recipe retains the canonical plan digest and selected declarations, so assessed anchors
retain their roles, bounds and reproducibility metadata after temporary-output cleanup.
Declare FIT/HOLDOUT roles before searches and freeze coefficients before independent validation.
Recorded FIT/HOLDOUT image roles cannot be swapped in later runs. LEAD checks cannot validate
a model. Failed, repeated or ambiguous images retain their proper status.

```text
python tools/reference-alignment/alignment.py search --episode 2 --plan <declared-plan.json> --image-id 847151 --image-id 847191 --ffmpeg <ffmpeg.exe> --ffprobe <ffprobe.exe> --mask 0,204,320,240
python tools/reference-alignment/models.py record --episode 2 --run-id <ALNRUN-id> --assessments <reviewed-assessments.json> --ffprobe <ffprobe.exe>
python tools/reference-alignment/models.py validate --current --episode 2 --ffprobe <ffprobe.exe>
```

Pass `--episode` explicitly when registering routine episode assessments; omission preserves the
old Episode 1 default for historical commands. `propose` derives the episode from its checked
anchors, rather than from a fixed Episode 1 value. Its existing FIT-only coefficients, frozen
proposal, independent HOLDOUT gates, bounded segment coverage and source checks remain in force.
`validate --episode` scopes current-media verification only; table validation still covers the
whole register. Without that filter, explicit current verification checks every recorded episode
and fails on unavailable or stale required inputs rather than silently skipping them.

Reproduction derives the episode from its accepted anchor; cleanup already takes `--episode`.
Both keep their existing hash checks, ownership, resource limits and cleanup gates. The workbook
builder's overview guidance now points to episode-specific mapping records instead of a fixed
Episode 1 formula. No maintained CSV schema, original locator field or historical timing value
was changed. The 900-frame, 600 MiB, 15-minute and 70-second total window caps remain unchanged.

### Validation and retained limits

- All **69 alignment tests passed**, with installed FFmpeg enabled; none were skipped.
  Plan contract tests cover all 26 episode IDs and invalid declarations. Synthetic end-to-end
  tests exercise Episode 2 and Episode 26 assessment registration, frozen FIT proposal,
  independent HOLDOUT validation, current verification and provenance-gated cleanup. Additional
  tests cover mixed-episode verification, stale gallery digests, Episode 26 projection and
  bounded hash reproduction without leaking estimates into an unmapped Episode 2.
- The live Episode 2 search selected gallery 025/847151 and 065/847191 as LEAD only. It checked
  the pinned source/subtitle inputs and decoded **143 frames over 26 requested window seconds**,
  including refinement. Both comparison sheets and their displayed neighbors were visually
  inspected. The expected case and arm-repair scenes were found, but both candidates reported
  BROAD_SCORE_REGION. No unique timing anchor or model was accepted from this tool check.
- Run `ALNRUN-11341c78396e4b56abeb43fc82faa69c`, input
  `f0ba53a3817ca06cc96b8208637c425df8c1ca07e27ead05fc2f763f260785ca`, used the Episode 2
  CBM source identified in the [preparation record](../../reference/indexes/episode-02-context-preparation.md).
  Video SHA-256: `df89f10afd35450152692a093df92fb91bed62ed044480af321a936dea5e5acb`;
  ASS SHA-256: `681eb5c7927e7c90c0fef83c699872f3a66db8afae55eef735a697909404f8bd`;
  locator SHA-256: `4ed16b437fcd21af2626a5aa52bc7a24a4f91b202acd59f7be5cd1b6c4c1e66e`.
  Stream 0 uses time base 1/1000 and origin 0; English ASS stream 4 is media-relative.
  Plan digest: `53fc47845fa3f149164258271f7a98750ba2105c750e8ee904d701864b60a932`.
  FFmpeg/FFprobe version: 9.0.1 essentials build; Python 3.12.14, Pillow 12.3.0.
- The reviewed cleanup preview explicitly classified the run as an **unregistered discard**,
  not validated-result cleanup. Applying preview
  `a15a9f5f4ae9ca21dd68350bf122454b284bcc284faa20ed78578abe8efc3a9e` removed
  **150 files / 124,591,657 bytes**. Directory absence and unchanged alignment/annotation table
  hashes were checked afterward. This deliberately preserves no accepted timing from the run.

The extension supports per-episode execution; actual matching quality and timing relationships
must still be established for each episode/release. At this extension checkpoint, Episode 2
was unmapped and its annotations were UNREVIEWED. Subsequent episode-specific execution and
coverage belong to the [Episode 2 alignment review](../../reference/indexes/episode-02-alignment-review.md),
not this tool-validation record. Phase 3.2A remains unstarted.
