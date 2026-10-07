# Player, camera, and control

One physical character owns movement, interaction, animation, and future equipment. A perspective layer supports first and third person; do not duplicate incompatible characters.

Control modes: exploration, console interaction, seated/passenger, piloting, grappler control, and possible future EVA. Camera modes are independent: first person, third person, cockpit, chase, orbit, cinematic, and grappler tactical.

Seat transitions, input routing, collision, camera clipping, and animation constraints will be designed after spatial evidence and an approved implementation phase.

The user agreed reusable switchable magnetic boots and an in-game character/equipment status HUD during
[Phase 1.2 discussion](../implementation/phase-1-2-spatial-motion-decision-packet.md#reusable-equipment-and-character-status-hud--agreed-direction).
Equipment belongs to the same physical player across camera modes and future environments.
Status presentation reads player condition and equipment/environment state; it does not own a
second simulation or imply that an enabled boot is attached to a surface. Detailed slice behavior,
health mechanics, gravity transition and UI format remain for the scoped planning contracts.

Future HOTAS/pedals, voice, and external-panel adapters map into shared commands; command authorization uses applicable control context independently of camera perspective. See [external-control-automation.md](external-control-automation.md).
