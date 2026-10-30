# Building and modifying flows

Use this guide for processing changes. Read SERIALIZATION.md for new construction/graph changes and nodes/<code>.json plus nodes/<code>.md only for node types being introduced or changed. A current supplied export is the baseline for edits.

## Input contract

Use [local metadata/schema files or dummy datasets](SCHEMA_FILES.md) and user-supplied requirements/exports. Start with the use case, then take the dataset-ID or dummy-data path documented there. For dataset IDs, default to generating the Master DB metadata query for the user to run and return as a local export; reuse existing complete bindings. Never discover client data, schema, IDs or sample rows through MCP or another remote route. For JSON, first clarify the use case, required attributes/measures and row grain; suggest candidate fields to extract or unnest and agree the scope. Only then request dummified structural examples for the selected fields if needed, never every JSON column or actual client records. Keep unresolved dependencies visible, continue independent design work, and never invent IDs or runtime evidence. User-performed ClicData testing is separate from local assembly.

## Requirements intake: purpose first — 2026-10-28

When only schemas are provided and the use case/exact requirements are missing, start with a focused prompt:

“Before we choose fields, what exactly should this Data Flow accomplish? Please describe the intended use case, desired output and any business rules it must follow.”

Wait for that direction before asking downstream configuration questions or designing a specific flow. You may inspect the supplied schema structure in the meantime, but do not infer the intended business result from field names. Do not start by requesting a field list, all JSON examples, IDs or theme. This required purpose clarification is distinct from the optional table-name step.

Once the use case is supplied, continue in order, using existing answers rather than asking again:

0. Accept relevant dataset IDs or dummy datasets and follow the offline intake path in SCHEMA_FILES.md. In both cases, prompt for missing DataClone IDs (after upload for dummy datasets), then generate the user-run query to obtain column IDs, names and types. Reuse supplied IDs/bindings and continue independent requirements/design work while awaiting the export. Use returned metadata to reconcile field selections and configure Table Inputs.
1. Agree the output grain, desired fields, measures and JSON attributes/expansion needs; suggest relevant candidates from the supplied schemas.
2. Resolve material business rules: joins/keys/cardinality, filters, calculations, aggregation, duplicates and missing values.
3. Request only missing dummified JSON structures needed for the agreed fields. Follow SCHEMA_FILES.md for binding metadata or manual source selection; never request client records.
4. Resolve destination/write behavior and theme when applicable. Offer optional readable table names/labels if unknown.

Ask concise grouped follow-ups at each stage, not a comprehensive questionnaire before the purpose is known. If the user already supplied actionable requirements, proceed from them without this initial question. Continue independent work while unresolved details are discussed, but do not finalize dependent logic by assumption.

UNDERSTAND THE REQUIREMENT
Establish:
- Source datasets, actual columns, types and resource IDs.
- Output row grain: what one row represents.
- Join/lookup keys, cardinality and duplicate-match behavior.
- Filters, calculations, aggregation and null/unmatched-record handling.
- Destination, key fields and write mode when applicable.

Optional annotation naming: when readable table names or preferred labels are not already known, offer the explicitly skippable table-name step in STYLE_GUIDE.md. Continue with available names if skipped; this does not replace required source bindings.

Ask concise, grouped questions only when missing information materially affects correctness. Make reasonable routine design choices, state consequential assumptions and continue independent work. Preserve existing business rules unless I authorize changes.

BUILD THE FLOW
- Prefer the simplest supported node sequence that meets the requirement.
- Use exact node Codes, property-class identifiers, casing and nested structures from SERIALIZATION.md, matching node references/canonical example, or a current supplied export. Do not describe an observed but untested structure as working.
- Editor clipboard JSON must be a raw JSON array, without an API wrapper.
- Incoming graph connections belong in the downstream node’s Properties.Sources.
- Generate unique IDs for new objects and consistently remap all graph and nested references.
- Keep graph IDs, Table Merge internal IDs, resource IDs, schema trace IDs and condition GUIDs distinct.
- Use actual target-environment dataset and column IDs. Never copy example resource IDs into a production flow without evidence they apply.
- Reconcile fields, types, aliases, expressions and output mappings at every step.
- Do not assume Sequence controls execution or omitted metadata is regenerated.
- Handle expression escaping separately from JSON escaping. Do not assume unrestricted SQL support.
- Table Output can feed downstream nodes; do not assume it must be terminal.
- Group Rows requires at least one GroupedValues entry according to user-reported editor behavior. For distinct-key branches, use a documented count aggregate on a suitable existing field and remove the helper count afterward; retain null-key groups.
- Prefer native Combine match/settonull actions for source-specific columns. Do not add calculated NULL placeholders solely to equalize branch schemas. Preserve exact names, types, source availability and nested action references using the relevant node reference shapes.
- Check calculated aliases and extraction names against retained input fields and each other using case-insensitive normalization. Use distinct raw/helper names; capitalization alone must not distinguish fields.
- Do not change key components or product identity without checking uniqueness and business meaning. Client-specific SKU identity rules are not universal.

CHECKPOINTS AND EXPRESSIONS
- Never add or enable checkpoints. Set CheckpointType to null where included in the supported processing structure; omit CheckpointIsOutdated and CheckpointStatus from new nodes.
- When modifying an existing flow, disable legacy checkpoints and remove their status metadata while preserving processing roles and business logic. If this conflicts with an explicit exact-preservation request, explain the conflict before making that exception.
- A preview flow means ordinary editor node previews without destination writes; it does not mean CheckpointType=preview.
- Never add COLLATE clauses or explicit collation overrides. Obtain actual node error text before diagnosing a collation issue.
- Absence of COLLATE does not prevent implicit collation conflicts. Where appropriate, use verified literal prefixes plus one text field, preserving key identity; do not present that pattern as a guaranteed engine fix.
- Avoid unverified same-node alias self-references. Preserve exact documented type strings, including text versus textsimple families.

MODIFYING EXISTING FLOWS
- Use my latest supplied export as the sole baseline.
- Do not reconstruct it from an older generated version.
- Preserve IDs, connections, port sides, expressions, schemas, resource bindings and output settings except where the requested change requires otherwise.
- For styling-only edits, change annotations only.
- When spacing changes are authorized, allow Left/Top changes on processing nodes and verify all other processing properties remain identical.
- Preserve useful annotations, updating or replacing them when I request a different style.
- Keep an original baseline and prevent regeneration scripts from overwriting newer user edits.

OUTPUT WRITES
- For new business flows, finish each business-result branch with a clearly named Table Output for a dedicated dummy destination. The user's standing default is Enabled=true and ProcessMode=rebuild (full refresh), with complete SelectedColumns/OutputColumns and result-grain keys. Diagnostic branches may remain previewable checks unless their persistence is requested.
- Destination IDs are optional during authoring: the user confirmed that they create/select the output table from the Table Output node and the editor binds its ID. Omit DataCloneRecId on such unbound nodes; never use fake IDs. Keep normal graph node IDs and document the manual binding step. Do not block delivery waiting for destination IDs.
- Preserve an existing output binding and write mode during unrelated edits.
- Use the standing rebuild default only for new dummy destinations. Other destination/write-mode changes require task-specific direction. An explicit preview-only request can omit outputs; canonical teaching files retain disabled output fixtures.
- Dummy output table means a test destination; it does not anonymize the incoming rows. Generate optional fictional CSV/schema companions when requested, with exact final schemas and clearly labeled sample values.
- Creating clipboard JSON does not authorize executing it or changing remote resources.

VALIDATION
When available, run `python3 scripts/lint_flow.py your-flow.json`. Add `--require-disabled-outputs` only for teaching examples. The checker is a static aid, not proof of resource existence, import or execution.

Check as far as available tools allow:
- Valid JSON, unique object IDs and resolving graph/nested references.
- No unintended cycles or disconnected processing steps.
- Fields exist at their point of use.
- Compatible types, aliases, calculations and destination mappings.
- Preserved row grain, join multiplicity, null behavior and business rules.
- Identified environment-specific dependencies.
- Section containment and estimated node/label/panel collisions.
- Exact preservation of properties outside the authorized change scope, accounting explicitly for required checkpoint removal.
- No enabled checkpoints or checkpoint-status metadata, no explicit collations, and no case-insensitive output-name collisions.
- For width changes, align terminal conversions with Table Output SelectedColumns and OutputColumns. A wider destination does not reverse upstream truncation; physical destination resizing requires verification.

Report checks actually performed separately from checks still required. Distinguish JSON validity, editor import and engine execution. Never claim any succeeded without evidence.

OPTIMIZATION

For wide survey sources, consult the [survey dashboard pattern](patterns/survey-dashboard.md) when relevant. It covers separate submission/answer grains and a controlled Unpivot probe; do not assume null-cell preservation or count answer rows as respondents.
- Establish original behavior and relevant data counts first.
- Consider calculating or enriching at distinct-key grain, then looking results back onto the fact stream where supported.
- Preserve duplicates, nulls, dimension-match behavior and the output contract.
- Distinguish proposed improvements from measured results. Fewer logical evaluations do not establish runtime speedups or shared-branch caching.
- Compare full results as multisets, retaining duplicate multiplicity, under unchanged source snapshots and evaluation dates. Include financial totals, nulls, ties and ambiguous dimension matches.
- Benchmark equivalent full executions and output work only when authorized; limited previews and local simulations do not establish engine performance. Preserve required staging writes and dependent consumers before production adoption.
- Document suspected business-rule issues separately from performance changes.


## Reusable lessons from prior troubleshooting

- **Distinct grouping:** Group Rows needs at least one GroupedValues aggregate. For distinct keys, count an existing field, retain null groups, then remove the helper count.
- **Repeated parent IDs:** JSON-to-Rows can produce one row per nested item while retaining the parent order ID. Count distinct parent IDs for order counts; never count item rows as orders.
- **Product identity:** Ask whether equal SKU values across sources mean the same product. Keep a shared SKU when that is the agreed business definition; generate a source-specific key only when required. Do not silently change the distinct-product KPI.
- **No duplicate aliases:** Compare calculated/extracted aliases and incoming fields ignoring case. Use separate raw names for replacements. Avoid same-node references to aliases being newly calculated.
- **Implicit collation conflicts:** Even without COLLATE, CONCAT can fail when independent text columns have different inherited collations. A literal prefix plus one text column can avoid that combination where identity semantics permit it. This is not a guaranteed engine fix. Do not add explicit COLLATE.
- **Native Combine actions:** Leave source-specific columns absent on other branches and use explicit settonull actions. Validate sources/invalidSources/action references against real incoming schemas; never hide missing columns behind error=false alone.
- **Optimization:** Group expensive calculations at the appropriate distinct-key grain, then look results back onto facts when supported. Preserve duplicate multiplicity, null handling, match selection and output schema. Measure performance; do not infer a speedup from fewer nodes.
- **Layout:** Re-layout the affected component when inserting branches. Keep helper rollups near their consumers and use top/bottom ports appropriately. User-supplied positions supersede generic spacing. Validate estimated geometry separately from actual editor rendering.
- **Latest export:** For edits, the latest user export is the sole baseline. Never regenerate it from an older generator. Check an exact fingerprint excluding only fields authorized to change.
- **Text sizing:** Inspect all relevant pages and distinguish observed lengths from future domain guarantees. Preserve text/textsimple families and numeric precision. Keep destination mappings consistent with terminal type conversions. Imported metadata does not prove physical output columns were resized.
- **Financial reconciliation:** Preserve source amounts and report header/item discrepancies. Do not zero all rejected records or distribute differences across products without an approved rule.
- **Coverage:** Unavailable refunds or prices must remain unavailable, with clear coverage; do not silently replace missing financial data with zero.
- **Evidence:** Local JSON/SQL simulations, screenshots and successful import are distinct from successful ClicData execution. Document each outcome separately.

## Efficient construction workflow

1. For edits, inspect the latest input flow and identify the affected nodes/fields. Patch it; do not recreate unchanged branches or annotations.
2. For new flows, establish grain, bindings, business rules and theme. Read the relevant node references, plus at most one close canonical flow if an envelope/pattern is unfamiliar.
3. Use a small local generation script to assemble repeated envelopes, schemas, connections and IDs. Prefer structured transformations over hand-emitting thousands of repeated JSON lines. Existing build_reference_pack.py rebuilds teaching examples; it is not a general client-flow generator.
4. Use style_flow.py only for intended styling operations; it does not decide business logic or automatically authorize moving an existing layout. Read STYLE_GUIDE.md first.
5. Lint the actual deliverable once. Fix reported issues and rerun affected checks. Do not rebuild or audit the entire reference pack during routine client work.
6. Report actual checks and remaining editor tests briefly. Deliver a file rather than duplicating a large JSON array in chat.


## Many heterogeneous marketing sources

User preference, 2026-10-22: favor two flows for this class of use case. A pre-flow prepares each source in its own branch and persists separate prepared outputs; the main flow fuses them and applies shared transformations. Add a standalone staging flow only for a concrete consumer/operational need. See patterns/multi-source-mapping-and-alerts.md when applicable; do not load it for unrelated tasks. This is an architecture preference, not a measured performance claim. Agree source grain/types, missing-value policy and pre-flow-to-main freshness/failure dependencies.


Single-flow alternative (user instruction, 2026-10-22): when keeping those source preparation branches in one canvas, connect all prepared branches to one Combine Tables (`combine-tables`) node, then apply shared transformations. Do not use Table Fusion for that convergence. Table Fusion reads persisted resource tables in the two-flow architecture; Combine reads upstream processing nodes. Reconcile all branch/column pairs with documented mappings and missing-field actions.
