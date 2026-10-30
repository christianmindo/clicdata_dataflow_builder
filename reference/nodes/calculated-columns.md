# calculated-columns — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="calculated-columns"></a>

### Calculate Columns — `calculated-columns`

Defines named expressions with explicit output types. Examples add `Resolution Time` using `DATEDIFF(day,[Date Opened],[Date Closed])` and a literal `Story` string.

- **Property class:** `DataFlowNodeCalculatedColumnsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `CalculatedColumns`.
- **Fixture examples:** `Calculate Columns #2`, `Calculate Columns #1`, `Calculate Columns #2 #1`.

Observed node-specific settings (not a complete node):

```json
{
  "CalculatedColumns": [
    {
      "Expression": "DATEDIFF(day,[Date Opened],[Date Closed])",
      "InternalType": "int32",
      "Name": "Resolution Time"
    }
  ]
}
```


## Additional observed marketing pattern — 2026-10-22

Generalized observed window expression. Counts up to 30 preceding rows excluding current row, not automatically 30 calendar days. Grain, missing dates, duplicate dates/order ties and short-history policy require validation.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "CalculatedColumns": [
    {
      "Name": "Previous30Average",
      "InternalType": "double",
      "Expression": "AVG(CAST([Measure] AS FLOAT)) OVER (PARTITION BY [SourceKey], [EntityKey] ORDER BY [Date] ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING)"
    }
  ]
}
```
