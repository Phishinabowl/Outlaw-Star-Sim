# Reference reorganization — Phase 3 migration

Status: implemented, checked and accepted by the maintainer on 2026-11-01 (America/New_York).
The subsequent [Phase 4 integration/workbook validation](reference-index-reorganization-phase-4.md)
was accepted on 2026-11-01; the results below retain the Phase 3 checkpoint scope.

The [plan](reference-index-reorganization-plan.md) owns scope. The
[file/section ledger](reference-index-reorganization-ledger.md) owns original/current record paths;
the [tool audit](reference-index-reorganization-tool-audit.md) owns helper routes and dependencies.
The frozen [Phase 1.1 baseline](reference-index-reorganization-baseline.json) remains historical.

## Completed Changes

- Moved all 152 root reference records to their ledgered destinations. The root now contains its
  navigation README and collection folders rather than episode/settei/performance records.
- Moved all 33 helpers into ignored `tools/historical/local/`. Original paths are absent and all
  destination hashes match. No historical helper was executed.
- Activated the prepared routing patch after checking its recorded hash, source hashes and
  applicability. Permanent outputs use organized source/episode/performance locations; existing
  media, subtitle, cache, archive and workbook destinations retain their owners.
- Relocated 49 README parts: 47 complete sections and two ledgered mixed-content ranges. They occupy
  26 history destinations: three existing retention records and 23 new files. Dated scope,
  attribution, heading order and findings remain intact; relative links were rebased. Claims were
  not consolidated. Shared schema/parser sections remain in the AnimeHistory README; old fragments
  have explicit compatibility anchors. Episode/comparison navigation links all new history files.
- Repaired owning Markdown links and path strings in six CSV tables. Basename-only historical
  references remain unchanged where the filename still identifies the record.

Moves used explicit workspace-bounded regular-file paths, destination/reparse-point/hash preflight
and post-move hash/source-absence checks. JSON and local script bytes are preserved. Text edits used
bounded apply-patch operations; bulk CSV patches used the installed apply-patch CLI with checked exits.

## CSV Reference Changes

| Register | Rows preserved | Path-only field changes |
| --- | ---: | --- |
| `animehistory/category-index.csv` | 9,204 | 58 detail references; 641 reported-context references; 384 uncertainty references |
| `animehistory/supplemental-index.csv` | 26 | 9 uncertainty references; 4 reported-context references |
| `context/context.csv` | 81 | 1 uncertainty reference |
| `context/links.csv` | 1,278 | 2 EVIDENCE target paths; original fragment retained |
| `context/subjects.csv` | 48 | 1 notes reference to relocated cross-episode history |
| `settei/settei-screening.csv` | 221 | 81 measurements/callout reference paths |

All 1,181 changed cells were compared with original parsed values: only mapped paths changed.
Columns, row order/counts, IDs, observations, classifications, review states, timestamps and timing
values are preserved. The 30 extra uncertainty pointers beyond the filename-based audit refer to
relocated README fragments and were included in the actual repair.

## Verification Results

- All 185 source paths are absent and destinations exist. All 66 moved JSON records and all 33
  historical scripts match original SHA-256 values. Recorded commands, media paths, selection-plan
  content, recipe hashes and stored JSON review references remain intact; ledgers resolve old paths.
- All 174 protected archive/receipt, contact-sheet and subtitle files match pre-migration hashes.
  Size/modification-time metadata for 251 source files is unchanged; this is not a new full-content
  video hash check. No original media was decoded or altered.
- All three XLSX files, all locator tables and both alignment registers remain byte-identical.
- All 150 prepared authored-file outputs matched expected normalized text before final navigation
  and status edits. Relocated history content retains those prepared values.
- Maintained-project Markdown checks resolve 1,681 local links and 361 fragments without errors.
  Migration records are excluded because old paths are intentional. Third-party plugin docs are
  outside this check; two pre-existing vendor fragment discrepancies observed in the broad scan
  were left unchanged.
- Category validation passes: 9,204 images, 26 supplements; 2,111 SCREENED, 13 NEEDS_RECHECK,
  7,080 UNREVIEWED. Detail states remain 2,066 INITIAL_REVIEW_COMPLETE, 58 PARTIAL, 7,080 NOT_REVIEWED.
- Context validation passes. Alignment validation passes with 105 anchors, 12 historical mappings
  and six validated mappings; current-media verification was not performed.
- Four activated output-routing tests pass using synthetic files and mocked media processes.
- Migration-owned snapshots, generated patches and helper scripts were removed after verification;
  only the maintained routing regression test and durable migration records remain.

## Phase 4 Handoff

Full integration acceptance remains Phase 4, including workbook regeneration and equivalence checks.
Existing workbook bytes are deliberately preserved here; displayed paths and links require refresh.
No episode review, source extraction or Phase 3.2A implementation starts automatically.
The maintainer confirmed Phase 3 for publication on 2026-11-01. The original Phase 2 patch is
retained as an activation artifact and must not be applied again to the migrated checkout.
