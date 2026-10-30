# Example selector

These are COMPLETE raw clipboard arrays with synthetic bindings. They are generated adaptations, locally checked against hand-authored synthetic expectations; none has a claimed new ClicData execution result. Output nodes are disabled. Never copy the illustrative resource IDs/write mode into an actual task.

Read one close example only when its pattern is useful, not all examples. Use its whole envelope and nested structures, then rebind IDs and adapt fields to the supplied requirement.

| Task | Complete example | Layout |
| --- | --- | --- |
| Start here for flat input tables and simple output mapping. | [Select, rename and type fields](canonical/01-select-and-type/flow.clipboard.json) | [SVG](canonical/01-select-and-type/layout.svg) |
| Use when expanding an array while retaining parent context. | [Nested JSON lines with parent IDs](canonical/02-nested-lines/flow.clipboard.json) | [SVG](canonical/02-nested-lines/layout.svg) |
| Use for unions, matching columns and explicit missing-source NULLs. | [Combine with source-specific fields](canonical/03-combine-native-null/flow.clipboard.json) | [SVG](canonical/03-combine-native-null/layout.svg) |
| Use to prevent event expansion from multiplying the final fact. | [Event rollup and lookup](canonical/04-event-rollup-lookup/flow.clipboard.json) | [SVG](canonical/04-event-rollup-lookup/layout.svg) |
| Use this instead of Group Rows with empty GroupedValues. | [Distinct keys with a count helper](canonical/05-distinct-key-helper/flow.clipboard.json) | [SVG](canonical/05-distinct-key-helper/layout.svg) |
| Use distinct raw names and sequential nodes for dependent formulas. | [Safe calculation aliases and NULLs](canonical/06-safe-calculations/flow.clipboard.json) | [SVG](canonical/06-safe-calculations/layout.svg) |
| Use for a supported Filter Query expression and clear row filtering. | [Filter a reporting subset](canonical/07-filter-before-output/flow.clipboard.json) | [SVG](canonical/07-filter-before-output/layout.svg) |
| Use for a complete nested-array-to-common-schema pipeline with two sources. | [Two-source line dashboard](canonical/08-two-source-line-dashboard/flow.clipboard.json) | [SVG](canonical/08-two-source-line-dashboard/layout.svg) |

Each folder also contains `preview.clipboard.json` (no Table Output), `bindings.json`, `synthetic-inputs.json`, `expected-output.json`, `manifest.json`, `sections.json` and `validation.json`. Resource bindings and data are deliberately invented. An empty nested array yields no line in the local model; verify actual editor behavior for your task.

[The all-node learning fixture](qa-flow-2026-10-01.json) and [legacy ticket variants](legacy/) are secondary historical examples, not the preferred template. Their structures have been generalized, their identifiers replaced and writes/checkpoints disabled; those adapted files are not byte-for-byte editor exports. User-confirmed tests in the historical README do not establish execution of these adapted copies.

## Historical fixture limitations

The final folder audit found six static errors in `qa-flow-2026-10-01.json`: source/type mismatches in Support Tickets ALL Append, Support Tickets ALL Reload, Geocoding - Output (two fields) and Transform Nodes - Output; and an unavailable-field reference in Filter Query #1. Preserve this fixture as historical serialization evidence, not a passing construction template. See [the audit report](../reference/folder-audit.json) for exact results across all clipboard fixtures. Canonical examples are the preferred starting points.

## JSON objects versus arrays — 2026-10-22

For a single JSON object whose attributes become columns, use the [JSON to Columns settings reference](../reference/nodes/json-to-columns.json) and its matching [node guide](../reference/nodes/json-to-columns.md). This is a node-settings example, not a ninth complete canonical flow. The existing nested-lines example demonstrates array expansion with JSON to Rows; do not substitute it for object extraction. The new export establishes configuration/schema evidence and user-reported intent, not independently verified execution.

## Masking, tokenization and conditional replacement — 2026-10-22

These are UI/clipboard settings references, not additional complete canonical flows: [Mask Text](../reference/nodes/mask-text.json), [Tokenize](../reference/nodes/tokenize.json), [Conditional Find & Replace](../reference/nodes/conditional-find-replace.json). Their matching reference/nodes/<code>.md files include controls, captured nested shapes and unverified behavior. Read only the selected node guide before adapting these settings; visible UI option labels are not proof of serialized enum values.

## Large multi-source cleanup / enrichment / alerts

For a similar marketing or multi-provider metrics task, read the [mapping and alert pattern](../reference/patterns/multi-source-mapping-and-alerts.md). It summarizes an observed 125-processing-node graph and its new settings. It is a pattern guide, not a ninth canonical executable flow. Do not load the original client export for unrelated tasks.

## Survey dashboards and controlled Unpivot testing

Use the [survey dashboard pattern](../reference/patterns/survey-dashboard.md) for submission/answer grains, respondent identity and KPI counting rules. The [controlled Unpivot example](survey-unpivot-probe/README.md) includes a complete six-node synthetic probe and expected null-preserving results. It is not a new canonical reference-pack example. Numeric output evidence suggests null omission in the original test; text behavior and the synthetic adaptation's engine execution remain unverified.

