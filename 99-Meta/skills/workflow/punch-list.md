---
name: punch-list
version: 1.0.0
trigger: an unattended run (skill-sweep, ticket-sweep, git-backup, Janitor) produces findings that need the owner, or a sweep is about to re-report an item it has already reported
inputs: this run's findings, the existing 99-Meta/generated/PUNCH_LIST.md, prior journal "needs"/"next" lines
outputs: 99-Meta/generated/PUNCH_LIST.md (one standing deduped list), plus a one-line pointer in the run's journal entry instead of a re-listed prose block
depends_on: brief, session-memory, PATTERN_LOG.md, janitor, architect
status: active
promoted: 2026-09-20
proposed: 2026-07-29
proposed_by: skill-sweep (acting as skill-creator)
---

# Punch List

## Purpose

Unattended runs find things. Right now each run writes its findings as prose into that day's journal entry, and the next run of the same task rediscovers the same unresolved item and writes it again. The sweep log shows the same four carryover items re-described on 2026-07-23, 2026-07-26 and again on 2026-07-29, each time with a slightly different wording and no first-seen date, no sighting count, and no owner. Nothing is wrong with any single report; the cost is that a reader cannot tell a new finding from the fourth restatement of an old one, and an item can sit unresolved for weeks without that fact being visible anywhere.

This skill gives recurring findings one home. A finding is written once, keyed by identity rather than by wording, and every later sighting bumps its count and its last-seen date instead of adding a new paragraph. Journals go back to recording what changed that day.

The original vault invented this pattern ad hoc in an unattended run before it was formalized here.

## When to use

- Any scheduled or background run that ends with items needing the owner: skill-sweep, ticket-sweep, git-backup, Janitor weekly, a Maestro run manifest.
- A sweep notices an item it reported on a previous run and that item is still open.
- Closing an unattended session where `blocked_on_owner` or `needs_human` items exist.

## When NOT to use

- For work the agent can finish itself. Do it, do not list it.
- For a capability gap or a repeated procedure. That is [[PATTERN_LOG]], which feeds skill-creator. The two are different: PATTERN_LOG counts patterns that should become skills; the punch list counts open items that need a decision.
- For ticketed work. If it is a ticket it lives in `tickets/` and shows up in TICKET_STATUS. The punch list is for what is too small or too undecided to ticket.
- As a second task tracker. Checkbox tasks in project hubs stay where they are.

## Procedure

1. Read `99-Meta/generated/PUNCH_LIST.md`. If it does not exist, create it with the table below.
2. For each finding this run produced, write a one-line identity: the file or system it concerns plus the defect. `sweep_tickets.py ACTIVE_STATUSES missing in-progress`, not `the sweep dropped a ticket`. Identity is what deduping matches on, so it must be stable across runs.
3. Match against existing rows by identity, not by wording.
   - New: append a row. `First seen` = today. `Sightings` = 1.
   - Already present and still open: bump `Sightings`, set `Last seen` = today. Do not add a row and do not rewrite the description.
   - Already present and now resolved: move it to the Closed section with the date and what closed it. Never delete a row.
4. Set `Owner` honestly. `the owner` only when the action genuinely requires them: a GUI setting, a security posture call, a naming decision, money, a submit. Anything an agent can do is owned by that agent, and if it has sat for three sightings with an agent owner, it is not really blocked, it is being skipped. Say so.
5. Escalate on the third sighting: an item at `Sightings: 3` with `Owner: The owner` gets flagged `[stale]` and named in the run's report. Do not silently re-report a fourth time.
6. In the journal entry, write one line: `punch list: N open, M new today, K flagged stale (see PUNCH_LIST)`. Not the list itself.
7. If an item turns out to need real work rather than a decision, hand it to [[architect]] to ticket, and close the row with `-> TICK-nnn`.

## Output format

```markdown
| Item | Where | Owner | First seen | Last seen | Sightings | Status |
|---|---|---|---|---|---|---|
| daily-notes plugin folder not set to 05-Journal/ | Obsidian settings | The owner | 2026-07-20 | 2026-07-29 | 3 | open [stale] |
```

Closed rows move under a `## Closed` heading with a `Resolution` column, keeping the original first-seen date.

## Style rules

- One line per item, no paragraph. The description is an identity, not a narrative.
- Numbers and paths, never adjectives. No "significant", no "critical" unless a boundary is involved.
- Never invent an owner. If it is unclear who can act, `Owner: unassigned` and say that in the report.
- No em dashes, no emoji.

## Example

Before, three journal entries carrying the same four items in prose:

```
2026-07-23: Carryover drift still open, needs the owner: writing-pipeline hub
  proposed table (2nd sweep flagging this), client-onboarding hub referencing
  a skill as "proposed", root daily-note stubs, W30 Janitor's 24-issue batch.
2026-07-26: Carryover drift still open, needs the owner: writing-pipeline hub
  proposed table (3rd sweep), client-onboarding hub stale refs (2nd sweep), root
  daily-note stubs, W30 Janitor 24-issue batch.
2026-07-29: (same items again, reworded)
```

After, one journal line and one row that carries its own history:

```
punch list: 6 open, 1 new today, 2 flagged stale (see PUNCH_LIST)
```

## Links

- [[PATTERN_LOG]]
- [[brief]]
- [[session-memory]]
- [[janitor]]
- [[architect]]
