# Episode 6 timing alignment

Status: implemented, verified and accepted by the maintainer on 2026-10-30 (America/New_York).
ALNMAP-000012 supplies bounded navigation for the pinned Episode 6 release. The
[context preparation](episode-06-context-preparation.md) owns source/subtitle identity and
the full dialogue read. Gallery annotation and Phase 3.2A remain unstarted.

## Selection and method

The [selection plan](episode-06-alignment-plan.json) initially declared six FIT images
(ordinals 002, 036, 165, 277, 324, 350) and seven HOLDOUT images
(004, 030, 180, 192, 280, 344, 354) before any search. After the initial late HOLDOUTs
proved ambiguous, ordinal 348 was added as another HOLDOUT before its own search.
The four accepted FIT votes and their coefficients were already frozen in ALNMAP-000011;
neither those votes nor coefficients were changed to accommodate HOLDOUT results.
Each run retains the canonical declaration used at its execution, including the plan digest.

Search windows use each web label plus/minus six seconds as an unverified seed, without
inheriting another episode's offset. Five runs searched three, three, four, three and one
images respectively. Each command stayed within the existing 1–5-image, frame/disk/time
and media-window limits. Coarse/native-PTS refinement used subtitle-region scoring mask
`0,204,320,240`, retaining 85% of the scoring image. All 14 comparison sheets, competing
regions and displayed native neighbors were visually inspected. Scores rank candidates;
they do not accept matches. Short supported holds retain intervals; broad repeated or
unclear content remains ambiguous. Correspondence does not mean pixel identity.

## Reviewed anchors

Anchor suffixes use ALNANC-. Local seconds refer to the pinned media axis.

| Suffix | Ordinal | Role | Result | Local seconds / limit |
| --- | --- | --- | --- | --- |
| 000092 | 002 | FIT | MATCHED | 105.439; opening jump, missile and shadow geometry. |
| 000093 | 036 | FIT | MATCHED | 229.020–229.062; short ship/platform/cloud interval. |
| 000094 | 165 | FIT | AMBIGUOUS | Shield-clash pose persists; changing arcs/hair do not secure a narrow corresponding interval. |
| 000095 | 277 | FIT | MATCHED | 1105.521; top-down duel and distinctive branching arcs. |
| 000096 | 324 | FIT | MATCHED | 1276.442; walking figures, limbs, coat and rocks. |
| 000097 | 350 | FIT | AMBIGUOUS | Held car composition and repeated mouth/eye drawings. |
| 000098 | 004 | HOLDOUT | AMBIGUOUS | Opening ship hold with tint/exhaust changes and differing best-candidate exhaust. |
| 000099 | 030 | HOLDOUT | MATCHED | 207.249; rear ship/cloud/exhaust geometry. |
| 000100 | 180 | HOLDOUT | MATCHED | 752.752; falling fragments, rotating chair, picture and dust. |
| 000101 | 192 | HOLDOUT | AMBIGUOUS | Multi-second city panorama and small rooftop figure. |
| 000102 | 280 | HOLDOUT | MATCHED | 1116.324–1116.407; short duel pose, hands, sword, hair and cloth. |
| 000103 | 344 | HOLDOUT | AMBIGUOUS | Held close-up over another figure's shoulder. |
| 000104 | 354 | HOLDOUT | AMBIGUOUS | Slow framing change against the moon does not securely narrow a direct interval. |
| 000105 | 348 | HOLDOUT | AMBIGUOUS | Additional declared late check; car composition and small repeated facial changes persist. |

Four FIT and three independent HOLDOUT matches pass the established OFFSET gates:

- Exact offset **-3037/2000 s**: `local = web - 1.5185 s`, scale 1.
- Half-open web-label domain **[107,1279)**, or **01:47–21:18 inclusive**.
- Ordinals **002–324** have navigation coverage: **seven direct intervals and 316 estimates**.
  Ordinal 001 and final ordinals 325–354 remain **UNMAPPED**: 31 images in total.
- Maximum FIT interval error **0.5385 s**; median HOLDOUT interval error **0.2325 s**;
  maximum HOLDOUT interval error **0.2705 s**; widest accepted interval **0.083 s**.
- Suggested navigation half-window **2 s**. These measured residuals are not a universal
  error bound or an exact subtitle/frame association.

ALNMAP-000011 is retained as the superseded FIT-only proposal. Its missing-HOLDOUT diagnostic
is historical, not a failure of the final model. Seven ambiguous attempts remain durable
records; none supplies a model vote or direct time. The accepted votes span early landing,
middle action and later exterior action, without proving the absence of every unsampled edit.
The late held-shot checks did not justify extending coverage. Narrative context remains usable
outside coverage, but those images need separate local-shot checks before timed associations.

Input identity: `80a145a8f49193cf15eeda7d6c6fab19c983a91a3d4b700f979c15a5d41b4177`.
The [anchor register](animehistory/alignment-anchors.csv) retains source/image/locator hashes,
PTS/time bases, commands, tool versions, mask recipes, declaration digests and review rationale.
Video stream 0 has time base 1/1000 and media origin 0; English ASS stream 4 is media-relative.
Original generated locator times and image annotation fields remain unchanged.

## Subtitle-context checks

Two separated checks reuse inspected search frames and the prepared full subtitle copy:

- The matched landing view at **229.020–229.062 s** lies after the engine/strut deployment
  exchange and before cue 57 at **231.68–233.31 s**. This is a silent action interval; the
  nearest line is not assigned to the frame or used to infer an unstated strut mechanism.
- The matched duel interval at **1116.324–1116.407 s** falls inside cue 270's
  **1115.23–1116.59 s** exclamation during the duel. This supports scene navigation,
  without inferring a speaker from proximity or a measured shield behavior.

No original-Japanese audio, English-dub transcript, character identity or machinery
specification is independently verified by timing alignment.

## Verification and retention

`models.py validate --current --episode 6 --ffprobe <installed executable>` passed
VERIFIED_CURRENT_EP06 before and after temporary cleanup. Reproduction of ALNANC-000092
decoded 24 frames and reproduced one retained hash; ALNANC-000102 decoded 23 frames and
reproduced all three retained hashes. Reproduction output was removed immediately.
All earlier 91 anchor rows and ten mapping-history rows remain identical. All 383 protected
file hashes matched their baseline, including current context tables/workbook, preparation
record, category/supplement/locator data, subtitle copy/provenance and gallery/sheet files.

The refreshed ImportExcel category workbook preserves 30 sheets, 9,204 gallery rows and
26 manual references. Saved-data checks passed for 432,588 gallery cells, 9,204 image links,
1,326 manual cells and 4,419 alignment cells. Global timing counts are 49 DIRECT_MATCH,
1,910 MAPPING_ESTIMATE and 7,245 UNMAPPED. Changed Episode 6 timing/boundary, anchor, mapping
and overview ranges were rendered and visually inspected. Routine workbook availability
remains RECORDED_UNCHECKED; the explicit current-input verification is separate. No fresh
native Office Viewer check is claimed. The context workbook required no refresh here.

The inspected cleanup preview removed all five registered run directories: **1,047 files /
769,808,022 bytes**. Preview digest:
`a2381088c398f9bc339a9b00ca729d6a1a9a5cedb8ea0cda459961130239c198`.
A subsequent preview reports no runs and zero removable bytes. Durable records preserve
reproduction provenance; reproducible search images are not added to the episode RAR.
Disposable assessment, baseline and workbook-preview helpers are removed after verification.

All 354 gallery originals and 15 contact sheets remain available. No gallery prune, RAR,
image annotation or context-to-image link is added here. Next separate step: the first
three contact sheets, ordinals 001–072, using context and the stated navigation limits.
No later episode or Phase 3.2A starts automatically.
