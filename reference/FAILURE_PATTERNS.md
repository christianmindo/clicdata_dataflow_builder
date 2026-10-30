# Troubleshooting patterns

Use these as diagnostic explanations, not alternate flow templates. Do not copy a failing pattern into a new flow. The nearest complete canonical example is the authoritative starting shape.

| Symptom | Check | Preferred construction |
| --- | --- | --- |
| Duplicate column name | New aliases versus all incoming names, ignoring case | Distinct raw names and normalized outputs; case changes are insufficient |
| CONCAT collation conflict | Two independent text columns in one expression | Avoid the synthetic key if unnecessary; otherwise a verified literal prefix + one text field can avoid that mixture; no COLLATE |
| Combine briefly mismatches | Real branch fields/types versus sources/actions/invalidSources | Native settonull for genuinely missing columns; do not falsify success metadata |
| Group Rows fails with no values | Empty GroupedValues | Count an existing field and project the helper away |
| Amounts multiply after nested extraction | More than one event row per fact key | Group events separately, lookup totals back, test unmatched facts |
| A dependent formula fails | It uses a just-created alias in the same node | Add the dependency in a preceding calculation node |
| Preview unexpectedly persists data | CheckpointType or enabled output | No checkpoints; use the ordinary node preview and a no-output variant |
| Import succeeds but data differs | Resource IDs, types, nulls, grain, duplicate matches | Compare full output multisets and totals; import is not execution validation |

An error icon alone does not establish the cause. Request the actual error message. A screenshot documents appearance, not engine behavior. Local SQLite does not model SQL Server collations, physical table migration or undocumented lookup selection.
