# filter-query — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="filter-query"></a>

### Filter Query — `filter-query`

Stores an expression. Examples are `[Assigned to] = 2` and `[Date Opened] >= DATEFROMPARTS(2023,10,7)`. The first differs in capitalization from Assigned To; successful parsing/execution and case sensitivity are not established.

- **Property class:** `DataFlowNodeFilterQueryProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `Expression`.
- **Fixture examples:** `Filter Query #1`, `Filter Query #1 #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Expression": "[Assigned to] = 2"
}
```
