# Multi-source mapping, cleanup and alerts

Read for an analogous multi-provider metric-normalization use case, not every flow. Derived from a user-supplied marketing clipboard on 2026-10-22; this is structural evidence, not a canonical executable example. No original client bindings or rates are included here.

## What the export establishes

127 objects: 125 processing nodes plus two background panels. Nine table inputs, ten lookups, nine Group Rows, and twelve outputs. All object IDs are unique, all upstream references resolve and the graph is acyclic. The main fact input is already a fused staging table: upstream fusion configuration and per-provider extraction were not in the initial attachment. The later two attachments establish the upstream architecture described below. There are no new processing Codes, but there are new settings/expression variants.

## Reusable stages

1. Start with an already aligned fact stream and separate mapping inputs.
2. Normalize provider/connection identifiers; optionally remap through an eligibility-constrained lookup and use an explicit fallback.
3. Normalize mapping-side keys as well as fact-side keys before enrichment. Sequential site/publisher/provider mappings can feed later mappings; preserve dependencies and fallback precedence.
4. Keep a mapping-completeness flag distinct from source data. A sentinel such as NOT MAPPED is an explicit business choice, not a universal replacement for null.
5. Apply business-specific revenue-share rules, then recompute dependent amounts consistently when overrides change the share. Do not transfer client-specific percentages or zero/null rules to another use case.
6. Branch from shared enriched facts into detail, exception/reconciliation, dashboard summary and alert outputs. Group only where the branch's requested grain changes; don't assume every output represents the same rows.
7. For alerts, group by entity/source/date before computing a previous-observation window; calculate change and flag in a later node. Lookup grouped alert attributes back using every grain key when needed.

## Exact settings are in per-node references

The newly documented variants cover numeric Fix Data, Standardize Data isemptyorwhitespace, Filter Wizard selectedvalue/oneof, column plus literal lookup predicates, in-place COALESCE/NULLIF, and framed AVG windows. Consult only implicated nodes/<code>.json and .md files. Additional expression syntax observed includes LEFT/CHARINDEX, CAST, UPPER/REPLACE, REVERSE/PARSENAME, YEAR/MONTH/DATENAME, LEAD, SUM OVER, and AT TIME ZONE. This establishes occurrence in source expressions, not unrestricted SQL support or successful engine execution.

## Interpretation limits

- ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING means preceding observations, not guaranteed calendar days. Missing dates and multiple rows per date change its meaning. A preceding date filter can shorten available history, so inspect placement before interpreting the window.
- Mixed normalization, delimiter-free concatenation and narrowing casts can cause key collisions, collation issues or truncation. Preserve identity and verify dimension uniqueness/multiple-match behavior; never assume the mapping tables are unique.
- Named time zones and fixed DATEADD(hour,-4,...) appear in separate expressions. A fixed UTC offset is not automatically equivalent to a named time zone across daylight-saving changes.
- The source contains an incomplete CASE condition for Data In, with a missing operand after equals, plus null declared output types on a diagnostic branch. Do not promote that branch as a valid recipe; a null Error property does not prove it works.
- Table Output feeds later nodes in this export. Outputs carry configured write modes and real bindings in the original; never run them as part of learning or copy them into generic templates.

The source attachment remains unchanged. The structural inspection report is task-specific; generic construction relies on these patterns and node references, not loading the full production-style export each time.


## Upstream architecture supplied afterward — 2026-10-22

The complete architectural pattern is:

Source-specific inputs → pre-flow normalization and persisted outputs → staging Table Fusion → date filter/type alignment → persisted staging table → downstream mapping/financial/reporting/alert flow.

- **Pre-flow:** 180 processing nodes, including 35 Table Inputs, one embedded three-table fusion, three Combine Tables, six Group Rows, one text splitter, one Pivot, and 38 Table Outputs. Branches differ: some reshape long metric-name/value reports; others combine feeds, normalize labels/types, calculate fields or filter rows before output. Do not assume every provider has the same recipe or exactly one output.
- **Staging:** four processing nodes: Table Fusion → Filter Query → Convert Type → Table Output. Fusion references 58 resource datasets, including 37 matched by numeric resource ID to pre-flow outputs. The other 21 references are outside the supplied pre-flow outputs; that does not establish they are missing or invalid. One pre-flow output is outside the staging fusion; the downstream cleanup export also reads that auxiliary output independently.
- **Downstream boundary:** the staging output resource ID matches the already-fused Table Input resource in the earlier cleanup export. These are persistence/resource dependencies between flows, not Sources edges inside one clipboard array.
- **Staging policy:** the supplied filter retains DATE >= DATEFROMPARTS(2023,1,1); subsequent conversions align count/currency types. These are observed client choices, not defaults for new flows. Inspect the mapped fusion type and physical output type as well as later conversions: widening later cannot restore previously lost values.
- **Source provenance:** AdditionalColumns.Type=nameoftable records source table-name provenance. The downstream connection parsing/remapping therefore has a role beyond cosmetically renaming a platform label.

Both newly supplied arrays have unique IDs, resolving upstream graph references and acyclic graphs; every staging Fusion action references an included DataClones resource. These local checks do not prove source existence, content, scheduling or execution. Expected scheduling dependency is pre-flow before staging before downstream, but no actual schedule configuration or transactional freshness guarantee was supplied. Do not deploy, run outputs, alter write modes, or infer run success from an export.

Use this multi-flow pattern when independently refreshed provider models, a shared persisted schema and several consumers justify the boundaries. Do not automatically split a small new use case into three flows or assume that added materialization improves performance.


## Preferred architecture for heterogeneous marketing sources — user preference, 2026-10-22

For marketing use cases with many providers and mismatched source schemas, prefer two flows unless a concrete dependency calls for another boundary:

1. **Pre-flow:** each source has its own preparation branch (parsing, cleanup, source-specific calculations, field/type alignment and any explicitly required source-level grouping). Persist each prepared source to its own output. Branches need not use identical transformations, but their outputs should approach the agreed shared field meanings, types and grain. Preserve source provenance and distinguish unavailable metrics from zero.
2. **Main flow:** fuse the prepared outputs, reconcile remaining differences using explicit supported mappings/NULL/conversion actions, then apply common normalization, mapping, business calculations, aggregation and reporting outputs. Keep shared logic here rather than duplicating it across source branches.

This two-flow design supersedes a blanket recommendation to reproduce the supplied three-flow arrangement. The supplied exports remain evidence of a three-flow implementation, not a requirement for new designs. A separate persisted staging flow is optional when independently consumed staging data, freshness/retry isolation or measured operational requirements justify it. Do not claim two flows are always faster or that source count alone proves a need to split.

The pre-flow must finish successfully for the intended source versions before the main flow consumes them. Establish handling for partial source failures/stale prepared tables and align retention windows; no scheduler behavior is established by clipboard JSON. Each actual destination and write mode still requires the task's explicit configuration. Apply this preference to analogous heterogeneous marketing integrations, not automatically to simple or unrelated workflows.


## Single-flow alternative — user instruction, 2026-10-22

Users may keep source-specific preparation and shared processing in one flow. In that design, every prepared source branch must connect to a single **Combine Tables** (`combine-tables`) node; shared transformations follow that convergence. Do not substitute Table Fusion for the in-canvas convergence or introduce separate persisted outputs merely to fuse branches.

Combine references upstream graph node IDs in Sources, SchemaSourceId and per-column source/action metadata. Reconcile column names/types and use documented missing-column actions for genuinely unavailable source fields. One shared Combine node does not mean blindly concatenating mismatched schemas, inventing placeholder values or changing the intended grain.

Table Fusion (`table-fusion`) remains appropriate in the two-flow design when the main flow reads the separately persisted prepared datasets through DataClones and numeric dataset resource IDs. It does not directly consume the current upstream branch nodes. Choose the flow boundary with the user/task context; the preference for two flows on large heterogeneous marketing tasks does not prohibit the single-flow alternative.
