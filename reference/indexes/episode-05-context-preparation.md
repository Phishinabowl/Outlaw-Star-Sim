# Episode 5 — subtitle and website-context preparation

Status: prepared, verified and accepted by the maintainer on 2026-10-30 (America/New_York).
This increment covers full subtitle reading and selected website context. Alignment was unstarted
at this preparation checkpoint; the subsequent [alignment record](episode-05-alignment-review.md)
owns its accepted results. Gallery annotation and Phase 3.2A remain unstarted.

## Gallery preparation

The preceding authorized download prepared all 354 gallery images, IDs 848189–848542, with
web labels 00:01:43–00:22:58. All images decoded and matched their recorded sizes and SHA-256s.
The 15 contact sheets have verified hashes, dimensions of 1600×2056 and exact chronological
ID/time/image-hash correspondence with the locator CSV. The final sheet contains 18 images.
First, middle and final layouts were visually inspected for readable labels and image placement.
This is preparation verification, not an annotated image survey.

Gallery originals occupy 62,036,965 bytes under `reference/cache/animehistory-review/EP-05/`;
the sheet PNGs occupy 52,773,132 bytes under
`reference/contact-sheets/animehistory-review/EP-05/`. Generated manifests and media remain local-only.
No Episode 5 RAR has been created; normal archive-and-prune follows the completed episode review.

## Pinned inputs and read scope

- Source: `_source_episodes/[CBM]_Outlaw_Star_-_05_-_The_Beast_Girl,_Ready_to_Pounce_[720p]_[CA71B58C].mkv`.
- Source bytes: 778,944,264; SHA-256
  `4efd642c052d5f55d07100eac3c3d25c65e9d73521000f3dc559067e4dbb2cfe`.
- Video stream 0, H.264, 960×720, time base 1/1000, media origin 0; duration 1502.826 s.
- English ASS stream 4, title English Subtitles; existing copy
  `reference/working/performance-subtitles/episode-05.ass`.
- Subtitle SHA-256 `82155c3163a03b4cd70f788c00fc2eddcfad9404aff1126672f7415176659fb2`
  matches the [coverage register](performance-subtitle-coverage.json). Source size and stream
  metadata passed read-only inspection; source size/modification signature was unchanged afterward.
- The first three FFprobe subtitle-packet starts, 0.98, 4.28 and 7.82 s, match the ASS events.
  This bounded comparison does not verify every packet, spoken line or translation. No video
  frames were decoded and no alignment runs were created.

All 379 ordered Dialogue events were read: 1–13 introductory Aisha narration; 14–29 opening
lyrics; 30–366 story dialogue; 367–373 ending lyrics; 374–379 Episode 6 preview. Empty Name
fields do not identify speakers. These are translated English subtitles, not a verified
English-dub transcript or original-Japanese transcription. Full text remains local-only.

## Local subtitle navigation notes

Intervals below belong to the pinned local release. They are not corrected AnimeHistory times.
No earlier episode's offset is reused, and no timed image/subtitle associations are made here.

| Cues | Local interval | Context and limits |
| --- | --- | --- |
| 1–13 | 00:00.98–00:54.18 | Aisha's education, status and assignment backstory. Narration precedes the opening and is not present-day Blue Heaven action. |
| 30–41 | 02:30.02–02:57.14 | Mikey contacts Swanzo about docking clearance; arriving ship is explicitly not Horus and Hilda is absent. Named conversation does not independently match every face/display. |
| 42–65 | 03:05.99–04:04.87 | Hilda's death, Gene's uncertainty, missing registration and paint, and Swanzo's agreement. Registration discussion is not a universal legal or port-access specification. |
| 66–77 | 04:05.15–04:38.07 | Missing supplies, weapons and ammunition; Swanzo limits repayment to registration/paint and says grappler weapons are unavailable locally. Do not describe this visit as complete combat outfitting. |
| 78–105 | 04:40.02–06:01.49 | Swanzo's five-year Hilda backstory, Ban versus Kei Pirates, limited MacDougall knowledge, Ctarl inquiry and hull-color selection. Earlier rumors and present knowledge remain distinct; dialogue alone does not establish the final paint pattern. |
| 106–133 | 06:12.21–07:41.93 | Grief, Melfina's missing memory, Gene's space anxiety and the Physical Navigation System explanation. Subjective pilot experience does not specify camera placement, sensors, control latency or complete navigation architecture. |
| 134–179 | 07:45.04–09:41.35 | Aisha identifies herself, demands Hilda and Leyline information, then pursues the crew. Gene says he does not know the coordinates; no actual coordinates are supplied. |
| 180–207 | 09:49.06–11:52.87 | Fight, attempted beast-power use, moon-phase statements, escape and Jim's caster-shell errand. Treat moon comments as scene dialogue pending visual assessment, not a complete universal transformation rule. |
| 208–243 | 12:12.20–14:57.66 | Gene's difficulty, artificial flowers, Melfina's questions about her creation and Gene's promise to find her past. The android description does not reveal her creator or full physiology; the flowers do not establish the room's location aboard a ship. |
| 244–257 | 14:58.47–16:12.10 | Radio rendezvous, renewed Aisha confrontation, half-power boast and calorie exhaustion. No measured durability, force, energy budget or successful transformation follows from dialogue alone. |
| 258–280 | 16:26.39–17:46.86 | Resident Officer status, lack of imperial pay, meal and reconciliation attempt. Food quantity and appetite are scene context, not a dietary specification. |
| 281–309 | 17:55.51–19:35.30 | Renewed arrest demand, Jim's number-12 shell and Gene leaving the bill with Aisha. Shell number is a translated identifier; exact effect and loading/shot timing require image review. Immortality is a character's boast, not verified invulnerability. |
| 310–324 | 19:43.25–20:24.39 | Repaint/registration aftermath, registration sent to the ship computer, Gilliam's integration and intended return to Sentinel III. Integration does not establish permanent technical inseparability or a complete AI-control boundary. |
| 325–347 | 20:27.73–21:39.19 | Kei/Ban territories, Heifong warning, plans to obtain parts/weapons through Fred Luo and departure thanks. Fred is a dialogue lead here; the preview's assassin encounter is not Episode 5 story action. No measured map or territorial boundary follows. |
| 348–359 | 21:46.91–22:26.40 | Departure clearance, guide beacons, crew conversation and launch call. Distinguish control-room clearance, following beacons and the later launch order; no complete flight checklist is established. |
| 360–366 | 22:34.69–22:58.65 | Aisha's restaurant-work aftermath. Exact environment, work arrangement and visible actions remain for image review. |

Silent actions and exact shot boundaries remain for the aligned survey. Ending lyrics and the
Suzuka/Fred Episode 6 preview do not extend Episode 5's narrative evidence.

## Website context and source reuse

The cached AnimeHistory hub's EPISODE:05/BLOCK:0001 synopsis was read using CTXSRC-000004.
It supplies a concise return-to-Blue-Heaven, registration, money and Aisha-encounter overview.
Its financial framing is secondary commentary, not a measured maintenance or fuel budget.
The cached lore entry LORE:lore-entry-3772 was also read; its cross-series power-scale commentary
and later tournament example are not adopted as Episode 5 observations or a new mechanics claim.

| Source | Version and selected location | Use and limits |
| --- | --- | --- |
| CTXSRC-000026, The Beast Girl, Ready to Pounce! | New API capture, page 2152, revision 9059; SECTION:0002 | Registration/paint, Aisha's demands, dinner aftermath and intended Sentinel course. Synopsis compresses events; local dialogue narrows the outfitting scope. |
| CTXSRC-000021, Aisha Clan-Clan | Existing revision 9510; SECTION:0004, Episode 5 portion only | Exhaustion during attempted beast-power use, caster incapacitation and restaurant bill. Earlier Episode 3 demotion assertion stays unchanged; later biography is excluded. |
| CTXSRC-000016, Swanzo | Existing revision 9413; SECTION:0003, SECTION:0005 and introductory partner prose | Hilda's earlier rescue, registration/paint repayment and Mikey relationship. Earlier secondary identification and partner assertions are reused. |
| CTXSRC-000017, Melfina | Existing revision 9442; SECTION:0005, Episode 5 portion only | Chase/dinner continuity and demotion context. Section also recounts Episodes 3–4; those are not reassigned to Episode 5. No redundant claim is added. |
| CTXSRC-000003, Outlaw Star (ship) | Existing revision 9123; SECTION:0004/BLOCK:0009, sentence tied to Episode 5 reference | Gene's search connected to Melfina's origin question. Surrounding naming interpretation, later episodes and Angel Links material remain outside the adopted assertion. |

The standalone Mikey API lookup returned NOT_FOUND. No successful source row is fabricated;
the established Swanzo source and translated dialogue remain the available partner-name context.
The initial sandbox request failed; the scoped network retry through the same anonymous API
captured the episode summary before reporting the missing Mikey article. No credentials, browser
control, alternate access route, full-site crawl or source refresh was used.

CTX-000066–000072 add seven SOURCE_CHECKED / SECONDARY_ONLY assertions and 32 typed links,
including reuse links for existing scoped context. No context-to-image links or primary-status
promotions are added. The new source retains revision/history links, capture/hash metadata,
attribution, licensing and PARTIAL parser warnings. Readable prose was compared directly;
unresolved templates do not establish hidden infobox statistics or quotation details.

## Validation and next scope

Context validation passed with 44 subjects, 26 source versions, 72 assertions and 872 links.
All 27 cached snapshots verified: 23 Fandom and four AnimeHistory. Category validation passed
across all 9,204 gallery records. All earlier subject/source/claim/link rows remain identical.
All 406 protected files matched their preparation baseline, including gallery originals and
sheet registries, locator/category/supplement CSVs, subtitle provenance/copy, alignment registers
and the category workbook. All 354 Episode 5 rows remain UNREVIEWED / NOT_REVIEWED.

The existing ImportExcel context workbook refreshed with five sheets, 10,306 verified cells,
1,908 verified links and authored-data equality checks. New source/claim rows and the overview
were rendered and visually inspected. This does not claim a fresh native Office Viewer test.
Cited website captures and subtitle copies retain their local-only retention. Disposable
preparation and workbook-preview helpers are removed after verification.

Next separate step: declare and run Episode 5's bounded alignment, then review the first three
contact sheets with the verified timing limits and this context. No alignment search, image
annotation, later episode or Phase 3.2A execution is included in this preparation.
