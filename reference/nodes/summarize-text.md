# summarize-text — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="summarize-text"></a>

### Summarize Text — `summarize-text`

Uses Story with `SourceType: document`, automatic language selection, and `OnFailure: fail`. Requests extractive summary sorted by offset and abstractive summary with an empty Language setting.

- **Property class:** `DataFlowNodeSummarizeTextProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `OnFailure`, `ProcessOutputColumns`, `SourceColumn`, `SourceLanguageType`, `SourceType`.
- **Fixture examples:** `Summarize Text #1`.

Observed node-specific settings (not a complete node):

```json
{
  "OnFailure": "fail",
  "ProcessOutputColumns": [
    {
      "Name": "Extractive Summary",
      "SortBy": "offset",
      "Type": "extractive_summary"
    },
    {
      "Language": "",
      "Name": "Abstractive Summary",
      "Type": "abstractive_summary"
    }
  ],
  "SourceColumn": "Story",
  "SourceLanguageType": "auto",
  "SourceType": "document"
}
```
