# Reference And Implementation Documentation Reorganization

The [plan](reference-index-reorganization-plan.md) owns scope, sequence and approval gates.
All nine reorganization phases are accepted. The maintainer explicitly accepted the Phase 5
component and Phase 9 combined closeout on 2026-11-01, following the accepted migration and
validation evidence. Closeout publication is verified in the combined closeout; earlier validation
acceptance alone did not close the component.

| Record | Purpose |
| --- | --- |
| [Reference migration ledger](reference-index-reorganization-ledger.md) | Original/current reference-index file and README-section dispositions |
| [Reference baseline](reference-index-reorganization-baseline.json) | Frozen Phase 1.1 hashes, counts and historical locations |
| [Tool audit](reference-index-reorganization-tool-audit.md) | Original tool/consumer audit and 33 historical helper routes |
| [Phase 2 preparation](reference-index-reorganization-phase-2.md) | Navigation/routing preparation and isolated checks |
| [Phase 3 migration](reference-index-reorganization-phase-3.md) | Reference-record/helper moves and routing activation |
| [Phase 4 validation](reference-index-reorganization-phase-4.md) | Accepted reference integration/workbook evidence |
| [Combined closeout](reference-index-reorganization-closeout.md) | Accepted Phase 5 component handoff and Phase 9 reconciliation, with verified publication receipt |
| [Documentation migration ledger](implementation-documentation-migration-ledger.md) | Exact documentation routes, dependency audit and actual migration dispositions |
| [Documentation baseline](implementation-documentation-migration-baseline.json) | Separate frozen Phase 6.1 snapshot; historical paths/status remain unchanged |
| [Phase 7 migration](implementation-documentation-migration-phase-7.md) | Actual documentation moves, reference repairs and bounded checks |
| [Phase 8 validation](implementation-documentation-validation-phase-8.md) | Accepted file/content/reference, live-reader and future-ownership validation |

Baseline snapshots and dated audit tables retain original paths as historical evidence. Use the
ledgers to resolve those locations. Their presence is not a fallback configuration or instruction
to recreate a flat index/implementation directory. The earlier routing patch is already applied;
do not replay it or historical local helpers.
