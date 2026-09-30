# Workflows

The recurring loops that make the brain useful, each with the commands that drive it.

## 1. The daily loop

```mermaid
flowchart LR
    M([Morning]) --> D["/daily<br/>carry over yesterday"]
    D --> W[Work: ask, draft, plan]
    W -->|anything to keep| C["/capture"]
    C --> IN[(00-Inbox)]
    W --> E([Evening])
    E --> I["/inbox<br/>approve homes"]
    IN --> I
    I --> P[(Projects, Areas,<br/>Resources)]
    W --> J[janitor closes each session<br/>one journal line]
```

| When | Command | Minutes |
|---|---|---|
| Start of day | `/daily` | 1 |
| Throughout | `/capture <thought>` | seconds |
| Picking something back up | `/resume` | 1 |
| End of day | `/inbox` | 5 |

Capture is cheap and happens anywhere, including from your phone into `00-Inbox/`. Filing happens once a day, with you approving.

## 2. The weekly loop

```mermaid
flowchart TD
    WK["/weekly"] --> R1[Wins, blockers, patterns, unfinished]
    WK --> R2[Janitor weekly sweep:<br/>lint-vault, dedupe, archive-stale]
    WK --> R3[Link suggestions into the Inbox]
    R1 --> Q[Two questions:<br/>what is no longer true in my profile?<br/>what should I drop?]
    R2 --> APP{You approve fixes}
    SWEEP[skill-sweep, scheduled twice a week] --> PL[(PATTERN_LOG counts)]
    PL -->|3 of a shape| PROP[(proposed/ drafts)]
    PROP --> APP
```

Reaper runs weekly too: stale notes move to Archives; items 30+ days in Archives appear on a delete manifest in your Inbox. Strike anything you want to keep.

## 3. A project, start to finish

```mermaid
sequenceDiagram
    participant You
    participant Architect
    participant Builder
    participant Coder
    participant Review as code-review
    You->>Architect: /plan goal (+ stakes, constraints)
    Architect-->>You: TICK-001..003, order, suggested tiers
    You->>Builder: go (or "spec TICK-001")
    Builder-->>You: exact plan, risks, questions if any
    You->>Coder: implement TICK-001
    Coder->>Review: diff + tests
    Review-->>Coder: critical issues block
    Review-->>You: passes, ready for your ok
    You->>You: accept, ticket done
    Note over You,Coder: /handoff before a break, so any session or model can continue
```

Useful lines along the way:
- "What can run in parallel?" (architect flags independent tickets)
- "Kick TICK-002 back to the architect, it's really two things."
- "Use the high-stakes tier for this one, it touches real payroll data."
- "/handoff" before switching to another model or stopping for the week.

## 4. Research that holds up

```mermaid
flowchart LR
    Q[Question] --> SQ[2 to 5 sub-questions]
    SQ --> S[Search wide]
    S --> O[Open the real pages<br/>not snippets]
    O --> X[Extract with citations]
    X --> CC[Cross-check across sources]
    CC --> G{Grade each claim}
    G --> V[verified]
    G --> SS[single-source]
    G --> NF[not found]
    V & SS & NF --> OUT[Answer + sources<br/>+ optional 03-Resources note]
```

Say `/research <question>`. Add "primary sources only" for regulations, filings and official data.

## 5. Writing in your voice

1. Once: "Here are three pieces I wrote. Learn the voice and save a style guide to 02-Areas/writing/."
2. Per piece: outline, approve, draft, edit as a diff.
3. After a few pieces, skill-creator will likely propose a writing skill tuned to you. If you publish regularly, the writing pipeline is a good sub-brain candidate.

## 6. Decks

```mermaid
flowchart LR
    IN[Intake: purpose, audience,<br/>register, time slot] --> INV[Content inventory:<br/>lead, support or appendix]
    INV --> OUT[Outline with action titles]
    OUT --> GH{Ghost-deck test:<br/>do titles alone tell the story?}
    GH -->|no| OUT
    GH -->|yes| APP{You approve}
    APP --> BUILD[Build] --> QA[QA against deck-standards]
```

## 7. Decisions under uncertainty

`/council <decision + context>`. Five advisors (for example the optimist, the sceptic, the operator, the customer, the long-term view) reason separately, critique each other, and a chairman returns one recommendation, the strongest counter-argument, and what would change the call.

## 8. Handing work to another model or person

- `/handoff` writes `HANDOFF.yaml`: state, next steps, files, how to run, conventions, errors already solved.
- "Package this for another model" (model-handoff) writes a self-contained prompt, then reviews what comes back through code-review before anything is accepted.

## 9. Backup

```mermaid
flowchart LR
    T[Daily schedule or 'back up now'] --> ST[git status]
    ST -->|nothing changed| DONE[clean, stop]
    ST -->|changes| SEN{sentinel scan}
    SEN -->|hit| Q[block, quarantine to _local-only,<br/>tell you file + pattern]
    SEN -->|clean| C[commit + push to<br/>your PRIVATE repo]
    C --> JL[one journal line]
```

Git-sync never force-pushes, never merges, never resolves conflicts. If the remote disagrees, it stops and tells you.

## 10. Growing the toolkit

| Signal | What happens |
|---|---|
| A request had no matching skill | One PATTERN_LOG line |
| The same shape three times | skill-creator drafts into `proposed/` |
| You approve | Moves to live, SKILL_MAP row, librarian indexes it |
| Monthly `/audit` | Overlaps, dead skills and contradictions proposed as diffs |
| A project runs a multi-role pipeline | Consider a sub-brain (`99-Meta/SUB_BRAIN_PATTERN.md`) |
