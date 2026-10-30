# Survey results for dashboards

Use when the user confirms that each source table represents a survey, rows represent respondent submissions, and question headers are columns. Read only this pattern and the node references needed for the current task.

## Preserve two grains

Prepare each source, then produce two independent Combine Tables branches:

| Branch | Grain | Suggested fields |
| --- | --- | --- |
| Submissions | One row per original source row, preserving repeats | SourceDatasetID, SurveyID, RespondentID, SubmittedDate, SubmissionCount = 1, QuestionCount, AnsweredQuestionCount |
| Answers | One row per submission × configured question, including unanswered cells when required | SourceDatasetID, SurveyID, RespondentID, SubmittedDate, QuestionID, QuestionText, QuestionKind, NumericAnswer or TextAnswer, IsAnswered, AnswerRowCount = 1 |

Keep original numeric types and text families/widths. Use native Combine missing-field actions to supply nulls for the absent answer type. Do not manufacture calculated NULL columns simply to equalize schemas.

When one source is one survey, its dataset ID can identify the survey; retain the original SurveyID too. A verified question-column RecId can identify a question in that source's current structure, but copying/recreating datasets may change it. Labels alone do not establish shared question identity.

Without a verified submission ID, preserve repeated rows. Do not invent uniqueness from respondent + survey + date, and do not join submissions and answers on that combination without resolving repeat submissions first.

## Unpivot decision and controlled test

Unpivot is a compact candidate for wide tables. Test null behavior and type handling before adopting it when unanswered cells matter. Separate numeric and text branches avoid coercing every measure to text.

The [controlled example](../../examples/survey-unpivot-probe/README.md) generates numeric NULL/0/5 and text NULL/empty/demo cells independently of respondent answers. Verify the generated cells before checking their Unpivot output. For N input rows, each three-column branch needs 3 × N rows if all cells survive. Compare per-probe counts, not only total rows; distinguish missing output from preview/export truncation.

Observed on 2026-10-28: the user returned a numeric output CSV with 100 rows across 50 identifier groups. It contained 50 zero probes and 50 value-5 probes, with no null-probe rows. This supports numeric-null omission for the tested configuration/export. Export completeness and the calculated-node preview were not independently verified, so universal engine behavior is not established. Text null/empty behavior is still pending.

If unanswered cells must be retained, explicit per-question Calculate Columns → Column Selector branches preserve the intended grain without depending on Unpivot null emission. A task-specific ten-source, 57-question flow using that construction passed local static checks with 146 processing nodes; editor execution of that full flow has not been established. Larger graphs are not a measured performance benefit. A more compact solution may use Unpivot when omitted null cells are acceptable or when a verified alternative preserves the denominator independently.

## KPI definitions

- Submissions: sum SubmissionCount in the submissions branch, never count answer rows as respondents.
- Unique respondents: distinct nonblank RespondentID. Confirm whether matching IDs across surveys identify the same person; record a provisional assumption explicitly. Distinct counts are nonadditive across periods and surveys.
- Surveys: distinct agreed survey identity.
- Configured questions: sum one QuestionCount per survey, or use a separate question inventory. Never sum QuestionCount over submission rows. Empty source surveys disappear from fact branches; an inventory is needed to include them.
- Answered cells: sum IsAnswered. Numeric zero counts as answered; null/empty-text policy must be agreed. Whitespace-only text requires an explicit cleaning rule.
- Answer coverage: answered cells / configured question opportunities. This does not establish eligibility-adjusted completion or invitation response rate.
- Fully answered submissions: rows where AnsweredQuestionCount = QuestionCount; this is not a verified completion status.
- Respondents/submissions over time: use the supplied submission date and label the selected count correctly. Do not sum daily unique-person counts into an overall unique-person count.
- Rating means, distributions and top-box rates: keep questions and scales separate; agree valid ranges and expose invalid answers.
- Recommendation NPS: only for an agreed recommendation question, among valid 0–10 answers: 100 × (count 9–10 − count 0–6) / valid count. Scores 7–8 remain in the denominator. Another 0–10 question is not automatically NPS.
- Price, duration and contact-count measures: preserve units; do not combine them into an overall rating average.
- Categorical rates require verified category coding. Invitation response rate requires the eligible/invited population; duration requires suitable timestamps.

Question types inferred from headers are proposed semantic mappings, not evidence of actual response values. No client records are needed for metadata-driven construction.

## Checks and evidence scope

Run local lint plus targeted binding, schema and geometry checks. In editor testing, reconcile N submissions and N × Q question opportunities for each source, including duplicates and unanswered cells. Reconcile submission AnsweredQuestionCount with answer IsAnswered totals. Verify zero, null, empty text, repeated IDs and question-label literals.

Local construction, returned output evidence and full engine verification are distinct. The generic example uses fictional bindings and records. Actual task bindings and generated client deliverables remain outside the reusable example. New destination keys/write modes require agreement; no destination writes are implied by this pattern.
