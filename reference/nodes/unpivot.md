# unpivot — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="unpivot"></a>

### Unpivot — `unpivot`

Lists three pivoted count columns, with output labels Assigned to and Count, int64 value type, and TextToRemove null. Its source is a table-output node.

- **Property class:** `DataFlowNodeUnpivotProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ColumnsToUnpivot`, `PivotColumnName`, `TextToRemove`, `ValueColumnInternalType`, `ValueColumnName`.
- **Fixture examples:** `Unpivot #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ColumnsToUnpivot": [
    "Ticket ID (Count) Emma Johnson",
    "Ticket ID (Count) John Smith",
    "Ticket ID (Count) Michael Davis"
  ],
  "PivotColumnName": "Assigned to",
  "TextToRemove": null,
  "ValueColumnInternalType": "int64",
  "ValueColumnName": "Count"
}
```

## Controlled numeric-null probe — 2026-10-28

A user-returned output CSV from the controlled numeric NULL/0/5 probe contained 100 rows: 50 zero rows and 50 value-5 rows across 50 respondent/date groups; no numeric-null probe rows appeared. This supports null omission for that configuration/export, not a universal guarantee: export completeness and the calculated-node preview were not independently verified. Text NULL/empty-string behavior remains pending.

Use the [reusable controlled probe](../../examples/survey-unpivot-probe/README.md) to check the target environment before depending on unanswered-cell preservation. Its synthetic adaptation has local static validation only. See the [survey pattern](../patterns/survey-dashboard.md) for counting implications and an explicit per-question alternative.
