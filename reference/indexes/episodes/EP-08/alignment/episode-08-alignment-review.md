# Episode 8 Timing Alignment

Status: implemented, verified and accepted by the maintainer on 2026-11-01 (local).
ALNMAP-000016 supplies bounded navigation for the pinned Episode 8 release. The
[context preparation](../preparation/episode-08-context-preparation.md) owns source/subtitle
identity and the full dialogue read. Gallery review remains unstarted.

## Selection And Method

The [initial plan](episode-08-alignment-plan.json) declared five FIT images (002, 124, 231,
347, 354) and six HOLDOUT images (019, 134, 223, 239, 352, 353) before searches. Each window
uses the web label ±6 seconds as an unverified seed. No other episode's offset was reused.
Two FIT runs searched three and two images. Three usable FIT anchors froze ALNMAP-000015
before HOLDOUT searches; the initial missing-HOLDOUT diagnostic is retained historically.

Two initial HOLDOUT runs searched three images each. Five of the six attempts remained
ambiguous because of held/repeated drawings or competing clusters. A separate
[HOLDOUT extension](episode-08-alignment-holdout-extension.json) declared 039, 235 and 305
before their search. It adds independent validation candidates without changing FIT votes,
coefficients, thresholds or earlier assessments. Two of these three were usable. The five
commands remained within the existing per-command resource and media-window limits.

All fourteen comparison sheets, displayed native neighbors and competing clusters were
visually assessed. Coarse/refined searches used scoring mask `0,204,320,240`, retaining 85%
of the normalized scoring image. Scores rank candidates; they do not establish matches.
Compression and minor framing differences remain distinct from pixel equality.

## Reviewed Anchors

Anchor suffixes use ALNANC-. Local seconds refer to the pinned media axis.

| Suffix | Ordinal | Role | Result | Local seconds / limit |
| --- | --- | --- | --- | --- |
| 000117 | 002 | FIT | MATCHED | 105.439; brief Gene pose, blue foreground and jagged background. Adjacent poses differ. |
| 000118 | 124 | FIT | MATCHED | 548.047; mech limbs, torso and red-ended cable align in a brief drawing. |
| 000119 | 231 | FIT | AMBIGUOUS | Countdown five persists across roughly 0.8 s. |
| 000120 | 347 | FIT | AMBIGUOUS | Jim pointing beside the instrument panel repeats over several seconds. |
| 000121 | 354 | FIT | MATCHED | 1382.506–1382.590; short rear-XGP/planet/ring/flare interval, with minor animation differences. |
| 000122 | 019 | HOLDOUT | AMBIGUOUS | Rear headband/ponytail composition repeats across roughly 1.8 s. |
| 000123 | 134 | HOLDOUT | AMBIGUOUS | Melfina profile and mouth variants persist across a broad region. |
| 000124 | 223 | HOLDOUT | AMBIGUOUS | Countdown 29 persists across roughly 0.9 s. |
| 000125 | 239 | HOLDOUT | AMBIGUOUS | Gene/sky view has competing clusters and changed framing. |
| 000126 | 352 | HOLDOUT | AMBIGUOUS | Gene cockpit smile repeats across several seconds. |
| 000127 | 353 | HOLDOUT | MATCHED | 1378.919; rear ship/planet composition without the white flare visible in both immediate neighbors. |
| 000128 | 039 | HOLDOUT | AMBIGUOUS | Dark group composition persists across roughly 7.5 s. |
| 000129 | 235 | HOLDOUT | MATCHED | 950.783; engine bells, launch structure and smoke contours. |
| 000130 | 305 | HOLDOUT | MATCHED | 1204.745; brief diagonal combat drawing with central strike marks; adjacent drawings differ. |

Five matches identify corresponding drawings and one identifies a short corresponding shot
interval. None claims pixel identity. Eight ambiguous assessments supply no direct timing,
fit or holdout vote. Their domain-based navigation estimates remain separate from these results.

## Validated Navigation And Limits

Three FIT and three independent HOLDOUT matches pass the established OFFSET gates:

- Exact offset **-363/250 s**: `local = web - 1.452 s`, scale 1.
- Half-open web-label domain **[107,1385)**, or **01:47–23:04 inclusive** for the gallery labels.
- Ordinals **002–354** have navigation coverage: **six direct matches and 347 estimates**.
  Ordinal 001 remains **UNMAPPED**. No extrapolation into the uncovered opening edge.
- Maximum FIT interval error **0.499 s**; median HOLDOUT interval error **0.235 s**;
  maximum HOLDOUT interval error **0.371 s**; widest accepted interval **0.084 s**.
- Suggested navigation half-window **2 s**. These are sampled residuals, not a universal
  error bound or exact subtitle/frame association for every gallery image.

ALNMAP-000016 supersedes the frozen proposal ALNMAP-000015 with unchanged FIT votes and
coefficients. Whole-second web labels constrain estimated precision. Samples cover opening,
ground attack, launch, orbital combat and final departure; they do not prove every intervening
shot or edit is identical. No LINEAR fit or whole-episode frame extraction was needed.

Input identity: `f2b615d53f3eba23384966c1d214ca107bc86e0c28c5d7aa33d429ce2bfd6fcc`.
The [anchor register](../../../animehistory/alignment-anchors.csv) retains source/image/locator
hashes, PTS/time bases, commands/versions, masks, declared roles/windows, plan digests, reviewed
frame hashes and assessment rationale. Video stream 0 has time base 1/1000 and media origin 0;
English ASS stream 4 is media-relative. Source SHA-256 is
`073135780d8bbceebd37885ccda8f5bf1168e92ae3d014fb43acc502963a1bd1`.

## Subtitle Context Checks

- Opening match **105.439 s** falls within prepared lyric cue 26, **101.80–110.60 s**.
  This supports opening navigation and lyric placement; it is not present-day story dialogue.
- Departure match **1378.919 s** falls within story cue 298, **1378.29–1381.26 s**, the
  farewell to Sentinel III. This supports the final departure scene without identifying a
  particular drive state from subtitle proximity alone.

No Japanese transcription, dub wording, speaker identification, mechanism or performance
specification is independently verified by timing alignment.

## Verification And Retention

Episode-scoped current-input verification passed **VERIFIED_CURRENT_EP08** before and after
search-output cleanup. Reproduction of
ALNANC-000117 decoded 24 frames and reproduced its retained hash. ALNANC-000130 decoded 23
frames and reproduced its retained hash. Reproduction output was removed immediately.

All earlier 116 anchor rows and fourteen mapping-history rows remain identical. All 414
protected file hashes match the pre-alignment baseline, covering gallery/sheets, original
locator/annotation/supplement data, current context tables/workbook, Episode 8 preparation,
targeted evidence metadata and subtitle copy. Current-media verification separately checks
the pinned video and subtitle identity. Context preparation and this alignment checkpoint
were accepted together on 2026-11-01.

The existing ImportExcel category workbook was refreshed, preserving 30 sheets, 9,204 gallery
rows and 26 manual references. Saved-data checks passed for 432,588 gallery cells, 9,204 image
links, 1,326 manual cells and 5,502 alignment cells. Global timing counts are 61 DIRECT_MATCH,
2,596 MAPPING_ESTIMATE and 6,547 UNMAPPED. Affected Episode 8 timing, anchor, mapping and overview
ranges were rendered and visually inspected. Routine browsing
availability is RECORDED_UNCHECKED; explicit current verification is separate. No fresh native
Excel/Office Viewer check is claimed. Gallery annotations and locator web labels are unchanged.

The inspected cleanup preview covers five registered runs: **1,097 files / 737,395,877 bytes**.
Preview digest: `4f5bbf69735ea47abc4baa2f0bd8b8960ac2945e089431d771bc66a4a4133462`.
Validated-result cleanup removed all five runs after durable provenance retention. No alignment
images were added to the episode RAR. A final preview reports no runs and zero removable bytes,
digest `5957c2d0b94cb2c5cd62eccba5397b8b7b4dcdc36a039c76e4f8a2e4f4cd3fbe`.
Task-owned assessment/projection/baseline and workbook-preview scratch was removed after checks.

All 354 gallery originals and 15 sheets remain available. Next separate step: first three
contact sheets, ordinals 001–072. No gallery archive/prune, image annotation, context-to-image
link, later episode work or Phase 3.2A implementation is included.
