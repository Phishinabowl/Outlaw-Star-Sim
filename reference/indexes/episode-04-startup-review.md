# Episode 4 startup — local evidence review

Reviewed 2026-10-06 from the [local episode source metadata](episode-04-metadata.json). The user's continuation authorized focused startup-scene inspection. Extracted 54 explicitly selected stills in four small batches, plus one initial FFmpeg timing-method probe; no continuous frame sampling or video clips were generated. PNGs/logs remain ignored under reference/extracted-frames/episode04/; the initial probe and subtitle copy remain under reference/working/episode04/. Sources are unchanged. No media is authorized for Git publication.

The local full English ASS subtitle stream (absolute index 4) was copied without transcoding to locate candidate scene times. It is a translation, not a Japanese transcript. Audio was not reviewed, extracted or compared. The entire subtitle copy remains local-only; only focused paraphrases are recorded below. Subtitle speaker attribution is not reliable by itself.

Subtitle provenance: FFmpeg 9.0.1 Essentials; arguments `-v error -n -i <local episode source> -map 0:4 -c:s copy reference/working/episode04/dialogue.ass`; SHA-256 `560974c33b10f385fd8c30d006959a7e33f741e6fa8ab7237b4c24bb8b294d0b`. The source is the exact filename recorded in episode-04-metadata.json.

## Timing and reproducibility

[Frame manifests](episode-04-startup-review-frames.json), [detail manifest](episode-04-startup-detail-frames.json), [mechanisms manifest](episode-04-startup-mechanisms-frames.json) and [clearance manifest](episode-04-startup-clearance-frames.json) record each request, actual decoded presentation timestamp (PTS), video stream 0, image/log path, PNG hash, FFmpeg version and reproducible argument array. All stills are 960×720, without resizing or subtitle burn-in. PNG conversion preserves the decoded image at native dimensions; it does not restore source compression losses or establish an authoritative color reference.

`extract_reference_frames.py` uses accurate input seeking with `-copyts` and records the first `showinfo` frame's original PTS/time base. It refuses an existing batch, accepts at most 32 distinct explicit requests per invocation, and fixes outputs under reference/. An additional buffered frame can appear in the log; `n=0` is the exported PNG. Manifest `UNREVIEWED` values are extraction-time defaults; this authored review supplies the observations.

Initial method probe: reference/working/episode04/probe-1105.png, requested 665 s, decoded PTS 665039 with time base 1/1000 (665.039 s), stream 0, 960×720. It used `-copyts -ss 00:11:05 -i <local source> -map 0:0 -an -sn -dn -vf showinfo -frames:v 1 -fps_mode passthrough` with FFmpeg 9.0.1 Essentials. It is a timing-method check, not an additional scene evidence record.

Validation: all 54 batch PNGs reopened successfully at native dimensions and matched their recorded hashes. Integer PTS/time-base calculations matched recorded seconds; every exported PTS was at or after its request and less than 43 ms later. Invalid nonfinite time and existing-batch calls were rejected before output creation. All 221 scan hashes matched the immutable-source manifest.

The two remote gallery-image requests (web labels 11:14 and 13:54) could not be opened through the web reader. **No web/local offset or gallery image match is established.** Existing generated gallery CSVs remain untouched and UNVERIFIED. The local findings below use local PTS independently. Approximate ranges group reviewed shots; they are not frame-precise scene boundaries.

## Visually reviewed observations — A, CANON_DIRECT

Frame references use batch suffix and frame number; the linked manifests resolve each to a source-relative PNG and PTS.

| Local decoded time | Frame reference | Directly visible observation | Reconstruction consequence / limit |
|---|---|---|---|
| 05:15.023 | startup-review 01 | Hilda leans over a cockpit station in a dim bridge; wheel/grip hardware and circular floor cap visible. | Establishes pre-brightening bridge appearance. Does not identify what she operates from this still alone. |
| 05:42.008 | startup-review 02 | Brightly lit bridge with Hilda, Gene, Jim and Melfina, seats and overhead structure. | Contrasts with the earlier dim shot. Exact lighting switch and power source remain unresolved. |
| 09:14.012; 09:18.016 | startup-clearance 03–04 | Melfina stands beside the circular cap near the rear doorway; the cap is raised/opening in the latter shot. | Corroborates apparatus location relative to seat/doorway. The occupant's full downward platform movement is not captured here. |
| 09:34.032; 09:35.033 | startup-mechanisms 05; startup-detail 01 | Front display presents a control manual with wheel/grip diagrams and a key-entry/start-engine illustration. | Onboard instructional UI is directly shown. Fine decorative/garbled text is not reliable technical documentation. |
| 09:37.035 → 09:40.038 → 09:41.039 → 09:42.040 | startup-detail 02; startup-review 03; startup-mechanisms 06; startup-detail 03 | Closed cap/low state progresses to a short raised shell, taller shell, then a higher cylinder from another angle. | Supports upward deployment matching SET-027/086. Camera changes prevent metric stroke or speed calculation. |
| 10:25.041; 10:30.004; 10:35.009 | startup-review 05; startup-detail 06–07 | Melfina appears within the blue-green apparatus, hair suspended and bubble-like specks visible. | Supports the depicted visual appearance. Substance, pressure, biological function and causal dependencies remain unestablished. |
| 10:42.016; 11:25.018 | startup-review 06,08 | Tall cylinder behind the seats; later view exposes Melfina through an opening bordered by segmented shielding. | Corroborates the raised apparatus and shield/open-view state. Exact shield motion onset and interlocks are not measured. |
| 11:56.007; 11:58.009 | startup-detail 13–14 | Jim is beside a small blue maintenance unit on a wall/overhead rail in the ship's passage; circular overhead opening and doorway visible. | Direct robot/rail/passage reference; does not establish a complete route or lifting capacity. |
| 12:04.015 → 12:05.016 → 12:06.017 → 12:07.018 | startup-detail 15; startup-mechanisms 07–09 | A gloved hand/grey sleeve manipulates a red bar in the round engineering face's central recess; circular front section extends away from its housing, revealing a cylindrical side and supports. Nearby shots establish Jim as the person undertaking this work. | Supports local manual manipulation and control-cylinder extension consistent with SET-030/091/196. Does not prove exterior engine translation, stroke length, four-unit sequence or exact unlock steps. |
| 13:53.041; 13:54.000 | startup-review 12; startup-detail 19 | Key socket beneath/right of an analog-style gauge; Gene's blue-gloved hand engages the key/socket in the later still. | Corroborates SET-040/087 key location. These stills do not measure a complete turn angle or prove the key alone satisfies all prerequisites. |
| 13:58.004 | startup-review 13 | Startup graphic shows a generator-like assembly and visible labels START GENERATOR, ENGINE CONDITION ALL GREEN and 起動設定 (startup settings; working reading). | Evidence for startup-display content, not a literal room layout or authenticated reactor type. |
| 14:02.008 | startup-review 14 | Schematic labeled POWER CONDUIT, with four MAIN branches and four SUB branches plus CONNECT labels. | Direct support for main/sub power presentation. Branch count on a graphic does not establish four physical batteries or circuit topology. |
| 14:05.011 | startup-review 15 | Gene and Jim seated ahead of Melfina's raised cylinder; bright cockpit with wheel/grip fittings. | Useful combined operating-state bridge view. Motion/lift is not proved by a single still. |

Other extracted stills were inspected but contain reaction shots, exterior combat, dock context, transitions or eyecatches rather than stronger startup-mechanism evidence. They are retained locally for an honest record of the focused search, not promoted into unrelated equipment evidence. The dock view at 12:15.026 (startup-detail 18) is context, not a measured hangar plan.

## Subtitle-supported claims — translation pending audio verification

| Local subtitle interval | Paraphrased content | Use and limits |
|---|---|---|
| 05:19.34–05:25.30 | Activation/key screen labels. | Early ship activation lead; keep distinct from later main-engine ignition. |
| 09:28.48–09:34.51 | Wait for Melfina; control manual will be displayed. | Consistent with the visually inspected manual. |
| 10:38.02–10:41.68 | Link established; engine activation proposed. | Supports ordering lead only; Japanese wording/speaker still unreviewed. |
| 10:52.50–11:02.17 | Engines described as sealed/unavailable; engine room indicated. | A startup obstacle is translated. Its precise physical cause remains open. |
| 11:17.22–11:23.12 | Engine tested individually, with no recorded test after installation. | Commissioning/history claim from English translation only. |
| 13:46.56–13:52.02 | Preparations complete; ignition key requested. | Supports preparation-before-ignition sequence. |
| 13:57.50–14:03.06 | Engines/generators operational; transfer from sub-circuits to mains. | Consistent with startup/power graphics; no battery chemistry, capacity or complete dependency model inferred. |
| 14:06.91–14:10.14 | Systems ready; ether drive standing by. | Post-ignition status lead. Does not settle Newton/Münchhausen terminology. |

Do not attribute the 09:58.81–10:02.41 translated ether-drive-active line to XGP without checking shot/speaker context: the intercut scene shows Hilda aboard the other ship. It cannot establish that XGP's ether drive is already active then. Likewise, a subtitle addressing Gene does not identify Jim's visibly shown engineering work as Gene's action.

## Result and remaining checks

[Opening/bootstrap extension](episode-04-opening-bootstrap-review.md), 2026-10-07, adds the user's
03:40-onward reveal/boarding and portable-computer sequence, Gilliam's introduction and registration.
It supplies early-stage references without changing the later observations or claiming audio verification.

Local startup evidence now supports separate early activation, navigation-apparatus preparation, manual engineering intervention, key engagement, generator startup and main/sub power presentation. This is an observed scene order plus translated dialogue leads, not an implemented simulation state machine.

Still open: complete occupant descent; fine hatch/shield trajectories; exact manual seal-release mechanism; wide engineering view with exposed control panel; whether/when all four cylinders are treated; Japanese/dub terminology; exact cut boundaries; web/local image alignment. Full-source frame sampling and a complete episode transcript are outside this increment.

[Follow-up dated 2026-10-07](startup-open-items-followup.md) adds closer handle/front-plate rotation and hatch-opening observations, while retaining the four-unit, full-platform/shield and spoken-terminology questions. It distinguishes a rear cylinder view from a front shield-state observation.
