# Episode 1 — subtitle context for gallery locators 001–072

Reviewed 2026-10-27. The full ordered English ASS track was read before revisiting the first
three contact sheets. All 293 Dialogue events were read, including opening/ending lyrics and
the next-episode preview; those presentation segments are distinct from Episode 1 story dialogue.
Later dialogue provides narrative context only: no annotation after locator 072 was changed.

## Source and timing scope

- Source: `_source_episodes/[CBM]_Outlaw_Star_-_01_-_Outlaw_World_[720p]_[A5BBC231].mkv`;
  video SHA-256 `05f4bfbe5e0d84d0e03a854699f2cc14bdcb8ded74f7ea4f6fef0ec3d0182e48`.
- English ASS stream 4; copied track SHA-256
  `edbb42674cf707b51122ddd54b132d16ffde7fe981b54f24170c155810d0b0f3` matches the
  [coverage register](performance-subtitle-coverage.json). Cue numbers below are one-based
  Dialogue-event ordinals, including song events. The Name fields are empty; speakers are not
  identified from those fields or time proximity alone. This is translated English text, not
  Japanese dialogue verification or an English-dub transcript.
- Video stream 0, time base `1/1000`, media origin zero. The registered subtitle media-relative
  basis was rechecked against the first three packets. The fresh source identity matched the
  existing alignment pilot. No mapping was extrapolated below web 06:40.
- All three existing sheets were re-inspected; gallery locators 037, 042, 057 and 071 were also
  inspected at full size. Nineteen bounded three-second local windows were sparsely decoded at
  approximately four frames per second: 228 frames across 57 seconds of requested windows.
  Selected neighboring frames from every window were visually inspected. This is a scene-context
  check, not continuous playback or frame-by-frame motion analysis.
- [Decode provenance](episode-01-subtitle-context-frames.json) retains source identity, commands,
  actual PTS, hashes and inspected-frame selection. Decoded images/comparison sheets are disposable
  and removed after review. The decode added no alignment anchors or mapping; the later supplied
  screenshot is registered below. No source-media publication is implied. Scene relationships
  below are not exact gallery-to-local frame matches.

## Launch scene

Locators **011–019** are a pre-title story sequence after the opening song, rather than opening
credit montage. Cue 23 ends at local 02:11.61; checked local 136–139 s shows the launch complex,
and 162–165 s includes the exhaust view followed by Gene's profile. Cue 24 (164.37–166.20 s)
expresses Gene's interest in space. Presentation is corrected to STORY while retaining unknown
launch-site/craft identity. Neither this line nor the later Sentinel III narration identifies this
launch facility or proves the departing vessel is XGP. Locator 007's opening figure remains
unidentified. No lyric is treated as a mechanical or character-identity statement.

## Pirate pursuit

| Locators | English ASS context | Checked visual relationship and limit |
| --- | --- | --- |
| 024–027 | Cues 25–26, 186.06–191.92 s: pursuit and fighter-launch order. | The established orange/blue pirate vessel and bridge shots precede fighter deployment. Existing tentative individual proper-name comparisons remain secondary-source leads. |
| 028–034 | Cues 27–36, 195.23–215.04 s: Blue-unit readiness calls and Blue Leader's briefing to capture Hilda and the treasure. | Local 192–195 and 202–205 s show the same goggled pilot/cockpit as the gallery sequence. This supports a pirate fighter pilot/leader-role context, not Hilda in Horus. No personal name or exact individual readiness-call attribution is assigned. The forward opening in 034 still needs a structural/layout check. |
| 035–040 | Cues 37–40, 225.87–237.67 s: missile order, a barrier reaction, then an order to close and capture with anchors. | Local 224–227 s cuts from a small green fighter to the physical screen; 231–234 s shows the distant target/light. Full-size 037 visibly includes MODE, MISSILE A-13 and GUN labels. The translation's A-3 wording is not silently equated to the visible A-13 label. Exact screen installation and the barrier's hardware/physics remain open. |
| 041–046 | Same pursuit/capture context; no dialogue names the aperture panel. | Local 238–245 s shows green attacking craft, Horus's blue/yellow rear assemblies and the aperture panel with pale shafts/red streaks. Local 249–252 s provides the broader four-cone rear view and nearby attacking craft. These do not establish panel function, shaft direction or an anchor-launcher identity. |
| 047–054 | Cues 41–49, 259.80–284.49 s: impacts, critical hull condition, emergency-escape recommendation, repeated inability to return fire, and Hilda's dangerous choice. | Local 257–260 s reaches the red-lit Horus cockpit after attack imagery. The later familiar goggled pilot remains on the pursuing side. Automated-sounding warnings are recorded as ship-warning dialogue without inventing an AI's personal name or a complete command protocol. |

The generic `pirate_fighter` and `pirate_fighter_pilot` subject tags identify this Episode 1 force.
They do not assert that these fighters and Episode 4's separately tagged pirate landing craft are
the same vehicle class.

## Horus sub-ether drives

Locators **055–059**, with broader assembly references **041 and 044**, are useful Horus drive
references. Checked local 286–293 s shows Hilda/control imagery, then the extended yellow cone
and changed fin/cone configuration. Local 294–297 s shows the larger assembly amid broad white
curved effects; 299–302 s cuts through the pursuing pilot, Horus/effect imagery, separation and
explosion imagery. Cues 50–52 (306.01–314.72 s) identify the escape as sub-ether drive use and
express disbelief that Horus activated it while damaged. The subtitle is a later reaction, not a
line spoken over every cone close-up.

**Maintainer identification, 2026-10-27:** the yellow cone assemblies are Horus's sub-ether drives,
spinning up in this sequence, with four units, one on each rear pylon. The supplied local-player
04:10 wider screenshot and independently checked local 249–252 s view show all four yellow
assemblies around the bright central exhaust region. The count/arrangement is directly visible;
the component identification and spin-up description retain this explicit attribution alongside
the corroborating escape dialogue. Tag these as sub-ether-drive references rather than leaving
them as wholly unidentified spikes. No rotation rate, complete extension/retraction path, internal
construction or equivalence to XGP's drive mechanism is established by these sparse frames.

Locators **060–062** show the pirate bridge reacting to that escape. The visible panel in 060 also
retains Horus-outline/interface reference value. No new proper pirate-leader names are established
by the translated reaction lines.

## Sentinel III

Locators **063–067** show the planet/city establishing sequence. Checked local 320–323 s spans
the globe and dissolve into the city, and 324–327 s continues that dissolve/city view. Cues 53–56,
321.93–331.94 s, explicitly introduce Sentinel III and supply translated classification/population
figures. The establishing sequence therefore supports the `sentinel_iii` location tag. These
images do not identify every visible district or prove this is the launch site in 011–019.
The later use of Locust in dialogue does not by itself give a measured city boundary or map.
Classification figures are subtitle statements, not independently verified environmental metrics.

## Clyde's Bar and the glass

Locators **068–072** introduce Clyde's Bar and the bartender. Cues 57–60, 341.98–352.56 s,
begin with a service question, a visitor asking for Gene and a grievance involving the visitor's
brother. Local 340–343 s shows the bartender holding/wiping the glass; 343–346 s shows the
close-up with repeated images of the male visitor across its facets. Full-size 071 confirms that
the repeated portrait is different from the mustached bartender. It is an optical/stylized bar-shot
presentation, not evidence of a computer display, magic or multiple physical people in the glass.
Whether to reproduce it as refraction, reflection or a deliberate animation cheat remains open.

Later cues 76–85 and 92–99 explain the Butch grievance, Rob Cain/Death Rob introduction and bounty
aftermath. These provide full-track narrative context; they do not create exact timing for 071,
authorize changes to later gallery rows, or justify tagging the bartender's portrait as Rob Cain.

## Annotation scope and remaining questions

Targeted context checks are recorded as PARTIAL, with this review linked, for 011–019 and
024–072. This status refers to the scoped subtitle/scene check, not completed translation,
mechanical analysis or full identity verification. The remaining first-batch images retain
INITIAL_REVIEW_COMPLETE; locators after 072 remain untouched. Original visual observations and
attributed prior context are preserved except for explicit corrections described above.

At the initial subtitle-follow-up checkpoint, open questions were: opening figure 007; launch craft/site in 011–019; fighter forward opening
034; exact screen installation/label relationship in 037; aperture-panel ownership/function in
042; complete Horus drive articulation; and physical reproduction of the faceted-glass effect.
No Japanese text was newly transcribed. No full-show or whole-episode timing mapping was added.

## Subsequent maintainer clarifications — 2026-10-27

These clarifications refine the initial findings above. Attribution remains explicit; the
tentative launch-site, launcher-count and laser-technology statements are not upgraded to
independently verified facts.

| Locators | Clarification and resulting annotation |
| --- | --- |
| 007 | Maintainer identifies Gene dodging incoming missiles during the intro. Gene replaces the unknown-character tag; the full evasive action is reported context. Initial screening is complete. |
| 011–014, 016–018 | Maintainer believes an ordinary unnamed ship launches from Sentinel III while Gene watches before title cards 020–021. Retain seven NEEDS_RECHECK records because the planet/site attribution is expressly tentative; do not identify the ship as XGP. |
| 034–036 | Maintainer identifies 034 as the fighter's launch tunnel, connecting the pilot in 028–033 to the downward-facing tubes beneath the pirate vessel in 035–036. Launch-role identification is resolved; precise geometry/count/full motion remain later detail work. |
| 037 | Maintainer identifies the fighter targeting screen. Ownership recheck is resolved. Visible A-13 versus translated A-3 remains an independent label/translation question, not an unknown screen owner. |
| 038 | Maintainer identifies the trails as fighter-launched missiles heading toward Hilda/Horus before meeting her barrier. Added missile/projectile context; barrier physics remain undefined. |
| 042 | Maintainer identifies Horus's aperture arrays as return-fire missile launchers. The wider supplied salvo image supports distributed firing around the rear assemblies. The estimate of likely at least four launcher installations remains tentative because the image shows trail origins rather than every aperture panel. |
| 045–046 | Maintainer identifies a deployed return-fire pod, described as a laser pod or similar weapon. Add defensive-weapon context without asserting an official weapon name or independently verified laser technology. |
| 071 | Maintainer confirms the faceted glass repeats the visitor's face and is unsure how it would be recreated. Scene classification is resolved; physical optics/rendering implementation remains a deferred material task. |

The supplied full screenshot is **EP-01-MAN-001**, preserved unchanged at
`reference/working/manual-supplements/EP-01/EP-01-MAN-001.png` and registered in the
[supplement index](animehistory/supplemental-index.csv). It shows Horus obliquely from the rear,
four yellow cone assemblies, a bright central exhaust region and multiple groups of white trails.
The original file is 2,772,871 bytes, SHA-256
`edf95d9e4ca6292356c3ad0bf945428ce26551337cbfd14c72fe6a88fb595088`.
The VLC label is **04:05**, retained as PLAYER_UI_WHOLE_SECONDS / UNRECONCILED; association
with locator 042 is contextual, not an exact frame alignment. It will join Episode 1's gallery
originals in that episode's RAR during completion cleanup. No archive/prune is run mid-review.

Current first-batch counts are **65 SCREENED / 7 NEEDS_RECHECK**. The seven flags are exactly
011–014 and 016–018. First-batch detail depths remain 58 PARTIAL / 14 INITIAL_REVIEW_COMPLETE;
007's supplied identification does not invent a new decoded-frame deep dive. A total of 59
gallery rows differ from the pre-follow-up checkpoint; all changes remain inside 001–072.
There are now ten manual supplements overall, including this one Episode 1 record. Later gallery
annotations, existing nine supplements and alignment registers remain unchanged.

Clarification validation passed for all 9,204 gallery rows and ten supplements. The refreshed
ImportExcel workbook passed its existing saved-value/link checks, including 510 manual cells;
changed identity, ownership, weapon-context and manual-reference views were visually checked.
Temporary patch/render outputs were removed after review. EP-01-MAN-001 remains hash-verified,
local-only and retained for episode-end archiving. The maintainer confirmed the follow-up and
clarifications on 2026-10-27.

## Validation and retention

Initial follow-up category validation passed for all 9,204 gallery rows and nine supplements. Exactly 58 rows in
the authorized first batch changed; the other 9,146 rows remain unchanged. The first-batch
counts are 60 SCREENED / 12 NEEDS_RECHECK and 58 PARTIAL / 14 INITIAL_REVIEW_COMPLETE.
The generated ImportExcel workbook was refreshed with explicit current-media verification;
save/reopen checks passed for 432,588 gallery cells, 9,204 image hyperlinks, 459 manual cells and
1,029 alignment cells. Changed launch/pilot/drive/location/provenance views were rendered from
the saved workbook and visually checked. The mapping registers and all later survey rows are
unchanged; no workbook layout or tool code changed in this follow-up.

All 228 decoded frame hashes were checked against retained provenance before cleanup. The
identified temporary scene-check workspace, including decoded PNGs, contact previews and workbook
render previews, was removed, reclaiming 184,220,360 bytes (about 176 MiB).
The source video, ASS copy, authored annotations, alignment registers and retained decode metadata
were byte-identical across deletion. The provenance flag was then updated to record removal.
Existing gallery originals and contact sheets remain for the ongoing Episode 1 review. The
maintainer confirmed this checkpoint on 2026-10-27; it does not start locators 073–144 or Phase 3.2A.
