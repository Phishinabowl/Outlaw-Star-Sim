# Episode 1 initial survey — batch 04

Status: implemented initial annotations for locators 217–288, 2026-10-27; accepted by the maintainer on 2026-10-28.
Phase 3.2A remains unstarted.

## Evidence and timing scope

All three contact sheets (217–240, 241–264, 265–288) were visually inspected. Full cached images
223, 224, 225, 226, 232, 250, 252, 253, 257, 258, 261, 265, 269, 270, 273, 274, 275, 276,
285 and 288 were also inspected. These initial annotations do not constitute a measured vehicle
model, full combat choreography, control translation or engineering repair specification.

The existing alignment input validator checked the pinned Episode 1 CBM video, English ASS stream 4,
gallery subset and source identities. Seven bounded windows requested 33 seconds and produced
132 temporary frames; a four-frame-per-window preview was visually inspected. Source hashes,
commands, frame PTS/hashes and selected inspection points are retained in the [decode provenance](episode-01-review-batch-04-frames.json).
Not every decoded frame was visually inspected. Source media were read only. Temporary frames,
logs and previews are pruned after hash verification; gallery originals remain for episode completion.

Batch web labels fall within the existing [400,1241) mapping: local = web - 1.388 seconds.
This is navigation support, not a new exact gallery-to-subtitle association. No anchor, mapping,
original locator, subtitle or source-video record changed.

Subtitle cues 164–221 were read for this batch; following cues were consulted as context only.
No later gallery records were annotated. Relevant local intervals:

- 164–171, 850.69–874.31: customer ID discussion, Jim's entered data and Gene leaving the HQ.
- 172–175, 883.25–897.37: Iris/Clyde discuss bar customers and jealousy about Gene's new companion.
- 176–187, 897.44–937.47: bodyguard negotiation; quoted rate is 800 per day plus expenses.
  Rachel's claim to be working for her father remains cover-story dialogue, not verified biography.
- 188–195, 939.18–959.75: waiting for Jim and Rachel's claimed agri-plant destination 30 km
  northeast, in wheat fields. No map coordinates or actual destination geometry are established.
- 196–203, 964.37–995.87: foot-soldier confrontation, threat and Gene fighting back.
- 204–213, 1006.34–1028.23: Jim arrives late from the shop and the group prepares to leave.
- 214–215, 1039.24–1044.97: checking the car and treating it as a restored classic.
- 216–221, 1055.49–1078.55: driving conversation about the attack and directions.
  Hilda's later spoken name reveal begins beyond this batch and is not assigned to locator 288.

## Secondary context and identity boundaries

Cached Hilda page 2048 revision 9440 (CTXSRC-000002), SECTION:0004/BLOCK:0003, supplies two
concise secondary associations: CTX-000036 for the Clyde's Bar bodyguard agreement and CTX-000037
for foot soldiers attacking before Jim arrives in his car. Cached Outlaw World page 2092 revision
9407 (CTXSRC-000008), SECTION:0003, was also consulted. Both remain secondary context; later
farm, caster and Episode 2 material in the articles is not imported into these earlier shots.
No new remote retrieval was needed. Existing Iris, Clyde and Hilda/Rachel identities are retained.

starwind_hawking_car is an added descriptive continuity ID for the red open-top car used by
Gene and Jim. It does not establish make/model, legal ownership, exact wheel count, propulsion
type or a shared design with any spaceship. The context register uses EQUIPMENT for this
ground vehicle under its existing subject-type vocabulary; image categories use ships_vehicles.

## Findings and revisit priorities

- 217–224: HQ reverse/low views, loft/ceiling, Gene's full coat and Jim's blue hinged computer.
  Cue 169 supports entered information; the rear-facing device still does not expose its data UI.
- 225: stylized white burst/red motif between HQ departure and bar exterior. It is classified
  OTHER presentation; no physical shooter, target, weapon or in-world blast is assigned.
- 226–242: bar layout, Iris/Clyde interaction, Rachel's glasses removal, costume and stemware.
  Dialogue establishes the bodyguard terms but not a general game economy or contract mechanic.
- 243–249: dense street lighting, elevated bridges, alley staging and Rachel's shoulder bag.
  Exact route geography and most non-Latin signage remain unverified.
- 250–262: recurring foot-soldier claw weapons, faceplates, action poses and Gene's ordinary
  compact pistol. The visible gun is not labeled caster. Sampled flashes/poses do not establish
  the full fight, every hit outcome, ammunition count or a death state for 260's hunched soldier.
- 263–273: red-car arrival, Jim's outer jacket, rear-passenger position, Gene's pedal contact,
  failed departure/smoke and tools/loose parts during repair. No exact fault or repair steps inferred.
- 274–275: valuable physical dashboard controls, gold plate/key slot, adjacent knob, red controls
  and illuminated round instruments. Non-Latin labels, readings and complete operating sequence
  remain unverified; these are car references, not XGP controls.
- 276–284: road traffic, yellow background vehicle, car front, driver/passenger poses and elevated
  dark road/headlight imagery. No pursuit role is assigned to the yellow vehicle.
- 285–288: front-seat backs, instrument cluster, mirror, headlight glare and pirate roadblock.
  285's seat backs obscure occupants; it is not evidence that the car is empty or abandoned.
  Existing provisional pirate-leader identities remain; no silent proper-name merge.

## Result and retention

72 new SCREENED / INITIAL_REVIEW_COMPLETE rows. Episode 1 totals: 288 reviewed, 281 SCREENED,
seven prior launch-site NEEDS_RECHECK; 230 INITIAL_REVIEW_COMPLETE and 58 PARTIAL; 66 unreviewed.
No earlier annotations or other episode records changed, and no new manual supplements were created.
Contact sheets, gallery originals and EP-01-MAN-001 remain under the episode-completion RAR policy.
This batch does not complete Episode 1, start its archive cleanup or authorize Phase 3.2A.

## Validation and cleanup

Category validation passed for all 9,204 gallery records and ten supplements; context validation
passed with 27 subjects, 13 captured sources and 37 context records. ImportExcel refreshed both
generated views without changing the maintained CSVs. Saved checks covered 432,588 gallery cells,
9,204 gallery links, 510 supplemental cells and 1,029 alignment cells; context checks covered
2,907 cells and 444 links. The saved repair/dashboard range was rendered and visually inspected.
Alignment-media verification passed within the unchanged mapping contract.

All 132 decoded-frame hashes were rechecked before removing the owned temporary directory,
including scripts, logs and previews, reclaiming 102,275,049 bytes. Provenance, original gallery
images, contact sheets, manual supplement and source media remain. Git diff whitespace checks
passed. This batch was accepted with the Episode 1 survey/retention checkpoint on 2026-10-28.
