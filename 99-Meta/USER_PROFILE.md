---
type: meta
layer: 1
status: template
owner: "{{OWNER_NAME}}"
updated: "{{DATE}}"
---

# User Profile

> Layer 1. Loaded at the start of every session. Filled by the onboarding interview (`/onboard`), then edited by the owner as things change. Anything still in `{{braces}}` has not been answered yet. Claude never fills a placeholder with a guess.

## Who {{OWNER_NAME}} is

- Name and what to call them: {{OWNER_NAME}}
- Role and organisation: {{ROLE_AND_ORG}}
- A normal week: {{NORMAL_WEEK}}
- Responsible for directly: {{DIRECT_RESPONSIBILITIES}}
- Oversees through others: {{OVERSEES}}
- Location and time zone: {{LOCATION_TIMEZONE}}

## How they work with AI

- Devices: {{DEVICES}}
- Daily apps: {{DAILY_APPS}}
- Claude surfaces: {{CLAUDE_SURFACES}}
- Other AI tools and what they are used for: {{OTHER_AI_TOOLS}}
- Backup: {{BACKUP_CHOICE}}

## Communication rules (non-negotiable)

- Length: {{SHORT_OR_FULL}}
- Words and styles to avoid: {{AVOID_LIST}}
- Language and spelling: {{LANGUAGE_SPELLING}}
- Answer first or reasoning first: {{ANSWER_ORDER}}
- Reporting after work: {{REPORT_STYLE}}
- When unsure: {{ASK_OR_DECIDE}}

Defaults until answered: concise, direct, no padding, no emoji, no summary of the question before answering, say "I'm not sure" rather than guess.

## Domains

| Domain | Their role (expert / decider / reviewer) | Help wanted (think / draft / research / track / review) |
|---|---|---|
| {{DOMAIN_1}} | | |
| {{DOMAIN_2}} | | |

Reference material they return to, and where it lives: {{REFERENCE_MATERIAL}}

## Standing preferences

- Daily journal: {{DAILY_JOURNAL}}
- Weekly review: {{WEEKLY_REVIEW_SLOT}}
- New skill proposals: {{SKILL_PROPOSALS}}
- Hygiene sweep: {{JANITOR_CADENCE}}

## Links

- [[FOUNDATION]]
- [[BOUNDARIES]]
- [[VAULT_MAP]]
- [[SKILL_MAP]]
