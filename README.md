# ClicData Data Flow Builder

A modular reference pack for generating ClicData editor clipboard JSON. Keep the folder structure when sharing. It is intentionally not a standalone document.

Use AGENTS.md as project instructions (Codex reads it automatically). Describe the task and provide the latest flow export or local schema CSV files and user-supplied binding evidence. Connected-account access is limited to binding metadata; table records must never be queried or read. The instructions route the LLM to a small set of relevant files instead of requiring the entire reference on every request.

## Client-sensitive data: metadata only

**DO NOT QUERY DATA. Only retrieve metadata for dataset/column IDs, names and types.** No record reads, previews, samples, distinct values, counts, aggregates or profiling, including on QA/dummy tables. Never use `query_data` / `QueryData` or a record endpoint to obtain IDs. Use scoped table-name/ID discovery and the dedicated schema endpoint with minimal selected fields. If unavailable, request a metadata-only export or manual binding.

The mandatory [project instructions](AGENTS.md#sensitive-client-data-metadata-only--mandatory) contain the access rules. These are agent instructions, not a server-enforced permission restriction. Editor previews and execution remain user-performed; local fictional fixture generation is allowed.

## Task entry points

| Need | Read |
| --- | --- |
| Schema CSV input, missing bindings, offline workflow | [Schema files](reference/SCHEMA_FILES.md) |
| Processing design, edits, validation, optimization | [Build guide](reference/BUILD_GUIDE.md) |
| Clipboard envelope, graph/resource IDs, schemas, metadata | [Serialization](reference/SERIALIZATION.md) |
| Exact settings for one node | [Node catalog](reference/node-catalog.json), then only its .json and .md files |
| Theme, category colors, panels, grid, centering, captions | [Style guide](reference/STYLE_GUIDE.md) |
| Construct annotation objects | [Annotation templates](reference/annotation-templates.json) |
| Find a close complete flow | [Example selector](examples/INDEX.md) |
| Discover a missing parameter value | [Supplemental API evidence](reference/api/README.md), only when needed |
| Diagnose a failure | [Failure patterns](reference/FAILURE_PATTERNS.md) |
| Check historical claims | [Evidence](reference/EVIDENCE.md) or archive/; not routine build input |

There are 35 documented processing types and eight complete synthetic teaching patterns. A documented node is not proof of every option or runtime behavior. Forecast SSA is not documented. Example resource IDs are synthetic or historical; supply actual target bindings.

## Why we ask for IDs

Dataset and column IDs let the builder preconfigure Table Input nodes so you do not have to select the source table and fields manually. They are reference metadata; the builder does not use them to access or read client records. Verify the bindings after importing into ClicData.

## Pivot and JSON inputs

Pivot category lists and JSON structures require a manual supplement: provide a safe distinct-value list collected locally for each required pivot column, and dummy JSON examples for selected fields being extracted or expanded. Keep JSON keys/nesting/types, replace values with invented ones. Metadata-only MCP can still resolve bindings; it must never query categories or JSON records. See the [intake procedure](reference/SCHEMA_FILES.md#manual-supplement-for-pivot-and-json--applies-to-both-intake-methods).

## Normal workflow

New business flows end in dedicated **dummy Table Output nodes**, one per business result, with mapped columns and a full-refresh (`rebuild`) default. Users create/select the destination tables from these nodes in ClicData; destination IDs are not required in advance. Unbound nodes omit DataCloneRecId and need that editor step before execution. Input source bindings still require real metadata. Existing output settings remain unchanged during unrelated edits. See [Build guide](reference/BUILD_GUIDE.md#output-writes).

1. Supply one schema file per source, business requirements and any required binding evidence; see the schema-file guide. No client-data connection is required. Read only the task-specific references.
2. Patch the latest export for edits; assemble new flows with code where possible.
3. Validate the actual deliverable with `python3 scripts/lint_flow.py path/to/flow.json`.
4. Test import and data behavior separately in ClicData. Local checks do not establish engine execution.

For layout, use `python3 scripts/style_flow.py --help` after reading the style guide. Screenshots and [visual examples](reference/VISUAL_GUIDE.md) are optional appearance evidence, not required processing input.

## Reference-pack maintenance only

- `python3 scripts/test_linter.py`: linter regressions.
- `python3 scripts/validate_reference_pack.py`: all canonical synthetic examples.
- `python3 scripts/check_reference_structure.py`: routing, links, catalogs and documentation structure.
- `python3 scripts/build_reference_pack.py`: intentionally rebuilds teaching examples; overwrites canonical files. Do not run during client builds.

The complete pre-reorganization README and instructions are preserved in archive/ for provenance. Current rules live in AGENTS.md and the focused guides. Node guides retain the detailed settings and limitations from that reference; later discoveries should be added there.

This organization reduces mandatory reading; it does not establish a measured generation-time improvement.
