# json-to-rows — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="json-to-rows"></a>

### JSON to Rows — `json-to-rows`

Extracts fields from the tickets JSON column using paths such as `$[].ticket_id`, with explicit types and IsArray/IsObject flags. Nested arrays, missing paths, and row expansion semantics need tests.

- **Property class:** `DataFlowNodeJSONToRowsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `Columns`, `SourceColumn`.
- **Fixture examples:** `JSON to Rows #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Columns": [
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "ticket_id",
      "Node": "$[].ticket_id"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "subject",
      "Node": "$[].subject"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "description",
      "Node": "$[].description"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "status",
      "Node": "$[].status"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "priority",
      "Node": "$[].priority"
    },
    {
      "InternalType": "datetime",
      "IsArray": false,
      "IsObject": false,
      "Name": "created_at",
      "Node": "$[].created_at"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "customer_name",
      "Node": "$[].customer_name"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Name": "customer_email",
      "Node": "$[].customer_email"
    },
    {
      "InternalType": "int64",
      "IsArray": false,
      "IsObject": false,
      "Name": "assigned_to",
      "Node": "$[].assigned_to"
    }
  ],
  "SourceColumn": "tickets"
}
```
