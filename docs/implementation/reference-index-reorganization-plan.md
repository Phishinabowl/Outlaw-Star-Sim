# Reference index reorganization plan

| Field | Value |
| --- | --- |
| Created / last edited | 2026-10-30 / 2026-10-30 |
| Status | Plan accepted by the maintainer on 2026-10-30; migration and tool changes unimplemented |
| Maintainer | Repository owner |
| Current checkpoint | Phase 1.1 inventory accepted 2026-10-30; Phase 1.2 dependency audit unstarted |

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

## Tool and helper inventory

This inventory records discovered locations and roles, not a new execution or runtime certification.
Maintained scripts were enumerated from Git; local helpers were found by filesystem inspection.
Repository-external installations and previously deleted helpers are not exhaustively inventoried.
Executable content is not invoked during planning.

### Maintained reference tools

| Location / files | Role and output ownership | Migration impact |
| --- | --- | --- |
| `tools/reference-extraction/inventory.py` | Source inventory and settei contact sheets; writes root `source-manifest.json` | Change manifest destination; retain media destination |
| `tools/reference-extraction/inspect_episode.py` | FFprobe inspection; writes root episode metadata JSON | Route metadata to episode preparation |
| `tools/reference-extraction/extract_reference_frames.py` | Bounded explicit frame extraction; root provenance JSON plus ignored frames/logs | Route manifest to episode evidence; preserve no-overwrite and source protections |
| `tools/reference-extraction/scan_performance_subtitles.py` | All-episode subtitle extraction/search; root coverage JSON and ignored ASS/candidate text | Change coverage destination and all consumers; do not rerun whole audit just to migrate |
| `tools/reference-extraction/cache_timestamp_index.py` | Cache gallery HTML and build locator CSVs/manifest | Existing `animehistory` ownership retained |
| `tools/reference-extraction/episode_gallery.py` | Gallery preparation, sheets, archive, verified restore/prune and supplements | Existing cache/archive ownership retained; audit embedded references |
| `tools/reference-extraction/category_index.py` | Annotation schema, validation and workbook projection input | Audit authored reference fields and links |
| `tools/reference-extraction/build_animehistory_workbook.ps1` | Locator-only ImportExcel view | Audit links; existing workbook destination retained |
| `tools/reference-extraction/build_category_workbook.ps1` | Annotation/alignment ImportExcel view | Update subtitle coverage input and any moved record links |
| `tools/reference-alignment/alignment.py` | Bounded frame search from selected plans | Update documented plan locations and coverage lookup; working outputs stay local |
| `tools/reference-alignment/models.py` | Reviewed anchors and fitted mapping registers | Shared registers retained; audit reference handling |
| `tools/reference-alignment/projection.py` | Joined timing/availability projection | Update coverage lookup |
| `tools/reference-alignment/reproduce.py` | Reproduce selected reviewed frame evidence | Preserve recorded recipes and hashes |
| `tools/reference-alignment/finish.py` | Preview and apply owned alignment-run cleanup | Preserve cleanup boundaries; audit references |
| `tools/reference-context/context_tool.py` | Context CLI: retrieve, inspect, verify and validate selected content | Shared context ownership retained; audit links |
| `tools/reference-context/animehistory.py`, `fandom.py` | Site adapters | No site behavior changes planned |
| `tools/reference-context/core.py` | Shared storage, safety and transaction support | No unrelated refactor |
| `tools/reference-context/views.py`, `build_context_workbook.ps1` | Context projection and ImportExcel view | Repair moved evidence links; retain workbook destination |

Existing usage/contracts live in each reference tool directory's README. Tests are supporting code,
not additional operational commands: extraction has `test_category_index.py`, `test_episode_gallery.py`;
context has `test_animehistory.py`, `test_context.py`, `test_views.py`; alignment has
`test_alignment.py`, `test_episodes.py`, `test_finish.py`, `test_models.py`, `test_projection.py`,
`test_reproduce.py`. Update fixtures and expectations where migrated paths require it.

### Other maintained project scripts

| Location / files | Purpose and runtime | Disposition |
| --- | --- | --- |
| `tools/unreal/create_scale_test_lab.py` | Create owned Phase 3.1 test map through Unreal editor Python | Inventory only; no map execution/change |
| `tools/unreal/verify_scale_handoff.py` | Inspect saved handoff packages through Unreal Python | Inventory only |
| `assets/recipes/create_scale_handoff.py` | Create owned rigid-mesh handoff fixture inside Blender | Retain with asset recipes |
| `assets/recipes/add_scale_handoff_uvs.py` | Add fixture UV coordinates inside Blender | Retain with asset recipes |
| `assets/recipes/export_scale_handoff.py` | Export selected owned Blender handoff meshes | Retain with asset recipes |
| `assets/recipes/revise_scale_handoff_flap.py` | Deliberate fixture revision for reimport proof | Retain historical/pilot role |
| `assets/recipes/create_handoff_marker_materials.py` | Create Unreal marker materials through the pilot tool execution interface | Retain with asset recipes |
| `Unreal/OutlawStarSim/Plugins/VisualStudioTools/Scripts/Package-Plugin.ps1` | Third-party Visual Studio integration packaging script | Identify as vendor code; no reorganization |

No `tools/unreal/README.md` or central `tools/README.md` currently provides a complete tool directory.
Phase 2 should add a concise maintained tool directory linking existing owners rather than copying
their command manuals. Asset recipes remain discoverable there without moving them into `tools`.

### Local and temporary helpers outside `tools`

| Location / files | Observed role | Proposed treatment |
| --- | --- | --- |
| `reference/working/build_review_sheets.py` | Builds 12-image named-section sheets from extracted-frame manifests; assumes the current index root | Review for promotion to a documented maintained helper, or label legacy; update before reuse. Not covered by gallery-sheet tooling automatically |
| `.local/blender-pilot/probe_bridge.py` | Read-only MCP handshake/inventory | Host-local pilot helper; retain ignored |
| `.local/blender-pilot/create_connectivity_fixture.py`, `remove_connectivity_cube.py` | Create/remove owned Blender connectivity fixture | Host-local, asset-mutating pilot helpers; not ordinary review commands |
| `.local/validation/phase-3-1/inspect_test_lab.py`, `verify_finished_test_lab.py` | Unreal test-lab inspection/verification | Local historical validation helpers |
| `.local/validation/phase-3-1/verify_blender_recovery.py`, `verify_unreal_recovery.py` | Recovery verification in application runtimes | Local historical recovery helpers; inspect host paths before reuse |
| `.tmp/screen_ep04_first.py`, `screen_ep04_025_096.py`, `screen_ep04_097_168.py`, `screen_ep04_169_240.py`, `screen_ep04_241_312.py`, `screen_ep04_313_354.py`, `refine_ep04_025_096.py` | One-off Episode 4 annotation scripts | Inventory as temporary; no replay against current indexes |
| `.tmp/correct_ep04_first.py`, `correct_ep04_111_167.py`, `correct_ep04_239.py`, `correct_ep04_anchor_dropship.py`, `correct_ep04_el_dorado.py`, `correct_horus_add_grapple.py`, `fix_ep04_344.py`, `confirm_ep04_022.py` | One-off correction/checkpoint scripts | Inspect before any future use; filenames do not establish safety or idempotence |
| `.tmp/add_ep04_manual_references.py`, `add_halcyon_flight.py`, `add_halcyon_supplements.py`, `adopt_initial_review_status.py` | Historical supplement/status changes | Temporary migration history, not supported entry points |
| `.tmp/ep04_cleanup_baseline.py`, `verify_ep04_cleanup.py` | Episode 4 cleanup checks | Temporary historical validation |
| `.tmp/category_preview_montage.py`, `category-preview.mjs` | Local visual previews | Temporary visualization helpers |
| `.tmp/alignment-stage5/validate_pilot.py`, `.tmp/animehistory-workbook/build-importexcel-test.ps1` | Historical tool/workbook pilot checks | Temporary validation helpers |
| `.local/blender-pilot/source/blender_mcp/`, its virtual environment, `.local/packages/` | Third-party source, runtime activation scripts, bundled application utilities | Record by package/family; exclude vendor internals from maintained project-tool count |

These local files remain ignored. This plan does not authorize deleting, publishing or promoting
them wholesale. Most have not had a fresh behavior audit. The working sheet builder is a concrete
dependency missed by a search limited to tracked `tools` files.

## Required process coverage

The implementation covers all four parts of the reorganization proposal:

1. **Map every existing file's destination.** Include records spanning multiple episodes and
   episode-specific sections embedded in shared READMEs. The complete ledger, not just filename
   patterns, controls the moves (Phase 1, executed in Phase 3).
2. **Trace every affected producer and reader.** Include tool output paths, subtitle coverage
   consumers, tests, workbook builders, authored reference fields, documentation links and relevant
   helpers outside `tools`. The inventory above is the starting point; Phase 1 resolves exact
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

**Prerequisite:** 1.1 inventory. **Deliverable:** producer/consumer dependencies in the ledger.

- [ ] Trace tracked tools, tests, documentation links and authored CSV reference fields.
- [ ] Inspect relevant helpers outside `tools`; distinguish maintained, local, temporary and vendor code.
- [ ] Classify old-path occurrences as active lookups/links, historical commands, stored recipes or prose.
- [ ] Resolve destinations and document input/output ownership without changing runtime behavior.

**Validation:** every inventoried file/section is accounted for; active dependencies have owners.
**Recovery / deferral:** leave ambiguous records in place and resolve their ownership before migration.

### Phase 1 Exit Gate

- [ ] Complete ledger and dependency baseline reviewed; no unassigned file or unresolved destination.
- [ ] Record Phase 1 acceptance and the authorized next increment.

## Phase 2: Navigation And Tool Destinations

**Prerequisite:** Phase 1 exit. **Deliverable:** navigation and coordinated path updates prepared for Phase 3.

- [ ] Add index navigation and episode ownership documents.
- [ ] Add `tools/README.md` as the maintained directory linking existing tool/recipe owners.
- [ ] Decide the working sheet builder's supported or legacy status explicitly.
- [ ] Update affected producers, readers, tests and command examples to the target destinations.
- [ ] Coordinate activation of path changes with Phase 3 moves; preserve source and no-overwrite protections.

**Validation:** every affected producer/consumer is covered by a corresponding ledgered move or explicit exception.
**Recovery / deferral:** keep the last usable layout recoverable; do not accept a half-migrated workflow.

### Phase 2 Exit Gate

- [ ] Navigation and tool changes are ready for coordinated migration; remaining dependencies recorded.
- [ ] Operational acceptance deferred until Phase 3 records and Phase 4 validation are complete.

## Phase 3: Record Migration And Reference Repair

**Prerequisite:** Phase 2 preparation complete. **Deliverable:** organized records and repaired active references.

- [ ] Execute the ledgered moves, preserving filenames and bytes wherever practical.
- [ ] Relocate episode README sections with dates, scope limits and acceptance provenance intact.
- [ ] Repair maintained Markdown links/anchors and authored CSV references.
- [ ] Preserve historical commands, recorded recipes, stable IDs and hashes; record path correspondence in the ledger.
- [ ] Confirm archive payloads and local media locations remain unchanged.

**Validation:** compare actual moves/edits with the ledger; account for old and new paths without duplicate authority.
**Recovery / deferral:** correct or restore only affected paths from the baseline; preserve unrelated edits.

### Phase 3 Exit Gate

- [ ] Every planned move is completed or has an explicit reviewed exception.
- [ ] Coordinated producer/reader changes are ready for integration checks; migration remains unverified until Phase 4.

## Phase 4: Integration Validation

### Phase 4.1: Files, References And Tools

**Prerequisite:** Phase 3 exit. **Deliverable:** recorded file, reference and tool check results.

- [ ] Verify file accounting and byte-preserved hashes against the baseline.
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
temporary directory is moved or deleted by this plan.
