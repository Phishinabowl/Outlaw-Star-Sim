# Implementation Documentation Migration Ledger — Phase 6.1

Status: Phase 6.1 inventory and Phase 6.2 consumer/output audit complete on 2026-11-01
(America/New_York); accepted by the maintainer on the same date. Subsequent Phase 7 migration
was implemented, checked and accepted on 2026-11-01; original inventory/audit checkpoints remain below.

The [plan](reference-index-reorganization-plan.md#phase-6-implementation-documentation-inventory-and-dependency-baseline)
owns scope, checklists and gates. The separate
[documentation baseline](implementation-documentation-migration-baseline.json) owns exact bytes,
SHA-256 values, heading line numbers/text/derived fragments, destination preconditions and IDs.
This ledger owns file placement, disposition, exceptions and the Phase 6.2 dependency findings
below rather than duplicating this inventory in the plan.

## Baseline And Worktree

- Starting HEAD: `e0ebf1c0311f64b47bcc792517dbb18722d57c5d`; `main` aligned with upstream.
  The worktree was clean. Reference Phase 5 preparation and the extended plan are already published
  in that commit; component acceptance remains pending. No uncommitted Phase 5 edits need recovery.
- The pre-edit snapshot contains 44 existing files: 29 at the implementation root and 15 under
  `validation`. It records 442 ATX headings outside fenced code and zero explicit HTML anchor IDs.
  Derived fragments are inventory aids, not a fresh whole-project link-resolution claim.
- Every original source is a regular file with no reparse point in its inspected ancestry.
  All 44 proposed destinations are unique, absent and contained within `docs/implementation`;
  inspected existing target ancestors contain no reparse points. No destination folder was created.
- The prior reference-index baseline (DOC-021) remains byte-preserved historical evidence. The new
  snapshot is a separate file; it does not rewrite old paths, pending-audit values or hashes.
- The documentation-baseline SHA-256 at creation is
  `976fd2a62b85797f5b9abfbe1c9e55776a5808ecb28e3d26257062eeaf2a403a`.
- Capture precedes the plan's Phase 6.1 completion/status edit. That intentional edit, later
  confirmation/status changes and any subsequent authorized records must be explicitly accounted
  for at migration preflight. This snapshot must not be overwritten to disguise later changes.

## Disposition And Preservation Rules

Every DOC row is now **MOVED_AND_CHECKED**. No deletion, merge or filename change is assigned.
Paths in the table are relative to `docs/implementation`, both before and after the proposed move.

DOC-021 is byte-preserved. For Markdown records, preserve findings, decisions, dates, approval
provenance, scenario/phase IDs and substantive headings. Active link repairs were performed in
Phase 7. Consumer details and historical-path exceptions are recorded in the Phase 6.2 sections
below; the placement decision and dependency audit remain distinct evidence.

## Existing File Routes

| ID | Current path | Exact destination | Ownership class |
| --- | --- | --- | --- |
| DOC-001 | `blender-sandbox-pilot-design.md` | `investigations/blender-sandbox/blender-sandbox-pilot-design.md` | DEFERRED_INVESTIGATION |
| DOC-002 | `phase-1-1-host-tooling-readiness.md` | `vertical-slices/slice-01-awakening/phase-1/1.1-tooling/phase-1-1-host-tooling-readiness.md` | SLICE_PHASE_RECORD |
| DOC-003 | `phase-1-2-closeout-proposal.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-closeout-proposal.md` | SLICE_PHASE_RECORD |
| DOC-004 | `phase-1-2-cockpit-motion-proposal.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-cockpit-motion-proposal.md` | SLICE_PHASE_RECORD |
| DOC-005 | `phase-1-2-corridor-route-amendment.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-corridor-route-amendment.md` | SLICE_PHASE_RECORD |
| DOC-006 | `phase-1-2-engineering-clearance-proposal.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-engineering-clearance-proposal.md` | SLICE_PHASE_RECORD |
| DOC-007 | `phase-1-2-layout-proposal-a.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-layout-proposal-a.md` | SLICE_PHASE_RECORD |
| DOC-008 | `phase-1-2-reservation-audit.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-reservation-audit.md` | SLICE_PHASE_RECORD |
| DOC-009 | `phase-1-2-spatial-motion-decision-packet.md` | `vertical-slices/slice-01-awakening/phase-1/1.2-spatial-motion/phase-1-2-spatial-motion-decision-packet.md` | SLICE_PHASE_RECORD |
| DOC-010 | `phase-1-3-action-readiness-draft.md` | `vertical-slices/slice-01-awakening/phase-1/1.3-actions-readiness/phase-1-3-action-readiness-draft.md` | SLICE_PHASE_RECORD |
| DOC-011 | `phase-1-3-closeout-audit.md` | `vertical-slices/slice-01-awakening/phase-1/1.3-actions-readiness/phase-1-3-closeout-audit.md` | SLICE_PHASE_RECORD |
| DOC-012 | `phase-1-4-architecture-asset-validation-draft.md` | `vertical-slices/slice-01-awakening/phase-1/1.4-architecture-assets/phase-1-4-architecture-asset-validation-draft.md` | SLICE_PHASE_RECORD |
| DOC-013 | `phase-1-4-closeout-review.md` | `vertical-slices/slice-01-awakening/phase-1/1.4-architecture-assets/phase-1-4-closeout-review.md` | SLICE_PHASE_RECORD |
| DOC-014 | `phase-1-5-gate-review.md` | `vertical-slices/slice-01-awakening/phase-1/1.5-gate-review/phase-1-5-gate-review.md` | SLICE_PHASE_RECORD |
| DOC-015 | `phase-2-1-closeout.md` | `vertical-slices/slice-01-awakening/phase-2/2.1-tooling/phase-2-1-closeout.md` | SLICE_PHASE_RECORD |
| DOC-016 | `phase-2-2-closeout.md` | `vertical-slices/slice-01-awakening/phase-2/2.2-project-setup/phase-2-2-closeout.md` | SLICE_PHASE_RECORD |
| DOC-017 | `phase-2-3-closeout.md` | `vertical-slices/slice-01-awakening/phase-2/2.3-build-editor/phase-2-3-closeout.md` | SLICE_PHASE_RECORD |
| DOC-018 | `phase-2-4-closeout.md` | `vertical-slices/slice-01-awakening/phase-2/2.4-packaging/phase-2-4-closeout.md` | SLICE_PHASE_RECORD |
| DOC-019 | `phase-2-exit-review.md` | `vertical-slices/slice-01-awakening/phase-2/phase-2-exit-review.md` | SLICE_PHASE_EXIT |
| DOC-020 | `phase-3-1-closeout.md` | `vertical-slices/slice-01-awakening/phase-3/3.1-player-scale/phase-3-1-closeout.md` | SLICE_PHASE_RECORD |
| DOC-021 | `reference-index-reorganization-baseline.json` | `projects/reference-index-reorganization/reference-index-reorganization-baseline.json` | REORGANIZATION_PROJECT |
| DOC-022 | `reference-index-reorganization-closeout.md` | `projects/reference-index-reorganization/reference-index-reorganization-closeout.md` | REORGANIZATION_PROJECT |
| DOC-023 | `reference-index-reorganization-ledger.md` | `projects/reference-index-reorganization/reference-index-reorganization-ledger.md` | REORGANIZATION_PROJECT |
| DOC-024 | `reference-index-reorganization-phase-2.md` | `projects/reference-index-reorganization/reference-index-reorganization-phase-2.md` | REORGANIZATION_PROJECT |
| DOC-025 | `reference-index-reorganization-phase-3.md` | `projects/reference-index-reorganization/reference-index-reorganization-phase-3.md` | REORGANIZATION_PROJECT |
| DOC-026 | `reference-index-reorganization-phase-4.md` | `projects/reference-index-reorganization/reference-index-reorganization-phase-4.md` | REORGANIZATION_PROJECT |
| DOC-027 | `reference-index-reorganization-plan.md` | `projects/reference-index-reorganization/reference-index-reorganization-plan.md` | REORGANIZATION_PROJECT |
| DOC-028 | `reference-index-reorganization-tool-audit.md` | `projects/reference-index-reorganization/reference-index-reorganization-tool-audit.md` | REORGANIZATION_PROJECT |
| DOC-029 | `validation/acceptance-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/acceptance-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-030 | `validation/foundation-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/foundation-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-031 | `validation/interaction-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/interaction-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-032 | `validation/machinery-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/machinery-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-033 | `validation/phase-2-1-tooling-preflight-2026-10-23.md` | `vertical-slices/slice-01-awakening/phase-2/2.1-tooling/phase-2-1-tooling-preflight-2026-10-23.md` | SLICE_VALIDATION_RESULT |
| DOC-034 | `validation/phase-2-3-build-editor-results.md` | `vertical-slices/slice-01-awakening/phase-2/2.3-build-editor/phase-2-3-build-editor-results.md` | SLICE_VALIDATION_RESULT |
| DOC-035 | `validation/phase-2-3-unreal-mcp-pilot.md` | `vertical-slices/slice-01-awakening/phase-2/2.3-build-editor/phase-2-3-unreal-mcp-pilot.md` | SLICE_VALIDATION_RESULT |
| DOC-036 | `validation/phase-2-4-package-results.md` | `vertical-slices/slice-01-awakening/phase-2/2.4-packaging/phase-2-4-package-results.md` | SLICE_VALIDATION_RESULT |
| DOC-037 | `validation/phase-3-1-blender-handoff-results.md` | `vertical-slices/slice-01-awakening/phase-3/3.1-player-scale/phase-3-1-blender-handoff-results.md` | SLICE_VALIDATION_RESULT |
| DOC-038 | `validation/phase-3-1-blender-mcp-pilot.md` | `vertical-slices/slice-01-awakening/phase-3/3.1-player-scale/phase-3-1-blender-mcp-pilot.md` | SLICE_VALIDATION_RESULT |
| DOC-039 | `validation/phase-3-1-player-scale-results.md` | `vertical-slices/slice-01-awakening/phase-3/3.1-player-scale/phase-3-1-player-scale-results.md` | SLICE_VALIDATION_RESULT |
| DOC-040 | `validation/phase-3-1-recovery-results.md` | `vertical-slices/slice-01-awakening/phase-3/3.1-player-scale/phase-3-1-recovery-results.md` | SLICE_VALIDATION_RESULT |
| DOC-041 | `validation/readiness-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/readiness-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-042 | `validation/spatial-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/spatial-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-043 | `validation/state-lifecycle-validation-procedures.md` | `vertical-slices/slice-01-awakening/validation/procedures/state-lifecycle-validation-procedures.md` | SLICE_SPECIFIC_PROCEDURE |
| DOC-044 | `vertical-slice-1-implementation-plan.md` | `vertical-slices/slice-01-awakening/vertical-slice-1-implementation-plan.md` | SLICE_PLAN |

Ownership classes distinguish the slice plan, phase decisions/closeouts, phase results, slice-specific
procedures, the reorganization project and the deferred investigation. All ordinary phase records
and result files belong to their named slice subphase; the Phase 2 exit review belongs to the
slice's Phase 2 directory. Reorganization records remain one project, including this plan's own move.

## Resolved Procedure Placement Exception

All seven procedure records (DOC-029–032 and DOC-041–043) belong to
`vertical-slices/slice-01-awakening/validation/procedures/`. Their titles, Scope/Authority fields,
VS1 scenario IDs and execution prerequisites explicitly bind them to this slice's machinery,
state, readiness, route and acceptance contracts. Even the foundation document combines generally
useful evidence rules with VS1-T01–T04 and the slice's Phase 2 gates. A reusable section does not
make the entire document a shared cross-slice procedure.

This is the plan's explicit slice-only exception, not a new gameplay or validation contract.
Keep the seven records together because they reference each other across several slice phases.
Do not split, generalize or duplicate their content during migration. Future efforts may link
relevant guidance; promotion/extraction of genuinely shared procedures needs its own scoped decision.
No shared procedure is established by this inventory, so do not create an empty global
`validation/procedures/` directory. The global validation README can explain ownership and link
the slice procedures without becoming their authority.

The Blender Sandbox record (DOC-001) uses the agreed investigation destination. Its dated
deferred status and findings remain intact; this assignment grants no installation/pilot approval.

## New Inventory Records And Planned Navigation

These additions are distinct from the frozen 44-file source snapshot. Their final destinations
are explicit, so the new inventory does not create another unledgered root-file residue.

| ID | Current / creation location | Final destination | Disposition |
| --- | --- | --- | --- |
| NEW-001 | `implementation-documentation-migration-ledger.md` | `projects/reference-index-reorganization/implementation-documentation-migration-ledger.md` | Created in 6.1; maintained through audit/migration; move in Phase 7 |
| NEW-002 | `implementation-documentation-migration-baseline.json` | `projects/reference-index-reorganization/implementation-documentation-migration-baseline.json` | Generated in 6.1; freeze bytes and move in Phase 7 |
| NAV-001 | Not created | `README.md` | Create in Phase 7: effort directory linking the existing roadmap and authoritative plans |
| NAV-002 | Not created | `vertical-slices/slice-01-awakening/README.md` | Create in Phase 7: slice record navigation and links to its plan/status owner |
| NAV-003 | Not created | `validation/README.md` | Create in Phase 7: ownership directory; distinguish slice procedures from future shared procedures |
| NAV-004 | Not created | `projects/reference-index-reorganization/README.md` | Create in Phase 7: links to project plan, ledgers, frozen baselines and result/closeout owners |

All four navigation destinations and both new records' final destinations were absent at capture.
The new baseline declares these records but does not recursively hash itself or the evolving ledger.
Capture NEW-001's current bytes at migration preflight; preserve NEW-002's generated bytes.
Further authorized artifacts require explicit added rows before migration. Do not create future
slices, empty phase directories or additional plans merely to fill out the tree.

## Phase 6.1 Checks And Remaining Work

All 44 original files matched their captured hashes immediately after baseline generation.
After the completion/status edit, only DOC-027 is expected to differ; all other original files and
the old/new frozen baselines must remain unchanged. The only additions are NEW-001 and NEW-002.
These checks concern file ownership and inventory, not research correctness, runtime behavior,
consumer compatibility or current source-media identity.

Phase 6.1 is complete and accepted within this scope. The subsequent Phase 6.2 findings
below cover dependencies without changing live paths or granting Phase 7 authorization.

## Phase 6.2 Audit Scope And Checkpoint

Completed 2026-11-01 against the Phase 6.1 working state: the owning plan is modified and NEW-001
and NEW-002 are untracked; no other pending change existed. This audit preserves those records.
The frozen baseline is not rewritten to include this later audit or change its historical status.

The read-only scan covers 406 first-party text/configuration/source files: root documentation and
configuration, all `docs`, authored reference-root/index records, tools (including all 33 ignored
historical helpers), project-owned assets/recipes, `.codex`/`.vscode` text configuration and the
Unreal project's root/source/configuration text. It includes all 37 CSV tables and 72 JSON files.
Source media, generated caches/frames/subtitles, binary assets/workbooks, `.tmp`, `.vs`, unscoped
private working/recovery trees, build outputs and third-party plugin code are outside this scan.
Scoped historical helpers are read only; no editor, helper, extractor or external source is invoked.

Links were resolved against each source's current directory and the 46-file move map (44 DOC rows
plus NEW-001/002). The audit records 568 relevant local Markdown links: 414 target a moving record
and 430 originate in a moving record, with 276 counted in both sets. Thus 138 arrive from unmoved
consumers and 154 leave moving documents for targets outside the move map. All 568 current targets
exist; all 143 referenced Markdown fragments resolve. Every DOC row has an incoming link.

Of these links, **468 need a different relative href across 91 consumer files**; 100 keep the same
href because the relative relationship is unchanged. These are pre-edit audit counts, not promised
post-navigation counts. The table below records current source locations and line ranges before
the Phase 6.2 ledger/plan additions; recompute against current bytes before Phase 7 repair.

## Active Markdown Repair Register

DOC and NEW consumer IDs refer to the exact current paths in the file tables above. Target IDs
identify moving targets; `outside-map` means an unchanged target that still needs a link rebased
because its source document moves. Counts and lines include only hrefs that change.

| Consumer at audit checkpoint | Hrefs to repair | Baseline lines | Moving target IDs / unchanged target |
| --- | ---: | --- | --- |
| `README.md` | 25 | 7,11,12,14,54,56,58,64,80,89,90 | DOC-002,DOC-003,DOC-005,DOC-011,DOC-012,DOC-014,DOC-015,DOC-016,DOC-017,DOC-018,DOC-019,DOC-020,DOC-033,DOC-038,DOC-040,DOC-044 |
| `docs/architecture/editor-automation.md` | 7 | 3,5,8,9,11,14,20 | DOC-001,DOC-017,DOC-018,DOC-037,DOC-038,DOC-040,DOC-044 |
| `docs/architecture/interaction-system.md` | 1 | 6 | DOC-011 |
| `docs/architecture/player-camera-control.md` | 2 | 7,13 | DOC-009,DOC-011 |
| `docs/architecture/ship-simulation.md` | 1 | 15 | DOC-011 |
| `docs/architecture/unreal-strategy.md` | 7 | 11,18,20,26,40,83,86 | DOC-002,DOC-012,DOC-015,DOC-017,DOC-018,DOC-033,DOC-044 |
| `docs/development/dusklight-learning-reference.md` | 1 | 10 | DOC-012 |
| `docs/development/game-development-glossary.md` | 9 | 7,49,279,299,330,340,358,382,389 | DOC-012 |
| `docs/development/player-scale-fixture.md` | 4 | 5,7,8,9 | DOC-039,DOC-040,DOC-042,DOC-044 |
| `docs/development/unreal-project-setup.md` | 3 | 4,7,122 | DOC-016,DOC-034,DOC-044 |
| `docs/development/work-annotation-standards.md` | 1 | 11 | DOC-044 |
| `DOC-001` | 3 | 8,16 | DOC-012,outside-map |
| `DOC-002` | 2 | 10,11 | DOC-044,outside-map |
| `DOC-003` | 5 | 5,6,10,32,130 | DOC-010,DOC-011,DOC-044,outside-map |
| `DOC-004` | 4 | 11,20,21,90 | outside-map |
| `DOC-006` | 2 | 16,22 | outside-map |
| `DOC-007` | 1 | 7 | outside-map |
| `DOC-008` | 6 | 9,10,11,22,23,24 | outside-map |
| `DOC-009` | 13 | 3,11,12,35,59,130,139,155,204,238,451,496,592 | DOC-011,DOC-044,outside-map |
| `DOC-010` | 13 | 17,20,21,22,23,24,25,26,75,176,192,237,531 | DOC-003,DOC-009,DOC-044,outside-map |
| `DOC-011` | 4 | 8,18,19,20 | DOC-003,DOC-044,outside-map |
| `DOC-012` | 21 | 10,12,13,14,15,16,17,19,521,580,639,657,721,744,746,748,750,752,754,756,771 | DOC-001,DOC-002,DOC-003,DOC-011,DOC-014,DOC-029,DOC-030,DOC-031,DOC-032,DOC-041,DOC-042,DOC-043,DOC-044,outside-map |
| `DOC-013` | 2 | 9,35 | DOC-044 |
| `DOC-014` | 9 | 8,20,26,37,92 | DOC-002,DOC-003,DOC-011,DOC-012,DOC-013,DOC-044,outside-map |
| `DOC-015` | 4 | 10,14,83 | DOC-030,DOC-033,DOC-044,outside-map |
| `DOC-016` | 3 | 10,35 | DOC-030,DOC-044,outside-map |
| `DOC-017` | 2 | 9 | DOC-034,DOC-035 |
| `DOC-018` | 2 | 8,9 | DOC-036,DOC-044 |
| `DOC-019` | 9 | 9,15,16,17,18 | DOC-015,DOC-016,DOC-017,DOC-018,DOC-030,DOC-034,DOC-036,DOC-044 |
| `DOC-020` | 5 | 15,17,22,34,40 | DOC-012,DOC-037,DOC-038,DOC-039,DOC-040 |
| `DOC-022` | 3 | 35,36,37 | outside-map |
| `DOC-024` | 1 | 40 | outside-map |
| `DOC-027` | 1 | 12 | DOC-044 |
| `DOC-028` | 1 | 18 | outside-map |
| `DOC-029` | 5 | 8,85 | DOC-011,DOC-012,DOC-044,outside-map |
| `DOC-030` | 7 | 8,16,17,26,27,94 | DOC-002,DOC-012,DOC-015,DOC-017,DOC-018,DOC-044,outside-map |
| `DOC-031` | 3 | 8 | DOC-010,DOC-011,DOC-044 |
| `DOC-032` | 3 | 8 | DOC-010,DOC-011,DOC-044 |
| `DOC-033` | 2 | 7,13 | DOC-002,DOC-014 |
| `DOC-034` | 1 | 42 | DOC-017 |
| `DOC-035` | 1 | 9 | outside-map |
| `DOC-037` | 3 | 8,129 | DOC-012,DOC-020,DOC-044 |
| `DOC-038` | 3 | 8,116 | DOC-020,DOC-044,outside-map |
| `DOC-039` | 2 | 9,91 | DOC-020,outside-map |
| `DOC-041` | 3 | 8 | DOC-011,DOC-044,outside-map |
| `DOC-042` | 7 | 8,74,93,115,116 | DOC-003,DOC-005,DOC-008,DOC-011,DOC-044 |
| `DOC-043` | 4 | 8,121 | DOC-011,DOC-012,DOC-044 |
| `DOC-044` | 170 | 49,54,57,69,74,76,77,80,91,93,95,97,99,100,101,102,103,105,267,280,281,288,312,318,322,349,351,358,364,372,374,381,387,399,424,425,434,441,445,450,453,458,459,462,468,471,472,482,487,496,498,507,512,531,533,538,540,545,546,551,552,554,558,563,564,566,571,575,578,581,596,605,608,613,618,623,630,640,646,652,657,666,672,684,692,696,709,715,720,724,729,735,741,747,753,759,766,773,780,787,793,803,805,812,819,827,833,841,848,855,860,868,876,894,900,906,912,916,921,927,934,941,947,954,959,965,971,977,985,993,1001,1010,1028,1061,1107,1110,1121,1152,1163,1174,1204,1215,1226,1273,1281,1293,1307,1340,1353,1364,1384,1395,1407,1419,1432,1436,1437,1438,1439,1440,1441,1442,1500,1501,1545 | DOC-001,DOC-002,DOC-003,DOC-005,DOC-008,DOC-009,DOC-010,DOC-011,DOC-012,DOC-013,DOC-014,DOC-015,DOC-016,DOC-017,DOC-018,DOC-019,DOC-020,DOC-021,DOC-022,DOC-023,DOC-024,DOC-025,DOC-026,DOC-027,DOC-028,DOC-029,DOC-030,DOC-031,DOC-032,DOC-033,DOC-034,DOC-035,DOC-036,DOC-037,DOC-038,DOC-039,DOC-040,DOC-041,DOC-042,DOC-043,outside-map |
| `docs/phase-0-report.md` | 1 | 4 | DOC-044 |
| `docs/reconstruction/baseline-v1/motion-clearance-envelopes.md` | 1 | 7 | DOC-011 |
| `docs/reconstruction/baseline-v1/operational-state-baseline.md` | 1 | 5 | DOC-011 |
| `docs/reconstruction/baseline-v1/spatial-constraint-map.md` | 2 | 5,7 | DOC-005,DOC-044 |
| `docs/reconstruction/baseline-v1/vertical-slice-1.md` | 7 | 7,11,74,75,86,115,116 | DOC-003,DOC-005,DOC-010,DOC-011,DOC-013,DOC-014 |
| `docs/reconstruction/open-questions.md` | 2 | 17,21 | DOC-011,DOC-044 |
| `docs/reconstruction/reference-phase-progress.md` | 3 | 4,5,36 | DOC-011,DOC-044 |
| `docs/reconstruction/xgp-reference-index.md` | 3 | 3,4,17 | DOC-003,DOC-008,DOC-011 |
| `docs/roadmap.md` | 16 | 39,43,74,76,80,82,83,85,86,90,92,93,97,102,107 | DOC-002,DOC-003,DOC-010,DOC-011,DOC-012,DOC-013,DOC-014,DOC-015,DOC-016,DOC-017,DOC-018,DOC-019,DOC-020,DOC-040,DOC-044 |
| `docs/vision.md` | 1 | 14 | DOC-011 |
| `reference/README.md` | 3 | 7,17,48 | DOC-011,DOC-022,DOC-044 |
| `reference/indexes/README.md` | 2 | 5,24 | DOC-022,DOC-027 |
| `reference/indexes/animehistory/README.md` | 1 | 23 | DOC-044 |
| `reference/indexes/comparisons/README.md` | 1 | 14 | DOC-023 |
| `reference/indexes/context/README.md` | 1 | 13 | DOC-044 |
| `reference/indexes/episodes/EP-01/README.md` | 1 | 24 | DOC-023 |
| `reference/indexes/episodes/EP-02/README.md` | 1 | 35 | DOC-023 |
| `reference/indexes/episodes/EP-03/README.md` | 1 | 25 | DOC-023 |
| `reference/indexes/episodes/EP-04/README.md` | 1 | 50 | DOC-023 |
| `reference/indexes/episodes/EP-04/evidence/episode-04-cockpit-case-staging-review.md` | 1 | 29 | DOC-009 |
| `reference/indexes/episodes/EP-04/evidence/episode-04-hilda-laptop-screen-review.md` | 1 | 46 | DOC-010 |
| `reference/indexes/episodes/EP-04/evidence/episode-04-opening-bootstrap-review.md` | 1 | 69 | DOC-009 |
| `reference/indexes/episodes/EP-05/README.md` | 1 | 15 | DOC-023 |
| `reference/indexes/episodes/EP-06/README.md` | 1 | 15 | DOC-023 |
| `reference/indexes/episodes/EP-07/README.md` | 1 | 16 | DOC-023 |
| `reference/indexes/episodes/EP-08/README.md` | 1 | 17 | DOC-023 |
| `reference/indexes/episodes/EP-11/README.md` | 1 | 21 | DOC-023 |
| `reference/indexes/episodes/EP-11/evidence/episode-11-subether-review.md` | 1 | 60 | DOC-010 |
| `reference/indexes/episodes/EP-26/README.md` | 1 | 16 | DOC-023 |
| `reference/indexes/episodes/README.md` | 1 | 23 | DOC-023 |
| `reference/indexes/performance/README.md` | 1 | 12 | DOC-023 |
| `reference/indexes/settei/README.md` | 1 | 52 | DOC-023 |
| `reference/indexes/settei/batches/settei-collection-review-batch-12.md` | 1 | 25 | DOC-005 |
| `reference/indexes/settei/batches/settei-collection-review-batch-20.md` | 2 | 107,118 | DOC-005 |
| `reference/indexes/settei/batches/settei-collection-review-batch-21.md` | 1 | 41 | DOC-005 |
| `reference/indexes/sources/README.md` | 1 | 11 | DOC-023 |
| `reference/indexes/supplied-references/README.md` | 1 | 11 | DOC-023 |
| `reference/indexes/supplied-references/to-be-continued-supplied-reference.md` | 1 | 41 | DOC-044 |
| `tools/README.md` | 4 | 6,50,72,76 | DOC-022,DOC-024,DOC-026,DOC-037 |
| `tools/historical/README.md` | 1 | 7 | DOC-028 |
| `tools/reference-alignment/README.md` | 1 | 26 | DOC-044 |
| `tools/reference-context/README.md` | 1 | 19 | DOC-044 |
| `tools/reference-extraction/README.md` | 1 | 39 | DOC-044 |

For each actual Markdown link, resolve against its old source directory, map both source and target
to their ledgered destinations, and compute the new relative href from the new source directory.
Keep the fragment text and substantive heading unchanged. This also rebases links from moving
records to unchanged architecture, reconstruction, source/evidence, tool and asset records.
Do not perform basename replacement across document bodies or treat every current href as changed.
Self-fragments and links between documents moving together may need no edit. Re-scan newly added
navigation and audit/status references after migration; line numbers above are historical locators.

## Prose Paths And Historical Exceptions

The filename scan found 195 non-link occurrences across five files. These are classified separately
from active Markdown links; no occurrence authorizes blanket text replacement.

| Source / location at audit | Classification | Phase 7 disposition |
| --- | --- | --- |
| `docs/development/work-annotation-standards.md:101` | Active durable-owner prose path | Change the slice-plan path to DOC-044's destination; preserve table meaning |
| DOC-012, line 55 | Broad `docs/implementation/` ownership | Root remains valid; keep it as the effort-directory umbrella rather than inventing a new authority |
| DOC-012, line 93 | Active VS1 procedure/result output convention | Replace the flat validation destination with the slice's `validation/procedures/` for procedures and owning `phase-N/subphase/` for results; preserve scenario IDs and raw-output ownership |
| DOC-030, line 33 | Active authored-result output convention | Route authored results to the slice's owning phase/subphase; keep raw captures/logs local and media-publication limits intact |
| DOC-027, lines 101, 113 and 140 | Planned tree filenames / placement rule | Keep filenames and the agreed target structure; these are not stale runtime lookups |
| DOC-028, lines 276–282 | Prior reference-migration audit source paths and baseline line numbers | Preserve historical table entries; resolve their former locations through this ledger, while rebasing the document's actual Markdown links |
| NEW-001 file-route tables / source-checkpoint descriptions | Documentation migration provenance | Preserve original/current route correspondence and dated audit lines; update execution/status fields only when supported |
| NEW-002 paths, headings and source metadata | Frozen documentation snapshot | Byte-preserve; original paths remain historical data, not live configuration |
| DOC-021 prior reference-index snapshot | Frozen earlier migration evidence | Byte-preserve; do not normalize or rewrite old paths, recipe fields or pending-audit values |
| Historical extraction/recipe/command evidence and local helper text | Historical provenance / unsupported scripts | Preserve bytes and recorded meaning; no documentation-path consumer or writer was found in the 33 helper sources |

The additional directory-path scan identifies the two active output-convention repairs above;
these do not match a particular filename and are not counted among the 195 filename occurrences.
New navigation and the tool directory should link these authoritative destinations rather than
duplicate their contracts. A documentation reorganization must not promote old planning status
to a runtime pass or silently revise the deferred Sandbox investigation.

## Structured Data, Runtime Consumers And Projections

- All 37 CSV tables were scanned. No moved-document filename or implementation-directory reference
  occurs in their fields. No annotation/context/locator/alignment/settei CSV edit is required.
- Of the 72 JSON inputs scanned, the documentation snapshot contains the expected historical move
  paths; no active configuration lookup to a moving document was found. Both frozen baselines
  retain their original bytes. Existing extraction manifests/recipes are not rewritten.
- No maintained Python, PowerShell, JavaScript, C++/C# or project configuration consumer reads or
  writes a moved implementation document. Broader `docs`/`implementation`/Markdown-string checks
  find only unchanged reference schema/evidence validation or test fixtures. There is no maintained
  automatic implementation-document writer requiring a routing patch for this move.
- `category_index.py` reads field/tag contracts from `reference/indexes/animehistory/README.md`;
  that schema owner and required headings stay in place. Context evidence validation remains
  generic and no maintained evidence target in its CSVs points to a moving implementation record.
- All three ImportExcel workbook builders retain their existing register/projection inputs and
  output locations. There is no changed data input or affected workbook hyperlink to regenerate
  from this documentation move. No workbook rebuild or visual regression run is required unless
  the actual Phase 7 diff introduces an audited structured-reference change.
- Unreal/Blender recipes and verification helpers continue to use owned `.local/validation`,
  recovery or asset-output locations. Those similarly named directories are not
  `docs/implementation/validation` and must not move or be rerouted.

## Future Output Ownership And Required Validation

Documentation remains authored within the owning effort. The global implementation README links
the existing roadmap and effort plans; it does not own a second phase/status registry. Keep the
slice plan, its phase decisions/results and seven VS1 procedures in their mapped slice locations.
Put reorganization records in their mapped project; preserve the deferred investigation's owner.
Create shared procedures only for an established cross-effort purpose, with an explicit owner.
No reusable script, runtime output or research record belongs in an ad hoc implementation root file.

Phase 7 needs Markdown/reference and the three active prose/convention repairs above, not a tool
behavior change. Phase 8 should re-account for all files and preserved hashes, compare substantive
content/headings, resolve current local links/fragments and re-run the stale-path classification.
Verify the reference registers, runtime scripts, workbooks, local helpers and source/media outputs
remain unchanged. Reuse Phase 4's runtime/workbook tests when dependencies remain unchanged;
introduce bounded tests or affected-projection refresh only if an actual audited code/data change
is required. Do not decode episodes, replay historical helpers or create replacement test frameworks
to prove a documentation move. Remove task-owned audit scratch after recording findings.

## Phase 6 Audit Result And Gate

All 46 current implementation files have a disposition, no current relevant link/fragment is broken,
and all detected references have a repair or preservation classification. Phase 6.1 and 6.2 work
was accepted by the maintainer on 2026-11-01 for documentation publication. At that checkpoint no
destination had been created and no live consumer had been repaired. Phase 7 subsequently received
authorization; its results follow. The frozen baseline retains its original pre-acceptance status; this
acceptance record does not rewrite its paths, counts or hashes.

## Phase 7 Actual Dispositions — 2026-11-01

All 44 DOC rows and NEW-001/002 were moved to their exact listed destinations, with absent
originals and matching hashes immediately after each move. All DOC rows and NEW-001/002 are now
MOVED_AND_CHECKED. Tables above retain original paths, planned destinations and pre-migration
audit lines as provenance; they do not instruct current consumers to use old paths. Both frozen
JSON baselines remain byte-identical, including historical status fields and original locations.

NAV-001–004 were created at their exact listed destinations. This phase also creates one result:

| ID | Current / final destination relative to `docs/implementation` | Disposition |
| --- | --- | --- |
| NEW-003 | `projects/reference-index-reorganization/implementation-documentation-migration-phase-7.md` | Created in Phase 7; owns migration results and limits |

This explicitly ledgered result is additional to the frozen snapshot; no baseline was amended to
hide it. There are 51 implementation files: 46 moved records, four navigation pages and NEW-003.
The implementation root now contains only its README and effort/validation/investigation folders.

The [Phase 7 result](implementation-documentation-migration-phase-7.md) records 468 href repairs
across 91 prepared text outputs plus the three prose/output conventions. Prepared normalized text
matched expected values before explicit status/navigation edits. The plan, this ledger, prepared
component closeout and slice checkpoint pointers then received supported status updates. The
repository README gained a directory link. Decisions, dates, scenario IDs and substantive headings
remain intact; runtime code, CSV fields, workbook bytes and local media/output paths were not changed.

Initial migration checks pass; full Phase 8 integration remains unstarted. Phase 7 was accepted
by the maintainer on 2026-11-01 for publication. No later episode review or gameplay implementation
is authorized here.

## Phase 8.1 Validation Record — 2026-11-01

| ID | Current / final destination relative to `docs/implementation` | Disposition |
| --- | --- | --- |
| NEW-004 | `projects/reference-index-reorganization/implementation-documentation-validation-phase-8.md` | Created for Phase 8 validation; 8.1–8.2 accepted 2026-11-01 |

The [8.1 result](implementation-documentation-validation-phase-8.md) independently verifies the
published migration and preserved content against `f000f4c`. All 51 prior implementation files are
accounted for; NEW-004 brings the collection to 52. Both frozen baselines remain unchanged. This
result extends the live ledger rather than altering a frozen inventory. Phase 8.1 acceptance and
the Phase 8 exit gate remain separate from check completion. Subsequent Phase 8.2 reader/cache and
future-ownership checks pass within the same result record; no further file or data move is required.

Phase 8.1–8.2 and the Phase 8 exit gate were accepted by the maintainer on 2026-11-01 for
documentation publication. Phase 9 remains unstarted and requires separate authorization; the prepared
Phase 5 component closeout remains pending combined final reconciliation.

## Phase 9 Closeout Reconciliation — 2026-11-01

The existing [combined closeout](reference-index-reorganization-closeout.md#phase-9-combined-reconciliation-and-acceptance)
now preserves the Phase 5 component evidence and records accepted documentation migration and
validation, the operating handoff, remaining limits and final publication scope. No new file or
destination is introduced; all 52 implementation files still match this ledger. Baselines, historical
audit paths and helper bytes remain unchanged. Final checks account for both components' routes
and active links. The maintainer accepted the Phase 5 component and Phase 9 combined closeout on
2026-11-01 and authorized documentation publication. The combined closeout records verified
publication of `53deb17`, a clean worktree and zero HEAD/upstream divergence on the same date.
