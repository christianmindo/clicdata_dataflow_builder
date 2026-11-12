# transform-data — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="transform-data"></a>

### Transform Data — `transform-data`

Defines TransformedColumns. The example replaces Priority with an int32 CASE expression mapping High to 1, Medium to 2, and other values to 3. This differs from the added Resolution Time field in Calculate Columns.

- **Property class:** `DataFlowNodeTransformDataProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `TransformedColumns`.
- **Fixture examples:** `Transform Data #1`.

Observed node-specific settings (not a complete node):

```json
{
  "TransformedColumns": [
    {
      "Expression": "case when [Priority] = 'High' then 1 when [Priority] = 'Medium' then 2 else 3 end",
      "InternalType": "int32",
      "Name": "Priority"
    }
  ]
}
```


## Additional observed marketing pattern — 2026-10-22

Generalized source expression replacing an existing column using its incoming value. Transform Data is distinct from adding a duplicate alias in Calculate Columns. Empty-string comparison and whitespace handling are engine-sensitive; verify rather than equating them with trim.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "TransformedColumns": [
    {
      "Name": "MappedLabel",
      "InternalType": "textsimple(250)",
      "Expression": "COALESCE(NULLIF([MappedLabel], ''), 'NOT MAPPED')"
    }
  ]
}
```

## NULL replacement — user-reported working, 2026-11-12

The user confirmed the generated standalone Transform Data node works in ClicData: text NULLs use `COALESCE([Field], 'NULL')`, numeric NULLs use `COALESCE([Field], 0)`, and datetime NULLs use `COALESCE([Field], DATEFROMPARTS(1900, 1, 1))`, preserving the declared types. This is user-reported evidence for that configuration, not an independently observed engine test or proof of arbitrary expression support.

The static linter checks nonempty transformation settings, required entries, duplicate targets, output presence/types and explicit COLLATE. Connected nodes also validate incoming expression fields, target availability, source count and complete output schema propagation. Standalone fragments warn that incoming fields/schema require connection before they can be verified. Static checks do not execute expressions.
