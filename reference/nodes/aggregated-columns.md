# aggregated-columns — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="aggregated-columns"></a>

### Aggregate Columns — `aggregated-columns`

Uses two upstream nodes and explicitly selects the grouped node through AggregatedNodeId. Matches Assigned To and requests maximum of Ticket ID (Count) with an alias. Row retention and unmatched behavior need verification.

- **Property class:** `DataFlowNodeAggregatedColumnsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 2.
- **Node-specific properties:** `AggregatedNodeId`, `Aggregates`, `Conditions`.
- **Fixture examples:** `Aggregate Columns #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Conditions": [
    {
      "ColumnName": "Assigned To",
      "Comparator": "equals",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "c0bbc51a-345b-52d2-abf8-729c15b63c71",
      "LogicalOperator": "and",
      "ValueType": "column",
      "Values": [
        "Assigned To"
      ]
    }
  ],
  "AggregatedNodeId": "84477db4-b82a-5ab4-8019-21b141c9fbea",
  "Aggregates": [
    {
      "Aggregation": "maximum",
      "Alias": "Ticket ID (Count) (Max)",
      "InternalType": "int64",
      "Name": "Ticket ID (Count)"
    }
  ]
}
```
