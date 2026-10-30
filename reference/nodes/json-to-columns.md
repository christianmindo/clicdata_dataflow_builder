# json-to-columns — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="json-to-columns"></a>

### JSON to Columns — `json-to-columns`

**User-reported, 2026-10-22:** extracts attributes of a JSON object directly into columns on the existing row; it is not the node for expanding an array. Use JSON to Rows for array-to-row expansion. Do not infer array support from the presence of IsArray/IsObject settings.

**Observed:** the supplied two-node export connects Table Input → JSON to Columns, with `variant_json` typed `json`. It extracts `$.pack_size` as `int64`, and `$.flavour_or_type` / `$.descriptor` as `textsimple(250)`. The output schema retains all 22 input fields (including `variant_json`) and appends the three extracted fields, for 25 fields. This is schema evidence, not a measured output row count. The snapshot has null Error/Warning values, but no source records or execution preview were supplied.

- **Property class:** `DataFlowNodeJSONToColumnsProperties:#Infinis.DataFlows`.
- **Observed upstream source count:** 1; exported MinSources and MaxSources are both 1.
- **Node-specific settings:** `SourceColumn`, `Columns`.
- **Observed version:** `_AppVersion: "2026.4.204.0"`, `_PatchVersion: 1`.
- **Category:** Parsing & Splitting (cyan), following the current palette.

Exact observed node-specific settings (not a complete node). `_itemid` values identify exported configuration items; their requiredness and regeneration behavior are unverified. They are distinct from node IDs, resource IDs and output trace IDs. These historical item IDs are serialization evidence, not reusable target bindings.

```json
{
  "SourceColumn": "variant_json",
  "Columns": [
    {
      "InternalType": "int64",
      "IsArray": false,
      "IsObject": false,
      "Node": "$.pack_size",
      "Name": "pack_size",
      "_itemid": "ff5ae319-3567-4257-bd64-37d875f5cc53"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Node": "$.flavour_or_type",
      "Name": "flavour_or_type",
      "_itemid": "63ab323c-83e1-4aae-abd2-4d660bbaa207"
    },
    {
      "InternalType": "textsimple(250)",
      "IsArray": false,
      "IsObject": false,
      "Node": "$.descriptor",
      "Name": "descriptor",
      "_itemid": "87eafdfe-cce3-49a1-9830-fd3f1f2e3be5"
    }
  ]
}
```

Illustrative object shape only (invented values, not supplied source records):

```json
{"pack_size": 6, "flavour_or_type": "Example type", "descriptor": "Example description"}
```

For that illustrative object, the intended new columns are pack_size=6, flavour_or_type="Example type", and descriptor="Example description" on the parent row. This illustrates the user-described behavior; it is not an engine test. Do not use `$[].field` paths for this object example. Preserve parent context and check extraction aliases against incoming field names, ignoring case.

**Unverified:** null/empty/malformed input handling, missing properties, incompatible values, nested object paths, use of IsArray/IsObject=true, item-ID omission/regeneration, and runtime row retention. Validate those cases in the editor before relying on them. No new editor import/execution is claimed.
