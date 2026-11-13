# table-input — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="table-input"></a>

### Table Input — `table-input`

Reads a referenced dataset using `DataCloneRecId`, with selected fields identified by name, type, and numeric `RecId`.

- **Property class:** `DataFlowNodeTableInputProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 0.
- **Node-specific properties:** `DataCloneName`, `DataCloneRecId`, `SelectedColumns`.
- **Fixture examples:** `Support Tickets 1 #1`, `Support Tickets 2 #1`, `IP Addresses #1`, `City, Latitude, Longitude #1`, `Support Tickets - Review`, `Agents #1`, `Support Tickets JSON`.

Observed node-specific settings (not a complete node). IDs below are synthetic adaptations; replace resource IDs with verified target bindings and remap graph/internal IDs consistently. Repeated columns are retained to preserve the observed mapping relationships.

```json
{
  "DataCloneName": "Support Tickets 1",
  "DataCloneRecId": 900002,
  "SelectedColumns": [
    {
      "InternalType": "int64",
      "Name": "Ticket ID",
      "RecId": 900003
    },
    {
      "InternalType": "date",
      "Name": "Date Opened",
      "RecId": 900004
    },
    {
      "InternalType": "date",
      "Name": "Date Closed",
      "RecId": 900005
    },
    {
      "InternalType": "textsimple(250)",
      "Name": "Customer Name",
      "RecId": 900006
    },
    {
      "InternalType": "textsimple(250)",
      "Name": "Issue Category",
      "RecId": 900007
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
      "Name": "Assigned To",
      "RecId": 900010
    },
    {
      "InternalType": "textsimple(250)",
      "Name": "Location",
      "RecId": 900011
    }
  ]
}
```

## Source intake — copied input nodes only

Use the user's copied Table Input JSON or input nodes in the latest supplied whole-flow export. These supply source bindings and selected fields; see [SCHEMA_FILES.md](../SCHEMA_FILES.md). Request an updated copy if fields or bindings are missing. Optional schema CSVs support design/comparison but do not replace input-node evidence. Never infer RecIds from names, row order, filenames or trace IDs. Do not collect IDs separately or use remote discovery or metadata queries. Verify source selections after import; copied metadata does not prove execution.
