# Episode 4 metadata inspection

Inspected 2026-10-06 with FFprobe 9.0.1 Essentials. Source was read only; no frames, audio, or subtitles extracted. [Raw metadata](episode-04-metadata.json) records tool version, arguments, and source-relative filename.

## Local source

_source_episodes/[CBM]_Outlaw_Star_-_04_-_When_the_Hot_Ice_Melts_[720p]_[000FA756].mkv

815,458,262 bytes; Matroska container; duration 1,519.018 s (**25:19.018**); container/video start time 0. No chapters are present. A creation-time tag is not proof of release provenance.

| Absolute stream index | Content | Notes |
|---|---|---|
| 0 | H.264 High video, 960×720, progressive, yuv420p (8 bit) | 4:3; square pixels; declared/average rate 24000/1001 (~23.976 fps); default |
| 1 | English AAC-LC stereo, 48 kHz | Default audio; title English: Stereo |
| 2 | Japanese AAC-LC stereo, 48 kHz | Title Japanese: Stereo |
| 3 | English ASS subtitles | Default, but **Signs/Songs**, not full dialogue |
| 4 | English ASS subtitles | Full-subtitle track by title: English Subtitles |
| 5–7 | Three TrueType font attachments | Subtitle-rendering resources; not evidence frames |

For original-language terminology review, explicitly select audio stream 2 and subtitle stream 4 (subtitle labels are English, not a Japanese transcript). Compare stream 1 dub where terminology differs. Default playback selects English audio and signs/songs, so leaving defaults untouched can omit dialogue subtitles. Track labels have been inspected; transcript accuracy and actual speech remain unreviewed.

Video timestamps use a 1/1000-second time base despite the fractional frame rate. Do not derive an exact presentation timestamp by multiplying frame number by a rounded 23.976 rate. Container metadata alone does not establish constant frame cadence or locate startup scenes.

## External timestamp index

[AnimeHistory Episode 4 gallery](https://www.animehistory.org/gallery/screencaps/outlaw-star/episode-4/) is the EXT-001 locator source. Prior research confirmed timestamp captions, but direct gallery retrieval returned cache-miss errors during this pass. No web frame was visually compared with the local episode, and no offset has been established. The earlier 14:37 example was illustrative, not a validated engineering timestamp.

Use gallery captions as candidate times only. Before a targeted extraction batch, match at least two recognizable shots against local playback/frame data (preferably before and after the relevant sequence). Record external time, local decoded PTS, source, and match status; allow changing offsets if the edits differ. No broad sampling is needed to inspect metadata.

Subsequent direct HTML caching succeeded: [local Episode 4 CSV](animehistory/episode-04.csv) now contains all 354 gallery records across four pages, covering 00:01:43–00:23:14. This resolves access to timestamp metadata, not visual matching or alignment. See [cache/index usage](animehistory/README.md).

## Proposed targeted evidence targets — not yet extracted

1. Exterior discovery/dock and physical entry: hatch approach, control access, entry direction, character scale.
2. Engineering before/during/after activation: four circular faces, manually operated parts, cylinder movement, local panel details and service clearance. Compare SET-030/046 and distinguish control cylinders from whole engines.
3. Bridge activation and Melfina apparatus: occupant descent, hatch/cylinder/shield stages, seating arrangement and indicator/rail position. Compare SET-006/022/027/028/040.

Select specific verified times/short intervals for approval. Extraction must target ignored reference/extracted-frames/episode04/, preserve source dimensions, use no subtitle burn-in for geometry evidence, and record requested time plus actual decoded PTS. PNG can preserve decoded pixels but cannot undo the source's lossy H.264 compression. Video origin from a particular Blu-ray release remains unverified.
