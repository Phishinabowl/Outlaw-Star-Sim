# Reference index reorganization plan

| Field | Value |
| --- | --- |
| Created / last edited | 2026-10-30 / 2026-11-01 |
| Status | Phases 1–3 accepted; Phase 4 integration/workbook validation unstarted |
| Maintainer | Repository owner |
| Current checkpoint | Phase 3 migration accepted 2026-11-01; Phase 4 integration/workbook validation unstarted |

The plan and documentation publication were confirmed by the maintainer on 2026-10-30.
Implementation phases require subsequent authorization.
This work supports the [pre-3.2A research checkpoint](vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research);
it does not start Episode 7 or Phase 3.2A.
Phase numbers below belong to this reorganization plan, not the vertical-slice implementation phases.

## Objective and observed baseline

Organize maintained evidence by source, episode and research purpose; document tool ownership
and output destinations so future reviews do not recreate the flat directory.

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

- [ ] Verify file accounting and byte-preserved hashes against the baseline.
- [ ] Verify all 33 archived helper hashes, unique destinations, source absence and ignored status; confirm no local helper is staged for publication.
- [ ] Validate links/anchors, schemas, register counts and affected tool tests.
- [ ] Check output routing using temporary fixtures or bounded tests; do not re-extract episodes or replay destructive helpers.
- [ ] Verify producers cannot silently recreate the former flat index layout.

### Phase 4.2: Workbook And Evidence Equivalence

**Prerequisite:** 4.1 passes. **Deliverable:** saved-data comparison and affected-link inspection.

- [ ] Regenerate annotation and context workbook views using ImportExcel.
- [ ] Compare saved authored data and inspect affected workbook links; check locator-only workbook links if affected.
- [ ] Allow only documented reference-path changes; preserve observations, timing values, review states and evidence IDs.

**Validation:** maintained consumers resolve the target layout and evidence remains traceable.
**Recovery / deferral:** a failed check blocks closeout; correct the coordinated change and repeat affected checks.

### Phase 4 Exit Gate

- [ ] File, reference, tool and workbook checks pass with results and material limits recorded.
- [ ] No unexplained evidence/data changes remain.

## Phase 5: Closeout And Publication

**Prerequisite:** Phase 4 exit. **Deliverable:** completed migration ledger and accepted closeout record.

- [ ] Record actual moves, intentional edits, validation results and unresolved local-helper limitations.
- [ ] Update workflow pointers and verify future episode records use the new destinations.
- [ ] Record maintainer acceptance separately from implementation/test completion.
- [ ] On explicit confirmation, review the scoped diff, run diff checks and follow established commit/push verification.

**Validation:** completed ledger matches the final worktree; publication includes only authorized in-scope changes.
**Recovery / deferral:** keep changes uncommitted until confirmation; publication problems do not justify destructive resets.

### Phase 5 Exit Gate

- [ ] Reorganization closeout accepted; publication status and any remaining limitations recorded.

No source media, RAR payload, contact-sheet collection, application configuration or unrelated
temporary directory is moved or deleted by this plan. Historical consolidation covers only the
33 named script files; their surrounding local output directories are not cleanup targets.
