# Episode alignment tool — proposal

**Status — 2026-10-27:** proposal confirmed and published as `10678c8`. Stage 1's data contract
and bounded test design are defined below. Stage 2's bounded candidate matcher is implemented
and tested against the five declared Episode 1 images, with comparison sheets visually inspected.
Maintained alignment CSVs, timing-model fitting and workbook integration remain unimplemented.
Stages 3–5 require scoped continuation. No all-episode extraction or retrospective verification
is implied. Changes following `10678c8` remain pending confirmation.

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

The Stage 2 prototype already provides explicit `cleanup --episode ... --run-id ...`, which
deletes the entire named owned run. It does **not** yet check maintained alignment records or
perform the planned episode-finish preview/provenance gate. Its retained Episode 1 pilot run is
still needed for the current review; this retention decision does not authorize deleting it now.

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

Proposal publication, Stage 1 contract design and the bounded Stage 2 matcher pilot are complete
within their recorded scopes. Stage 1 used metadata only; Stage 2 added the executable, synthetic
tests, selected-video hashing, bounded decoding, candidate comparison and duplicate-run cleanup
documented below. No maintained alignment CSV initialization, accepted anchors, fitted model,
timing-field change or workbook integration has occurred. Stages 3–5 remain unstarted.

## Stage 1 data contract v1

This section is authoritative for the new alignment records; the existing image-index README
continues to own survey fields. It specifies later implementation, not currently available commands.
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

Exact ordered header for later initialization:

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

Exact ordered header for later initialization:

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

The final run took **13.344 s**, saved **381 decoded PNGs**, and occupied **285,988,256 bytes**
(about **272.74 MiB**) after final manifest writing. Initial search coverage was 60 s; the sum
of initial/refinement window widths was 66 s, a conservative upper bound on their union and
within the 70 s cap. The duplicate earlier run was removed through `cleanup`; the retained
run remains local and ignored for review. Synthetic test fixtures are removed automatically.

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

Cleanup validates the explicit resolved run path, run ID, owner manifest and descendants before
recursive removal. It cannot delete a gallery cache, source directory or arbitrary path. This
section records prototype behavior and validation; it is not yet the accepted integrated procedure.
