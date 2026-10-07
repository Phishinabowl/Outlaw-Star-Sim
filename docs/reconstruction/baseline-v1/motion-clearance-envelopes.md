# Baseline v1 — motion and clearance envelopes

Companion to the [spatial map](spatial-constraint-map.md), [operational vocabulary](operational-state-baseline.md) and [slice contract](vertical-slice-1.md). This is a list of space reservations, not modeled geometry, exact millimetres or an approved animation rig. Apply the [canon policy](../../canon-policy.md): evidence-supported motion is separate from D required clearance and E chosen margins/mechanisms.

## Reservation register

Sources resolve through the [interior review](../../../reference/indexes/settei-interior-review.md), [follow-up](../../../reference/indexes/startup-open-items-followup.md), [startup comparison](../../../reference/indexes/startup-sequence-comparison.md), [EP-26 review](../../../reference/indexes/episode-26-platform-review.md) and [component matrix](../component-evidence-matrix.md). B remains a production candidate. Unless stated, no metric travel, timing or collision margin is measured.

| ID / assembly | Supported motion / states | Space that must stay available | Unknowns / implementation boundary |
|---|---|---|---|
| M01 — apparatus cap H01 | Opening in EP-04 A; open cap throughout EP-26 descent A; close stage in SET-027/086 B candidate | Cap opening sweep above floor and occupant approach; do not put a wall/console across it | Closure animation, exact hinge/path and interlocks unresolved. Reserve, do not invent sealing hardware. |
| M02 — occupant descent | Standing occupant lowers through shaft in EP-26 A; platform-stage explanation B candidate | Occupant/support corridor below floor, opening clear of seating and structures | Support hardware, full stroke and cavity depth unknown. Do not derive depth from camera zoom. |
| M03 — cylinder rise | EP-04 rising cylinder A; deployed/stowed designs SET-022/028 B candidate | Vertical swept volume from floor to operating position; overhead space and coexistence with M02 | Full continuous choreography, overlap of platform/cylinder volumes, travel unmeasured. |
| M04 — lateral covers/shields | EP-04 10:33.508–10:35.009 withdrawal A; SET-027/086 B candidate | Left/right travel around front opening and raised cylinder | Exact endpoints, storage pockets and seals unknown; keep rear-shell views distinct from front closure. |
| M05 — seat/control cluster | Relative upward movement in EP-04/08 A; bridge drawings B candidate | Lift sweep of seat/console assembly, occupied head/limb space, access around raised/stowed states | Camera changes prevent metric stroke; no chosen actuator or rigid-body linkage. |
| M06 — seat-side grips/panels | SET-026 B candidate shows articulating/open control sections | Local panel/grip swing and operator reach at stations | Bus-door analogy is not actuator engineering. Full grappler-control rig is future work; reserve space in slice. |
| M07 — four engineering control cylinders | 2×2 closed bank and A all-four extended states; one manual band/handle/extension sequence EP-04 | Closed housings, frontward extension sweep of every unit, control-panel reach and continued operator route | Cylinder stroke, plate rotation angle, wrap disposal and individual operation of three units unknown. Do not treat whole exterior engines as sliding here. |
| M08 — maintenance robot rail | SET-028/044/046 B candidate; blue robot passage/bridge shot EP-04 A | Guide rail corridor, robot body sweep and station/doorway approach overhead | Complete rail route/robot variants unreviewed. Slice may reserve it without mobile robot AI. |
| M09 — entry/airlock/emergency hatches | Separate H02–H06 records; SET-047 cover-down B candidate and inward-slide provisional reading; EP-04 inside/outside A | Each opening, panel/door movement and occupant standing/approach space; H03 needs floor access volume | Do not merge hatch identities. Exact trajectory and pressure locks unknown. Only chosen entry operates in slice; other openings retain reservations. |
| M10 — grappler roots and arms | Exterior joint/mount/deployment candidates SET-024/025/083/100/104; airlock-relative SET-126 note | Stowed roots, deployment sweep and airlock opening exclusion zone | Full swept volume and accessible root compartment unknown. Future reservation only; no combat or arm deployment in slice. |
| M11 — Assault Tube/Shooter | SET-045 ladder; SET-125 telescoping/capsule/hatch/seat stages B candidate, SET-192 comparison pending | Stowed nested envelope, outward deployment line, capsule/hatch movement, ladder/access approach | Full hull attachment, deployed length and ladder correspondence unresolved. Future reservation only, not an ordinary extra corridor. |
| M12 — aft screw / landing assembly | SET-032/098 folding/retracting/support stages B candidate; EP-11 aft activation effects A | Stowed/deployed mechanical sweep and support/ground approach | Fin transition mechanism, load path, ground height and propulsion relationship unfinished. Ship stays supported; no flight/landing implementation in slice. |
| M13 — convertible lounge furniture | Final SET-088/089 B candidate, distinct from preliminary SET-043 | Floor-panel conversion and table/bed emergence/access | Dimensions/mechanisms unresolved. Out-of-slice reservation; no furniture animation requirement. |

Service/access volumes are D necessities for the chosen physically operable arrangement, not measured canonical clearances. Standing reach, body size and comfortable player camera margins need later E/F choices. No fixed corridor width, clearance height, extension length or hatch dimension is specified here.

## Interference checks for a later blockout

| Check | Volumes to evaluate together | Pass condition |
|---|---|---|
| MC-01 | M01–M05, bridge doorway and H02 | Cap, descent, cylinder, covers and seating can reach their supported states without a wall, ceiling or neighboring station blocking them. |
| MC-02 | M02/M03 and forward hull/internal floors | Below-floor cavity fits the actual hull; it is not achieved by inventing a deck or shrinking the occupant without a recorded compromise. |
| MC-03 | M07 all four extended, engineering platform/route/M08 | All cylinders can be deployed together while operators can reach required controls and leave the room. |
| MC-04 | M08 and M05/M09/overhead structures | Reserved rail corridor avoids seat/hatch sweep and traversable head space. |
| MC-05 | H03 floor access and ordinary passage circulation | Opening remains accessible without an unrelated apparatus occupying its route. |
| MC-06 | M09/M10 at airlock | Airlock access and future arm-root sweeps do not share an unexamined solid obstruction. |
| MC-07 | M11 and ladder/hull/stowed equipment | Access and nested/deployed Shooter reservations fit without assuming an unverified complete route. |
| MC-08 | M12 and static hangar supports | Supported dormant ship and aft mechanism reservations coexist; do not animate a landing fold as a proven jump-transition fold. |

These are future review conditions, not assertions that geometry already passes. V1 slice requires moving M01–M05/M07 and its selected M09 entry, with other mechanisms reserved or represented statically as stated in the [slice contract](vertical-slice-1.md). Whether M06 must move for station access is resolved during the concrete blockout proposal; no full control rig is implied.

## Deliverable at the graybox gate

For each implemented movement, provide a stowed/deployed proxy and a swept-volume representation, operator-access path, supporting evidence, and any provisional E dimensions/F timings. Demonstrate relevant MC checks before detailed art. A reserve volume can remain unresolved in shape/size now; a future wall placement cannot assume it is zero.
