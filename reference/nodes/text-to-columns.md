# text-to-columns — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="text-to-columns"></a>

### Text to Columns — `text-to-columns`

Uses delimiter `-` on Priority and a ValueColumns entry named Test with Position 1 and InternalType null. Position indexing and type inference are not yet verified.

- **Property class:** `DataFlowNodeTextToColumnsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `Delimiter`, `SourceColumn`, `ValueColumns`.
- **Fixture examples:** `Text to Columns #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Delimiter": "-",
  "SourceColumn": "Priority",
  "ValueColumns": [
    {
      "InternalType": null,
      "Name": "Test",
      "Position": 1
    }
  ]
}
```
