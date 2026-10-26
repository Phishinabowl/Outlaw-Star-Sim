# Reference tools

scan_performance_subtitles.py implements the user's approved all-26-episode subtitle-text screening. Run `python tools/reference-extraction/scan_performance_subtitles.py` from the repository root with FFmpeg/FFprobe on PATH. It selects the unique English ASS track excluding signs/songs by title, copies subtitle packets without decoding audio/video, and writes full subtitle/candidate context under ignored reference/working/performance-subtitles/. A trackable coverage JSON records filenames, source sizes, track tags, copied-text hashes, commands/version and scan counts. Existing outputs cause a refusal rather than overwrite. The broad keyword/number pattern produces leads only; manually authored review/CSV supplies subject attribution, interpretation and limits. It does not authorize frames, original-language transcription or a simulation model.

inventory.py requires Python 3 and Pillow. It only reads source media; outputs are fixed under reference/, with settei contact sheets in reference/contact-sheets/settei/. Run from any directory. No installation or episode decoding is performed.

inspect_episode.py requires Python 3 and FFprobe on PATH. Run python tools/reference-extraction/inspect_episode.py 4 from the repository root to inspect Episode 4. It selects exactly one matching numbered source, reads container/stream/chapter metadata, and writes reference/indexes/episode-04-metadata.json. No media is decoded/extracted or modified. Metadata output for that episode is replaced when rerun; no episode content hash is computed.

cache_timestamp_index.py uses Python's standard library to cache public AnimeHistory HTML under ignored reference/cache/animehistory/ and generate timestamp/caption/image-link CSVs under reference/indexes/animehistory/CSVs/, with all-episodes.csv and manifest.json in the parent folder. It downloads no images. It validates cached hashes, pagination, IDs and declared counts; reruns reuse cached pages and replace the generated index. build_animehistory_workbook.ps1 creates the ignored local XLSX browsing view from these CSVs using the installed PowerShell ImportExcel module, validates the saved data/links and then replaces the generated workbook. See reference/indexes/animehistory/README.md for refresh instructions, alignment limits and ownership.

The established reference workflow uses FFprobe metadata, FFmpeg selected frames, Pillow contact sheets and CSV/JSON provenance. ImageMagick is optional. Manual visual review precedes transcription/translation; no blind OCR.

## Episode gallery review tool — proposal

**Status — 2026-10-26:** `episode_gallery.py` is implemented as a pilot. Disposable-fixture tests
and full Episode 4 cache/contact-sheet/RAR round-trip checks passed within the scope recorded below.
Maintainer readability acceptance and full Episode 4 preparation passed on 2026-10-26;
category-index initialization and first-subset integration passed within the evidence scope below;
this is not an adopted operating procedure. Episode 4 category screening is in progress; the
[authored index and survey record](../../reference/indexes/animehistory/README.md#episode-4-category-survey-progress)
own current per-image progress. Full episode screening remains pending. The
[pre-3.2A research checkpoint](../../docs/implementation/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research)
owns research order and acceptance; this section owns the proposed tool behavior and validation.

### Scope and outputs

Prepare sampled gallery images for category screening, preserve resumable progress, and archive
inactive episode caches for later detailed review. Start with Episode 4, then 1–3 and 5–26, one
episode at a time. Complete category splitting across the series before collaborative detailed
cross-episode XGP reviews. Other subject groups remain available for future research.

- Read existing episode CSV locators from `reference/indexes/animehistory/CSVs/`. Preserve episode,
  image ID, web time and image/page URL. Expected counts come from the locator input/manifest;
  the current baseline is 354 per episode, 9,204 total.
- Cache only the requested episode's gallery images, with paced access, bounded retries and
  resumable downloads. Validate image decoding and preserve original downloaded bytes; record
  URL, retrieval time, size, SHA-256, dimensions and any failure in a local recovery manifest.
  Access restrictions or unexpected responses stop the affected work; do not bypass them.
- Generate numbered chronological contact sheets, initially 24 images in a 4-by-6 grid, labeled
  with stable image ID and web timestamp. A full baseline episode would require 15 sheets, with
  the final sheet partially filled. Test image size, aspect-ratio preservation and label readability
  before adopting those dimensions. Original cached images remain available for closer inspection.
- Keep one authored category-index CSV across episodes, with image-level screening state,
  overlapping subject tags, scene/group identifiers and uncertainty/notes. Preserve individual
  locators when grouping repeated shots; do not call a contact-sheet classification detailed review.
  Save progress after each reviewed group so later turns can resume from disk.
- Generate the human-facing workbook with ImportExcel from authoritative textual records. The
  existing locator workbook remains a locator view. The
  [category-index version 1 contract](../../reference/indexes/animehistory/README.md#category-index-field-contract--version-1)
  defines the authored fields and initial tag vocabulary. `category_index.py` validates the authored
  CSV; `build_category_workbook.ps1` creates its separate ImportExcel view. No separate Markdown record per batch.

Implemented pilot storage uses existing ignored areas: episode image caches and recovery manifests under
`reference/cache/animehistory-review/`, contact sheets under
`reference/contact-sheets/animehistory-review/`, and RAR packages under
`reference/cache/animehistory-review/archives/`. Authored category records remain outside archives
under `reference/indexes/animehistory/` in `category-index.csv`. Pilot commands are listed below.
No source media, downloaded images, generated sheets or archives are published through Git.

### Proposed command responsibilities

| Operation | Required behavior |
| --- | --- |
| Prepare | Select one episode or a bounded trial subset; download/resume verified image cache and generate requested contact sheets. Do not overwrite conflicting existing data silently. |
| Status | Report expected, cached, missing/failed, screened and detail-reviewed counts separately; show available sheets, archive state and disk use. An archive alone does not imply review completion. |
| Cleanup | Remove only tool-generated contact sheets for the selected episode after annotations/progress are saved; retain image cache, archives and authored indexes. Sheets are reproducible from verified images. |
| Archive | Package downloaded original images and their recovery manifest into an episode RAR. Record compression settings, input/output bytes and actual savings. Verify before replacing any earlier verified archive. |
| Restore | Extract the selected archive into an owned staging directory, validate inventory and every image hash, then make the cache available. Regenerate sheets on demand. Refuse conflicting cache contents. |
| Prune unpacked cache | Separate explicit option after archive verification and a successful restore/hash comparison. Remove only the validated episode cache and its regenerable sheets, never the archive or authored annotations. |

WinRAR command-line executables were located read-only on this laptop at
`C:\Program Files\WinRAR\Rar.exe` and `UnRAR.exe`, file version 7.13.0. The pilot uses Rar.exe for
creation, integrity testing, member listing and streamed member recovery. Detect availability on the executing host;
no automatic installation or assumption that another host has the same paths.

JPEG data is already compressed, so RAR size reduction may be modest. Measure Episode 4 before
choosing routine compression settings; do not promise a storage-saving percentage. Preserve image
quality through lossless packaging, not JPEG recompression. Avoid keeping redundant contact sheets
in archives when they can be regenerated.

Archive creation must use a temporary candidate, run the archive integrity test, extract into an
owned verification directory and compare the restored file list and hashes with the manifest.
Retain recovery metadata inside the archive and enough external status metadata to identify it
without extraction. Missing/failed downloads remain explicit: an archive of an incomplete cache
must not be reported as a complete episode. An interrupted or failed archive/restore must leave
the last verified archive and available source cache intact.

Before extraction, reject absolute/traversing archive member paths. Before cleanup or pruning,
resolve the exact targets, reject reparse-point/path escapes and verify containment in the selected
tool-owned episode directory. Never delete by broad episode-name matching across the repository.

### Staged validation before procedure adoption

- [x] Implement only the bounded Episode 4 trial first: prepare the first 24 available locators,
  produce one contact sheet, visually inspect it and obtain feedback on image/label readability.
  Maintainer accepted the 4-by-6 image/label layout on 2026-10-26 and authorized the next validation step.
- [x] Test repeat preparation and interrupted-download resume with unchanged cached hashes, stable
  image identities, explicit failures and no duplicate or silently skipped records. Disposable-fixture
  tests passed; the live 24-image trial also passed an offline repeat without image downloads.
- [x] Prepare the full Episode 4 baseline after trial acceptance; reconcile every locator with the
  cache manifest. All 354 images cached without failures, 15 sheets mapped in exact locator order,
  and the final 18-image sheet verified on 2026-10-26.
- [x] Validate category-index progress/resume and overlapping tags on a reviewed subset; keep
  unreviewed, unavailable, category-screened and detail-reviewed states distinct. Reopen the
  generated ImportExcel view without losing notes or stable-ID associations. Initialization,
  first-24 screening, validator/resume tests and saved-workbook data/link checks passed on
  2026-10-26. Native viewer acceptance remains an owner-run check.
- [x] Measure RAR size and runtime; test archive integrity, staged restore and exact hash/inventory
  equality. Full Episode 4 round trip passed on 2026-10-26. Missing/corrupt inputs and interrupted
  operations were exercised using disposable fixtures, not by damaging the live cache.
- [ ] Demonstrate bounded sheet cleanup and explicit unpacked-cache pruning only after verified
  recovery. Restore again from the retained archive and regenerate the same image/label mapping.
- [ ] Record actual commands, versions, paths, outcomes, limitations and retention decisions here
  while testing. Obtain acceptance before replacing this proposal with an official procedure.

This proposal authorizes no broad local-video extraction, concept generation, geometry work,
gameplay or automatic transition into Phase 3.2A. Detailed image inspection, local-video timing
alignment and canon classification retain the project's existing evidence requirements.

### Pilot commands and observed results — 2026-10-26

Use Python with Pillow already available on the current host. Tests used bundled Python 3.12.14,
Pillow 12.3.0 and RAR 7.13 x64. No packages were installed. The commands below are pilot examples,
not an adopted general operating procedure. The first-sheet readability review passed; full
Episode 4 preparation subsequently passed. First-subset category integration passed; full survey,
post-review live cleanup/prune and procedure adoption remain pending.

```text
python tools/reference-extraction/episode_gallery.py prepare --episode 4 --limit 24
python tools/reference-extraction/episode_gallery.py prepare --episode 4 --limit 24 --offline
python tools/reference-extraction/episode_gallery.py status --episode 4
python tools/reference-extraction/episode_gallery.py sheets --episode 4 --limit 24
python tools/reference-extraction/episode_gallery.py archive --episode 4 --allow-partial
python tools/reference-extraction/episode_gallery.py cleanup --episode 4 --progress-saved
python tools/reference-extraction/episode_gallery.py prune --episode 4 --progress-saved
python tools/reference-extraction/episode_gallery.py restore --episode 4
python tools/reference-extraction/test_episode_gallery.py
```

`--start` is a 1-based locator position; `--limit` bounds the number selected. Without a limit,
prepare/sheets select the remaining episode, so keep the trial limit explicit. `--offline` never
requests the website; uncached selections appear as placeholders. Missing data is never marked
reviewed. Live requests are at least one second apart, respect robots guidance and use bounded
transient retries. Access restrictions, rate limits or unexpected content stop the affected run.

`--allow-partial` is required for an incomplete trial archive, which remains labeled incomplete.
`--compression 0..5` controls RAR compression; the pilot used 3, non-solid. Existing verified
archives require explicit `--replace-archive`; a replacement is verified before promotion.
`--progress-saved` acknowledges saved review notes, or that disposable trial sheets contain no
unique annotations. It is required for cleanup/prune; the tool cannot verify future annotation
records yet. Prune independently restores/hashes the archive and compares the current manifest
before deleting an unpacked cache. Restore refuses an existing destination. Per-episode OS locks
prevent concurrent command mutations; the lock is released even when its process exits unexpectedly.

| Evidence | Observed result / limit |
| --- | --- |
| Initial live preparation | First 24 Episode 4 locators, image IDs 847835–847858, web times 00:01:43–00:03:07. All images decoded and hashed; 330 locators were uncached at that checkpoint. The first sheet includes opening-credit material as present in the gallery. |
| Full Episode 4 preparation | Subsequent authorized run reused the first 24 images and downloaded the remaining 330. All 354 cached, zero failures/missing; image IDs 847835–848188, web times 00:01:43–00:23:14. All 15 sheet hashes, dimensions and individual ID/time mappings checked against the source CSV; final sheet contains 18 images. Sheets total 49,086,238 bytes. Early, middle and final sheet layouts visually inspected; no category annotations implied. |
| Contact-sheet trial | `reference/contact-sheets/animehistory-review/EP-04/sheet-0001-0024.png`, 1600×2056 pixels. Aspect ratios preserved; ordinal, stable ID and web-time labels visually inspected by Codex. Maintainer accepted readability/layout on 2026-10-26. |
| Initial live archive/round trip | 24 images plus manifest: 4,548,973 input bytes → 4,507,922 RAR bytes, saving 41,051 bytes (about 0.9%), compression 3/non-solid. Archive test and extracted inventory/image hashes passed in about 4.7 s on this host. This partial archive/receipt was subsequently replaced by the verified full episode below. |
| Full Episode 4 archive/round trip | 354 images plus manifest: 56,238,483 input bytes → 55,678,192 RAR bytes, saving 560,291 bytes (about 1.0%), compression 3/non-solid. Native archive integrity, staged restore and all image hashes/inventory passed in about 60.5 s. The tool replaced the partial archive only after this verification. Full archive/receipt, live cache and all 15 sheets retained; no live prune performed. |
| Disposable recovery tests | Resume after request failure and interrupted file promotion; deterministic sheet mapping; corrupted-cache and unregistered-file refusals; explicit cleanup/prune; real RAR restore/replacement; corrupted-archive rejection; simulated archive/restore failure retention; path traversal/reparse-point refusal; OS lock release. These tests do not replace a full-episode production proof. |
| Review integration | Authored CSV initialized with 9,204 unreviewed records. The first-sheet checkpoint passed with 22 SCREENED / 2 NEEDS_RECHECK after attributed maintainer corrections, leaving 330 unreviewed and no completed detailed review at that checkpoint. Further survey progress is recorded in the authored index. The generated 27-tab ImportExcel view reopened with all 285,324 displayed values and 9,204 image links matching source/joined records. Gallery status reads validated annotations and reports recheck, unavailable, unreviewed and detailed states separately from caching. See the [annotation evidence](../../reference/indexes/animehistory/README.md#category-index-initialization-and-first-screening--2026-10-26). |

The initial sandbox network attempt failed DNS resolution; the authorized scoped retry outside
that restriction downloaded the trial. Source CSVs and source episode/settei media were not modified.
Archives, manifests and contact sheets remain ignored/local-only. Further category screening,
live cleanup/prune after saved review, and official procedure adoption remain pending above.

Extractor constraints: source folders remain immutable, existing batches are refused, arguments are explicit, seek accuracy/actual timestamps are documented and extraction is limited to approved intervals. Broad episode extraction is not approved.

extract_reference_frames.py implements focused still extraction for explicitly requested times. Example: `python tools/reference-extraction/extract_reference_frames.py 4 --batch example --time 833 --time 834`. It accepts seconds, up to 32 distinct times per invocation, refuses existing batches, reads video only and saves native-size PNGs/logs under ignored reference/extracted-frames/episode04/example/. A trackable JSON manifest records source, stream, FFmpeg version, requested time, original decoded PTS/time base, PNG hashes and arguments. `UNREVIEWED` is the initial annotation status; observations belong in authored evidence notes. It does not authorize new episode/frame scope. See the Episode 4 startup review for the authorized batch and its limitations.

Verified user-environment tools: Python 3.14.6, Pillow 12.3.0, FFmpeg/FFprobe 9.0.1 Essentials, and ImageMagick 7.1.2-30 Q16-HDRI x64. Python and Pillow were already installed; the initial sandbox PATH check did not expose them. FFmpeg and ImageMagick were installed by the user after Phase 0. Windows app aliases may require running in the user environment rather than the sandbox. Codex also provides a bundled Python/Pillow runtime, used for the initial inventory/contact sheets.
