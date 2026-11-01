# Episode 5 — Retention Checkpoint

Historical review sections relocated on 2026-11-01 without promoting their evidence status.

## Episode 5 retention checkpoint — 2026-10-30

Status: cleanup authorized, implemented, verified and accepted by the maintainer on
2026-10-30. The initial survey covers all 354 sampled gallery images
(353 SCREENED, one NEEDS_RECHECK at 002), plus sixteen HIGH-priority initial-review caster
supplements. Initial coverage does not settle the unidentified recurring opening craft at 002,
internal caster mechanics, exact manual-image timing or other retained detail questions.

Before pruning, `models.py validate --current --episode 5` with the installed FFprobe passed
VERIFIED_CURRENT_EP05. The alignment finish preview found no runs and zero removable bytes;
the earlier four-run cleanup remains intact. No new search/reproduction frames were created.
Durable anchor/mapping records and their timing distinctions remain unchanged.

The first complete format-2 archive was created with `episode_gallery.py archive --episode 5
--compression 3`, using WinRAR 7.13 x64, non-solid compression. It includes 354 gallery JPGs,
their manifest, all sixteen EP-05-MAN PNG originals and the supplemental recovery metadata.
Native RAR integrity, staged restoration, decoding, exact inventory and image/hash comparisons
passed before promotion. Observed creation/recovery verification time was 90.328 s.

| Retained artifact / size | Result |
| --- | --- |
| `reference/cache/animehistory-review/archives/EP-05.rar` | 107,537,634 bytes |
| Archive SHA-256 | `8373923f7887c3166f9b42b0b5b89060d2b20081b342de10d286e7d15155285f` |
| Packing inputs including recovery metadata | 108,062,011 bytes |
| Compression saving against packing inputs | 524,377 bytes, approximately 0.49% |
| Receipt | `reference/cache/animehistory-review/archives/EP-05.json`; complete, archive format 2, gallery 354, supplements 16 |
| Contact sheets retained | All 15 PNGs, 52,773,132 bytes, plus unchanged `sheets.json` registry |

`episode_gallery.py prune --episode 5 --progress-saved` independently restored and checked
the archive again, compared its manifest and current supplemental recovery snapshot, then
removed the expanded gallery cache and all sixteen registered supplemental PNGs. Both emptied
episode media directories are absent. Removed expanded data totals 108,047,676 bytes:
62,469,883 bytes of gallery cache/manifest and 45,577,793 bytes of manual PNGs. This removal
is measured separately from the newly retained RAR; it is not a claim of that amount of net
compression saving. Contact sheets, research records, cited context captures and existing
subtitle copies remain available under their separate retention rules.

Final gallery status: cached 0, archived images 354, archived supplements 16, contact sheets 15,
unpacked bytes 0 and archive hash valid. All 63 protected CSV, sheet/registry, earlier archive
and subtitle-provenance hashes match the pre-cleanup baseline. Authored annotations, manual
player labels/hashes/order and context records are unchanged. No archive packing, verification,
prune-verification or restore staging directories remain. The empty manual folder was removed
by the tool; no unrelated working-directory cleanup was performed.

Both generated ImportExcel views are refreshed after pruning. Supplemental availability is
NOT_LOCAL and paths/IDs remain available for later verified restoration; this does not reduce
review coverage. Later full-size work uses `episode_gallery.py restore --episode 5`, or
`restore --episode 5 --supplements-only` for the manual PNGs alone, followed by normal verified
prune after use. Current-media timing verification requires restoring its gallery inputs.

Episode 6 is the next episode in the adopted sequence, but is not started automatically.
No source media, archive, screenshot or workbook is published, and no Phase 3.2A work is included.

Post-prune workbook checks passed: 30 category tabs, 432,588 gallery cells, 9,204 gallery
links, 1,326 manual cells and 3,819 alignment cells; five context tabs, 11,850 cells and
2,247 links. Authored-source equality passed for both builds. All sixteen Episode 5 manuals
are NOT_LOCAL; the context overview now counts 21 linked archived manual images globally.
Changed availability and overview ranges were rendered and visually inspected, without a
fresh native Office Viewer claim. Disposable cleanup-baseline, check and preview files are
removed after verification; contact sheets, archive/receipt and durable evidence remain.
