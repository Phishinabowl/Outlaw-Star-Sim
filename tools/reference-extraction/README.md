# Reference tools

inventory.py requires Python 3 and Pillow. It only reads source media; outputs are fixed under reference/. Run from any directory. No installation or episode decoding is performed.

inspect_episode.py requires Python 3 and FFprobe on PATH. Run python tools/reference-extraction/inspect_episode.py 4 from the repository root to inspect Episode 4. It selects exactly one matching numbered source, reads container/stream/chapter metadata, and writes reference/indexes/episode-04-metadata.json. No media is decoded/extracted or modified. Metadata output for that episode is replaced when rerun; no episode content hash is computed.

cache_timestamp_index.py uses Python's standard library to cache public AnimeHistory HTML under ignored reference/cache/animehistory/ and generate timestamp/caption/image-link CSVs under reference/indexes/animehistory/. It downloads no images. It validates cached hashes, pagination, IDs and declared counts; reruns reuse cached pages and replace the generated index. See reference/indexes/animehistory/README.md for alignment limits and usage.

Planned video tools: FFprobe for JSON container/stream/duration metadata; FFmpeg for selected timestamped frames; Pillow for contact sheets; CSV/JSON for scene/evidence records. ImageMagick is optional, not required. Manual visual review precedes transcription/translation; no blind OCR.

Future extractor requirements: reject destinations inside either source folder, refuse overwrites by default, use literal paths/argument arrays, document seek accuracy and actual timestamps, and extract only approved intervals. Broad episode extraction is not approved.

extract_reference_frames.py implements focused still extraction for explicitly requested times. Example: `python tools/reference-extraction/extract_reference_frames.py 4 --batch example --time 833 --time 834`. It accepts seconds, up to 32 distinct times per invocation, refuses existing batches, reads video only and saves native-size PNGs/logs under ignored reference/extracted-frames/episode04/example/. A trackable JSON manifest records source, stream, FFmpeg version, requested time, original decoded PTS/time base, PNG hashes and arguments. `UNREVIEWED` is the initial annotation status; observations belong in authored evidence notes. It does not authorize new episode/frame scope. See the Episode 4 startup review for the authorized batch and its limitations.

Verified user-environment tools: Python 3.14.6, Pillow 12.3.0, FFmpeg/FFprobe 9.0.1 Essentials, and ImageMagick 7.1.2-30 Q16-HDRI x64. Python and Pillow were already installed; the initial sandbox PATH check did not expose them. FFmpeg and ImageMagick were installed by the user after Phase 0. Windows app aliases may require running in the user environment rather than the sandbox. Codex also provides a bundled Python/Pillow runtime, used for the initial inventory/contact sheets.
