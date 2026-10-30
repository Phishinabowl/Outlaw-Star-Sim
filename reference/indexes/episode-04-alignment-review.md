# Episode 4 timing alignment

Status: implemented, verified and accepted by the maintainer on 2026-10-29.
ALNMAP-000008 provides bounded navigation coverage for the pinned Episode 4 release.
The accepted earlier survey and context-preparation changes are preserved.
The subsequent [reconciliation sweep](episode-04-reconciliation-review.md) records annotation/context
updates and final retention; those were outside this alignment checkpoint. Phase 3.2A remains unstarted.

## Selection and method

The [initial plan](episode-04-alignment-plan.json) predates candidate searches. FIT ordinals:
001, 004, 065, 148, 174, 190, 256, 318 and 354. HOLDOUT ordinals: 011, 095, 169, 180, 287 and 353.
Search bounds are unverified whole-second web labels plus/minus six seconds, without inheriting
another episode's offset. Five supported FIT matches froze ALNMAP-000007 before any HOLDOUT
search. The [validation plan](episode-04-alignment-validation-plan.json) added HOLDOUT 002/352;
the later [edge plan](episode-04-alignment-edge-plan.json) added HOLDOUT 342/351. Each addition
predates its searches, retains unsuccessful attempts and leaves FIT coefficients unchanged.

Seven completed runs searched 1–4 selected images each within existing frame/disk/time bounds.
One premature search failed before decoding because gallery restoration was still in progress;
it was explicitly discarded during cleanup. Coarse sampling and native-PTS refinement use mask
`0,204,320,240`, retaining 85% of the scoring picture. Uncropped gallery/candidate comparisons,
clusters and displayed native neighbors were inspected for all 19 attempts. Scores rank candidates
only; held/repeated drawings do not establish precise timing from score alone.

## Reviewed anchors

Anchor suffixes use ALNANC-. Seconds follow the pinned local media axis.

| Suffix | Ordinal | Role | Result | Local seconds / limit |
| --- | --- | --- | --- | --- |
| 000060 | 001 | FIT | AMBIGUOUS | Held opening Gene drawing. |
| 000061 | 004 | FIT | MATCHED | 112.738–112.779; running pose, missile and explosion. |
| 000062 | 065 | FIT | AMBIGUOUS | Held crew/cockpit composition. |
| 000063 | 148 | FIT | MATCHED | 639.305; Melfina pose, hair and floating background. |
| 000064 | 174 | FIT | AMBIGUOUS | Held hangar/XGP drawing. |
| 000065 | 190 | FIT | MATCHED | 792.875; distinctive Gene muzzle flash. |
| 000066 | 256 | FIT | MATCHED | 1034.075; Harry hand/body and Ron framing. |
| 000067 | 318 | FIT | MATCHED | 1260.885; XGP tilt, arms, exhaust and background. |
| 000068 | 354 | FIT | AMBIGUOUS | Small ship/nebula lacks distinctive frame evidence. |
| 000069 | 011 | HOLDOUT | MATCHED | 138.388; Melfina turn and petals. |
| 000070 | 095 | HOLDOUT | AMBIGUOUS | Repeated Gilliam drawing over broad region. |
| 000071 | 169 | HOLDOUT | MATCHED | 716.132; Jim, wall and maintenance unit. |
| 000072 | 180 | HOLDOUT | AMBIGUOUS | Competing repeated combat-effect clusters. |
| 000073 | 287 | HOLDOUT | MATCHED | 1147.521–1147.563; Gene mouth/head and framing. |
| 000074 | 353 | HOLDOUT | AMBIGUOUS | Repeated/held open-mouth Gene portrait. |
| 000075 | 002 | HOLDOUT | AMBIGUOUS | Held filmstrip layout over broad region. |
| 000076 | 352 | HOLDOUT | AMBIGUOUS | Closed-mouth Gene drawing persists for seconds. |
| 000077 | 342 | HOLDOUT | MATCHED | 1348.639; XGP position, stellar corona and exhaust. |
| 000078 | 351 | HOLDOUT | AMBIGUOUS | Held Gilliam close-up. |

ALNMAP-000008 supersedes the frozen proposal with identical coefficients. Five FIT and four
independent HOLDOUT matches pass the existing OFFSET gates:

- Exact offset **-2483/2000 s**: `local = web - 1.2415 s`.
- Half-open web-label domain **[114,1351)**: **01:54–22:30 inclusive**.
- Gallery **004–342**: **nine direct intervals and 330 estimates**. Gallery **001–003 and
  343–354 remain unmapped**. Ambiguous attempts inside coverage receive estimates, not direct matches.
- Maximum FIT interval error **0.6835 s**; median HOLDOUT error **0.283 s**;
  maximum HOLDOUT error **0.3735 s**; widest accepted interval **0.042 s**.
- Navigation half-window **2 s**. Observed residuals are not a universal error bound or
  exact-frame predictions. No extrapolation, drift or absence of unobserved edits is established.

FIT 148 precedes the sampled mid-episode break at 176–178; FIT 190 follows it. The supported
matches show no unexplained discontinuity across that region, without verifying every frame.
The ten ambiguous attempts are retained. Nine manual supplements keep their original player-time
leads and unresolved archive associations; this model does not reconcile them automatically.

Input identity: `0e207719605c497f5a2ca9ec8b5dbe72a370cde879ee2ddc1bffedde68cf5410`.
The [context preparation](episode-04-context-preparation.md) owns pinned video/subtitle provenance.
The [anchor register](animehistory/alignment-anchors.csv) retains PTS, hashes, commands, masks,
tool versions, plan declarations/digests and reproduction recipes. Original web labels are unchanged.

## Subtitle-context checks

Pinned input identity and first-three-cue packet starts were rechecked. English ASS stream 4 is
media-relative; video stream 0 has time base 1/1000 and origin 0. No original-Japanese audio or
English-dub wording check is claimed. Two separated windows used already decoded search frames:

- Cues 160–168, **619.93–650.56 s**: repeated connection attempts, connection established/engine
  activation, then crew reactions. PTS **636010, 640014, 644018** show Melfina with closed eyes,
  Melfina with open eyes, then Gene/Jim in the cockpit. Accepted 148 at 639.305 s falls inside
  cue 165, but subtitle proximity alone does not establish speaker identity or system mechanics.
  Frames belong to ALNRUN-dcf0d7d4daa5487eb94b5bd9ca4a8e4a.
- Cues 318–322, **1256.65–1266.82 s**: urgency to Hilda, output counts 85–87, then a call to Hilda.
  PTS **1258007, 1261010, 1265014** show Gene, XGP exterior and Hilda on the tether. Accepted 318
  at 1260.885 s falls during output count 86; the exterior is not treated as an on-screen speaker.
  Frames belong to ALNRUN-bf38787d4239486ea6d7e6c3bcb51232.

These checks support scene navigation, not full motion choreography or stronger technical claims.

## Verification and retention

`models.py validate --current --episode 4` passed as VERIFIED_CURRENT_EP04 before and after
alignment-output cleanup. Reproduction of ALNANC-000061 decoded 24 frames and reproduced both
retained frame hashes; ALNANC-000077 decoded 23 frames and reproduced its retained hash. Both
temporary reproduction directories were removed. Fifty-four protected non-alignment input hashes
match the baseline, including category/supplement data, locators, context tables, context-preparation
record, contact sheets and archive/receipt. Earlier 59 anchors and six mapping-history rows are unchanged.

The ImportExcel category workbook preserves 30 sheets, 9,204 gallery rows and ten supplements.
Validation compared 432,588 gallery cells, 9,204 hyperlinks, 510 manual cells and 3,258 alignment
cells. The context workbook refresh preserves five sheets, 9,406 cells and 1,743 links; its local
manual-image availability reflects restoration. Routine timing projections remain RECORDED_UNCHECKED;
the explicit current-media verification above is separate. No new native-viewer test is claimed.
Rendered overview, direct/estimate and uncovered-edge views, new anchor/mapping rows and the
context availability summary were visually inspected.

The inspected finish preview removed eight owned run directories: seven registered runs and the
failed empty search, totaling **1,523 files / 1,111,216,828 bytes**. Preview digest:
`027e1a5af377241eaa6aa5f18927d24b70e331ed75b63882d02ccb8735157b2a`.
No Episode 4 alignment search output remains. Disposable assessment/QA helpers are removed after
verification. The verified RAR and all 15 contact sheets are unchanged. The restored 354 gallery
images and nine supplements remain available for the separate reconciliation sweep; they require
the established archive/prune step afterward. This is not a new completed episode-retention checkpoint.
