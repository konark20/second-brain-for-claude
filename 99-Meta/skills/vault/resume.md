---
name: resume
version: 1.0.0
trigger: start of a working session that continues yesterday's work, or any time the owner asks "where did I leave off"
inputs: 05-Journal/ latest entries, open run manifests, TICKET_STATUS.md, HANDOFF.yaml files
outputs: a short where-you-left-off report and one recommended next action
depends_on: context-loader, brief, maestro, TICKET_INDEX.md, BOUNDARIES.md
---

# Resume

## Purpose

Answers one question: what was I doing, and what is the next move. [[context-loader]] loads who the owner is and what the rules are; this skill loads *where the work stopped*.

The distinction matters because none of the mechanical resume layers carry meaning. A terminal multiplexer can restore a desk layout. `claude --continue` restores a conversation. Neither tells you that a run is half-finished, that three lanes returned audits nobody has read, or that a decision has been waiting two days. Only the vault knows that, because only the vault is written down on purpose.

## When to use

- First session of the day, or the first after a reboot.
- Picking up a project that has been idle for more than a day.
- After any Maestro run that ended with lanes blocked or reports unread.

## When NOT to use

- Mid-session. You already have the context; rereading it is noise.
- A brand new project with no history. There is nothing to resume.

## Procedure

1. Read the two most recent files in `05-Journal/`. The `next:` lines are the highest-signal thing in the vault: they are what the previous session believed should happen now.
2. Find open run manifests: `01-Projects/*/runs/RUN-*/manifest.yaml` and any `RUN-*.yaml`. Report any whose `outcome`/`status` shows lanes still `blocked`, `partial`, or unread.
3. Read `99-Meta/generated/TICKET_STATUS.md` for what is in progress, and note anything sitting in `review` (waiting on a human, not on an agent).
4. Collect anything marked `blocked_on_owner` or `needs_human` across those manifests and results. These are the real queue; everything else can proceed without them.
5. If you run several terminals or agent panes, check which are still live, so a second session is not started on work already open elsewhere.
6. Report in [[brief]] format, then name **one** recommended next action. Not a menu.

## Style rules

- Short. This is a status read, not a briefing document. If it runs past a screen, it has failed.
- Distinguish "waiting on the owner" from "waiting on an agent". They can only act on the first kind.
- Never re-summarize completed work they have already seen. Only what is open.
- One recommendation, with the reason in a clause. If two things genuinely tie, say so in one line.
- No em dashes, no emoji, no AI-sounding language.

## Concurrency check

Step 5 exists because two Claude sessions editing one vault will clobber each other. This happened on 2026-07-29: a second session edited `maestro.md` mid-run and an edit was rejected because the file moved underneath. If a live agent pane is already open on the same project, say so before starting work, and let the owner decide which one continues.

## Links

- [[context-loader]]
- [[brief]]
- [[session-memory]]
