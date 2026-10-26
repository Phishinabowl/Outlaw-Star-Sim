# Reference context tool — proposal

**Status — 2026-10-26:** modular tool direction and storage layout agreed; proposal documented
for review. Bounded Fandom access tests passed. No reusable tool, context tables, workbook or
data migration has been implemented. This is not yet an operating procedure.

## Purpose and ownership

Collect selected AnimeHistory and Outlaw Star Wiki article text and support concise, attributed
research context for the episode surveys and later reconstruction. Reduce repeated ad hoc helpers
and manual exports without downloading either entire site. Coverage includes characters, ships,
equipment/weapons, machinery, locations, factions and events useful to the long-term game.

This document owns the proposed tool, storage and validation design. The
[implementation plan](../../docs/implementation/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research)
owns execution order and acceptance. The existing
[AnimeHistory index contract](../../reference/indexes/animehistory/README.md) continues to own
image annotations and survey progress. Context records supplement those observations; they do
not replace evidence reviews or the [canon policy](../../docs/canon-policy.md).

## Proposed storage

All paths below are repository-relative. Create operational directories and files only during
authorized implementation; the present change adds this proposal only.

| Location | Contents / ownership |
| --- | --- |
| `tools/reference-context/` | Shared processing, site adapters, validation, workbook generator and tests; this README owns tool usage and validation until a procedure is accepted. |
| `reference/indexes/context/README.md` | Future authoritative data schema, vocabulary, research coverage and review rules; link to this tool document rather than duplicate commands. |
| `reference/indexes/context/subjects.csv` | Maintained subject IDs, names, aliases, types and concise identification cues. Reuse existing image-index subject IDs. |
| `reference/indexes/context/sources.csv` | Maintained source/article identities, URLs, relevant sections and cited revisions; distinguish retrieved revision metadata from editorial notes. |
| `reference/indexes/context/context.csv` | Maintained concise claims, source pointers, continuity, uncertainty and review/verification provenance. |
| `reference/indexes/context/links.csv` | Maintained typed relationships connecting claims, subjects, episodes and image records as appropriate. |
| `reference/indexes/context/context-review.xlsx` | Generated multi-tab ImportExcel browsing view of the shared tables; explicitly Git-ignore during implementation. |
| `reference/cache/context/animehistory/` | Ignored local source text/responses and retrieval metadata. Separate from the existing gallery cache. |
| `reference/cache/context/fandom/` | Ignored local API responses, optional XML inputs and retrieval metadata. |
| `reference/working/context/` | Ignored disposable fixtures, comparison output and intermediate files. Authoritative records must not depend on this directory. |

Use one cross-site research collection and one workbook, not separate files per character, article
or episode. Existing gallery indexes, caches, RAR archives and contact sheets retain their current
locations and retention procedure. Do not reorganize unrelated reference files.

Cache by stable source/page identity and revision or content digest, with a manifest for current
retrievals. Repeated retrieval of unchanged content must not create duplicate snapshots. Preserve
snapshots cited by maintained research; deletion of uncited obsolete snapshots needs an explicit,
validated cleanup operation. A changing remote page must not overwrite the only copy of a cited
revision. Keep raw article text and responses local-only; publish only reviewed condensed research
and necessary attribution through the normal confirmation workflow.

The test XML currently in `reference/working/fandom-export-test/` remains a temporary fixture.
Move or delete it only in an explicitly scoped implementation/cleanup step after validation.

## Proposed architecture and workflow

- A shared core validates identities, source metadata, hashes, links and table relationships;
  manages cache reuse and refresh; and produces browsing/report projections.
- An AnimeHistory adapter selects episode summaries, character sections and lore articles,
  preserving headings, links and source boundaries. Hub anchors may identify sections of one
  page rather than separate articles. Do not duplicate downloads for those anchors.
- A Fandom adapter uses the public MediaWiki Action API for selected article text and revision
  metadata. XML export import remains a supported fallback/test input, not a recurring manual task.
- Deterministic collection/parser operations remain separate from editorial interpretation.
  Retrieval does not mark a claim reviewed, establish an identity or promote secondary prose to
  verified anime/settei evidence. Unsupported templates or incomplete parses must be visible.
- Before each episode, select its summary and relevant subjects, reuse existing context, then
  retrieve only missing or explicitly refreshed articles. Review useful new claims and preserve
  source links. Expand by encountered subjects rather than recursively crawling all links.
- Use bounded explicit selections, an identifiable client, request pacing, caching, timeouts and
  bounded retry/backoff. Respect robots/access rules and API service errors; stop on an access
  denial. Do not route around restrictions with alternate hosts, proxies or browser fingerprinting.
  Browser automation is not required by the verified API route.
- Refresh produces reviewable proposed source/claim changes. Never overwrite maintained notes,
  image annotations, attributed recollections or contradictions with generated summaries.

Exact CLI commands, field names, controlled values and link-table grain remain to be finalized
before initializing the data. Prefer small modules and reuse suitable existing reference-tool
patterns without refactoring unrelated gallery tooling. No new dependency installation is approved.

## Data and evidence requirements

Use stable text keys, UTF-8 CSV, explicit types and ISO 8601 UTC retrieval/review timestamps.
The workbook is a generated view, authored with the installed PowerShell ImportExcel module.
Power BI must join through subject, source, claim, episode and image identities rather than local
paths or display names. Relationships must have documented grain and valid targets; independent
many-to-many associations must not multiply counts or imply unsupported subject/detail links.

Record a concise paraphrase, source section/revision and continuity for each useful claim. Retain
article and revision links, retrieval date/hash and applicable attribution/license metadata.
Keep anime, manga, Angel Links and other material distinguishable at claim/section level, including
mixed articles. Unknown continuity stays explicit. Two secondary sites repeating a claim do not
establish independent primary verification.

Secondary-source reporting, observed image content, attributed maintainer context, original-source
verification and reconstruction proposals are separate statuses/provenance. Do not assign a canon
category solely because a secondary article asserts a fact. Link original episode/settei evidence
when checked; preserve disagreement and uncertainty. Do not silently assign proper names to the
currently provisional pirate-leader IDs. Cache retention is not evidence verification.

## Access feasibility evidence — 2026-10-26

Fandom documents selective [XML export](https://community.fandom.com/wiki/Help%3AImporting_and_exporting_pages)
and use of the [MediaWiki API](https://community.fandom.com/wiki/Help%3ANamespaces).
The upstream [Revisions API](https://www.mediawiki.org/wiki/API:Revisions) describes article-text
retrieval; [API etiquette](https://www.mediawiki.org/wiki/API:Etiquette) informs request behavior.

- The browsing service returned HTTP 402 for article pages and reported robots restrictions;
  its API/export opens were also unavailable. These results did not establish that an account,
  subscription or browser automation was necessary for public API access.
- A maintainer-run browser export yielded valid MediaWiki XML with Horus, Hilda and Outlaw Star
  (ship), one revision each. XML SHA-256:
  `d1bec92374e524b1928121a86beb4b31d812ee789effcd7408e18d5aa11b89e5`.
- The first shell API attempt failed DNS inside the network sandbox. A scoped authorized network
  retry returned HTTP 200 JSON anonymously for Horus; a second request retrieved all three titles.
  No credentials, browser cookies, account login, payment or browser automation were used.
- Read-only comparisons found identical revision IDs and exact text equality between API and XML:

| Article | Page ID | Revision ID | Text characters |
| --- | --- | --- | --- |
| Horus | 2691 | 9335 | 452 |
| Hilda | 2048 | 9440 | 18,661 |
| Outlaw Star (ship) | 2159 | 9123 | 12,281 |

Tested request shape: `https://outlawstar.fandom.com/api.php` with `action=query`,
`prop=revisions`, explicit `titles`, `rvprop=ids|timestamp|content`, `rvslots=main`,
`format=json` and `formatversion=2`. The three-title comparison also used `redirects=1`
and `maxlag=5`. This proves bounded public text retrieval on this host, not full adapter correctness,
all-page access, future availability or automatic service-policy compliance for arbitrary requests.
Article text retains infobox arguments, references and wiki links; template definitions and image
binaries are not included. Horus is a short stub, not a truncated retrieval.

## Proposed pilot and acceptance

1. Finalize the table contract and vocabulary, then implement the shared core and site adapters.
2. Use bounded Episode 4 subjects and existing access-test fixtures. Check AnimeHistory section
   boundaries and Fandom mixed-continuity text, references, aliases and unresolved templates.
3. Validate cache reuse, revision changes, cited-snapshot retention, explicit missing/redirected
   pages, malformed responses, service denial/backoff and safe temporary-file cleanup. Never
   interpret an HTTP success containing an error/challenge page as successful article retrieval.
4. Compare selected imported records to source content; validate stable IDs, links, duplicate
   claims, unknown continuity and preservation of existing authored image/subject annotations.
5. Generate and reopen the ImportExcel workbook; compare saved values, row counts and hyperlinks
   to maintained tables and test intended Power BI joins without building/publishing a report yet.
6. Review usefulness against known Episode 4 distinctions such as Horus versus its dropship,
   Gene's flashback and missile context. Absence from a short article is not negative evidence.
7. Record actual validation and obtain procedure acceptance before describing this proposal as an
   established workflow. No next episode, Phase 3.2A, modeling or gameplay starts automatically.
