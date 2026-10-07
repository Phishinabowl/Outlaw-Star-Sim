# Reference tools

inventory.py requires Python 3 and Pillow. It only reads source media; outputs are fixed under reference/. Run from any directory. No installation or episode decoding is performed.

Planned video tools: FFprobe for JSON container/stream/duration metadata; FFmpeg for selected timestamped frames; Pillow for contact sheets; CSV/JSON for scene/evidence records. ImageMagick is optional, not required. Manual visual review precedes transcription/translation; no blind OCR.

Future extractor requirements: reject destinations inside either source folder, refuse overwrites by default, use literal paths/argument arrays, document seek accuracy and actual timestamps, and extract only approved intervals. Broad episode extraction is not approved.

Verified user-environment tools: Python 3.14.6, Pillow 12.3.0, FFmpeg/FFprobe 9.0.1 Essentials, and ImageMagick 7.1.2-30 Q16-HDRI x64. Python and Pillow were already installed; the initial sandbox PATH check did not expose them. FFmpeg and ImageMagick were installed by the user after Phase 0. Windows app aliases may require running in the user environment rather than the sandbox. Codex also provides a bundled Python/Pillow runtime, used for the initial inventory/contact sheets.
