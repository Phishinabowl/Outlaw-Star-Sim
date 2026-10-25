# Spatial Validation Procedures — VS1-G01–G03

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 3 player/route/clearance proxies; later integrated repeats retain their existing owners |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [Phase 1.2 closeout](../phase-1-2-closeout-proposal.md), [Phase 1.3 behavior contract](../phase-1-3-closeout-audit.md) |
| Execution prerequisite | Phase 2 exit and explicit authorization for the applicable Phase 3 subphase |

These procedures add no geometry, gameplay, numerical gravity settings or new acceptance dimensions.
The selected E layout and F interactions remain reconstruction/gameplay choices, not canon. Phase 1.4
remains planning in progress; Phase 1.5 and implementation remain unstarted.

## Shared Setup And Evidence

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules):
  identify revision/settings, actual starting state, performer, expected/actual result and untested parts.
  Codex reviews authorized asset/configuration evidence; the repository owner observes feel, visibility
  and physical fit unless another observation method is specifically authorized. Computer Use retains
  its separate permission requirement.
- Use measured owned proxies and a dimensioned fixture. Record the actual body, collision, camera,
  equipment and occupant sizes instead of silently inheriting mannequin/template dimensions.
  The closeout's nominal 1.80 m standing proxy and 0.20 m head-clearance target are initial E fit
  proposals, not verified character measurements or permission to shrink the eventual body.
- Capture relevant views/sections and collision evidence. A state flag, bounds box or attractive
  screenshot alone does not prove traversal, reach or occupied motion clearance.
- Distinguish proxy geometry, temporary test placement and functioning runtime mechanisms. Inspecting
  endpoint/sweep proxies cannot close actual-motion validation in Phase 6.4.
- Keep the existing MC-01–08 and RA-01–10 references; do not create a competing mechanism ledger.
  Raw captures remain local; authored summaries link source IDs, E/F choices and evidence locations.

## VS1-G01

**One physical body with first- and third-person views**

**Owning checkpoints:** 3.1; occupied repeat 3.4 and integrated repeat 8.1.

**Starting state:** authorized neutral player/scale fixture, one player actor and recorded body/camera
configuration. No detailed Gene model, full inventory, controller support or ship machinery is required.

### Planned Steps

1. Record physical actor identity, transform, collision dimensions and the two camera configurations.
   Compare measured body scale with the selected fit proposal; document differences before room fitting.
2. Traverse the neutral reference floor/opening in first person, stop at a repeatable marker and switch
   views. Compare actor identity, physical position and collision before/after the switch; camera
   position may change, but the player must not be replaced or teleported.
3. Repeat switching while moving, near a wall and beside a reachable marker. Observe clipping,
   visibility and collision behavior. Both views must use the same physical location/reach basis;
   a detached third-person camera must not grant additional interaction reach.
4. When equipment/context placeholders exist, repeat with carried/stowed bounds and compare their
   attachment and ownership across views. If those states are absent in 3.1, record them as pending
   and repeat at 3.4/later integration rather than inventing equipment gameplay for this check.
5. Record perceptual issues separately from identity/state errors: camera offsets, view obstruction
   or awkward framing may require iteration even if the actor identity test passes.

**Expected outcome / evidence:** one actor and collision body persist; basic traversal is usable in
both views without a camera change bypassing physical limits. Retain identity/transform evidence,
measured fixture configuration and observed movement/switching records. Unavailable equipment or
control-context states remain untested, not implicitly passed.

**Recovery:** revise only affected body/camera/attachment assumptions and rerun the fixture before
fitting tight rooms. Preserve established scale; seek review for a changed E allocation rather than
silently shortening the player or disabling collision. Actual input permissions repeat in VS1-I01.

## VS1-G02

**Supported hull, boarding path and interior round trip**

**Owning checkpoints:** 3.2 and 3.4; actual entry repeat 5.2 and route interaction repeat 5.4.

**Starting state:** G01 player fixture and authorized hull/room/route proxies using the accepted
[Phase 1.2 closeout route](../phase-1-2-closeout-proposal.md#concrete-route-proposal-and-remaining-correspondence).
Use the supported dormant ship pose and separate source-derived landmarks from invented connections.

### Planned Steps

1. Compare the oriented exterior proxy against the 72 × 21 × 16 m overall envelope and source-shaped
   silhouette. Inspect room sections inside it; the envelope is not a rectangular usable interior.
   Record provisional local bands and support/entry positions from the selected layout.
2. Traverse facility entry/light-control approach to the exterior ship opening with the same body,
   checking support feet/struts, boarding height, carried bounds and the readable reveal viewpoint.
   In the graybox, represent planned low-gravity/handhold constraints explicitly; do not claim the
   real boot/jump/hatch workflow has passed before its implementation.
3. Follow the selected lower entrance, lower connector and H03 ascent into the main passage, then
   reach the cockpit. Keep the boarding hatch, H03, cockpit emergency access and unresolved airlock
   identities distinct. Preserve the separate apparatus cavity below the forward cockpit.
4. Walk cockpit → central corridor → engineering → cockpit in both
   views. Check openings, headroom, corners and return paths with the actual body/collision, recording
   any temporary equipment/occupant proxies used. Closed future branches must not conceal an active
   route conflict or imply verified rooms beyond them. Include an adjustable closed kitchen/dining
   side-hatch placeholder under the [2026-10-25 route amendment](../phase-1-2-corridor-route-amendment.md);
   entering a kitchen/dining shell is not required. Its room placement and fit remain deferred.
5. Repeat affected route portions with the G03 endpoint/reservation proxies present. If a debug/test
   placement establishes a future machinery state, label it as setup rather than a successful startup.

**Expected outcome / evidence:** a connected, usable round trip within the supported ship/hangar
proposal, with traceable S/H references and E connections. Retain measured plans/sections, traversal
observations, exact setup limitations and relevant MC-05/06/08 results. Static route success does not
certify operating hatch motion, gravity transitions, seal checks or finished reveal lighting.

**Recovery:** revise the smallest affected E room/connector/support allocation and repeat its route
and dependent clearance checks. Do not enlarge the canonical exterior, merge hatch identities or
disable collision to hide failures. Structural contradictions return to the Phase 1.2 layout review.

## VS1-G03

**Occupied endpoints, motion envelopes and future reservations**

**Owning checkpoints:** 3.3/3.4; repeat with actual mechanisms in 6.4.

**Starting state:** G01 body and G02 connected route, recorded occupant/equipment proxies, mechanism
dimensions and endpoint/sweep representations. Use the existing
[MC demonstration plan](../phase-1-2-closeout-proposal.md#mc-demonstration-plan) and
[reservation audit](../phase-1-2-reservation-audit.md). Future hardware remains reservation-only.

### Planned Steps

1. Place stowed/deployed seat and apparatus proxies together, including occupant, source-shaped cap,
   covers, station controls, trunk/lid, doorway and canopy. Inspect intermediate/swept regions rather
   than only endpoints; check below-floor occupant/platform/cylinder space in hull sections.
2. Verify cockpit circulation and camera/body clearance in both views at the relevant endpoints.
   Retain the demo trunk's player-nonblocking exception, but still check its visible relationship to
   apparatus, seat and occupant paths. The exception does not apply to hull or machinery collision.
3. Inspect engineering with closed, one-extended and all-four-extended units. For each upper/lower
   control, record the operator standing surface, target position, reach, turning/pulling/pushing
   accommodation and return/escape path. Include the actual platform and fixed central equipment.
   A reachable lower unit does not establish all-four reach or reverse-travel clearance.
4. Inspect H03 ascent/carried bounds, exterior boarding against root reservations, and rail/carrier
   regions against canopy/headroom. Review Shooter, aft/support and possible furniture reservations
   only to their agreed extent; do not add their deployment/gameplay to prove a reservation.
5. Record each applicable MC check as demonstrated proxy fit, failed, not executed or reservation-only
   with explicit unknowns. Keep RA limitations attached. Repeat G02 routes affected by machinery or
   equipment occupancy; distinguish all-four endpoints from actual playable extension behavior.

**Expected outcome / evidence:** required occupied proxy endpoints and reserved sweeps coexist with
local access and circulation, or failures are explicit. Record dimensions, actual collision/reach
observations, endpoint/intermediate sections and links to MC evidence. Phase 3 acceptance can cover
the demonstrated graybox and scoped future reservations only; actual motion/collision integration
requires the later VS1-M01–M03/6.4 repeats. Unknown future geometry is not a passed deployment test.

**Recovery:** preserve the working route; revise only affected profiles, placements or E allocations.
Rerun dependent MC checks plus G01/G02 portions. Inaccessible upper controls require review of the
bank/platform proposal, not remote completion, hidden occupant scaling or an unapproved extra catwalk.
Do not treat rail-free ceilings, zero-size stowed hardware or another deck as automatic solutions.

## Completion Boundary

These procedures are accepted for planning on 2026-10-23. Phase 3 acceptance requires observed evidence and its
existing exit review; procedure publication does not grant it. Later machinery, input/state, gravity,
lighting and packaged integration checks remain necessary at their own checkpoints. No modeling,
Unreal/Blender launch, asset import or test execution occurs in this documentation increment.
