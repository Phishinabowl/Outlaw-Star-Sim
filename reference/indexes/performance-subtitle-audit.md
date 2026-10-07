# All-episode subtitle performance audit

Publication approval: the user confirmed this audit and the accompanying numerical follow-up on 2026-10-07; the closing uncommitted-status note describes the pre-confirmation review state. Full subtitle/candidate text remains local-only.

Reviewed 2026-10-07 following the user's request to search all episodes for performance metrics that could constrain a later simulation model. This is a **subtitle-text audit**, not an audio, visual or complete canon verification pass. No simulation model is selected or implemented.

## Coverage and reproducibility

[Coverage/provenance JSON](performance-subtitle-coverage.json) records **all 26 numbered local MKVs**, exact source-relative filenames/byte sizes, selected English subtitle stream index/title, FFmpeg command/version, copied-text SHA-256, ASS entry counts and keyword counts. The separate pilot is not part of the numbered 26-episode run. All selected streams are ASS stream 4, English full-dialogue tracks rather than the signs/songs track.

The [scanner](../../tools/reference-extraction/scan_performance_subtitles.py) copies subtitle packets only, with no audio/video decoding. Local copies and complete candidate/context text are ignored under `reference/working/performance-subtitles/`. It refuses existing output destinations. The candidate/provenance indexes were regenerated from the same hash-checked copies after broadening the search to spelled-out numbers, degrees, mass and inertia terms; no subtitle copy was overwritten.

**9,343 ASS Dialogue entries** were scanned, yielding **1,060 broad keyword/number leads**. These counts include song/title text stored as Dialogue, not just spoken lines. Candidate text was screened, and promising passages were read with surrounding dialogue to check the subject, operating condition and units. Keywords include digits and spelled numbers/fractions, speed/acceleration, distance/time, power/reactors, gravity, sensors/range, fuel, pressure/temperature, launch and operating modes. Keywords cannot guarantee discovery of every implicit metric; no blanket claim that all unselected lines are irrelevant is made.

The [curated CSV](performance-metrics.csv) contains **41 XGP/route/environment/technology records and 6 separately marked other-ship leads**. Values are paraphrased, with local subtitle start/end intervals, subject, review status, intended evidence use and limits. Exact source/stream/hash resolve through the episode ID in the coverage JSON. These are translated anime statements checked in this release; original Japanese and visual displays remain unreviewed here. None of the rows is an automatically verified numerical simulation constant. Calculations below are **D inferences, never canon**; any eventual design curve or time compression is E/F.

## Most useful findings

| Record | Evidence | Potential constraint and limits |
|---|---|---|
| PERF-015, EP-11 02:41.68–03:12.04 | 108% engine output, engines normal, subsequent instruction to return to normal. | Actual incident differs from EP-07 training. Supports an over-nominal event, not a permanent 108% safe rating. |
| PERF-009, EP-08 20:31.45–20:35.58 | Engine 2 abnormal and output dropped 30%. | Damage derating lead; a drop by 30% is not output at 30%. Scope of output remains ambiguous. |
| PERF-019, EP-11 09:33.93–09:47.47 | Ether interference; subspace-radar error 24%, standard-radar effective radius reduced 30%. | Different sensor measures, not a universal accuracy/visibility multiplier. Baseline ranges are absent. |
| PERF-020, EP-11 09:56.02–10:03.81 | 12 km/s, next 180 km clear. | Local-navigation speed and clear path; not maximum speed or sensor radius. |
| PERF-025, EP-11 17:45.72–17:54.52 | 600 million km, about 96 h, stated 50% propulsion. | Existing damaged ether-only trip-average anchor; retain the separate two-reactor 50% statement. |
| PERF-029, EP-12 13:59.21–14:09.37 | Approximately 100 km effective signal range in current interference, discussed for remote cameras. | Camera-link range in adverse conditions, not ordinary radar or weapons range. |
| PERF-036, EP-20 19:13.50–19:36.99 | External monitors cut except Gene's; arm response raised to 150%; boosted system can operate for one minute. | Response/time limit tied to a special mode; no absolute arm speed, force or thermal cause supplied. |
| PERF-031, EP-16 00:17.38–00:35.40 | Dragonite enables Münchhausen technology and acts as catalyst releasing ether energy. | Stronger translated primary-context lead than the supplied screenshot's burned-fuel wording; no consumption law or joules/kg. |
| PERF-039/040, EP-24 | Engine output 70% at 15:05; acceleration dropped to 70% at 19:36 amid Leyline pull/guidance. | Two separately stated quantities/events; does not prove power and acceleration scale linearly. |

## Distances, times and calculations to keep separate

The race course is about **1.6 billion km** (PERF-012). Other specified legs include **230 million km to Heifong III** (PERF-013), **500 million km toward Heifong V** (PERF-016), and **140 million km from Heifong V to checkpoint 3** (PERF-018). These constrain route scale, not each planet's orbital radius or a single fixed course. The race offers alternative checkpoint routes and sub-ether/ether-stream travel. Screen time, standings and staggered two-minute starts do not establish an exact XGP completed-race duration.

The existing [EP-11 numerical follow-up](episode-11-subether-review.md#numerical-travel-performance-follow-up--2026-10-07) is authoritative for PERF-020/024/025's detailed interpretation and **D** average calculation: `600,000,000 km / (96 × 3,600 s) ≈ 1,736 km/s`, approximately 0.58% of light speed. This is a damaged-trip forecast, not a speed cap.

**PERF-D02 — conditional D clearance interval:** `180 km / 12 km/s = 15 s` if the reported clear path lies along the flight direction and speed stays constant. This is a potential navigation reaction interval, not a guaranteed safe time, stopping distance or measured sensor latency.

**Hold PERF-013:** the local English subtitle literally gives an ETA of approximately **1000 hours** for the 230-million-km leg. Soon afterward the race commentary says leading ships reach the first checkpoint after **14 hours**. These are not automatically the same ship/start time/route, but the disparity warrants original-language/audio verification. Do not silently replace 1000 with 10 or assume 1000 is a clock time. No preferred speed is calculated from this disputed wording.

**Do not pair PERF-011:** EP-09 says another 20 light years to **Kozat space**, then approximately three days in Sentinel time to **Heifong**. EP-08 separately calls the Heifong trip about 20 light years. Endpoints and route position are not reconciled; no 20-light-years/three-days FTL speed is established.

**Do not divide PERF-023:** 360 million km above an orbital plane and 2 minutes 24 seconds since a disrupted entry do not supply a known start/end displacement or path length. The starting height above that plane is unknown.

## Operating and environmental context

- EP-04's 81% output/escape report lacks Farfallas mass, ship radius from the star and numerical escape velocity; later 85/86/87 callouts do not establish a ramp law. Stabilization-before-full-output cautions are separately retained.
- EP-06 fuel shortage prevents repeating a landing approach; a surface-distance callout says 100 without a unit, and landing strut 3 is yellow. Neither tank capacity nor load limit follows.
- EP-11's at-least-one-hour stop is a race maintenance requirement; all systems are reported green. It does not demonstrate one hour of unavoidable engine cooldown. Its 24-minute penetration estimate is route/preparation context, not a universal startup time.
- EP-12 confirms Newton 1/3 green after completed rush repairs. That supports repair recovery after EP-11 damage, not recovery from a simple restart.
- EP-14 reports surviving oxygen circulation/attitude control/grapplers with other systems compromised. Its no-radio-lag inference places a caller probably within 30,000 km; this is not a communications maximum or a calibrated latency measurement.
- EP-16 calls both ether/sub-ether systems into waiting mode for silent running, then disengages it for full thrust. The 15-ton dragonite treasure belongs to another pirate ship; it is not XGP payload capacity. A preview's 50-ton wording is not substituted for the episode's 15-ton cargo report.
- EP-22 gives Hecatoncheir equatorial/polar/prison gravity as 1G/10.4G/3G and a human-time day of 74 minutes. These describe the environment, not XGP acceleration tolerance. EP-24's approximately 0.974G describes the Leyline arrival location, not onboard gravity-control range.
- A ship detected emerging 700 km to starboard in EP-24 is an encounter separation, not maximum sensor range or jump-navigation precision. EP-19's 20% predicted missile impacts and EP-11's 87% missile classification are incident predictions, not universal probabilities.

## Other-ship and rejected-number handling

OTHER-001–006 preserve useful leads without assigning them to XGP: Horus's two jumps/final countdown, less than 50 parsecs before recommended servicing, asteroid-clearance ETA, later transition timing and Farfallas distance; the cruiser's shield-drop/course/thruster command needs visual/audio attribution before further use. Remaining servicing distance is not a complete service interval. A 3-degree course command plus a 10-second thruster firing is not a measured 0.3-degree/s angular rate.

The EP-04 34% ammunition report belongs to Horus; EP-12's 24% remaining concerns enemy missiles. Currency, calendar years, character ages, caster-shell numbers, ship/dock IDs, ground-car travel, bomb deadlines, preview exaggerations, lyrics and tournament statistics were excluded from the performance CSV. Empty-unit distance callouts were retained only where navigation-relevant, explicitly unresolved.

## Per-episode result map

| Episode | Selected records / screening result |
|---|---|
| 01 | No additional numerical XGP performance anchor; opening chase precedes XGP discovery. |
| 02 | OTHER-001; qualitative claim of the sought ship's ether-Sargasso capability. Resuscitation countdown is not propulsion. |
| 03 | OTHER-002–006; Horus/cruiser context, not XGP. |
| 04 | PERF-001–005; other-ship ammunition excluded. |
| 05 | No additional ship-performance metric; half-power/energy remarks concern Aisha. |
| 06 | PERF-006; three-hour journey concerns rented car. |
| 07 | PERF-007 retained as training-only; output units unspecified. |
| 08 | PERF-008–010; unitless 20,000 encounter distance and combat countdown do not establish speed. |
| 09 | PERF-011; mismatched travel endpoints. |
| 10 | PERF-012–014; ETA wording held for verification. |
| 11 | PERF-015–025; strongest numeric cluster and existing transition review. |
| 12 | PERF-026–029; enemy ammunition and duel deadline excluded. |
| 13 | No additional ship metric; meter-long description concerns the organism. |
| 14 | PERF-030; qualitative failure/air circulation context, bomb timer not endurance. |
| 15 | No additional XGP metric; preview treasure quantity not payload specification. |
| 16 | PERF-031–033; catalyst/mode evidence and separately attributed cargo mass. |
| 17 | No additional ship metric; car travel times excluded. |
| 18 | No additional ship metric; tournament measurements excluded. |
| 19 | PERF-034; inertial-control/anchor commands are further qualitative leads without calibrated ratings. |
| 20 | PERF-035–036; combat pressure increase has no pressure value. |
| 21 | No additional ship metric; 2 km distance is a ground location. |
| 22 | PERF-037; high-gravity pickup is a visual-review lead, no flight-speed figure. |
| 23 | No additional ship metric; caster capacities are character/weapon context. |
| 24 | PERF-038–041; special Leyline context kept separate. |
| 25 | No additional ship metric; caster types/counts excluded. |
| 26 | No additional numerical ship metric in screened text; power remarks concern Leyline/magic. |

Prioritize audio/visual verification of EP-10 ETA, EP-20 boost/limit, EP-11 over-nominal output and sensor figures, and EP-24 acceleration wording before fitting a model. No absolute reactor watts, measured thrust, ship mass, propellant consumption, complete acceleration curve or validated maximum sub-ether speed was established by this audit. Authored additions remain uncommitted; complete subtitle copies remain local-only.
