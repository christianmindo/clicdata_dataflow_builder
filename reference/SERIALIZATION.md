# Clipboard serialization

Read for new construction or structural/schema changes. Read only the relevant node files for node-specific settings.

## Shared JSON format

### Clipboard structure and node identity

The supplied text parses directly as a JSON array, without a flow wrapper or an extra JSON-string decoding step. This establishes the supplied format; the editor’s complete clipboard contract remains untested.

The initial fixture contains `Code`, `Description`, `Error`, `Id`, `Name`, `Properties`, `Sequence`, and `Warning`. A user-supplied two-node editor clipboard on 2026-10-29 omits `Sequence` on both nodes; it is not universally required by the observed format. `Code` identifies the node type; `Name` is a display name; `Id` is a UUID-shaped string. Annotation objects have a smaller envelope (`Code`, `Id`, `Properties`). Do not assume every object is a processing node.

Common processing properties:

| Property | Observed representation / interpretation |
| --- | --- |
| `__type` | Serialized property-class name ending in `:#Infinis.DataFlows`; exact per-type values are in nodes/<code>.json |
| `_AppVersion`, `_PatchVersion` | Version metadata; compatibility and migration rules unknown |
| `Enabled` | Boolean in the supplied nodes; disabled-node behavior untested |
| `CheckpointType` | null, `preview`, or `complete` |
| `Left`, `Top` | Canvas coordinates, including negative values |
| `OutputColumns` | Schema entries with `Name`, `InternalType`, and `traceId` |
| `Sources` | Incoming graph connections; empty on standalone data-source nodes |

`Sequence` exists, but its effect on evaluation is unknown. Preserve it while learning rather than treating it as a substitute for graph connections. `OutputColumns` and `traceId` may include editor-maintained schema metadata; whether the editor can regenerate them is unverified.

### Complete processing-node envelope

This teaching example reduces an observed Table Input to one field and resets its position. It illustrates how the node-specific settings fit into a complete raw clipboard array; this reduced variant has not been editor-tested. Its resource IDs are synthetic teaching values, so it is not ready for a target environment. Generate fresh node/schema IDs for new flows and resolve actual dataset/field IDs. Match each node's exact property class from the catalog; annotation envelopes differ.

```json
[
  {
    "Code": "table-input",
    "Description": "",
    "Error": null,
    "Id": "3c3b02b4-defa-5185-8533-dc63001709f4",
    "Name": "Support Tickets 1 #1",
    "Properties": {
      "__type": "DataFlowNodeTableInputProperties:#Infinis.DataFlows",
      "_AppVersion": "2026.4.200.0",
      "_PatchVersion": 1,
      "CheckpointType": null,
      "Enabled": true,
      "Left": 0,
      "OutputColumns": [
        {
          "InternalType": "int64",
          "Name": "Ticket ID",
          "traceId": "d18b8310-e647-5d20-975a-392b96adcf5e"
        }
      ],
      "Sources": [],
      "Top": 0,
      "DataCloneName": "Support Tickets 1",
      "DataCloneRecId": 900002,
      "SelectedColumns": [
        {
          "InternalType": "int64",
          "Name": "Ticket ID",
          "RecId": 900003
        }
      ]
    },
    "Sequence": 2,
    "Warning": null
  }
]
```

### Connections and resource IDs

Connections are stored on the **downstream** node:

```json
{
  "Sources": [
    {
      "Id": "<upstream-node-id>",
      "SourceSide": "right",
      "TargetSide": "left"
    }
  ]
}
```

This fragment uses a placeholder and is not a paste-ready node. Side values observed across the fixture include left, right, top, and bottom. They correspond to canvas attachment sides; whether they also affect semantics needs verification. Several downstream nodes can reference the same upstream node, forming branches.

Do not remap all IDs as though they were interchangeable:

- Graph node IDs appear in Sources, SchemaSourceId, LookupNodeId, AggregatedNodeId, join condition Parts.Source, and combine-column source/action metadata.
- Table Merge has its own internal DataClones IDs referenced by Connections and condition Parts.Source.
- DataCloneRecId and dataset RecId values identify existing resources. SelectedColumns RecId values identify source fields.
- OutputColumns traceId and condition Guid values have separate roles; regeneration requirements are unknown.

User-confirmed Table Output exception (2026-10-29): omit Properties.DataCloneRecId on a new unbound dummy output. Users create/select the table from the node in the editor, which binds the resource ID. SelectedColumns still maps the final schema; graph node Id is still required. This exception does not apply to source Table Inputs. See nodes/table-output.md.

Table Fusion and Table Merge embed dataset references despite having empty Sources. A graph with all Sources resolved can still depend on unavailable datasets. The fixture has multiple disconnected components and does not include source data, credentials, schedules, or a complete account-resource definition.

### Types, expressions, and schemas

Observed schema types include `int32`, `int64`, `double`, `decimalstrict(28,9)`, `date`, `datetime`, `json`, `text(128)`, `text(250)`, `text(max)`, and `textsimple(10/20/250/353/max)` (the slash notation here abbreviates separate observed sizes). Preserve exact type strings; do not assume text and textsimple are interchangeable.

Expressions include bracketed field references, single-quoted literals, DATEDIFF, DATEFROMPARTS, and CASE WHEN. This is evidence of these particular expressions, not proof of unrestricted SQL support. JSON escaping and expression-language escaping are separate concerns.

Schemas are recorded at multiple points and can differ: Resolution Time is int32 in Calculate Columns but mapped to int64 in two output configurations. A generator must reconcile intended field types and mappings rather than copy one schema everywhere.

### Checkpoints and annotations

CPoint 50 and CPoint ALL are both `combine-tables` nodes with CheckpointType preview and complete respectively. Join also uses preview. These nodes include CheckpointIsOutdated true and CheckpointStatus load. The custom name “50” does not establish a row-limit setting. Current generation disables checkpoints: CheckpointType=null and no checkpoint status metadata. These named examples are historical observations only.

The array also contains background-panel and label annotations. Their inclusion shows that clipboard content can describe more than data-processing nodes. The historical screenshot informed layout interpretation; it is not needed for the inline structures and does not prove execution outcomes.

## Node ownership metadata: Info — 2026-10-22

User preference: omit the top-level `Info` object from newly generated clipboard nodes. Do not fabricate CreatedDate, CreatorName, CreatorRecId, OwnerName or OwnerRecId. The current canonical builder already omits Info, and all 16 canonical clipboard files were checked without it. Whether ClicData recreates ownership metadata on paste, save or re-export is unverified. This omission preference does not authorize removing metadata from an existing flow during an unrelated exact-preservation edit.

A single unstyled Table Input test was prepared without Info, using the actual source binding from the supplied 2026-10-22 export, fresh node/schema IDs, no checkpoints and no Table Output. JSON/static validation is separate from editor testing. Paste in a blank test flow, verify the node appears and its source binding remains selected, then save/copy or re-export it to inspect whether Info is created and whose metadata it contains. A pre-save and post-save export can distinguish when it appears. Do not claim regeneration until an export confirms it. This account-bound test is not a generic canonical example.


### Experimental identity/version omission test — 2026-10-22

At the user’s request, a second single-input test omits root Id and Info plus Properties._PatchVersion and Properties._AppVersion. Other configuration is preserved apart from the test name. OutputColumns.traceId values and actual dataset/field resource IDs remain: they are separate identifiers and were not part of this omission request. This unconnected node avoids unresolved downstream references; acceptance does not establish how connected flows should be serialized without root IDs. Normal generation still uses unique node IDs and documented version metadata until editor evidence establishes a supported alternative. The existing linter requires root IDs, so this intentionally nonconforming probe was checked with targeted JSON/omission/preservation assertions instead. Paste/save/re-export results and metadata regeneration remain unverified.


### Metadata omission follow-up — 2026-10-22

The user confirmed that the single Table Input probe omitting root Id/Info and Properties._PatchVersion/_AppVersion works in the editor. This establishes user-reported acceptance of that input-node probe; generated metadata values and connected-flow behavior were not supplied. A matching JSON to Columns probe was prepared with the same omissions and unchanged extraction/output schema settings. Its Sources array is deliberately empty so the user can connect it to the newly pasted input without assuming its generated node ID. This disconnected paste probe is not an executable complete flow; JSON to Columns acceptance and processing remain pending. Item _itemid values and output traceId values were retained, not tested for omission.

## Schema files and resource bindings

Use copied Table Input nodes for standard bindings. For VMF migrations, verified user-supplied MasterDB metadata is an alternative under [AGENTS.md](../AGENTS.md#client-source-bindings). Use documented DataCloneRecId and SelectedColumns serialization with verified column ownership, RecIds, names, and exact types. Request missing evidence or a copied node when binding properties are uncertain. Never infer IDs from order, filenames, graph IDs, or trace IDs. Editor import and binding verification remain separate checks.
