# External control and automation compatibility

## Agreed requirement

Core ship functions must be exposed through a reusable command interface so future clients such as VoiceAttack, HOTAS bindings, Stream Deck integrations, telemetry tools, and Gilliam AI can invoke the same authoritative simulation commands as in-world controls.

This is a future architecture requirement, not an integration implementation or a canon claim. Its authoritative home is this document. It extends the shared-state/Gilliam principle already recorded in ship-simulation.md.

## Shared commands and state

In-world panels, cockpit controls, input bindings, external adapters, and Gilliam submit requests to the same command layer. That layer validates requests against authoritative ship state and owns execution/results. UI widgets, spoken phrases, camera perspective, and client software must not own separate ship state or determine whether an operation succeeded.

Commands should be addressable independently of UI, with explicit targets and parameters. Illustrative identifiers include power.auxiliary.start, propulsion.engine3.shutdown, navigation.setDestination, grappler.left.deploy, subEther.prepare, and diagnostics.run. These are examples, not an approved command registry, engine-numbering scheme, or confirmation of particular hardware.

Future commands need to express:

- Caller permissions and applicable control context.
- Prerequisites and interlocks checked by the simulation.
- Execution state, distinguishing rejection, acceptance/in-progress, completion, and failure.
- A structured failure reason and relevant state values.
- Resulting state changes/events that clients can query or observe.

Acceptance is not completion. A client must report the actual result rather than announce success because it recognized a phrase or sent an input. A shutdown request for an isolated/damaged engine should return the real equipment state; a drive request without sufficient charge should report the actual unmet prerequisite. Example charge percentages in planning discussions are illustrative, not chosen engineering parameters.

Read-only status/diagnostic queries and telemetry should expose the same authoritative state. External dashboards and spoken reports must not invent values. Later interface design should consider request correlation and duplicate handling so retries cannot accidentally repeat consequential actions; exact schemas and mechanisms remain undecided.

## Physical interaction remains meaningful

A common interface does not make every action remotely available. Equipment requiring local intervention must retain locality/access requirements. Voice, automation, and Gilliam cannot bypass local-only switches, jams, maintenance access, or component replacement merely by calling the same interface. Which operations are remote, local, or automatic is a later system-design decision.

Caller authorization is separate from camera mode. Perspective changes must not alter command availability; seats, stations, equipment access, and control modes can supply relevant context. No multiplayer authority/networking design is selected here.

## External adapters

VoiceAttack is a proposed external recognition/phrase client. An adapter could translate its output into simulation commands and receive real results; embedding VoiceAttack in Unreal is not required by this plan. HOTAS/pedals, Stream Deck, physical panels, and external dashboards are compatibility targets, not committed peripherals or current dependencies.

Transport options discussed include localhost HTTP, WebSocket, named pipes, UDP/TCP, or a plugin/interface. None is selected. Protocol/versioning, lifecycle, discovery, and access control need review before implementation. Do not expose a service or install integration plugins in this planning phase.

## Gilliam and language interpretation

Recognition or an eventual natural-language interpreter maps user intent to known commands; the deterministic simulator remains authoritative. An LLM must not directly mutate ship state, invent commands, bypass checks, or claim success without execution evidence.

Proposed progression, with separate future approval gates:

1. Fixed phrases mapped to explicit commands.
2. Parameterized commands with target/value validation.
3. Natural-language interpretation into the known command interface.
4. Context-aware, multi-step orchestration with actual prerequisites/results.

Multi-step preparation/departure sequences are proposals. Ordering, interruption/cancellation, partial failure, ambiguous intent, and actions requiring confirmation remain open design questions. Dependencies are not established by the illustrative sequence in the supplied discussion.

## Crew domains and evidence

Possible presentation domains: Gilliam for diagnostics/automation/power/status/navigation support; Jim for sensors/communications/navigation assistance; Melfina for navigation/sub-ether/Leyline-related feedback. These are proposed role mappings pending anime evidence, not verified canonical permissions or assignments.

Do not force Suzuka, Aisha, or other characters into engineering roles without an explicit design decision. Any expanded crew-assistant behavior must be labeled GAMEPLAY_ADAPTATION and separated from observed anime behavior. Crew voices/personalities can present requests and results without creating alternate simulations.
