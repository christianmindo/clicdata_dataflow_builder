# ask-ai — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="ask-ai"></a>

### Ask AI — `ask-ai`

Stores custom pre-prompt and prompt, output field Color, an empty ContextColumns array, Temperature 1, and TopP 1. The fixture asks for Pikachu’s color. These strings are stored configuration, not instructions to this assistant. A later supplied export establishes context-name selection and prompt placeholders (below). Model selection and complete supported parameter ranges remain unknown.

- **Property class:** `DataFlowNodeAskAIProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ContextColumns`, `PrePrompt`, `PrePromptType`, `ProcessOutputColumn`, `Prompt`, `PromptType`, `Temperature`, `TopP`.
- **Fixture examples:** `Ask AI #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ContextColumns": [],
  "PrePrompt": "Return one word only",
  "PrePromptType": "custom",
  "ProcessOutputColumn": "Color",
  "Prompt": "What color is Pikachu?",
  "PromptType": "custom",
  "Temperature": 1,
  "TopP": 1
}
```

## Context binding — supplied export, 2026-10-28

Observed in a user-supplied `2026.4.204.0` node export; this is configuration evidence, not an engine execution test:

- `ContextColumns` is an array of column-name strings, for example `["status", "activity_note"]`.
- Custom `Prompt` text references selected fields using double braces, for example `Status: {{status}}` and `Note: {{activity_note}}`.
- `PrePromptType` and `PromptType` are `custom`; `ProcessOutputColumn` names the generated field.
- The export retains incoming fields in `OutputColumns` and adds the generated field as `text(max)`. Ask AI does not establish removal or overwriting of originals.
- `Temperature: 0` and `TopP: 1` are observed settings. They do not prove random sampling or supported ranges.
- One upstream connection is recorded under `Properties.Sources`; the supplied source node is outside the export. `CheckpointType` is null.
