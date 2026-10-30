# conditional-find-replace — usage and limitations

Evidence: UI and clipboard inspection in Dia on 2026-10-22, not engine execution. Columns/Replacements item UUIDs (_itemid) were omitted from generalized fragments; omission/regeneration remains untested.

<a id="conditional-find-replace"></a>

### Conditional Find & Replace — `conditional-find-replace`

- **Property class:** `DataFlowNodeConditionalFindReplaceProperties:#Infinis.DataFlows`.
- **Observed upstream source count:** 1.
- **Observed node-specific settings:**

```json
{
  "ColumnNames": [],
  "Replacements": [
    {
      "Comparator": "equals",
      "Find": "DEMO_FIND",
      "ReplaceMode": "all",
      "ReplaceWith": "DEMO_REPLACE",
      "Values": [
        "DEMO_CONDITION"
      ],
      "ValueType": "value"
    }
  ]
}
```

The initially inspected node had ColumnNames=[] and Replacements=[], empty OutputColumns, and an error indicating no column was selected. A temporary rule was configured solely to capture its nested serialization, then removed; no node execution or flow save was requested/performed. The snippet retains ColumnNames=[] to reflect that capture and is deliberately not an executable configuration. Select actual target fields before building a usable flow. Do not confuse ColumnNames (target fields) with Values (predicate operand values).

Observed rule editor:

| Field | Choices / controls inspected |
| --- | --- |
| Find | Pattern to find text input |
| Replace with | Replacement text input |
| Replace | All occurrences; First occurrence; Last occurrence; First and last occurrences |
| Condition | None; Equals; Not equal; Is null; Is not null; Is empty; Is not empty; Is empty or whitespace; Is not empty or whitespace; Greater than; Greater than or equal; Less than; Less than or equal; Contains; Does not contain; Starts with; Does not start with; Ends with; Does not end with; One Of; Not One of; Between; Not Between |
| Type (observed under Equals) | Value; Selected Value; Column; Query Expression; Account Parameter |
| Equals / Value | One operand text input |
| Between / Value | Two operand text inputs |

Captured serialized values are Comparator=equals, ReplaceMode=all and ValueType=value. Do not fabricate enum mappings for the other visible choices, predicate grouping, expression syntax or account-parameter representation. Rule order/interaction, predicate scope (for example whether it evaluates each selected field), case sensitivity, literal-versus-regex matching, null behavior, and first/last occurrence semantics require execution or additional documentation. The presence of the word Pattern alone does not prove regex support. This node is distinct from ordinary find-replace.
