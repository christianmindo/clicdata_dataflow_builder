# table-merge — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="table-merge"></a>

### Table Merge — `table-merge`

Joins embedded dataset references using internal DataClones IDs and Connections. The example uses an inner join between Agent ID and Assigned To, with ForceTableNamePrefix false. These internal IDs differ from graph-node IDs.

- **Property class:** `DataFlowNodeTableMergeProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 0.
- **Node-specific properties:** `Connections`, `DataClones`, `ForceTableNamePrefix`.
- **Fixture examples:** `Table Merge #1`.

Observed node-specific settings (not a complete node). IDs below are synthetic adaptations; replace resource IDs with verified target bindings and remap graph/internal IDs consistently. Repeated columns are retained to preserve the observed mapping relationships.

```json
{
  "Connections": [
    {
      "Conditions": [
        {
          "Comparator": "equals",
          "LogicalOperator": "and",
          "Parts": [
            {
              "Source": "cd00eaa7-2c23-574e-9727-866b610aaf84",
              "ValueType": "column",
              "Values": [
                "Agent ID"
              ]
            },
            {
              "Source": "3321999e-fa7a-5640-916a-863e2d6905b8",
              "ValueType": "column",
              "Values": [
                "Assigned To"
              ]
            }
          ]
        }
      ],
      "Id": "8b217556-9287-5a71-9095-77c4519948b2",
      "JoinType": "inner",
      "SourceId": "cd00eaa7-2c23-574e-9727-866b610aaf84",
      "SourceSide": "left",
      "TargetId": "3321999e-fa7a-5640-916a-863e2d6905b8",
      "TargetSide": "right"
    }
  ],
  "DataClones": [
    {
      "Alias": "Agents",
      "ColumnVisibility": "all",
      "ConnectorCode": "localfile",
      "Height": 108,
      "Id": "cd00eaa7-2c23-574e-9727-866b610aaf84",
      "Left": 299,
      "Name": "Agents",
      "RecId": 900032,
      "RenamedColumns": [],
      "SelectedColumns": [
        {
          "InternalType": "textsimple(250)",
          "Name": "Agent Name",
          "RecId": 900034
        }
      ],
      "Top": 67
    },
    {
      "Alias": "Support Tickets 1",
      "ColumnVisibility": "all",
      "ConnectorCode": "localfile",
      "Height": 269,
      "Id": "3321999e-fa7a-5640-916a-863e2d6905b8",
      "Left": 50,
      "Name": "Support Tickets 1",
      "RecId": 900002,
      "RenamedColumns": [],
      "SelectedColumns": [
        {
          "InternalType": "int64",
          "Name": "Assigned To",
          "RecId": 900010
        },
        {
          "InternalType": "textsimple(250)",
          "Name": "Customer Name",
          "RecId": 900006
        },
        {
          "InternalType": "date",
          "Name": "Date Closed",
          "RecId": 900005
        },
        {
          "InternalType": "date",
          "Name": "Date Opened",
          "RecId": 900004
        },
        {
          "InternalType": "textsimple(250)",
          "Name": "Issue Category",
          "RecId": 900007
        },
        {
          "InternalType": "textsimple(250)",
          "Name": "Location",
          "RecId": 900011
        },
        {
          "InternalType": "textsimple(250)",
          "Name": "Priority",
          "RecId": 900008
        },
        {
          "InternalType": "textsimple(250)",
          "Name": "Status",
          "RecId": 900009
        },
        {
          "InternalType": "int64",
          "Name": "Ticket ID",
          "RecId": 900003
        }
      ],
      "Top": 30
    }
  ],
  "ForceTableNamePrefix": false
}
```
