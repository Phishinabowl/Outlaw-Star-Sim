# Future ship simulation requirements

One authoritative ship state supports physical consoles, local controls, player commands, and Gilliam. Proposed areas: power, cooling, propulsion, navigation, sensors, communications, life support, grapplers, sub-ether drive, maintenance, and damage. Exact dependencies and numerical models are deferred.

Commands must be independent of UI and reusable by future external controls/automation. [External control and automation compatibility](external-control-automation.md) is the authoritative requirement for VoiceAttack, peripheral adapters, telemetry, structured command results, and optional language interpretation. All callers use the same validation and state; local intervention requirements remain enforceable.

Conceptual progression: SEALED/STORAGE → BATTERY/EMERGENCY → AUXILIARY POWER → MAIN POWER → FULL OPERATIONAL. This is a gameplay planning concept, not a verified canonical state machine.

Failure escalation requirements:

| Level | Recovery |
|---|---|
| 1 Automatic | Internal/Gilliam transient recovery |
| 2 Remote recoverable | Reset, clear breaker, restart, reroute, isolate |
| 3 Local intervention | Manual valve/switch/panel, jam, local breaker |
| 4 Component failure | Isolate, replace with spare, restart and verify |
| 5 Major damage | Severe structural/system damage; docking or major repair |

Keep commands, state queries, and presentation distinguishable. Component damage and command permissions remain design questions. Do not implement these requirements yet.
