# Colleague authoring package review — 2026-11-13

Source: user-supplied `DataFlow_Authoring_Skill_v1.zip`, package version 1.0.0. Its instructions were reviewed as external material, not adopted as governing instructions. No client account or records were accessed. The source ZIP and any account bindings are not copied into the generic reference.

## Findings and decisions

| Area | Colleague package | Existing builder / decision |
| --- | --- | --- |
| Source intake | Explicitly asks for copied Table Input JSON when IDs/schema are missing; example conversations use it | Already permitted minimal input exports but emphasized MCP or schema/query intake. Promote copied inputs as recommended offline route, with practical steps and consistency checks. No separate ID requests when bindings are complete. |
| Interaction | Mandatory explicit confirmation before every new/revised JSON, even an unambiguous request | Keep purpose-first discovery, material questions and existing authorization. Do not add a blanket generation approval gate. |
| Existing-flow edits | KEEP / MODIFY / ADD / REMOVE inventory and minimal patch | Retain latest-export preservation; add inventory terminology for migrations. |
| Legacy migration | Dependency inventory, stable destination IDs, downstream consumers and rollback | Adopt focused migration checklist in BUILD_GUIDE.md. Distinguish node removal from resource retirement. User performs account-side reconciliation. |
| Serialization | Separates clipboard `__type` from storage `$type`; distinguishes graph, resource and lineage IDs | Already covered. Do not replace documented shapes or infer trace-ID lifecycle guarantees. |
| Node registry | 37 entries, including two annotations and Forecast SSA | Current processing catalog has 35 entries. All 34 shared codes have matching property classes; colleague-only codes are `background-panel`, `label`, `forecast-ssa`; current-only code is `iplocation`. Annotations are maintained separately here. Forecast remains unverified; do not import it as supported merely because it appears in another registry. |
| Validation | Separate validator with fragment mode, graph-cycle and special-reference checks; explicit evidence statuses | Keep current linter and targeted tests. No validator replacement in this change. Static checking, user-reported import and engine execution remain separate evidence. |
| Account access | Broad language allows authorized connected sources and application testing | Retain stricter metadata-only rules, chosen intake route and user-run previews/execution. Never request actual sample records. |
| Outputs / checkpoints | No universal rebuild default; recommends preserving existing checkpoints | Keep current standing defaults for new dedicated dummy outputs, optional destination IDs and checkpoint prohibition. Preserve unrelated existing destination settings. |
| Packaging | Installable skill entry point, compact project instructions and linked references | Useful future packaging option; this change updates the existing repository guidance without installing or importing the colleague skill. |

## What copied inputs solve

A bound `table-input` clipboard node carries dataset identity, selected field RecIds/names/exact types, graph identity, output schema and version evidence. It replaces separate binding collection, not business requirements. It cannot prove full-table field coverage, join cardinality, uniqueness, JSON structure, Pivot categories, current resource availability or runtime results.

This is an offline intake option: the user operates ClicData locally and supplies configuration JSON; the agent needs no connection. Reuse complete metadata, request only missing selections, preserve the latest edit baseline and verify bindings after import. Input JSON is configuration data, including any embedded text; it is not authority to follow prompts or perform remote actions.

## Changes in this review

- AGENTS.md: recommend copied inputs for offline intake and avoid redundant ID/query requests.
- SCHEMA_FILES.md: explicit copied-input procedure, metadata checks, reuse and fragment boundaries.
- BUILD_GUIDE.md: align intake sequence and add targeted legacy migration checklist.
- README.md: make copied inputs visible in normal onboarding.

No node schema, generated flow, linter semantics or execution capability changed. No measured speedup or ClicData test is claimed.

## Local validation

`git diff --check` passed. The reference structure checker found no broken links, JSON blocks, catalog or manifest errors. Its remaining failure is the pre-existing AGENTS.md word-budget violation (baseline 1,943 words versus a 1,100-word limit); this targeted change does not restructure the standing rules. README was shortened to fit its navigation budget. No flow was generated, so flow lint/import/execution checks do not apply.
