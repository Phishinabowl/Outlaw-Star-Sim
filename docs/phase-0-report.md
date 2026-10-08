# Phase 0 report

Historical bootstrap snapshot. Tool/media/Git absence and counts below describe Phase 0, not the
current checkout. See the [roadmap](roadmap.md) and [implementation plan](implementation/vertical-slice-1-implementation-plan.md)
for completed Phase 1.1–1.3 planning, later source reviews and the unstarted implementation boundary.

## Completed

- Initialized a local Git repository; no files staged or committed.
- Created project documentation, architecture requirements, canon policy, reconstruction indexes/matrices, and next-phase roadmap.
- Protected immutable sources and generated media with .gitignore.
- Inventoried 221 JPEG scans and 28 episode-folder files (26 numbered episodes, pilot MKV, SFV).
- Recorded scan SHA-256 hashes and dimensions; generated eight local contact sheets.
- Screened all scans and marked 57 XGP-relevant records; contextual/uncertain records remain separate.
- Individually reviewed selected bridge, engineering, passage, lounge, Assault Shooter, and airlock scans, plus two misleading non-XGP locations.
- Identified Episode 4 uniquely by filename; documented future metadata/frame/scene workflow.

## Findings

Useful material extends beyond img023–048. Lounge configuration drawings at img088/089, built-in equipment at img100, Assault Shooter at img125/192, and airlock interior at img126 expand the initial evidence base. Many later scans appear to repeat earlier subjects; visual similarity is not proof of identical files or identical design revision.

The preliminary rest-room sheet img043 is marked first draft. Its status is preserved rather than treated as final production canon. Similar doors and rooms in other ship/location drawings must not be silently assigned to XGP.

The engineering drawing img030 shows four circular units, with one extended service/control cylinder. The brief's Episode 4 observations still require video review. No final deck plan or metric reconstruction was derived.

## Tooling gap and limits

Bundled Codex Python/Pillow ran the initial inventory and image generation successfully. The initial sandbox PATH check did not expose the user's Python installation; subsequent user-environment verification confirmed Python 3.14.6 and Pillow 12.3.0 were already installed. The user then installed FFmpeg/FFprobe 9.0.1 Essentials and ImageMagick 7.1.2-30 Q16-HDRI x64; all were verified working. Unreal/Blender development setup is a later-phase decision, and their installation status was not audited.

No source media was altered. No episode decoding/extraction, tool installation, Unreal initialization, modeling, gameplay code, or commits occurred. Screening is complete at thumbnail level; full Japanese transcription, source provenance, image revision comparison, and anime corroboration remain proposed next-phase work.

## Verification

Rechecked all 221 scan SHA-256 digests against the generated manifest; all matched. Rechecked all 28 episode-folder file sizes; all matched (episode bytes were not hashed). CSV contains 221 screening rows and 57 XGP-relevant records; eight contact sheets exist. Git check-ignore confirms both source types and contact sheets are ignored; git ls-files is empty.

Git initialized under the sandbox account. Running Git as the desktop user triggers an ownership trust warning. Verification succeeded with a command-scoped safe.directory exception for this exact workspace; no global Git configuration was changed. Resolve the desktop user's repository trust/ownership during tool setup.
