# Controlled Unpivot probe

This reusable example supports the [survey dashboard pattern](../../reference/patterns/survey-dashboard.md). It is separate from the canonical reference-pack generator.

`probe.clipboard.json` is a complete six-processing-node clipboard array with fictional dataset/column bindings. It has no outputs or checkpoints. Rebind its Table Input to a nonempty test source with SurveyID, RespondentID and SubmittedDate before testing. It is not ready for a real environment without that rebinding.

Each source row generates numeric NULL, zero and five, and text NULL, empty string and demo. The two Unpivot branches test each family separately. First verify those calculated cells in the editor; then compare per-probe output counts. The example's fictional records deliberately repeat respondent/date identifiers, so checks must preserve multiplicity rather than assume keys are unique.

- `synthetic-inputs.json`: two fictional source rows.
- `expected-preserving-nulls.json`: six numeric and six text rows if every test cell survives.
- `observed-numeric-summary.json`: identifier-free counts from the returned test export, with its evidence limits.

The synthetic adaptation has been checked locally only. The returned CSV tested the original task-bound numeric branch, not this rebound adaptation. Text behavior and export completeness remain unverified. If a preview/export is capped, inspect a smaller source or otherwise verify complete counts before concluding that missing rows were dropped.
