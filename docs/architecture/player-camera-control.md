# Player, camera, and control

One physical character owns movement, interaction, animation, and future equipment. A perspective layer supports first and third person; do not duplicate incompatible characters.

Control modes: exploration, console interaction, seated/passenger, piloting, grappler control, and possible future EVA. Camera modes are independent: first person, third person, cockpit, chase, orbit, cinematic, and grappler tactical.

Seat transitions, input routing, collision, camera clipping, and animation constraints will be designed after spatial evidence and an approved implementation phase.

Future HOTAS/pedals, voice, and external-panel adapters map into shared commands; command authorization uses applicable control context independently of camera perspective. See [external-control-automation.md](external-control-automation.md).
