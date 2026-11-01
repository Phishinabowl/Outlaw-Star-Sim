# Reference And Implementation Documentation Reorganization Plan

| Field | Value |
| --- | --- |
| Created / last edited | 2026-10-30 / 2026-11-01 |
| Status | Phases 1–4 and 6–7 accepted; Phase 5 reference closeout prepared; Phases 8–9 unstarted |
| Maintainer | Repository owner |
| Current checkpoint | Phase 7 documentation migration accepted 2026-11-01; no runtime changes; Phase 8 unstarted |

The plan and documentation publication were confirmed by the maintainer on 2026-10-30.
Implementation phases require subsequent authorization.
This work supports the [pre-3.2A research checkpoint](../../vertical-slices/slice-01-awakening/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research);
it does not start Episode 7 or Phase 3.2A.
Phase numbers below belong to this reorganization plan, not the vertical-slice implementation phases.

**Scope extension — 2026-11-01:** add organization of `docs/implementation` by vertical slice,
supporting project, shared validation procedure and investigation. The folder direction was agreed
in discussion; the amended plan was confirmed for documentation publication on 2026-11-01.
This confirms the planning record, not execution of the new phases or any documentation moves.
Phases 1–5 retain their reference-index scope and recorded acceptance state. Phase 5's prepared
closeout remains unaccepted; publication of that prepared record is not component acceptance or acceptance of
the expanded effort. Phases 6–9 cover the additional documentation work and combined final closeout.
Do not move this plan or its supporting records until the new ledger and migration phase authorize it.

## Objective and observed baseline

Organize maintained evidence by source, episode and research purpose; document tool ownership
and output destinations so future reviews do not recreate the flat directory.

The additional objective is to make implementation documentation scale beyond the first playable
slice. Vertical Slice 1 is one effort within the game, not the parent of every future slice or
feature project. Keep each document with the effort it serves; shared placement requires an actual
cross-effort purpose. Existing architecture, development, reconstruction, policy and roadmap
ownership outside `docs/implementation` remains unchanged, apart from necessary link repairs.

Read-only inspection found 152 files directly under `reference/indexes`: 84 Markdown, 66 JSON
and two CSV files. These include 48 extracted-frame manifests and 33 settei collection batches.
The existing `animehistory` and `context` subfolders already separate their shared registers.
Episode-specific records are inconsistent: early surveys have separate batch files, while recent
batch and retention records are embedded in the AnimeHistory README.

The root contains both authored evidence and generated provenance. JSON does not imply disposable
output: frame manifests preserve decoded timestamps, hashes and extraction commands after media
cleanup; alignment plans are authored inputs. Neither category is a deletion candidate merely
because the associated working images have been removed.

## Target structure

```text
reference/indexes/
├── README.md                         Navigation and ownership
├── animehistory/                     Existing shared image/timing registers and workbook views
├── context/                          Existing shared website-context registers and workbook view
├── sources/
│   ├── source-manifest.json
│   └── external-sources.md
├── settei/
│   ├── README.md
│   ├── settei-screening.csv
│   ├── batches/                      Collection-review batch Markdown
│   └── reviews/                      Focused reviews and paired structured records
├── episodes/
│   ├── README.md                     Episode directory and progress pointers
│   └── EP-NN/                        Create only needed episode folders
│       ├── README.md                 Current status and record navigation
│       ├── preparation/              Subtitle/site context and metadata inspection
│       ├── alignment/                Selection plans and alignment review
│       ├── survey/                   Batch reviews and retention checkpoint
│       └── evidence/                 Targeted reviews and extracted-frame manifests
├── performance/
│   ├── performance-metrics.csv
│   ├── performance-subtitle-audit.md
│   └── performance-subtitle-coverage.json
├── comparisons/                      Cross-episode/source reconciliation
└── supplied-references/              Supplied/third-party reference notes
```

Keep existing filenames where practical. Shared image/context CSVs remain authoritative in their
current folders. Generated workbooks remain ignored projections. Media, archives, contact sheets,
source caches and subtitle copies retain their existing local-only locations.

The AnimeHistory README retains its schema and ordered workflow. Episode progress, batch findings
and retention records move to episode records with links from the shared README. Preserve dated
acceptance and historical scope; an earlier preparation checkpoint must not be silently rewritten
to claim knowledge of later completion. Cross-episode records have one owner under `comparisons`,
with episode pointers rather than duplicate copies.

## Implementation Documentation Target Structure — Phases 6–9

Read-only inspection on 2026-11-01 found 29 files directly under `docs/implementation` and
15 under its existing `validation` directory, including the uncommitted Phase 5 closeout.
These 44 files are a preliminary count, not the Phase 6 frozen inventory. Phase 6 must also account
for any newly authorized planning records and existing worktree changes before migration.

```text
docs/implementation/
├── README.md                         Directory of efforts; link the existing overall roadmap
├── vertical-slices/
│   └── slice-01-awakening/
│       ├── README.md                 Slice scope/status and record navigation
│       ├── vertical-slice-1-implementation-plan.md
│       ├── phase-1/
│       │   ├── 1.1-tooling/
│       │   ├── 1.2-spatial-motion/
│       │   ├── 1.3-actions-readiness/
│       │   ├── 1.4-architecture-assets/
│       │   └── 1.5-gate-review/
│       ├── phase-2/
│       │   ├── 2.1-tooling/
│       │   ├── 2.2-project-setup/
│       │   ├── 2.3-build-editor/
│       │   ├── 2.4-packaging/
│       │   └── phase-2-exit-review.md
│       ├── phase-3/
│       │   └── 3.1-player-scale/
│       └── validation/
│           └── procedures/           Seven existing VS1-specific procedure documents
├── projects/
│   └── reference-index-reorganization/   This plan, baselines, ledgers and closeout records
├── validation/
│   ├── README.md
│   └── procedures/                   Procedures with a supported shared purpose
└── investigations/
    └── blender-sandbox/              Retained deferred investigation and its status
```

Create future slice/project and phase folders only when records need them. Do not create empty
future slices or infer implementation authorization from directory names. Keep existing filenames
where practical; folder ownership supplies the organization. Do not split documents into status
folders such as `draft`, `approved` or `archive`: preserve status and approval evidence in the records.

### Documentation Placement And Authority Rules

| Current record family | Proposed destination / rule |
| --- | --- |
| Overall Vertical Slice 1 implementation plan | `vertical-slices/slice-01-awakening/`, beside its README; retains slice execution/status authority |
| `phase-1-*`, `phase-2-*`, `phase-3-*` proposals, decisions, amendments and closeouts | Corresponding slice phase/subphase folder; keep each subphase's related records together |
| Existing `validation/phase-*` result and pilot records | Corresponding slice phase/subphase folder, beside the closeout they support |
| Existing reusable `*-validation-procedures.md` | `validation/procedures/` only when the content has a supported shared purpose; slice-only procedures stay within that slice and are explicitly mapped in Phase 6 |
| `blender-sandbox-pilot-design.md` | `investigations/blender-sandbox/`; preserve deferred status, dated findings and authority links |
| All `reference-index-reorganization-*` records, including this plan, frozen JSON baseline and pending closeout | `projects/reference-index-reorganization/`; one maintained owner for the expanded reorganization |
| New navigation | Root README indexes efforts/status and links the existing roadmap; slice README indexes slice records; validation README distinguishes shared procedures from phase-specific results |

The implementation root is a directory, not a competing project roadmap or slice status register.
The existing roadmap retains overall project ownership. Individual effort plans retain their gates;
the root README links those owners rather than duplicating their checklists. Phase 6 resolves exact
placements and exceptions before any move, including procedures whose shared scope is uncertain.

**Phase 6.1 placement finding — 2026-11-01:** all seven existing validation procedure documents
are explicitly scoped to VS1 scenario IDs, authorities and execution gates. They are mapped together
under the slice's `validation/procedures/`, using the slice-only exception above. No whole procedure
document currently qualifies as shared across efforts; do not create an empty global procedures
folder. The global validation README will link ownership. The separate documentation ledger owns
the file-by-file rationale and routes.

Preserve document bodies, decisions, dates, phase identifiers, acceptance provenance and substantive
heading anchors. Repair active relative links against the new owning document location. Original
paths recorded in historical commands, extraction recipes, frozen baselines or audit evidence remain
historical and resolve through the new documentation migration ledger. Do not rewrite frozen JSON
to make historical paths appear current. The new inventory/baseline must be separate from the
accepted reference-index baseline.

Keep the detailed documentation file/dependency ledger and baseline beside this plan, initially
at its current location and later in its ledgered project destination. They own exact file routes,
hashes, consumers and exceptions; this plan owns sequence and gates. Preserve the pending Phase 5
worktree explicitly so migration cannot overwrite or silently accept those changes. No renewed
reference-media cleanup, research rewrite, tool consolidation or application setup is included.

## Planned move rules and migration ledger

These rules specify destinations; Phase 1 expands them into an exhaustive, reviewed ledger before
any move. Exceptions and embedded README sections must be explicit rows.

| Current root file/family | Planned destination under `reference/indexes` |
| --- | --- |
| `source-manifest.json`, `external-sources.md` | `sources/` |
| `settei-screening.csv` | `settei/` |
| `settei-collection-review-batch-*.md` | `settei/batches/` |
| `settei-interior-review.json`, paired Markdown, `settei-variant-review.md` | `settei/reviews/` |
| `episode-index.md` | `episodes/episode-index.md`, linked from its README |
| Single-episode `*-context-preparation.md`, `*-metadata.json`, `*-inspection.md` | `episodes/EP-NN/preparation/` |
| Single-episode alignment plans, boundary/edge/holdout/validation plans and review | `episodes/EP-NN/alignment/` |
| `episode-NN-review-batch-*.md`, `episode-NN-retention-checkpoint.md` | `episodes/EP-NN/survey/` |
| All `episode-NN-*-frames.json`, including survey extraction manifests | `episodes/EP-NN/evidence/` |
| Other single-episode targeted reviews, including Episode 4 reconciliation | `episodes/EP-NN/evidence/` |
| `performance-*` CSV/JSON/Markdown | `performance/` |
| `episode-01-02-melfina-case-review.md`, `startup-sequence-comparison.md`, `startup-open-items-followup.md`, `image-map-reconciliation.md`, `passage-entry-level-reconciliation.md` | `comparisons/` |
| `fan-melfina-pod-reference.md`, `to-be-continued-supplied-reference.md` | `supplied-references/` |
| Episode-specific sections currently inside `animehistory/README.md` | Corresponding episode preparation, survey, alignment or evidence record; enumerate sections before splitting |

Ledger fields: old path (and heading for section moves), new path, record type, producer/owner,
active consumers, byte-preserved or edited, baseline SHA-256, migration status, validation result
and exception rationale. Store the completed textual ledger beside this plan. Every one of the
152 root files must have exactly one disposition; no unlisted deletion or implicit consolidation.

## Audit And Record Ownership

The [file/section migration ledger](reference-index-reorganization-ledger.md) owns the exact
record destinations. The [tool and dependency audit ledger](reference-index-reorganization-tool-audit.md)
owns the tool inventory, active consumers, path classifications and required migration actions.
The [Phase 1.1 baseline](reference-index-reorganization-baseline.json) preserves the pre-migration
hashes and data counts. Keep detailed inventory/findings in those ledgers; this plan owns scope,
sequence, checklists and gates. Phase 2's concise tool directory will link existing usage manuals.

## Tool Consolidation And Output Ownership

**Scope amendment — 2026-10-31:** consolidate the 33 inventoried local helpers under
`tools/historical/local/`, grouped by purpose. The tool audit ledger owns their individual
old/new paths and pre-move hashes. These are additional script moves, separate from the 152
reference-record moves; the accepted Phase 1.1 snapshot remains unchanged.

```text
tools/
├── README.md                         Supported tool/recipe directory
├── reference-extraction/             Maintained extraction/gallery/review tools
├── reference-context/                Maintained cross-site context tools
├── reference-alignment/              Maintained alignment tools
├── unreal/                           Maintained Unreal development helpers
└── historical/
    ├── README.md                     Historical status and navigation
    └── local/                        Ignored; preserve former local-only status
        ├── reference-review/         Episode corrections, previews and old sheet helper
        ├── reference-alignment/      Earlier alignment pilot checks
        ├── reference-workbooks/      Earlier workbook pilot checks
        ├── blender/                  Connectivity pilot scripts
        └── validation/               Historical recovery/fixture checks
```

Install the ignore rule before moving local helper files. Preserve their bytes, timestamps where
practical, hashes and original-location records; do not treat relocation as runtime support or
rewrite old scripts to appear current. Some depend on their former location or host-specific paths.
The historical directory is for inspection, not a supported execution workflow. A reusable helper
can later be promoted into a maintained tool family with explicit routing, documentation and checks;
its archived original remains distinct. Asset recipes retain their asset ownership and are linked
from the central directory. Third-party source, virtual environments and packaged utilities stay
with their dependencies rather than being copied into historical project tools.

Maintained tools write permanent textual evidence to the target index structure and generated
media/workbooks to their established ignored locations. Temporary outputs use task-owned working
directories with bounded cleanup. Do not place new reusable scripts in disposable output folders,
or runtime outputs in `tools`. The audit ledger owns the exact producer/consumer routing changes.
Existing media/archive paths are unchanged; historical scripts are archived rather than rerun to
regenerate their outputs.

## Required process coverage

The implementation covers all four parts of the reorganization proposal:

1. **Map every existing file's destination.** Include records spanning multiple episodes and
   episode-specific sections embedded in shared READMEs. The complete ledger, not just filename
   patterns, controls the moves (Phase 1, executed in Phase 3).
2. **Trace every affected producer and reader.** Include tool output paths, subtitle coverage
   consumers, tests, workbook builders, authored reference fields, documentation links and relevant
   helpers outside `tools`. The separate tool audit ledger owns the inventory; Phase 1 resolves exact
   dependencies and Phase 2 updates their contracts and destinations.
3. **Protect historical provenance.** Distinguish active paths from recorded extraction commands,
   recipes and hashes. Preserve original evidence meaning and approval history; use the migration
   ledger to resolve moved records without rewriting history (Phases 1 and 3).
4. **Check the migration end to end.** Account for every file, verify preserved contents and
   links/anchors, validate registers and affected tools, and confirm unchanged workbook data apart
   from intentional reference-path changes (Phase 4, recorded at Phase 5 closeout).

Structural migration and later editorial consolidation are separate work. Do not use this move to
rewrite findings, merge differing evidence claims or remove older research as allegedly redundant.

## Dependencies And Delivery Sequence

| Phase | Prerequisite | Main checkpoint / acceptance evidence |
| --- | --- | --- |
| 1 — inventory and dependencies | Authorization for bounded inventory work | Complete file/section ledger, tool dependencies and preserved-data baseline |
| 2 — navigation and tool destinations | Phase 1 exit | Documented ownership and coordinated producer/consumer changes |
| 3 — record migration | Phase 2 preparation complete | Ledgered moves and repaired references; coordinated with Phase 2 |
| 4 — integration validation | Phase 3 moves complete | File accounting, links, schemas, tool checks and workbook equivalence |
| 5 — closeout | Phase 4 passes | Actual change/validation record and explicit confirmation for publication |
| 6 — implementation-documentation inventory and dependencies | Phase 4 accepted; Phase 5 prepared state preserved; explicit authorization for Phase 6 | Exact documentation ownership/move ledger, separate baseline and consumer audit |
| 7 — implementation-documentation migration | Phase 6 exit accepted; Phase 7 authorized | Slice/project/shared structure, navigation and coordinated reference repairs |
| 8 — documentation integration validation | Phase 7 migration complete; Phase 8 authorized | File/content accounting, links/anchors and affected reader/writer checks |
| 9 — combined closeout and publication | Phase 8 passes; Phase 9 authorized | Both reorganization components recorded, final acceptance and verified publication |

Unchecked tasks are planned work, not completed evidence. Check an item only after its deliverable
and relevant validation exist. Record phase acceptance separately from task completion/publication.
Phases 2 and 3 form one coordinated migration: neither is an accepted operational checkpoint while
active tools and records use incompatible paths. Do not begin dependent work with a blocking finding.

## Phase 1: Inventory And Dependency Baseline

### Phase 1.1: Complete File And Section Ledger

**Prerequisite:** authorized inventory scope. **Deliverable:** exhaustive migration ledger beside this plan.

- [x] Assign every root file one destination and disposition using the move rules above.
- [x] Enumerate embedded episode sections and their destination records, including cross-episode exceptions.
- [x] Capture Git status, file hashes, register counts and workbook data baselines.

**Completion record — accepted by the maintainer 2026-10-30:** the
[migration ledger](reference-index-reorganization-ledger.md) maps all 152 root files and all 60
AnimeHistory README heading sections, including retained sections and two mixed-content splits.
The [baseline snapshot](reference-index-reorganization-baseline.json) records 193 index-file hashes,
37 CSV tables and three existing workbook projections. Read-only ZIP/XML inspection records saved
cell/formula and link digests without recalculation or a new CSV-to-workbook equality claim.
All 193 protected files remained byte-identical, destinations were absent and no records moved.
The producer roles are preliminary; exact consumers and path classifications remain Phase 1.2.

### Phase 1.2: Tool And Consumer Dependency Audit

**Prerequisite:** 1.1 inventory. **Deliverable:** separate tool and dependency audit ledger.

- [x] Trace tracked tools, tests, documentation links and authored CSV reference fields.
- [x] Inspect relevant helpers outside `tools`; distinguish maintained, local, temporary and vendor code.
- [x] Classify old-path occurrences as active lookups/links, historical commands, stored recipes or prose.
- [x] Resolve destinations and document input/output ownership without changing runtime behavior.

**Completion record — audited 2026-10-30; accepted by the maintainer 2026-10-31:** the
[tool and dependency audit ledger](reference-index-reorganization-tool-audit.md) owns the relocated
tool inventory, static findings and exact consumer change lists. No runtime changes or record moves
were performed. Acceptance includes the 2026-10-31 historical-helper consolidation amendment.
Phase 1 is accepted; Phase 2 remains unstarted and requires subsequent authorization.

**Validation:** every inventoried file/section is accounted for; active dependencies have owners.
**Recovery / deferral:** leave ambiguous records in place and resolve their ownership before migration.

### Phase 1 Exit Gate

- [x] Complete ledger and dependency baseline reviewed; no unassigned file or unresolved destination.
- [x] Record Phase 1 acceptance and the authorized next increment.

**Exit record — accepted by the maintainer 2026-10-31:** Phase 1.1's file/section ledger and
baseline and Phase 1.2's separate tool/dependency audit are accepted, including the 33 planned
historical-helper routes. Confirmation authorizes documentation publication only. Phase 2 is the
next increment; it has not started and is not authorized by this confirmation.

## Phase 2: Navigation And Tool Destinations

**Prerequisite:** Phase 1 exit. **Deliverable:** navigation and coordinated path updates prepared for Phase 3.

- [x] Add index navigation and episode ownership documents.
- [x] Add `tools/README.md` as the maintained directory linking existing tool/recipe owners.
- [x] Decide the working sheet builder's supported or legacy status explicitly.
- [x] Add historical-tool navigation and ignore protection before moving any local helper.
- [x] Verify the 33 historical-script routes and hashes; keep supported entry points separate from archived originals.
- [x] Prepare affected producer, reader, test and command-example updates as a coordinated patch for activation with Phase 3.
- [x] Document permanent, generated and temporary output ownership for each maintained tool family.
- [x] Coordinate activation of path changes with Phase 3 moves; preserve source and no-overwrite protections.

**Completion record — accepted by the maintainer 2026-11-01:** the
[Phase 2 preparation record](reference-index-reorganization-phase-2.md) owns the navigation,
ignore checks, pending routing patch and isolated test results. Live maintained executables retain
the existing layout. New navigation links current records; 193 pre-existing index files and all
33 helper sources remain unchanged. The legacy named-section sheet builder is assigned to history.

**Validation:** every affected producer/consumer is covered by a corresponding ledgered move or explicit exception.
**Recovery / deferral:** keep the last usable layout recoverable; do not accept a half-migrated workflow.

### Phase 2 Exit Gate

- [x] Navigation and tool changes are ready for coordinated migration; remaining dependencies recorded.
- [x] Operational acceptance deferred until Phase 3 records and Phase 4 validation are complete.

Preparation was accepted by the maintainer on 2026-11-01. Phase 3 requires subsequent
authorization. This confirmation publishes preparation only; the routing patch remains unapplied.

## Phase 3: Record Migration And Reference Repair

**Prerequisite:** Phase 2 preparation complete. **Deliverable:** organized records and repaired active references.

- [x] Execute the ledgered moves, preserving filenames and bytes wherever practical.
- [x] Relocate the 33 ledgered local scripts into their historical destinations after ignore protection is verified; preserve hashes and remove only verified source copies.
- [x] Relocate episode README sections with dates, scope limits and acceptance provenance intact.
- [x] Repair maintained Markdown links/anchors and authored CSV references.
- [x] Preserve historical commands, recorded recipes, stable IDs and hashes; record path correspondence in the ledger.
- [x] Confirm archive payloads and local media locations remain unchanged.

**Completion record — accepted by the maintainer 2026-11-01:** the
[Phase 3 migration record](reference-index-reorganization-phase-3.md) records all moves, README
relocation, routing activation and path-only repairs. Checks pass within the recorded scope;
workbooks remain unchanged for Phase 4.

**Validation:** compare actual moves/edits with the ledger; account for old and new paths without duplicate authority.
**Recovery / deferral:** correct or restore only affected paths from the baseline; preserve unrelated edits.

### Phase 3 Exit Gate

- [x] Every planned move is completed or has an explicit reviewed exception.
- [x] Coordinated producer/reader changes are ready for integration checks; migration remains unverified until Phase 4.

Phase 3 was accepted by the maintainer on 2026-11-01 for publication. Phase 4 requires subsequent authorization.

## Phase 4: Integration Validation

### Phase 4.1: Files, References And Tools

**Prerequisite:** Phase 3 exit. **Deliverable:** recorded file, reference and tool check results.

- [x] Verify file accounting and byte-preserved hashes against the baseline.
- [x] Verify all 33 archived helper hashes, unique destinations, source absence and ignored status; confirm no local helper is staged for publication.
- [x] Validate links/anchors, schemas, register counts and affected tool tests.
- [x] Check output routing using temporary fixtures or bounded tests; do not re-extract episodes or replay destructive helpers.
- [x] Verify producers cannot silently recreate the former flat index layout.

### Phase 4.2: Workbook And Evidence Equivalence

**Prerequisite:** 4.1 passes. **Deliverable:** saved-data comparison and affected-link inspection.

- [x] Regenerate annotation and context workbook views using ImportExcel.
- [x] Compare saved authored data and inspect affected workbook links; check locator-only workbook links if affected.
- [x] Allow only documented reference-path changes; preserve observations, timing values, review states and evidence IDs.

**Completion record — accepted by the maintainer 2026-11-01:** the
[Phase 4 validation record](reference-index-reorganization-phase-4.md) records file/hash and
37-register equivalence, maintained-link checks, passing tool suites and two refreshed ImportExcel
views. All 62 workbook tabs retain their data apart from 1,104 reference-path cells and two
hyperlinks; 298 row heights expand for longer paths. The locator workbook remains byte-identical.
Windows temporary-file access failures and the unchanged-suite rerun environment are documented.

**Validation:** maintained consumers resolve the target layout and evidence remains traceable.
**Recovery / deferral:** a failed check blocks closeout; correct the coordinated change and repeat affected checks.

### Phase 4 Exit Gate

- [x] File, reference, tool and workbook checks pass with results and material limits recorded.
- [x] No unexplained evidence/data changes remain.

Phase 4 was accepted by the maintainer on 2026-11-01 for documentation publication. Phase 5
requires subsequent authorization.

## Phase 5: Closeout And Publication

**Prerequisite:** Phase 4 exit. **Deliverable:** completed migration ledger and accepted closeout record.

This phase closes the reference-index component only. Its prepared closeout remains pending while
the documentation extension is planned. Phase 6 may begin after explicit authorization without
misrepresenting Phase 5 as accepted. Phase 9 owns the expanded effort's final closeout; preserve
and resolve the pending component acceptance/publication explicitly there.

- [x] Record actual moves, intentional edits, validation results and unresolved local-helper limitations.
- [x] Update workflow pointers and verify future episode records use the new destinations.
- [ ] Record maintainer acceptance separately from implementation/test completion.
- [ ] On explicit confirmation, review the scoped diff, run diff checks and follow established commit/push verification.

**Validation:** completed ledger matches the final worktree; publication includes only authorized in-scope changes.
**Recovery / deferral:** keep changes uncommitted until confirmation; publication problems do not justify destructive resets.

**Prepared closeout — 2026-11-01; acceptance pending:** the
[closeout record](reference-index-reorganization-closeout.md) links actual migration and validation
evidence, records historical-helper limitations and defines the operating handoff. Current navigation
and the numbered episode workflow use the organized destinations. The frozen baseline and dated
audit tables retain historical paths. No source extraction, media move or workbook regeneration
was performed in Phase 5. Final acceptance/publication remain separate pending steps below.

### Phase 5 Exit Gate

- [ ] Reorganization closeout accepted; publication status and any remaining limitations recorded.

No source media, RAR payload, contact-sheet collection, application configuration or unrelated
temporary directory is moved or deleted by this plan. Historical consolidation covers only the
33 named script files; their surrounding local output directories are not cleanup targets.

## Phase 6: Implementation Documentation Inventory And Dependency Baseline

### Phase 6.1: File Ownership And Move Ledger

**Prerequisite:** explicit authorization for Phase 6; accepted Phase 4 and preserved Phase 5 worktree.
**Deliverable:** separate documentation migration ledger and baseline beside this plan.

- [x] Inventory every current file under `docs/implementation`, including uncommitted files and any newly authorized records.
- [x] Assign each file one exact destination using the agreed slice/project/shared/investigation structure; resolve shared-procedure exceptions.
- [x] Include moves of this plan, the prior reference-index ledgers/baseline and the prepared Phase 5 closeout.
- [x] Capture source hashes, document headings/anchors, Git/worktree status and destination preconditions without modifying the frozen reference-index baseline.
- [x] Record navigation files to create; preserve existing filenames and avoid duplicate authority or empty future-effort scaffolding.

**Completion record — accepted by the maintainer 2026-11-01:** the
[documentation migration ledger](implementation-documentation-migration-ledger.md) maps all 44
existing files, the two new inventory records and four planned navigation files. The separate
[documentation baseline](implementation-documentation-migration-baseline.json) captures file
hashes, 442 ATX headings, source/destination preconditions and the clean starting checkpoint at
`e0ebf1c`. The prior Phase 5 preparation is already published, with component acceptance still
pending; no uncommitted Phase 5 edits existed at capture. All original files matched after snapshot
generation; only this plan receives the subsequent completion/status edit. No files or folders moved.
Phase 6.2 was unstarted at that checkpoint; its subsequent findings are recorded below.

### Phase 6.2: Consumer And Output Audit

**Prerequisite:** 6.1 inventory. **Deliverable:** dependency findings in the separate documentation ledger.

- [x] Trace incoming/outgoing Markdown links and fragments across root documentation, reference records, tools, recipes and scoped local helpers.
- [x] Inspect CSV/JSON reference fields and maintained scripts/configuration for active documentation-path lookups or outputs.
- [x] Distinguish active references from historical commands, frozen snapshots, recipe values and provenance paths; record preservation exceptions.
- [x] Identify any affected generated projections or tool tests; require rebuilds/tests only where the documentation move affects their inputs or behavior.
- [x] Specify future documentation ownership/output conventions so later work does not recreate a flat implementation directory.

**Completion record — accepted by the maintainer 2026-11-01:** the existing
[documentation ledger](implementation-documentation-migration-ledger.md#phase-62-audit-scope-and-checkpoint)
records the 406-file audit, 468 relative-link repairs across 91 consumers, active prose/output
conventions and historical-path exceptions. All current relevant links/fragments resolve. No
maintained runtime or structured-register input requires rerouting, so no workbook refresh or new
runtime tests are required for the planned documentation-only move. No files or live links moved;
both frozen baselines remain unchanged. Phase 7 remains unstarted.

**Validation:** every file has one disposition; every active consumer has a repair or a reviewed
exception; pending worktree edits are accounted for. No moves or runtime changes occur here.
**Recovery / deferral:** resolve ambiguous ownership before migration; retain existing records intact.

### Phase 6 Exit Gate

- [x] Documentation ledger, baseline, placement exceptions and repair scope are reviewed and accepted.
- [x] Record acceptance separately from authorization for Phase 7.

**Exit record — accepted by the maintainer 2026-11-01:** Phase 6.1 inventory and Phase 6.2 audit,
including the slice-specific procedure placement, are accepted for publication. Confirmation does
not authorize Phase 7 moves; Phase 7 requires subsequent authorization. The frozen baseline retains
its pre-acceptance checkpoint values and hashes.

## Phase 7: Implementation Documentation Migration And Navigation

**Prerequisite:** accepted Phase 6 exit and explicit authorization for Phase 7.
**Deliverable:** ledgered documentation layout with repaired active references and navigation.

- [x] Preflight workspace-bounded source/destination paths and hashes, preserving all inventoried uncommitted edits.
- [x] Move files to their exact ledgered destinations, including the reorganization project's own records; preserve baseline JSON bytes and substantive document content.
- [x] Create root/slice/validation navigation with links to authoritative plans, status and the existing roadmap; keep phase results with their owning effort.
- [x] Repair active relative links, fragments and ledgered structured references across consumers in the same coordinated increment.
- [x] Apply only audited producer/reader/example changes needed for current and future documentation paths; preserve historical recipes and commands.
- [x] Record actual dispositions, intentional reference edits and exceptions in the documentation ledger without duplicating research or approval records.

**Completion record — accepted by the maintainer 2026-11-01:** the
[Phase 7 migration record](implementation-documentation-migration-phase-7.md) records 46 checked
moves, four navigation pages, 468 href repairs and three prose/convention repairs. Prepared text
results matched expected values before explicit navigation/status edits. Frozen baselines,
runtime/register inputs and workbook bytes are preserved. Full integration acceptance remains Phase 8.

**Validation:** actual moves match the ledger and new navigation resolves; historical evidence and
pending acceptance remain distinct. Do not accept a half-migrated active workflow.
**Recovery / deferral:** restore or repair only affected files from the captured baseline/worktree
snapshot; preserve unrelated changes and do not run historical helpers.

### Phase 7 Exit Gate

- [x] Every documentation move is complete or has an explicit reviewed exception.
- [x] Active consumers agree on the new layout; full integration acceptance remains Phase 8.

Phase 7 was accepted by the maintainer on 2026-11-01 for publication. Phase 8 requires subsequent
authorization.

## Phase 8: Documentation Integration And Preservation Validation

### Phase 8.1: File, Content And Reference Checks

**Prerequisite:** Phase 7 migration complete and explicit authorization for Phase 8.
**Deliverable:** recorded documentation-preservation and link results.

- [ ] Account for every original/new file, unique destination and original-path disposition; reject accidental duplicate authorities or unlisted deletion.
- [ ] Verify byte-preserved baselines/records and compare edited documents allowing only ledgered navigation/path/status changes.
- [ ] Verify preserved decisions, dates, approval history, phase numbering and substantive headings/anchors.
- [ ] Validate maintained local links and fragments across all affected consumers; keep historical-path and third-party exclusions explicit.
- [ ] Verify source media, reference data, local-only helpers and unrelated application/assets remain outside the migration's changes.

### Phase 8.2: Affected Tools And Future Effort Checks

**Prerequisite:** 8.1 passes. **Deliverable:** bounded consumer/output checks and current navigation review.

- [ ] Test affected maintained readers/writers with temporary fixtures where needed; do not execute historical helpers or source extraction merely to validate documentation paths.
- [ ] If structured reference fields changed, validate their schemas/data preservation and refresh only affected projections using their established authoring/verification workflow.
- [ ] Check that future slice/project records have documented owners and destinations, with reusable procedures separated from phase-specific results.
- [ ] Confirm navigation distinguishes implemented/tested/accepted/deferred work and links the existing roadmap without creating competing status authority.
- [ ] Remove only task-owned migration/validation scratch files after evidence is recorded.

**Validation:** no unexplained content/data change, broken active reference or affected runtime/output
regression remains. Reuse earlier evidence where dependencies are unchanged; state material limits.
**Recovery / deferral:** a failed check blocks closeout; correct and repeat affected checks only.

### Phase 8 Exit Gate

- [ ] File/content, link, consumer and future-ownership checks pass with evidence and limits recorded.
- [ ] Record validation acceptance separately from final Phase 9 closeout/publication.

## Phase 9: Combined Reorganization Closeout And Publication

**Prerequisite:** Phase 8 passes and explicit authorization for Phase 9.
**Deliverable:** final closeout covering both reference indexes and implementation documentation.

- [ ] Reconcile the prepared Phase 5 component closeout with the documentation migration; preserve its completed evidence and resolve its pending acceptance explicitly.
- [ ] Record actual documentation moves, intentional edits, tests, preserved baselines, exceptions and remaining historical-helper limitations using the owning ledgers/results.
- [ ] Update current workflow/navigation pointers and the implementation-effort directory; verify the final documented destinations match the worktree.
- [ ] Record maintainer acceptance separately from implementation/test completion and identify the exact scope authorized for publication.
- [ ] On explicit confirmation, review the scoped diff, run diff checks, stage only in-scope changes, commit/push and verify worktree status plus HEAD/upstream parity.

**Validation:** both components' final records match their ledgers and accepted evidence; publication
contains no source media, derivative frames, ignored helpers or unrelated changes.
**Recovery / deferral:** keep changes uncommitted until confirmation; report unrelated worktree
changes without staging or discarding them. Publication does not authorize Episode 7 or Phase 3.2A.

### Phase 9 Exit Gate

- [ ] Combined closeout accepted; publication status, final ownership pointers and remaining limitations recorded.

Phase 6.1 inventory and 6.2 dependency audit were accepted by the maintainer on 2026-11-01.
Phase 7 migration was subsequently authorized, implemented and accepted on 2026-11-01.
Phases 8–9 remain unstarted; no later execution or project/slice boundary changes are implied.
