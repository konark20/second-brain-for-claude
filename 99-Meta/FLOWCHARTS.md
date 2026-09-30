---
type: meta
layer: 2
status: active
owner: system
tags: [diagram, pipeline, ticket-index]
---

# Flowcharts

> Visual companion to [[FOUNDATION]] and [[PIPELINE]]. Obsidian renders these natively (no plugin needed, Mermaid support is built in). If a diagram and the text docs ever disagree, the text docs win — update this file to match, not the other way around.

## 1. Whole-vault routing (four layers + ticket pipeline)

```mermaid
flowchart TD
    Chat["Layer 4: Interface\n(chat, Claude Code, Obsidian)"] --> Nav

    Nav["Navigator (sonnet)\nreads USER_PROFILE, VAULT_MAP, SKILL_MAP"]

    Nav -->|"size 1: quick chat"| Chat
    Nav -->|"size 2: known skill/agent"| Skill["Skill or domain agent\ne.g. deck-builder (fable)"]
    Nav -->|"size 3: project/ticket work"| Arch

    Arch["Architect (sonnet)\nscopes goal into TICK-NNN.yaml"] -->|draft| Build
    Build["Builder (fable)\nplans the how"] -->|specced| Code
    Code["Coder (sonnet, opus if flagged)\nwrites the diff"] -->|review| Done((done))

    Jan["Janitor\nend-of-session + weekly sweep"] -.watches.-> Nav
    Jan -.watches.-> Arch
    Jan -.watches.-> Build
    Jan -.watches.-> Code
```

## 2. Ticket lifecycle

```mermaid
flowchart LR
    draft -->|architect| specced -->|builder| coding -->|coder| review -->|The owner / self-correction| done --> archived
```

## Links

- [[FOUNDATION]]
- [[PIPELINE]]
- [[TICKET_INDEX]]
- [[MODEL_SELECTOR]]
