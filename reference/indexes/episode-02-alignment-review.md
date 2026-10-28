# Episode 2 timing alignment

Status: implemented and verified; accepted by the maintainer on 2026-10-28.
ALNMAP-000004 provides bounded navigation coverage for the pinned Episode 2 release.
Phase 3.2A remains unstarted. Image annotations remain unchanged.

## Predeclared selection and method

The [initial plan](episode-02-alignment-plan.json) was recorded before candidate searches.
FIT gallery ordinals: 010, 034, 072, 144, 216, 288, 348.
Independent HOLDOUT ordinals: 018, 108, 180, 252, 330.
Each initial search uses the unverified web label plus/minus six seconds as a search lead only.
Episode 1 timing is not reused. Roles remain fixed; extra attempts must be declared separately
and unsuccessful/ambiguous original selections retained.

The existing tool bounds, reviewed-interval width gate, FIT-only coefficients, frozen proposal
and independent HOLDOUT validation gates apply. The selection spans opening and early/middle/late
story, but does not establish absence of edits or coverage outside successfully checked labels.
Repeated drawings cannot establish unique times by top score alone. Missing coverage remains
unmapped. The prior two-image tool check supplied no accepted anchors or mapping.

Before model fitting or HOLDOUT matching, the [boundary plan](episode-02-alignment-boundary-plan.json)
adds FIT ordinals 001 and 354 to test the sampled gallery endpoints. The two original sparse
portrait matches and static arm/station views retain their individual uncertainty; endpoint
checks do not replace failed selections or relax model gates.

## Frozen proposal and supplementary independent checks

ALNMAP-000003 freezes four precise FIT observations (ALNANC-000026/031/032/033) at
`local = web - 1.286 s` before any HOLDOUT candidate search. Maximum FIT interval error is
0.330 s; maximum accepted interval width is 0.042 s. At that FIT checkpoint the proposal was
unvalidated. The other five FIT attempts remain AMBIGUOUS.

The initial HOLDOUT set supplied one precise animated-effect match (108) and four held/repeated
or ambiguous views (018/180/252/330). The full comparison sheets and displayed native neighbors
were inspected; a high score alone did not promote any broad candidate region.

The [supplementary HOLDOUT plan](episode-02-alignment-holdout-plan.json) declares 177, 185, 249
and 312 before their searches. They were selected from contact-sheet motion/effect leads,
including either side of the mid-episode break. No local candidate or model residual was
consulted to select these images. FIT coefficients remain frozen; all original attempts remain.

## Reviewed anchors and validation

All 18 comparison sheets were inspected with their uncropped gallery views, candidate clusters
and displayed native temporal neighbors. Eight attempts support precise corresponding frames;
ten remain AMBIGUOUS. No ambiguity was resolved by selecting a favorable model residual.

| Anchor suffix | Ordinal | Role | Result | Local interval / ambiguity |
| --- | --- | --- | --- | --- |
| 000026 | 010 | FIT | MATCHED | 134.384 s; moving opening framing |
| 000027 | 034 | FIT | AMBIGUOUS | Held exposed-arm drawing |
| 000028 | 072 | FIT | AMBIGUOUS | Repeated dialogue poses |
| 000029 | 144 | FIT | AMBIGUOUS | Potentially cyclic firing effect |
| 000030 | 216 | FIT | AMBIGUOUS | Held station composition |
| 000031 | 288 | FIT | MATCHED | 1140.639–1140.681 s |
| 000032 | 348 | FIT | MATCHED | 1357.856 s; moving rear pose |
| 000033 | 001 | FIT | MATCHED | 101.768 s; leap/background motion |
| 000034 | 354 | FIT | AMBIGUOUS | Held final sampled shot |
| 000035 | 018 | HOLDOUT | AMBIGUOUS | Held closed-eye gesture |
| 000036 | 108 | HOLDOUT | MATCHED | 489.114 s; animated dragon effect |
| 000037 | 180 | HOLDOUT | AMBIGUOUS | Held break logo |
| 000038 | 252 | HOLDOUT | AMBIGUOUS | Repeated dialogue drawings |
| 000039 | 330 | HOLDOUT | AMBIGUOUS | Held room composition |
| 000040 | 177 | HOLDOUT | MATCHED | 738.821 s; drive effect before break |
| 000041 | 185 | HOLDOUT | MATCHED | 767.809 s; ships/exhaust after break |
| 000042 | 249 | HOLDOUT | AMBIGUOUS | Broad robot/worker composition |
| 000043 | 312 | HOLDOUT | MATCHED | 1227.518 s; fast action pose |

Anchor suffixes above use the ALNANC- prefix. ALNMAP-000004 supersedes the frozen proposal
ALNMAP-000003 without changing its coefficients. Four FIT and four independent HOLDOUTs pass
the existing OFFSET gates:

- **Local seconds = web seconds - 643/500**, or **web time minus 1.286 s**.
- Half-open whole-second web-label domain **[103,1360)**: 01:43 through 22:39 inclusive.
  Gallery **001–348** receives navigation coverage; **349–354 remains unmapped**.
- Maximum FIT interval error **0.330 s**, median HOLDOUT interval error **0.1515 s**,
  maximum HOLDOUT interval error **0.400 s**, maximum accepted interval width **0.042 s**.
- Suggested navigation half-window **2 s**. These measured residuals are not a universal
  error bound or exact-frame predictions. Sparse samples do not establish absence of every
  intervening edit. No drift or LINEAR model is asserted.

Input identity: `f0ba53a3817ca06cc96b8208637c425df8c1ca07e27ead05fc2f763f260785ca`.
The [anchor register](animehistory/alignment-anchors.csv) retains video/subtitle/gallery hashes,
exact PTS/time bases, plan digests, commands, masks, software versions, accepted frame hashes
and review rationale. The [preparation record](episode-02-context-preparation.md) owns the
source profile. Separate initial/boundary/supplementary plan files preserve role declarations.

## Subtitle-context checks

The English ASS is media-relative: video stream 0, time base 1/1000, origin 0; ASS stream 4.
Matching rechecked input identity and the first-three-cue packet timing. This does not verify
original Japanese audio, English-dub wording or every translated subtitle line.

Two separated scene/dialogue windows were checked from already decoded search frames; no
additional extraction or permanent transcript was created:

- Cues **93–96, 353.14–365.98 s**: continued Melfina questioning, the 360-second resuscitation
  announcement and response. PTS **356022, 358024, 360026, 362028** show the weapon pressing
  the repaired hand, then Gene/Hilda. The announcement is off-screen; no visible timer is
  inferred. Locator 072's estimate is 358.714 s, but its exact pose remains ambiguous.
- Cues **306–309, 1134.35–1147.33 s**: outlaw hangout, recruiting help and questions about
  the job. PTS **1138012, 1140014, 1142016, 1144018** show the bar conversation and Gene
  close-up. Accepted locator 288 falls within cue **308, 1140.43–1142.76 s**.

These checks support contextual navigation, not speaker identification from empty subtitle
metadata or broader dialogue/technical claims. The first window belongs to run
ALNRUN-30d4288a48064638a23fb7d1f8c7f3e5; the second to
ALNRUN-6bca1be91a7044f2896c27c007dbf886. Their retained recipes reproduce the selected windows.

## Verification, workbook and retention

`models.py validate --current --episode 2` passed. Bounded reproduction regenerated accepted
hashes for ALNANC-000033 and ALNANC-000041: 24 and 23 decoded frames respectively, with one
retained accepted-frame hash checked per anchor. Both reproduction directories were removed.
Episode 1 records and its separate offset/coverage remain unchanged.

The existing ImportExcel workbook is refreshed: 9,204 gallery rows, ten supplements and 30 sheets
preserved. Validation compared 432,588 gallery cells, 9,204 image links, 510 manual cells and
1,785 alignment cells. Episode 2 has eight direct rows, 340 estimates and six unmapped rows.
Rendered overview, Episode 2 direct/estimate and uncovered-tail views, and the new anchor/mapping
rows were visually inspected. Existing workbook structure and presentation were preserved.
Direct intervals and estimates remain separate. Routine builds honestly label timing records
RECORDED_UNCHECKED; the explicit Episode 2 current-input check above is separate.

All five registered search runs passed durable-assessment/provenance checks. Applying the
inspected finish preview `c12065834708803e0a160592ce4adcbafa9c452835f04e0718bf33f3d8c240fc`
removed **1,396 files / 1,008,059,897 bytes** of candidate frames, comparison sheets and logs.
Retained records own reproduction metadata. Gallery originals and contact sheets follow the
separate episode-review/archive policy. Temporary assessment/QA files are removed after checks.

Category and supplement annotation hashes remain unchanged. Episode 2 annotations remain
UNREVIEWED / NOT_REVIEWED; the first 001–072 batch resumes separately. No other episode matching
or Phase 3.2A work follows automatically.
