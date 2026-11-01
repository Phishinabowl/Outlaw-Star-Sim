# Episode 7 Timing Alignment

Status: implemented, verified and accepted by the maintainer on 2026-11-01.
ALNMAP-000014 supplies bounded navigation for the pinned Episode 7 release. The
[context preparation](../preparation/episode-07-context-preparation.md) owns source/subtitle identity
and the full dialogue read. Annotated gallery review remains unstarted.

## Selection And Method

The [selection plan](episode-07-alignment-plan.json) declared five FIT images (ordinals 008,
034, 158, 273, 349) and six HOLDOUT images (019, 036, 162, 275, 318, 352) before searches.
Each local window uses the web label ±6 seconds as an unverified seed. No other episode's
offset was reused. Four commands searched three, two, three and three images within the
existing per-command resource and media-window limits.

Coarse search and native-PTS refinement used scoring mask `0,204,320,240`, retaining 85% of
the normalized scoring image. All eleven comparison sheets, displayed neighboring frames and
competing clusters were visually assessed. The six frames spanning the accepted street-action
interval were inspected across the comparison sheet and additional native views. Scores rank
candidates and do not establish matches automatically. Held/repeated drawings retain ambiguity.

Three accepted FIT anchors froze an OFFSET proposal in ALNMAP-000013 before any HOLDOUT
search. Independent validation preserved those votes and coefficients; ALNMAP-000014 supersedes
that proposal. The original missing-HOLDOUT diagnostic remains historical, not a final failure.

## Reviewed Anchors

Anchor suffixes use ALNANC-. Local seconds refer to the pinned media axis.

| Suffix | Ordinal | Role | Result | Local seconds / limit |
| --- | --- | --- | --- | --- |
| 000106 | 008 | FIT | MATCHED | 127.669–127.711; opening jump, missile and jagged shadow. |
| 000107 | 034 | FIT | AMBIGUOUS | Pilot expression and warning-overlay composition persist across a broad region. |
| 000108 | 158 | FIT | MATCHED | 682.473–682.515; toppled limbs, hand and cushion. |
| 000109 | 273 | FIT | MATCHED | 1107.732–1107.940; short airborne action interval, silhouettes, weapon and coat. |
| 000110 | 349 | FIT | AMBIGUOUS | Bloodied glove composition persists for roughly two seconds. |
| 000111 | 019 | HOLDOUT | NO_MATCH | No corresponding XGP hull view secured in the declared opening window; best candidate is a different Gene/firearm shot. Cause unresolved. |
| 000112 | 036 | HOLDOUT | MATCHED | 231.273–231.314; keypad, fingers and cuff. |
| 000113 | 162 | HOLDOUT | AMBIGUOUS | Near-identical impact drawings occur in competing temporal clusters. |
| 000114 | 275 | HOLDOUT | AMBIGUOUS | Street/body composition persists too broadly for a unique narrow interval. |
| 000115 | 318 | HOLDOUT | MATCHED | 1274.273–1274.315; brief entry pose, hair, arms, coat and bag. |
| 000116 | 352 | HOLDOUT | MATCHED | 1399.982–1400.024; slumped head, harness and arm before the next changed pose. |

All six accepted matches are short corresponding intervals rather than claims of pixel identity.
Four ambiguous attempts and one unsuccessful attempt supply no fit/validation votes or direct times.

## Validated Navigation And Limits

Three FIT and three independent HOLDOUT matches pass the established OFFSET gates:

- Exact offset **-131/100 s**: `local = web - 1.310 s`, scale 1.
- Half-open web-label domain **[129,1402)**, or **02:09–23:21 inclusive**.
- Ordinals **008–352** have navigation coverage: **six direct intervals and 339 estimates**.
  Ordinals 001–007 and 353–354 remain **UNMAPPED**, nine images in total.
- Maximum FIT interval error **0.175 s**; median HOLDOUT interval error **0.375 s**;
  maximum HOLDOUT interval error **0.376 s**; widest accepted interval **0.208 s**.
- Suggested navigation half-window **2 s**. These residuals are measured sample results, not
  a universal error bound or exact subtitle/frame association.

**Opening exception:** ordinal 019 retains NO_MATCH. The projection still supplies its domain-based
estimate, **02:48.690**, separately from its empty direct-match fields and NO_MATCH anchor status.
That estimate must not be used to claim the gallery hull shot occurs there. Separate local-shot
inspection is required before a timed association. No cause such as a changed opening edit is
established. Matching other opening/story anchors supports bounded navigation but does not prove
that every sampled gallery shot exists in this release or that every unsampled edit is absent.

The checks span opening material, early simulation, the middle story before/after the transition
to maintenance, later combat and the ending scene. They do not establish complete shot-boundary
equivalence or justify extrapolation into the opening narration, uncovered edges, ending song or
next-episode preview. No LINEAR model or broader search was required.

Input identity: `1ffa633ebad19629a2222f5a66b94b46581315a5481c9124011ab166c91a259d`.
The [anchor register](../../../animehistory/alignment-anchors.csv) retains source/image/locator hashes,
actual PTS and time bases, commands, versions, scoring mask, declared roles/windows and plan digest,
reviewed frame hashes and assessment rationale. Stream 0 has time base 1/1000 and media origin 0;
English ASS stream 4 is media-relative. Original locator and annotation fields remain unchanged.

## Subtitle Context Checks

Two separated checks reuse inspected search frames and the prepared subtitle copy:

- The keypad interval **231.273–231.314 s** lies within cue 57 at **230.86–231.95 s**, the
  tentative control-selection question during simulation recovery. This supports scene navigation;
  no specific key function, reactor wiring or speaker identity is inferred from proximity alone.
- The entry pose **1274.273–1274.315 s** lies within cue 281 at **1272.23–1274.60 s**, the
  surprised question on returning to Melfina. This supports the return scene without assigning
  dialogue to every surrounding gallery frame or establishing a complete building layout.

No original-Japanese wording, dub transcript, character identity or machinery specification is
independently verified by timing alignment.

## Verification And Retention

Episode-scoped current-input verification passed **VERIFIED_CURRENT_EP07** before and after
search-output cleanup. Reproduction of ALNANC-000106 decoded 24 frames and reproduced both
retained hashes; ALNANC-000116 decoded 23 frames and reproduced both retained hashes.
Reproduction output was removed immediately.

All earlier 105 anchor rows and twelve mapping-history rows remain identical. All 413 protected
file hashes match their baseline, covering gallery/sheets, original locator and annotation data,
current context tables/workbook, Episode 7 preparation/metadata and the subtitle copy. The current
media verification separately checks the pinned video and subtitle identity.

The refreshed ImportExcel category workbook preserves 30 sheets, 9,204 gallery rows and 26 manual
references. Saved-data checks passed for 432,588 gallery cells, 9,204 image links, 1,326 manual
cells and 4,902 alignment cells. Global timing counts are 55 DIRECT_MATCH, 2,249 MAPPING_ESTIMATE
and 6,900 UNMAPPED. Changed Episode 7 timing/boundary, anchor, mapping and overview ranges were
rendered and visually inspected. Routine workbook availability remains RECORDED_UNCHECKED;
explicit current verification is separate. No fresh native Office Viewer check is claimed.

The inspected cleanup preview removed all four registered runs: **849 files / 618,899,703 bytes**.
Preview digest: `3308ab5420c2ca08054d69a5194b9e07f6d5e367121767dd29b39f681c997cb6`.
A subsequent preview reports no runs and zero removable bytes. Durable provenance remains in the
registers; reproducible alignment images are not added to the episode RAR. Task-owned assessments,
baseline/projection and workbook-preview helpers are removed after verification.

All 354 gallery originals and 15 contact sheets remain available. No gallery prune, archive,
context-to-image link or image annotation is included. Next separate step: the first three
contact sheets, ordinals 001–072, with the context and timing limits above. Episode 8 and Phase
3.2A remain unstarted.
