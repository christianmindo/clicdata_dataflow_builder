# remove-duplicates — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="remove-duplicates"></a>

### Remove Duplicates — `remove-duplicates`

Uses Status as UniqueKey. OrderBy and OrderByDesc are empty; which duplicate survives and the formats of populated ordering settings remain unknown.

- **Property class:** `DataFlowNodeRemoveDuplicatesProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `OrderBy`, `OrderByDesc`, `UniqueKey`.
- **Fixture examples:** `Remove Duplicates #1`.

Observed node-specific settings (not a complete node):

```json
{
  "OrderBy": [],
  "OrderByDesc": [],
  "UniqueKey": [
    "Status"
  ]
}
```
