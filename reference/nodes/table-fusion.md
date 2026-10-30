# table-fusion — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="table-fusion"></a>

### Table Fusion — `table-fusion`

Combines referenced datasets with column matching. The example maps `Ticket Status` to `Status` using `matchto`, with `MatchedColumnsOnly: true`. Its datasets are embedded in `DataClones`; it has no upstream graph sources.

- **Property class:** `DataFlowNodeTableFusionProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 0.
- **Node-specific properties:** `AdditionalColumns`, `Columns`, `DataClones`, `MatchedColumnsOnly`.
- **Fixture examples:** `Table Fusion #1`.

Observed node-specific settings (not a complete node). IDs below are synthetic adaptations; replace resource IDs with verified target bindings and remap graph/internal IDs consistently. Repeated columns are retained to preserve the observed mapping relationships.

```json
{
  "AdditionalColumns": [],
  "Columns": [
    {
      "Actions": [],
      "InternalType": "int64",
      "Name": "Ticket ID"
    },
    {
      "Actions": [],
      "InternalType": "date",
      "Name": "Date Opened"
    },
    {
      "Actions": [],
      "InternalType": "date",
      "Name": "Date Closed"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Customer Name"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Issue Category"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Priority"
    },
    {
      "Actions": [],
      "InternalType": "int64",
      "Name": "Assigned To"
    },
    {
      "Actions": [
        {
          "Action": "matchto",
          "DataCloneRecId": 900001,
          "MatchedColumnName": "Ticket Status"
        }
      ],
      "InternalType": "textsimple(250)",
      "Name": "Status"
    }
  ],
  "DataClones": [
    {
      "ConnectorCode": "localfile",
      "Name": "Support Tickets 1",
      "RecId": 900002
    },
    {
      "ConnectorCode": "localfile",
      "Name": "Support Tickets 2",
      "RecId": 900001
    }
  ],
  "MatchedColumnsOnly": true
}
```


## Pre-flow / staging evidence — 2026-10-22

A three-table fusion inside the pre-flow has AdditionalColumns=[{Name:"Connection",Type:"nameoftable"}] and MatchedColumnsOnly=true. The separate staging fusion uses the same provenance structure named CONNECTION, 58 embedded datasets, MatchedColumnsOnly=false, and matchto/settonull/converttype column actions. Sources=[] does not mean no data dependencies: DataClones binds existing resource tables.

Table Fusion action keys use DataCloneRecId (numeric dataset resource ID), unlike Combine Tables actions which use SourceId (graph node UUID). Observed conversion actions have MatchedColumnName=null with the target type on the column. Do not interchange these formats. AdditionalColumns.Type=nameoftable is an observed serialized value; values are derived from the source table name, not automatically a canonical platform/business identifier. Rename/mapping drift must be considered.

Generalized settings fragment (synthetic IDs and field/table names, not a tested complete fusion; actual source schemas are needed to complete/reconcile the actions):

```json
{
  "AdditionalColumns": [
    {
      "Name": "SourceTable",
      "Type": "nameoftable"
    }
  ],
  "Columns": [
    {
      "Name": "Entity",
      "InternalType": "textsimple(250)",
      "Actions": [
        {
          "Action": "matchto",
          "DataCloneRecId": 900001,
          "MatchedColumnName": "entity_name"
        },
        {
          "Action": "settonull",
          "DataCloneRecId": 900002,
          "MatchedColumnName": null
        }
      ]
    },
    {
      "Name": "Amount",
      "InternalType": "decimalstrict(28,9)",
      "Actions": [
        {
          "Action": "converttype",
          "DataCloneRecId": 900002,
          "MatchedColumnName": null
        }
      ]
    }
  ],
  "DataClones": [
    {
      "ConnectorCode": "table",
      "Name": "SYNTHETIC_SOURCE_A",
      "RecId": 900001
    },
    {
      "ConnectorCode": "table",
      "Name": "SYNTHETIC_SOURCE_B",
      "RecId": 900002
    }
  ],
  "MatchedColumnsOnly": false
}
```

The actual staging source also has DataLossWarning=true on several column entries. Treat that as evidence of warning metadata; do not generate it as a policy or assume a later wider type reverses earlier truncation/rounding. The staging flow explicitly filters dates and converts metrics before persisting its output. Only those observed shapes are established; import/execution, implicit matches, null behavior and conversion outcomes remain unverified.
