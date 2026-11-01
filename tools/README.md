# Project tools

Use this directory to find maintained entry points and their owning documentation. Tests and
support modules are not separate tools. Reference records now use the organized index layout;
the coordinated Phase 3 migration is accepted. Full integration/workbook validation remains Phase 4.

## Reference review

| Job | Entry point in `tools` | Documentation |
| --- | --- | --- |
| Download/restore episode gallery, build 24-image sheets, archive supplements and prune expanded originals | `reference-extraction/episode_gallery.py` | [Gallery procedure](reference-extraction/README.md#episode-gallery-review-tool--proposal) |
| Validate image annotations and prepare workbook data | `reference-extraction/category_index.py` | [Extraction/review tools](reference-extraction/README.md) |
| Refresh annotation/alignment workbook | `reference-extraction/build_category_workbook.ps1` | [Extraction/review tools](reference-extraction/README.md) |
| Refresh locator-only workbook | `reference-extraction/build_animehistory_workbook.ps1` | [Locator ownership](../reference/indexes/animehistory/README.md#workbook-refresh-and-ownership) |
| Cache gallery HTML and build timestamp locators | `reference-extraction/cache_timestamp_index.py` | [Extraction/review tools](reference-extraction/README.md) |
| Retrieve/inspect/validate selected AnimeHistory and Fandom context | `reference-context/context_tool.py` | [Context tool](reference-context/README.md) |
| Refresh shared context workbook | `reference-context/build_context_workbook.ps1` | [Context tool](reference-context/README.md) |
| Search bounded local frames for selected gallery images | `reference-alignment/alignment.py` | [Alignment tool](reference-alignment/README.md) |
| Record reviewed anchors and fit/validate timing mappings | `reference-alignment/models.py` | [Alignment tool](reference-alignment/README.md) |
| Reproduce accepted frame evidence | `reference-alignment/reproduce.py` | [Alignment tool](reference-alignment/README.md) |
| Preview/apply owned temporary alignment cleanup | `reference-alignment/finish.py` | [Alignment tool](reference-alignment/README.md) |

The context adapters/core/views and alignment projection module support these entry points.
The [ordered episode workflow](../reference/indexes/animehistory/README.md#ordered-episode-review-workflow)
owns review order and scope; individual commands do not authorize the next episode or broad extraction.

## Older maintained reference helpers

| Entry point | Purpose |
| --- | --- |
| [inventory.py](reference-extraction/inventory.py) | Read-only source inventory and settei screening sheets |
| [inspect_episode.py](reference-extraction/inspect_episode.py) | One episode's FFprobe metadata; no video decoding |
| [extract_reference_frames.py](reference-extraction/extract_reference_frames.py) | Up to 32 explicitly requested frames with decoded PTS and extraction provenance |
| [scan_performance_subtitles.py](reference-extraction/scan_performance_subtitles.py) | All-episode English subtitle audit; existing outputs cause refusal |

See the [reference-tool manual](reference-extraction/README.md) before execution. Existing subtitle
coverage and source records should be reused; reorganization does not require fresh extraction.

## Blender and Unreal development

| Location | Purpose / runtime |
| --- | --- |
| [create_scale_test_lab.py](unreal/create_scale_test_lab.py) | Owned Phase 3.1 map creation in Unreal editor Python |
| [verify_scale_handoff.py](unreal/verify_scale_handoff.py) | Saved Unreal handoff package inspection |
| [Asset recipes](../assets/recipes/create_scale_handoff.py) | Blender fixture creation, UVs, export and deliberate flap revision; recipes retain asset ownership |
| [Marker-material recipe](../assets/recipes/create_handoff_marker_materials.py) | Unreal material creation through the pilot execution interface |

The [handoff record](../docs/implementation/validation/phase-3-1-blender-handoff-results.md) and
[editor automation contract](../docs/architecture/editor-automation.md) own runtime boundaries.
These scripts are not ordinary shell tools and may create or alter owned development assets.

## Output ownership

| Output | Owner / location |
| --- | --- |
| Shared image, locator, alignment and context registers | `reference/indexes/animehistory` and `reference/indexes/context` |
| Permanent source, settei, episode, performance and comparison records | [Index navigation](../reference/indexes/README.md); migration ledger defines target layout |
| Gallery originals and verified RARs/receipts | Ignored `reference/cache/animehistory-review`; archive/restore/prune tool owns lifecycle |
| Contact sheets | Ignored `reference/contact-sheets`; retained during normal episode closeout |
| Full subtitle text, context captures, extracted frames and temporary alignment runs | Existing ignored `reference/working`, `reference/cache`, `reference/extracted-frames`; use owning cleanup procedure |
| Workbook projections | Existing ignored XLSX files beside their authoritative CSVs |
| Build scratch/proofs | Task-specific directories under ignored `.tmp`; remove only owned outputs after verification |

Keep runtime outputs out of `tools`. Reusable scripts belong with their maintained tool family;
historical scripts belong in the [historical collection](historical/README.md). Do not introduce
new scripts into disposable evidence/output directories.

## Reorganization preparation

[Phase 2 preparation](../docs/implementation/reference-index-reorganization-phase-2.md) owns the
pending routing patch and isolated checks. That patch is a migration artifact, not another CLI.
It was activated with the Phase 3 record moves and is retained as an implementation artifact;
do not reapply it to the migrated checkout. Full integration validation remains Phase 4.
