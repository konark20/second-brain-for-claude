---
type: meta
layer: 2
status: active
owner: system
---

# Skill Map

> Layer 2. The Navigator consults this file when a request needs a tool. Living catalog: every new skill, agent or command gets a row here or it does not exist. Full tag index: [[SKILL_INDEX]].

## Agents (99-Meta/agents/)

| Name | One line | Use when | Do NOT use when |
|---|---|---|---|
| [[navigator]] | Triage router; never does real work itself | Any request whose destination is unclear | The skill to use is already obvious |
| [[researcher]] | Finds, extracts and verifies external facts with sources | Any step needing current external facts | The fact is in the vault, or a single known URL (ingest-url) |
| [[janitor]] | Vault hygiene at session end, weekly, or on /janitor | Session close, weekly sweep, explicit audit | Mid-task; it is a closer, not a worker |
| [[librarian]] | Tags and indexes new content the moment it is created | New skill, agent, project, resource or ticket | As an excuse to rewrite content |
| [[skill-creator]] | Turns repeated patterns into draft skills or agents for approval | A pattern repeats 3+ times, or the owner asks for a new skill | Inventing capabilities nobody needs; fixing existing ones |
| [[capability-auditor]] | Audits agents, skills, commands and code as a system; proposes fixes as diffs | /audit, monthly, after a batch of edits | Note hygiene (janitor); building new things (skill-creator) |
| [[architect]] | Scopes a goal into ordered tickets: what and why, never how | A new goal enters the pipeline | Mid-ticket; one-line fixes |
| [[builder]] | Turns a ticket into an exact plan: research, sequence, risks | Ticket approved for planning | Before architect scopes it |
| [[coder]] | Reads the plan, writes the diff, tests, reports | Plan approved for execution | Without a builder plan |
| [[sentinel]] | Secrets and ID-document firewall on anything leaving the vault | Before every commit, push or share; /sentinel | As a secrets manager |
| [[reaper]] | Archive stale notes, hard-delete from Archives after 30 days and a veto window | Weekly cleanup, on request | Deleting from active folders |
| [[git-sync]] | Scheduled, sentinel-gated backup to the owner's private repo | Daily backup, or "push the vault" | Public repos, conflicts, force-push |
| [[github-manager]] | Creates and maintains project repos | Working on code repos | Vault backup (git-sync) |
| [[deck-builder]] | Slide-deck lifecycle: intake, outline approval, build, QA | Any deck or presentation | A single chart with no argument |

## Vault skills (99-Meta/skills/vault/)

| Name | One line | Use when | Do NOT use when | Produces |
|---|---|---|---|---|
| [[onboard]] | First-run interview: quick, standard or deep, suggestions on every question, resumable, ends with a portrait | First session in a new copy (auto), /onboard | Small profile edits; weekly tuning (calibrate) | USER_PROFILE, BOUNDARIES owner section, hubs, voice, portrait |
| [[calibrate]] | Two or three tuning questions a week from what actually happened | Weekly; after a correction; /calibrate | Mid-task; re-asking declined questions | Approved profile and portrait diffs |
| [[context-loader]] | Session-start ritual | Start of any vault session | Never skipped | One-line status |
| [[capture]] | Quick note dump into the Inbox with frontmatter | Any fleeting thought or link | Content already has a home | Inbox note |
| [[process-inbox]] | Classify inbox items, propose destinations, move on approval | Inbox has items; daily | Auto-filing without approval | Empty inbox |
| [[daily]] | Today's journal entry with yesterday's carry-over | First vault touch of the day | A second entry the same day | `05-Journal/YYYY-MM-DD.md` |
| [[weekly-review]] | Wins, blockers, patterns, unfinished items for the week | Sunday or on request | Mid-week | `05-Journal/YYYY-Www-review.md` |
| [[connect]] | Find related notes and propose wikilinks | A note feels orphaned; after ingest | Mass auto-linking | Proposed links |
| [[ingest-url]] | Summarize an article into Resources and cross-link | The owner shares a URL worth keeping | Paywalled or trivial pages | `03-Resources/` note |
| [[resume]] | Where the work stopped and the one next move | First session of the day; after a break | Mid-session | Status plus one recommendation |
| [[lint-vault]] | Broken links, orphans, missing frontmatter, bad dates | Weekly; on request | As an excuse to mass-edit | Issue report |
| [[dedupe]] | Flag near-duplicate notes | Weekly | Auto-merging | Duplicate pairs |
| [[archive-stale]] | Propose archiving untouched project notes | Weekly; project close | Areas or resources | Archive proposals |

## Workflow skills (99-Meta/skills/workflow/)

| Name | One line | Use when |
|---|---|---|
| [[brief]] | Scannable per-task status block (did / needs / next) | Default report after work |
| [[web-research]] | Query wide, open pages, extract with sources, cross-check | Any external fact (run by researcher) |
| [[council]] | Five angled advisors plus a chairman verdict | A hard decision with real uncertainty |
| [[session-memory]] | Cross-session continuity from journal and HANDOFF.yaml | Session end; picking work back up |
| [[model-handoff]] | Package a self-contained prompt for another model, review the result | Handing code to another AI |
| [[punch-list]] | One deduplicated standing list of items needing the owner | Unattended runs end with open items |
| [[runbook-writeback]] | Turn a workaround into a reviewable fix to its own procedure | A run deviated from its written steps |
| [[skill-sweep]] | Scheduled pattern count and proposal drafting | Twice weekly, scheduled |

## Coding skills (99-Meta/skills/coding/)

| Name | One line | Use when |
|---|---|---|
| [[code-review]] | Severity-graded review; critical issues block done | A ticket reaches review |
| [[systematic-debugging]] | Four-phase root cause before any fix | A bug or failing test |
| [[worktrees]] | Isolated git branch and folder per ticket | Multi-file or parallel tickets |

## Presentation

| Name | One line |
|---|---|
| [[deck-standards]] | Action titles, ghost-deck test, one exhibit per slide, structure by register |

## Portable skills (skills/)

Full Claude skills that travel with the vault. Rename `<name>.md` to `SKILL.md` to install into a Claude skill store.

| Name | One line |
|---|---|
| [[skill-orchestrator]] | Picks and sequences other skills for a multi-phase task |
| [[project-planner]] | Design conversation first, then a YAML plan, before any code |
| [[project-handoff]] | HANDOFF.yaml so another agent or person picks up without re-reading everything |
| [[self-correction]] | Internal quality pass on every substantive output |
| [[professional-writing]] | Emails and messages that sound human |
| [[research-documentation]] | Reports and papers with clean structure and human tone |
| [[application-tailoring]] | Tailored answers for job and program applications |
| [[compressed-response]] | Short answers for quick lookups; /caveman for ultra-short |
| [[context-management]] | Explore a large codebase incrementally |
| [[architecture-review]] | Review and restructure code, tests first |
| [[data-analysis-coding]] | Readable pandas-first Python |
| [[tdd]] | Tests before implementation for substantial code |
| [[ponytail]] | Lazy senior dev ladder: reuse, stdlib, minimum |
| [[ponytail-review]] | Review a diff for over-engineering |
| [[trading-finance-tutor]] | Finance concepts taught trader-first |

## Slash commands (.claude/commands/)

| Command | Points at |
|---|---|
| /brain | Full boot plus routing, then the task |
| /onboard | [[onboard]] (quick, standard, deep, resume, redo) |
| /calibrate | [[calibrate]] |
| /portrait | 99-Meta/onboarding/portrait.md |
| /cold-start | [[context-loader]] |
| /daily | [[daily]] |
| /capture | [[capture]] |
| /inbox | [[process-inbox]] |
| /ingest | [[ingest-url]] |
| /research | [[researcher]] |
| /weekly | [[weekly-review]] |
| /new-project | templates/project-hub.md plus [[librarian]] |
| /plan | [[architect]] |
| /handoff | [[project-handoff]] |
| /council | [[council]] |
| /resume | [[resume]] |
| /janitor | [[janitor]] |
| /audit | [[capability-auditor]] |
| /sentinel | [[sentinel]] |
| /ticket-status | `code/ticket-sweep` |

## Code tools (code/)

| Tool | One line |
|---|---|
| `code/capability-audit/scan.py` | Read-only inventory and drift scan used by capability-auditor |
| `code/ticket-sweep/sweep_tickets.py` | Writes `99-Meta/generated/TICKET_STATUS.md` |
| `code/link-suggester/` | Suggests wikilinks into the Inbox, used by janitor weekly |
| `code/onboarding/first_run_check.py` | SessionStart hook: first-run welcome or resume notice |

## Optional packs (packs/)

Install by copying a pack's agents and skills into the folders above, then add their rows here. See `packs/README.md`.

| Pack | Agents | Skills |
|---|---|---|
| job-search | job-coordinator, dossier-keeper | jd-decoder, project-organiser, bullet-writer, number-miner, resume-layout, resume-critic, interview-defender |
| linkedin | linkedin-strategist | linkedin-keyword-mapper, linkedin-bio-writer, linkedin-post-writer, linkedin-photo-review |
| trading | none | strategy-builder, event-backtest, payoff-check, session-cadence, tilt-guard, conviction-override, scenario-analysis, trade-analysis, performance-analysis, retrospective-writer |

## Project sub-brains

Add a row when a project earns its own coordinator, rules and scoped map ([[SUB_BRAIN_PATTERN]]).

| Project | Coordinator | Map | Rules |
|---|---|---|---|

## Proposed (awaiting approval)

| Name | Proposed | One line | Cites |
|---|---|---|---|
