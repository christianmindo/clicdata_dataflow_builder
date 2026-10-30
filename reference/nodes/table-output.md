# table-output — usage and limitations

## User-confirmed manual destination binding — 2026-10-29

New business flows always include clearly named dummy Table Output nodes, defaulting to Enabled=true and ProcessMode=rebuild. Map final fields/types and result-grain keys. The user confirmed that output IDs are not needed while authoring: omit Properties.DataCloneRecId until the user creates/selects the destination from the node in the editor, which supplies the binding. Do not invent IDs or omit graph-node Id. Manual destination binding is required before execution; this confirmation does not establish any generated flow's engine result. Existing destinations/modes remain unchanged outside requested scope. Explicit preview-only requests and canonical teaching fixtures retain their exceptions. A dummy destination is a test table, not automatic data anonymization.

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="table-output"></a>

### Table Output — `table-output`

Maps source fields to destination names and types for a referenced output dataset. Observed `ProcessMode` values are `updateappend`, `append`, and `rebuild`; the UI name “Reload” corresponds to `rebuild`. `IsKey: true` occurs on Ticket ID, including append/rebuild examples. Exact key and write semantics require execution tests. Output nodes can also feed downstream nodes: Pivot - Output feeds Unpivot.

- **Property class:** `DataFlowNodeTableOutputProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `DataCloneName`, `DataCloneRecId`, `ProcessMode`, `SelectedColumns`.
- **Fixture examples:** `Support Tickets ALL Update/Append`, `Support Tickets ALL Append`, `Support Tickets ALL Reload`, `Summarize Text - Output`, `Ask AI - Output 3`, `IP to Location - Output`, `Geocoding - Output`, `Sentiment Analysis - Output`, `Grouping - Output`, `Table Merge - Output`, `Column Selector - Output`, `Filter Query - Output 1`, `Filter Query - Output 2`, `Filter Wizard - Output`, `Pivot - Output`, `Aggregation - Output`, `Unpivot - Output`, `JSON to Rows - Output`, `Text to Rows - Output`, `Text to Columns - Output`, `Transform Nodes - Output`, `Translate Text - Output`, `Detect Language - Output`.

Observed node-specific settings (not a complete node). IDs below are synthetic adaptations; replace resource IDs with verified target bindings and remap graph/internal IDs consistently. Repeated columns are retained to preserve the observed mapping relationships.

```json
{
  "DataCloneName": "Support Tickets ALL Update/Append",
  "DataCloneRecId": 900029,
  "ProcessMode": "updateappend",
  "SelectedColumns": [
    {
      "InternalType": "int64",
      "IsKey": true,
      "OutputName": "Ticket ID",
      "SourceName": "Ticket ID"
    },
    {
      "InternalType": "date",
      "OutputName": "Date Opened",
      "SourceName": "Date Opened"
    },
    {
      "InternalType": "date",
      "OutputName": "Date Closed",
      "SourceName": "Date Closed"
    },
    {
      "InternalType": "textsimple(250)",
      "OutputName": "Customer Name",
      "SourceName": "Customer Name"
    },
    {
      "InternalType": "textsimple(250)",
      "OutputName": "Issue Category",
      "SourceName": "Issue Category"
    },
    {
      "InternalType": "textsimple(250)",
      "OutputName": "Priority",
      "SourceName": "Priority"
    },
    {
      "InternalType": "textsimple(250)",
      "OutputName": "Status",
      "SourceName": "Status"
    },
    {
      "InternalType": "int64",
      "OutputName": "Assigned To",
      "SourceName": "Assigned To"
    },
    {
      "InternalType": "int32",
      "OutputName": "Resolution Time",
      "SourceName": "Resolution Time"
    }
  ]
}
```
