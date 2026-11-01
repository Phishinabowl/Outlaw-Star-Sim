# Reference reorganization — Phase 2 preparation

Status: Phase 2 preparation implemented, tested and accepted by the maintainer on 2026-11-01 (America/New_York).

Subsequent state: the [Phase 3 migration](reference-index-reorganization-phase-3.md) activated the
patch and moved the records. The preparation and hash tables below describe the pre-activation checkpoint.

The [plan](reference-index-reorganization-plan.md) owns scope and phase gates. The
[file ledger](reference-index-reorganization-ledger.md) owns record destinations; the
[tool audit](reference-index-reorganization-tool-audit.md) owns tool dependencies and historical
script routes. This record owns Phase 2 preparation and validation results.

## Activation boundary

Phase 2 adds navigation and ignore protection now. Routing edits are prepared as a single patch
and tested in an isolated copy. The live readers retain the current paths until Phase 3 moves
their inputs and activates the patch in the same coordinated increment. There is no automatic
old-path fallback, duplicate authoritative input or partially switched production workflow.

The prepared patch belongs in the existing `tools/reference-extraction` family. It is a migration
artifact, not a new tool family or additional top-level tools directory. Command examples in that
patch change with its activation. Other moved evidence links are repaired through the Phase 3 ledger.

## Navigation and preservation

The new index and episode README pages link existing records at their current locations. Planned
folders do not imply completed migration or episode review. Phase 3 rebases these links together
with the records. Shared AnimeHistory schema/parser headings and context contracts remain in place.

`tools/README.md` lists supported entry points, asset-owned recipes, documentation and output
ownership. `tools/historical/README.md` classifies archived helpers as unsupported; the legacy
12-frame named-section sheet builder is assigned to history rather than promoted.

The `/tools/historical/local/` ignore rule must match all 33 planned destinations before any
script moves. The source scripts remain where they were during Phase 2. No media or archive moves,
workbook rebuilds, third-party relocation or historical script execution is performed here.

## Prepared Routing Patch

[reorganization-routing.patch](../../../../tools/reference-extraction/reorganization-routing.patch) contains 11 file changes:
four output writers, two alignment readers, the category workbook input hash lookup, two alignment
fixtures, current command documentation and a new four-test output-routing module. The patch remains
unapplied in the live checkout. No old-path fallback is introduced.

Patch SHA-256: `82ea9960dfe61538116b128f2d00b80f7fa621450809643e70a9af6db55df19c`. It uses zero context to avoid whitespace-only context
lines in the tracked patch artifact. Phase 3 must first verify the source hashes below, then use
`git apply --unidiff-zero --check tools/reference-extraction/reorganization-routing.patch` before
coordinated activation. A source mismatch requires review/regeneration, not forced application.
The patch was first tested with full context in the isolated tree; the final zero-context form
passed forward applicability against the live source and reverse applicability against that tested tree.

| File | Before SHA-256 (actual bytes) | Prepared SHA-256 (LF-normalized text) |
| --- | --- | --- |
| `tools/reference-extraction/inventory.py` | `ae7bc284366062e876f81da709e23b1f1e47aa68ebae53a33ff162a016c8c9d6` | `7c74d4fcd9fbd9828ea687cbaa2c25da6476cae6eb7637982dfb67dcdd3d155f` |
| `tools/reference-extraction/inspect_episode.py` | `5734945af9ac8771b4c31f522c7d972f935910657fdd2e0ae161abd2292090dd` | `5683390f82aa9294afb979b4ea23fefb5afd2b958891089cff3e096f496cf56f` |
| `tools/reference-extraction/extract_reference_frames.py` | `7d3260009049caf91cc0d40b576f29fd9d4e8b00db699987df31ad68b74e4674` | `93dad17f6724a80cdbe68e05eb50d55e7e670cf4d748eb50ebb695b481146ada` |
| `tools/reference-extraction/scan_performance_subtitles.py` | `27636a846cc0a23aad0e0152063c8f5abd92f7bd367fada72e1b0f2a221fb304` | `104b4f30c1e710d354f3fce1597ddc6c809114bcdfb5844c7ed9bd1b90daffaf` |
| `tools/reference-alignment/alignment.py` | `8381b0c2a863243bdb0d9208adf10863c87c6e864045d1fa4a102b514bba3d76` | `9052d1f5605770d90bbd5ab29a2c2b2e81de05310532414de1ffebb1a131482d` |
| `tools/reference-alignment/projection.py` | `53b2ddb7c1e6fe7ecaffa979355f06261adccf7950d2122291f04a5111c6f383` | `592b1e2ab602223e900b6c8aa25af3a68019014105f162389c14d9812199542e` |
| `tools/reference-extraction/build_category_workbook.ps1` | `24c5049bb286943440cb770193ef6209015df8909ce80f017e1a1b5e58af11af` | `73bef324aaa7675cfc36ce7e130ad9c042c5bde316c27b56fac505107c76967c` |
| `tools/reference-alignment/test_alignment.py` | `bc69a97730de0ad7e7d7069113dc633942c052e751b4368bf9a503be9b638156` | `66c3b3e56571aac1c2c47a33b12fe123360c6a76c18af2596f7ae8b8aaeda833` |
| `tools/reference-alignment/test_projection.py` | `ea21dcc852375a00a2fc0ea624ea84822444f11ea8714b26c89ba879c61e1e55` | `355e36ea7c8cc9c1087ea844c1e8f0bc62124e9c9a637681273089a7b655ffb7` |
| `tools/reference-extraction/README.md` | `eed4cfcf8eb30a577eb0a29883ceb709fc0ce5bc380743d3bdfdc558c7decc08` | `493de1b8b565e13cffd4bfb1ebbfb68049d78f31d2de56c6ad47738e355fceeb` |
| `tools/reference-extraction/test_output_routing.py` | `NEW_FILE` | `b8e008e3d010cbf2810f29944a61c537b2c4c2fda0acb3b63e432345addda234` |

## Validation Results

- Navigation: 17 index/episode README pages added; existing records are linked at current paths.
- Final navigation/tool/preparation-page check: all 220 local links resolved.
- Historical protection: all 33 planned destinations match the new ignore rule; central and historical README files remain trackable.
- Preservation: all 193 pre-existing index files and 33 helper sources match their recorded hashes; all planned moved-file destinations remain absent.
- Isolated routing tests: 4 passed, using synthetic files and mocked FFmpeg/FFprobe responses. They cover nested output destinations, subtitle-output preservation and refusal on an existing frame batch or subtitle audit.
- Isolated annotation regressions: 10 passed using an unchanged copy of the parser-owning README.
- Isolated alignment suite: 69 tests run, 68 passed, 1 skipped. The optional FFmpeg synthetic decode integration was not enabled; no fresh decode/version compatibility claim is made.
- Prepared category workbook builder: PowerShell parser reported no syntax errors. ImportExcel was not invoked and no workbooks were rebuilt.
- Prepared Python code in the isolated copy matches the patch output hashes. Live maintained executable files remain unchanged.
- The owned isolated proof directory and three temporary preparation/test scripts were removed after validation; the routing patch retains the four new regression tests for activation in Phase 3.

## Phase 3 Handoff

Acceptance of this preparation does not activate output routing. Phase 3 must refresh the ledger
baseline for intervening changes, move the textual inputs, activate the prepared patch, repair
authored evidence pointers and navigation links, and relocate only the 33 named historical scripts.
Apply the routing patch before rebasing links in its affected tool README, or regenerate the
coordinated patch after reviewing those intervening edits; do not bypass source-hash checks.
Phase 4 still owns current-layout integration checks and workbook equivalence.
