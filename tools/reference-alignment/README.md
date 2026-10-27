# Episode alignment tool — proposal

**Status — 2026-10-27:** direction and staged development approach agreed; proposal documented.
No alignment tool, maintained alignment tables, fitted timing model or workbook integration is
implemented by this increment. Stage execution requires its own scoped continuation. Episode 1
is the initial pilot; no all-episode extraction or retrospective verification is implied.

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
Finalize exact ordered fields and vocabulary in Stage 1 before initialization.

| Location | Proposed role |
| --- | --- |
| `tools/reference-alignment/` | This proposal, later bounded matching/model/validation commands and tests. Reuse existing gallery/source helpers where appropriate; do not duplicate episode download or RAR tools. |
| `reference/indexes/animehistory/alignment-anchors.csv` | Authored alignment evidence: selected gallery image keys and visually checked local frame/shot matches, including ambiguity and failed attempts. |
| `reference/indexes/animehistory/alignment-mappings.csv` | Authored episode/release/segment mappings, supporting and independent validation anchors, fitted parameters, applicability and verification limits. |
| `reference/indexes/animehistory/category-review.xlsx` | Existing generated ImportExcel workbook; later alignment-anchor/mapping tabs and joined timing fields. No additional workbook or editable spreadsheet authority. |
| `reference/working/alignment/EP-NN/<run-id>/` | Ignored, owned temporary search frames, comparison sheets, candidate scores and execution metadata. Bounded by selected images/windows and recorded resource limits. |
| Existing gallery cache / RAR and subtitle copies | Read-only inputs at their existing locations. Restore selected gallery inputs through the gallery tool when needed; do not reorganize or duplicate collections. |

Stage 1 must define these record requirements:

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
do not delete gallery originals, registered supplements, source videos, subtitle copies or cited
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

Proposal only. No executable, CSV initialization, video/ASS processing, frame extraction,
screenshot copying, timing-field change, source hash computation, workbook change or cleanup
operation was performed for this proposal. The first authorized implementation increment is
Stage 1; a later accepted pilot is required before routine use.
