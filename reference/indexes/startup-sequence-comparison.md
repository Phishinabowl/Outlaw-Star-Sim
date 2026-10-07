# Startup comparison — Episodes 4, 7 and 8

Reviewed 2026-10-07 using the user's [episode-time notes](../episode-times.md). The Episode 7 range is **02:56–04:16**, as corrected by the user in chat; the original note is preserved unchanged. These locators were checked against the local MKVs. The Episode 4 08:15–08:20 hatch locator did not match the inspected shots; the confirmed hatch-opening frames remain around 09:18–09:19. A few adjoining frames and Episode 7's immediate debrief were inspected to establish context.

This pass reviews the named startup/launch sections and the supplied Episode 4 exterior/engine/grappler highlights. It does not audit whole episodes or complete the remaining settei scope. No gameplay state machine, geometry or startup checklist has been implemented.

## Sources and review method

- [Episode 4 metadata](episode-04-metadata.json): local source already identified in the first startup review.
- [Episode 7 metadata](episode-07-metadata.json): Creeping Evil; 807,002,816 bytes; 25:33.696.
- [Episode 8 metadata](episode-08-metadata.json): Forced Departure; 922,739,633 bytes; 25:08.672.

Episodes 7/8 both have 960×720 H.264 video stream 0, square pixels, 24000/1001 declared rate, 1/1000 video timestamp base, no chapters; English audio 1, Japanese audio 2, signs/songs ASS 3, full English ASS 4. Track 4 was copied with FFmpeg 9.0.1 Essentials using `-v error -n -i <source> -map 0:4 -c:s copy <ignored working path>`. Full copies remain local-only. Japanese audio and English dub were not listened to or transcribed.

Subtitle SHA-256: Episode 7 `bbabde4d258cc36ee543b0342df5a8cf43de143bfd51fe83a749dba475b3a931`; Episode 8 `f4213b818358da51c8a5e4d8cb261e5e657f347f5741fbb6d4db1bfb2fa32c6c`. Episode 4 subtitle provenance remains in [the earlier review](episode-04-startup-review.md).

**305 new native-size stills** were inspected using labeled contact sheets, with key engineering, console and reactor-display frames also opened individually. Sampling was one second across Episode 7's practice section and Episode 8's principal startup sections, selected points/three-second spacing for launch/context, and finer selected points for Episode 4's shield motion. This is not a complete frame-by-frame audit. Fine lettering is transcribed only where individually legible; no measurements were inferred from resized contact sheets.

| Episode/batch | Frames | Manifest |
|---|---|---|
| EP-04 user-leads-a / b | 32 / 22 | [a](episode-04-user-leads-a-frames.json), [b](episode-04-user-leads-b-frames.json) |
| EP-04 apparatus-details / motion-transitions | 32 / 15 | [apparatus](episode-04-apparatus-details-frames.json), [motion](episode-04-motion-transitions-frames.json) |
| EP-07 practice-a / b / c | 32 / 32 / 22 | [a](episode-07-practice-a-frames.json), [b](episode-07-practice-b-frames.json), [c](episode-07-practice-c-frames.json) |
| EP-08 departure-a / b / c / d | 31 / 32 / 32 / 23 | [a](episode-08-departure-a-frames.json), [b](episode-08-departure-b-frames.json), [c](episode-08-departure-c-frames.json), [d](episode-08-departure-d-frames.json) |

Each manifest carries exact source-relative filename, source byte size, tool/version, stream, requested seconds, decoded PTS/time base, PNG path/hash and argument array. All PNGs/logs/contact sheets remain ignored. Extraction-time UNREVIEWED flags are left intact; this authored record supplies observations. Web gallery offsets remain unverified and generated gallery CSVs are unchanged.

## Episode 7 — practice and an injected fault

The interval starts with a standby/liftoff-manual display, then a system activation exercise. The apparent critical failure is a training scenario: the immediate debrief explicitly refers to simulations in the English subtitle track (04:31.33–04:43.04). The ship remains at the dock afterward. Do not record a real reactor explosion or infer that normal startup is supposed to fail.

| Local timing and frame references | Direct visual evidence (A) | English subtitle evidence, original speech unverified |
|---|---|---|
| 02:57.010–03:08.021; practice-a 02–13 | LIFT OFF MANUAL lists SENCER (spelling as drawn), DRIVE and NAVIGATION as STAND BY; sensor line changes to START. | 03:04.18–03:14.59: sensor activation, CFS, subspace radar and sensor checks. CFS expansion is not supplied. |
| 03:09.022–03:14.027; practice-a 14–19 | C.F.S and SUBSPACE RADAR graphics occupy the front display. | Consistent with the preceding sensor callouts. This does not reveal all actual sensor hardware. |
| 03:20.033–03:27.040; practice-a 25–32 | ETHER DRIVE SYSTEM, SUB ETHER DRIVE SYSTEM and G.C.U / GRAVITY CYCLE UNIT appear together with schematics and Gilliam's display. | 03:15.26–03:27.63: ether drive, gravity control, sub-ether drive and navigation readiness called out. Preserve gravity control versus gravity-cycle wording as potentially different functions. |
| 03:28.041–03:35.006; practice-b 01–08 | Gene reacts and operates a small physical keypad/panel; display changes to STARTUP REACTOR / NEWTON REACTOR. | 03:28.17–03:32.14: Gene attempts gravity-cycle activation; Gilliam corrects him that the Newton reactor comes first. 03:33.91–03:35.97: Newton activation follows. This is the corrected dependency, not a complete universal order for every preceding callout. |
| 03:36.007–03:42.013; practice-b 09–15 | Numbered entries appear under the Newton heading; operating indicators, a falling-output indicator and a danger display are shown. | 03:36.81–03:47.91: units 1/2 operational, unit 3 abnormal, output falling through spoken numbers, Gene uncertain how to respond. Numeric units are unspecified; do not assume percentages or simulation constants. |
| 03:47.018–03:57.028; practice-b 20–30 | Gene uses the panel; display shows entries 2/4 rising and warnings. | 03:47.99–03:59.60: Gilliam advises balancing with remaining reactors; units 2/4 rise to increasingly high reported values. |
| 03:59.030–04:16.006; practice-b 32; practice-c 01–17 | Warning overlays, countdown reactions and a white flash. | 03:59.90–04:14.68: imminent explosion/critical countdown in the exercise. |
| 04:24.014–04:42.032; practice-c 18–22 | The real dock/sky is visible again, with Gene and Gilliam. | 04:24.86–04:43.04: failed simulated liftoff and need for manual response to unexpected faults. |

Individually inspected practice-b frame 25 at **03:52.023** shows the four numbered rows labeled **1 UPPER ENGINE, 2 RIGHT ENGINE, 3 LOWER ENGINE, 4 LEFT ENGINE** beneath STARTUP REACTOR / NEWTON REACTOR. Selected Japanese screen labels: 作動 (operating), 低下 (decreasing), 上昇 (rising), 危険 (danger). These are directly visible Japanese words, not a Japanese dialogue transcript. The orientation labels belong to that schematic's frame of reference; they do not establish ship-world port/starboard coordinates or the mapping of interior controls to exterior pods.

This is primary evidence that the show uses the Newton name and displays four indexed engine entries under that heading. The English translation also discusses reactors/sub-reactors. It strengthens the four-unit connection but does not establish the exact reactor topology, whether there is one shared Newton source, or the identity/count of any Münchhausen units. Neither the reviewed screens nor these subtitle intervals names Münchhausen. The complete naming conflict remains open, with stronger primary evidence now available.

## Episode 8 — standby to an actual planetary departure

| Local timing and frame references | Direct visual evidence (A) | English subtitle evidence, original speech unverified |
|---|---|---|
| 12:43.012–12:46.015; departure-a 01–04 | Gene at the dock, speaking before the bridge sequence. | 12:42.28–12:46.77: release systems from standby and transfer to navigation mode. 12:48.65–12:51.59: departure without tower guidance. This describes standby; it does not demonstrate long-term storage or a fully powerless cold start. |
| 13:04.033–13:08.037; departure-a 06–10 | External dock arms/support hardware against the vertically held red ship. | 13:08.94–13:10.63: container loaded. Exact loader attachment, container purpose and interface remain open. |
| 13:15.003–13:27.015; departure-a 11–23 | Gene adjusts restraints; close-up finger/button action; seating/control assembly moves upward relative to the floor and navigation cylinder in the subsequent bridge shot. | 13:18.71–13:28.11: CFS, Newton reactor, normal systems and verniers called out. No button function is assigned solely from the close-up. |
| 13:32.020–13:39.027; departure-a 28–31; departure-b 01–04 | Jim at his console and Melfina in the raised apparatus. | 13:32.46–13:41.76: weather-data acquisition, ether and sub-ether readiness. The weather-data acquisition is an illicit story action, not a normal docking protocol to reproduce. |
| **13:40.028–13:42.030**; departure-b 05–07 | All four engineering cylinders extended from the 2×2 bank, with control panels visible on several sides; no red wrapping bands in this shot. | 13:42.84–13:45.14: engine operation verified. This is a shared operating state; it does not show four separate manual unlocking procedures. |
| 14:12.018–14:16.022; departure-b 13–17 | Exterior engine mouth glows yellow; bright narrow blue/white elements appear, followed by a larger exhaust bloom and smoke. | Supports prelaunch engine effects; no calibrated temperature, thrust or fuel model. |
| 14:21.027–14:30.036; departure-b 22–31 | Ship remains at the launch structure amid exhaust/smoke, with external support/arm hardware nearby. | 14:24.71–14:33.41: crew readiness and gravity-cycle operational report. Engines running and ship released/lifting off are visibly distinct stages. |
| 14:34.040–14:58.022; departure-c 03–25 | Dock/ship, crew and Gilliam status views; lower hatch/support hardware at departure-c 25–27. | 14:48.24–15:00.01: airtightness, navigation data, life support, controls and all-system readiness. These are translated checks; unshown sensor layouts remain open. |
| 14:59.023–15:05.029; departure-c 28–32; departure-d 01–02 | Physical panel with illuminated indicators/map; Melfina status view. | 15:00.45–15:05.61: output stable, countdown begins at T-minus 30. Stability is checked before launch in this sequence. |
| 15:25.007–15:27.009; departure-d 04–06 | Bright engine plume while still alongside launch hardware. | Useful running-engine appearance. Increasing output is plausible from appearance but is not a measured output curve. |
| 15:42.024–16:30.031; departure-d 07–23 | Gene launch reaction, ship rises away, exhaust impacts dock structures, upward flight, roll/orientation changes and continuing ascent. | 15:41.09–15:42.72: zero/launch command; 16:05.35–16:07.28: roll complete. Nearby tower damage is story context, not a normal launch requirement. |

The whole visible procedure does not repeat Episode 4's ribbon removal. That is evidence about what is depicted, not proof that maintenance/unlocking can never be needed during later starts. A routine standby-to-navigation transition is supported; a definitive storage-to-standby power source or shutdown/storage checklist is not.

## Episode 4 — commissioning, shields and access

| Local timing and frame references | Direct observations and limits |
|---|---|
| 08:02.023–08:11.032; user-leads-a 01–03; apparatus-details 01–02 | Status graphics around the front display before later ignition. The inspected 08:15–08:20 points show crew dialogue, not the expected hatch. Treat user times as scene locators, not automatically exact. |
| 09:18–09:19; earlier unlock-followup 09–10 | Actual cap opening established by the previous focused frames. The additional 09:23–09:33 points show Jim/Gene/manual-display context. No full occupant descent is established here; absence from samples is not proof the action never appears elsewhere. |
| **10:33.508–10:35.009**; motion-transitions 05–09; apparatus-details 24–25 | Segmented front covers withdraw laterally from across Melfina's face/body toward the edges, exposing the front view. This resolves the direction and visible reveal stage. Exact end frames, travel, sealing and the full platform sequence remain open. The digital/connection view is stylized, not proof of a physical tunnel inside the cylinder. |
| 11:03.037–11:06.040; user-leads-a 18–19 | Small blue robot on the rail and corridor shot; supports the bridge/passage rail relationship. |
| 11:28.021–11:29.022; user-leads-a 20–21 | Schematic labeled SENSOR SCREEN / MODE 2 with sensor geometry. These two points do not establish the exact subsequent switch to a full forward exterior picture. |
| **11:59.010–12:00.011**; user-leads-a 23–24 | All four circular engineering faces are closed and carry crossed red bands. |
| **12:01.012–12:02.013**; user-leads-a 25–26 | Jim pulls a red strip away near a circular face. Earlier 12:03–12:07 close-ups show handle/front-plate rotation then cylinder extension. Combined visible external procedure: remove the crossed wrapping, manipulate the central handle, then extend the front cylinder. Internal latch/seal mechanism and force/angle limits remain open. |
| **13:56.002–13:57.003**; user-leads-a 32; user-leads-b 01 | All four cylinders are extended by ignition time, with visible local controls. This narrows the all-four question: initial wrapping and final extension apply to all four; the animation does not individually demonstrate Jim operating each unit. |
| 13:23.011–13:29.517; user-leads-a 27–30; motion-transitions 01–04 | Gene at external rectangular access hatch, then inside with hatch shut and hand at internal hardware. Confirms exterior/inside views and local control/latch interaction; precise inward/slide trajectory is not resolved by these samples. |
| 13:34.022; user-leads-a 31 | Access opening seen on the hull near attacking figures. Supports exterior location context; not a dimensioned hull position. |
| 13:59.005–14:08.014; user-leads-b 02–07; motion-transitions 10–15 | Generator/startup and MAIN/SUB power-conduit graphics, then bridge with apparatus open. The cluster changes position during the bridge shots, corroborated more clearly by Episode 8. No measured lift stroke or full circuit diagram established. |
| 18:52.006; user-leads-b 08 | Grey hull among asteroid debris, arms deployed. Useful pre-repaint exterior state; debris occludes detail. |
| 19:09.023–19:15.029; user-leads-b 09–15 | Pod/ship exhaust and acceleration shots. English subtitles at 18:57.70–19:05.74 separately discuss stabilizing before full output and warn against simultaneous rapid increase. The reported four sub-light engines at 19:17.99–19:20.89 is translated dialogue, not a reactor-name assignment. |
| 19:59.031–20:01.033; user-leads-b 17–19 | Escape pod, XGP and deployed grapplers. Exact anchor snag is not established in these points; use as grappler/encounter context. |
| 21:00.009–21:02.011; user-leads-b 20–22 | Grey ship with deployed arms and visible engine plume. Does not quantitatively establish a slow ramp or exit from the gravity well at that instant. |

The English subtitles tie packaging to initial commissioning: 11:09.75–11:15.21 describe a first-use wrapper metaphor; 12:00.53–12:02.76 attribute it to a Space Forces tradition. Treat that explanation as translated dialogue pending original-language listening. The visibly crossed bands themselves are direct evidence.

## What this settles, and what remains

| Open item | Current result |
|---|---|
| Visible engine unwrapping/unlocking | External one-unit action sequence now documented: band removal → handle/front-plate rotation → cylinder extension. Internal engineering and exact mechanical tolerances remain unresolved. |
| Treatment of all four units | All four start banded/closed in Episode 4 and end extended; all four also appear extended during Episode 8. Individual manual operation of every unit remains inferred, not directly shown. |
| Melfina apparatus | Hatch opening, cylinder rise and front-cover withdrawal have local frame evidence here; the subsequent [Episode 26 review](episode-26-platform-review.md) directly verifies occupant descent. Closure, complete continuous choreography and metric travel remain open. |
| Japanese terminology | Selected written Japanese labels remain available, including operating/output/danger indicators here. Spoken Japanese is unreviewed. English ASS is not original-language evidence. |
| Engine/reactor conflict | Primary on-screen NEWTON REACTOR plus four indexed engine entries is established; translated ordering/failure dialogue adds context. Münchhausen identity/count and full reactor-to-engine assignments remain unresolved. |
| Geometry-critical families | Stronger four-cylinder and moving seat-cluster evidence now constrains engineering service clearance and bridge motion. Remaining settei comparison, hull fit and unshown connections remain unfinished. |

For later design discussion, preserve three different contexts: first-use commissioning (EP-04), training/fault exercise (EP-07), and actual standby-to-launch operation (EP-08). The observed order and Gilliam correction can inform prerequisites; unobserved cold-storage stages, numerical balances, fault rules and shutdown behavior would require further evidence or explicit D/E/F design decisions.
