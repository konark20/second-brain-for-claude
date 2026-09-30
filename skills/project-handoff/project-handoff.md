---
tags: [skill, workflow]
name: project-handoff
version: 1.0.0
description: "Use this skill to create and maintain a project handoff file — a single structured YAML document that lets another agent, model, or person pick up a coding project without re-reading the whole codebase or re-deriving its history. Trigger when work is being handed off (pushed to git, passed to another model/agent/person), when a long coding session is winding down with significant work done, after hitting and resolving a notable error, or when the user explicitly says 'update the handoff' / 'create a handoff file.' The file is designed to be read first, before any code, so a fresh agent learns what's done, what's left, where data lives, and what pitfalls to avoid — without running anything. Pairs with context-management (which governs reading it efficiently)."
---

# Project Handoff Manifest

This skill produces and maintains a single handoff file that carries a coding project's state across sessions, agents, and people. The problem it solves: when a project moves to a new session, a different model, git, or another person, all the context built up (what's done, why decisions were made, what errors were hit, where data lives) is normally lost, forcing the next worker to re-explore the repo and re-derive history. That re-exploration burns time and tokens. A good handoff file is read once, top to bottom, and replaces most of that re-exploration.

The file is meant to be **read first, before any code is run or explored**, and it should make running the code unnecessary just to understand the project.

## Format: YAML, one file per project

Use a single YAML file per project (default name `HANDOFF.yaml` at the repo root), continuously updated rather than a new file per session. YAML is chosen over JSON because it cleanly holds both structured fields (paths, statuses, dependencies) and multi-line prose (why a decision was made, what an error was), while staying readable to humans and parseable by agents.

The file is structured so the most immediately useful information is at the top (current state, what to do next) and the historical/reference material (changelog, error log) is lower down. A fresh agent reads top-down and can stop as soon as it has what it needs.

**Starting from a project plan:** if a `PROJECT_PLAN.yaml` already exists (created by the project-planner skill), don't maintain both files. When implementation starts, merge the plan into `HANDOFF.yaml`: the plan's `capabilities` and `tasks` become the basis for `current_state` and `next_steps`, the plan's `architecture` carries over directly, and the plan's `existing_resources` informs the handoff's `architecture.dependencies`. One file, one source of truth.

## File structure

```yaml
project:
  name: <project name>
  purpose: <one or two lines: what this project does and why it exists>
  last_updated: <date/time of this update>
  updated_by: <which session/agent/person made this update>

current_state:
  summary: <short prose: where things stand right now, the single most useful paragraph>
  working: <what is functional and verified right now>
  not_working: <what is known broken or incomplete>

next_steps:
  - step: <concrete next action>
    why: <what it accomplishes / why it matters>
    where: <which file(s) or component this touches>
  # ordered by priority, most important first

architecture:
  entry_point: <where execution starts: main file, CLI, notebook>
  key_files:
    - path: <file path>
      role: <what this file is responsible for>
      key_items: <important functions/classes, not every helper>
  data:
    - what: <what data this is>
      location: <where it lives: path, DB, API>
      how_to_access: <how to load/query it, format, gotchas>
  dependencies: <key libraries/services and versions if they matter>

run_instructions:
  setup: <how to set up the environment, install deps>
  run: <exact commands to run the main pipeline/script>
  test: <exact command to run tests, if any exist>
  expected_output: <what correct output looks like, so it can be verified without guessing>

conventions:
  - <project-specific rules a new worker must follow: naming, diff-only edits, LaTeX notation, no running real data, etc.>

# --- reference / history below this line: read only if needed ---

error_log:
  - error: <what went wrong>
    cause: <root cause, once understood>
    resolution: <how it was fixed, or current status if unresolved>
    date: <when>
  # most valuable section for avoiding repeated mistakes — keep separate from current_state so it doesn't clutter

changelog:
  - date: <date>
    by: <session/agent/person>
    changes: <what was done in this session, briefly>
```

Not every section is mandatory on every project. Omit sections that genuinely don't apply (e.g. `test` if there are no tests yet), but keep the skeleton consistent so a reader always knows where to look.

## When to create or update the file

Update the handoff file at these checkpoints:

- **When a long session is winding down with significant work done.** If a lot has been accomplished and the session looks like it's nearing its end, update the file so none of that context is lost before it's handed off. Since a skill can't literally watch a clock, treat this as: when a meaningful chunk of work has accumulated and a natural stopping point is reached, update before stopping.
- **After hitting and resolving a notable error.** When a real error was encountered and worked through, add it to `error_log` while the details are fresh. This is one of the highest-value parts of the file, since it stops the next worker (or the next session) from falling into the same trap.
- **When the owner explicitly asks** ("update the handoff," "create a handoff file," "get this ready to hand off").

Don't update the file after every trivial change, that creates noise and churn. Update at meaningful checkpoints, not continuously.

## How to write each section well

**current_state.summary** is the single most important field. Write it so that if someone read only this paragraph, they'd understand where the project stands. Concrete and specific: "Parser handles TT and ADL formats correctly; ASE format is stubbed but not implemented. Output writes to CSV but the timestamp column is still in UTC and needs converting to ET." Not vague: "Made good progress on the parser."

**next_steps** must be actionable, not aspirational. "Implement ASE parsing in `parsers/ase_parser.py` following the TT parser pattern" is actionable. "Improve the parser" is not. Order by priority so the next worker knows what to pick up first.

**data.how_to_access** is where a lot of re-exploration time is lost, so be specific: file format, how to load it, any quirks (encoding, schema, namespaces). For the owner's work this often matters a lot (e.g. XML namespace stripping, schema-agnostic parsing), so capture those gotchas explicitly.

**error_log** entries should capture the *cause and resolution*, not just the symptom. "Got a KeyError" is useless later; "KeyError on Price field because ADL uses 'Px' not 'Price' as the attribute name, fixed by mapping field names per system" prevents the next person from rediscovering it.

**conventions** should capture the project-specific rules that aren't obvious from the code, including any of the owner's standing preferences that apply (diff-only edits, never running code against real data, LaTeX notation standards, etc.) so a different agent or model follows them too.

## How a fresh agent should use this file

When this skill is active and a `HANDOFF.yaml` exists, the correct first move on entering a project is to read it before exploring code or running anything. The file is designed so that:

1. `project` + `current_state` tells you what this is and where it stands (read first)
2. `next_steps` tells you what to do
3. `architecture` + `run_instructions` tells you where things are and how to run them, without exploring
4. `conventions` tells you the rules to follow
5. `error_log` + `changelog` are reference, consult only if relevant

This ordering means a new agent can often start productive work after reading just the top half of the file, which is the whole point: less re-exploration, fewer tokens, faster handoff.

**Keep the chain alive.** A receiving agent, model, or person isn't just a consumer of this file, they become the next author of it. After doing their own work, they should update `HANDOFF.yaml` the same way (current state, next steps, any errors hit, changelog entry) before they in turn hand off or push. A handoff file only stays useful if every hand that touches the project updates it, otherwise it goes stale after the first pass and misleads everyone after that.

## What to avoid

- **Don't let the file go stale.** A handoff file that says "next: implement X" when X was finished three sessions ago is worse than no file, since it actively misleads. If updating, make sure `current_state` and `next_steps` reflect reality.
- **Don't dump everything.** This is not a transcript of the session. It's a curated state document. Capture what the next worker needs, not every step that was taken.
- **Don't bury the current state in history.** Keep `current_state` and `next_steps` at the top and accurate. The changelog and error log are reference material and stay below.
- **Don't reproduce code in the file.** Reference file paths and function names, don't paste implementations. The code lives in the repo; the file points to it.
