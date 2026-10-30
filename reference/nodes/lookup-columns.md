# lookup-columns — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="lookup-columns"></a>

### Lookup Columns — `lookup-columns`

Uses two upstream nodes; LookupNodeId explicitly selects Agents as the lookup source. An equality condition matches Agent ID to Assigned To and Values requests Agent Name with an alias. Missing/multiple matches are untested.

- **Property class:** `DataFlowNodeLookupColumnsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 2.
- **Node-specific properties:** `Conditions`, `LookupNodeId`, `Values`.
- **Fixture examples:** `Lookup Columns #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Conditions": [
    {
      "ColumnName": "Agent ID",
      "Comparator": "equals",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "c735ef8b-c583-5a31-a503-1eabea438539",
      "LogicalOperator": "and",
      "ValueType": "column",
      "Values": [
        "Assigned To"
      ]
    }
  ],
  "LookupNodeId": "4fe45f3d-fb91-52f3-be3d-4aefcd509abc",
  "Values": [
    {
      "Alias": "Agent Name",
      "Name": "Agent Name"
    }
  ]
}
```


## Additional observed marketing pattern — 2026-10-22

Generalized from an observed lookup with both a column equality and literal eligibility condition. LookupNodeId and Values selection still required from the base shape. Main/lookup role follows LookupNodeId, not Sources order. InputMode=text was also observed in other conditions; optionality unverified.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "Conditions": [
    {
      "ColumnName": "LookupKey",
      "Comparator": "equals",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "64f636da-b93f-5e8d-8947-533e4151428f",
      "LogicalOperator": "and",
      "ValueType": "column",
      "Values": [
        "FactKey"
      ]
    },
    {
      "ColumnName": "EnabledFlag",
      "Comparator": "equals",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "41883e54-2022-5ac6-9ffc-0c030f5dc37d",
      "LogicalOperator": "and",
      "ValueType": "value",
      "Values": [
        "1"
      ]
    }
  ]
}
```
