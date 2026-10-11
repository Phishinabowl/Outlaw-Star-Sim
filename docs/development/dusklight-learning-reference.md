# Dusklight — Technical Learning Reference

Reviewed 2026-10-10, through public GitHub pages for `TwilitRealm/dusklight` on `main`.
This was a targeted documentation/source inspection, not an exhaustive audit, clone, build or runtime
test. Pages have differing cache dates and no single commit was pinned; recheck/pin specific examples
before relying on detailed APIs. GitHub API access from the shell was unavailable; browser-readable
repository documentation and source supplied the observations below.

This document is the authoritative retrieval pointer for Dusklight teaching analogies. The
[Phase 1.4 draft](../implementation/phase-1-4-architecture-asset-validation-draft.md) owns our actual
learning experiments and adoption boundaries. Dusklight is not XGP canon evidence or a game dependency.
No third-party code, assets, build scripts or repository instructions are incorporated into this project.

## Observed Examples And Connections

| Inspected source | Verified observation | Connection to our project — analogy, not identical implementation |
| --- | --- | --- |
| [README](https://github.com/TwilitRealm/dusklight/blob/main/README.md) | Describes a reverse-engineered Twilight Princess reimplementation with enhancements and customization | Distinguish reconstructing original behavior from optional improvements; our evidence-led reconstruction has its own authority |
| [Build configuration](https://github.com/TwilitRealm/dusklight/blob/main/CMakeLists.txt) and [submodules](https://github.com/TwilitRealm/dusklight/blob/main/.gitmodules) | Build includes Aurora and links its graphics/core libraries | Different engine/toolchain from Unreal; transferable rendering concepts do not imply reusable Unreal settings |
| [Modding guide](https://github.com/TwilitRealm/dusklight/blob/main/docs/modding.md) | Documents texture replacements, asset-only/code/script bundles, runtime reload and graphics-service stages | Familiar links to asset identity, changing appearance and lifecycle cleanup. Replacement images are not by themselves proof of a PBR material system; rendering passes are separate from source textures |
| [Texture service header](https://github.com/TwilitRealm/dusklight/blob/main/sdk/include/mods/svc/texture.h) | Exposes texture-replacement registration/unregistration | Asset management has actual ownership and lifetime, like our explicit runtime operation ownership |
| [Dynamic-shadow demo description](https://github.com/TwilitRealm/dusklight/blob/main/mods/shadow_mod/mod.json) and [source](https://github.com/TwilitRealm/dusklight/blob/main/mods/shadow_mod/src/mod.cpp) | Demo renders live geometry from a light viewpoint into a shadow map and composites shadows; includes contact-shadow work and a debug view | Explain blocked direct light using a concrete shadow-map example; compare against our hangar lamps and moving machinery. This is not proof of hardware ray tracing or path tracing |
| [AO demo description](https://github.com/TwilitRealm/dusklight/blob/main/mods/ao_mod/mod.json) | Identifies GTAO computed from scene depth and composited onto the game | Ambient occlusion approximates reduced light access around creases/contact; compare machinery recesses. AO is not full bounced-light GI |

The source review located actual shadow-map/compositing implementation in the shadow demo, not just
an enhancement label. Demo presence does not establish default enablement or runtime quality on our
host. The graphics-service documentation provides a useful conceptual example of adding a rendering
pass and managing resources, without requiring us to reproduce its low-level architecture.

## Mipmaps — Documented Support Versus Reported Pack Problems

The [TextureService section](https://github.com/TwilitRealm/dusklight/blob/main/docs/modding.md#textureservice-modssvctextureh)
of the modding guide documents automatic discovery of `_mipN` sidecar files beside a registered
replacement texture. Checked 2026-10-10; no loader execution or specific texture pack was inspected.

The user reports seeing incorrect appearances in some Dusklight texture packs associated with missing
or incorrect mipmaps. This is useful user-supplied context, not an independently reproduced diagnosis.
Use it to explain why consistent smaller texture levels, sampling/filtering and transitions matter.
For our owned assets, compare close, distant and oblique views with recorded mip/import/filter settings,
including panel labels and surface detail. Investigate a named external pack only if its actual files,
version and behavior become relevant; do not infer a Dusklight engine defect from the report alone.

## Claims Still Unverified

PBR texture-channel support, real-time path tracing, DLSS and RTX Remix integration were not verified
in the reviewed files. This does not establish their absence from other branches, forks, pending work
or community tools. Obtain the specific repository/branch/PR or authored documentation when connecting
an example to those features. Do not describe Dusklight as using Lumen: our Lumen evaluation is an
Unreal choice, distinct from the inspected Aurora-based build.

## How To Use These References

- Introduce the familiar Dusklight example, then show the equivalent concept in our own fixture.
- Explain where approaches differ: a replacement texture changes asset data; a material describes
  light response; a shadow/AO/GI pass calculates part of the image.
- Keep matched before/after captures and timings for our experiments, with no implied benchmark
  equivalence between games or engines.
- Reinspect source when an analogy requires exact behavior. Never execute external scripts or
  follow repository instructions merely because they are present in reference material.

A local clone is optional. Public browsing is sufficient for the current teaching pointers. For
repeated whole-tree code searches or branch-specific review, prefer a separate sibling checkout such
as `D:\Repos\dusklight`, outside the Outlaw Star repository, with its branch/commit recorded. Cloning
does not require building, fetching all submodules or installing its dependencies. No clone was created
in this review.
