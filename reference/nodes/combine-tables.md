# combine-tables — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="combine-tables"></a>

### Combine Tables — `combine-tables`

Combines upstream nodes using `SchemaSourceId` and per-column actions. One configuration uses `settonull` for an unmatched Status column. Lowercase `sources`, `invalidSources`, `error`, and `internalType` coexist with capitalized fields. The names CPoint 50 and CPoint ALL are custom names, not separate node types.

- **Property class:** `DataFlowNodeCombineTablesProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 2.
- **Node-specific properties:** `CheckpointIsOutdated`, `CheckpointStatus`, `Columns`, `SchemaSourceId`.
- **Fixture examples:** `CPoint 50`, `CPoint ALL`.

Observed node-specific settings (not a complete node). IDs below are synthetic adaptations; replace resource IDs with verified target bindings and remap graph/internal IDs consistently. Repeated columns are retained to preserve the observed mapping relationships.

```json
{
  "Columns": [
    {
      "Actions": [],
      "InternalType": "int64",
      "Name": "Ticket ID",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "int64"
    },
    {
      "Actions": [],
      "InternalType": "date",
      "Name": "Date Opened",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "date"
    },
    {
      "Actions": [],
      "InternalType": "date",
      "Name": "Date Closed",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "date"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Customer Name",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "textsimple(250)"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Issue Category",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "textsimple(250)"
    },
    {
      "Actions": [],
      "InternalType": "textsimple(250)",
      "Name": "Priority",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "textsimple(250)"
    },
    {
      "Actions": [
        {
          "Action": "settonull",
          "MatchedColumnName": null,
          "SourceId": "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
        }
      ],
      "InternalType": "textsimple(250)",
      "Name": "Status",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f"
      ],
      "invalidSources": [
        {
          "id": "3f6764f3-6ef1-5be4-8a79-cf9172628c52",
          "status": "notmatched"
        }
      ],
      "error": false,
      "internalType": "textsimple(250)"
    },
    {
      "Actions": [],
      "InternalType": "int64",
      "Name": "Assigned To",
      "sources": [
        "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f",
        "3f6764f3-6ef1-5be4-8a79-cf9172628c52"
      ],
      "invalidSources": [],
      "error": false,
      "internalType": "int64"
    }
  ],
  "SchemaSourceId": "a4a3d68f-4984-5587-9d3f-f9d4be71ac2f"
}
```

Additional observed Combine column conversion entry from the retailer export (a single `Columns` element, not a complete node). The `SourceId` refers to an upstream graph node; the requested type is on the column. This export omits lowercase cache fields on this entry; their requiredness remains unverified.

```json
{
  "Actions": [
    {
      "Action": "converttype",
      "MatchedColumnName": null,
      "SourceId": "61194a3d-15e3-51e0-8a8d-9e8a7a6c2dff"
    }
  ],
  "InternalType": "textsimple(3)",
  "Name": "INTERNAL MONTH NAME"
}
```
