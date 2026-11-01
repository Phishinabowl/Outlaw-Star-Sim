# Reference reorganization — Phase 4 integration validation

Status: completed, checked and accepted by the maintainer on 2026-11-01 (America/New_York).
Confirmation authorized Phase 4 documentation publication as `68dd4e3`. The subsequent
[Phase 5 closeout](reference-index-reorganization-closeout.md) is prepared with acceptance pending.

The [plan](reference-index-reorganization-plan.md) owns scope and gates. The
[migration ledger](reference-index-reorganization-ledger.md),
[tool audit](reference-index-reorganization-tool-audit.md) and frozen
[Phase 1.1 baseline](reference-index-reorganization-baseline.json) own the original/current paths,
dependencies and preserved-data controls. [Phase 3](reference-index-reorganization-phase-3.md)
records the moves and routing activation; this phase validates the resulting integration.

## File And Reference Accounting

- All 152 ledgered root records have unique, existing destinations and absent original paths.
  The index root contains only its navigation README and collection directories.
- All 66 moved JSON records match their baseline SHA-256 values. Across the 193 original index
  files, 101 remain byte-identical; the 92 intentional changes comprise 84 Markdown records,
  six CSV tables and two refreshed workbook projections. Markdown/reference changes belong to
  Phase 3; Phase 4 introduced no further evidence edits.
- All 33 historical helper destinations are unique and match their recorded hashes. Original
  paths are absent. The historical local subtree is ignored and contains no tracked helper.
  No historical helper was executed.
- All 37 CSV tables match the frozen ordered-row digests after reversing only the ledgered
  file/README-fragment reference substitutions. Field order, row order/counts and all other values
  are unchanged. The frozen baseline contains some misdecoded heading punctuation; the checker
  normalized that encoding for fragment derivation without editing the baseline or evidence.
- A maintained Markdown scan resolves 1,659 local links, including 360 heading fragments.
  Scope: root instructions/README, `docs`, index records, maintained tool manuals and asset recipes;
  fenced code, migration records containing intentional old paths, historical local scripts and
  third-party/plugin documentation are excluded. This scope differs from the Phase 3 scan.
- Category, context and alignment validators pass: 9,204 gallery rows, 26 supplements, 105 anchors,
  12 historical mappings and six validated mappings. Source-cache verification passes for 26 Fandom
  and four AnimeHistory snapshots; 29 captured source versions are linked by the context register.
  Snapshot-cache counts and registered-source counts have different scopes.

## Tool Integration Checks

| Suite | Result | Scope |
| --- | --- | --- |
| Reference extraction/gallery | 30 passed | Annotation validation, synthetic image/gallery fixtures, real RAR CLI round trips on disposable fixtures, four output-routing regressions |
| Reference context | 53 passed | Offline parser, cache, bounded transport fixtures, table relationships and view projections |
| Reference alignment | 69 run: 68 passed, one skipped | Model/projection/cleanup/reproduction and episode contracts; optional FFmpeg decode integration skipped |

Initial extraction/context runs intermittently failed with Windows access-denied errors during
temporary file/directory replacement. The failing cases varied between runs, including unchanged
cache operations. Both suites passed unchanged using normal Windows temporary fixture directories
outside the sandbox. A temporary runner changed only the disposable fixture-root selection;
repository inputs and tool implementations were unchanged. The alignment suite passed in the
workspace. This establishes the recorded test results, not a diagnosis of the Windows locking cause.

Four routing tests use synthetic sources and mocked FFmpeg/FFprobe to verify source-manifest,
episode metadata, extracted-frame provenance and subtitle-coverage destinations. They explicitly
reject recreation of the corresponding former flat paths and preserve the existing source and
no-overwrite contracts. Static inspection finds no former moved-root path in maintained Python
or PowerShell runtime consumers. Historical scripts and the already-applied routing patch remain
historical artifacts, not supported entry points.

No source episode was decoded or re-extracted. No existing episode archive was restored or pruned,
and no original media, archive payload, contact-sheet collection or retained subtitle was changed.
RAR round-trip tests operated only on generated fixture images. These checks do not constitute a
new full-content hash verification of the source videos or current-media alignment verification.

## Workbook Refresh And Equivalence

The installed ImportExcel 7.8.10 builders regenerated the existing local annotation and context
workbooks. The locator-only workbook was unaffected: its file SHA-256 still matches the frozen
baseline, so it was not regenerated. CSVs remain authoritative and all workbooks remain ignored.

| Projection | Saved-output checks |
| --- | --- |
| Annotation workbook | 30 tabs; 9,204 gallery records; 26 manual records; 432,588 gallery cells, 1,326 manual cells and 4,419 alignment cells verified by the builder; 9,204 image links verified |
| Context workbook | Five tabs; 14,252 cells and 2,736 links verified by the builder; 48 subjects, 29 registered source versions, 81 context records and 1,278 relationship rows retained |
| Locator workbook | 27 tabs; original bytes, saved values/formula and 9,230 links unchanged |

An independent ZIP/XML comparison captured the three existing workbooks before regeneration and
compared all **593,493 stored cells and 21,331 hyperlinks across 62 tabs** afterward. These stored
XML counts include layout/empty cells and differ from the builders' authored-data counts above.

- Exactly 1,104 cell values changed, all reversible ledgered reference paths. No other value,
  cell type, formula or cell style index changed. Timing values, evidence IDs, observations,
  review states and recorded availability remain unchanged.
- Exactly two hyperlink destinations changed: context Links `H81` and `H263`. Both resolve to
  the moved evidence/preparation records; `H263` retains `#horus-two-jump-dialogue-check`, which
  resolves to the existing heading. All other hyperlinks are unchanged.
- Sheet names/order, stored cell coordinates, column widths, panes, merge definitions,
  conditional-format/data-validation definitions and other compared row attributes are unchanged.
  The existing builders increased 298 row heights to accommodate longer reference paths:
  EP-01 119 rows, EP-02 111, EP-03 three, EP-04 63 and context Links two. Every resized row
  contains an expected reference-path change. No workbook layout was redesigned.
- No saved error cells were found. The locator overview's existing `SUM(C8:C33)` formula and
  saved value 9,204 are unchanged; no formulas were added. The refreshed views contain static
  projections, so no new native Excel recalculation claim is needed or made.
- Read-only Artifact Tool rendering was visually inspected for context Links `C80:I82` before
  and after refresh and annotation EP-02 `U233:X235` after refresh. The affected path/identity
  context is readable with the existing formatting. Native Excel/Office Viewer opening and
  interactive hyperlink activation were not performed.

## Exit Evidence And Limits

File accounting, preserved-data checks, maintained links, runtime routing, schemas, test suites
and workbook equivalence pass within the scopes above. No unexplained evidence/data difference
remains. Temporary validation scripts, workbook snapshots and render previews are task-owned
scratch files, not additional maintained tools or research records, and are removed after use.

The maintainer accepted Phase 4 and authorized its documentation publication on 2026-11-01.
Phase 5 owns the subsequent closeout review and requires separate authorization. Episode 7 and
vertical-slice Phase 3.2A remain unstarted.
