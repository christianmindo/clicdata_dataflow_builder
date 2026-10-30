# find-replace — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="find-replace"></a>

### Find & Replace — `find-replace`

Defines ColumnNames and Find/ReplaceWith pairs. One example introduces hyphens into priority labels; another replaces Linda with Chris. Substring versus whole-value matching and case sensitivity are untested.

- **Property class:** `DataFlowNodeFindReplaceProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ColumnNames`, `Replacements`.
- **Fixture examples:** `Find & Replace #1`, `Find & Replace #2`.

Observed node-specific settings (not a complete node):

```json
{
  "ColumnNames": [
    "Priority"
  ],
  "Replacements": [
    {
      "Find": "High",
      "ReplaceWith": "Hi-gh"
    },
    {
      "Find": "Low",
      "ReplaceWith": "L-ow"
    },
    {
      "Find": "Medium",
      "ReplaceWith": "Med-ium"
    }
  ]
}
```
