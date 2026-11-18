---
name: clicdata-dataflow-builder
description: Build, edit, explain, diagnose, and optimize ClicData Data Flow editor clipboard JSON, and plan legacy Views/Merges/Fusions migrations using supplied definitions. Use for ClicData flow tasks, not generic ETL or dashboard authoring.
---

# ClicData Data Flow Builder

Use this skill's bundled reference to produce ClicData editor clipboard flows for the user's own task. All paths below are relative to this SKILL.md, even when the user's working directory is elsewhere.

This entry point works in Codex and Claude. In Claude Code, invoke `/clicdata-dataflow-builder`; in Claude chat, enable the uploaded skill and request it by name. Read AGENTS.md explicitly on every platform; do not rely on automatic project-instruction discovery.

## Start here

Before each new task, check the current published reference once with `python3 <installed-skill>/scripts/sync_skill.py --cache <writable-cache-directory>`. Use a persistent user cache for local tools, or a session-writable temporary cache in hosted ChatGPT/Claude. This accesses only this public repository, never client sources. Do not send client content in requests.

The helper compares release versions and downloads only when different. Read SKILL.md and AGENTS.md from the returned `path` and use that directory for all references and scripts for the rest of the task. Do not repeat the check when reading that updated entry point in the same task. Keep the chosen version fixed during a task. Cached copies are separate from installed platform-managed skills and user artifacts.

If network/tool access or writable storage is unavailable, state that the update check failed and that the bundled version is being used; do not claim it is current. Never bypass platform permissions or overwrite platform-managed installations. Hosted caches may disappear between chats: this updates the working copy for the task, not the account's installed skill. Local persistent caches reuse the updated copy on subsequent tasks.

Read [AGENTS.md](AGENTS.md) before working. Its standing rules and task-to-reference table govern this workflow. Then read only the files needed for the actual task; do not preload the repository or all examples. If a required bundled file is missing, report the incomplete installation instead of inventing its contents.

Apply AGENTS.md's initial task selection: create/modify an entire Data Flow, optimize an existing Data Flow, or Views/Merges/Fusions migration. Ask only when the intended route is unclear. Migration automation is under development; follow the build guide's migration limitations before proposing discovery or cutover actions.

Start with the business use case and desired result. If only schemas are supplied, ask what the flow must accomplish and wait before asking for field selections or bindings. For edits, use the latest user-supplied clipboard export as the sole baseline.

Use user-supplied Table Input clipboard JSON for new flows and ordinary edits. For VMF migrations, AGENTS.md also allows sanitized MasterDB configuration metadata supplied by the user when it establishes complete source bindings. Do not use account connections, MCP, APIs, or browser sessions to collect inputs. Never query or read source records, previews, samples, counts, aggregates, or distinct values, including on QA/dummy tables. Users perform ClicData previews and execution.

## Focused reference

- Intake and optional schema checks: [reference/SCHEMA_FILES.md](reference/SCHEMA_FILES.md).
- New flows, processing changes, and optimization: [reference/BUILD_GUIDE.md](reference/BUILD_GUIDE.md).
- New graph/schema structures: [reference/SERIALIZATION.md](reference/SERIALIZATION.md).
- New layouts or styling changes: [reference/STYLE_GUIDE.md](reference/STYLE_GUIDE.md). Ask light or dark theme for a new styled flow if unknown.
- Errors: [reference/FAILURE_PATTERNS.md](reference/FAILURE_PATTERNS.md), the actual error, and the affected branch.
- Unfamiliar node Codes/classes: [reference/node-catalog.json](reference/node-catalog.json), then only the relevant `reference/nodes/<code>.json` and `.md`.
- A construction pattern: [examples/INDEX.md](examples/INDEX.md), then at most one close example initially. Example bindings are not client bindings.

Pivot categories and selected JSON structures need manual supplements as described in AGENTS.md. Never infer complete categories or JSON paths from metadata; ask for user-collected safe categories or user-created dummy JSON preserving keys, nesting, and types.

## Deliver and validate

Write task artifacts in the user's working directory or requested destination, outside the installed skill. Preserve unrelated properties when patching flows. Follow AGENTS.md for dedicated dummy Table Outputs, unbound destinations, exact serialization, and disabled checkpoints. Do not execute remote flows.

Run `python3 <skill-directory>/scripts/lint_flow.py <deliverable.json>` using the resolved absolute skill directory. Add targeted preservation, schema, or geometry checks appropriate to the change. Use `--require-disabled-outputs` only for teaching examples. Do not run `build_reference_pack.py` for a user flow.

Deliver the complete JSON file when known, a brief result, material assumptions, actual validation, and remaining editor checks. Mark unresolved bindings and manual dependencies explicitly; local linting does not establish editor import or engine execution.
