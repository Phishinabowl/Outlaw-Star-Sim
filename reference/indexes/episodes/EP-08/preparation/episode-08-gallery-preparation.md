# Episode 8 Gallery Preparation

| Field | Value |
| --- | --- |
| Date | 2026-11-01 |
| Episode | EP-08 — Forced Departure |
| Status | Download and contact-sheet verification complete; accepted by the maintainer 2026-11-01 |
| Locator scope | 354 images, IDs 849251–849604, web labels 00:01:43–00:23:04 |

The maintained gallery tool downloaded all 354 indexed images and generated 15 chronological
contact sheets. Final status reports zero failed and zero missing images. Cache validation
decoded originals and verified manifest hashes/inventory. JPEG payload totals 55,110,549 bytes;
expanded cache including manifest totals 55,522,199 bytes. The cache remains local under
`reference/cache/animehistory-review/EP-08/`. No Episode 8 RAR exists at this checkpoint.

Contact sheets are local under `reference/contact-sheets/animehistory-review/EP-08/`.
Independent verification checked every sheet's registry hash, 1600 × 2056 dimensions and
complete ordered image-ID/web-time/source-hash mapping against the locator CSV and cache
manifest. All 354 locators occur exactly once; the final sheet has 18 images. Sheet PNGs
total 48,144,086 bytes, excluding the registry. First, middle (169–192) and final sheets
were visually inspected for readable labels and image presentation.

Command: `python tools/reference-extraction/episode_gallery.py prepare --episode 8`, using
the installed bundled Python/Pillow runtime. Scoped network-enabled execution completed
successfully without reported download failures. No browser automation, installation or tool
modification was required. The task-owned independent verification helper was removed afterward.

All 354 gallery annotation rows remain UNREVIEWED / NOT_REVIEWED. This preparation is not
an annotated survey or a local-video timing association. Existing targeted Episode 8 evidence
and source media remain unchanged. Next steps are subtitle/selected website context, independent
Episode 8 alignment and bounded three-sheet review batches. Phase 3.2A remains unstarted.
