# Episode 1 initial survey — batch 02

Status: implemented initial annotations for gallery locators 073–144, 2026-10-27. No 3.2A work.

## Scope and evidence

All three retained contact sheets (073–096, 097–120, 121–144) were visually inspected. Full cached
images 080, 084, 095, 099, 101, 109, 122, 137, 143 and 144 were also inspected. This is an initial
category/context review, not a measured reconstruction or continuous fight-animation analysis.

Primary local evidence uses the pinned Episode 1 CBM release and extracted ASS stream 4.
The [decode provenance](episode-01-review-batch-02-frames.json) records source/subtitle SHA-256,
stream/time basis, commands, 132 frame hashes/PTS and the selected preview frames across eleven
three-second windows (33 seconds total). The two previews were visually inspected. Generated
decode frames/previews were hash-checked and pruned; source media were not modified.

Subtitle cues 57–116 were reviewed for the bar visitor, card game, confrontation, cyborg fight,
bounty and walkway conversation. Cues 80–85 (local 412.45–431.26) identify Rob Cain / Death Rob;
86 (441.58–444.31) warns of the cyborg, and 90–91 (464.34–469.10) identify Type C and the bias-line
weakness. Cues 92–100 (480.59–507.71) support Clyde, the sheriff call and 4,000-wong bounty/repair
discussion. Cues 101–116 (508.81–571.14) cover crowd reactions and the nighttime separation.
No full subtitle text is reproduced here.

The existing validated navigation rule is local = web - 1.388 seconds only for whole-second
web labels [400,1241). Locators 073–086 fall before that range: bounded local scene inspection
and sequence context are used without extrapolating the mapping. Supported estimates for later
images remain navigation aids; no exact frame/subtitle match or new anchor was added.

## Secondary context

Cached Fandom Outlaw World page 2092 revision 9407, SECTION:0003 (CTXSRC-000008), provides the
Iris caption and Jim/PDA synopsis associations recorded as CTX-000029–030. Its Rob Kane spelling
is retained as an alias alongside the subtitle spelling Rob Cain. Cached Hilda page 2048 revision
9440, SECTION:0004 (CTXSRC-000002), supplies CTX-000031's Rachel/disguised-observer association.
These remain SECONDARY_ONLY. The captured source versions were reused; no new site retrieval
or later-episode biography material was needed.

## Findings and limits

- 080 shows cards and chips; complete game rules and printed designs remain unverified.
- 084 shows boot detailing; the maintainer identifies the orange part as belonging to Gene's boot.
  No separate holster or functional mechanism is asserted.
- 095 shows Gene pointing a gloved finger, not holding a gun in that still.
- 099 shows the back of Jim's blue hinged device; the PDA role is secondary and no diagnostic
  screen is readable. Local dialogue supports the Type C warning without establishing UI design.
- 101 shows Rob's mechanical-arm strike with Gene's pistol raised overhead; do not describe a kick.
- 109 shows a physical knife blade with blue contact arcs. No energy-blade technology is inferred.
- 075 and 112–118 show Iris, identified by the maintainer. Secondary summary/biography
  associations remain separately attributed; her name is not spoken in the checked passage.
- 122 is attributed to Hilda/Rachel through secondary context; the name is not spoken in this shot.
- 127–128 establish a sky view then an orange incoming streak; subtitles describe an unusual
  arriving flight, not a positively identified vessel in the streak itself.
- 137–139 provide rocky outskirts/industrial transition references. Exact facility geography is unknown.
- 140–144 show the pirate ship from the beginning of Episode 1, identified by the maintainer.
  Reuse pirate_attack_ship for continuity; exact facility geography remains unverified. The orange
  hull, antennae, gantries and boarding ramp remain useful exterior/access references.

## Result

After maintainer clarifications, all 72 new INITIAL_REVIEW_COMPLETE rows are SCREENED.
Episode 1 totals: 144 reviewed, 137 SCREENED, seven NEEDS_RECHECK, 210 unreviewed;
58 PARTIAL and 86 INITIAL_REVIEW_COMPLETE. Prior annotations and other episodes are preserved.
Gallery originals, contact sheets and the manual supplement remain local pending episode completion.
No RAR cleanup, alignment-model change or phase acceptance is implied.

Validation: all 9,204 gallery rows and ten supplemental records pass the category validator;
the 24-subject, 12-source, 31-context register passes its validator. ImportExcel refreshed the
category workbook (432,588 gallery cells, 9,204 image links, 510 supplemental cells and 1,029
alignment cells checked) and context workbook (2,342 cells and 348 links checked), preserving
the maintained CSVs. A read-only render of saved EP-01 rows 112–115 was visually inspected.
All 132 decoded frame hashes were rechecked before removing the owned temporary directory,
including its previews/helpers, reclaiming 107,278,108 bytes. Provenance and retained episode
media remain. Changes are uncommitted pending confirmation.

## Maintainer clarifications and Iris lookup — 2026-10-27

The maintainer identifies Iris in 075 as one of Gene's flings, the orange detail in 084 as part
of Gene's boot, and 140–144 as the pirate ship seen in the opening chase. Related Iris-tagged
shots retain the same identity; these reported clarifications do not manufacture primary checks.
The six batch rechecks are resolved without assigning an exact landing-facility geography.

The supported Fandom API retrieved Iris page 2090 revision 8723 as CTXSRC-000013. Its selected
Outlaw Star biography paragraph (SECTION:0003/BLOCK:0001) supports CTX-000032–033: her workplace
at Clyde's Bar and romantic interest/flirtation with Gene. Angel Links content and later plot
events were excluded. Unresolved template warnings remain recorded; no image downloads or
full article text were added to tracked files. No timing or review-depth changes were needed.

Post-clarification validation passed for the unchanged 9,204-row gallery/ten-supplement population
and the expanded 25-subject, 13-source, 33-context register. Both ImportExcel views refreshed with
saved-value/link checks; corrected boot and ship rows were rendered and visually inspected.
The category workbook retained verified alignment availability and unchanged timing records.
