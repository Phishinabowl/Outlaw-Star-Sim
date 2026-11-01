# Tool and dependency audit ledger — Phase 1.2

Status: Phase 1.2 audit accepted 2026-10-31; Phase 3 migration/routing implemented and accepted 2026-11-01.
Audit date: 2026-10-30 (America/New_York); consolidation scope amended and accepted 2026-10-31.

This ledger owns the tool inventory and producer/consumer findings for the
[reorganization plan](reference-index-reorganization-plan.md). The separate
[file/section migration ledger](reference-index-reorganization-ledger.md) owns destinations;
the accepted [Phase 1.1 baseline](reference-index-reorganization-baseline.json) remains frozen.
Inventory material formerly in the plan is relocated here; the plan owns execution checklists.

The tables and source line numbers below describe the static pre-migration audit. The
[Phase 3 migration record](reference-index-reorganization-phase-3.md) now owns activation and
preservation results; active references have been repaired and historical helpers have moved.
The [accepted Phase 4 validation](reference-index-reorganization-phase-4.md) records passing
runtime/routing tests and workbook equivalence. The [closeout record](reference-index-reorganization-closeout.md)
owns final acceptance/publication status and remaining helper limitations. Pre-migration dependency
tables and source line numbers below remain historical; the [tool directory](../../tools/README.md)
owns current supported entry points and output locations.

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

The 2026-10-31 amendment assigns these local scripts historical destinations under `tools` while
preserving ignored status. No moves have been performed. Publication or promotion to supported
entry points is separate. Static inspection below does not certify runtime behavior. The working sheet builder is a concrete
dependency missed by a search limited to tracked `tools` files.

### Supporting Runtimes And External Utilities

These are dependencies of the scripts, not additional maintained project entry points. This audit
records how the code uses them; it does not install anything or reverify host versions.

| Dependency | Role / discovery | Reorganization action |
| --- | --- | --- |
| Python and Pillow | Reference CLIs; Pillow image decoding, contact sheets and alignment scoring | Retain installed runtime; no package changes |
| FFmpeg / FFprobe | Metadata, subtitle extraction, bounded decoded frames and alignment; legacy scripts discover PATH, alignment CLI accepts executable arguments | Retain media commands and source limits |
| PowerShell / ImportExcel | Three workbook builders; category/context builders require ImportExcel 7.8.10 or later | Retain installed module and saved-data checks |
| WinRAR CLI | `episode_gallery.py:406` checks PATH then Program Files for `WinRAR/Rar.exe`; archive/restore/integrity operations | Keep archives, executable discovery and receipt semantics unchanged |
| Node / artifact-tool | Local `.mjs` workbook preview helper; outside normal CSV-to-XLSX authoring | Preview only if later validation needs it; no runtime relocation |
| Blender / Unreal Python and MCP pilots | Asset recipes and local development/recovery checks | Inventory only; no application execution required for index migration |
| Third-party package sources and virtual environments | Local Blender MCP checkout, package utilities and activation scripts | Keep package ownership separate; no vendor-source migration |

## Audited Reference Dependencies

Static inspection completed 2026-10-30; accepted by the maintainer 2026-10-31. No reference files or tool behavior changed.
Tracked-source baseline: `e93922d` (the accepted Phase 1.1 commit). Scope: 318 project text files
from the tracked inventory, plus 33 present local helper scripts outside vendor/runtime trees.
Migration plan/ledger/baseline documents are excluded from dependency counts because their old paths
are intentional migration mappings. Vendor plugin internals and downloaded package/virtual-environment
internals are inventoried by family, not audited as maintained project tools. No external host-wide search,
network requests, application automation, media restoration or executable helper replay was performed.

### Classification And Migration Actions

| Class | Required treatment |
| --- | --- |
| Active output/input path | Change producer/consumer together in Phases 2–3. Preserve output safety checks and local-media boundaries. |
| Active Markdown link | Rebase from relocated source to relocated or retained target. For moved README sections use SEC IDs from the file ledger; preserve original anchors or explicit landing aliases. |
| Active authored evidence pointer | Update path/fragment only; retain evidence ID, attribution, status and original claim. Validators must still resolve it. |
| Authored prose pointer | Replace a full obsolete path only. Retain basename-only mentions where the unchanged filename and ledger unambiguously identify the record. Do not rewrite research wording. |
| Historical command/recipe/hash | Preserve bytes and original identity; use old-to-new ledger correspondence for navigation. New commands use current destinations. |
| Local legacy helper | Retain ignored and do not replay. Record affected lookup or emitted text before any later authorized reuse. |
| Unchanged shared input | Preserve path/schema/parser headings; audit is evidence for no change, not a request to refactor. |

### Active Code Changes Required

Locations below are baseline line numbers. FILE destinations come from the file ledger; episode templates apply beyond the episodes already reviewed.

| Baseline location | Producer/consumer action |
| --- | --- |
| `tools/reference-extraction/inventory.py:11–25` | Write the source manifest under `reference/indexes/sources/`; leave source inventory logic and settei sheet destination unchanged. |
| `tools/reference-extraction/inspect_episode.py:31–33` | Write `episode-NN-metadata.json` under `episodes/EP-NN/preparation/`; retain source selection and metadata semantics. |
| `tools/reference-extraction/extract_reference_frames.py:52–63,95–99` | Write manifests under `episodes/EP-NN/evidence/`; ensure the nested index parent exists before use. Keep frame/log paths, recorded commands and no-overwrite checks. |
| `tools/reference-extraction/scan_performance_subtitles.py:34–36,87` | Move coverage JSON output lookup to `performance/`; retain refusal on existing outputs and current ignored subtitle/candidate directory. No audit re-extraction needed. |
| `tools/reference-alignment/alignment.py:237,381` | Read/pin moved subtitle coverage JSON in both input inspection and search; retain source/subtitle/locator identity fields. |
| `tools/reference-alignment/projection.py:36` | Read moved coverage path; otherwise routine workbook refresh would silently derive missing/stale availability. |
| `tools/reference-extraction/build_category_workbook.ps1:14` | Hash the moved coverage input as part of stale-input protection. |
| `tools/reference-alignment/test_alignment.py:134`; `test_projection.py:101` | Place temporary coverage fixtures at the new path. Test the new path without keeping a fallback that conceals wrong output routing. |
| `reference/working/build_review_sheets.py:9` | Legacy manifest lookup currently joins an index-root basename. Require an explicit new relative manifest path or a documented episode/evidence destination before reuse. Its separate 12-frame sheets are not the 24-image gallery sheets. |

The three older extraction writers have no dedicated path-routing tests today. Phase 4 must verify
their new destinations with bounded/temporary fixtures; existing gallery tests do not prove those writers.
The working sheet helper is classified LEGACY_NOT_SUPPORTED for the routine gallery workflow; promotion
would require explicit maintained placement/documentation and relevant checks in Phase 2. It remains untouched.

### Shared Readers And Invariants To Preserve

| Reader / location | Audited dependency and action |
| --- | --- |
| `category_index.py:30–49` | Parses `animehistory/README.md` by exact field-contract/tag headings and table delimiters. Keep these sections and their controlled values in place when moving episode history. |
| `category_index.py:119–124` | Validates `detail_references` as existing repository-relative files. Update the 58 affected CSV references during migration; file moves alone break validation. |
| `core.py:507–526` in `tools/reference-context` | EVIDENCE `target_id` validation checks Markdown file existence and generated/explicit fragment anchors. Update both affected context targets, preserving the Episode 2 anchor. |
| `views.py:89–94`, `build_context_workbook.ps1` | EVIDENCE target IDs become local file URLs. Rebuild context workbook after target updates; source URLs and image link ownership stay unchanged. |
| `alignment.py:328–354,392` | CLI supplies the plan path; selection-plan digest uses canonical content rather than its filename. Move authored plan JSON byte-for-byte and update invocation/document links; do not refit mappings. |
| `models.py:133–135`; `reproduce.py:22–44` | Recipes retain original implementation hash, command windows and accepted frame hashes. Reproduction parses bounded windows, not arbitrary recorded commands. A path-only code edit does not authorize updating old implementation hashes. |
| `finish.py:89–93`, `models.py:33,101`, `views.py:8,17,107`, `context_tool.py:133–137` | Shared CSV paths in `animehistory`/`context` remain in place. No runtime path changes required here. |
| `cache_timestamp_index.py`, `episode_gallery.py`, `build_animehistory_workbook.ps1` | Locator tables, gallery cache, archive receipts/payloads and sheet paths remain unchanged. Do not migrate media or rewrite archive recovery metadata. |
| Remaining tests and adapters in the inventory | Shared fixture paths and schema/readme contracts remain valid; rerun affected suites after implementation, not during this static audit. |
| `assets/recipes/*`, `tools/unreal/*`, seven `.local` Blender/recovery scripts | No index-root dependency found in the inspected scripts. Retain current placement/runtime ownership; no Blender/Unreal run required for this reorganization. |

### Authored CSV Reference Fields

The audit found 1,737 field cells containing a moved-record filename or active index evidence pointer.
These are reference occurrences, not 1,737 changed research claims. A field may contain multiple targets.
Full obsolete paths require targeted replacement; bare filenames can remain when unique and unchanged.
Rows below use CSV record ordinals with the header counted as 1, not physical lines (quoted fields can span lines).
FILE IDs resolve through the file ledger. Multiple matching fields/targets can refer to the same record.

| CSV / field | Matched cells | Full old-path cells | Treatment |
| --- | ---: | ---: | --- |
| `reference/indexes/animehistory/category-index.csv` / `detail_references` | 58 | 58 | Update active pointer paths |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | 641 | 641 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/animehistory/category-index.csv` / `uncertainties` | 354 | 354 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/animehistory/supplemental-index.csv` / `reported_context` | 4 | 4 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/animehistory/supplemental-index.csv` / `uncertainties` | 9 | 9 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/context/context.csv` / `uncertainties` | 1 | 1 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/context/links.csv` / `notes` | 541 | 0 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/context/links.csv` / `target_id` | 2 | 2 | Update active pointer paths |
| `reference/indexes/context/subjects.csv` / `identification_cues` | 2 | 0 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/settei-screening.csv` / `image_map_disposition` | 3 | 0 | Path-only prose repairs; retain basename-only references |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | 122 | 81 | Path-only prose repairs; retain basename-only references |

Exact active pointers: 58 `category-index.csv.detail_references` cells point to FILE-013
(`episode-01-subtitle-context-review.md`); CTXLINK-000076 points to FILE-072
(`episode-04-startup-review.md`); CTXLINK-000258 points to FILE-018
(`episode-02-context-preparation.md#horus-two-jump-dialogue-check`). FILE IDs in this sentence
are verified against the separate accepted file ledger; record ordinals provide an independent lookup.

| CSV / field | Target FILE ID | Record ordinals |
| --- | --- | --- |
| `reference/indexes/animehistory/category-index.csv` / `detail_references` | FILE-013 | 12–20, 25–73 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-005 | 74–145 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-007 | 146–217 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-009 | 218–289 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-011 | 290–355 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-023 | 356–427 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-024 | 462–473 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-025 | 428–499 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-026 | 519–524 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-027 | 500–571 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-028 | 572–643 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-030 | 644–709 |
| `reference/indexes/animehistory/category-index.csv` / `reported_context` | FILE-147 | 1293, 1297–1299, 1302 |
| `reference/indexes/animehistory/category-index.csv` / `uncertainties` | FILE-067 | 1064–1417 |
| `reference/indexes/animehistory/supplemental-index.csv` / `reported_context` | FILE-147 | 4–7 |
| `reference/indexes/animehistory/supplemental-index.csv` / `uncertainties` | FILE-067 | 2–10 |
| `reference/indexes/context/context.csv` / `uncertainties` | FILE-067 | 15 |
| `reference/indexes/context/links.csv` / `notes` | FILE-023 | 267–299 |
| `reference/indexes/context/links.csv` / `notes` | FILE-025 | 300–348 |
| `reference/indexes/context/links.csv` / `notes` | FILE-027 | 351–425 |
| `reference/indexes/context/links.csv` / `notes` | FILE-028 | 426–514 |
| `reference/indexes/context/links.csv` / `notes` | FILE-030 | 515–583 |
| `reference/indexes/context/links.csv` / `notes` | FILE-036 | 612–647 |
| `reference/indexes/context/links.csv` / `notes` | FILE-037 | 652–678 |
| `reference/indexes/context/links.csv` / `notes` | FILE-038 | 679–708 |
| `reference/indexes/context/links.csv` / `notes` | FILE-039 | 709–735 |
| `reference/indexes/context/links.csv` / `notes` | FILE-040 | 736–770 |
| `reference/indexes/context/links.csv` / `notes` | FILE-050 | 771–793 |
| `reference/indexes/context/links.csv` / `notes` | FILE-067 | 794–841 |
| `reference/indexes/context/links.csv` / `target_id` | FILE-018 | 259 |
| `reference/indexes/context/links.csv` / `target_id` | FILE-072 | 77 |
| `reference/indexes/context/subjects.csv` / `identification_cues` | FILE-027 | 35–36 |
| `reference/indexes/settei-screening.csv` / `image_map_disposition` | FILE-107 | 29, 39 |
| `reference/indexes/settei-screening.csv` / `image_map_disposition` | FILE-146 | 44 |
| `reference/indexes/settei-screening.csv` / `image_map_disposition` | FILE-148 | 29 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-107 | 33, 39, 82, 100, 103–104, 129–134, 176–178, 219 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-112 | 2–5 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-113 | 6–9 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-114 | 10–13 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-115 | 14–17 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-116 | 18–21 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-117 | 22–25 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-118 | 26–29 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-119 | 30–33 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-120 | 34–37 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-121 | 38–41 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-122 | 42–45 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-123 | 46–49 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-124 | 50–53 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-125 | 54–57 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-126 | 58–61 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-127 | 62–65 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-128 | 66–69 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-129 | 70 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-130 | 71–80 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-131 | 81–90 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-132 | 91–100 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-133 | 101–110 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-148 | 83, 86–88, 92, 98, 196–197 |
| `reference/indexes/settei-screening.csv` / `measurements_callouts` | FILE-150 | 24, 26, 93–94, 96–97, 99, 109, 198 |

### Markdown Consumer Change List

832 parsed local Markdown links across 103 source files need rebasing or retargeting because
the source file/section or target moves. All current target files exist; all 150 Markdown fragments
in this affected set resolve under the context validator heading-slug/explicit-anchor rules.
This is a static baseline, not a claim about external websites or links outside the affected set.

For each listed source, parse links at these baseline lines. Resolve each target against the old
source directory, apply the FILE destination map and SEC section map, then express the link relative
to its new source directory. This also rebases links to unchanged source media, tools and docs.
Keep retained shared contract anchors intact. Mixed section splits use the explicit line boundaries
in the file ledger; do not treat their entire parent section as moved.

| Source at audit baseline | Affected link count | Baseline lines |
| --- | ---: | --- |
| `README.md` | 2 | 47 |
| `docs/implementation/phase-1-2-closeout-proposal.md` | 1 | 32 |
| `docs/implementation/phase-1-2-cockpit-motion-proposal.md` | 4 | 11, 20–21, 90 |
| `docs/implementation/phase-1-2-engineering-clearance-proposal.md` | 2 | 16, 22 |
| `docs/implementation/phase-1-2-reservation-audit.md` | 3 | 22–24 |
| `docs/implementation/phase-1-2-spatial-motion-decision-packet.md` | 9 | 35, 59, 130, 155, 204, 238, 451, 496, 592 |
| `docs/implementation/phase-1-3-action-readiness-draft.md` | 5 | 75, 176, 192, 237, 531 |
| `docs/implementation/vertical-slice-1-implementation-plan.md` | 49 | 49, 692, 698, 703, 707, 712, 718, 724, 736, 742, 749, 756, 763, 770, 776, 786, 788, 795, 802, 810, 816, 824, 831, 838, 843, 851, 859, 877, 883, 889, 895, 899, 904, 910, 917, 924, 930, 937, 942, 948, 954, 960, 968, 976, 984, 993, 1256, 1483–1484 |
| `docs/reconstruction/baseline-v1/motion-clearance-envelopes.md` | 4 | 12 |
| `docs/reconstruction/baseline-v1/operational-state-baseline.md` | 7 | 40, 42, 59, 72, 74 |
| `docs/reconstruction/baseline-v1/spatial-constraint-map.md` | 4 | 16 |
| `docs/reconstruction/component-evidence-matrix.md` | 8 | 5, 13, 39, 44, 53, 57, 75 |
| `docs/reconstruction/open-questions.md` | 10 | 41, 50, 52, 54, 56, 82, 84, 86, 94, 96 |
| `docs/reconstruction/reference-phase-progress.md` | 16 | 16–17, 19, 52, 56, 62, 66, 70–71, 75, 83, 85, 89, 93 |
| `docs/reconstruction/room-evidence-matrix.md` | 4 | 22, 24, 30, 44 |
| `docs/reconstruction/xgp-reference-index.md` | 15 | 9, 11, 13, 18, 22–25, 76, 78, 82, 84 |
| `docs/roadmap.md` | 2 | 19, 21 |
| `reference/README.md` | 14 | 13, 23, 27, 29, 31, 33, 35–37, 39 |
| `reference/indexes/animehistory/README.md` | 47 | 59, 92, 94, 96, 203–204, 434, 718, 891, 909, 928, 946, 966, 987, 1004, 1019, 1033, 1047, 1062, 1077, 1087, 1130, 1143, 1159, 1173, 1184, 1196, 1208, 1222, 1237, 1250, 1259, 1286, 1301, 1346, 1853, 1872, 1896–1897, 1982–1983, 2063–2064, 2155–2156, 2253–2254 |
| `reference/indexes/episode-01-02-melfina-case-review.md` | 4 | 9, 13–14, 16 |
| `reference/indexes/episode-01-review-batch-02.md` | 1 | 12 |
| `reference/indexes/episode-01-review-batch-03.md` | 1 | 15 |
| `reference/indexes/episode-01-review-batch-04.md` | 1 | 16 |
| `reference/indexes/episode-01-review-batch-05.md` | 2 | 17, 119 |
| `reference/indexes/episode-01-subtitle-context-review.md` | 3 | 14, 26, 135 |
| `reference/indexes/episode-02-alignment-review.md` | 5 | 9, 22, 38, 84, 86 |
| `reference/indexes/episode-02-context-preparation.md` | 2 | 27, 93 |
| `reference/indexes/episode-02-review-batch-01.md` | 2 | 14, 20 |
| `reference/indexes/episode-02-review-batch-02.md` | 2 | 12, 20 |
| `reference/indexes/episode-02-review-batch-03.md` | 2 | 13, 24 |
| `reference/indexes/episode-02-review-batch-04.md` | 3 | 12, 18, 114 |
| `reference/indexes/episode-02-review-batch-05.md` | 3 | 13, 25, 105 |
| `reference/indexes/episode-03-alignment-review.md` | 4 | 9, 16, 70–71 |
| `reference/indexes/episode-03-context-preparation.md` | 2 | 5, 17 |
| `reference/indexes/episode-03-review-batch-01.md` | 2 | 12, 24 |
| `reference/indexes/episode-03-review-batch-02.md` | 2 | 11, 18 |
| `reference/indexes/episode-03-review-batch-03.md` | 1 | 13 |
| `reference/indexes/episode-03-review-batch-04.md` | 1 | 15 |
| `reference/indexes/episode-03-review-batch-05.md` | 2 | 24, 126 |
| `reference/indexes/episode-04-alignment-review.md` | 6 | 6, 11, 15–16, 70–71 |
| `reference/indexes/episode-04-cockpit-case-staging-review.md` | 3 | 9, 11, 29 |
| `reference/indexes/episode-04-cockpit-headroom-review.md` | 2 | 9, 22 |
| `reference/indexes/episode-04-context-preparation.md` | 3 | 9, 12, 24 |
| `reference/indexes/episode-04-entry-hall-review.md` | 4 | 4, 11, 14, 18 |
| `reference/indexes/episode-04-hatch-location-review.md` | 2 | 10, 12 |
| `reference/indexes/episode-04-hilda-laptop-screen-review.md` | 2 | 12, 46 |
| `reference/indexes/episode-04-inspection.md` | 6 | 3, 26–27, 35, 45 |
| `reference/indexes/episode-04-opening-bootstrap-review.md` | 14 | 3–4, 10, 15, 19, 21, 29–34, 43, 69 |
| `reference/indexes/episode-04-reconciliation-review.md` | 12 | 5, 142–150 |
| `reference/indexes/episode-04-startup-review.md` | 9 | 3, 11–12, 16, 65, 73 |
| `reference/indexes/episode-05-alignment-review.md` | 3 | 5, 10, 66 |
| `reference/indexes/episode-05-context-preparation.md` | 2 | 5, 31 |
| `reference/indexes/episode-06-alignment-review.md` | 3 | 5, 10, 67 |
| `reference/indexes/episode-06-context-preparation.md` | 3 | 5, 10, 26 |
| `reference/indexes/episode-11-subether-review.md` | 10 | 7, 15–17, 60, 97 |
| `reference/indexes/episode-26-platform-review.md` | 5 | 7, 9, 33, 35 |
| `reference/indexes/episode-index.md` | 11 | 3, 5, 13, 15, 17, 19, 27 |
| `reference/indexes/external-sources.md` | 4 | 16, 19–21 |
| `reference/indexes/fan-melfina-pod-reference.md` | 4 | 29–31 |
| `reference/indexes/image-map-reconciliation.md` | 5 | 3, 5–6, 42, 66 |
| `reference/indexes/passage-entry-level-reconciliation.md` | 5 | 11, 15, 17–18 |
| `reference/indexes/performance-subtitle-audit.md` | 4 | 9, 11, 15, 35 |
| `reference/indexes/settei-collection-review-batch-01.md` | 5 | 4, 17, 30, 47, 61 |
| `reference/indexes/settei-collection-review-batch-02.md` | 6 | 4, 15, 31–32, 49, 72 |
| `reference/indexes/settei-collection-review-batch-03.md` | 5 | 4, 14, 30, 47, 63 |
| `reference/indexes/settei-collection-review-batch-04.md` | 5 | 4, 15, 31, 46, 60 |
| `reference/indexes/settei-collection-review-batch-05.md` | 5 | 4, 15, 33, 48, 62 |
| `reference/indexes/settei-collection-review-batch-06.md` | 7 | 4, 15, 31–32, 47–48, 65 |
| `reference/indexes/settei-collection-review-batch-07.md` | 9 | 4, 15–16, 34–35, 50–51, 68–69 |
| `reference/indexes/settei-collection-review-batch-08.md` | 7 | 4, 15, 33–34, 51, 67–68 |
| `reference/indexes/settei-collection-review-batch-09.md` | 5 | 4, 11, 31, 46, 62 |
| `reference/indexes/settei-collection-review-batch-10.md` | 7 | 4, 12, 28–29, 44, 63–64 |
| `reference/indexes/settei-collection-review-batch-11.md` | 7 | 4, 11, 27, 42–43, 59–60 |
| `reference/indexes/settei-collection-review-batch-12.md` | 8 | 11–12, 25, 31–32, 46–47, 62 |
| `reference/indexes/settei-collection-review-batch-13.md` | 6 | 4, 12, 32, 49, 64–65 |
| `reference/indexes/settei-collection-review-batch-14.md` | 9 | 4, 13–14, 29–30, 45–46, 62–63 |
| `reference/indexes/settei-collection-review-batch-15.md` | 8 | 4, 12–13, 25–26, 41–42, 57 |
| `reference/indexes/settei-collection-review-batch-16.md` | 9 | 4, 12–13, 28–29, 45–46, 61–62 |
| `reference/indexes/settei-collection-review-batch-17.md` | 10 | 4, 12–13, 28–30, 46–47, 61–62 |
| `reference/indexes/settei-collection-review-batch-18.md` | 3 | 4, 11–12 |
| `reference/indexes/settei-collection-review-batch-19.md` | 20 | 4, 14, 19, 25, 29, 36, 41, 47, 52, 58, 63, 69, 80, 85, 91, 96, 102, 107, 113 |
| `reference/indexes/settei-collection-review-batch-20.md` | 24 | 4, 13, 17, 24, 29, 35, 41, 46, 57, 62, 68, 73, 79, 84, 90, 95, 101, 103, 107, 112, 114, 118 |
| `reference/indexes/settei-collection-review-batch-21.md` | 23 | 4, 13, 18, 24, 29, 35, 39, 41, 46, 50, 57, 62, 68, 73, 79, 85, 90, 95, 101, 106, 112, 118 |
| `reference/indexes/settei-collection-review-batch-22.md` | 17 | 4, 13, 24, 29, 35, 40, 46, 51, 57, 62, 68, 79, 90, 101, 106, 112, 116 |
| `reference/indexes/settei-collection-review-batch-23.md` | 25 | 4, 13, 18, 24, 29, 35, 40, 46, 51, 57, 63, 68, 73, 79, 84, 90, 95, 101, 104, 106, 112, 117 |
| `reference/indexes/settei-collection-review-batch-24.md` | 15 | 4, 13, 18, 24, 35, 46, 51, 57, 62, 68, 79, 90, 101, 112 |
| `reference/indexes/settei-collection-review-batch-25.md` | 17 | 4, 13, 19, 24, 35, 41, 46, 52, 57, 63, 68, 73, 79, 90, 101, 112 |
| `reference/indexes/settei-collection-review-batch-26.md` | 21 | 4, 14, 20, 25, 30, 36, 47, 52, 58, 69, 74, 80, 91, 96, 102, 107, 113, 118 |
| `reference/indexes/settei-collection-review-batch-27.md` | 12 | 4, 14, 25, 36, 47, 58, 69, 71, 80, 91, 102, 113 |
| `reference/indexes/settei-collection-review-batch-28.md` | 18 | 4, 13, 24, 27, 35, 46, 57, 62, 68, 73, 79, 84, 90, 101, 106, 112, 115 |
| `reference/indexes/settei-collection-review-batch-29.md` | 20 | 4, 13, 18, 24, 29, 35, 46, 52, 57, 63, 68, 74, 79, 90, 101, 106–107, 112, 117 |
| `reference/indexes/settei-collection-review-batch-30.md` | 18 | 4, 13, 19, 24, 35, 40, 46, 51, 57, 63, 68, 79, 90, 95, 101, 106, 112, 118 |
| `reference/indexes/settei-collection-review-batch-31.md` | 23 | 4, 13, 19, 24, 35, 41, 46, 52, 57, 63, 68, 74, 79, 85, 90, 96, 101, 107, 112, 118 |
| `reference/indexes/settei-collection-review-batch-32.md` | 16 | 4, 14, 20, 25, 31, 36, 47, 49, 58, 69, 80, 91, 102, 113 |
| `reference/indexes/settei-collection-review-batch-33.md` | 19 | 4, 13, 19, 24, 35, 40, 46, 51, 57, 68, 79, 90, 101, 107, 113, 124, 130, 135 |
| `reference/indexes/settei-interior-review.md` | 16 | 19, 32, 44, 59, 72, 86, 100, 112, 125, 140, 154, 168, 181, 193, 207, 222 |
| `reference/indexes/settei-variant-review.md` | 1 | 20 |
| `reference/indexes/startup-open-items-followup.md` | 7 | 7, 58, 60, 62 |
| `reference/indexes/startup-sequence-comparison.md` | 17 | 3, 9–11, 15, 21–24, 93 |
| `reference/indexes/to-be-continued-supplied-reference.md` | 5 | 10–12, 37, 41 |
| `tools/reference-alignment/README.md` | 2 | 971, 987 |
| `tools/reference-context/README.md` | 1 | 389 |
| `tools/reference-extraction/README.md` | 1 | 37 |

### Non-Link Text And Stored Provenance

| Location | Classification / action |
| --- | --- |
| `reference/README.md:17` | Current inventory-tool usage prose: update the source-manifest destination. |
| `tools/reference-extraction/README.md:22` | Current inspection-tool usage prose: update episode metadata output destination. |
| `reference/indexes/episode-index.md:7` | Bare `source-manifest.json` identity remains valid; add/rebase its navigation pointer without changing source observations. |
| `reference/indexes/episode-04-startup-review.md:7` | Subtitle extraction arguments/hash are historical and unchanged; bare metadata filename remains identifiable. |
| `episode-02-review-batch-02-frames.json:858`, `episode-02-review-batch-03-frames.json:1421`, `episode-02-review-batch-05-frames.json:858` under the old index root | Stored `review_reference` values point to the original record location. No maintained code reads this key in the inspected tools. Preserve JSON bytes; use the FILE ledger to resolve the new review location. |
| All 48 frame manifests, metadata JSON, coverage JSON and authored selection-plan JSON | Preserve content, source/media paths, commands and hashes when moving. The coverage JSON file location changes, not its recorded ASS/source locations. |
| `alignment-anchors.csv.recipe_json` and archive receipts/payloads | No moved-root filename occurrence found in stored recipes. Keep their bytes/identity unchanged; they are not live tool configuration. |
| Baseline JSON and migration ledgers | Old paths/line ranges are intentional historical mappings. Do not run global replacement over the migration records. |

### Local Helper Inspection Record

The 33 scripts below were read as text and hashed, not executed. The existing inventory supplies
their purpose. Only seven contain direct index/README reference lines; many other temporary scripts
import the maintained category module and write shared annotation tables. No direct moved-root
dependency does not make those scripts safe to replay. All remain ignored and unchanged at their
original locations at the audit checkpoint. Phase 3 moved them to the table's historical destinations:
every row is now MOVED_HASH_VERIFIED, with original paths absent and ignored targets.
Preserve historical script bytes; any later reuse requires a current-data check and explicit scope.

| Original helper | Historical destination | SHA-256 | Direct index/README reference lines |
| --- | --- | --- | --- |
| `.tmp/add_ep04_manual_references.py` | `tools/historical/local/reference-review/episode-04/add_ep04_manual_references.py` | `99453f07a65e305515bcfb2c1f377f2ca80123c591dec457f52515eebce82fff` | — |
| `.tmp/add_halcyon_flight.py` | `tools/historical/local/reference-review/episode-04/add_halcyon_flight.py` | `287eab1c08bf4e644f96f0a93f3768dbf6843e8a9f61e94edf62ee161113e1c8` | — |
| `.tmp/add_halcyon_supplements.py` | `tools/historical/local/reference-review/episode-04/add_halcyon_supplements.py` | `bc02f1135e0b47d7c8a7ecdd7cfc0b65fc18b2c847df8d215f7549ced5a6e663` | 21 |
| `.tmp/adopt_initial_review_status.py` | `tools/historical/local/reference-review/adopt_initial_review_status.py` | `8d9dc19755524272e001a1eb737ed15827804136b4bdd7eec2cdd69aad1cac89` | — |
| `.tmp/alignment-stage5/validate_pilot.py` | `tools/historical/local/reference-alignment/stage-5/validate_pilot.py` | `bebb747320f693a28abc6c3ebe2c4fb8e5697b60558ead5d4d38b70239a40cba` | 13–14 |
| `.tmp/animehistory-workbook/build-importexcel-test.ps1` | `tools/historical/local/reference-workbooks/build-importexcel-test.ps1` | `94145c1698890d98a7ad46e7e34f199ef22a10a8ac9e22fd7fb58849a05097db` | 3 |
| `.tmp/category-preview.mjs` | `tools/historical/local/reference-review/previews/category-preview.mjs` | `a0d742dbb45fdd7b44e1fae4def73c6f84a29f7657957548bb58baf91e9b3be5` | 8 |
| `.tmp/category_preview_montage.py` | `tools/historical/local/reference-review/previews/category_preview_montage.py` | `dda067bdac792a8a9e17fc57330084935ac0480e76b46e485002126bc8690a17` | — |
| `.tmp/confirm_ep04_022.py` | `tools/historical/local/reference-review/episode-04/confirm_ep04_022.py` | `126d48518432235131440c5bb6ebdc7c06a00d64e0e1473493ff656231143490` | — |
| `.tmp/correct_ep04_111_167.py` | `tools/historical/local/reference-review/episode-04/correct_ep04_111_167.py` | `2effa4cbc9b344d733acfc0fc55a90e4a454d76b94a775ef569f50fc2c42c87e` | — |
| `.tmp/correct_ep04_239.py` | `tools/historical/local/reference-review/episode-04/correct_ep04_239.py` | `42f93376f4d2242dccd441ff2dc8b663db57834c148306ff0467c9680c13f23b` | — |
| `.tmp/correct_ep04_anchor_dropship.py` | `tools/historical/local/reference-review/episode-04/correct_ep04_anchor_dropship.py` | `a67ae5b300943c446405887442a2ce53403209b3dc52172cacc8b81dcbb60664` | — |
| `.tmp/correct_ep04_el_dorado.py` | `tools/historical/local/reference-review/episode-04/correct_ep04_el_dorado.py` | `1c628a05b8e5b49dd1ad07eb9edbaf81d1a05a045672cb7efb756c5c15a47434` | 9 |
| `.tmp/correct_ep04_first.py` | `tools/historical/local/reference-review/episode-04/correct_ep04_first.py` | `951f3112d03a7fce5968689a4761119b039fd4b06e8f3cd8a69dfc122e4bdb22` | — |
| `.tmp/correct_horus_add_grapple.py` | `tools/historical/local/reference-review/episode-04/correct_horus_add_grapple.py` | `5f455eaa432320744bcda46f840c3d32a32339c181851873c357c7d21ad95a09` | — |
| `.tmp/ep04_cleanup_baseline.py` | `tools/historical/local/reference-review/episode-04/ep04_cleanup_baseline.py` | `f80eaf907f207066416c7f16ae5647cfe5c274339d019bc637efa3755889fddc` | 4–5 |
| `.tmp/fix_ep04_344.py` | `tools/historical/local/reference-review/episode-04/fix_ep04_344.py` | `1f0bd1f00203e436a9f5a825c49056464376c9a0993e0a576610ac5b6a871342` | — |
| `.tmp/refine_ep04_025_096.py` | `tools/historical/local/reference-review/episode-04/refine_ep04_025_096.py` | `750abc28af2bc514847b55d73fdbc4b0b197bb6304f3f8c023068e5ed9d651ac` | — |
| `.tmp/screen_ep04_025_096.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_025_096.py` | `fec6d22d65408ed02dda70bded336acb1d91e2e18dd1078b6f52b912074ceefe` | — |
| `.tmp/screen_ep04_097_168.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_097_168.py` | `57c4f3e8da1893e57ac1bee33c18c3388962c2397971e289a8552d98b9f415fc` | — |
| `.tmp/screen_ep04_169_240.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_169_240.py` | `f9a987b0fb5fec17d18a3a97f1fca294427e3991fe4258eb4387ba1516fabb06` | — |
| `.tmp/screen_ep04_241_312.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_241_312.py` | `56c86a0a287f20e57f10710b33864cabf7245b66c89eb0135022ee4ce18f42f6` | — |
| `.tmp/screen_ep04_313_354.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_313_354.py` | `4be811670f77cc2395d1aea5296454144d1071965fdf2b93330e6cdda68bcfa0` | — |
| `.tmp/screen_ep04_first.py` | `tools/historical/local/reference-review/episode-04/screen_ep04_first.py` | `87df8212f6072383e778d33a88acd4692b2bbbd1ae7b1b2fde2f11030ad980df` | — |
| `.tmp/verify_ep04_cleanup.py` | `tools/historical/local/reference-review/episode-04/verify_ep04_cleanup.py` | `cf3b54d6cd41a204d0c83154cab0d22422fd0a50eeff8e91511d43e2190f0aec` | — |
| `.local/blender-pilot/create_connectivity_fixture.py` | `tools/historical/local/blender/connectivity/create_connectivity_fixture.py` | `10fbae91590a601faadab20ec58423eb78c7b337ffe488c46588148769a62f95` | — |
| `.local/blender-pilot/probe_bridge.py` | `tools/historical/local/blender/connectivity/probe_bridge.py` | `9c1f056dea0a52f77a4efd7d99402ce3251b3dca4f27ddf239daad55cc255880` | — |
| `.local/blender-pilot/remove_connectivity_cube.py` | `tools/historical/local/blender/connectivity/remove_connectivity_cube.py` | `189d8ea31b1cee3c0358c922eb2462391c400b62eeb559791b21257c747e31c7` | — |
| `.local/validation/phase-3-1/inspect_test_lab.py` | `tools/historical/local/validation/phase-3-1/inspect_test_lab.py` | `5cb4f82d92a27d1a329673924b8da513ff4262dfb22accb716b6a214fcd99553` | — |
| `.local/validation/phase-3-1/verify_blender_recovery.py` | `tools/historical/local/validation/phase-3-1/verify_blender_recovery.py` | `0123506a49046bef3e0bd1f2982b67bcab8d2e867b9e88ab7e84a04e4a361c6b` | — |
| `.local/validation/phase-3-1/verify_finished_test_lab.py` | `tools/historical/local/validation/phase-3-1/verify_finished_test_lab.py` | `18ecd13a820d0005853cf57027d6ff9914e4a8e82d3d71cbdb2c4591192aaa35` | — |
| `.local/validation/phase-3-1/verify_unreal_recovery.py` | `tools/historical/local/validation/phase-3-1/verify_unreal_recovery.py` | `6d01e008da3870f63bb87c8994f2afc29d16af9b75c8b3e9e1b5ebf6a78f2e61` | — |
| `reference/working/build_review_sheets.py` | `tools/historical/local/reference-review/named-section-sheets/build_review_sheets.py` | `8bb29d15c054088b7bd60dfc0f1e761f9bbf61c578c5a0e7d597eb5f3ba3cff9` | 9 |

Historical consolidation requires `/tools/historical/local/` ignore protection before any file move,
a tracked `tools/historical/README.md` explaining local-only preservation and unsupported status,
and central tool navigation distinguishing active entry points from these archived originals.
No archive payload, generated output, third-party source or entire `.tmp`/`.local` directory moves.
Some archived helpers use `__file__`-relative roots; byte-preserved relocation intentionally does not
claim they remain executable. Keep original paths in this table for historical interpretation.

The legacy sheet helper is assigned a historical route; any maintained replacement needs a separate
routing decision in Phase 2. The old alignment pilot
checker contains the former coverage path at line 14 and must be adapted before any authorized reuse.
The two old supplemental/correction scripts that emit a settei path (`add_halcyon_supplements.py:21`,
`correct_ep04_el_dorado.py:9`) must not reintroduce that obsolete path. Existing shared workbook/CSV
references in the other three index-bearing helpers remain valid; their historical editing behavior is not revalidated.

### Validation And Next Scope

- Static inventory, constructed-path inspection, link resolution, CSV-field classification and local-helper inspection complete.
- Phase 1.1 baseline files remain frozen; exact consumers are recorded here instead of modifying historical pending-audit fields.
- The runtime change list has owners/destinations; implementation and test execution remain Phases 2–4.
- The 2026-10-31 consolidation amendment adds 33 unique historical script destinations without changing the frozen index-file baseline; the script moves remain unimplemented.
- No site adapters, Unreal/Blender behavior, source media, archives, contact sheets, registers or workbooks changed.
- Refresh baseline line numbers after intervening edits; compare content/IDs rather than applying blind line-number replacements.
- Phase 1 was accepted by the maintainer on 2026-10-31; later implementation remains separately authorized.

### Phase 2 Preparation Pointer

The authorized [Phase 2 preparation](reference-index-reorganization-phase-2.md) was implemented
and tested on 2026-11-01, and accepted by the maintainer the same day. It adds index/tool navigation and historical
ignore protection and prepares the active routing changes in an isolated-tested patch. Original
record/script paths in this audit remain the pre-migration baseline; no records or helpers moved.
