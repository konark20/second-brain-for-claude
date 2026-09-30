---
type: meta
layer: 4
status: active
owner: system
tags: [interface, how-to]
---

# How to Brief This System

> Layer 4. Practical answer to "how do I hand you a project or task." Three sizes of request, what to include, and how model/agent selection happens so you don't have to think about it unless you want to override it.
>
> If this is a brand new chat or newly connected folder that hasn't seen this vault before, point it at [[START_HERE]] first — that's the single file to hand a fresh session so it loads the rules, the pipeline, and the current state before doing anything.

## The three sizes of request

**1. Quick chat.** A question, a lookup, a small edit, thinking out loud. No ceremony. Just talk. This is most of what happens day to day and it should stay that way — don't wrap something small in ticket machinery.

**2. Skill or agent-shaped work.** A known, bounded job that already has a skill or agent for it: process the inbox, write today's journal, tailor a resume to a JD, run a weekly review, tag and file something new. Just say what you want in plain language ("tailor my resume to this posting," "process my inbox") and [[navigator]] routes it to the right skill or agent. You don't need to name the skill.

**3. Project or ticket-shaped work.** Real scope: multiple files, spans more than one sitting, needs tracking, or has real ambiguity worth scoping before anyone writes code. Say "architect this" or "make tickets for X" and [[architect]] scopes it into `TICK-NNN.yaml` files, which then move through [[builder]] and [[coder]]. This is worth the overhead when a task is big enough that losing track of it mid-way would actually cost you something. It is not worth it for a one-line fix.

If you're not sure which size a request is, just describe the goal — Navigator or Architect will tell you if it's bigger or smaller than you think, rather than you having to guess the right ceremony upfront.

## What to include in a brief, for any size

- **The goal in one line.** What does done look like.
- **Which project it belongs to**, or "new project" if it isn't one yet. Everything eventually needs a home in `01-Projects/` or `02-Areas/`.
- **Stakes and ambiguity, if you know them.** Does this touch real data, credentials, money, or something hard to undo? Say so explicitly — that's what pushes a ticket to opus regardless of how simple it looks (see [[MODEL_SELECTOR]] rule 1). Is the request itself underspecified and you want judgment calls made? Say that too, rather than letting Architect guess.
- **Constraints that aren't obvious from the code.** Deadlines, things you've already tried, decisions you've already made that shouldn't get re-litigated.

You do not need to specify a model. That is what [[MODEL_SELECTOR]] is for — Architect assigns it per ticket. You can always override it directly ("use opus for this one, it's touching real sensitive data") and that overrides the rubric.

## Explicitly invoking a pipeline stage

Usually you won't need to — Navigator handles dispatch. But if you want to be direct:

- "Architect a plan for X" — scopes tickets, doesn't write anything else.
- "Run builder on TICK-004" — specs out the how, doesn't write code.
- "Have coder implement TICK-004" — executes a ticket that's already specced.
- "Compare models on X" — runs the same task across sonnet/fable/opus and logs the result to `MODEL_SELECTOR.md`'s evidence log, same pattern as the three tests already on file.

## When you want a new skill or agent built

Don't design it yourself first unless you want to. Just describe the repeated need ("I keep having to manually cross-reference these two files") or ask directly ("make an agent that tags new notes as they're created"). [[skill-creator]] drafts both: one-shot procedures as skills, persistent roles with a model bound to them as agents. It writes to a `proposed/` folder for your review, nothing goes active without approval.

## The departments, at a glance

Think of the agents as departments rather than individual tools. Full roster and current model assignments live in [[MODEL_SELECTOR]]; the short version:

- **Navigator** — routes every request to the right place.
- **Architect / Builder / Coder** — the project pipeline: scope, plan, execute.
- **Janitor** — end-of-session and weekly hygiene, fixes rot.
- **Librarian** — tags and documents new content as it's created, keeps indexes current.
- **Skill-creator** — notices repeated patterns, formalizes them into new departments, on request or on their own trigger.
- **Domain coordinators** — agents you add for your own sub-brains (see [[SUB_BRAIN_PATTERN]]).

## What this doesn't replace

None of this stops you from just talking. The system exists to catch the work that's big enough to need tracking, or repetitive enough to be worth formalizing. Most conversations should still just be conversations.

## Links

- [[START_HERE]]
- [[FOUNDATION]]
- [[navigator]]
- [[PIPELINE]]
- [[MODEL_SELECTOR]]
- [[skill-creator]]
