# Reference index migration ledger — Phase 1.1

Status: Phase 1.1 inventory accepted by the maintainer on 2026-10-30; moves planned and unimplemented.
Baseline date: 2026-10-30 (America/New_York). This record implements Phase 1.1 of the [plan](reference-index-reorganization-plan.md).

The [baseline JSON](reference-index-reorganization-baseline.json) records exact paths, byte counts, SHA-256 values,
section boundaries/hashes, ordered CSV data digests and per-sheet workbook data/link digests.
Initial Git HEAD: `e7d62d52cd3c74e25e83e8bf6b6bb2f9fe8b7c4e`; worktree clean and upstream aligned.
No migration directories were created. Consumer auditing remains Phase 1.2; entries below do not claim it is complete.

## File dispositions

Paths below are relative to `reference/indexes`. Every row is PLANNED_NOT_MOVED; all destinations were absent.
JSON provenance bytes are to be preserved. For Markdown/CSV, only coordinated active-reference edits are planned;
findings, evidence IDs, historical commands and recorded recipes remain unchanged. Full hashes are in the baseline.

| ID | Existing path | Destination | Producer / record type |
| --- | --- | --- | --- |
| FILE-001 | `episode-01-02-melfina-case-review.md` | `comparisons/episode-01-02-melfina-case-review.md` | Authored research / review record |
| FILE-002 | `episode-01-melfina-case-frames.json` | `episodes/EP-01/evidence/episode-01-melfina-case-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-003 | `episode-01-retention-checkpoint.md` | `episodes/EP-01/survey/episode-01-retention-checkpoint.md` | Authored research / review record |
| FILE-004 | `episode-01-review-batch-02-frames.json` | `episodes/EP-01/evidence/episode-01-review-batch-02-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-005 | `episode-01-review-batch-02.md` | `episodes/EP-01/survey/episode-01-review-batch-02.md` | Authored research / review record |
| FILE-006 | `episode-01-review-batch-03-frames.json` | `episodes/EP-01/evidence/episode-01-review-batch-03-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-007 | `episode-01-review-batch-03.md` | `episodes/EP-01/survey/episode-01-review-batch-03.md` | Authored research / review record |
| FILE-008 | `episode-01-review-batch-04-frames.json` | `episodes/EP-01/evidence/episode-01-review-batch-04-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-009 | `episode-01-review-batch-04.md` | `episodes/EP-01/survey/episode-01-review-batch-04.md` | Authored research / review record |
| FILE-010 | `episode-01-review-batch-05-frames.json` | `episodes/EP-01/evidence/episode-01-review-batch-05-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-011 | `episode-01-review-batch-05.md` | `episodes/EP-01/survey/episode-01-review-batch-05.md` | Authored research / review record |
| FILE-012 | `episode-01-subtitle-context-frames.json` | `episodes/EP-01/evidence/episode-01-subtitle-context-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-013 | `episode-01-subtitle-context-review.md` | `episodes/EP-01/evidence/episode-01-subtitle-context-review.md` | Authored research / review record |
| FILE-014 | `episode-02-alignment-boundary-plan.json` | `episodes/EP-02/alignment/episode-02-alignment-boundary-plan.json` | Authored selection plan / alignment input |
| FILE-015 | `episode-02-alignment-holdout-plan.json` | `episodes/EP-02/alignment/episode-02-alignment-holdout-plan.json` | Authored selection plan / alignment input |
| FILE-016 | `episode-02-alignment-plan.json` | `episodes/EP-02/alignment/episode-02-alignment-plan.json` | Authored selection plan / alignment input |
| FILE-017 | `episode-02-alignment-review.md` | `episodes/EP-02/alignment/episode-02-alignment-review.md` | Authored research / review record |
| FILE-018 | `episode-02-context-preparation.md` | `episodes/EP-02/preparation/episode-02-context-preparation.md` | Authored research / review record |
| FILE-019 | `episode-02-melfina-activation-frames.json` | `episodes/EP-02/evidence/episode-02-melfina-activation-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-020 | `episode-02-melfina-resuscitation-frames.json` | `episodes/EP-02/evidence/episode-02-melfina-resuscitation-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-021 | `episode-02-retention-checkpoint.md` | `episodes/EP-02/survey/episode-02-retention-checkpoint.md` | Authored research / review record |
| FILE-022 | `episode-02-review-batch-01-frames.json` | `episodes/EP-02/evidence/episode-02-review-batch-01-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-023 | `episode-02-review-batch-01.md` | `episodes/EP-02/survey/episode-02-review-batch-01.md` | Authored research / review record |
| FILE-024 | `episode-02-review-batch-02-frames.json` | `episodes/EP-02/evidence/episode-02-review-batch-02-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-025 | `episode-02-review-batch-02.md` | `episodes/EP-02/survey/episode-02-review-batch-02.md` | Authored research / review record |
| FILE-026 | `episode-02-review-batch-03-frames.json` | `episodes/EP-02/evidence/episode-02-review-batch-03-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-027 | `episode-02-review-batch-03.md` | `episodes/EP-02/survey/episode-02-review-batch-03.md` | Authored research / review record |
| FILE-028 | `episode-02-review-batch-04.md` | `episodes/EP-02/survey/episode-02-review-batch-04.md` | Authored research / review record |
| FILE-029 | `episode-02-review-batch-05-frames.json` | `episodes/EP-02/evidence/episode-02-review-batch-05-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-030 | `episode-02-review-batch-05.md` | `episodes/EP-02/survey/episode-02-review-batch-05.md` | Authored research / review record |
| FILE-031 | `episode-03-alignment-boundary-plan.json` | `episodes/EP-03/alignment/episode-03-alignment-boundary-plan.json` | Authored selection plan / alignment input |
| FILE-032 | `episode-03-alignment-plan.json` | `episodes/EP-03/alignment/episode-03-alignment-plan.json` | Authored selection plan / alignment input |
| FILE-033 | `episode-03-alignment-review.md` | `episodes/EP-03/alignment/episode-03-alignment-review.md` | Authored research / review record |
| FILE-034 | `episode-03-context-preparation.md` | `episodes/EP-03/preparation/episode-03-context-preparation.md` | Authored research / review record |
| FILE-035 | `episode-03-retention-checkpoint.md` | `episodes/EP-03/survey/episode-03-retention-checkpoint.md` | Authored research / review record |
| FILE-036 | `episode-03-review-batch-01.md` | `episodes/EP-03/survey/episode-03-review-batch-01.md` | Authored research / review record |
| FILE-037 | `episode-03-review-batch-02.md` | `episodes/EP-03/survey/episode-03-review-batch-02.md` | Authored research / review record |
| FILE-038 | `episode-03-review-batch-03.md` | `episodes/EP-03/survey/episode-03-review-batch-03.md` | Authored research / review record |
| FILE-039 | `episode-03-review-batch-04.md` | `episodes/EP-03/survey/episode-03-review-batch-04.md` | Authored research / review record |
| FILE-040 | `episode-03-review-batch-05.md` | `episodes/EP-03/survey/episode-03-review-batch-05.md` | Authored research / review record |
| FILE-041 | `episode-04-alignment-edge-plan.json` | `episodes/EP-04/alignment/episode-04-alignment-edge-plan.json` | Authored selection plan / alignment input |
| FILE-042 | `episode-04-alignment-plan.json` | `episodes/EP-04/alignment/episode-04-alignment-plan.json` | Authored selection plan / alignment input |
| FILE-043 | `episode-04-alignment-review.md` | `episodes/EP-04/alignment/episode-04-alignment-review.md` | Authored research / review record |
| FILE-044 | `episode-04-alignment-validation-plan.json` | `episodes/EP-04/alignment/episode-04-alignment-validation-plan.json` | Authored selection plan / alignment input |
| FILE-045 | `episode-04-apparatus-details-frames.json` | `episodes/EP-04/evidence/episode-04-apparatus-details-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-046 | `episode-04-cockpit-case-staging-frames.json` | `episodes/EP-04/evidence/episode-04-cockpit-case-staging-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-047 | `episode-04-cockpit-case-staging-review.md` | `episodes/EP-04/evidence/episode-04-cockpit-case-staging-review.md` | Authored research / review record |
| FILE-048 | `episode-04-cockpit-headroom-frames.json` | `episodes/EP-04/evidence/episode-04-cockpit-headroom-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-049 | `episode-04-cockpit-headroom-review.md` | `episodes/EP-04/evidence/episode-04-cockpit-headroom-review.md` | Authored research / review record |
| FILE-050 | `episode-04-context-preparation.md` | `episodes/EP-04/preparation/episode-04-context-preparation.md` | Authored research / review record |
| FILE-051 | `episode-04-corridor-engine-junction-frames.json` | `episodes/EP-04/evidence/episode-04-corridor-engine-junction-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-052 | `episode-04-entry-hall-gilliam-frames.json` | `episodes/EP-04/evidence/episode-04-entry-hall-gilliam-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-053 | `episode-04-entry-hall-review.md` | `episodes/EP-04/evidence/episode-04-entry-hall-review.md` | Authored research / review record |
| FILE-054 | `episode-04-hatch-location-frames.json` | `episodes/EP-04/evidence/episode-04-hatch-location-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-055 | `episode-04-hatch-location-review.md` | `episodes/EP-04/evidence/episode-04-hatch-location-review.md` | Authored research / review record |
| FILE-056 | `episode-04-hilda-laptop-screen-review.md` | `episodes/EP-04/evidence/episode-04-hilda-laptop-screen-review.md` | Authored research / review record |
| FILE-057 | `episode-04-inspection.md` | `episodes/EP-04/preparation/episode-04-inspection.md` | Authored research / review record |
| FILE-058 | `episode-04-metadata.json` | `episodes/EP-04/preparation/episode-04-metadata.json` | inspect_episode.py / stream metadata |
| FILE-059 | `episode-04-motion-transitions-frames.json` | `episodes/EP-04/evidence/episode-04-motion-transitions-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-060 | `episode-04-opening-bootstrap-a-frames.json` | `episodes/EP-04/evidence/episode-04-opening-bootstrap-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-061 | `episode-04-opening-bootstrap-b-frames.json` | `episodes/EP-04/evidence/episode-04-opening-bootstrap-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-062 | `episode-04-opening-bootstrap-detail-frames.json` | `episodes/EP-04/evidence/episode-04-opening-bootstrap-detail-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-063 | `episode-04-opening-bootstrap-review.md` | `episodes/EP-04/evidence/episode-04-opening-bootstrap-review.md` | Authored research / review record |
| FILE-064 | `episode-04-opening-connection-frames.json` | `episodes/EP-04/evidence/episode-04-opening-connection-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-065 | `episode-04-opening-port-458-frames.json` | `episodes/EP-04/evidence/episode-04-opening-port-458-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-066 | `episode-04-opening-port-lead-frames.json` | `episodes/EP-04/evidence/episode-04-opening-port-lead-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-067 | `episode-04-reconciliation-review.md` | `episodes/EP-04/evidence/episode-04-reconciliation-review.md` | Authored research / review record |
| FILE-068 | `episode-04-startup-clearance-frames.json` | `episodes/EP-04/evidence/episode-04-startup-clearance-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-069 | `episode-04-startup-detail-frames.json` | `episodes/EP-04/evidence/episode-04-startup-detail-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-070 | `episode-04-startup-mechanisms-frames.json` | `episodes/EP-04/evidence/episode-04-startup-mechanisms-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-071 | `episode-04-startup-review-frames.json` | `episodes/EP-04/evidence/episode-04-startup-review-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-072 | `episode-04-startup-review.md` | `episodes/EP-04/evidence/episode-04-startup-review.md` | Authored research / review record |
| FILE-073 | `episode-04-unlock-followup-frames.json` | `episodes/EP-04/evidence/episode-04-unlock-followup-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-074 | `episode-04-user-leads-a-frames.json` | `episodes/EP-04/evidence/episode-04-user-leads-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-075 | `episode-04-user-leads-b-frames.json` | `episodes/EP-04/evidence/episode-04-user-leads-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-076 | `episode-05-alignment-plan.json` | `episodes/EP-05/alignment/episode-05-alignment-plan.json` | Authored selection plan / alignment input |
| FILE-077 | `episode-05-alignment-review.md` | `episodes/EP-05/alignment/episode-05-alignment-review.md` | Authored research / review record |
| FILE-078 | `episode-05-context-preparation.md` | `episodes/EP-05/preparation/episode-05-context-preparation.md` | Authored research / review record |
| FILE-079 | `episode-06-alignment-plan.json` | `episodes/EP-06/alignment/episode-06-alignment-plan.json` | Authored selection plan / alignment input |
| FILE-080 | `episode-06-alignment-review.md` | `episodes/EP-06/alignment/episode-06-alignment-review.md` | Authored research / review record |
| FILE-081 | `episode-06-context-preparation.md` | `episodes/EP-06/preparation/episode-06-context-preparation.md` | Authored research / review record |
| FILE-082 | `episode-07-metadata.json` | `episodes/EP-07/preparation/episode-07-metadata.json` | inspect_episode.py / stream metadata |
| FILE-083 | `episode-07-practice-a-frames.json` | `episodes/EP-07/evidence/episode-07-practice-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-084 | `episode-07-practice-b-frames.json` | `episodes/EP-07/evidence/episode-07-practice-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-085 | `episode-07-practice-c-frames.json` | `episodes/EP-07/evidence/episode-07-practice-c-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-086 | `episode-08-departure-a-frames.json` | `episodes/EP-08/evidence/episode-08-departure-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-087 | `episode-08-departure-b-frames.json` | `episodes/EP-08/evidence/episode-08-departure-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-088 | `episode-08-departure-c-frames.json` | `episodes/EP-08/evidence/episode-08-departure-c-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-089 | `episode-08-departure-d-frames.json` | `episodes/EP-08/evidence/episode-08-departure-d-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-090 | `episode-08-metadata.json` | `episodes/EP-08/preparation/episode-08-metadata.json` | inspect_episode.py / stream metadata |
| FILE-091 | `episode-11-metadata.json` | `episodes/EP-11/preparation/episode-11-metadata.json` | inspect_episode.py / stream metadata |
| FILE-092 | `episode-11-recovery-a-frames.json` | `episodes/EP-11/evidence/episode-11-recovery-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-093 | `episode-11-recovery-b-frames.json` | `episodes/EP-11/evidence/episode-11-recovery-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-094 | `episode-11-recovery-c-frames.json` | `episodes/EP-11/evidence/episode-11-recovery-c-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-095 | `episode-11-subether-a-frames.json` | `episodes/EP-11/evidence/episode-11-subether-a-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-096 | `episode-11-subether-b-frames.json` | `episodes/EP-11/evidence/episode-11-subether-b-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-097 | `episode-11-subether-c-frames.json` | `episodes/EP-11/evidence/episode-11-subether-c-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-098 | `episode-11-subether-review.md` | `episodes/EP-11/evidence/episode-11-subether-review.md` | Authored research / review record |
| FILE-099 | `episode-11-transition-detail-frames.json` | `episodes/EP-11/evidence/episode-11-transition-detail-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-100 | `episode-26-metadata.json` | `episodes/EP-26/preparation/episode-26-metadata.json` | inspect_episode.py / stream metadata |
| FILE-101 | `episode-26-platform-locator-frames.json` | `episodes/EP-26/evidence/episode-26-platform-locator-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-102 | `episode-26-platform-review.md` | `episodes/EP-26/evidence/episode-26-platform-review.md` | Authored research / review record |
| FILE-103 | `episode-26-platform-transitions-frames.json` | `episodes/EP-26/evidence/episode-26-platform-transitions-frames.json` | extract_reference_frames.py / extraction provenance |
| FILE-104 | `episode-index.md` | `episodes/episode-index.md` | Authored research / review record |
| FILE-105 | `external-sources.md` | `sources/external-sources.md` | Authored research / review record |
| FILE-106 | `fan-melfina-pod-reference.md` | `supplied-references/fan-melfina-pod-reference.md` | Authored research / review record |
| FILE-107 | `image-map-reconciliation.md` | `comparisons/image-map-reconciliation.md` | Authored research / review record |
| FILE-108 | `passage-entry-level-reconciliation.md` | `comparisons/passage-entry-level-reconciliation.md` | Authored research / review record |
| FILE-109 | `performance-metrics.csv` | `performance/performance-metrics.csv` | Authored research / register |
| FILE-110 | `performance-subtitle-audit.md` | `performance/performance-subtitle-audit.md` | Authored research / review record |
| FILE-111 | `performance-subtitle-coverage.json` | `performance/performance-subtitle-coverage.json` | scan_performance_subtitles.py / subtitle provenance |
| FILE-112 | `settei-collection-review-batch-01.md` | `settei/batches/settei-collection-review-batch-01.md` | Authored research / review record |
| FILE-113 | `settei-collection-review-batch-02.md` | `settei/batches/settei-collection-review-batch-02.md` | Authored research / review record |
| FILE-114 | `settei-collection-review-batch-03.md` | `settei/batches/settei-collection-review-batch-03.md` | Authored research / review record |
| FILE-115 | `settei-collection-review-batch-04.md` | `settei/batches/settei-collection-review-batch-04.md` | Authored research / review record |
| FILE-116 | `settei-collection-review-batch-05.md` | `settei/batches/settei-collection-review-batch-05.md` | Authored research / review record |
| FILE-117 | `settei-collection-review-batch-06.md` | `settei/batches/settei-collection-review-batch-06.md` | Authored research / review record |
| FILE-118 | `settei-collection-review-batch-07.md` | `settei/batches/settei-collection-review-batch-07.md` | Authored research / review record |
| FILE-119 | `settei-collection-review-batch-08.md` | `settei/batches/settei-collection-review-batch-08.md` | Authored research / review record |
| FILE-120 | `settei-collection-review-batch-09.md` | `settei/batches/settei-collection-review-batch-09.md` | Authored research / review record |
| FILE-121 | `settei-collection-review-batch-10.md` | `settei/batches/settei-collection-review-batch-10.md` | Authored research / review record |
| FILE-122 | `settei-collection-review-batch-11.md` | `settei/batches/settei-collection-review-batch-11.md` | Authored research / review record |
| FILE-123 | `settei-collection-review-batch-12.md` | `settei/batches/settei-collection-review-batch-12.md` | Authored research / review record |
| FILE-124 | `settei-collection-review-batch-13.md` | `settei/batches/settei-collection-review-batch-13.md` | Authored research / review record |
| FILE-125 | `settei-collection-review-batch-14.md` | `settei/batches/settei-collection-review-batch-14.md` | Authored research / review record |
| FILE-126 | `settei-collection-review-batch-15.md` | `settei/batches/settei-collection-review-batch-15.md` | Authored research / review record |
| FILE-127 | `settei-collection-review-batch-16.md` | `settei/batches/settei-collection-review-batch-16.md` | Authored research / review record |
| FILE-128 | `settei-collection-review-batch-17.md` | `settei/batches/settei-collection-review-batch-17.md` | Authored research / review record |
| FILE-129 | `settei-collection-review-batch-18.md` | `settei/batches/settei-collection-review-batch-18.md` | Authored research / review record |
| FILE-130 | `settei-collection-review-batch-19.md` | `settei/batches/settei-collection-review-batch-19.md` | Authored research / review record |
| FILE-131 | `settei-collection-review-batch-20.md` | `settei/batches/settei-collection-review-batch-20.md` | Authored research / review record |
| FILE-132 | `settei-collection-review-batch-21.md` | `settei/batches/settei-collection-review-batch-21.md` | Authored research / review record |
| FILE-133 | `settei-collection-review-batch-22.md` | `settei/batches/settei-collection-review-batch-22.md` | Authored research / review record |
| FILE-134 | `settei-collection-review-batch-23.md` | `settei/batches/settei-collection-review-batch-23.md` | Authored research / review record |
| FILE-135 | `settei-collection-review-batch-24.md` | `settei/batches/settei-collection-review-batch-24.md` | Authored research / review record |
| FILE-136 | `settei-collection-review-batch-25.md` | `settei/batches/settei-collection-review-batch-25.md` | Authored research / review record |
| FILE-137 | `settei-collection-review-batch-26.md` | `settei/batches/settei-collection-review-batch-26.md` | Authored research / review record |
| FILE-138 | `settei-collection-review-batch-27.md` | `settei/batches/settei-collection-review-batch-27.md` | Authored research / review record |
| FILE-139 | `settei-collection-review-batch-28.md` | `settei/batches/settei-collection-review-batch-28.md` | Authored research / review record |
| FILE-140 | `settei-collection-review-batch-29.md` | `settei/batches/settei-collection-review-batch-29.md` | Authored research / review record |
| FILE-141 | `settei-collection-review-batch-30.md` | `settei/batches/settei-collection-review-batch-30.md` | Authored research / review record |
| FILE-142 | `settei-collection-review-batch-31.md` | `settei/batches/settei-collection-review-batch-31.md` | Authored research / review record |
| FILE-143 | `settei-collection-review-batch-32.md` | `settei/batches/settei-collection-review-batch-32.md` | Authored research / review record |
| FILE-144 | `settei-collection-review-batch-33.md` | `settei/batches/settei-collection-review-batch-33.md` | Authored research / review record |
| FILE-145 | `settei-interior-review.json` | `settei/reviews/settei-interior-review.json` | Authored structured settei observations |
| FILE-146 | `settei-interior-review.md` | `settei/reviews/settei-interior-review.md` | Authored research / review record |
| FILE-147 | `settei-screening.csv` | `settei/settei-screening.csv` | Authored research / register |
| FILE-148 | `settei-variant-review.md` | `settei/reviews/settei-variant-review.md` | Authored research / review record |
| FILE-149 | `source-manifest.json` | `sources/source-manifest.json` | inventory.py / source inventory |
| FILE-150 | `startup-open-items-followup.md` | `comparisons/startup-open-items-followup.md` | Authored research / review record |
| FILE-151 | `startup-sequence-comparison.md` | `comparisons/startup-sequence-comparison.md` | Authored research / review record |
| FILE-152 | `to-be-continued-supplied-reference.md` | `supplied-references/to-be-continued-supplied-reference.md` | Authored research / review record |

## Embedded README section dispositions

Ranges are inclusive baseline line numbers, ending before the next heading regardless of heading level.
Thus parent sections do not accidentally include or duplicate child-section text. Keep dates and attribution.
Existing detailed batch/context/alignment records remain separate evidence; relocated summaries link to them.
Multiple sections targeting a new history file retain their original ordered headings; no findings consolidation.
For retention records already present in EP-01–03, append the historical summary as a clearly labeled section.
Moved headings leave navigation pointers in the shared README; old fragment aliases may be retained for active consumers.

| ID / lines | Heading | Action / destination | Exception or ownership |
| --- | --- | --- | --- |
| SEC-001 / 1–19 | Local AnimeHistory timestamp index | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-002 / 20–159 | Ordered episode-review workflow | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-003 / 160–177 | Episode 1 preparation — 2026-10-26 | RELOCATE_SECTION: `episodes/EP-01/preparation/episode-01-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-004 / 178–199 | Episode 1 annotated survey — sheets 1–3 | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-005 / 200–236 | Episode 1 subtitle-context follow-up — 2026-10-27 | RELOCATE_SECTION: `episodes/EP-01/evidence/episode-01-subtitle-context-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-006 / 237–244 | Using the records | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-007 / 245–290 | Authored category index and future Power BI view | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-008 / 291–328 | Category-index field contract — version 1 | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-009 / 329–368 | Annotated survey and targeted review depth — accepted 2026-10-26 | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-010 / 369–478 | Initial tag vocabulary | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-011 / 479–495 | Initial validation and review operation | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-012 / 496–545 | Category-index initialization and first screening — 2026-10-26 | SPLIT_MIXED: `animehistory/README.md` | Keep heading and lines 498–512, 538–544 here; move 513–536 into EP-04/survey/episode-04-survey-history.md, retaining dates and original counts. |
| SEC-013 / 546–719 | Episode 4 category survey progress | RELOCATE_SECTION: `episodes/EP-04/survey/episode-04-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-014 / 720–824 | Manual supplemental references | SPLIT_MIXED: `animehistory/README.md` | Keep heading/schema 722–752 and tool notes 819–824 here; move 753–818 into EP-04/evidence/episode-04-supplement-history.md. Fix schema ownership wording only during coordinated migration. |
| SEC-015 / 825–830 | Reproducing the cache/index | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-016 / 831–862 | Workbook refresh and ownership | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-017 / 863–885 | Category workbook alignment view | RETAIN_SHARED: `animehistory/README.md` | Shared workflow/schema/tool ownership retained. |
| SEC-018 / 886–904 | Episode 1 annotated survey — sheets 4–6 (2026-10-27) | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-019 / 905–923 | Episode 1 annotated survey — sheets 7–9 (2026-10-27) | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-020 / 924–943 | Episode 1 annotated survey — sheets 10–12 (2026-10-27) | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-021 / 944–963 | Episode 1 annotated survey — sheets 13–15 | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-022 / 964–980 | Episode 1 retention checkpoint — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-01/survey/episode-01-retention-checkpoint.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-023 / 981–1001 | Episode 2 preparation — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/preparation/episode-02-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-024 / 1002–1016 | Episode 2 bounded alignment — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/alignment/episode-02-alignment-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-025 / 1017–1030 | Episode 2 annotated survey — batch 01, 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-026 / 1031–1044 | Episode 2 annotated survey — batch 02, 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-027 / 1045–1059 | Episode 2 annotated survey — batch 03, 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-028 / 1060–1074 | Episode 2 annotated survey — batch 04, 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-029 / 1075–1089 | Episode 2 annotated survey — batch 05, 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-030 / 1090–1104 | Episode 2 retention checkpoint — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-02/survey/episode-02-retention-checkpoint.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-031 / 1105–1127 | Episode 3 gallery preparation — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-03/preparation/episode-03-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-032 / 1128–1140 | Episode 3 subtitle/context preparation — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-03/preparation/episode-03-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-033 / 1141–1156 | Episode 3 bounded alignment — 2026-10-28 | RELOCATE_SECTION: `episodes/EP-03/alignment/episode-03-alignment-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-034 / 1157–1170 | Episode 3 annotated survey — batch 01, 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-035 / 1171–1181 | Episode 3 annotated survey — batch 02, 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-036 / 1182–1193 | Episode 3 annotated survey — batch 03, 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-037 / 1194–1205 | Episode 3 annotated survey — batch 04, 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-038 / 1206–1219 | Episode 3 annotated survey — batch 05, 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-039 / 1220–1234 | Episode 3 retention checkpoint — 2026-10-29 | RELOCATE_SECTION: `episodes/EP-03/survey/episode-03-retention-checkpoint.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-040 / 1235–1256 | Episode 4 retrospective subtitle/context preparation — 2026-10-29 | RELOCATE_SECTION: `episodes/EP-04/preparation/episode-04-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-041 / 1257–1283 | Episode 4 retrospective reconciliation — 2026-10-29 | RELOCATE_SECTION: `episodes/EP-04/evidence/episode-04-reconciliation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-042 / 1284–1298 | Episode 5 gallery and subtitle/context preparation — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/preparation/episode-05-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-043 / 1299–1313 | Episode 5 bounded alignment — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/alignment/episode-05-alignment-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-044 / 1314–1378 | Episode 5 annotated survey — batch 01, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-045 / 1379–1412 | Cross-episode Mikey identification — 2026-10-30 | RELOCATE_SECTION: `comparisons/mikey-identification.md` | Cross-episode identity owner; episode pointers only. |
| SEC-046 / 1413–1472 | Episode 5 annotated survey — batch 02, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-047 / 1473–1540 | Episode 5 annotated survey — batch 03, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-048 / 1541–1611 | Episode 5 annotated survey — batch 04, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-049 / 1612–1707 | Episode 5 annotated survey — batch 05, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-050 / 1708–1767 | Episode 5 caster supplements — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/evidence/episode-05-supplement-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-051 / 1768–1828 | Episode 5 retention checkpoint — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-05/survey/episode-05-retention-checkpoint.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-052 / 1829–1850 | Episode 6 gallery preparation — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/preparation/episode-06-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-053 / 1851–1869 | Episode 6 subtitle and website context — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/preparation/episode-06-preparation-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-054 / 1870–1887 | Episode 6 bounded alignment — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/alignment/episode-06-alignment-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-055 / 1888–1973 | Episode 6 annotated survey — batch 01, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-056 / 1974–2054 | Episode 6 annotated survey — batch 02, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-057 / 2055–2148 | Episode 6 annotated survey — batch 03, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-058 / 2149–2244 | Episode 6 annotated survey — batch 04, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-059 / 2245–2346 | Episode 6 annotated survey — batch 05, 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-survey-history.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |
| SEC-060 / 2347–2399 | Episode 6 retention checkpoint — 2026-10-30 | RELOCATE_SECTION: `episodes/EP-06/survey/episode-06-retention-checkpoint.md` | Keep historical checkpoint; link to existing detailed record, do not merge claims. |

## Register baseline

| Path under indexes | Rows | Columns |
| --- | ---: | ---: |
| `animehistory/alignment-anchors.csv` | 105 | 33 |
| `animehistory/alignment-mappings.csv` | 12 | 22 |
| `animehistory/all-episodes.csv` | 9204 | 14 |
| `animehistory/category-index.csv` | 9204 | 21 |
| `animehistory/CSVs/episode-01.csv` | 354 | 14 |
| `animehistory/CSVs/episode-02.csv` | 354 | 14 |
| `animehistory/CSVs/episode-03.csv` | 354 | 14 |
| `animehistory/CSVs/episode-04.csv` | 354 | 14 |
| `animehistory/CSVs/episode-05.csv` | 354 | 14 |
| `animehistory/CSVs/episode-06.csv` | 354 | 14 |
| `animehistory/CSVs/episode-07.csv` | 354 | 14 |
| `animehistory/CSVs/episode-08.csv` | 354 | 14 |
| `animehistory/CSVs/episode-09.csv` | 354 | 14 |
| `animehistory/CSVs/episode-10.csv` | 354 | 14 |
| `animehistory/CSVs/episode-11.csv` | 354 | 14 |
| `animehistory/CSVs/episode-12.csv` | 354 | 14 |
| `animehistory/CSVs/episode-13.csv` | 354 | 14 |
| `animehistory/CSVs/episode-14.csv` | 354 | 14 |
| `animehistory/CSVs/episode-15.csv` | 354 | 14 |
| `animehistory/CSVs/episode-16.csv` | 354 | 14 |
| `animehistory/CSVs/episode-17.csv` | 354 | 14 |
| `animehistory/CSVs/episode-18.csv` | 354 | 14 |
| `animehistory/CSVs/episode-19.csv` | 354 | 14 |
| `animehistory/CSVs/episode-20.csv` | 354 | 14 |
| `animehistory/CSVs/episode-21.csv` | 354 | 14 |
| `animehistory/CSVs/episode-22.csv` | 354 | 14 |
| `animehistory/CSVs/episode-23.csv` | 354 | 14 |
| `animehistory/CSVs/episode-24.csv` | 354 | 14 |
| `animehistory/CSVs/episode-25.csv` | 354 | 14 |
| `animehistory/CSVs/episode-26.csv` | 354 | 14 |
| `animehistory/supplemental-index.csv` | 26 | 30 |
| `context/context.csv` | 81 | 17 |
| `context/links.csv` | 1278 | 6 |
| `context/sources.csv` | 29 | 19 |
| `context/subjects.csv` | 48 | 7 |
| `performance-metrics.csv` | 47 | 10 |
| `settei-screening.csv` | 221 | 16 |

## Workbook baseline

Read-only ZIP/XML inspection of existing local XLSX files; no recalculation, authoring, rendering or application control.
Canonical per-sheet digests cover ordered cell coordinates/types/resolved values/formulas and hyperlink relationships.
File/XML hashes also protect the exact original bytes. These checks record the starting state, not a fresh CSV-to-workbook equality proof.
After migration, expected link changes must be compared explicitly; binary XLSX hashes alone are not data-equivalence checks.

| Workbook | Sheets | Stored cells | Hyperlinks |
| --- | ---: | ---: | ---: |
| `animehistory/animehistory-review.xlsx` | 27 | 138747 | 9230 |
| `animehistory/category-review.xlsx` | 30 | 440198 | 9364 |
| `context/context-review.xlsx` | 5 | 14548 | 2737 |

## Phase 1.1 validation and limits

- All 152 root files have unique destinations; every source was hashed and every destination was absent.
- All 60 Markdown heading sections are mapped, including retained shared sections and two explicit mixed-content splits.
- Baseline covers 193 files under indexes, 37 CSV tables and 3 existing workbooks.
- Read-only hashing and parsing do not validate research claims, source media or current media availability.
- Active consumer inventory, historical-path classification and exact link repair actions remain Phase 1.2.
- No records moved; tools, CSVs, workbooks, archives, contact sheets and source media unchanged.
- Recheck hashes and inventory before Phase 2/3; classify any intervening edits instead of overwriting them.
