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

## Offline schema inputs — 2026-10-28

Use user-supplied schema CSVs for current names/types; see [SCHEMA_FILES.md](../SCHEMA_FILES.md). The five-column export lacks field RecIds; the user-confirmed schema_<six-digit-ID>.csv filename provides the dataset ID. Obtain those from a user-supplied minimal Table Input export or explicit mapping. Do not substitute source_column_name, infer RecIds from row order or query an account through MCP. Schema-only design remains possible, but target-bound clipboard construction requires its binding dependencies to be resolved.
