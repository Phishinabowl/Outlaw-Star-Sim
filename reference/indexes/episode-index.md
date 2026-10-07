# Episode source index

26 numbered episode MKVs plus one S3 pilot and one SFV are present. Exact names and byte sizes are in source-manifest.json. The numbered run is 01–26 with one file per number. The pilot is separate and must not shift episode numbering.

Episode 4 resolves uniquely by the filename token _-_04_-_:

_source_episodes/[CBM]_Outlaw_Star_-_04_-_When_the_Hot_Ice_Melts_[720p]_[000FA756].mkv

Filename title: When the Hot Ice Melts. Filename resolution marker: 720p; actual video stream dimensions, duration, codecs, frame rate, language tracks, subtitles and offsets are not yet probed. The bracketed checksum token is not a verified content digest.

The highest-priority review is the discovery/activation/startup sequence supplied by the brief. No timestamps are invented and no frames have been extracted.

External scene-locator links and their verification limits are recorded in [external-sources.md](external-sources.md). Item 12 of the supplied earlier research passage identifies the all-episode timestamp source as AnimeHistory's screencap galleries. Source identification is resolved; web timestamps still require alignment with the local files.

## Proposed scene record schema

scene_id, episode_id, source_filename, start_timestamp, end_timestamp, time_basis, stream_id, observation, evidence_classification, verification_status, frame_paths, related_scan_ids, open_questions.

Use file playback timestamps for the local release. Record any episode-relative offset explicitly. Split observations about sealed engine state, manual actions, extended assemblies, local panels, character scale, room entry, and bridge activation into independently checkable records.
