# pivot — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="pivot"></a>

### Pivot — `pivot`

Groups by Status, pivots Agent Name across three explicit values, and counts Ticket ID. Its output schema names columns such as Ticket ID (Count) Emma Johnson.

- **Property class:** `DataFlowNodePivotProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `Aggregates`, `GroupByColumns`, `PivotedColumn`, `PivotedValues`.
- **Fixture examples:** `Pivot #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Aggregates": [
    {
      "Aggregation": "count",
      "Alias": "Ticket ID (Count)",
      "InternalType": "int64",
      "Name": "Ticket ID"
    }
  ],
  "GroupByColumns": [
    "Status"
  ],
  "PivotedColumn": "Agent Name",
  "PivotedValues": [
    "Emma Johnson",
    "John Smith",
    "Michael Davis"
  ]
}
```


## Metric-name/value source normalization — 2026-10-22

Observed pre-flow branch: Text to Columns splits a composite rows.name on comma into Date (Position=1) and Domain (Position=2), both text(250). Pivot then groups by those two fields, pivots rows.data.name over explicit values imps/pub_payout/total_traffic/participation_rate, and sums decimalstrict(28,9) rows.data.value. Exported column names combine the aggregate alias and pivot value. This is schema/configuration evidence, not execution proof, nor a reason to sum every kind of rate metric in a different task. Position indexing, delimiter/escaping edge cases, absent pivot values and date parsing still need runtime tests.
