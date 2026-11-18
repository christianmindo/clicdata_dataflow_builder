# ClicData Data Flow Builder

A modular reference for ClicData editor clipboard JSON. Keep the folder structure when sharing.

Use AGENTS.md as project instructions (Codex reads it automatically). Describe the task and provide the latest flow export or copied Table Input JSON. Schema CSVs are optional design supplements. Use copied inputs for standard bindings, or verified user-supplied MasterDB configuration metadata for VMF migrations; connected accounts are not used for intake and table records must never be queried or read. The instructions route the LLM to a small set of relevant files instead of requiring the entire reference on every request.

## Install for your own Codex tasks

This repository is also a self-contained skill: [SKILL.md](SKILL.md) is its entry point, with the existing references, scripts, and examples alongside it. No ClicData account connection is required.

Paste this into Codex, which provides the Skill Installer:

```text
Use $skill-installer to install the skill from
https://github.com/christianmindo/clicdata_dataflow_builder
using repository path . and installation name clicdata-dataflow-builder.
Keep the bundled AGENTS.md, reference, scripts, and examples with SKILL.md.
```

Restart Codex after installation so it discovers the skill. In your own project/chat, invoke it with:

```text
Use $clicdata-dataflow-builder to help with my ClicData flow.
My use case is: [describe the task and desired result].
```

Then supply the latest clipboard export or required copied Table Input nodes when requested. The skill does not need write access to this GitHub repository; keep your client artifacts in your own project, outside the installed skill. Pasting the repository link alone does not install it.

## Current-version check

At the start of each task, the skill checks the public release manifest and uses a current working copy. It downloads the ZIP only if the published version differs from the installed/cached version, verifies its SHA-256 checksum, and keeps that version fixed for the task. This requires permitted network access and writable storage; otherwise it reports the failed check and uses its bundled reference.

Local Codex/Claude Code can retain a persistent cache. Hosted ChatGPT/Claude may only allow a temporary session cache, so this does not promise permanent updates to the account's installed skill. The installed entry point remains a bootstrap; the current working copy supplies the task instructions, references, and linter. Existing installations from before this feature need one update to obtain that bootstrap.

Maintainers must run `python3 scripts/package_skill.py` after reference changes and publish both `dist/clicdata-dataflow-builder.zip` and `dist/clicdata-dataflow-builder.version.json` together. The version is a content hash of bundled files; a GitHub push without rebuilding the package does not publish a new skill version. Checksums detect inconsistent downloads, not independent publisher authenticity.

Alternatively, clone/download the repository and open the folder as a Codex project to use its AGENTS.md directly.

## Use with Claude

The same [SKILL.md](SKILL.md) and bundled rules support Claude; no separate flow reference is maintained.

**Claude chat / Desktop:** Download [clicdata-dataflow-builder.zip](dist/clicdata-dataflow-builder.zip) (use GitHub's **Download raw file** button). In **Customize > Skills**, choose the option to upload a skill, upload this ZIP, and enable it. Code execution/file creation must be enabled, and your organization must allow custom skills. Then ask: “Use the ClicData Data Flow Builder skill to help me with [use case and desired result].” See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**Claude Code:** Extract the ZIP so its entry point is at `~/.claude/skills/clicdata-dataflow-builder/SKILL.md` for personal use, or `.claude/skills/clicdata-dataflow-builder/SKILL.md` in your own project for project use. Keep the whole extracted skill folder together. Start a new session and invoke:

```text
/clicdata-dataflow-builder Help me with [use case and desired result].
```

These are [Claude Code's documented skill locations and invocation format](https://code.claude.com/docs/en/skills). Installing the skill does not grant account access or execute ClicData flows. Claude reads the bundled AGENTS.md through SKILL.md explicitly.

The upload ZIP contains the tracked skill entry point, AGENTS.md, reference, examples, runtime helpers, and a generated version marker. It excludes local client deliverables, untracked folders, Git history, and Codex UI metadata. ZIP structure and bundled linting can be checked locally; successful Claude upload and invocation still require a check in Claude.

## Client-sensitive data: metadata only

**DO NOT QUERY DATA.** Only binding metadata is allowed, including on QA/dummy tables. Follow the mandatory [metadata-only rules](AGENTS.md#sensitive-client-data-metadata-only--mandatory). These are agent instructions, not server-enforced permissions. The user performs editor previews and execution.

## Task entry points

| Need | Read |
| --- | --- |
| Copied Table Input JSON, schemas, missing bindings, offline workflow | [Schema files](reference/SCHEMA_FILES.md) |
| Processing design, edits, validation, optimization | [Build guide](reference/BUILD_GUIDE.md) |
| Clipboard envelope, graph/resource IDs, schemas, metadata | [Serialization](reference/SERIALIZATION.md) |
| Exact settings for one node | [Node catalog](reference/node-catalog.json), then only its .json and .md files |
| Theme, category colors, panels, grid, centering, captions | [Style guide](reference/STYLE_GUIDE.md) |
| Construct annotation objects | [Annotation templates](reference/annotation-templates.json) |
| Find a close complete flow | [Example selector](examples/INDEX.md) |
| Discover a missing parameter value | [Supplemental API evidence](reference/api/README.md), only when needed |
| Diagnose a failure | [Failure patterns](reference/FAILURE_PATTERNS.md) |
| Check historical claims | [Evidence](reference/EVIDENCE.md) or archive/; not routine build input |

There are 35 documented processing types and eight complete synthetic teaching patterns. A documented node is not proof of every option or runtime behavior. Forecast SSA is not documented. Example resource IDs are synthetic or historical; supply actual target bindings.

## Supply copied Table Input nodes

Add/select the required tables and fields as Table Input nodes in ClicData, copy those nodes and share their JSON. Inputs in an existing whole-flow export also qualify. VMF migrations can also use verified MasterDB configuration metadata supplied by the user under AGENTS.md. The JSON already carries dataset/column IDs, names and exact types. See the [copied-input procedure](reference/SCHEMA_FILES.md#copied-table-input-json). Verify source selections after import.

## Pivot and JSON inputs

Pivot category lists and JSON structures require a manual supplement: provide a safe distinct-value list collected locally for each required pivot column, and dummy JSON examples for selected fields being extracted or expanded. Keep JSON keys/nesting/types, replace values with invented ones. Copied inputs cannot establish categories or JSON structures. See the [intake procedure](reference/SCHEMA_FILES.md#manual-supplement-for-pivot-and-json).

## Normal workflow

Start by identifying the task: **create/modify an entire Data Flow**, **optimize an existing Data Flow**, or **Views/Merges/Fusions migration**. Reuse a clear selection in the user's request; otherwise ask which route they need. See [task selection](AGENTS.md#determine-the-task-first). VMF migration is a developing workflow; its planned metadata discovery and production cutover are not implemented by this routing update.

New business flows end in dedicated **dummy Table Output nodes**, one per business result, with mapped columns and a full-refresh (`rebuild`) default. Users create/select the destination tables from these nodes in ClicData; destination IDs are not required in advance. Unbound nodes omit DataCloneRecId and need that editor step before execution. Input source bindings still require real metadata. Existing output settings remain unchanged during unrelated edits. See [Build guide](reference/BUILD_GUIDE.md#output-writes).

1. Supply business requirements and copied Table Input JSON, plus optional supporting schemas; see the schema-file guide. No client-data connection is required. Read only the task-specific references.
2. Patch the latest export for edits; assemble new flows with code where possible.
3. Validate the actual deliverable with `python3 scripts/lint_flow.py path/to/flow.json`.
4. Test import and data behavior separately in ClicData. Local checks do not establish engine execution.

For layout, use `python3 scripts/style_flow.py --help` after reading the style guide. Screenshots and [visual examples](reference/VISUAL_GUIDE.md) are optional appearance evidence, not required processing input.

## Reference-pack maintenance only

- `python3 scripts/test_linter.py`: linter regressions.
- `python3 scripts/validate_reference_pack.py`: all canonical synthetic examples.
- `python3 scripts/check_reference_structure.py`: routing, links, catalogs and documentation structure.
- `python3 scripts/build_reference_pack.py`: intentionally rebuilds teaching examples; overwrites canonical files. Do not run during client builds.

The complete pre-reorganization README and instructions are preserved in archive/ for provenance. Current rules live in AGENTS.md and the focused guides. Node guides retain the detailed settings and limitations from that reference; later discoveries should be added there.
