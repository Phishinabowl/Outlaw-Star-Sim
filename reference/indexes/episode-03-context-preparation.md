# Episode 3 — subtitle and website-context preparation

Status: prepared and accepted by the maintainer on 2026-10-28. This increment covers subtitle and selected
website context only. Episode-specific alignment and gallery annotations remain unstarted.
The [gallery preparation record](animehistory/README.md#episode-3-gallery-preparation--2026-10-28)
owns the 354 downloaded images and 15 contact sheets. No Phase 3.2A work is included.

## Pinned inputs and read scope

- Source: `_source_episodes/[CBM]_Outlaw_Star_-_03_-_Into_Burning_Space_[720p]_[3FF6E5E5].mkv`.
- Source bytes: 916,088,236; SHA-256
  `8434f039972a2086a77b7b9a6ff5f5bd60db4c783d0f24de8f6d5949d5bfdb98`.
- Video stream 0, time base 1/1000, media origin 0; 960×720; duration 1511.53 s.
- English ASS stream 4; existing local copy
  `reference/working/performance-subtitles/episode-03.ass`.
- Subtitle SHA-256 `c0eb3460f3f9e8350831043d87406f12e9f5e14efec7b472d6e29a1a1cf50ea2`
  matches the [coverage register](performance-subtitle-coverage.json). Source size, track and
  first three subtitle-packet starts passed the alignment tool's read-only input inspection.
  Packet starts 1.55, 4.59 and 7.86 s match the ASS cues. This bounded check does not verify
  every subtitle packet, spoken line or translation. No video frames were decoded.

All 372 ordered Dialogue events were read: 1–17 introductory narration; 18–33 opening lyrics;
34–356 story dialogue; 357–363 ending lyrics; 364–372 Episode 4 preview. Empty Name fields do
not identify speakers. These are translated English subtitles, not verified Japanese dialogue
or an English-dub transcript. Full subtitle text remains ignored/local-only.

## Dialogue navigation notes

Intervals below use the pinned local release only. They are not AnimeHistory gallery timestamps.
Episode 1 or 2 offsets must not be reused. No Episode 3 timing mapping was created or accepted.

| Cues | Local interval | Useful context and limits |
| --- | --- | --- |
| 34–59 | 02:40.13–04:32.26 | Paint-bullet fight and interrogation naming MacDougall. Text alone does not identify a particular brother or the mechanical opponent's operator. |
| 60–76 | 04:34.81–05:28.42 | Departure preparations, Swanzo, the attack and Leyline discussion. Reported treasure context is not verified cosmology. |
| 77–97 | 05:28.93–06:24.25 | Horus resupply, engines green, and less than 50 parsecs until recommended sub-ether-drive overhaul. This is maintenance advice, not remaining fuel range or a guaranteed failure distance. |
| 98–139 | 06:48.64–09:19.18 | Five class-C grappler pursuers, gunner and auxiliary-control assignments, approach-lane constraints, anti-laser defenses and 482-second belt-clearance report. No universal docking or measured acceleration specification follows. |
| 140–178 | 09:28.80–11:16.77 | Orta Honehone broadcast, Aisha's ambassador identification and collision-course confrontation. The three-degree port and ten-second starboard-thruster orders concern the Ctarl ship, not Horus or the XGP. |
| 179–206 | 11:31.12–13:19.53 | Arrest/pursuit aftermath, Horus's belt-clearance countdown, acceleration warning and Aisha's firing order. Exact victims and combat outcomes require scene review rather than synopsis inference. |
| 207–224 | 13:23.24–14:47.75 | Small-system rendezvous plan and three further jumps; next drive wait stated as 2 h 10 min. Route/occasion-specific dialogue does not establish a universal cooldown. |
| 225–247 | 14:47.89–15:48.07 | Leyline treasure rumor and MacDougall mercenary reputation. Quarters mentioned in dialogue do not establish ship layout. |
| 248–273 | 16:00.86–17:42.46 | Moon rendezvous, calls to Marx/O'Malley, Leprechaun/Purgatory wreckage and pirate encounter. Exact wreck, speaker and ship identifications await visual review. |
| 274–303 | 17:45.70–19:57.89 | Hilda's reaction, Gene taking the gunner chair, lasers/missiles and starboard contact. A no-damage report does not rule out a tracking device or other later consequence. |
| 304–318 | 19:58.10–20:39.19 | Farfallas named about 40 light-years away; hidden ship and Melfina conversation. Distance dialogue is not a measured transit time or speed. |
| 319–344 | 20:49.21–22:12.99 | Pursuit continues; Aisha's CommCube message is a recording, followed by demotion and orders to remain on Blue Heaven. Do not mistake recorded messaging for a live conversation. |
| 345–356 | 22:24.74–22:56.40 | Hot stellar approach and hidden ship described as combining pirate ideas and Space Forces technology. No exact temperature, construction dimensions or operating state is inferred. |

The Episode 4 preview is retained as a boundary, not treated as Episode 3 story footage.

## Selected website context

The cached AnimeHistory hub's EPISODE:03/BLOCK:0001 synopsis was read, reusing CTXSRC-000004.
Selected Hilda prose was checked for continuity boundaries; no existing Episode 2 assertion was
rewritten. Four selected Fandom articles were captured through the established anonymous API:

| Source | Article | Page / revision | Reviewed selection |
| --- | --- | --- | --- |
| CTXSRC-000020 | Into Burning Space | 2120 / 9054 | Episode summary: departure, Aisha encounter, failed rendezvous and onward course. |
| CTXSRC-000021 | Aisha Clan-Clan | 2036 / 9510 | Episode 3 portion of Blue Heaven Incident and selected appearance prose. The same biography section continues into Episode 5; those later events are excluded. |
| CTXSRC-000022 | Ctarl-Ctarl | 2689 / 9170 | Introduction identifying the humanoid species only; biology, powers and broader history are not adopted. |
| CTXSRC-000023 | Orta-Honehone | 3504 / 9337 | Introductory ship/commander relationship; later command changes referenced to Episode 24 are excluded. |

Three captures are PARTIAL because unresolved templates remain; Ctarl-Ctarl is COMPLETE within
parser scope. These labels describe parsing, not factual verification. Selected readable prose,
revision links, hashes, attribution, licensing and warnings remain available in the local cache
and maintained source register. No full articles are copied into maintained tables.

The initial Aisha Clanclan and Orta Honehone lookups returned NOT_FOUND; successful titles are
Aisha Clan-Clan and Orta-Honehone. Failed attempts remain recorded locally without fabricated
source rows. Farfallas in the local English subtitles/Fandom and Farfallus in AnimeHistory remain
lookup variants, with original Japanese spelling unverified.

CTX-000051–000059 add nine SOURCE_CHECKED / SECONDARY_ONLY assertions and 28 typed links.
Four subject rows register Aisha, Orta-Honehone, Ctarl-Ctarl and Farfallas; the existing image
vocabulary's aisha_clanclan ID is reused. Catalogue identities do not establish image matches.
No CONTEXT_FOR_IMAGE links or primary-evidence promotions are added during preparation.

## Validation and next scope

Context validation passed with 39 subjects, 23 source versions, 59 assertions and 610 links.
All 20 Fandom and four AnimeHistory cached snapshots passed verification. Category validation
passed across all 9,204 rows. Category, supplement, alignment-anchor and alignment-mapping CSV
hashes match their pre-preparation baseline; all earlier 35 subjects, 19 sources, 50 assertions
and 582 links remain unchanged.

The ImportExcel context workbook refreshed successfully: five sheets, 7,557 verified cells,
1,365 verified links and authored data unchanged. Rendered selections of the new Context,
Subjects, Sources and Links rows were visually checked for readable text and visible statuses.
This does not claim a fresh native Excel/Office Viewer test. Cited website snapshots and gallery
media remain local; disposable authoring/preview helpers are removed after validation.

The next separate step is Episode 3 alignment before substantive timed image/subtitle review.
All 354 Episode 3 image rows remain UNREVIEWED / NOT_REVIEWED. This preparation does not advance
the all-episode survey gate or authorize Phase 3.2A.
