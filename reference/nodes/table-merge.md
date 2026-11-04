# table-merge — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="table-merge"></a>

### Table Merge — `table-merge`

Joins embedded datasets and, in the upcoming-update exports documented below, an upstream graph node. The legacy format uses internal DataClones IDs and Connections. The example uses an inner join between Agent ID and Assigned To, with ForceTableNamePrefix false. Legacy embedded input IDs differ from graph-node IDs; the connected format explicitly reuses the upstream node ID.

- **Property class:** `DataFlowNodeTableMergeProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 0 (legacy), 1 (connected exports).
- **Node-specific properties:** `Connections`, legacy `DataClones`, new `MergeInputs`, `ForceTableNamePrefix`.
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

## Connected input format — observed 2026-11-04

User-reported: the next ClicData update allows upstream nodes to feed Table Merge. Observed: two supplied clipboard exports, one inner and one right join, use `_AppVersion: "2026.5.153.0"` and Table Merge `_PatchVersion: 2`. This is export evidence, not a verified release availability or engine-execution result. Both examples feed a Table Input into Table Merge; arbitrary processing nodes, multiple upstream nodes and other join types remain unverified.

The adapted exact settings are in `table-merge.json` → `connectedInputExample`. Identifiers there are synthetic reference identities, never target bindings. The existing `exampleSettings` remains the legacy format; do not combine its `DataClones` with `MergeInputs` or silently migrate old exports.

- The downstream merge has a normal `Sources` entry: `Id` is the upstream graph node ID, `SourceSide` is `"right"`, and `TargetSide` is `"left"`.
- `MergeInputs` replaces `DataClones` in these exports. The embedded Agents input has its own internal `Id`, `ConnectorCode: "localfile"`, and `DataCloneRecId` (rather than the legacy `RecId`). Its selected output field retains a dataset-column `RecId`.
- The upstream input entry has `Id` and `SourceNodeId` both equal to the upstream graph node ID, `ConnectorCode: null`, `DataCloneRecId: 0`, and `SelectedColumns` with `RecId: 0` plus exact upstream names and types. These zeros are observed node-backed-input markers, not missing dataset bindings to invent or fill in.
- `Connections.SourceId`, `TargetId` and each condition `Parts[].Source` refer to the corresponding `MergeInputs[].Id`. Here Agents is the source and the incoming tickets node is the target. Conditions compare `Agent ID` to `Assigned To` using `Comparator: "equals"`, `LogicalOperator: "and"`, and `ValueType: "column"`. `Agent ID` is referenced by the condition even though only `Agent Name` is selected for output.
- Both exports use connection `SourceSide: "left"`, `TargetSide: "right"`. These inner-canvas sides are distinct from the outer `Sources` edge ports. `JoinType` is respectively `"inner"` or `"right"`; the latter targets the tickets side. Preserve orientation when changing join type.
- `Alias` and `Name` can differ (as in the supplied right-join export); resolve connections by IDs, not labels. `ForceTableNamePrefix` is false in both examples.
- The right-join export includes output `traceId` values; the inner-join export omits them. Do not treat traces as node/resource identities or infer that join type controls their presence. The merge emits Agent Name followed by the nine upstream ticket fields with their observed types.

Validation scope: local structural regression checks only. No remote discovery, editor import, join-result comparison or engine execution was performed. Existing legacy teaching flows have not been regenerated.

## Multi-table capacity — user-confirmed 2026-11-04

Table Merge supports joining more than two tables within one node. Join (`join-tables`) accepts exactly two upstream node inputs; use Table Merge for a multi-table join within one node, or chain binary Join nodes when appropriate.

This capacity is user-confirmed. The supplied connected Table Merge exports still demonstrate two tables and one upstream node only. No maximum table count, three-table connection topology or multiple-upstream-node serialization has been established by those exports; do not invent those details from the capacity statement.
