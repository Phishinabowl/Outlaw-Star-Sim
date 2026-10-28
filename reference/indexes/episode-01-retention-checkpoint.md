# Episode 1 survey retention checkpoint

Date: 2026-10-28 (America/New_York).

Status: Episode 1 pending batches 04–05, code-reading follow-up and verified retention checkpoint
accepted by the maintainer on 2026-10-28. The eight unresolved rechecks remain open.

## Survey coverage and open questions

The initial survey covers all 354 sampled AnimeHistory Episode 1 gallery images: 346 SCREENED
and eight NEEDS_RECHECK, with 296 INITIAL_REVIEW_COMPLETE and 58 prior targeted PARTIAL records.
The eight flags are locators 011–014 and 016–018 (tentative launch-site/craft identity), plus
350 (case-code O/0 transcription). VSDO2C is the maintainer's tentative reading; the subtitle,
screen and secondary transcription variants remain documented. This is sampled-gallery coverage,
not complete video coverage or acceptance of a reconstruction. Phase 3.2A remains unstarted.

## Verified archive

The existing gallery tool created the first Episode 1 format-2 archive at
`reference/cache/animehistory-review/archives/EP-01.rar`, with its external receipt at
`reference/cache/animehistory-review/archives/EP-01.json`. Both are local-only ignored files.

- Payload: 354 gallery JPEGs, their manifest, EP-01-MAN-001 PNG and supplemental recovery metadata.
- Archive SHA-256: `7671735d3681651aa4c8fabab849d43f6a373f9fe2fbacd0012d85c10d9b06b6`.
- Input: 63,496,157 bytes; RAR: 62,978,197 bytes; compression saving: 517,960 bytes (about 0.82%).
- WinRAR 7.13 x64, compression level 3, non-solid; archive/round-trip verification took 69.125 s.
- Native integrity test and staged recovery passed with exact inventory, decoded-image and hash
  checks before archive promotion. The supplemental recovery snapshot preserves its original
  bytes, player timestamp and contextual gallery association; it does not establish exact alignment.

Compression is modest for already-compressed images. Removing redundant expanded originals is
the principal storage benefit. Contact sheets remain outside the archive for routine browsing.

## Alignment boundary

Before gallery pruning, `models.py validate --current` returned VERIFIED_CURRENT_EP01 for the
pinned inputs. The episode-finish preview found no remaining image runs and zero removable
alignment bytes. Only the existing one-byte writer-lock marker remained in the episode working
folder; no decoded imagery or failed/unregistered run required removal. Twenty-five anchors and
two mapping records remain unchanged. Unsupported timing regions remain unmapped.

## Cleanup result

Prune independently recovered and verified the archive again, compared its manifest and current
supplement metadata/hashes, then removed the expanded gallery folder and registered manual PNG.
Final tool status: cached 0, archived gallery 354, archived supplements 1, contact sheets 15,
archive hash valid, unpacked bytes 0. No candidate RAR, packing, verification or restore directory
remained. Expanded gallery/manifest occupied 60,722,405 bytes; the supplement occupied 2,772,871
bytes. Removing both reclaimed 63,495,276 bytes of redundant expanded data.

Pre/post SHA-256 checks matched all 20 preserved files: the category and supplemental CSVs,
both alignment CSVs, all 15 contact sheets and their registry. Retained sheets/registry total
51,091,835 bytes. Source videos, source settei, subtitle copies, website context caches and
prior evidence records were outside the pruning scope. The eight rechecks and review depths
remain unchanged. Batches 04–05 and this retention result were accepted together on 2026-10-28.

Both ImportExcel workbooks were refreshed with authored-data equality checks. Saved category
checks covered 432,588 gallery cells, 510 manual cells, 1,029 alignment cells and 9,204 gallery
links; context checks covered 3,191 cells and 504 links. The saved EP-01-MAN-001 row reports
NOT_LOCAL. Helper/baseline files used for the preservation check were removed after verification.
Git diff whitespace checks passed. No source or derivative media is staged or published.

## Recovery on demand

Use `episode_gallery.py restore --episode 1` to recover the originals when a full-size recheck
is needed. After that review, use `prune --episode 1 --progress-saved` to remove the expanded
copies again. Retain sheets by omitting `--remove-sheets`; the separate `cleanup` command is not
the normal retention operation. Restoring never overwrites maintained annotation CSVs.
