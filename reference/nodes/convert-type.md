# convert-type — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="convert-type"></a>

### Convert Type — `convert-type`

Requests conversion of Ticket ID to text(250). Invalid conversions, null behavior, and truncation are untested.

- **Property class:** `DataFlowNodeConvertTypeProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ConvertedColumns`.
- **Fixture examples:** `Convert Type #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ConvertedColumns": [
    {
      "InternalType": "text(250)",
      "Name": "Ticket ID"
    }
  ]
}
```
