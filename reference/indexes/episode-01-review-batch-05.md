# Episode 1 initial survey — batch 05

Status: implemented initial annotations for locators 289–354, 2026-10-27; accepted by the maintainer on 2026-10-28, including the tentative code-reading follow-up.
Phase 3.2A remains unstarted.

## Evidence and timing scope

All three contact sheets (289–312, 313–336, 337–354) were visually inspected. Full cached images
293, 299, 301, 302, 311, 312, 313, 314, 316, 321, 325, 326, 327, 332, 337, 342, 346, 350,
351 and 354 were also inspected. Initial annotations do not establish measured geometry, complete
combat choreography, a magic system or a transport-case life-support specification.

The alignment input validator checked the pinned Episode 1 CBM video, English ASS stream 4,
gallery subset and source identities. Eight bounded windows requested 39 seconds and produced
156 temporary frames. A preview of four selected frames per window was visually inspected;
not every decoded frame was inspected. Commands, source hashes, frame PTS/hashes and selected
inspection points are retained in the [decode provenance](episode-01-review-batch-05-frames.json).
Source media were read only. Disposable frames, logs and previews are removed after hash checks;
contact sheets, gallery originals and the registered supplement remain for episode completion.

Locators 289–330 fall within the existing [400,1241) web-label mapping: local = web - 1.388 s.
This supports navigation, not new exact gallery/subtitle associations. **331–354 are outside
validated mapping coverage.** Farm, barn, code and reveal windows were selected from ordered
dialogue/narrative context without extrapolating the mapping or assigning gallery estimates.
No anchors, mappings, original locators, subtitles or source-video records changed.

The remaining ordered dialogue cues 222–278 were consulted, with ending/preview cues 279–293
kept outside this gallery's story coverage. Relevant local intervals and evidence limits:

- 222–231, 1098.64–1124.73: pirates demand Hilda, eye-covering instruction, smoke escape and pursuit.
- 232–238, 1146.99–1170.76: Rachel cover identity, Hilda name and the continuing bodyguard requirement.
  The bounded wig window independently shows removal of the blonde hairpiece.
- 239–246, 1171.64–1197.02: incoming pursuer, Tao-magic identification, taking the wheel,
  short-barrel-blaster request and evasive action. The platform is visibly composed of linked
  foot soldiers, not a spacecraft or XGP grappler. These samples do not resolve a complete spell.
- 247–254, 1200.47–1229.46: further attacks, request for number 3, limited ammunition dialogue,
  caster recognition and firing. Number 3 is dialogue context; the red cartridge's printed number
  is not independently readable here. Do not assign a general ammunition count from the kit still.
- 255–259, 1240.41–1254.29: post-blast reaction and farm/job completion conversation.
- 260–268, 1261.07–1289.56: farm confrontation, trunk retrieval order, Gene's return and
  explanation involving Jim's PDA. A prone Gene still alone does not prove death or the stopping
  material. Cached CTX-000022 provides the separately attributed PDA-survival summary.
- 269–278, 1289.99–1319.16: electronic lock, demand for the code, unlock success and discovery.
  The ASS spells the code VSDO2C (letter O); the display and cached Hilda article are provisionally
  transcribed VSD02C (zero). Locator 350 retains NEEDS_RECHECK rather than normalizing the variants.

**Maintainer follow-up — 2026-10-28:** VSDO2C (letter O) is the tentative preferred reading.
The reported spoken delivery is "oh two C," and the displayed character has no apparent slash.
The maintainer explicitly remains uncertain. Spoken "oh" can represent zero, and an unslashed
glyph does not establish letter O. Both source variants and the existing NEEDS_RECHECK remain;
this follow-up does not independently verify the audio or settle the exact code.

## Secondary context and identity boundaries

Cached Outlaw World page 2092 revision 9407 (CTXSRC-000008), SECTION:0003/BLOCK:0001, and
Hilda page 2048 revision 9440 (CTXSRC-000002), SECTION:0004/BLOCK:0003, were reread.
Existing CTX-000020, CTX-000022 and CTX-000024 are reused through 30 added context links;
no new secondary assertion or source capture was needed. Secondary summaries do not replace
the primary visible descriptions or extend timing coverage. Episode 2 resuscitation and arm
repair details in the same biography paragraph are not imported into Episode 1.

Two descriptive retrieval subjects are registered: gene_modular_blaster for the purple
revolver-style weapon/component kit, and melfina_transport_case for the reinforced trunk.
The blaster is distinct from the gold caster. The trunk is distinct from the XGP pod/apparatus
and Hilda's laptop. These IDs establish continuity metadata, not manufacturer, caliber,
engineering design or common internal mechanisms. Existing pirate-leader candidate names
remain separate from the maintained role IDs; no identity merge occurred.

## Findings and revisit priorities

- 289–302: leader costumes, Guugaku's neck bolts, foot-soldier arrangement/claws, smoke escape
  and hand gestures. Locator 293 does not visibly expose a grenade; that action is secondary
  sequence context. Long mechanical fingers in 301 are not assigned paper talismans.
- 303–310: red-car escape, blonde wig removal and Hilda's dark hair/forehead-band reveal.
- 311–324: mirror pursuit view, Hilda driving, modular purple blaster kit, Guugaku's linked
  foot-soldier flying support, long blade and energy effects. Exact flight/spell mechanics,
  component assembly and projectile trajectories remain unverified.
- 325–330: cropped coat pocket/holster, red cartridge at open gold caster breech, aiming view
  with illuminated barrel vents and blast imagery. 326–327 are high-value follow-up references
  alongside SET-136; dimensions, cartridge marking and measured yield remain open.
- 331–345: pirate reaction, wheat-field farm and silos, apparent shooting aftermath, Jim at
  gunpoint, barn rafters/boxes/shadows and Gene's return with the purple blaster.
- 346–354: concealed metal trunk, code-screen controls/connector, partial lid opening, vapor,
  reactions and Melfina curled in the lined case. 346/350/351/354 are valuable transport-case
  references; fluid composition, life support, full hinge travel and later pod equivalence are
  not established. The case-code O/0 reading is the only new explicit recheck.

## Result and retention

66 new INITIAL_REVIEW_COMPLETE rows: 65 SCREENED and one NEEDS_RECHECK. Episode 1 now has
**354/354 sampled gallery records surveyed**, 346 SCREENED and eight NEEDS_RECHECK;
296 INITIAL_REVIEW_COMPLETE and 58 prior targeted PARTIAL records. The seven earlier tentative
launch-site flags remain. All 9,204 gallery rows and ten supplement records are preserved;
no earlier annotations or other episodes changed. No manual supplement was added.

Survey coverage is complete for this sampled inventory, not every shot of the episode.
Corrections and the accepted Episode 1 RAR integrity/recovery/prune step remain pending.
Gallery originals, contact sheets and EP-01-MAN-001 are retained until then. No next episode,
full-show alignment, modeling, gameplay or Phase 3.2A work is authorized by this batch.

## Validation and cleanup

Category validation passed for all 9,204 gallery records and ten supplements; context validation
passed with 29 subjects, 13 captured sources, 37 context records and 210 links. Exactly the 66
previously unreviewed gallery rows were edited in this batch; earlier and other-episode row
objects were compared and preserved. Batch 04's pending changes remain intact.

ImportExcel refreshed both generated workbooks with maintained CSV equality checks. Category
checks covered 432,588 gallery cells, 9,204 image links, 510 supplemental cells and 1,029 alignment
cells; context checks covered 3,191 cells and 504 links. Alignment-media verification passed
without changing the existing 25 anchors, two mapping records or their coverage. The saved case
access/lid annotation range was rendered and visually inspected.

All 156 temporary frame hashes were rechecked against retained provenance before deleting the
owned temporary directory, including helper scripts, decode logs and previews: 100,519,668 bytes
reclaimed. Directory absence and provenance retention were verified. Gallery and supplemental
originals remain for corrections and the later episode archive step. Git whitespace checks passed.
This batch was accepted with the Episode 1 survey/retention checkpoint on 2026-10-28. The later
[retention record](episode-01-retention-checkpoint.md) supersedes the pre-archive availability
state above; the unresolved rechecks and evidence limits remain unchanged.
