# Episode 4 — subtitle and website-context preparation

Status: implemented, verified and accepted by the maintainer on 2026-10-29 (America/New_York).
This retrospective increment adds subtitle and selected website context to the already accepted
Episode 4 initial survey. It does not re-review gallery images, revise earlier observations or
retroactively describe those batches as subtitle-assisted. Episode 4 alignment and the subsequent
annotation/documentation reconciliation remain separate steps. Phase 3.2A remains unstarted.

The subsequent [alignment checkpoint](episode-04-alignment-review.md) is also accepted. The
preparation-time scope and retention observations below remain historical; the alignment record
owns the subsequent timing coverage and restored-gallery state. The reconciliation sweep remains next.

## Pinned inputs and read scope

- Source: `_source_episodes/[CBM]_Outlaw_Star_-_04_-_When_the_Hot_Ice_Melts_[720p]_[000FA756].mkv`.
- Source bytes: 815,458,262; SHA-256
  `47dd82cdb4beb00aac606b79b6f8764f557cacd760347a6b0c5754ef589ab411`.
- Video stream 0, time base 1/1000, media origin 0; 960×720; duration 1519.018 s.
- English ASS stream 4; existing local copy
  `reference/working/performance-subtitles/episode-04.ass`.
- Subtitle SHA-256 `560974c33b10f385fd8c30d006959a7e33f741e6fa8ab7237b4c24bb8b294d0b`
  matches the [coverage register](performance-subtitle-coverage.json). Source size, selected
  stream/codec/language and unchanged source file signature passed read-only inspection.
- A bounded FFprobe inspection compared the first three subtitle-packet starts with the ASS:
  1.75, 8.79 and 14.22 s match. This establishes that bounded timing check, not every packet,
  translation or spoken line. No video frames were decoded, gallery images restored or alignment
  runs created. Source media and subtitle bytes were not modified.

All 355 ordered Dialogue events were read: 1–15 introductory grappler-history narration;
16–31 opening lyrics; 32–340 story dialogue and translated on-screen captions; 341–347 ending
lyrics; 348–355 Episode 5 preview. The ASS Dialogue event type includes captions such as the
bootstrap countdown and registration labels; those are not assumed spoken lines. Empty Name
fields do not identify speakers. These are translated English subtitles, not a verified English-dub
transcript or an original-Japanese transcription. Full text remains ignored/local-only.

## Local subtitle navigation notes

All intervals below follow this pinned local release. They are not corrected AnimeHistory
timestamps and must not be attached automatically to the closest gallery label. No Episode 4
mapping is created or accepted here; offsets from Episodes 1–3 must not be reused. Earlier
local-frame reviews retain their own evidence scope until the authorized reconciliation step.

| Cues | Local interval | Context and limits |
| --- | --- | --- |
| 1–15 | 00:01.75–01:09.71 | Introductory grappler-arm history and computer assistance. Narrated history does not establish every vessel's mechanism or measured pilot load. |
| 32–46 | 02:50.52–04:27.85 | Orbit matching, asteroid approach, transfer and XGP15A-II reveal; pirate/Space Forces origins. Do not infer a full docking route from dialogue alone. |
| 47–58 | 04:40.93–05:17.32 | Unusual controls, Hilda's theft and development explanation. The alarm-clock joke does not independently identify every pictured prop. |
| 59–65 | 05:19.34–05:25.30 | Translated ACTIVATE/KEY/HOLD and three-to-zero captions. Subtitle event durations are not independent verification of screen animation, button input or hardware behavior. |
| 66–89 | 05:41.52–06:54.96 | Gilliam's introduction, maintenance responsibility, crew claim, missing personnel rules and declined recovery. A scene-specific exchange, not a universal AI/security specification. |
| 90–115 | 06:54.93–07:57.18 | Registration captions; Gilliam says he supports other systems but cannot pilot, and Hilda assigns Melfina to assist. Keep systems support, piloting and interface roles separate. |
| 116–127 | 07:57.46–08:29.36 | Ship-status request, missing furnishings, ten emergency food packs, incomplete naming and incoming Horus warning. The unqualified distance number does not establish a unit. |
| 128–145 | 08:37.86–09:23.13 | Horus detection delay attributed to magnetic conditions/Tao field; Hilda returns to defend in Horus while Gene, Melfina and Jim are assigned stations. No exact sensor performance or seat geometry follows. |
| 146–152 | 09:24.18–09:48.10 | Jim's preferred name, waiting for Melfina and the displayed control manual. Dialogue alone does not establish the complete manual or apparatus motion. |
| 153–159 | 09:52.37–10:11.72 | Main Horus engine/anchor/ammunition discussion. The 34% ammunition report concerns Horus in this scene, not XGP inventory. |
| 160–168 | 10:19.93–10:50.56 | Repeated connection reports and established Melfina link. Captions/lines do not independently establish connector count, fluid properties or every intermediate movement. |
| 169–183 | 10:51.43–11:26.59 | Sealed engines, engine-room directions and testing history. The engine itself was reportedly tested, with no record of testing after installation; this is not a claim that no testing of any kind occurred. |
| 184–193 | 11:30.57–12:17.14 | External hailing, hurry warning and Space Forces packing/sealing tradition. Exact seal-removal sequence requires the existing visuals and later reconciliation. |
| 194–200 | 12:32.25–13:02.47 | Dock intrusion, Horus remaining anchored to rotate the asteroid as a shield, and pirate grappler-section separation orders. Distinguish parent ship, grappler section and Horus. |
| 201–215 | 13:15.26–14:14.44 | Attack orders, Gilliam's remote gate operation, startup readiness, ignition key, generators and switch from sub-circuits to mains. The lifting line is a contextual cue, not independent verification of seat-lift geometry. |
| 216–235 | 14:15.25–15:14.57 | Blocked exit, Horus anchor release, XGP's operational but unarmed grappler arms, wall-clearance concern and enemy anchor order. Current unarmed state is not a lifetime armament limit. |
| 236–256 | 15:16.88–16:28.68 | Initial incoming projectile warning, MacDougall ship recognition and expired/new-contract exchange. The initial projectile description must not be conflated with the later specifically named missile; new client identity is not supplied in these lines. |
| 257–270 | 16:33.49–17:55.34 | Gravity-well warning, dock-camera request, Gene's recognition/flashback context, later missile order and brothers' departure. Their fastest-ship boast is not a verified comparative speed measurement. |
| 271–290 | 18:03.47–19:09.67 | SUN/ESCAPE/CRASH captions, gravity-catapult risk, asteroid breakout, attitude stabilization and rapid engine-power warning. No complete trajectory or universal throttle/stability law established. |
| 291–300 | 19:16.29–19:46.41 | Four sub-light engines observed by an opponent, pirate boarding preparations, 81% output and escape-velocity report. Four-engine terminology is not a four-sub-ether-drive claim; numerical output does not establish thrust. |
| 301–317 | 19:55.72–20:42.50 | Attempted Hilda pickup, rescue/deceleration constraint, pirate tether and abandonment exchange. Maintain main-Horus/dropship distinctions from existing visual notes; empty speaker fields do not resolve each radio voice automatically. |
| 318–333 | 20:56.65–22:08.31 | Increasing output, failed rescue/anchor-distance reply and Hilda's final message. No measurable anchor range or fully verified explosive mechanism follows from dialogue alone. |
| 334–340 | 22:41.92–23:10.38 | Gravity-well exit, course request and Gene naming the ship Outlaw Star. The naming event is explicit; inferred motivation remains attributed secondary interpretation. |

Ending and preview material is a boundary, not additional Episode 4 story evidence. Gallery
frame association, exact shots during silent sequences and subtitle-to-image timing remain for
alignment and the subsequent bounded sweep. Existing manual supplements retain their whole-second
player labels and unreconciled timing status.

## Website context and source reuse

The original context-tool pilot already captured substantial Episode 4 material. Existing
CTX-000001–000017 are reused for Horus/dropship distinctions, asteroid concealment, Melfina,
Gilliam, Gene's childhood memory and other scoped leads. Their earlier verification status,
image links and uncertainty wording are unchanged. No repeated assertion is created merely
because it is useful again.

Selected reads this increment:

| Source | Version / selection | Use and limits |
| --- | --- | --- |
| CTXSRC-000004, AnimeHistory series hub | Cached EPISODE:04/BLOCK:0001 | Episode synopsis; naming and sacrifice context. Farfallus retained as a lookup spelling variant. |
| CTXSRC-000002, Hilda | Page 2048, revision 9440, SECTION:0006 | Existing defense, dropship and missile leads. This section spans Episodes 3–4 and has inconsistent star/planet wording; it does not verify exact cuts, all casualties or client identity from Episode 4 dialogue. |
| CTXSRC-000003, Outlaw Star (ship) | Page 2159, revision 9123, selected Episode 4 paragraphs of SECTION:0004; SECTION:0009 | Concealment and origins context. Later episodes/Angel Links references, broad equipment claims and Newton-reactor mechanics are not adopted as fresh Episode 4 evidence. |
| CTXSRC-000006, Ships, Casters & Tao Magic | Cached LORE:lore-entry-3768 | Existing Gilliam systems/personality commentary. Editorial interpretation is not a complete control-system specification. |
| CTXSRC-000024, When the Hot Ice Melts | New API capture, page 2147, revision 9063, SECTION:0002 | Crew activation, destroy-XGP mission, recognition and naming context. The synopsis compresses events and uses inconsistent celestial wording. |
| CTXSRC-000025, Gilliam II | New API capture, page 2049, revision 9415, SECTION:0001 prose | Introductory AI identity only. Activation section is empty; unresolved infobox/quote material does not establish bot dimensions, age or piloting capability. |

Both new captures are PARTIAL because templates remain unresolved. Readable selected prose
supports the five concise new SOURCE_CHECKED / SECONDARY_ONLY records CTX-000061–000065.
The preserved source rows retain revision/history links, retrieval time, hashes, attribution,
license metadata and parser warnings. Existing cached Melfina section navigation was checked;
the read SECTION:0004 concerns earlier events and supplies no new Episode 4 assertion.
No entire-site crawl, credentials, image download or source refresh was required. The first
sandboxed episode-summary request timed out; the scoped network retry through the same API
adapter succeeded. No access-denial bypass was used.

## Reconciliation leads retained for the next steps

- **Missile terminology:** local English cue 263 (17:09.99–17:11.89) spells the later order
  "halcyon missile"; Hilda SECTION:0006 says Helicon. This is evidence of a translation/source
  discrepancy, not proof that the maintainer's earlier spelling was a typo or that both names
  are canonically equivalent. CTX-000014, halcyon_missile identity and earlier attributed notes
  remain unchanged pending the sweep, settei/Japanese comparison and any necessary footage check.
- **Gilliam/Melfina boundary:** local cues 101–112 describe Gilliam's piloting limitation and
  Melfina's assistance. Reconcile these with existing systems descriptions without expanding
  or rewriting the accepted first-slice implementation contract.
- **Startup:** engine seals and testing history, operator preparation, ignition and the mains
  transition need to remain distinct. Dialogue timing alone does not prove every moving part.
- **Vehicle and weapon continuity:** retain main Horus versus dropship, pirate main/grappler
  sections, initial smaller projectiles versus later missile, and local sub-light versus
  sub-ether terminology. Do not replace existing maintainer-supplied identities with generic
  synopsis wording.
- **Celestial and chronology wording:** Farfallas/Farfallus spelling and source star/planet
  inconsistencies remain explicit. No universal speed, cooldown, anchor range or gravity model
  is inferred. Earlier local review times and manual screenshots are not silently retimed.

## Preservation and next scope

All 52 protected input hashes matched: untouched index CSVs, Episode 4 contact sheets/registry
and the archived RAR/receipt. All earlier 44 subjects, 23 source rows, 60 assertions and 769
links are preserved exactly; the three edited context tables only append two sources, five
assertions and 23 subject/episode links. There are no new context-to-image links or promotions
to primary-corroborated status. Current context counts are 44 subjects, 25 sources, 65 assertions
and 792 links. All 26 cached snapshots verified (22 Fandom, four AnimeHistory).

Context relationships and all 9,204 category rows passed validation. ImportExcel refreshed
the five-sheet context workbook, verifying 9,406 cells and 1,743 links with authored-data
equality checks. New claim, Gilliam, source-version and relationship-link ranges were rendered
and visually checked. No category-workbook or native Office Viewer re-test was needed for
this context-only increment. Git whitespace checks passed.

Category/supplement annotations, reported context, review states, alignment registers and
locator rows are unchanged. The accepted Episode 4 RAR remains pruned; contact sheets remain
available. Generated subtitle copies and cited website caches retain their existing local-only
retention. Disposable preparation and workbook-QA helpers are removed after verification.

Next separate step: Episode 4 bounded alignment using restored verified gallery inputs as
needed. After timing validation, reconcile the existing annotations, supplements and selected
documentation in bounded increments. No alignment execution, automatic annotation sweep,
next episode or Phase 3.2A is included in this preparation.
