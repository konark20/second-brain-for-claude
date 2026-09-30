---
name: skill-sweep
version: 1.0.0
trigger: the scheduled skill-sweep task, Sunday and Wednesday 9pm, or the owner asks for a sweep
inputs: 99-Meta/PATTERN_LOG.md, project hubs, recent 05-Journal/ entries, code/capability-audit/scan.py output
outputs: PATTERN_LOG rows, drafts in proposed/, a refreshed 99-Meta/generated/Brain-Health.md, a `## skill-sweep (unattended)` journal entry
depends_on: skill-creator, capability-auditor, PATTERN_LOG.md, BOUNDARIES.md
---

# Skill Sweep

## Purpose

The scheduled task that keeps the self-improving loop turning. Documented here because the task itself lives in the scheduler and the vault had no note describing it, which left `[[skill-sweep]]` as a broken wikilink for five sweeps. This file records what the runs do, taken from the run logs 2026-07-20 to 2026-09-19. The scheduler's own prompt is the executable copy.

## When to use

- Runs itself Sunday and Wednesday at 9pm, unattended.
- The owner asks for a sweep by hand.

## When NOT to use

- A capability audit with verdicts. That is [[capability-auditor]]. The sweep only counts and surfaces.
- Vault note hygiene. That is [[janitor]].

## Procedure

1. Cold start: read FOUNDATION, USER_PROFILE, BOUNDARIES. Check `_local-only/AUTONOMY_OFF`; if present, no-op.
2. Read PATTERN_LOG and the projects' recent activity. Append a row for any new gap. A shape at 3 rows gets drafted to `proposed/` by acting as [[skill-creator]].
3. Skill-health check: run `python3 code/capability-audit/scan.py` and take the catalog drift section as the check. This replaces the hand cross-check of disk against SKILL_MAP and SKILL_INDEX.
3a. **Hub-capability sync, added 2026-09-24 (PATTERN_LOG `hub-schema-gap`, 3 sightings, the owner asked directly).** For every active project hub (`01-Projects/*/_hub.md` with `status: active`): if it has no `## Agents and skills assigned` section, flag it by name (the template now includes the section for new hubs; this catches the backlog). If it has the section, check every named agent/skill against current `SKILL_MAP.md`/`SKILL_INDEX.md`: still exists, not renamed, not merged into something else, not archived to `04-Archives/retired-capabilities/`. A hub naming a retired or renamed capability is drift, not just an outdated phase-match — flag both kinds. Do not silently rewrite a hub's section; report the drift, let the hub's own project fix it (or fix it directly if the correction is unambiguous, e.g. a straight rename with no judgment call, and note it in the journal).
4. Refresh `99-Meta/generated/Brain-Health.md`: counts, project status, ticket pipeline, drift and risks.
5. Keep recurring findings in the standing list with [[punch-list]] and put one line in the journal (`punch list: N open, M new, K stale`), not a re-listed block. If a run worked around a defect in its own procedure, write the fix as a diff with [[runbook-writeback]].
6. Write the journal entry with what changed and what needs the owner.
7. Never push, never spend, never edit FOUNDATION or BOUNDARIES. Drafts only.

## Style rules

- Numbers and paths, no adjectives. No em dashes, no emoji.

## Links

- [[PATTERN_LOG]]
- [[Brain-Health]]
- [[skill-creator]]
- [[capability-auditor]]
- [[BOUNDARIES]]
