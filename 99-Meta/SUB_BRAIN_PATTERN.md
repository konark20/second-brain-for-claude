---
type: meta
layer: 2
status: active
owner: system
created: 2026-07-22
tags: [pattern, architecture, sub-brain]
---

# Sub-brain pattern

> Extracted from the original author's job-applications "Resume Brain", which proved it. This documents a reusable way to scale a single project into its own coordinated system without forking the main brain. Reference from a project hub when the project outgrows a flat set of notes.

## When a project earns a sub-brain

Most projects do not need one. A project earns a sub-brain when all of these hold:

- It runs a repeatable multi-step pipeline (not one-off tasks).
- The pipeline needs several distinct specialist roles, not one skill.
- It has its own body of rules and data stores that would clutter the main brain if globalized.

The Resume Brain qualified: a JD-to-materials pipeline with jd-decoder, organiser, bullet-writer, number-miner, layout-guard, interview-defender, and dossier-keeper, plus its own RESUME_RULES and data stores.

## The holding-company model

Think of the vault as a holding company and the sub-brain as one operating company under it.

- **One coordinator.** A single agent runs the pipeline and delegates. Resume Brain: `resume-builder`.
- **Native specialists** live in the main `99-Meta/skills/` and `99-Meta/agents/` folders (so the janitor and indexes see them) but serve one project. They must be registered in SKILL_MAP/SKILL_INDEX under a project-scoped heading, or they drift.
- **Borrowed staff.** Main-brain agents (navigator, librarian, sentinel, architect, web-research) take secondary, project-scoped roles rather than being duplicated. The sub-brain does not re-implement sentinel; it uses it.
- **Its own map and rules.** A `<PROJECT>_SKILL_MAP.md` mirrors the main SKILL_MAP at project scope, and a `<PROJECT>_RULES.md` consolidates every project decision into numbered enforceable rules. BOUNDARIES always wins on conflict.
- **Single source per data store.** One canonical file per kind of data (archive, bank, inventory, cache, tracker), with a defined update order.

## Rules that keep it from becoming a second silo

1. Native specialists register in the main SKILL_MAP/SKILL_INDEX under a project-scoped section. No hidden skills.
2. BOUNDARIES is the holding-company law and always wins over any project rule file.
3. The sub-brain borrows main agents; it never re-implements navigator, sentinel, librarian, or architect.
4. The project hub links the sub-brain's map and rules so a cold session finds them.

## How to stand one up

1. Confirm the project meets the "earns a sub-brain" test above. If not, keep it flat.
2. Name the coordinator (existing agent or a new one via [[skill-creator]]).
3. Write `<PROJECT>_RULES.md` (numbered) and `<PROJECT>_SKILL_MAP.md` (mirrors SKILL_MAP at project scope).
4. Build only the specialist skills the pipeline genuinely needs, one job each, in the main folders, and register them.
5. Link both files from the project hub. Point the main SKILL_MAP's "Project sub-brains" table at the new map.

## Candidates in your vault

- Writing pipelines (topic, research, outline, draft, edit, publish), client-delivery pipelines, hiring pipelines and trading books are typical candidates.
- Do not sub-brain a project just because it is active. Flat is fine until the three tests all hold.

## Links

- [[SKILL_MAP]]
- [[FOUNDATION]]
- [[BOUNDARIES]]
