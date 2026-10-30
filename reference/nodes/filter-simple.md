# filter-simple — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="filter-simple"></a>

### Filter Wizard — `filter-simple`

Uses structured Filters. The example compares Agent Name to a selected value with equals/and; includes Guid, Disabled, DisabledIfNull, and an empty Groups array.

- **Property class:** `DataFlowNodeFilterSimpleProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `Filters`.
- **Fixture examples:** `Filter Wizard #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Filters": [
    {
      "ColumnName": "Agent Name",
      "Comparator": "equals",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "182b28f9-9f98-5696-96a3-d9aa662a4853",
      "LogicalOperator": "and",
      "ValueType": "selectedvalue",
      "Values": [
        "John Smith"
      ]
    }
  ]
}
```


## Additional observed marketing pattern — 2026-10-22

Observed Comparator=oneof and ValueType=selectedvalue; synthetic choices/field/GUID. Source also uses ValueType=expression for date comparisons. No complete flow or execution guarantee.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "Filters": [
    {
      "ColumnName": "SourcePlatform",
      "Comparator": "oneof",
      "Disabled": false,
      "DisabledIfNull": false,
      "Groups": [],
      "Guid": "19f84d9f-e396-5348-81e4-285b5aaf7907",
      "LogicalOperator": "and",
      "ValueType": "selectedvalue",
      "Values": [
        "SOURCE_A",
        "SOURCE_B"
      ]
    }
  ]
}
```
