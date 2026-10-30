# translate-text — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="translate-text"></a>

### Translate Text — `translate-text`

Translates Story into Croatian (hr) and Japanese (ja), with automatic source-language selection, SourceType plain, and ProfanityFilter true.

- **Property class:** `DataFlowNodeTranslateTextProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ProcessOutputColumns`, `ProfanityFilter`, `SourceColumn`, `SourceLanguageType`, `SourceType`.
- **Fixture examples:** `Translate Text #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ProcessOutputColumns": [
    {
      "Language": "hr",
      "Name": "Croatian"
    },
    {
      "Language": "ja",
      "Name": "Japanese"
    }
  ],
  "ProfanityFilter": true,
  "SourceColumn": "Story",
  "SourceLanguageType": "auto",
  "SourceType": "plain"
}
```
