# Episode 5 timing alignment

Status: implemented, verified and accepted by the maintainer on 2026-10-30 (America/New_York).
ALNMAP-000010 provides bounded navigation coverage for the pinned Episode 5 release.
The preceding [context preparation](episode-05-context-preparation.md), gallery data and earlier
episodes' records are preserved. Image annotation and Phase 3.2A remain unstarted.

## Selection and method

The [selection plan](episode-05-alignment-plan.json) predates all searches. FIT ordinals:
001, 094, 163, 228, 328 and 353. HOLDOUT ordinals: 011, 078, 154, 181, 235, 334 and 354.
Windows use each whole-second web label plus/minus six seconds as an unverified search seed;
no earlier episode's offset is inherited. Four completed runs searched three or four images
each within the existing resource bounds. No source or gallery file was modified.

Uncropped gallery/candidate comparisons, competing score regions and displayed native neighbors
were visually inspected for all 13 attempts. The accepted 181 interval's start frame was checked
separately. Coarse sampling and native-PTS refinement used the explicit subtitle-region mask
`0,204,320,240`, retaining 85% of the scoring image. Scores rank candidates; they do not accept
anchors. Compression/color differences are not pixel identity. Broad held/repeated drawings
remain ambiguous even when their best scores are high.

Three supported FIT matches froze ALNMAP-000009 before any HOLDOUT search. Four independent
HOLDOUT matches then validated identical coefficients in ALNMAP-000010, superseding the proposal.
The proposal's missing-holdout gate diagnostic remains historical, not a failure of the final model.

## Reviewed anchors

Anchor suffixes use ALNANC-. Local seconds refer to the pinned media axis.

| Suffix | Ordinal | Role | Result | Local seconds / limit |
| --- | --- | --- | --- | --- |
| 000079 | 001 | FIT | MATCHED | 101.768; moving XGP, exhaust, credits and nebula. |
| 000080 | 094 | FIT | AMBIGUOUS | Held crew/Gene hand-to-shoulder composition spans a broad region. |
| 000081 | 163 | FIT | MATCHED | 686.811–686.853; running Aisha pose, hands, legs, braid and alley framing. |
| 000082 | 228 | FIT | MATCHED | 921.546–921.587; raised-arm strike pose, hair and mouth. |
| 000083 | 328 | FIT | AMBIGUOUS | Held Gene/Jim composition and repeating mouth animation. |
| 000084 | 353 | FIT | AMBIGUOUS | Repeated dishwashing pose, bubbles and expression. |
| 000085 | 011 | HOLDOUT | MATCHED | 137.888; two ships, relative angles, exhaust and nebula. |
| 000086 | 078 | HOLDOUT | AMBIGUOUS | Held shaving composition; top mouth drawing differs. |
| 000087 | 154 | HOLDOUT | AMBIGUOUS | Raised-arm crew composition persists with repeated facial drawings. |
| 000088 | 181 | HOLDOUT | MATCHED | 751.459–751.793 short pose interval; Gene leaning and Melfina's hand on his shoulder. |
| 000089 | 235 | HOLDOUT | MATCHED | 946.737–946.821; Gene lean, eyes, mouth and shoulders. |
| 000090 | 334 | HOLDOUT | AMBIGUOUS | Held launch-platform view and recurring small lights. |
| 000091 | 354 | HOLDOUT | MATCHED | 1376.500–1376.542; Aisha close-up, fist, mouth and background. |

The OFFSET model passes the established count, interval-width and residual gates:

- Exact offset **-154/125 s**: `local = web - 1.232 s`, with scale 1.
- Half-open web-label domain **[103,1379)**: **01:43–22:58 inclusive**.
- All **354 gallery labels** fall inside coverage: **seven direct matched intervals and 347
  estimate-only rows**. Ambiguous attempts receive estimates, never direct times.
- Maximum FIT interval error **0.181 s**; median HOLDOUT interval error **0.060 s**;
  maximum HOLDOUT interval error **0.226 s**; widest accepted interval **0.334 s**.
- Suggested navigation half-window **2 s**. Measured residuals are not a universal error bound
  or exact-frame prediction. No extrapolation outside this domain is supported.

FIT 163 precedes the sampled mid-episode break at 171–173; HOLDOUT 181 and FIT 228 follow it.
The checks support the same offset across that region, without proving the absence of every
unsampled edit. Coverage of all sampled labels does not align the unsampled introductory narration,
ending credits, preview or entire video runtime. Recheck actual footage/subtitles when navigation
reveals a mismatch. The six ambiguous attempts remain available as durable records.

Input identity: `b58dffe00b3d6674ad5d4504b5696e9fb5b7d571431699df117c16d36d71368d`.
The context-preparation record owns the pinned source/video/subtitle metadata. The
[anchor register](animehistory/alignment-anchors.csv) retains source/image/locator hashes, PTS,
time bases, command/mask recipes, tool versions, plan digest/declarations and assessment rationale.
Original generated locator times and annotation fields are unchanged.

## Subtitle-context checks

Input inspection rechecked the pinned source/subtitle identity and first-three subtitle-packet
starts. English ASS stream 4 is media-relative; video stream 0 uses time base 1/1000 and origin 0.
Two separated windows used the already inspected search frames and prepared full subtitle copy:

- Cues 197–199, **683.09–690.78 s**, cover the escape and pursuit. The matched running Aisha
  drawing at **686.811–686.853 s** falls inside cue 198's **685.56–687.35 s** pursuit call.
  This supports scene navigation, without assigning a speaker solely from subtitle proximity.
- Cues 365–366, **1371.21–1378.65 s**, cover the restaurant-work aftermath. The matched Aisha
  close-up at **1376.500–1376.542 s** falls inside cue 366's **1376.21–1378.65 s** final threat.
  This does not establish every action in the dishwashing sequence or exact spoken-language wording.

No original-Japanese audio, English-dub transcript, machinery behavior, power scale or character
identity is independently verified by timing alignment.

## Verification and retention

`models.py validate --current --episode 5` passed as VERIFIED_CURRENT_EP05 before and after
temporary-output cleanup. Reproduction of ALNANC-000079 decoded 24 frames and reproduced its
retained hash; ALNANC-000091 decoded 23 frames and reproduced both retained hashes. Both temporary
reproduction directories were removed immediately. Earlier 78 anchor rows and eight mapping-history
rows are unchanged. All 53 protected non-alignment file hashes matched their baseline, including
context tables/workbook, category/supplement/locator data, subtitle provenance/copy and all Episode 5
contact sheets/registry. The pending context-preparation document is unchanged.

The ImportExcel category workbook preserves 30 sheets, 9,204 gallery rows and ten supplements.
Checks compared 432,588 gallery cells, 9,204 image links, 510 manual cells and 3,819 alignment cells.
Global timing counts are 42 DIRECT_MATCH, 1,594 MAPPING_ESTIMATE and 7,568 UNMAPPED.
Rendered first/last Episode 5 timing views, new anchor/mapping rows and overview were visually
inspected. Routine workbook timing availability remains RECORDED_UNCHECKED; the explicit current
verification above is separate. No fresh native Office Viewer test is claimed. The context workbook
needs no further refresh because its inputs and media availability are unchanged.

The inspected finish preview removed all four registered run directories, totaling **996 files /
776,723,199 bytes**. Preview digest:
`73c8d5c55263d8f1d0f7412218de1377047d728941e192174da89efacd408792`.
A subsequent preview reports no runs and zero removable bytes. The durable records retain the
recipes needed after cleanup; no reproducible search PNGs enter the episode RAR. Disposable
assessment and workbook-QA helpers are removed after final checks.

All 354 gallery originals and 15 contact sheets remain available for the upcoming annotated
survey. No Episode 5 RAR, gallery prune, image annotation or context-to-image link is added here.
Next separate step: the first three contact sheets, ordinals 001–072, with context and supported
navigation timing. No later episode or Phase 3.2A starts automatically.
