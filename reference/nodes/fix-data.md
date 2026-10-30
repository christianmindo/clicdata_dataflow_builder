# fix-data — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="fix-data"></a>

### Fix Data — `fix-data`

Applies a typed text Fix action to Status: uppercase, remove spaces, and trim both ends. Other removal flags are false and RemoveCharacters is null; ordering of cleanup actions is unknown.

- **Property class:** `DataFlowNodeFixDataProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ColumnNames`, `Fix`.
- **Fixture examples:** `Fix Data #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ColumnNames": [
    "Status"
  ],
  "Fix": {
    "__type": "DataFlowFixDataActionText:#Infinis.DataFlows",
    "ChangeCase": "uppercase",
    "RemoveAllCharacters": false,
    "RemoveAllDigits": false,
    "RemoveAllHTML": false,
    "RemoveAllNonAlphaNumerics": false,
    "RemoveAllNonDigits": false,
    "RemoveAllNonLetters": false,
    "RemoveAllNonVisible": false,
    "RemoveAllSpaces": true,
    "RemoveCharacters": null,
    "TrimLeft": true,
    "TrimRight": true
  }
}
```


## Additional observed marketing pattern — 2026-10-22

Numeric Fix action class observed; Amount is a generic field alias. Setting invalid/empty numeric values to zero is a source business rule, never a universal default. Threshold controls were null; non-null threshold behavior remains unverified.

This is a generalized settings fragment from a supplied export, not an engine-tested recipe.

```json
{
  "ColumnNames": [
    "Amount"
  ],
  "Fix": {
    "__type": "DataFlowFixDataActionNumeric:#Infinis.DataFlows",
    "BiggerSetTo": "null",
    "BiggerSetToValue": null,
    "LowerSetTo": "null",
    "LowerSetToValue": null,
    "SetInvalidEmptyValuesTo": 0,
    "ValuesBiggerThan": null,
    "ValuesLowerThan": null
  }
}
```
