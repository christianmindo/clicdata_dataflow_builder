# standardize-data — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="standardize-data"></a>

### Standardize Data — `standardize-data`

Applies a rule to Status with Condition exactly, Pattern Resolved, and ReplaceWith Closed. Other conditions and precedence are unknown.

- **Property class:** `DataFlowNodeStandardizeDataProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ColumnNames`, `Rules`.
- **Fixture examples:** `Standardize Data #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ColumnNames": [
    "Status"
  ],
  "Rules": [
    {
      "Condition": "exactly",
      "Pattern": "Resolved",
      "ReplaceWith": "Closed"
    }
  ]
}
```


## Additional observed marketing pattern — 2026-10-22

Observed condition spelling and null Pattern; MappedLabel is generic. The literal fallback is a deliberate business choice, not missing-data policy for other tasks.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "ColumnNames": [
    "MappedLabel"
  ],
  "Rules": [
    {
      "Condition": "isemptyorwhitespace",
      "Pattern": null,
      "ReplaceWith": "NOT MAPPED"
    }
  ]
}
```
