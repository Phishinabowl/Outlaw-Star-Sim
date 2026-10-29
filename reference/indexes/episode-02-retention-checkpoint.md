# Episode 2 survey closeout and retention checkpoint

Date: 2026-10-28 (America/New_York).

Status: initial annotated survey accepted by the maintainer; authorized episode-level cleanup
completed and verified. Archive creation, staged recovery and independent pre-prune recovery passed.
The maintainer confirmed this checkpoint for publication on 2026-10-28. No next episode or
Phase 3.2A work is included.

## Survey coverage and retained limits

All 354 sampled AnimeHistory Episode 2 gallery images have INITIAL_REVIEW_COMPLETE annotations:
353 SCREENED and one NEEDS_RECHECK, locator 003's unidentified opening ship/launch-site view.
Batches 01–02 were accepted previously; remaining batches 03–05 and clarification follow-ups
were accepted during this closeout. This is sampled-gallery review, not complete video coverage,
full text translation or acceptance of a reconstructed design.

The survey preserves Horus/dropship distinctions, Melfina case/awakening continuity, the childhood
flashback, Blue Heaven docking/market/hotel, Swanzo, McCoy and the ambush. The tall mechanic's
Mikey identification remains an unverified lead. The final yellow mechanical opponent's operator,
model and exact blue-tool function remain unassigned. These bounded unknowns remain in image
notes rather than being silently resolved by closeout.

Accepted ALNMAP-000004 provides local = web - 1.286 s navigation for whole-second web labels
[103,1360), covering gallery 001–348. Gallery 349–354 remains unmapped. The current-input check
passed as VERIFIED_CURRENT_EP02 before pruning. Alignment tables remain at 43 total anchors and
four mappings across the reviewed episodes. The Episode 2 finish preview found no remaining
image runs and zero removable alignment bytes; no alignment evidence needed discarding.

## Verified archive

The established gallery tool created a complete format-2 archive at
`reference/cache/animehistory-review/archives/EP-02.rar`, with receipt
`reference/cache/animehistory-review/archives/EP-02.json`. Both remain ignored/local-only.

- Payload: 354 gallery JPEGs, gallery manifest and supplemental recovery metadata. Episode 2
  has zero registered manual supplements; no unregistered attachment is assumed archived.
- Archive SHA-256: `411cc7c39ef519821395f0235e4b88af46422547ed6f11f6c32ffed0b5292657`.
- Input: 61,969,565 bytes; RAR: 61,505,246 bytes; saving 464,319 bytes, approximately 0.75%.
- WinRAR 7.13 x64; compression level 3, non-solid. Archive/round-trip operation: 77.484 s.
- Native integrity testing and staged recovery passed exact inventory, image decoding and hashes
  before archive promotion. The tool recorded verification at 2026-10-29T02:12:59.890588Z.

JPEG compression savings are modest. Removing the redundant expanded cache leaves the archive
as the recoverable original-image store; the 15 contact sheets remain available for browsing.

## Cleanup and preservation

The pre-cleanup expanded gallery/manifest occupied 61,969,457 bytes. The preservation baseline
records SHA-256 and size for 20 maintained inputs: category and supplemental CSVs, both alignment
CSVs, all 15 contact sheets and their registry. Sheets plus registry total 51,033,327 bytes.

Prune independently recovered and verified the archive again, compared the current manifest and
supplement inventory, then removed the expanded gallery folder. Final status: cached 0, archived
gallery 354, archived supplements 0, contact sheets 15, archive hash valid, unpacked bytes 0.
Removal reclaimed 61,969,457 bytes of redundant expanded data while retaining the RAR. No candidate
RAR, packing, verification or restore directory remained. Only the tool's persistent lock marker
remained in the episode cache scope; the alignment working scope contained its writer-lock marker.

All 20 pre/post preservation hashes and sizes matched. Review states, the 003 flag, alignment
tables and sheet bytes are unchanged. No source videos, settei, subtitle copies, website context
caches or maintained evidence records were removed. There were no registered Episode 2 manual
supplements to prune; future registered supplements remain governed by the same archive contract.

Both ImportExcel views were refreshed with authored-data equality checks. The category workbook
verified 432,588 gallery cells, 9,204 gallery links, 510 manual cells and 1,785 alignment cells.
The context workbook verified 6,994 cells and 1,284 links. Routine view refresh did not repeat
the media check; the explicit VERIFIED_CURRENT_EP02 check above supplies that evidence.
Temporary preservation helper/baseline files were removed after verification. Git whitespace
checks passed. Source and derivative media remain local-only and are not staged or published.

## Recovery on demand

Run `python tools/reference-extraction/episode_gallery.py restore --episode 2` to recover
originals for a full-size recheck. After review, run the same tool with
`prune --episode 2 --progress-saved` to remove expanded copies again. Omit `--remove-sheets`
to retain contact sheets. Restore does not overwrite maintained annotation CSVs.
