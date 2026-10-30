# API documentation as supplemental parameter evidence

Read only when a requested node option/enum is missing from the clipboard references. Do not load this during routine flows whose settings are already documented.

Source: [ClicData 2026.3 Data Flow Nodes Properties](https://help.clicdata.com/api?section=section/Object-Properties/Data-Flow-Nodes-Properties&version=2026.3), reviewed 2026-10-28. The linked Help Center embeds [the version-selected API reference](https://api.clicdata.com/help/api/user/index?version=2026.3#section/Object-Properties/Data-Flow-Nodes-Properties). The version selector displayed 2026.3. Public documentation was read without authentication, client data retrieval, API mutations or test execution.

## Purpose

Use [parameter-values-2026.3.json](parameter-values-2026.3.json) to discover documented parameter values and compare them with existing node examples. Continue delivering editor clipboard JSON. API snake_case envelopes and objects are not paste-ready clipboard structures, and required/optional API flags do not establish clipboard requiredness.

## Evidence levels

- **Clipboard-confirmed:** the exact value appears in a supplied clipboard configuration for that node/property. This confirms serialization, not runtime success.
- **API-documented:** the exact value appears in the selected official reference. It is a supported API parameter candidate, not automatically a proven clipboard value.
- **UI-observed:** a setting appears in the editor. UI labels may differ from serialized enum strings.
- **Tested:** an explicit editor import/execution result confirms only the tested configuration and outcome.

Do not promote API-only values into clipboard-confirmed subsets or silently expand linter/generator capabilities. If an existing clipboard property has a corresponding documented API value, use it as a focused test candidate and verify its mapping. New setting names/property classes require a known editor structure, not mechanical snake_case-to-PascalCase conversion. Request only the minimal export needed for a real gap.

## Findings worth using

- IP output types: all 12 identifiers are listed; four match the user's selected clipboard export. The other eight now have documented candidate strings rather than guesses. Full country name is not in that IP list.
- Text casing and Standardize rules have broader enumerations than our initial samples. The API confirms exactly/uppercase/isemptyorwhitespace already seen in clipboard and documents additional candidates.
- Aggregation includes distinct count, dispersion statistics and string aggregation as well as the familiar count/sum/min/max/average choices. Check the actual target clipboard shape and semantics before generating an untested variant.
- Filter predicates and value types have explicit spellings, including less obvious negative forms. Preserve those strings when documenting candidates rather than translating UI labels yourself.
- Fix Data describes Boolean, Date, DateTime, DateTime Offset and Time variants in addition to Text/Numeric. Their parameters include missing-value replacements, range limits and date/time/timezone handling. These extend the investigation list; unobserved clipboard subtype classes remain unknown.
- Fusion provenance also documents dataupdateddate alongside the observed nameoftable. Translation documents HTML input/transliteration options; sentiment documents opinion-mining output options; several language nodes document fail/leaveempty handling. These are not general settings for unrelated nodes.

## Gaps and cautions

The inspected node section has no on_failure option on IP to Location, so it does not resolve invalid-IP handling. A label named Country can still contain country_code. Documentation of join types does not specify duplicate lookup selection. Broad Output process_mode values must not become automatic allowed clipboard write choices. Keep the existing authorization and disabled-output rules.

Detailed Forecast SSA/Mask Text/Tokenize/Conditional Find & Replace sections were not found in this node-properties section even though newer node Codes appear in endpoint enums. It is not a complete replacement for editor examples. Clipboard compatibility and runtime behavior remain separate verification steps.
