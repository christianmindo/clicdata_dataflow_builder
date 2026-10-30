# sentiment-analysis — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="sentiment-analysis"></a>

### Sentiment Analysis — `sentiment-analysis`

Uses Review Text with automatic source-language selection; requests sentiment and positive, neutral, and negative confidence scores. `OnFailure` is `fail`.

- **Property class:** `DataFlowNodeSentimentAnalysisProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `OnFailure`, `ProcessOutputColumns`, `SourceColumn`, `SourceLanguageType`.
- **Fixture examples:** `Sentiment Analysis #1`.

Observed node-specific settings (not a complete node):

```json
{
  "OnFailure": "fail",
  "ProcessOutputColumns": [
    {
      "Name": "Sentiment",
      "Type": "sentiment"
    },
    {
      "Name": "Positive Confidence Score",
      "Type": "positive_confidence_score"
    },
    {
      "Name": "Neutral Confidence Score",
      "Type": "neutral_confidence_score"
    },
    {
      "Name": "Negative Confidence Score",
      "Type": "negative_confidence_score"
    }
  ],
  "SourceColumn": "Review Text",
  "SourceLanguageType": "auto"
}
```
