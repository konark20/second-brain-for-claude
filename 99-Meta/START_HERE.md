---
type: meta
layer: 1
status: active
tags: [entry-point, bootstrap]
---

# Start Here

> The one file to hand a new chat, a newly connected folder, or any session that has not touched this vault before. Read it in full before doing anything else. It is a map to the authoritative files, not a replacement for them. When in doubt, the file it points to wins.

## The boot prompt

> This is my second-brain vault. Read `99-Meta/START_HERE.md` in full before doing anything else, then proceed with the request below.

That line plus the task is the whole bootstrap. In Claude Code, `/brain <task>` does the same thing.

## First run

If `99-Meta/onboarding/progress.yaml` says `not_started`, stop here: greet the owner with `99-Meta/onboarding/welcome.md` and run the onboarding interview (`99-Meta/skills/vault/onboard.md`). It asks one question at a time with suggested answers, saves progress after every answer, and can resume across sessions. If it says `in_progress`, offer to resume after the current task.

## Read in this order

1. `99-Meta/FOUNDATION.md`: the constitution. If it is missing or unreadable, stop and tell the owner.
2. `99-Meta/USER_PROFILE.md` and, once it exists, `99-Meta/onboarding/portrait.md`: who the owner is and how they want to be spoken to.
3. `99-Meta/BOUNDARIES.md`: hard rules, non-negotiable.
4. `99-Meta/ACTIVE_SESSION.md`: check for another assistant writing right now.
5. `99-Meta/VAULT_MAP.md`: where things live.
6. `99-Meta/SKILL_MAP.md` and `SKILL_INDEX.md`: every agent and skill, with when to use and when not.
7. `99-Meta/MODEL_SELECTOR.md`: which model tier does what.
8. `99-Meta/PIPELINE.md` and `FLOWCHARTS.md`: the architect, builder, coder ticket pipeline.
9. `99-Meta/HOW_TO_BRIEF.md`: how to phrase requests and how much ceremony each needs.

Files 1 to 4 are the minimum. Read 5 onward when the task needs them.

## Rules that apply no matter what (full text in BOUNDARIES.md)

- Never delete a note. Move it to `04-Archives/`.
- Never mass-rewrite existing content without showing a diff first.
- Nothing leaves the machine (git push, email, upload) without a sentinel pass.
- Never store ID numbers, card or bank numbers, passwords or API keys in any note.
- Never send, submit, apply or pay on the owner's behalf. Drafts only.
- Never spend money without the owner confirming that specific action.
- One skill, one agent, one job.
- If uncertain, say so. Never fabricate.

## The system in one paragraph

The [[navigator]] sizes every request. A quick question needs no ceremony. A known job (capture a thought, process the inbox, ingest a link, draft an email) goes straight to the matching skill. Real project work goes through the ticket pipeline: [[architect]] scopes it into `TICK-NNN.yaml` files, [[builder]] turns each into an exact plan, [[coder]] executes it as a tight diff. [[janitor]] handles hygiene at session end and weekly. [[librarian]] tags and indexes new content as it is created. [[skill-creator]] turns repeated patterns into new skills, always drafted for approval. [[sentinel]] is the one gate that is never skipped.

## Every substantive reply starts with a routing line

```
Routing: <task type> -> <agent or skill, or "no match, proceeding generically">
```

This lets the owner see at a glance whether the session actually followed the system.
