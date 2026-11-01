# Episode 6 — Retention Checkpoint

Historical review sections relocated on 2026-11-01 without promoting their evidence status.

## Episode 6 retention checkpoint — 2026-10-30

Status: cleanup authorized, implemented, verified and accepted by the maintainer on 2026-10-30.
All 354 gallery images retain INITIAL_REVIEW_COMPLETE: 353 SCREENED and the recurring
unknown opening craft at 005 NEEDS_RECHECK. There are no registered Episode 6 manual
supplements. This closeout preserves the recheck and all mechanism, identity and timing limits.

Before pruning, `models.py validate --current --episode 6` with the installed FFprobe passed
VERIFIED_CURRENT_EP06. The alignment finish preview found no runs and zero removable bytes,
confirming that the earlier five-run cleanup remains intact. No new search/reproduction
frames were created. The fresh no-run preview digest is
`0282b42c74d8bbf933d6dcf0a243c0255dcc63519b0c82f917531353a65c0f8f`.

The first complete format-2 archive was created with `episode_gallery.py archive --episode 6
--compression 3`, using WinRAR 7.13 x64, non-solid compression. It contains all 354 gallery
JPGs, their manifest and an empty supplemental recovery snapshot. Native RAR integrity,
staged restoration, decoding, exact inventory and hash comparisons passed before promotion.
Creation and round-trip verification took 85.860 seconds.

| Retained artifact / size | Result |
| --- | --- |
| `reference/cache/animehistory-review/archives/EP-06.rar` | 62,187,300 bytes |
| Archive SHA-256 | `7fcb881253f8fd7d460455d71b5f62473d267c090cf832102fab5ab34590bbcc` |
| Packing inputs including recovery metadata | 62,623,125 bytes |
| Compression saving against packing inputs | 435,825 bytes, approximately 0.70% |
| Receipt | `reference/cache/animehistory-review/archives/EP-06.json`; complete, format 2, gallery 354, supplements 0 |
| Contact sheets retained | All 15 PNGs, 52,085,220 bytes, plus unchanged registry |

`episode_gallery.py prune --episode 6 --progress-saved` independently restored and checked
the archive again, compared its manifest and current supplemental recovery snapshot, then
removed the expanded gallery cache. Removed cache/manifest data totaled 62,623,017 bytes;
this is separate from net compression saving because the RAR remains. No manual PNGs needed
removal. Final status: cached 0, archived images 354, archived supplements 0, contact sheets
15, unpacked bytes 0 and archive hash valid. The Episode 6 cache directory is absent. No
packing, verification, prune-verification, restore or candidate-archive leftovers remain.

All 55 protected annotation/context/locator CSV, contact-sheet/registry, alignment-plan/review
and subtitle/provenance hashes match the pre-cleanup baseline. Source media remain immutable.
No review status, association, manual-image record or timing mapping changed. Cited website
captures and existing subtitle copies retain their separate retention rules. Unrelated working
files and application attachments were not swept.

Both ImportExcel views were refreshed after pruning. The category view retains 30 tabs,
432,588 verified gallery cells, 9,204 image links, 1,326 manual cells and 4,419 alignment cells.
The context view retains five tabs, 14,252 verified cells and 2,736 links. Authored-data equality
passed. Post-refresh timing-boundary and context-overview visual checks passed;
no fresh native Office Viewer acceptance test is claimed. Routine RECORDED_UNCHECKED timing
availability is distinct from the explicit pre-prune current-media verification above.

Later full-size work uses `episode_gallery.py restore --episode 6`, followed by normal verified
prune after use. Restore gallery inputs before a fresh current-media timing verification.
Episode 7 is next in the adopted sequence and is not started automatically. Phase 3.2A
remains unstarted.
