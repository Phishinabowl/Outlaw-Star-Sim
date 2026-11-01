# Historical project helpers

This directory owns historical navigation. The `local/` subtree is Git-ignored so relocating the
33 previously local-only scripts does not publish them. All 33 scripts now occupy their ledgered
historical destinations; original source files are absent and byte hashes are preserved.

The [tool audit ledger](../../docs/implementation/projects/reference-index-reorganization/reference-index-reorganization-tool-audit.md#local-helper-inspection-record)
owns the exact original paths, planned destinations and hashes. Groups under `local/` cover
reference review/corrections/previews, alignment pilots, workbook pilots, Blender connectivity
and development/recovery validation.

Historical scripts are preserved for inspection, not offered as supported commands. Some contain
host-specific paths, infer the repository from their original location or perform one-off edits
against an earlier data state. Relocation preserves bytes; it does not make them safe to rerun.
Use the [maintained tool directory](../README.md) for current work.

Phase 3 moved only the 33 named script files after source/destination/hash and ignore checks.
Generated media, logs, virtual environments, third-party source and surrounding `.tmp`/`.local`
directories remain with their existing owners. No cleanup of those directories is implied.

The old `reference/working/build_review_sheets.py` is classified as a legacy historical helper.
It creates 12-frame named-section sheets and is distinct from the supported 24-image gallery
sheets. Any future maintained version needs explicit routing, documentation and relevant checks;
the byte-preserved historical original stays separate.
