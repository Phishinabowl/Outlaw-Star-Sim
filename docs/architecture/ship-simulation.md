# Future ship simulation requirements

One authoritative ship state supports physical consoles, local controls, player commands, and Gilliam. Proposed areas: power, cooling, propulsion, navigation, sensors, communications, life support, grapplers, sub-ether drive, maintenance, and damage. Exact dependencies and numerical models are deferred.

Commands must be independent of UI and reusable by future external controls/automation. [External control and automation compatibility](external-control-automation.md) is the authoritative requirement for VoiceAttack, peripheral adapters, telemetry, structured command results, and optional language interpretation. All callers use the same validation and state; local intervention requirements remain enforceable.

Earlier conceptual progression: SEALED/STORAGE → BATTERY/EMERGENCY → AUXILIARY POWER → MAIN POWER
→ FULL OPERATIONAL. Historical E/F sketch only; it is not the current slice state contract or a
verified canonical power topology.

Use [Baseline v1 operational vocabulary](../reconstruction/baseline-v1/operational-state-baseline.md) for commissioning, standby departure, sub-ether and emergency context. The single ladder above must not replace those separate sequences or imply a known power topology. The [Slice 1 contract](../reconstruction/baseline-v1/vertical-slice-1.md) defines the first implementation destination after a separately approved phase gate.

Failure escalation requirements:

For the current slice, the [accepted Phase 1.3 closeout](../implementation/phase-1-3-closeout-audit.md)
owns limited-service bootstrap, registered local preparation, actual key ignition, graceful OFF and
restart validation. Separate live service/unit state, retained per-run startup milestone and departure
warnings. No menu/animation/Gilliam line owns another completion flag. Engineering may stow/relock
only after completed OFF; every restart checks current all-four preparation. The failure ladder below
is future architecture, not a damage/repair or emergency-cutoff requirement for this demo.

| Level | Recovery |
|---|---|
| 1 Automatic | Internal/Gilliam transient recovery |
| 2 Remote recoverable | Reset, clear breaker, restart, reroute, isolate |
| 3 Local intervention | Manual valve/switch/panel, jam, local breaker |
| 4 Component failure | Isolate, replace with spare, restart and verify |
| 5 Major damage | Severe structural/system damage; docking or major repair |

Keep commands, state queries, and presentation distinguishable. Component damage and command permissions remain design questions. Do not implement these requirements yet.
