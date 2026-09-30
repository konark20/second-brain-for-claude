---
name: session-memory
version: 1.0.0
trigger: end of a working session, or start of a session that continues prior work
inputs: the session's work, 05-Journal/ entries, the project HANDOFF.yaml if any
outputs: an appended observation to 05-Journal/, a refreshed HANDOFF.yaml, no external calls
depends_on: project-handoff, 99-Meta/skills/daily.md, BOUNDARIES.md
---

# Session Memory

## Purpose

Cross-session continuity without a third-party memory service. claude-mem and claude-subconscious solve the "Claude forgets between sessions" problem by shipping captured tool-usage to a cloud model, which conflicts with BOUNDARIES (no vault content to unapproved external services, no PII leaving the machine). This skill is the vault-native answer: it builds the same continuity from the journal and HANDOFF files already in the repo, entirely local, sentinel-visible, nothing leaves the machine. Observational, not directive: it records what happened, it does not editorialize.

## When to use

- Ending a session that produced real work worth carrying forward.
- Starting a session that continues a project; load the last observation and HANDOFF first.
- The owner asks "where did we leave off" on a project.

## When NOT to use

- Trivial sessions with nothing to carry. Silence is fine; do not manufacture an observation.
- As a replacement for the journal's daily narrative. This is the continuity layer, [[daily]] is the day's log.
- To store anything on the BOUNDARIES blocklist. Government ID numbers, credentials, real sensitive data never enter an observation, same as everywhere else.

## Procedure

### Session end

1. Write one observation block to today's `05-Journal/` entry under `## Session memory`:
   - `did`: what changed this session, concrete, file-level.
   - `decided`: choices made and the one-line why.
   - `next`: the immediate next step for the future session.
   - `gotcha`: anything that burned time, so it is not rediscovered.
2. If the session touched a project, refresh `HANDOFF.yaml` next to that project's `_hub.md`, in the format defined by [[project-handoff]] (`current_state`, `next_steps`, `architecture`, `conventions`). Update the hub's status paragraph if it changed materially. A handoff files the state for the next worker; the journal records the day. Existing HANDOFF.yaml files in the older `done / next / state / pitfalls / decisions` shape stay valid and migrate the next time they are touched. Skip for trivial sessions.
   - This absorbed the handoff-writer skill on 2026-09-20. It listed a second schema that disagreed with project-handoff, so project-handoff is the single definition.
3. Keep it factual and terse. No reflection, no advice, no restating the conversation.

### Session start (continuation)

1. Read the most recent `## Session memory` block for the project and its `HANDOFF.yaml`.
2. Surface `next` and any open `gotcha` in one line before starting: `resuming <project>: next was <x>, watch <gotcha>`.
3. Do not act on it automatically; it is context, not an instruction.

## Durable memory blocks (per project)

Beyond the per-session observations, each project hub may carry a `## Memory` section with these standing blocks, refreshed rather than appended. Schema borrowed from claude-subconscious's memory architecture, trimmed to what earns its place here and kept local:

- `preferences`: coding style, tool choices, communication style learned from the owner's corrections. Overlaps USER_PROFILE; keep only project-specific deltas here.
- `context`: the project's architecture decisions and known gotchas.
- `patterns`: recurring behaviors or repeated struggles worth naming.
- `pending`: unfinished work and explicit TODOs (mirror to the hub's `## Tasks` checkboxes).

Rules for the blocks: observational voice, updated in place not appended, never carrying anything on the BOUNDARIES blocklist, and never a substitute for FOUNDATION or USER_PROFILE which remain canonical. If a "preference" contradicts USER_PROFILE, USER_PROFILE wins and the block is wrong.

## Style rules

- Observational voice: "changed X", "chose Y because Z". Never "you should".
- Everything local. This skill never calls an external service. If continuity ever seems to need cloud memory, that is a BOUNDARIES amendment, not a workaround.
- No em dashes, no AI-sounding language.

## Links

- [[project-handoff]]
- [[daily]]
- [[weekly-review]]
- [[BOUNDARIES]]
