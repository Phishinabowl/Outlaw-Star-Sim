# Episode 3 timing alignment

Status: implemented, verified and accepted by the maintainer on 2026-10-28.
ALNMAP-000006 provides bounded navigation coverage for the pinned Episode 3 release.
Image annotations remain unchanged; Phase 3.2A remains unstarted.

## Predeclared selection and method

The [initial selection plan](episode-03-alignment-plan.json) predates all candidate searches.
FIT ordinals: 001, 002, 083, 146, 196, 214, 285 and 351. Independent HOLDOUT ordinals:
009, 095, 160, 202, 287 and 354. Initial search bounds are each unverified web label plus/minus
six seconds, not an inherited Episode 1 or 2 offset. Contact sheets were inspected to select
motion/framing leads only; this did not annotate or classify gallery rows.

After initial FIT inspection and before fitting or any HOLDOUT search, the
[boundary plan](episode-03-alignment-boundary-plan.json) added FIT ordinals 340 and 352.
The original late silhouetted ship view remained ambiguous; these additional selections seek
distinctive late movement without replacing the failed attempt or relaxing eligibility gates.

Five runs searched 1–4 explicitly selected images each, within the existing frame/disk/time
bounds. Coarse sampling and native-PTS refinement used the existing comparison method and mask
`0,204,320,240`, retaining 85% of the 320×240 scoring picture. Uncropped gallery/candidate views,
candidate clusters and displayed native neighbors were inspected for all 16 attempts. Scores
rank candidates only; broad or repeated drawings were not accepted by score alone. Original
web labels remain whole-second navigation inputs, not exact-frame times.

## Reviewed anchors

Anchor suffixes use the ALNANC- prefix. Local seconds follow the pinned media-relative time axis.

| Suffix | Ordinal | Role | Result | Supported interval / limit |
| --- | --- | --- | --- | --- |
| 000044 | 001 | FIT | AMBIGUOUS | Held opening drawing; broad matching region. |
| 000045 | 002 | FIT | MATCHED | 105.439 s; running pose, explosion and wall alignment. |
| 000046 | 083 | FIT | AMBIGUOUS | Docked ship composition with intermittent effect. |
| 000047 | 146 | FIT | AMBIGUOUS | Similar ship/exhaust drawings over a broad region. |
| 000048 | 196 | FIT | MATCHED | 810.893–810.935 s; ship/debris and impact shapes. |
| 000049 | 214 | FIT | MATCHED | 876.417 s; ship, streak/background and exhaust alignment. |
| 000050 | 285 | FIT | MATCHED | 1134.592 s; ship angle and background/exhaust alignment. |
| 000051 | 351 | FIT | AMBIGUOUS | Nearly stationary silhouette against stellar background. |
| 000052 | 340 | FIT | MATCHED | 1334.625 s; fast ship position and blur configuration. |
| 000053 | 352 | FIT | MATCHED | 1378.252 s; moving foreground framing relative to doorway. |
| 000054 | 009 | HOLDOUT | MATCHED | 130.839–130.881 s; hair, petals and body pose. |
| 000055 | 095 | HOLDOUT | MATCHED | 443.652–443.693 s; seated figures' head/hand positions. |
| 000056 | 160 | HOLDOUT | MATCHED | 679.846–680.013 s; full short exhaust/rock shot interval before a cut. |
| 000057 | 202 | HOLDOUT | AMBIGUOUS | Station composition persists beyond 0.5-second eligibility limit. |
| 000058 | 287 | HOLDOUT | MATCHED | 1141.891 s; missile and smoke/launcher configuration. |
| 000059 | 354 | HOLDOUT | AMBIGUOUS | Similar closed-mouth portraits; numerical cluster is insufficient. |

Six FIT observations froze ALNMAP-000005 at `local = web - 1.4845 s` before any HOLDOUT search.
Its PROPOSED state correctly lacked independent validation. ALNMAP-000006 supersedes that
proposal without changing coefficients. Six FIT and four independent HOLDOUT observations pass
the existing OFFSET gates:

- Exact offset: **-2969/2000 s**, or **web time minus 1.4845 s**.
- Half-open web-label domain **[107,1381)**: **01:47 through 23:00 inclusive**.
- Gallery **002–352** receives navigation coverage: ten direct intervals and 341 estimates.
  **001 and 353–354 remain unmapped**; ambiguous attempts within coverage receive estimates
  rather than fabricated direct matches.
- Maximum FIT interval error **0.3775 s**; median HOLDOUT interval error **0.327 s**;
  maximum HOLDOUT interval error **0.3755 s**; widest accepted interval **0.167 s**.
- Suggested navigation half-window **2 s**. These observed residuals are not a universal error
  bound, exact-frame predictions or proof that no unobserved edit exists. No drift is asserted.

FIT 196 precedes the sampled mid-episode break at 198–200; FIT 214 follows it. HOLDOUT 202 was
retained as ambiguous. The checked samples show no unexplained timing discontinuity across that
region, without claiming frame-by-frame verification of the break or entire episode.

Input identity: `1af64b5d29c70f18555941954adb7d729d32d8dbd1653b6c59d3b0551ec483a8`.
The [preparation record](episode-03-context-preparation.md) owns the video/subtitle hashes and
read scope. The [anchor register](animehistory/alignment-anchors.csv) retains exact PTS, hashes,
commands, masks, software versions, plan declarations/digests and accepted-frame hashes for
reproduction after cleanup. Failed/ambiguous selections remain durable records.

## Subtitle-context checks

Input inspection rechecked the pinned media/subtitle identity and bounded first-three-cue packet
starts. English ASS stream 4 is media-relative; video stream 0 uses time base 1/1000 and origin 0.
No original-Japanese audio or English-dub wording verification is claimed.

Two separated windows were checked using existing decoded search frames, with no further video
extraction or permanent transcript:

- **Cues 112–116, 436.20–452.18 s:** firing instructions followed by Melfina's auxiliary-control
  assignment. PTS **440023, 444277, 448031** show Gene/Melfina seated, then Hilda at the control
  chair during that assignment. The accepted 095 interval lies in the intervening dialogue gap;
  it is not assigned a spoken line merely because of proximity. These frames belong to
  ALNRUN-b48bd87a52ea41ab8583021a4745fb67.
- **Cues 355–356, 1371.74–1376.40 s**, with the following reaction shot: PTS
  **1376041, 1377793, 1380045** show the ship/asteroid against the star, then Gene behind Hilda
  in the cockpit. Accepted 352 at 1378.252 s follows the final acknowledgement, rather than
  falling inside it. These frames belong to ALNRUN-41e5727bb7cf414b9bde197c52d91c11.

The checks support scene navigation and guard against attaching nearby lines to silent images.
They do not establish speaker identity from empty subtitle Name fields, engineering dimensions,
full motion choreography or stronger technical claims.

## Verification, workbook and cleanup

`models.py validate --current --episode 3` passed as VERIFIED_CURRENT_EP03. Reproduction of
ALNANC-000045 and ALNANC-000053 decoded 24 and 23 frames respectively and reproduced each
retained accepted-frame hash; both temporary reproduction directories were removed.
Existing Episode 1 and 2 anchor/mapping records remain unchanged.

The existing ImportExcel workbook refreshed with 9,204 gallery rows, ten supplements and all
30 sheets preserved. Checks compared 432,588 gallery cells, 9,204 image hyperlinks, 510 manual
cells and 2,463 alignment cells. Rendered overview, Episode 3 direct/estimate and uncovered-edge
views, plus new anchor/mapping rows, were visually inspected. Direct intervals and estimates
remain separate. Routine workbook generation labels timing RECORDED_UNCHECKED; the explicit
VERIFIED_CURRENT_EP03 check above is a separate operation, repeated successfully after cleanup.
No new native Excel/Office Viewer test is claimed.

Applying the inspected finish preview removed five eligible registered runs containing
1,271 files / 945,585,294 bytes. Preview digest:
`42340a7b4b639b3e3682d3fb5db399a6867488e2c0d36522378c84f2fe010484`.
Only owned reproducible alignment frames/comparison output were removed; no Episode 3 search
runs or candidate frames remain. Gallery originals, contact sheets, supplements, subtitles and
cited website caches follow their separate policies. Thirty-three non-alignment input hashes
match the baseline, including category/supplement tables, all gallery locators and four context
CSVs. All earlier 43 anchors and four mapping-history rows remain unchanged. Disposable
assessment/QA helpers and previews are removed after these checks.

All 354 Episode 3 annotation rows remain UNREVIEWED / NOT_REVIEWED. The first 001–072 image
review is a separate step; this alignment does not start it or Phase 3.2A automatically.
