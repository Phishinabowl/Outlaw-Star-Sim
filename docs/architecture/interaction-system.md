# Interaction requirements

Doors, hatches, access panels, seats, consoles, engine service controls, and maintenance access should map to physical equipment and authoritative state. Future reusable C++ foundations should allow editor-configured prompts, access conditions, command requests, and animation/audio responses.

Local actions and remote commands must affect the same equipment state. Gilliam uses the shared
command interface. The [accepted Phase 1.3 contract](../implementation/phase-1-3-closeout-audit.md)
selects contextual clicks, specific holds/directional inputs, local laptop connections, focused
typing, resumable dialogue and actual progress/cancel/completion rules. Exact ranges/bindings and
implementation APIs/UI technology remain Phase 1.4 or tuning decisions. Multiplayer is outside this slice.

Controls submit simulation commands rather than owning their effects or success state. Follow [external-control-automation.md](external-control-automation.md) for shared validation/results and caller context. A common interface must preserve actions that require physical presence or local maintenance.
