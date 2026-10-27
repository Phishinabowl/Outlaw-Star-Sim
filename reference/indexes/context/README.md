# Cross-site reference context — data contract v1

**Stage 1 — defined 2026-10-26:** shared schema, identities, review vocabulary and adapter/cache
contract. Stages 2–3 implement the shared validation/cache core and both site adapters, with bounded
evidence in the [tool record](../../../tools/reference-context/README.md#stage-3-commands-and-evidence--2026-10-26).
Stage 4 initialized the maintained Episode 4 pilot: 14 subjects, seven source versions,
18 context records and 76 links. Its generated ImportExcel browsing view and scoped validation
are recorded in the [tool results](../../../tools/reference-context/README.md#stage-4-commands-and-evidence--2026-10-26).
Stage 5's [closeout and cleanup](../../../tools/reference-context/README.md#stage-5-closeout--2026-10-26)
are accepted within the bounded workflow after successful maintainer-reported native filter/link checks.
This document owns the data contract; the [tool proposal](../../../tools/reference-context/README.md)
owns implementation stages and validation. The
[implementation plan](../../../docs/implementation/vertical-slice-1-implementation-plan.md#pre-32a-checkpoint-all-episode-visual-reference-research)
owns research order and acceptance. The data contract does not imply full workflow acceptance.

## Collection boundaries and file ownership

Maintain four UTF-8 CSVs: `subjects.csv`, `sources.csv`, `context.csv` and `links.csv`.
Use the exact ordered headers defined below, one header row, RFC-style quoting, no formulas or
decorative rows. Empty optional fields mean unknown/unrecorded, not false or zero. IDs are text,
even when numeric-looking. UTC timestamps use ISO 8601 with `Z` or `+00:00`; dates never establish
review by themselves. Logical paragraphs may use quoted newlines. Schema version 1 applies to
all four files together; incompatible field/meaning changes require a documented migration.

The generated ImportExcel `context-review.xlsx` has Overview, Subjects, Sources, Context and Links
tabs. It is ignored/generated and must never become a second editable authority. Refresh derives
its data and hyperlink projections from the maintained CSVs and validated local cache metadata.
No downloaded article text is copied into a maintained table as a full article. No media is
embedded. Power BI implementation remains later work.

Raw responses, normalized source text and retrieval manifests belong under ignored
`reference/cache/context/<site>/`; disposable output belongs under `reference/working/context/`.
Existing image indexes, settei records, episode locators and archive-retention rules are unchanged.
Do not rewrite them to initialize this register or migrate their reported context automatically.

## Identity and row grain

| Table | Exactly one row represents | Primary key / uniqueness |
| --- | --- | --- |
| Subjects | One catalogued subject identity, including provisional unknown identities | `subject_id` |
| Sources | One successfully captured article/page version, shared by all its selected sections | `source_id`; also unique `(document_key, version_key)` |
| Context | One concise, independently assessable assertion attributed to one source version and location | `context_id` |
| Links | One typed relationship between a context record and a subject, episode, image, context record or repository evidence pointer | `link_id`; also unique `(context_id, relation, target_type, target_id)` |

Reuse existing lowercase snake_case subject IDs, including `xgp`, `horus`, `horus_dropship` and
provisional pirate-leader IDs. A display name or alias is not a key or proof of identity. Import
the existing subject vocabulary by validation, not by renaming its IDs. Unknown aggregate tags
remain aggregates; create a distinct provisional ID when a specific unresolved entity is needed.
Resolving a provisional identity requires reviewed evidence and an explicit migration if merging
IDs would change existing links. Do not infer anime/manga identity equivalence solely from a name.

Allocate `CTXSRC-000001`, `CTX-000001` and `CTXLINK-000001` style sequential IDs once, with a
minimum six-digit numeric suffix. Never recycle IDs, derive them from row position, or renumber
after sorting. Assign new IDs from the validated current tables under a single writer; parallel
edits require reconciliation before saving. Source IDs are distinct from existing `EXT-*` source
references. Refreshing the same document/version reuses its source ID.

`document_key` is adapter-specific, stable and independent of local paths: Fandom uses
`fandom:outlawstar:page:2691` style page IDs; AnimeHistory uses
`animehistory:url:<sha256-of-canonical-document-URL-UTF8>` with the complete lowercase digest.
Canonical document URLs exclude fragments, tracking parameters and default ports. Preserve path
case and meaningful parameters; do not merge different resources speculatively. Resolve known
redirects before assigning identity, preserving requested URLs in retrieval metadata. A URL change
without a stable page ID requires explicit alias mapping, not an automatic new/merged identity.

Fandom `version_key` is `revision:9335` style; AnimeHistory uses
`sha256:<content_sha256>`. An AnimeHistory anchor identifies a section, not another document.
Missing/denied pages do not receive fabricated successful source rows. Record attempts in the
local retrieval manifest instead. Editorial edits to a source row cannot silently change its
document/version identity or captured content hash.

## Ordered field contracts

### subjects.csv

| Field | Requirement / meaning |
| --- | --- |
| `subject_id` | Required stable existing or newly defined lowercase snake_case ID. |
| `display_name` | Required human-readable label; a provisional label is allowed. |
| `subject_type` | Required controlled value below. |
| `aliases` | Optional unique semicolon-separated search labels, no literal semicolons within an alias. Labels are not verified identity assertions. |
| `identity_status` | Required `PROVISIONAL`, `ESTABLISHED` or `AGGREGATE`; established means a curated catalogue identity, not canon verification. |
| `identification_cues` | Optional brief lookup aid; nonempty cues require an ABOUT-linked context record documenting their basis. No uncited biography or dimensions. |
| `notes` | Optional catalogue/identity limits; factual narrative belongs in context records. |

`subject_type`: `CHARACTER`, `SHIP`, `EQUIPMENT`, `WEAPON`, `MACHINERY`, `LOCATION`, `FACTION`,
`EVENT`, `CONCEPT`, `PRESENTATION`, `UNKNOWN`. Choose one primary type; classification here need
not match the image index's broad overlapping categories.

### sources.csv

| Field | Requirement / meaning |
| --- | --- |
| `source_id` | Required stable CTXSRC ID. |
| `site` | Required `FANDOM` or `ANIMEHISTORY`. |
| `document_key` | Required document identity as defined above. |
| `version_key` | Required revision/content identity as defined above. |
| `title` | Required captured article/page title. |
| `canonical_url` | Required absolute HTTPS article/document URL without fragment. |
| `version_url` | Optional actual revision permalink; do not fabricate an AnimeHistory historical URL. |
| `remote_page_id` | Fandom page ID as text; blank if not supplied by the source. |
| `remote_revision_id` | Fandom revision ID as text; blank if not supplied. |
| `remote_modified_utc` | Optional source-supplied revision time; never substitute retrieval time. |
| `captured_utc` | Required time this exact source version was first captured by this workflow. XML imports retain export/revision times separately in the manifest. |
| `content_sha256` | Required lowercase SHA-256 of exact source text encoded as UTF-8, before parser/display normalization. |
| `capture_method` | Required `FANDOM_API`, `FANDOM_XML` or `ANIMEHISTORY_HTML`. |
| `parse_status` | Required `COMPLETE`, `PARTIAL` or `FAILED`; successful capture can coexist with failed parsing. |
| `parse_warnings` | Required for PARTIAL/FAILED; concise loss/unsupported-structure description. |
| `license_name` | Optional applicable source-declared license; unknown remains blank and explained in notes. |
| `license_url` | Optional verified license link. |
| `attribution_url` | Required article/history/credit pointer for the captured content; retaining only the last editor does not establish complete authorship attribution. |
| `notes` | Optional source quality, provenance and attribution limitations. |

COMPLETE means all selected content structures within the documented parser scope were accounted
for; it does not mean every template was rendered or every factual claim is correct. Record
unresolved structures explicitly and use PARTIAL when they may hide relevant content. FAILED
content remains cached for diagnosis; it cannot supply a source-checked context record.

### context.csv

| Field | Requirement / meaning |
| --- | --- |
| `context_id` | Required stable CTX ID. |
| `source_id` | Required reference to exactly one sources row. |
| `source_locator` | Required section path, anchor or infobox field plus occurrence where needed; use `DOCUMENT` only for genuinely document-level claims. |
| `summary` | Required short paraphrase of one assertion; split independently assessable assertions into separate rows. No full-article copying. |
| `claim_kind` | Required `IDENTIFICATION`, `DESCRIPTION`, `RELATIONSHIP`, `EVENT_CONTEXT` or `INTERPRETATION`. |
| `continuity` | Required `ANIME`, `MANGA`, `ANGEL_LINKS_ANIME`, `ANGEL_LINKS_MANGA`, `OTHER`, `MIXED` or `UNKNOWN`. |
| `review_status` | Required `DRAFT`, `SOURCE_CHECKED` or `NEEDS_RECHECK`. |
| `evidence_status` | Required `SECONDARY_ONLY`, `PRIMARY_CORROBORATED`, `PRIMARY_CONFLICT` or `NOT_ASSESSED`. |
| `research_priority` | Required `UNASSESSED`, `HIGH`, `NORMAL` or `LOW`. |
| `revisit_reason` | Required for HIGH priority; specific future research/design use. |
| `uncertainties` | Required for NEEDS_RECHECK, PRIMARY_CONFLICT, MIXED or UNKNOWN continuity. |
| `authored_by` | Required identity of the person/agent recording the paraphrase. |
| `authored_utc` | Required timestamp of initial authorship. |
| `source_checked_by` | Required for SOURCE_CHECKED; preserved when a checked record later needs recheck. |
| `source_checked_utc` | Paired with source_checked_by; timestamp of the latest explicit source comparison. |
| `primary_checked_by` | Required for PRIMARY_CORROBORATED or PRIMARY_CONFLICT. |
| `primary_checked_utc` | Paired with primary_checked_by; timestamp of the documented primary-evidence assessment. |

DRAFT means a proposed paraphrase, not usable as established context. SOURCE_CHECKED means the
paraphrase and continuity were compared against the cited saved source content. It does not verify
the article against the anime. NEEDS_RECHECK keeps an unresolved interpretation discoverable;
never erase earlier notes because a new source disagrees. Primary evidence states require a
CHECKED_AGAINST link to an existing scoped evidence record identifying observations and limits.
An image alone, article citation or maintainer recollection cannot automatically set those states.
PRIMARY_CORROBORATED applies only to the assertion's documented scope, not the whole article.
SOURCE_CHECKED requires at least one ABOUT subject link and a non-FAILED source parse; relevant
PARTIAL warnings must be addressed in uncertainties or resolved before checking the claim.

Split mixed-continuity passages wherever possible. MIXED is a flagged unresolved source mixture,
not a way to treat manga information as anime evidence. Do not assign A/B/C canon categories from
secondary text. Reconstruction decisions stay in their owning design/evidence documents.
The original image-index `reported_context` and its attribution remain unchanged.

### links.csv

| Field | Requirement / meaning |
| --- | --- |
| `link_id` | Required stable CTXLINK ID. |
| `context_id` | Required originating context row. |
| `relation` | Required controlled relation from the matrix below. |
| `target_type` | Required type matching that relation. |
| `target_id` | Required stable target key or repository evidence pointer as defined below. |
| `notes` | Optional relation limits; no unsupported factual relationship between subjects. |

| relation | target_type | Meaning / target_id |
| --- | --- | --- |
| `ABOUT` | `SUBJECT` | The assertion is about this subjects.subject_id. Multiple ABOUT links are allowed. |
| `MENTIONS` | `SUBJECT` | Incidental subject mentioned in the assertion, distinct from its focus. |
| `APPLIES_TO_EPISODE` | `EPISODE` | Relevant narrative episode, e.g. `EP-04`, checked against existing locators; not necessarily where flashback events originally occurred. |
| `CONTEXT_FOR_IMAGE` | `IMAGE` | Existing `episode_id:image_id`, including `EP-04:EP-04-MAN-001` supplements. Contextual association only, not proof of visible content or exact timing. |
| `SAME_ASSERTION_AS` | `CONTEXT` | Another context ID makes the same assertion; store one pair in ascending numeric-ID order, without a reverse duplicate. Retain each source attribution. |
| `CONTRADICTS` | `CONTEXT` | Explicitly reviewed conflict with another context ID; same pair-order rule, with notes stating the conflict. |
| `CHECKED_AGAINST` | `EVIDENCE` | Repository-relative existing file path, optionally with a heading anchor, pointing to the scoped primary-evidence assessment. No arbitrary external article or naked image key. |

Do not use links to assert that a subject owns a ship or one room adjoins another. Such a
relationship is a sourced context assertion with ABOUT/MENTIONS links, not an unsourced graph
edge. Require nonempty notes for CONTRADICTS and CHECKED_AGAINST. Reject self-links, invalid target
types, missing targets and ABOUT/MENTIONS duplicates for the same context/subject. Image ranges
expand into explicit image-key links; do not store ambiguous ranges in target_id. Scene-group and
settei relationships can use existing evidence pointers in v1; add new target types only through
a documented contract extension.

## Common adapter result and cache contract

Adapters return the same structured result, not maintained CSV edits:

- `schema_version: 1`, `site`, requested URLs/titles and resolved canonical document identity;
  requested-to-resolved redirects/aliases remain explicit.
- Outcome `OK`, `NOT_FOUND`, `DENIED`, `RETRY_EXHAUSTED` or `INVALID_RESPONSE`, with diagnostics.
  Only OK creates a successful capture; parser status is a separate field. A transient error
  must not replace the last valid source or a cached successful response.
- Optional remote page/revision IDs and modification time; captured UTC; exact UTF-8 source text
  and content digest; capture method; raw response digest, byte count, final URL and media type.
  For API/XML comparisons, hash the identical decoded wikitext, not the differently wrapped payloads.
  For HTML, hash the decoded document before parser normalization and retain original response
  bytes/encoding. Raw byte hashes are separate from content hashes.
- Ordered sections containing `locator`, `heading_path`, `text`, outbound links and typed
  structural blocks as available: `PROSE`, `INFOBOX_FIELD`, `REFERENCE`, `TEMPLATE`, `OTHER`.
  Locators must distinguish repeated headings/fields and preserve source order. Mark unresolved
  templates/markup explicitly; do not silently discard their arguments or promote guessed text.
- Parse status/warnings, declared license/attribution information and parser version. Adapters may
  suggest subject matches, episode links and continuity candidates but cannot assign reviewed
  identities, author claims or set review/evidence states automatically.

Use a shared manifest and document/version snapshot storage within each site's cache. Cache paths
are projections of validated IDs/hashes, not arbitrary titles, URLs or user-supplied traversal paths.
Preserve raw payload, source text, normalized adapter result and their hashes separately. Refresh
may update last-attempt/last-success metadata in the manifest, never a pinned snapshot's identity.
Different API/XML captures of identical document/version/text share one source identity; capture
receipts retain their distinct methods and original payload hashes. A changed text digest for the
same remote revision is an error requiring investigation, not a silent overwrite.

Parsers may be rerun against retained raw data without refetching. A parser-version change creates
a separately identifiable normalized result; it cannot mutate cited raw text or authored records.
Referenced snapshots must be verified present before cleanup. A missing/corrupt snapshot is an
explicit cache-health problem, not permission to mark a source or claim verified. Keep access
attempt history locally, never credentials/cookies in CSVs, logs or published documentation.

## Validation and Power BI projections

Stage 2 implements validation against this contract before maintained data initialization. Check
headers/types/enums, unique stable keys and composite grains, paired provenance fields, SHA-256s,
document/version consistency, safe paths and exact adapter-source comparisons. Validate all link
targets against these tables, gallery/supplement keys, episode IDs or existing evidence files.
An anchor needs verification against its heading when used. Check required status-dependent fields,
evidence links and missing cited snapshots. Do not manufacture reviewer timestamps to pass checks.

Overview/browsing output may include drafts, but labels and filters must expose them prominently.
Default reusable context consists of SOURCE_CHECKED records; primary status and uncertainty remain
visible. Duplicate-source agreement is not independent corroboration. Reviewed semantic duplicate
and contradiction links are editorial; string similarity can only propose candidates.

Derive separate context-to-subject, context-to-episode and context-to-image bridge tables from
links.csv for Power BI; derive context-to-context/evidence views separately. Do not join all bridges
into one multiplied fact table. Count distinct context IDs, source IDs or image keys for the stated
metric. Subject counts overlap. Do not infer an assertion applies to every image of a tagged subject.
Join image keys to existing locators/supplements for captions, times, availability and URLs; do not
maintain duplicate timing fields here. Section links fall back to document/revision links when an
exact public anchor is unavailable. Never invent historical HTML links or assume ignored local
cache paths work in a published report.

## Stage 1 design checks and remaining work

The contract accommodates the three existing Fandom XML fixtures: numeric page/revision IDs map
to document/version identity; identical API/XML wikitext maps to one content hash; section and
infobox/reference markup stay distinct. Horus's stub status can be recorded without inventing
missing content. Hilda and XGP mixed anime/manga material requires assertion-level continuity.
AnimeHistory can use URL/content identities without fabricated revision IDs, and multiple hub
anchors share one page version while retaining separate locators. Existing gallery and manual
image keys follow the existing derived `episode_id + ':' + image_id` convention.

These describe Stage 1's schema/design checks, not runtime evidence. Stages 2–4 subsequently
implemented and tested the shared core, both adapters and the bounded Episode 4 workbook pilot;
the tool record owns those results. Existing image annotations remain authoritative. Procedure
acceptance is recorded in Stage 5. Further surveys require their own scoped continuation;
Phase 3.2A is unstarted.
