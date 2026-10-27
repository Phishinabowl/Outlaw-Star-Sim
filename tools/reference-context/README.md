# Reference context tool — proposal

**Status — 2026-10-26:** modular tool direction and storage layout agreed; proposal documented
for review. Stage 1's [shared data contract](../../reference/indexes/context/README.md) is defined.
Stages 2 and 3's shared core, Fandom adapter and AnimeHistory adapter are implemented and passed
the bounded pilots below. Stage 4's maintained Episode 4 context tables and generated ImportExcel
view have passed the scoped checks recorded below. Stage 5 is accepted for the bounded workflow
after the maintainer reported successful native filtering and website/internal navigation checks.
The procedure's limits remain explicit; broader site coverage is not implied.

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
authorized implementation. Stages 2–3 populated the Fandom/AnimeHistory source caches and
disposable test storage; Stage 4 initialized the maintained CSVs and generated workbook.

| Location | Contents / ownership |
| --- | --- |
| `tools/reference-context/` | Shared processing, site adapters, validation, workbook generator and tests; this README owns tool usage and validation until a procedure is accepted. |
| `reference/indexes/context/README.md` | Authoritative data schema and vocabulary defined in Stage 1; future research coverage/review records belong here. Link to this tool document rather than duplicate commands. |
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

Stage 5 removed the duplicate `reference/working/fandom-export-test/` folder after verifying
that its exact XML bytes remain in the Fandom payload cache under the recorded SHA-256.
The optional live-fixture test reads that cached payload after cleanup. Cited caches remain
local-only; they are not disposable previews and must not be swept up with temporary files.

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

Stage 1 defines field names, controlled values, link-table grain and the common adapter/cache
contract in the [context-index README](../../reference/indexes/context/README.md). Exact CLI
commands remain to be implemented and validated. Prefer small modules and reuse existing reference-tool
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

## Staged implementation and acceptance

**Sequence agreed — 2026-10-26:** build and validate one adapter with the shared core before
adding the second adapter. Fandom comes first because the anonymous API and independent XML
comparison already provide a bounded validation baseline. Stages 1 and 2 are completed within the
scope recorded below. Stages 3 and 4 passed their bounded pilots; Stage 5 is accepted within
the recorded limits.

### Stage 1 — shared data contract

**Defined — 2026-10-26:** the [data contract v1](../../reference/indexes/context/README.md) specifies
ordered fields, stable IDs, relationship grain, continuity, review vocabulary and attribution rules
before maintained-table initialization. Common adapter output and cache identities accommodate
both Fandom revisions/wiki markup and AnimeHistory URL/content hashes/HTML sections. Design checks
cover existing gallery/supplement keys and the three Fandom fixtures; executable validation is
Stage 2 work. No CSVs or source content were initialized or migrated during Stage 1.

### Stage 2 — shared core and Fandom adapter

**Implemented and bounded validation passed — 2026-10-26:** see
[Stage 2 commands and evidence](#stage-2-commands-and-evidence--2026-10-26). Shared schema
validation is exercised with disposable CSV fixtures; no maintained CSVs or editorial claims have
been created. The text-only structural parser flags unresolved templates rather than rendering them.

Implement bounded retrieval, revision-aware caching, XML fixture import, source parsing and shared
validation. Compare Horus, Hilda and Outlaw Star (ship) against the existing XML export and checked
API results. Preserve mixed-continuity sections, references, infobox arguments, aliases and
unresolved templates. Validate cache reuse and repeat runs, changed revisions, cited-snapshot
retention, missing/redirected pages, malformed responses, denial/backoff and safe temporary-file
cleanup. HTTP success containing an error/challenge page must not count as article retrieval.

Record passing results and resolve failures before starting Stage 3. Validate the shared core
through this bounded end-to-end path rather than building both adapters before testing either.

### Stage 3 — AnimeHistory adapter

**Implemented and bounded validation passed — 2026-10-26:** see
[Stage 3 commands and evidence](#stage-3-commands-and-evidence--2026-10-26). Public HTML retrieval,
robots checks, sitemap deduplication, anchor selection and offline cache/reparse checks passed.
The then-current 48-test suite included all Stage 2 regressions. At that checkpoint no maintained
CSVs, workbook or editorial claims had been created; the Stage 4 results below supersede that state.

Add selected episode-summary, character and lore retrieval through the same contract. Check
section boundaries, episode links and shared-page anchors against source content; anchors must
not duplicate a page download or merge distinct sections. Validate site-specific failure handling
and run the shared validation again. Record passing results and resolve failures before Stage 4;
any shared-contract change must also pass the Fandom regression checks.

### Stage 4 — combined Episode 4 pilot and browsing view

**Implemented and bounded validation passed — 2026-10-26 (local):** see
[Stage 4 commands and evidence](#stage-4-commands-and-evidence--2026-10-26).

Use bounded Episode 4 subjects across both sites. Compare imported records to source content and
validate cross-site subject joins, separately attributed claims, stable IDs, links, duplicate
claims, unknown continuity and preservation of existing authored image/subject annotations.
Generate and reopen the ImportExcel workbook; compare saved values, row counts and hyperlinks to
maintained tables and test intended Power BI joins without building/publishing a report yet.
Review usefulness against known distinctions such as Horus versus its dropship, Gene's flashback
and missile context. Absence from a short article is not negative evidence.

### Stage 5 — procedure acceptance

**Accepted — 2026-10-26 (local):** combined checks and scoped cleanup passed as recorded
[below](#stage-5-closeout--2026-10-26). The maintainer subsequently reported successful native
filter and website/internal-link checks. Acceptance covers this bounded procedure and its stated
limitations; it does not authorize Git publication or automatically start further research.

Record the combined results, limitations and cleanup state; obtain maintainer acceptance before
describing the tool as an established procedure or using it for the remaining episode surveys.
Each stage must pass its applicable validation before the next begins; a failure is resolved in
that increment rather than carried into routine use. These technical checkpoints do not introduce
additional publication approvals or replace the established confirmation workflow. No next episode,
Phase 3.2A, modeling or gameplay starts automatically.

## Stage 2 commands and evidence — 2026-10-26

Files: `core.py` owns schema/read-only table validation, contained paths, atomic writes, OS writer
locking and immutable snapshots; `fandom.py` owns the anonymous API client, XML import and
conservative structural parser; `context_tool.py` provides the CLI. `test_context.py` uses
disposable workspace fixtures. No dependencies were installed; all Stage 2 code uses Python's
standard library. The bundled Python 3.14 runtime was used for this host's validation.

Run from the repository root with that interpreter or a suitable installed Python:

```text
python tools/reference-context/context_tool.py fetch --title Horus --title Hilda --title "Outlaw Star (ship)"
python tools/reference-context/context_tool.py fetch --refresh --title Horus --title Hilda --title "Outlaw Star (ship)"
python tools/reference-context/context_tool.py compare-xml "reference/working/fandom-export-test/Outlaw+Star+Wiki-20261026234357.xml"
python tools/reference-context/context_tool.py import-xml "reference/working/fandom-export-test/Outlaw+Star+Wiki-20261026234357.xml"
python tools/reference-context/context_tool.py reparse --title Horus --title Hilda --title "Outlaw Star (ship)"
python tools/reference-context/context_tool.py verify
python -m unittest discover -s tools/reference-context -p "test_*.py" -v
```

`fetch` accepts 1–10 unique explicit main-namespace titles, reuses checked cached content by
default, and makes no recursive requests. `--refresh` explicitly queries the current version.
Titles containing namespace separators are conservatively rejected in this pilot. Only the
documented `outlawstar.fandom.com/api.php` HTTPS endpoint is allowed; HTTP redirects and access
denials stop without alternate routes. Requests are paced at least one second between starts;
retryable network failures, rate limits, server errors and API maxlag receive at most three
attempts, with bounded backoff. Retry-After values outside the supported bounded numeric delay
stop for later retry. Responses are limited to 8 MiB, checked as JSON and validated as article
revisions. No authentication, credentials, cookies, browser control or rendered-page scraping is used.

The site's robots endpoint separately returned an automated-access challenge during preparation;
its contents were not recovered or treated as blanket permission. The adapter uses the documented
public API route already verified for these explicit text requests, not that blocked HTML route.
This pilot does not establish permission or availability for broader crawling.

`compare-xml`, `reparse` and `verify` are offline. XML imports reject external/internal DTD/entity
declarations, unsupported encodings, wrong-site exports, duplicate pages and multiple historical
revisions. Exact wikitext is preserved alongside its UTF-8 digest. Importing an older revision
does not roll the cached current-title alias back from a newer revision of the same page.
Import does not create maintained research records. `validate` is also available for the four
future maintained CSVs; until they exist, it fails explicitly rather than initializing them.

Cache layout under ignored `reference/cache/context/fandom/`:

- `manifest.json`: document/version catalogue, title aliases, receipt pointers and parser versions.
- `snapshots/<identity-hash>/`: immutable first-capture record, exact `source.txt` and file hashes.
- `payloads/<raw-sha256>.bin`: deduplicated original API/XML response bytes.
- `receipts/<receipt-sha256>.json`: method, retrieval metadata and source/payload associations.
- `normalized/<result-sha256>.json`: versioned parser results; offline reparse preserves previous
  results and raw snapshots. Changed output under an unchanged parser version is refused.
- `attempts.jsonl`: controlled failure diagnostics when CLI retrieval fails; successful catalogue
  entries are retained. `writer.lock` is an OS lock, released on process exit.

No snapshot cleanup/prune command is exposed at this stage; pinned snapshots cannot be deleted
through the tool. Atomic writes clean their own temporary files, and snapshot promotion removes
only the freshly created contained temporary directory on failure. Interrupted writes can leave
unreferenced complete cache objects; those are retained rather than swept up speculatively.

| Validation | Result / scope |
| --- | --- |
| Live anonymous API initial fetch and explicit refresh | All three articles returned successfully. Revision IDs and exact text remained equal to the manual XML fixture; refresh retained three source snapshots, not six. Source-declared rights information returned CC-BY-SA and the Fandom licensing link. |
| Exact API/XML comparison | Horus 452 characters, Hilda 18,661 and Outlaw Star (ship) 12,281; all three revisions/texts match. XML fixture SHA-256 remains unchanged from the feasibility test. |
| Parser inspection | Horus: 2 sections / 1 infobox field / 0 reference tags; Hilda: 20 / 22 / 7; XGP article: 20 / 15 / 19. Counts include the leading section and reference uses. Anime/manga headings remain separate. All three parse states are PARTIAL because templates are intentionally unresolved; raw template names/arguments are retained. |
| Offline cache repeat and XML import | All three title requests reused cache without network; XML/API captures share the same three document/version identities. Three receipts per article after initial fetch, XML import and refresh. |
| Parser regression and offline reparse | A self-closing reference initially masked following headings. Regression coverage fixed the boundary; parser v2 results are stored separately while first-capture text/results remain intact. |
| Disposable automated suite | 30 tests passed: schema/header parity, CSV round trip, source/link/UTC/status rules, missing pinned snapshots, evidence anchors, duplicate identities, nested templates, references/headings, XML bounds, redirect/missing/denied/malformed responses, bounded retries, cache corruption, changed revisions, stale imports, reparse preservation, locks, paths and interrupted promotion. Most failure conditions are simulated, not induced against the live service. |
| Preservation / cleanup | Existing gallery and supplemental CSVs have no diff. Original XML retained unchanged; no maintained context CSVs, workbook, source media or images changed. Disposable test directories and cache `.pending-*` directories are absent after checks. Ignored source cache remains available for Stage 3/4 validation. |

Limits: this is a structural wikitext reader, not a MediaWiki renderer or full syntax validator.
It does not expand templates, resolve every nested link/extension, infer continuity or identities,
verify article claims, or mark research reviewed. The XML import keeps a credit/history pointer,
not full edit histories; it does not establish complete attribution for republication of raw text.
Article title lists and source comparisons remain explicit. No maintained CSVs, workbook or Power BI
report have been generated. Stage 3 results follow; full workflow acceptance remains Stage 5.

## Stage 3 commands and evidence — 2026-10-26

`animehistory.py` implements selected public HTML retrieval and known content-container parsing,
using the same capture contract and immutable cache as Fandom. Shared changes move access outcomes
to `core.py`, verify AnimeHistory document keys against canonical URL hashes, and add read-only
`CacheSet` routing so future CSV validation can resolve pinned sources across both site caches.
No existing CSV headers, field meanings or review states changed. Standard library only; no
dependencies installed, browser automation or private/internal endpoint access.

**Input-route discovery:** searches and inspected public pages did not reveal a documented public
API or advertised full-content RSS/Atom feed. The hub's embedded JSON provides series metadata
and navigation, not the full biographies/lore. The public
[robots file](https://animehistory.org/robots.txt) advertises the
[sitemap index](https://animehistory.org/sitemap.php). Its selected
[character](https://animehistory.org/sitemap-characters.php) and
[lore](https://animehistory.org/sitemap-lore.php) inventories provide URLs rather than article text.
This is a bounded finding, not proof that no private API exists. The adapter uses these advertised
public routes, not guessed API endpoints or the disallowed `/php/` routes.

```text
python tools/reference-context/context_tool.py animehistory-discover
python tools/reference-context/context_tool.py animehistory-fetch --url "https://animehistory.org/anime/outlaw-star/#characters" --url "https://animehistory.org/anime/outlaw-star/#lore"
python tools/reference-context/context_tool.py animehistory-fetch --url "https://animehistory.org/anime/outlaw-star/characters/1050/" --url "https://animehistory.org/anime/outlaw-star/lore/ships-casters-tao/#lore-entry-3768"
python tools/reference-context/context_tool.py animehistory-fetch --refresh --url "https://animehistory.org/anime/outlaw-star/lore/ships-casters-tao/#lore-entry-3768"
python tools/reference-context/context_tool.py animehistory-reparse --url "https://animehistory.org/anime/outlaw-star/characters/1050/"
python tools/reference-context/context_tool.py show --site animehistory --article "https://animehistory.org/anime/outlaw-star/" --locator "EPISODE:04"
python tools/reference-context/context_tool.py show --site fandom --article Horus
python tools/reference-context/context_tool.py verify --site all
```

Discovery reads robots and two sitemap inventories, lists only Outlaw Star URLs, deduplicates
documents and follows none of the listed articles. It returns inventory counts/hashes on stdout;
it does not initialize research records or cache other series' articles. Fetch accepts 1–10
explicit URLs in this series' hub, numeric character-profile or lore-page paths. Different anchors
on one page share a download/snapshot. Known `#characters`, `#lore`, `#episodes`, episode anchors
and lore-entry anchors select distinct normalized sections; missing/unsupported selections fail
explicitly. Requests do not automatically follow source links, download images or execute scripts.

Fresh network work checks robots guidance first and fails closed if it is unavailable/malformed
or disallows the requested path. Receipt metadata retains the policy text/hash/time. Request
starts are paced, responses bounded to 8 MiB and 30-second timeouts, with at most three attempts
for transient failures and bounded Retry-After/backoff. Redirects are limited to selected public
paths on the two known host spellings, checked against robots guidance. Login, internal routes,
external hosts, arbitrary query URLs and encoded path tricks are refused. Robots redirects cannot
be used to request articles before policy validation. Denied/missing/malformed responses keep the
last successful cache intact; challenge/navigation pages do not count as captured source articles.

The parser extracts hub synopsis, episode summaries, character role/biography blocks and the lore
page index; standalone profiles also retain their related lore entries. Lore entries preserve
their source anchor, heading group, description, commentary labels, episode pointers and source
links. Editorial analysis is tagged `SOURCE_INTERPRETATION`, breakdowns remain separately labeled,
and unspecified commentary is not assumed factual. These are source-structure labels, not canon,
continuity or reviewed subject assignments. Missing expected fields, altered counts and repaired
nesting are flagged; ambiguous duplicate locators are refused. COMPLETE means the known selected
containers were structurally accounted for, not exhaustive website support or verified claims.

`show` is an offline reader shared by both adapters. Without `--locator`, it lists section keys;
with 1–5 explicit section/block locators, it returns that cached source content and its version
metadata for review. It makes no network requests, writes no claims and changes no review status.
`animehistory-reparse` is also offline and retains earlier raw/parser versions.

| Validation | Observed result / scope |
| --- | --- |
| Live discovery | 24 unique character URLs; 57 lore sitemap entries reduce to six unique pages. Only metadata inventories were fetched, not all 30 articles. |
| Bounded live text pilot | Hub plus Hilda (`characters/1050`) plus Ships, Casters & Tao Magic. Three distinct documents captured; hub `#characters` and `#lore` selected from one fetch. Public requests and robots checks passed. |
| Content boundaries | Hub: 52 sections (synopsis, 26 episode summaries, 24 character summaries, lore index). Hilda: profile plus five related lore entries. Lore page: seven separate anchored entries. All three have COMPLETE structural parse status in parser v2. No source facts were marked reviewed. |
| Source comparison | Hilda's hub/profile biography text matches exactly after HTML text normalization. Episode 4 retains its source episode anchor and links. Lore descriptions, analytical commentary and episode pointers remain separate blocks. |
| Cache repeat / refresh | All three documents reused cached content offline. Refresh of the same lore page with two anchors made one document request. Exact HTML changed while normalized sections stayed equal; both source versions were retained. Final cache: four AnimeHistory snapshots across three documents, plus three unchanged Fandom snapshots. |
| Shared-core/regression suite | 48 tests passed, including all 30 Stage 2 tests. Added coverage includes robots denial/malformed guidance, missing/denied pages, media types/encodings, bounded retry, redirect restrictions, URL containment, duplicate sitemap entries, section boundaries, missing layout/duplicate anchors, script/navigation exclusion, two-anchor deduplication, offline reading, changed-HTML retention and mixed-site source-row validation without authored mutations. Failure cases are mostly disposable simulations. |
| Preservation | Existing gallery/supplement CSVs and original Fandom XML unchanged. No maintained context CSVs or workbook created. No source media accessed or new episode surveyed. Test fixtures clean up inside ignored working storage; source snapshots remain ignored/local-only. |

**Limits:** page layouts are not a published API contract. The parser supports the inspected
Outlaw Star containers, not arbitrary site pages, every future layout or every possible anchor.
New pages must pass structural review before relying on their output. No license or historical
revision link is invented when the source does not declare one. Exact HTML hashes include page
boilerplate, so explicit refresh can create another version even when article text is unchanged;
default reads reuse the cache. The pilot retains those versions and does not introduce automatic
polling or deletion. Current public source availability is not a guarantee of future access.

Those results describe the Stage 3 checkpoint. Stage 4 results follow. Stage 5 still owns
acceptance of the combined procedure before further surveys; Phase 3.2A remains unstarted.

## Stage 4 commands and evidence — 2026-10-26

The bounded editorial pilot initializes four maintained CSVs under `reference/indexes/context`:
14 subjects, seven cited source versions, 18 context records and 76 relationship rows. Stable
subject IDs match the existing episode annotations; no existing image annotations were migrated
or rewritten. Fandom and AnimeHistory assertions remain separately attributed. Similarity links
identify two pairs of assertions without implying independent primary corroboration.

The source set adds one selected Fandom article, Gene Starwind, to the earlier pilot. Exact API
queries for El Dorado and Helicon missile returned NOT_FOUND; attempts are recorded locally.
This does not establish that the wiki contains no relevant information. No successful source
row was fabricated for either title. Both adapters' source caches verify: four Fandom snapshots
and four AnimeHistory snapshots, including the retained earlier lore HTML version.

| Check | Result and limits |
| --- | --- |
| Editorial states | 16 SOURCE_CHECKED, one NEEDS_RECHECK, one DRAFT. Website comparison alone remains SECONDARY_ONLY. One placement assertion is PRIMARY_CORROBORATED within the narrow scope described below. |
| Useful distinctions | Main Horus and its dropship remain distinct. Gene's escape-pod flashback has its own context; psychological interpretation is labeled separately. The wiki's Helicon spelling does not overwrite the provisional `halcyon_missile` identity or identify the initial small nose missiles. |
| Primary corroboration | CTX-000015 checks only the raised Melfina apparatus behind the forward cockpit seats against the existing visually reviewed [startup record](../../reference/indexes/episode-04-startup-review.md), especially 10:42.016 and 14:05.011. No fresh media extraction, dialogue verification, dimensions or complete layout proof is implied. |
| Deliberate uncertainty | Horus's two-jump travel statement remains DRAFT/UNKNOWN continuity without a primary episode citation. Galley existence does not establish corridor placement or side-hatch adjacency. Source template and chronology limits remain explicit. |
| Shared validation | All four CSV schemas, IDs, locators, pinned snapshots, relationships and evidence heading links pass. All 15 distinct linked image keys resolve to existing gallery/manual metadata. Five manual originals are NOT_LOCAL following the earlier accepted RAR cleanup; this check does not restore or revalidate the archive. |
| ImportExcel output | Five tabs: Overview, Subjects, Sources, Context and Links. Reopened output matches 1,329 data cells and 193 external/internal links, with tables, frozen identifiers, filters and separately displayed review/evidence states. IDs and ISO UTC values remain text. No formulas or media are embedded. |
| Visual review | Representative ranges on all five tabs rendered and inspected read-only. Inspection caught alphabetic JSON-property ordering and automatic date conversion; the builder now sets explicit display order, preserves timestamp strings and refuses unresolved internal links. Native Excel/VS Code viewer acceptance is still untested for this new workbook. |
| Repeat and regression | Repeated builds passed saved-value/link checks without modifying authored inputs. The 53-test suite includes earlier adapter/core checks plus combined projection preservation, dangling cache refusal, metadata-only source-row generation, separated bridge grains and explicit missing/corrupt supplemental media states. |
| Preservation and cleanup | Existing gallery/category/supplement CSVs have no diff; input hashes are checked during workbook generation. Original XML SHA-256 remains `d1bec92374e524b1928121a86beb4b31d812ee789effcd7408e18d5aa11b89e5`. Per-build UUID staging folders are removed; ignored workbook/preview projections, cited source caches and original XML remain local for acceptance. No source media or new episode was accessed. |

### Read and regenerate the pilot

From the repository root, use an available Python 3 interpreter and the installed ImportExcel
module (validated here with 7.8.10). The builder preserves existing output if validation fails;
close the workbook before refresh. PowerShell versions that automatically convert JSON dates
must support `ConvertFrom-Json -DateKind String` (7.5+); otherwise the builder refuses converted
timestamps rather than silently changing provenance.

```powershell
python tools/reference-context/context_tool.py validate
python tools/reference-context/context_tool.py verify --site all
python -m unittest discover -s tools/reference-context -p 'test*.py' -q
& tools/reference-context/build_context_workbook.ps1 -Python python
```

`context-review.xlsx` is an ignored/generated browsing projection; maintain the CSVs and rebuild.
Context IDs link to the Context tab, source IDs to Sources, and subject/context targets to their
records. Website links use an exact captured revision or a verified public section anchor where
available; local evidence/image links require those local files to be present. A missing manual
image is an availability state, not permission to download or restore it automatically.

For offline metadata proposals, `source-row --site fandom --article 'Gene Starwind'
--source-id CTXSRC-000007` prints source fields without editing CSVs or marking prose reviewed.
`view-data --output .tmp/context-workbook/pilot.json` validates and exports the workbook data,
input hashes and five separate Power BI bridge projections. It accepts generated JSON only under
`.tmp` or `reference/working/context`. Bridge output keeps context-to-subject, episode, image,
context and evidence relationships separate; no multiplied fact table or Power BI report was built.

Stage 4 is technically validated within this pilot. Stage 5 below records subsequent native-viewer
confirmation, cleanup and bounded procedure acceptance. No further episode survey, Phase 3.2A,
modeling or gameplay begins automatically.

## Stage 5 closeout — 2026-10-26

**Accepted — 2026-10-26 (local).** Stage 5 consolidates the validated commands below
into the proposed routine. It does not add another adapter, expand article coverage, resume episode
surveys or authorize Phase 3.2A. Following the Stage 5 closeout, the maintainer reported that all
three requested checks worked: Context review-status filtering, a source website link and subject
navigation through Links. This is maintainer-reported native-viewer evidence, not desktop-control
observation or a guarantee of compatibility with every viewer/version.

### Proposed routine

1. Select the current episode or a bounded research question. Reuse existing subject IDs and
   image keys. Check the maintained context tables and offline cache before collecting more text.
2. Retrieve only explicitly selected Fandom titles with `fetch`, or selected supported AnimeHistory
   URLs with `animehistory-fetch`. Defaults reuse checked cache; use `--refresh` only for an
   intentional current-version check. Stop on denial, malformed output or changed structure;
   investigate rather than trying alternate access routes. Manual XML is an optional fallback,
   not a recurring requirement. No account, subscription or browser-control step was needed here.
3. Inspect selected source sections using `show --site ... --article ... --locator ...`.
   Review template warnings, continuity, attribution and source interpretation labels. Generate
   metadata with `source-row` if useful; a proposed source row does not review article prose.
4. Author concise paraphrases in the four maintained CSVs. Allocate stable IDs once; link
   subjects, episodes, images, related claims and existing evidence separately. Keep source checking
   separate from primary corroboration. Record unresolved identities and draft leads explicitly;
   repeated website assertions do not establish independent evidence. Preserve existing image notes.
5. Run `validate` and `verify --site all`, then regenerate the workbook with the documented
   ImportExcel builder. Address validation errors before using the projection. Use workbook filters
   and source/record links for browsing; edit CSVs, not this generated workbook. Separate bridge
   projections are available for later Power BI work; no report is built by this routine.
6. Keep cited source snapshots and attribution metadata. Remove only identified disposable build
   or preview artifacts after validation. Episode image/RAR cleanup stays under the existing
   gallery tool's procedure; this context tool neither restores nor prunes episode media.
   Keep research changes reviewable and uncommitted until the established confirmation workflow.

### Closeout evidence and acceptance

- The combined 53-test suite passes after duplicate-XML cleanup, including the live XML comparison
  using the retained, hash-checked cached payload rather than skipping that test.
- Four Fandom and four AnimeHistory snapshots verify; all maintained tables and links validate.
  Workbook regeneration after the missile clarification again checks saved values/hyperlinks and
  authored-input preservation. No additional website fetch, image extraction or episode survey ran.
- The temporary export folder and Stage 4 workbook-preview folder were removed after checking
  absolute containment and reparse points. The exact XML digest remains
  `d1bec92374e524b1928121a86beb4b31d812ee789effcd7408e18d5aa11b89e5` in the Fandom payload cache.
  UUID build folders are removed by the builder. The finished workbook and cited caches are retained.
- The maintainer's clarification that the earlier Halcyon spelling was probably a typo is recorded
  on the subject and CTX-000014. The stable ID remains unchanged; primary terminology/equivalence
  remains a research recheck, not a tool failure or a new requirement to resolve before acceptance.
  The Horus travel statement likewise remains a draft lead. Neither blocks bounded routine use
  if those visible evidence limits are accepted.
- Maintainer viewer check passed by report: filtering Context by `review_status`, opening a
  source website link and following an internal subject target from Links all worked. The bounded
  procedure is accepted with the recorded research and tool limits. Publication still follows
  the separate Git confirmation instructions; this response did not authorize a commit or push.

Full-site support, automated fact verification, canonical Japanese missile terminology, historical
AnimeHistory revision links, web/local image-time alignment, universal viewer compatibility and
Power BI report implementation remain outside the demonstrated result. Cache contents are ignored
and host-local; a fresh checkout needs explicit selected retrieval or transfer of pinned snapshots,
not an assumption that successful cache validation will work without those files.
