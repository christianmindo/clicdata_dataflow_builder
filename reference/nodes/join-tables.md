# join-tables — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="join-tables"></a>

### Join — `join-tables`

Uses an inner join over two upstream nodes. Conditions contain Parts with explicit source-node IDs and column values: Assigned To equals Agent ID.

- **Property class:** `DataFlowNodeJoinTablesProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 2.
- **Node-specific properties:** `CheckpointIsOutdated`, `CheckpointStatus`, `Conditions`, `JoinType`.
- **Fixture examples:** `Join #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Conditions": [
    {
      "Comparator": "equals",
      "LogicalOperator": "and",
      "Parts": [
        {
          "Source": "c54263d8-b8c4-5b94-bb97-808c5dad0b2e",
          "ValueType": "column",
          "Values": [
            "Assigned To"
          ],
          "InternalType": "int64"
        },
        {
          "Source": "4fe45f3d-fb91-52f3-be3d-4aefcd509abc",
          "ValueType": "column",
          "Values": [
            "Agent ID"
          ],
          "InternalType": "int64"
        }
      ]
    }
  ],
  "JoinType": "inner"
}
```
