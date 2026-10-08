# Open questions

## Ongoing parallel research track

The reference foundation is substantially complete for initial-slice implementation purposes, as requested on 2026-10-07. This backlog remains active alongside future project work. It does not require completing every translation, room or performance calculation before a bounded slice can be planned. If a question would invalidate an adopted entry route, machinery clearance or physical interaction, investigate it before that concrete choice is built or record an explicit E/F assumption for agreement.

| Research thread | Current unresolved work | When it matters |
|---|---|---|
| Entry and circulation | Hatch correspondence, unshown boarding/engineering connections, dining/lounge identity | Before fixing affected slice geometry; broader cabins/cargo layout can continue later. |
| Motion and fit | Apparatus closure/cavity dimensions, seat/cylinder sweeps, per-unit manual treatment | Before affected mechanism/access implementation; preserve the [baseline reservations](baseline-v1/motion-clearance-envelopes.md). |
| Mechanical families/provenance | 22 scope records without focused passes, remaining annotations/variants, collection authentication | Prioritize sheets that constrain a chosen asset; full archaeology stays ongoing. |
| Terminology/topology | Original Japanese, Newton/Münchhausen assignments, actual initial-service source, circuits | Before making naming/power dependencies authoritative; no invented topology as canon. |
| Performance | Disputed ETA, percentage meanings, special modes, normal undamaged transition | Before numerical flight/power/combat models; not a prerequisite for Slice 1's non-flight endpoint. |

UE/toolchain direction is recorded in [Unreal strategy](../architecture/unreal-strategy.md). Phase 1.1
verified target MSVC 14.50 installed; build validation and remaining setup gaps are later work.
The [implementation plan](../implementation/vertical-slice-1-implementation-plan.md) records completed
1.1–1.3 planning and unstarted 1.4 onward. This research track does not authorize those later phases.

Planning-resolved is distinct from source-resolved: provisional entry/room choices and initial-service,
occupant/all-four, readiness/interruption behavior are accepted in the [1.3 closeout](../implementation/phase-1-3-closeout-audit.md).
Original topology, unshown all-four manual procedures and dimensions remain research/fit questions.
The 22-record figure is the original structured-pass checkpoint; later targeted reservations/headroom
reviews do not silently authenticate sheets or constitute full fine-callout passes.

## Existing findings and unresolved details

### Passage floor hatch / storage recollection — pending, 2026-10-07

The user recalls Jim or Melfina below a round passage floor hatch among food/gear, with a Gilliam
robot assisting handling. Episode, timestamp and hatch identity are unknown. This is an unverified
user lead; it does not replace SET-044/045's reviewed exterior-access label for H03 or prove that
the recollected space is reached through H03 rather than another opening. An exterior-access route
could involve an intermediate space; its complete topology remains unresolved.

A focused keyword search of the already cached 26 English ASS tracks found a useful separate lead:
EP-09 11:00.03–11:07.13 mentions a cargo hold and Jim occupying it. Adjacent 11:07.30–11:12.47
mentions quarters and a maintenance rail. These are translated dialogue references, not visual proof
of the floor hatch, room placement or robot-assisted handling. EP-06 15:27.67–15:30.73 mentions
ship supplies, but the surrounding dialogue is outside-storage story context and supplies no hatch
correspondence. Source/track provenance remains in [subtitle coverage](../../reference/indexes/performance-subtitle-coverage.json).

Next targeted check: locate the recalled storage/handling scene and compare opening shape, ladder,
wall/rail features and local route with H03 and other hatch records. Retain below-floor access volume
as unresolved before fixing passage geometry. Storage gameplay or another playable room is not added
to the slice by this lead; any proposed reserved destination remains explicit E until verified.

[Baseline v1](baseline-v1/spatial-constraint-map.md) converts evidence into constraints for the [first slice](baseline-v1/vertical-slice-1.md). VS-D01–07 identify focused decisions before graybox/implementation approval: entry correspondence/route, room connections, motion fit, initial service power, occupant/all-four preparation adaptations, readiness behavior and tool/asset policy. Unresolved full-ship questions below do not automatically expand the slice.

The [all-26-episode subtitle audit](../../reference/indexes/performance-subtitle-audit.md) now collects performance leads. Priority checks: EP-10's literal 1000-hour ETA versus subsequent race progress; EP-20's 150% grappler-response/one-minute mode; EP-11's 108% output and sensor-error/range measures; EP-24's acceleration-versus-output wording. Original Japanese, absolute power/thrust/mass, normal sensor ranges and full drive topology remain unresolved. EP-16's translated narration calls dragonite an ether-energy catalyst; do not adopt a burned-fuel consumption model from the supplied screenshot alone.

Performance follow-up: [Episode 11 numerical evidence](../../reference/indexes/episode-11-subether-review.md#numerical-travel-performance-follow-up--2026-10-07) records the 600-million-km / approximately 96-hour ether-only forecast at stated 50% propulsion, plus a separate 12 km/s navigation report. The derived approximately 1,736 km/s trip average is non-canon D evidence. Verify original-language numbers, percentage basis and any route/acceleration assumptions before choosing a power/speed model; absolute reactor output remains unknown.

Latest propulsion update: [Episode 11 transition/recovery](../../reference/indexes/episode-11-subether-review.md) documents preparation visuals, disrupted jump, key removal/restart and auxiliary operation. English subtitles link Münchhausen output to sub-ether transition and separately identify Newton reactors 1–4 in the adjoining damage report. This narrows earlier naming uncertainties; original speech, physical assignments, fuel and complete power topology remain unresolved. An undamaged successful transition and fin motion across cuts still need review.

Latest apparatus update: [Episode 26 follow-up](../../reference/indexes/episode-26-platform-review.md) directly verifies Melfina descending through the open circular floor hatch at 21:25.784–21:27.536. This supersedes earlier occupant-descent uncertainties below. Hatch closure, continuous complete choreography, support hardware, cavity depth and metric travel remain open. The user's reactor/drive screenshot is a secondary research lead; dragonite fuel, the Münchhausen/sub-ether dependency and full Newton/Münchhausen assignment remain unverified.

- Resolved: [Sunrise World's official profile](https://www.sunrise-world.net/titles/pickup_094.php) supports the 72 × 21 × 16 m exterior envelope (EXT-004). Usable internal dimensions remain open.
- What is the collection's provenance, and which sheets are final/approved versus preliminary?
- Which printed sheet numbers and Japanese titles are legible at full resolution?
- Primary Episode 7 display now names NEWTON REACTOR and groups four indexed engine entries beneath it. What source establishes the exact reactor/engine assignments and the Münchhausen identity/count? The complete conflict remains unresolved.
- What connects bridge, crew/cabin/cargo/utility areas, dorsal Assault Shooter, grapplers, and aft engineering?
- What is the actual deck count and usable interior envelope?
- What engine motion, clearance, service access, and panel behavior does Episode 4 show?
- How do the four main engine assemblies relate to exterior propulsion geometry and the distinct sub-ether drive?
- What is the spatial relationship of Melfina's apparatus to seats and bridge access?
- Which doors, hatches, ladders, maintenance units, and panels are repeatable across scenes?
- What scale constraints can character references support without treating perspective distortion as measurement?
- Which contradictions require explicitly classified connecting geometry?
- Which power progression and maintenance actions are canon, inference, or gameplay adaptation?
- Which episode audio/subtitle tracks should support terminology review? Do translations disagree?
- UE 5.8 is selected with installed candidate 5.8.3; actual build proof and project-owned binary/LFS policy remain later work.

Detailed interior review adds these concrete checks:

- SET-006 states approximately 2 m floor-to-ceiling for ship sections: how does this reconcile with engineering platforms, apparatus motion, and character shots?
- SET-030 labels an engine control cylinder: which components actually extend during Episode 4 startup?
- SET-045 labels access to the Assault Tube: how does that connect to the Assault Shooter assembly in SET-125?
- SET-027 needs a below-floor navigation-platform cavity: how deep is it and where does it fit in the forward hull?
- Are the July rest-room/lounge configurations SET-088/089 the same space as the dining room? Keep the April preliminary SET-043 geometry separate.
- Do the bridge emergency hatch, passage exterior-access floor hatch, and airlock connect or represent separate openings?
- What web-to-local timestamp offset applies to the Episode 4 gallery? Metadata has no chapters; defaults select English audio and signs/songs subtitles, so full-dialogue review must choose tracks explicitly.

The [focused Episode 4 startup review](../../reference/indexes/episode-04-startup-review.md) now establishes local PTS for cylinder rise, manual engineering extension, key engagement and generator/main-sub power graphics. Complete trajectories, precise cut boundaries and original-language wording remain open. Determine the exact engine seal-release procedure and whether all four units receive the same treatment. Keep Jim's visibly shown engineering work distinct from Gene's cockpit-key operation, and distinguish other-ship dialogue in intercut scenes.

The [six-item follow-up](../../reference/indexes/startup-open-items-followup.md) refines the visible handle/front-plate rotation before extension, and confirms selected plasma-drive/hyperspace-screw production labels. It leaves the exact internal lock mechanism, all-four procedure, complete navigation-platform/shield animation and Newton/Münchhausen assignments open. Recollections are requested as episode-search leads, not direct evidence.

[Review of the user's Episode 4/7/8 locators](../../reference/indexes/startup-sequence-comparison.md) verifies crossed bands, one manual sequence, all-four endpoints and front-shield withdrawal around 10:33.5–10:35. EP-26 separately verifies occupant descent; complete joined choreography remains unverified. Episode 7's Newton-before-gravity-cycle instruction is training evidence; Episode 8 shows standby departure. Original speech, canonical storage/shutdown and every-unit manual treatment remain research questions; the demo's bounded adaptations are accepted separately.
