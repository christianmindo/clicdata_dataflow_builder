# detect-language — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="detect-language"></a>

### Detect Language — `detect-language`

Uses the Japanese column and requests Language Code of type language_code, with OnFailure fail.

- **Property class:** `DataFlowNodeDetectLanguageProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `OnFailure`, `ProcessOutputColumns`, `SourceColumn`.
- **Fixture examples:** `Detect Language #1`.

Observed node-specific settings (not a complete node):

```json
{
  "OnFailure": "fail",
  "ProcessOutputColumns": [
    {
      "Name": "Language Code",
      "Type": "language_code"
    }
  ],
  "SourceColumn": "Japanese"
}
```
