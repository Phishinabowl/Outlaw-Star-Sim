# Player, camera, and control

One physical character owns movement, interaction, animation, and future equipment. A perspective layer supports first and third person; do not duplicate incompatible characters.

Control modes: exploration, console interaction, seated/passenger, piloting, grappler control, and possible future EVA. Camera modes are independent: first person, third person, cockpit, chase, orbit, cinematic, and grappler tactical.

The accepted [Phase 1.3 contract](../implementation/phase-1-3-closeout-audit.md) now selects Gene
for the demo, ladder controls, equipment draw/stow, key-triggered seat raising/lowering, temporary
seat locks and pause/focus behavior. Exact bindings, animation technology, camera offsets and
physical collision/clipping proof remain later work. No implementation is authorized here.

The user agreed reusable switchable magnetic boots and an in-game character/equipment status HUD during
[Phase 1.2 discussion](../implementation/phase-1-2-spatial-motion-decision-packet.md#reusable-equipment-and-character-status-hud--agreed-direction).
Equipment belongs to the same physical player across camera modes and future environments.
Status presentation reads player condition and equipment/environment state; it does not own a
second simulation or imply that an enabled boot is attached to a surface. Detailed slice behavior,
health mechanics and UI artwork remain deferred. Selected ship gravity becomes available after
completed ignition; hangar low gravity remains separate across exit/re-entry. OFF lowers the seat
before withdrawing ship gravity. The closeout owns behavior; metrics/field blending still need fit/tuning.

Future HOTAS/pedals, voice, and external-panel adapters map into shared commands; command authorization uses applicable control context independently of camera perspective. See [external-control-automation.md](external-control-automation.md).
