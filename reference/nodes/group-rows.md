<!-- Last updated: 2026-10-29; version: 2 -->
# group-rows — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="group-rows"></a>

### Group Rows — `group-rows`

Groups by Assigned To and counts Ticket ID as Ticket ID (Count). GroupByColumns contains objects here, whereas Pivot uses strings.

- **Property class:** `DataFlowNodeGroupRowsProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `GroupByColumns`, `GroupedValues`.
- **Fixture examples:** `Group Rows #1`.

Observed node-specific settings (not a complete node):

```json
{
  "GroupByColumns": [
    {
      "Name": "Assigned To"
    }
  ],
  "GroupedValues": [
    {
      "Aggregation": "count",
      "Alias": "Ticket ID (Count)",
      "InternalType": "int64",
      "Name": "Ticket ID"
    }
  ]
}
```

#### String concatenation — `string_agg` (2026-10-06)

**User-confirmed correction:** Group concat requires an explicit `Separator` on the `GroupedValues` entry where `Aggregation` is `string_agg`. Do not generate string aggregation without this property. The user repaired the flight SMS digest node with `Separator: ","`; the supplied corrected node reports null Error and Warning. Full output contents and row counts were not supplied with this correction.

Observed corrected settings (not a complete node):

```json
{
  "GroupByColumns": [
    {
      "Name": "sms_digest_key"
    }
  ],
  "GroupedValues": [
    {
      "Aggregation": "string_agg",
      "Alias": "candidate_digest",
      "InternalType": "textsimple(1223)",
      "Name": "candidate_facts",
      "Separator": ","
    },
    {
      "Aggregation": "count",
      "Alias": "candidate_count",
      "InternalType": "int64",
      "Name": "candidate_facts"
    }
  ]
}
```

`Separator` belongs to the individual string-aggregation value, not the node's top-level Properties or GroupByColumns. The count entry in the corrected node has no Separator. Preserve the intended delimiter explicitly; a comma is the user-supplied example, not an established default. Other separator values and concatenation ordering have not been tested here.

The editor supplied `_itemid` UUIDs on GroupByColumns and GroupedValues entries; whether these are required on generated clipboard objects remains unverified. It also resolved candidate_digest to `textsimple(1223)` and sms_digest_key to `textsimple(19)`. These are observed schema values for this example, not universal sizes or a concatenation limit. Reconcile the actual output schema when generating downstream nodes.

## Editor-copied sum configuration — 2026-10-29
Observed: the user directly supplied a two-node Table Input / Group Rows clipboard export after being asked to configure it manually in the editor. This is serialization evidence; no explicit preview totals or new generated-flow execution result accompanied it.

The Group Rows configuration uses GroupByColumns entries with Name and _itemid. GroupedValues entries contain Aggregation="sum", Alias, Name, InternalType="int64" and _itemid. The aggregate OutputColumns.Name equals Alias exactly. No numeric source field RecId is present in either grouping entry. Numeric dataset/field IDs belong to Table Input binding settings; grouping references the bound upstream fields by Name.

Incoming edges use Id (the upstream node UUID), SourceSide="right" and TargetSide="left". The node-level Id, output traceId and settings _itemid have distinct roles. Preserve those roles rather than substituting one for another.

The supplied Group Rows properties also include Code, DefaultName, CanBeProcessed=false, HasOutput=true, MinSources=1, MaxSources=1 and CanBeDisabled=true. These are observed editor fields, not proven generation requirements or errors. The input reports app version 2026.4.204.0 / patch 0; Group Rows reports 2026.4.205.0 / patch 1. Preserve a supplied baseline rather than forcing every node to one version. Neither node includes Sequence; its absence alone is not a static error for this observed envelope.

Do not substitute AggregateColumns, AggregatedColumns, AggregateType, AggregationType, SourceColumnName, Operation or OutputName for the observed GroupedValues settings. Do not replace Sources.Id/port sides with NodeId/Code edges. These alternatives appeared in user-reported failing generated files, not this editor-copied reference. Their individual contribution to paste failure has not been isolated.

The generic settings JSON includes a separately labeled sum example with fresh synthetic setting/schema IDs. No actual dataset/field bindings, ownership names, ownership IDs or timestamps from the user's export are copied into it. Earlier string_agg separator evidence remains unchanged.
