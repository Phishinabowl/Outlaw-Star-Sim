# Episode 2 annotated survey — batch 01

Status: implemented initial survey, accepted by the maintainer on 2026-10-28. Reviewed 2026-10-28.
Scope: gallery 001–072 (847127–847198), contact sheets 0001–0024, 0025–0048 and
0049–0072. Phase 3.2A remains unstarted.

## Evidence and timing

All three sheets were visually reviewed. Selected originals inspected across the initial
paused review and this continuation are 006, 007, 009, 010, 012, 015, 018, 025, 029,
030, 034, 049, 050, 065, 069 and 071. The full-size views of 009–010 show Aisha,
Melfina and Suzuka; Jim is not visible in that composition.

The [earlier bounded frame record](episode-02-review-batch-01-frames.json) retains the
pre-alignment inspection of eight windows, 40 requested seconds and 160 extracted frames,
with 32 preview frames inspected. Those temporary files were already removed. Its paused
status is historical; the present record resumes annotations after accepted alignment.
No new video extraction was performed for this continuation.

The [accepted alignment](episode-02-alignment-review.md), ALNMAP-000004, supplies
local = web - 1.286 seconds throughout this batch. Its ±2-second navigation window does
not establish an exact subtitle/frame association. Gallery 001 and 010 have direct matching
intervals; ambiguous attempts for 018, 034 and 072 remain ambiguous. Translated English
ASS cues 31–94 were reread against the accepted mapping and prior bounded scene checks.
Speaker attribution follows scene context, not the empty ASS Name field.

Relevant local cue windows are the pirate search (163.22–172.05 s), Melfina/case check
and countdown (181.10–214.66 s), arm repair bargain (216.71–260.61 s), repair setup
(261.38–274.69 s), NanoPrometheus mention (276.20–279.50 s), Hilda's account
(282.54–331.75 s), and hand testing/further questions (332.39–359.04 s).
The countdown does not establish a complete life-support specification. Hilda's account
of leaving a ship in orbit, stealing Melfina and killing a Guild leader remains reported
dialogue rather than independently verified history. The sampled gun-handover window did
not visibly show a transfer; a spoken request is not evidence that it occurred.

## Findings

Ten contiguous scene groups preserve the opening Gene/ship/caster shots, MacDougall
montage, crew/combat montage, pirate search, title, barn case check, arm bargain, farm
exterior, repair conversation and hand test. Opening images remain distinct from story events.

High-value equipment references include the case's changing indicators and corner posts:
025 has blue indicators and flush caps; 028–029 have gold/unlit indicators and flush caps;
030 has raised perforated posts with gold/unlit indicators; 031 has raised posts and red
indicators. Images 060–061 return to raised posts with gold/unlit indicators. These visible
states do not establish the complete mechanism, medical operation or XGP pod design.

Images 034, 049–050 and 065–071 preserve the exposed prosthetic, repair contact/sparks,
Jim's needle-ended tools, detached forearm and hand movement test. The NanoPrometheus
dialogue concerns the prosthetic; it does not establish the tools' brand. Image 066 shows
Hilda seated, Jim working and Gene standing. The blaster in this scene is distinct from
the opening caster. Images 057–058 have a pale overlay of unresolved material/origin.

Selected cached secondary prose supplies CTX-000049 (Harry's green hair/purple eyes,
CTXSRC-000019, SECTION:0009) and CTX-000050 (Jim repairing Hilda's arm during Melfina's
resuscitation, CTXSRC-000002, SECTION:0004/BLOCK:0003). Both remain SOURCE_CHECKED /
SECONDARY_ONLY. The wider biography is not adopted wholesale. Existing caster, repair
and Soi Len appearance context is linked narrowly; the pirate leader's descriptive role
ID is not merged with a proper-name candidate on that basis.

## Remaining questions and retention

- 003: launch-site and upright-craft identities remain unresolved. Neither XGP nor Sentinel III
  is established for this opening shot. Maintainer clarification on 2026-10-28 identifies
  the craft as the same unnamed intro ship discussed for Episode 1 gallery 011–014 and
  016–018. Possible recurrence across episode openings is a lead to check during later
  surveys, not verified series-wide coverage. The proper-name/site recheck remains open.
- 012: maintainer clarification on 2026-10-28 identifies the gold ship as El Dorado and
  the foreground assembly as one of its grappler arms. This is a brief opening fight
  vignette, not a specific Episode 2 story event. The identification recheck is resolved;
  complete engagement geometry remains outside this survey.

All 72 rows are INITIAL_REVIEW_COMPLETE: 71 SCREENED and one NEEDS_RECHECK (003). The remaining
282 Episode 2 rows are untouched. Context registers contain 33 subjects, 19 sources,
50 assertions and 298 links. Initial survey completion does not constitute a targeted
modeling or mechanism deep dive.

Validation passed for all 9,204 category rows, context relationships and 20 cached source
snapshots. ImportExcel refreshed both browsing workbooks: the 30-sheet category view verified
432,588 gallery cells and 9,204 image links; the five-sheet context view verified 4,424 cells
and 716 links. Rendered samples of the case states, arm repair and both new context assertions
were visually checked. Both builders confirmed that authored CSV data was unchanged.
The alignment registers remain at 43 anchors and four mappings; routine view generation did
not re-verify media inputs or alter the accepted alignment. Git whitespace validation passed.

Episode originals and contact sheets remain available for subsequent batches. Episode-level
RAR bundling/pruning is deferred until survey completion; only temporary authoring and
workbook QA files from this batch are removed.
