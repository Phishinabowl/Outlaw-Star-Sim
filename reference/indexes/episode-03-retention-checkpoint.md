# Episode 3 survey retention checkpoint

Date: 2026-10-29 (America/New_York).

Status: initial survey accepted in commit 515773f; separately authorized episode cleanup
completed and verified. The maintainer confirmed this retention checkpoint for publication
on 2026-10-29. No next
episode or Phase 3.2A work is included.

## Coverage and retained limits

All 354 sampled Episode 3 gallery images retain INITIAL_REVIEW_COMPLETE annotations:
353 SCREENED and one NEEDS_RECHECK, locator 005's recurring opening launch-site/vessel
identity. Provisional character-name leads, mechanism questions and the high-value 347
hiding-asteroid display remain in the accepted annotations. This is sampled-gallery survey
completion, not full video coverage or acceptance of a reconstructed design.

ALNMAP-000006 remains unchanged: local = web -1.4845 seconds over web-label domain
[107,1381), covering gallery 002–352 with ten direct intervals and 341 mapped estimates.
Gallery 001 and 353–354 remain unmapped. The alignment finish preview found no remaining
image runs and zero removable bytes; no alignment cleanup apply or new media verification
was needed. Anchor and mapping registers retain 59 and six total rows respectively.

## Verified archive and recovery

The established gallery tool created a complete format-2 archive at
`reference/cache/animehistory-review/archives/EP-03.rar`, with receipt
`reference/cache/animehistory-review/archives/EP-03.json`. Both remain ignored/local-only.

- Payload: 354 gallery JPEGs, gallery manifest and supplemental recovery metadata.
  Episode 3 has zero registered manual supplements; no unregistered attachment is assumed archived.
- Archive SHA-256: `073bf540944bd6b488c46ebca2aa4f663dfe69e9370dbe2815be7f418ab87a1f`.
- Input: 64,204,277 bytes; RAR: 63,800,869 bytes; saving 403,408 bytes, approximately 0.63%.
- WinRAR 7.13 x64, compression level 3, non-solid. Archive/round-trip operation: 85.219 s.
- Native integrity testing, staged recovery, exact inventory, image decoding and hash checks
  passed before promotion. Receipt verification time: 2026-10-30T00:04:39.285813+00:00
  (2026-10-29 in the project timezone).

Prune independently recovered and verified the archive again, then compared the current
manifest and supplement inventory before removing expanded images. Final status: cached 0,
archived gallery 354, archived supplements 0, contact sheets 15, archive hash valid,
unpacked bytes 0. Removing the redundant expanded gallery/manifest reclaimed 64,204,169 bytes.
The modest JPEG compression saving is separate from this removal of duplicate expanded data.

## Preservation and verification

All 53 pre/post preservation hashes and sizes matched: maintained CSVs under the index tree,
15 Episode 3 contact sheets and their registry. Sheets plus registry retain 52,914,693 bytes.
Review notes/statuses, locator identities, alignment records and sheet bytes are unchanged.
No source video, settei, subtitles, website context cache or maintained evidence record was removed.
There were no registered Episode 3 supplemental originals to prune.

No candidate RAR, packing, verification or restore directory remains. Episode alignment scope
contains only its persistent writer-lock marker; the gallery scope retains its persistent lock
marker. Temporary preservation helper/baseline files are removed after verification.

Both ImportExcel views were refreshed. Category generation verified 432,588 gallery cells,
9,204 image links, 510 supplemental cells and 2,463 alignment cells. Context generation
verified 9,046 cells and 1,684 links. Both builders checked authored-data equality. No annotation
or layout changed, so the prior rendered-view checks remain applicable; no fresh native
Office Viewer test or current-source-media verification is claimed. Git whitespace checks passed.

## Commands and recovery on demand

Executed with the installed bundled Python and WinRAR:

```text
python tools/reference-extraction/episode_gallery.py status --episode 3
python tools/reference-alignment/finish.py --episode 3
python tools/reference-extraction/episode_gallery.py archive --episode 3
python tools/reference-extraction/episode_gallery.py prune --episode 3 --progress-saved
```

Run `python tools/reference-extraction/episode_gallery.py restore --episode 3` for a later
full-size recheck. After review, use `prune --episode 3 --progress-saved` to remove expanded
copies again. Omit `--remove-sheets` to retain contact sheets. Restore never overwrites the
maintained annotation CSVs. The tool's existing containment/reparse checks constrain cleanup
to its owned episode cache and registered selected-episode supplements.
