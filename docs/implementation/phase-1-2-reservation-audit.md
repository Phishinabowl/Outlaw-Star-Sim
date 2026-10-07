# Phase 1.2 — Machinery And Access Reservation Audit

Planning audit, 2026-10-07. This checks [Layout A](phase-1-2-layout-proposal-a.md), the
[cockpit](phase-1-2-cockpit-motion-proposal.md) and
[engineering](phase-1-2-engineering-clearance-proposal.md) trials against remaining reservations.
Its constraints were accepted with the Phase 1.2 closeout on 2026-10-07; no modeled intersection, clearance pass or new mechanism
implementation is claimed. General room arrangement remains accepted; numerical fit remains pending.

Use Baseline v1's [M01–M13 / MC-01–MC-08 register](../reconstruction/baseline-v1/motion-clearance-envelopes.md)
and [S/H spatial records](../reconstruction/baseline-v1/spatial-constraint-map.md).
The [canon policy](../canon-policy.md) applies: drawings remain B production candidates;
necessary access is D, proposed allocation/margins are E, and demo behavior is F.

## Targeted Source Inspection

Re-inspected local scans SET-006, 024, 026, 032, 033, 045, 088, 104, 114, 125, 126 and 192.
Identifiers resolve through the [screening index](../../reference/indexes/settei-screening.csv),
[interior review](../../reference/indexes/settei-interior-review.md) and
[variant review](../../reference/indexes/settei-variant-review.md).
This was visual inspection of selected sheets, not a complete dimensional reconstruction or
new Japanese transcription pass. No episode extraction, audio review or source-media changes.

| Source | Observation relevant to this audit | Limit |
| --- | --- | --- |
| SET-026 | Pilot-side control panels/grips articulate outside the simplified seat footprint. | Exact swept path, reach and fixed neutral position remain unmeasured. |
| SET-033 / 114 | Rail-mounted maintenance robot includes body, carrier, extending neck/manipulators; a 350 cc can is drawn for comparison. SET-033 is marked first draft; SET-114 final. | Compact robot reference, not a human-sized guide. Can capacity is not a robot height; unspecified can dimensions cannot yield a metric envelope. Do not automatically import first-draft details into the final design. |
| SET-006 | Cockpit emergency floor access is distinct from the navigation apparatus opening. | Its complete below-floor escape path and exact placement in Layout A are unresolved. |
| SET-045 | Upper Assault Tube ladder/access and round passage floor access are separate features in the passage views. | Do not assume they share one vertical shaft or station. |
| SET-126; 024 / 104 | Airlock-relative drawing places grappler machinery at both sides; exterior designs show substantial articulated roots and stowed arm structures. | Root compartment boundaries and correspondence with the chosen rectangular boarding hatch remain unresolved. |
| SET-125 / 192 | Related Shooter drawings show nested telescoping hardware, occupant capsule, hatch and seat stages, with a dorsal hull attachment sketch. | Related views are not independent metric confirmation. Full attachment, length and passage-ladder connection remain unknown. |
| SET-032 | Landing/support poses and a separate aft folding assembly require external space. | Landing supports and aft screw are distinct parts of M12; load paths and their relation to propulsion are not established here. |
| SET-088 | Convertible furniture uses floor panels and emergence/access volume. | Lounge versus slice dining-room identity remains unresolved; no conversion dimensions measured. |

## Reservation Ledger

“Candidate conflict” means the current trial omits a volume or may overlap it. It does not mean
the proposed ship has been proven impossible. A protected region below is an E planning constraint,
not a measured solid box. Unknown envelope size must not be treated as zero.

| ID / affected records | Protected region and recommendation | Status / later check |
| --- | --- | --- |
| RA-01 — M06; M05 | Cockpit station-side strips: include panel/grip movement and operator reach before calling the nominal side aisles usable. Keep access around both sides of the seat group. | Candidate conflict: cockpit trial omits articulated hardware from its simple footprint. Resolve neutral pose and whether access requires movement in 3.3/3.4; recheck occupied seat states in 6.4. No full grappler-control rig required. |
| RA-02 — M08; MC-03/04 | Passage, cockpit and engineering overhead route: reserve rail **plus carrier/body/reach**, separate from traversable head space, seat lift, canopy and hatch sweep. Preserve service approach to the bank. | Route/profile pending. A thin rail line alone is insufficient. No mobile robot AI needed for the slice; later proxies must check the selected final robot design and local rail sections, rather than assume continuous routing everywhere. |
| RA-03 — H02; M09; MC-01 | Forward cockpit floor-access region: retain a visible closed cap and an unobstructed approach, separate from the rear apparatus cavity. Keep its unknown below-floor continuation available for reconciliation. | Exact coordinates/envelope pending. Do not fill that continuation with a new cargo room or claim an escape route is implemented. Check against seating/controls/cavity in 3.3/3.4. |
| RA-04 — H03; M09; MC-05 | Passage floor access near the bridge and proposed lower-route junction: retain opening, ladder/occupant approach and normal passage circulation. | Proposed 1.5 m diameter is E trial only. Distinguish floor access from upper Assault Tube ladder and cockpit emergency cap. Check carried trunk/computer and player ascent before accepting the junction in 3.2/3.4; actual entry repeat in 5.2. |
| RA-05 — H04/H05/H06; M09/M10; MC-06 | Lower entry and paired lateral root regions: reserve inside/outside boarding approach, door/panel sweep and grappler stowage/mount space together. | Candidate conflict: Layout A's 3 × 3 m entry box does not prove space is free of roots. Do not move the hatch or declare all H records identical merely to fit. Reconcile exterior cross-section and chosen hatch proxy in 3.2/3.4; arm deployment remains future reservation only. |
| RA-06 — M11; S04/S05; MC-07 | Dorsal machinery region and main-passage upper access: preserve nested hardware, capsule/hatch/seat space and a future outward deployment line. Keep the ladder's approach free. | Envelope/station extent unknown. Do not reserve only the exterior extended tube or certify the unused aft approach as free of its stowed body. A closed access representation is sufficient now; reconcile full hull attachment before fixing affected roof/bulkhead geometry in 3.4. No Shooter operation required. |
| RA-07 — M12; MC-08 | External supports, ground approach and aft machinery: preserve the supported dormant pose and future folding/sweep space. Treat Layout A's unallocated aft interval as unresolved structure/machinery, not an empty room. | Support feet/struts may affect the exterior jump, light-switch route and entry approach. Check the static supported pose in 3.2/3.4, separately from future screw/landing motion. Do not infer landing fold equals sub-ether transition. |
| RA-08 — M13; S15 | Minimal dining/common-area shell: if later identified with the lounge, protect floor-panel and furniture emergence space plus circulation. Keep floor services and fixed furniture provisional. | Identity pending. Do not create another full room solely to avoid the question. No moving furniture required; revisit affected floor allocation in 3.2/3.4 if the identity or layout changes. |
| RA-09 — future branches | At source-supported passage destinations, allow closed doors/hatches without claiming a complete cabin/cargo plan behind them. | Exact branch coordinates pending. Avoid invented named-room adjacency and do not use closed doors to conceal interference with the required route. Full rooms remain deferred. |
| RA-10 — carried/stowed equipment; M01–M05/M09 | Boarding/climb path, entering-right trunk stage and pilot workspace: reserve carried equipment, opened trunk/lid, occupant transfer and a real stowed computer/cable location. | Stow location remains unselected. Disconnect/close/stow before seat lift is agreed; do not leave equipment suspended in the seat sweep. Placed trunk's F player-nonblocking exception does not waive visible machinery, carried-equipment or hull fit. Check in 3.3/3.4 and repeat with actual mechanisms in 6.4. |

The initial station bands locate rooms for a trial; they do not locate every mechanism. In particular,
the lower entry band, dorsal Shooter machinery and exterior supports need cross-section/profile
reconciliation before affected walls or floors are fixed. No unsupported millimetre values were added
to make this audit look complete.

## Slice Work Versus Future Protection

- **Active slice fit:** M01–M05, all-four M07, selected operating entry M09, case/occupant/computer,
  player route and both camera views. Their motion and access must work, with explicit E/F choices.
- **Static/access fit now:** station-side controls in their selected access pose, protected rail/robot
  regions, H02 and upper access representations, exterior supported pose and required dining shell.
  M06 needs limited movement only if the chosen station access requires it.
- **Future reservation only:** grappler deployment/combat, Shooter operation, mobile maintenance
  robot behavior, aft/landing transitions and convertible furniture. Recording these does not add them
  to the playable slice or prove their complete future geometry fits.

## Validation And Iteration Ownership

This audit contributes the inventory/constraints part of the completed Phase 1.2 planning package.
The [accepted closeout](phase-1-2-closeout-proposal.md) specifies how MC-01–08 will be demonstrated,
which are active fit versus future reservation checks, and reconciles opening additions with
Baseline v1's slice contract. MC checks remain unexecuted. Actual geometry and occupied motion proof belong to authorized
Phase 3 and the integrated Phase 6 repeat.

Before accepting an affected graybox region, record source landmarks, proxy dimensions, relevant
swept/access volumes and the result. If a check fails, reopen the smallest affected E allocation:
local ceiling/profile, station position, lower route or support/entry approach. Recheck its dependent
MC cases and route; preserve accepted source observations and unrelated working regions. Do not
solve failure by silently shrinking occupants, merging hatch identities or applying the trunk's
nonblocking exception to ship machinery.

No new creative choice must be made just to record this audit. Computer storage and the local
rail/canopy/platform profiles remain concrete proposal work for the closeout; climb/stow input
behavior stays with Phase 1.3. The audit does not authorize that subphase or later implementation.
