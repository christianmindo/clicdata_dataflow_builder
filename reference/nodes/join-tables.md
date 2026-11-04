# join-tables — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="join-tables"></a>

### Join — `join-tables`

The observed fixture uses an inner join over two upstream nodes. This is one configuration example, not a default or an exhaustive list of supported join types. Conditions contain Parts with explicit source-node IDs and column values: Assigned To equals Agent ID.

- **Property class:** `DataFlowNodeJoinTablesProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 2.
- **Input capacity (user-confirmed 2026-11-04):** exactly two upstream node inputs. Table Merge supports more than two tables in one node; larger joins using Join require a chain of binary Join nodes.
- **Node-specific properties:** `Conditions`, `JoinType` (historical checkpoint status fields must be omitted on new nodes).
- **Fixture examples:** `Join #1`.

Observed node-specific settings (not a complete node):

```json
{
  "Conditions": [
    {
      "Comparator": "equals",
      "LogicalOperator": "and",
      "Parts": [
        {
          "Source": "c54263d8-b8c4-5b94-bb97-808c5dad0b2e",
          "ValueType": "column",
          "Values": [
            "Assigned To"
          ],
          "InternalType": "int64"
        },
        {
          "Source": "4fe45f3d-fb91-52f3-be3d-4aefcd509abc",
          "ValueType": "column",
          "Values": [
            "Agent ID"
          ],
          "InternalType": "int64"
        }
      ]
    }
  ],
  "JoinType": "inner"
}
```

## Preserve the requested join semantics

Choose join behavior from the business requirement, not from the fixture. A requested left join must preserve unmatched rows from the intended left source; substituting an inner join can drop those rows and change counts and totals. Confirm which source is the left side and the expected duplicate-match behavior.

Observed join types are `inner` and `left`; use `JoinType: "left"` for a requested left join. Do not silently substitute inner. Preserve a supplied source order and condition-to-source references. The export does not independently establish which source-order position the engine treats as the preserved left input; confirm this in the editor when constructing a new connection layout. `SourceSide: "right"` and `TargetSide: "left"` describe connection endpoints and do not distinguish the two join roles in this export.

## Left join — supplied export, 2026-10-30

Observed configuration in version `2026.4.204.0`, patch `0`:

- `JoinType` is the lowercase string `left`.
- `Properties.Sources` contains two ordered connections, each with `Id`, `SourceSide: "right"`, `TargetSide: "left"` and an editor `_itemid`.
- Two conditions use `Comparator: "equals"` and `LogicalOperator: "and"`. Each has two `Parts` identifying the source node, `ValueType: "column"`, a single-element `Values` array and the exact `InternalType`.
- The supplied conditions compare text keys of type `textsimple(250)` and dates of type `date`. Conditions have their own editor `_itemid`; these are distinct from node IDs.
- `CheckpointType` is null. New nodes must omit `Info` and checkpoint status fields under the standing rules.

The companion JSON includes a generic left-join settings example with invented graph IDs and field names, and omits editor item IDs. It is reference metadata, not an importable connected flow or a client binding. Original upstream definitions were not supplied. Import, preserved-side behavior, null-key matching, duplicate multiplicity and engine execution have not been tested from this evidence.

User-reported issue: an assistant substituted inner for a requested left join because only inner was documented. This export resolves the missing `JoinType` value; it does not establish other unobserved join enum values.

## Right join — user-confirmed support, inferred serialization, 2026-10-30

The user confirms that Right Join is supported and authorizes documenting the inferred setting:

```json
{
  "JoinType": "right"
}
```

The lowercase value `right` is inferred from the observed `inner` and `left` values; it has not been observed in a Right Join editor export or tested by import/execution. Treat this as a candidate setting requiring editor verification, not observed serialization. Preserve the intended right-side rows and duplicate multiplicity; do not substitute inner. Retain the documented Sources/Conditions structure and explicit source references; do not swap connector endpoint labels to select the join type. Verify which source is the right input in the editor. No additional join enum values are established by this inference.
