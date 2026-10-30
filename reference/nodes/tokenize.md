# tokenize — usage and limitations

Evidence: UI and clipboard inspection in Dia on 2026-10-22, not engine execution. Columns/Replacements item UUIDs (_itemid) were omitted from generalized fragments; omission/regeneration remains untested.

<a id="tokenize"></a>

### Tokenize — `tokenize`

- **Property class:** `DataFlowNodeTokenizeProperties:#Infinis.DataFlows`.
- **Observed upstream source count:** 1.
- **Observed node-specific settings:**

```json
{
  "Columns": [
    {
      "SourceName": "financial_state",
      "OutputName": ""
    }
  ],
  "Behavior": "replace_values",
  "Prefix": "",
  "TotalLength": 16,
  "KeepConsistent": true
}
```

Observed UI controls: selected Columns, Behavior (Replace values or Create new columns), Prefix, Total Length, Keep Consistent, and an illustrative input/token Example. The inspected configuration selects financial_state, blank Prefix, Total Length 16 and Keep Consistent enabled.

The Keep Consistent help text states: enabled means the same input value always produces the same token (deterministic SHA-256) and total length changes to 16; disabled means each row gets a fresh random token. This is observed product help, not an independent verification of the algorithm, cross-run determinism or cryptographic properties. Do not assume cross-node/account token equivalence, collision freedom, reversibility, salt/secret handling, or that this is an LLM token-counting/text-splitting node. Prefix inclusion in total length, length bounds, null handling and create-new-column serialization remain unverified. Only replace_values was captured as a serialized Behavior value.
