# Todo Tree And Working Annotation Standards

## Purpose And Authority

Use Todo Tree as a small source-local intake and navigation layer for follow-ups, defects,
questions, assumptions, workarounds, review needs and verification needs. It is not the project
backlog, evidence register or phase checklist. This convention applies to maintainers and coding agents.

Adapted from the user-supplied LoTM working convention for this repository. The
[canon policy](../canon-policy.md), approved Reconstruction / Implementation Baseline v1 and
[implementation plan](../implementation/vertical-slice-1-implementation-plan.md) retain authority.
An annotation does not approve a phase, resolve research or authorize installation/publication.

## Eligible Locations And Editor Behavior

Use annotations beside a precise implementation or contract location that will remain useful:

- Executable source and configuration formats that support comments.
- Maintainer-facing architecture, planning and reconstruction documents.
- Later project-owned Blender scripts and Unreal C++ source, when those work scopes are approved.

Do not annotate immutable source media, extracted frames/subtitles, quoted dialogue, source
transcriptions, evidence records or generated exports. Route research follow-ups to
`docs/reconstruction/open-questions.md` and link the existing evidence record. Never alter evidence
wording merely to create a Todo Tree entry. Do not add comments to JSON or binary assets; place a
useful annotation in the owning script or maintainer document instead.

Tracked `.vscode/settings.json` owns the editor configuration. The ignored local workspace file points
to the repository without duplicating settings; both folder-open and workspace-open use the same
configuration. Avoid overriding it with another copied settings block in the workspace launcher.

Todo Tree uses `workspace` scan mode (workspace and open files), groups by parenthesized owner,
and respects configured file/search exclusions plus explicit annotation exclusions. Source media,
generated reference/Unreal outputs, local/editor working folders and the `reference` tree are excluded
from its scan. The latter remains searchable through ordinary text search where applicable.
This standards document is excluded so its examples do not become live work items.

Markdown phase checkboxes remain normal checklist syntax. `[ ]` and `[x]` are deliberately absent
from Todo Tree's tag list; do not add them to restore task highlighting.

## Format And Supported Tags

Use this format; tracking is optional for local work:

```text
TAG (OWNER): TRACKING - concise source-local explanation.
```

Use ASCII punctuation, end complete statements with a period, and keep the indexed line specific
enough to understand without the originating conversation. Put supporting context in continuation
comments using the host file's valid syntax. In Markdown, use an HTML comment:

```markdown
<!-- QUESTION (UNASSIGNED): Decide the provisional bridge-to-engineering connection.
     Contract: docs/reconstruction/open-questions.md; implementation Phase 1.2.
-->
```

| Tag | Meaning |
| --- | --- |
| `TODO` | Small source-local follow-up. |
| `FIXME` | Known incorrect, unsafe or unreliable behavior. |
| `QUESTION` | Unresolved requirement, design or ownership decision. |
| `ASSUMPTION` | Deliberately unverified premise; identify its validation trigger or consequence. |
| `HACK` | Intentional temporary workaround; explain why it exists and when to revisit it. |
| `REVIEW` | Source, contract or interpretation needs human judgment. |
| `VERIFY` | Behavior or assertion needs explicit testing or confirmation. |

Use only these tags unless a recurring need warrants updating this standard and editor settings.
When an assumption is disproven, resolve its dependent work or convert it to a defect annotation.
When verified and still useful, move it to an ordinary explanation or the owning contract rather
than leaving it permanently open.

Example for a later approved implementation surface:

```cpp
// VERIFY (OWNER): Confirm stale motion callbacks cannot complete readiness after reset.
//   Validation: VS1-S03; retain an actual regression case if a failure is found.
```

## Ownership And Evidence Boundaries

Before public issue promotion, use identity-neutral ownership:

- `OWNER`: the repository owner is responsible.
- `UNASSIGNED`: no local owner has been selected.

Do not insert private names, guessed public handles or agent identities as durable owners.
Todo Tree extracts the parenthesized value as a subtag for grouping.

Annotation tags are work status, not evidence categories. `VERIFY` does not establish A/B/C
evidence; resolving `REVIEW` does not authenticate a production scan. D/E/F remain non-canon.
Unclear Japanese stays unresolved rather than guessed. An accepted reconstruction/gameplay
choice belongs in the owning decision record with its E/F classification, source references and
validation limits. A source-local assumption comment is not a substitute for that record.

## Route Work To Its Durable Owner

| Information | Authoritative home |
| --- | --- |
| Slice phases, dependencies, validation and acceptance status | `docs/implementation/vertical-slice-1-implementation-plan.md` |
| Project stage and later directions | `docs/roadmap.md`, pointing to the detailed plan |
| Unresolved research or source-verification needs | `docs/reconstruction/open-questions.md`, linking evidence records |
| Source observations, provenance and classification | Existing authored reference/evidence records; no annotation backlog inside them |
| Baseline spatial/motion/operational/scope amendment | Owning document under `docs/reconstruction/baseline-v1/`, with explicit review |
| Stable architecture, tooling or interoperability rule | Owning document under `docs/architecture/` |
| Precise local defect/reminder/verification anchor | Annotation at the eligible source/contract location |
| Private untriaged idea | Ignored `.local/` notes; inbox only |
| Agreed durable public engineering tracking | GitHub Issue, with a useful source annotation if appropriate |

Avoid disconnected copies. An annotation may point to an owning plan/question/issue when its exact
location is useful. Do not turn every plan checkbox or known research question into another annotation.
Permanent testing requirements belong in the validation contract and later relevant executable tests.

## GitHub Promotion And Reconciliation

Recommend promotion when work needs public coordination, scheduling, substantial design discussion,
acceptance criteria or durable tracking beyond the current increment. Drafting a proposal is allowed;
creating, assigning, commenting on, closing or otherwise modifying an issue requires an explicit user
request. Normal approved Git publication is separate from issue management.

Use `[GH-PENDING]` only after promotion has been agreed but before the issue exists:

```python
# FIXME (OWNER): [GH-PENDING] - Startup status reports completion before machinery stops.
```

After verifying the actual issue and assignment, include its number and full URL. Use an exact public
handle only if that account is assigned. An unassigned issue retains `UNASSIGNED` and no assignee line:

```python
# FIXME (UNASSIGNED): GH #<number> - Startup status reports completion before machinery stops.
#   Issue: https://github.com/Phishinabowl/Outlaw-Star-Sim/issues/<number>
```

These placeholders are examples, not claims that an issue exists. For an assigned issue, replace the
owner with `@<verified-handle>` and add `Assignee: https://github.com/<verified-handle>` on a continuation
line. Never infer a number, handle or assignment. The issue owns public work status/assignment; project
contracts still own requirements and canon classification. Keep source links and assignment current.

Remove linked annotations when the source work is complete, the location no longer exists or the
maintainer requests removal. An issue closed while source work remains requires reconciliation,
not silent deletion of the reminder.

## Agent And Review Workflow

1. Add only durable, useful source-local information; do not annotate internal reasoning or work
   that should simply be completed in the current authorized change.
2. Use questions/assumptions instead of silently resolving unknown requirements or inventing canon.
3. Route consequential findings to their owning records and link any retained annotation.
4. Review touched annotations for current meaning, ownership and tracking; resolve or revise them
   with the change that addresses the work.
5. Before increment/branch closure, reconcile outstanding items and report annotations added,
   changed or removed. Keep deferred work explicit without expanding the authorized scope.

## Validation Status

This repository currently uses the written convention and editor configuration. No annotation linter,
fixture suite or CI enforcement has been installed or implemented. LoTM's executable policy and
workflow are possible later tooling references, not commands that work in this repository.

For now, review tag/owner syntax, valid host-file comments, placement, tracking references and routing
in the intended diff. Check settings JSON and keep tags/exclusions aligned with this standard.
Editor configuration has been checked against the installed Todo Tree schema; actual visual behavior
in VS Code remains a user-observed check. Do not claim automated enforcement or verified issue state
from a syntax-only review.
