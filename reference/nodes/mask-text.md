# mask-text — usage and limitations

Evidence: UI and clipboard inspection in Dia on 2026-10-22, not engine execution. Columns/Replacements item UUIDs (_itemid) were omitted from generalized fragments; omission/regeneration remains untested.

<a id="mask-text"></a>

### Mask Text — `mask-text`

- **Property class:** `DataFlowNodeMaskTextProperties:#Infinis.DataFlows`.
- **Observed upstream source count:** 1.
- **Observed node-specific settings:**

```json
{
  "Columns": [
    {
      "SourceName": "customer_email",
      "OutputName": ""
    }
  ],
  "Behavior": "replace_values",
  "DataType": "emails",
  "MaskUserName": false,
  "MaskDomain": false,
  "MaskFirstName": false,
  "MaskMiddleName": false,
  "MaskLastName": false,
  "MaskingCharacter": "asterisk",
  "KeepOriginalCharacter": "start",
  "CharacterToKeep": 0,
  "MaskLetters": false,
  "MaskDigits": false,
  "MaskSpecialCharacter": false
}
```

Observed UI controls:

| Area | Choices / controls inspected |
| --- | --- |
| Columns | Selected source columns; the inspected source is customer_email |
| Behavior | Replace values; Create new columns |
| Create new columns | Adds an Output Columns mapping area; an unset destination is shown as Not mapped and the node gains an error indicator |
| Data Type | Email; Names; Text |
| Email | Mask User Name; Mask Domain |
| Names | Mask First Name; Mask Middle Name; Mask Last Name |
| Text | Mask Letters; Mask Digits; Mask Special Characters |
| Masking Character | `*`, `?`, `-`, `_`, `•`, `#`, `x`, `X` |
| Keep Original Characters | At Start; At End; Both Start & End |
| Characters to keep | Numeric control; inspected value 0 |
| Example | Email/name/text illustration changes with the selected mode; this is a UI example, not an engine preview |

The observed email configuration has both mask switches false and its example remains user@domain.com. Do not assume selecting a Data Type alone enables masking. Mode-specific flags coexist in the exported properties even when their controls are hidden. The UI labels above do not establish their serialized enum strings: only DataType=emails, Behavior=replace_values, MaskingCharacter=asterisk and KeepOriginalCharacter=start were captured. Other enum mappings, both-end character-count semantics, Unicode classification, malformed/null values and multi-column behavior need configured exports or execution tests. Do not infer regular-expression support. Masking is not evidence of irreversible anonymization.
