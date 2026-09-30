---
type: meta
layer: 3
status: active
owner: system
tags: [pipeline, model-routing]
---

# Pipeline — Architect / Builder / Coder

> Layer 3 addition to the four-layer system in [[FOUNDATION]]. Three agents, three model tiers, one ticket file carrying state between them. Purpose: keep the most expensive model (coding) doing the least open-ended thinking, by front-loading scoping and research onto cheaper/faster tiers.

## The idea

| Stage | Agent | Default model | Job |
|---|---|---|---|
| 1 | [[architect]] | sonnet | Linear thinking. Turns a goal into scoped, ordered tickets. What and why, never how. |
| 2 | [[builder]] | fable | Heavy lifting. Turns a ticket's "what" into an exact "how" — research, exploration, sequencing, risk-spotting. |
| 3 | [[coder]] | opus (ceiling) | Tight loop. Reads the finished plan, writes the diff, tests it, reports. No exploration, no re-deciding scope. |

The model column is a default, not a hardcoded binding. Architect stamps a `suggested_model` per ticket for the builder and coder stages using [[MODEL_SELECTOR]]'s decision rule — three comparison tests so far found sonnet performs identically to opus on well-specced, bounded coding and debugging work, so many tickets should run coder on sonnet, not opus. See `MODEL_SELECTOR.md` for the evidence and the live decision rubric; this table is the starting point, not the rule.

The ticket file (`templates/ticket.yaml`) is the handoff mechanism between stages, same pattern as [[project-handoff]]: state lives in a file, not in conversation memory, so any agent, session, or model can pick up a ticket without replaying the chat that produced it.

## Ticket lifecycle

```
draft --(architect)--> specced --(builder)--> coding --(coder)--> review --> done --> archived
```

- **draft**: architect has filled the `architect:` block. Goal, acceptance criteria, files touched, dependencies, out-of-scope.
- **coding**: builder has filled the `builder:` block. Approach, sequence, research notes, risks. (Ticket schema uses `coding` as the status builder sets when handing to coder — see `templates/ticket.yaml`.)
- **review**: coder has filled the `coder:` block. Diff summary, tests, status notes. Waiting on the owner or self-correction pass.
- **done**: reviewed and accepted.
- **archived**: moved with the project when it closes, per [[VAULT_MAP]] `01-Projects` lifecycle.

Tickets live at `01-Projects/<project>/tickets/TICK-NNN.yaml`. [[TICKET_INDEX]] holds the cross-project at-a-glance view; the ticket file itself is the source of truth.

## Where tickets live and why (scalability)

Per-project storage, not one global ticket file, for the same reason [[SKILL_MAP]]/[[SKILL_INDEX]] split detail from index:

- Each project's tickets scale with that project only — a 50-ticket project doesn't bloat a file every other project has to load.
- Git- and Obsidian-friendly: one file per unit of work, diffable, greppable, linkable.
- `TICKET_INDEX.md` gives the bird's-eye view (what's active, whose court is it in) without duplicating ticket content — same split as detail-file vs index-file used everywhere else in this vault.
- New projects need zero setup beyond a `tickets/` subfolder; the pattern doesn't need a schema migration to add a project.

## Running the pipeline live in this environment

This Cowork/Claude Code session does not have `architect`, `builder`, `coder` registered as literal subagent types — the available types are the generic ones (`claude`, `general-purpose`, `Plan`, `Explore`, etc.) plus a `model` override parameter. The bridge is: **dispatch a general-purpose agent, and hand it the relevant persona file as its instructions.**

Concretely, to run one stage:

```
Agent({
  description: "Architect: scope <feature>",
  subagent_type: "general-purpose",
  model: "sonnet",
  prompt: "Read 99-Meta/agents/architect.md in full and follow it exactly.
           Goal: <the request>. Project: <project-slug>.
           Read the project's _hub.md and any existing tickets first."
})
```

Then for builder:

```
Agent({
  description: "Builder: spec TICK-004",
  subagent_type: "general-purpose",
  model: "fable",
  prompt: "Read 99-Meta/agents/builder.md in full and follow it exactly.
           Ticket: 01-Projects/<project>/tickets/TICK-004.yaml."
})
```

Then coder:

```
Agent({
  description: "Coder: implement TICK-004",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "Read 99-Meta/agents/coder.md in full and follow it exactly.
           Ticket: 01-Projects/<project>/tickets/TICK-004.yaml."
})
```

The calling session (whatever model is driving the conversation) plays the role of orchestrator between stages: reads each agent's report, checks the ticket file updated correctly, and only then dispatches the next stage. It does not need to be Sonnet itself, though Sonnet is the natural fit since routing is exactly its job elsewhere in this system (see [[navigator]]).

## When NOT to use this pipeline

- Trivial fixes. One-line changes don't need three agents and a YAML file.
- Pure exploration/research with no coding outcome — that's [[context-management]] or a plain research pass, not a ticket.
- Anything where the owner wants to design and code in the same breath, in one conversation. This pipeline is for work worth the separation-of-concerns overhead.

## Open design questions (unresolved, flag if relevant)

- Whether Builder should be allowed to write throwaway spike code to de-risk a plan, or stay strictly non-code. Currently: stay non-code, keep the boundary clean.
- Whether `coding` should split into two statuses (`specced` after builder, `coding` once coder starts) for finer-grained tracking. Currently collapsed into one to keep the schema simple; revisit if tickets start sitting ambiguously.

## Links

- [[FOUNDATION]]
- [[architect]]
- [[builder]]
- [[coder]]
- [[TICKET_INDEX]]
- [[TICKET_BOARD]] (live Dataview board over all tickets)
- [[FLOWCHARTS]] (visual version of this pipeline and the ticket lifecycle)
- [[project-handoff]]
- [[navigator]]
- [[MODEL_SELECTOR]]
