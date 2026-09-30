---
tags: [skill, workflow]
name: skill-orchestrator
version: 1.0.0
description: "Use this skill at the start of any new project or substantial task, before reaching for any single skill, to decide which combination of the user's saved Secondary Brain skills apply and in what order. Trigger for 'I'm starting a new project,' 'help me set this up,' 'what skills should I use for this,' or any request that spans multiple phases (planning, building, documenting, handing off) where more than one skill in skills/ is relevant. Also trigger when it's unclear which single skill fits, since this skill's job is to map a request to the right sequence of skills and hand off cleanly between them. Reads the Secondary Brain skills/ index first, then plans the chain before doing the work. Does not replace any individual skill's logic — it decides which skills to invoke and in what order, then defers to each one for the actual execution."
---

# Skill Orchestrator

This skill turns the Secondary Brain's `skills/` folder from a flat pile of individual skills into a toolkit that gets applied deliberately. Instead of picking one skill that seems closest and running with it, this skill first figures out which combination of saved skills the project actually needs, and in what order their outputs feed each other.

## Step 1: Read the full index, not just the README

Read, in order: `99-Meta/SKILL_INDEX.md` (every skill and agent in the brain, tagged), `99-Meta/SKILL_MAP.md` (when/when-not rules), and the vault `README.md`. The README alone is not the inventory — it summarizes; SKILL_INDEX is authoritative. The pool to draw from is all three groups: portable skills in `skills/`, vault workflow skills in `99-Meta/skills/`, and agents in `99-Meta/agents/`. A chain that only ever considers `skills/` will systematically miss web-research, connect, ingest-url, lint-vault, and every agent. If the indexes disagree with what's on disk, reconcile against disk and update them before proceeding.

If the project being launched has a `_hub.md` with an "Agents and skills assigned" section, that list is the starting chain — extend or prune it, don't rediscover it from scratch.

## Step 2: Classify the incoming request

Identify what kind of project or task this is. Most requests fall into one of these shapes:

- **Starting something new that doesn't exist yet** (a tool, pipeline, agent, or feature) → needs upfront scoping before code.
- **Resuming or continuing existing work** (yours or someone else's, from a prior session) → needs context recovery before any changes.
- **Producing a written deliverable** (email, application answer, report, paper) → needs tone/structure work, possibly tailored to an audience.
- **Working on existing code that already runs** (refactor, extend, debug) → needs the codebase understood before it's touched.
- **A finance/trading concept or question** → needs domain teaching, not general coding skills.
- **Anything ending in a handoff** (pushing to git, ending a long session, passing to another person or agent) → needs state captured on the way out, regardless of what the earlier phase was.

Many real requests span more than one of these in sequence. That's the normal case, not an edge case.

## Step 3: Pick the chain

Once the shape is identified, assemble the skill sequence. The chain matters as much as the selection: each skill's output is the next one's input, not just a set of skills applied independently side by side.

**New project / new build:**
`project-planner` → `tdd` (if the code is substantial enough to warrant tests-first) → `data-analysis-coding` (if it involves data work) → `project-handoff` (once there's a meaningful stopping point)
The plan produced by `project-planner` becomes the `architecture` and `next_steps` seed for `project-handoff` — don't re-derive scope from scratch when the handoff file is created; carry it over.

**Resuming existing work:**
`context-management` (to explore the codebase efficiently, or read an existing `HANDOFF.yaml` first if one exists) → `project-handoff` (to update it once new work is done)
If a `HANDOFF.yaml` already exists in the project, read it before doing any exploration — that's the entire point of the file. Only fall back to `context-management`'s incremental-exploration approach if no handoff file exists yet.

**Refactor or architecture work on an existing codebase:**
`context-management` (to understand the codebase first) → `architecture-review` (to propose changes) → `tdd` (if new tests are needed to safety-net the refactor) → `project-handoff` (to record what changed and why)

**Job/program application:**
`application-tailoring` (to build the tailored content and keyword-match it to the role) → `professional-writing` (to polish tone and strip AI-sounding phrasing) → `self-correction` (final pass before sending)

**Written report, paper, or analysis writeup:**
`research-documentation` (structure and section flow) → `trading-finance-tutor` (only if the content is finance/trading-specific and needs domain accuracy) → `self-correction` (final check on claims and numbers)

**Professional correspondence (not an application):**
`professional-writing` directly, with `self-correction` as a final pass if the message is consequential (negotiation, conflict, something that can't be walked back).

**Data pipeline or analysis tool:**
`project-planner` (scope what the pipeline needs to do) → `data-analysis-coding` (build it) → `tdd` (if it's complex enough — parsers, business logic, multiple code paths) → `project-handoff` (capture data locations and gotchas, which is often the highest-value part of the handoff for this category)

**Finance/trading learning or concept work:**
`trading-finance-tutor` on its own, unless the output feeds into a report, in which case chain into `research-documentation` afterward.

**Live trading (idea, book, or review), only if the optional trading pack is installed:**
`strategy-builder` (new idea) → `event-backtest` + `payoff-check` (pre-trade; payoff-check is mandatory before any option order) → `session-cadence` (daily/weekly book work, `tilt-guard` alongside, `conviction-override` on rule-vs-trader conflicts) → `trade-analysis` (closes) → `performance-analysis` (period) → `retrospective-writer` (period end). `scenario-analysis` splices in before any known catalyst.

**Anything needing external facts (any chain above):**
splice `web-research` (via the [[researcher]] agent) in before the step that consumes the facts. Company research before a cover letter, library comparison before a build decision, current-data lookup before an analysis. Never let a chain step answer an external factual question from memory or from search snippets.

## Step 3.5: Flag the gaps, don't absorb them

If no existing skill covers a real step of the chain, do the step manually this time, but append a row to `99-Meta/PATTERN_LOG.md` describing the gap. Three rows of the same shape and skill-creator (as a skill, or as an agent for persistent roles) drafts it. Silently absorbing gaps is why the toolkit stopped growing.

## Step 4: Apply `self-correction` as a closing pass, not a separate step

`self-correction` isn't a phase like the others — it's a quality gate that runs on top of whatever the last skill in the chain produced, before handing it to the user. Apply it as the final check regardless of which chain was used, skipping it only for trivially short outputs.

## Step 5: State the chain before executing it

When a project clearly needs more than one skill, say which skills will be used and in what order before diving in — one short line, not a full plan document unless the user wants one. This keeps the sequencing visible and lets the user redirect before work starts down the wrong chain. For a single-skill task, this step is unnecessary; just use the one skill.

## Step 6: Keep the index current

If, over the course of a project, a skill gets created, edited, or removed from `skills/`, update the root `README.md` index so the next orchestration pass (this session or a future one) has an accurate map to read in Step 1. An index that drifts from reality defeats the purpose of keeping it.

## What this skill does not do

- It does not perform the work of any individual skill itself — it routes to them.
- It does not force a multi-skill chain onto a task that genuinely only needs one skill. Over-chaining wastes as much effort as under-chaining.
- It does not skip Step 1. Picking skills from memory instead of the actual current index is the most common way this goes stale.
