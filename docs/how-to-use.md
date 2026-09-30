# How to use it, by example

Four real-shaped sessions, start to finish, so you can see what talking to the brain looks like. Names and companies are fictional.

## 1. A normal morning (desktop app, no terminal)

```text
You:    This is my second-brain vault. Read 99-Meta/START_HERE.md ... Task: start today.

Claude: Routing: first touch of the day -> daily

        Journal
        - did: 05-Journal/2026-10-06.md created, 2 items carried from Friday
        - needs: nothing
        - next: the one thing today, per your note: send the Q4 shortlist to two partners (you send)

        Inbox
        - did: 3 items waiting, oldest 2 days
        - next: say "process my inbox" when you have 5 minutes
```

Then through the day:

```text
You:    capture: ask the vendor whether data stays in India
Claude: captured -> 00-Inbox/2026-10-06 vendor-data-residency.md

You:    Turn these notes from the 11am call into actions per person. <paste>
Claude: Routing: meeting notes to actions -> no match, proceeding generically
        (logged to PATTERN_LOG as "meeting-actions", count 2)
        ...actions table...
```

Evening:

```text
You:    process my inbox
Claude: Routing: inbox triage -> process-inbox
        1. vendor-data-residency -> 01-Projects/ai-adoption-q4/ (open thread)   approve?
        2. article on GST changes -> 03-Resources/ via ingest-url              approve?
        3. "book dentist" -> not vault material, archive?                       approve?
You:    yes, yes, archive
```

## 2. A project (Claude Code)

```text
You:    /plan a script that merges our three regional sales exports every month,
        flags duplicate invoices and writes one clean sheet. Project: ops-reporting.
        Stakes: real sales data, never modify the source files.

Claude: Routing: new build -> architect
        TICK-001 read and normalise the three exports (fast tier)
        TICK-002 duplicate detection rules (careful tier: rules need judgment)
        TICK-003 write the clean sheet + summary tab (fast tier)
        TICK-002 depends on 001; 003 on 002. Nothing parallel.
        Needs you: approve the three tickets.

You:    approved, go
Claude: Routing: ticket planning -> builder
        TICK-001 plan: ... risks: region C uses dd/mm dates ...
You:    implement it
Claude: Routing: execution -> coder, then code-review
        coded: TICK-001, 2 files, tests 6/6 (run command: pytest tests/)
        review: pass, 1 minor (magic number for header row)
You:    /handoff
Claude: HANDOFF.yaml updated: next step TICK-002, known issue: region C dates
```

## 3. Research that holds up

```text
You:    /research Which document-review AI tools keep data in India, and what do
        they cost for 20 users? Primary sources.

Claude: Routing: external facts -> researcher (web-research)
        | Tool | Data location | Price (20 users) | Grade |
        | A    | Mumbai region, per their security page | quote only | verified |
        | B    | "India option" on enterprise plan      | not public | single-source |
        | C    | not stated                             | listed     | not found (location) |
        Sources: ...
        Saved: 03-Resources/document-review-tools-2026.md
```

## 4. The brain learns a skill

After the third "meeting notes to actions" request:

```text
Claude: skill-creator: "meeting-actions" reached 3 in PATTERN_LOG.
        Draft at 99-Meta/skills/proposed/meeting-actions.md:
        decisions, actions (owner and date only if stated), open questions,
        filed in the project folder, open actions added to the hub.
        Approve, edit or reject?
You:    approve, and never invent a due date
Claude: promoted to 99-Meta/skills/vault/meeting-actions.md, SKILL_MAP row added,
        rule added: dates only if stated.
```

From then on the routing line reads `Routing: meeting notes -> meeting-actions`.

## Habits that pay off

| Habit | Why |
|---|---|
| Start each chat with the boot prompt, or `/brain` | Guarantees the rules and routing are loaded |
| Glance at the routing line | If it is missing on a real task, say "route that through the skill map" |
| Capture everything, file once a day | Keeps the inbox the only messy place |
| Say the stakes | "client-facing" or "real data" changes the tier and the checks |
| `/handoff` before switching models or stopping | Any session can pick up where you left off |
| Friday `/weekly` | It is where your next skill comes from |

## Where to go next

- The full command list: [commands.md](commands.md)
- 70 ready prompts: [prompting-guide.md](prompting-guide.md)
- What to tell it about yourself: [profile-guide.md](profile-guide.md)
- Which apps and connectors to add: [apps-and-connections.md](apps-and-connections.md)
