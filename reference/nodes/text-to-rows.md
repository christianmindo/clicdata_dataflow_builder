# text-to-rows — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="text-to-rows"></a>

### Text to Rows — `text-to-rows`

Splits Priority using delimiter `-`, with output ColumnName Split. Empty tokens and preservation of other columns require execution checks.

- **Property class:** `DataFlowNodeTextToRowsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ColumnName`, `Delimiter`, `SourceColumn`.
- **Fixture examples:** `Text to Rows #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ColumnName": "Split",
  "Delimiter": "-",
  "SourceColumn": "Priority"
}
```
