# Episode 1 initial survey — batch 03

Status: implemented initial annotations for locators 145–216, 2026-10-27; uncommitted pending confirmation.
Phase 3.2A remains unstarted.

## Evidence and scope

All three retained contact sheets (145–168, 169–192, 193–216) were visually inspected. Full cached
images 145, 146, 147, 151, 154, 163, 164, 165, 170, 175, 176, 188, 195, 196, 208 and 215 were
also inspected. Individual annotations remain INITIAL_REVIEW_COMPLETE; this is not a measured
floorplan, typography transcription, combat-animation analysis or equipment implementation contract.

The pinned local Episode 1 CBM source and English ASS stream 4 were checked through the existing
alignment input-validation path. Source/subtitle SHA-256, stream basis, bounded commands, frame
PTS/hashes and inspection selections are retained in the [decode provenance](episode-01-review-batch-03-frames.json).
Eight windows requested 25 seconds and produced 100 frames. A preview containing four selected
frames per window was visually inspected. Decode frames, logs and preview are disposable and
pruned after hash verification; original media are immutable and unchanged.

Subtitle cues 117–163 were read for this batch; following cues were consulted only as context,
without annotating later gallery records. Relevant local cue intervals:

- 117–120, 606.25–617.15: pirates search for Hilda and discuss her arrival three days earlier.
- 121–131, 637.81–673.37: Gene and his companion discuss going into space, pirate hunting and
  his lack of a ship. Her proper name is not established by this passage.
- 132–146, 708.58–773.54: Jim calls Gene from bed, discusses the tractor job and reports last
  night's arriving pirate ship. This corroborates the arrival context without naming a guild.
- 147–154, 777.45–802.40: Starwind and Hawking business greeting, parts/bodyguard request,
  and caller introducing herself as Rachel.
- 155–163, 818.22–849.75: customer discussion, deposited money and expensive biological/organic/
  nanotech parts. Later lines extend beyond locator 216 and remain context only.

All batch web labels fall within the existing [400,1241) navigation mapping, local = web - 1.388 s.
Estimates guide scene retrieval; they do not establish an exact subtitle/frame pairing. No anchors,
mapping rows, original locators or media versions changed.

## Secondary associations

Cached Fandom Outlaw World page 2092 revision 9407 (CTXSRC-000008), SECTION:0003/BLOCK:0001,
supports CTX-000034 (Club Temptation/private room) and CTX-000035 (next-day headquarters/call).
Existing Hilda/Rachel association CTX-000020 supports the disguised caller/image links. The visible
club/company signs and local greeting separately support location identification. Secondary claims
remain SECONDARY_ONLY; no automatic primary promotion. No new remote article retrieval was needed.
The Hilda biography's inferred foot-soldier deaths and later Episode 2 material are not adopted.

## Findings and research priorities

- 145–150: three pirate leaders, recurring foot-soldier armor and landed-ship ramp/supports.
  Existing provisional leader IDs remain; proper-name candidates are not silently merged.
- 151–169: Club Temptation exterior and private room, broad window, furniture, Gene's star mark,
  drink can and unnamed companion. She is not assigned to Iris or Hilda. 164 dissolves into 165's
  bright star-filled sky band; no explosion, flashback or astronomical classification is inferred.
- 170: dark armored foot-soldier alley sample. Bounded frames show movement through the alley;
  they do not establish the complete encounter, opponent identity or a verified kill.
- 171–175: day transition, dense city panorama and weathered Starwind & Hawking storefront.
  Most non-Latin signs remain untranslated; exact urban geography is not established.
- 176–195: high-value future HQ references. Loft, railing, sleeping area, kitchen/workbench,
  storage, sink, cookware, table and seating are visible from several angles. Shared-space
  relationships are observations, not measured clearance or an accepted build layout. Preserve
  the early Sentinel location separately from later Heifong premises. Food recipe is unverified.
- 196–203: wall telephone with hinged display, physical controls, wired handset and Rachel call.
  Different caller/receiver backgrounds do not establish the caller's room location.
- 204–207: mid-episode EYECATCH logo/emblem sequence, distinct from end-card references.
  Sampled lettering states do not establish complete motion, durations or synchronized audio.
- 208: high-value search/profile UI. Visible RACHELL SWEET spelling is distinct from spoken Rachel
  and catalogue Rachel Sweet. On-screen birth date, age, height, weight, credentials and database
  labels are cover-profile content, not verified Hilda specifications. No working database design
  or translation of small non-Latin text is implied.
- 209–216: alternate yellow-green Gene coat and high views of the HQ table, electronics, rug,
  seating, worn floor and boxes; useful future home-base dressing and spatial references.

## Result and retention

72 new SCREENED / INITIAL_REVIEW_COMPLETE rows. Episode 1 now has 216 reviewed gallery records:
209 SCREENED, seven prior launch-site NEEDS_RECHECK; 158 INITIAL_REVIEW_COMPLETE, 58 PARTIAL;
138 remain unreviewed. No previous annotation or other episode record changed. No new manual
supplements were created. Contact sheets, cached gallery originals and EP-01-MAN-001 remain
under the episode-completion archive policy; this batch does not complete Episode 1 or trigger RAR cleanup.

## Validation and cleanup

The category validator passed for all 9,204 gallery records and ten supplements. The context
validator passed with 26 subjects, 13 captured sources and 35 context records. ImportExcel
refreshed both generated workbooks without changing maintained CSVs: 432,588 gallery cells,
9,204 gallery links, 510 supplemental cells and 1,029 alignment cells checked; context view
2,692 cells and 406 links checked. Saved HQ and profile ranges were rendered and visually
inspected. Alignment-media verification passed within the unchanged mapping contract.

All 100 decoded-frame hashes were rechecked against retained provenance before deleting the
owned temporary batch directory, including helper scripts, logs and previews. Original gallery
images, contact sheets, manual supplements and source media remain. Git diff whitespace checks
passed. Changes remain uncommitted pending confirmation.
