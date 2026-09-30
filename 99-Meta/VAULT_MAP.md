---
type: meta
layer: 2
status: active
owner: system
---

# Vault Map

> Layer 2. The Navigator consults this file when a note needs to be routed. Living document: update when folder conventions change.

## Quick reference

| Folder | Purpose | Lifecycle |
|---|---|---|
| `00-Inbox/` | Capture zone, unprocessed | Processed within 7 days, then moved |
| `01-Projects/` | Active work with defined outcome | Archived when project closes |
| `02-Areas/` | Ongoing responsibilities, no end date | Reviewed in weekly review |
| `03-Resources/` | Reference material | Permanent, pruned rarely |
| `04-Archives/` | Done or dormant | Read-only unless reopened |
| `05-Journal/` | Daily and weekly notes | Permanent, append-only |
| `99-Meta/` | Operating layer | The owner-governed |
| `skills/` | Claude SKILL.md packages (portable) | Updated as skills evolve |
| `code/` | Runnable scripts and apps serving the vault | Not vault notes; do not lint |
| `_local-only/` | Sentinel quarantine | Gitignored, never synced |

## 00-Inbox

**Belongs:** anything unprocessed. Quick captures from mobile, pasted links, half-thoughts, meeting fragments.
**Does not belong:** anything older than 7 days. Anything already classified.
**Naming:** `YYYY-MM-DD short-slug.md`. Frontmatter optional at capture time; added by `process-inbox`.
**Lifecycle:** `process-inbox` classifies each item, proposes a destination, moves on approval. Empty inbox is the healthy state.

## 01-Projects

**Belongs:** active work with a defined outcome and an end. A client engagement, a product launch, a course, this vault itself. Each project gets a subfolder with a `_hub.md` index note (from `templates/project-hub.md`).
**Does not belong:** ongoing areas (those are 02), reference material (03).
**Naming:** subfolder per project, kebab-case. Notes inside prefixed by date where order matters.
**Lifecycle:** when the outcome is reached or the project goes dormant for 30+ days, `archive-stale` proposes a move to `04-Archives/`.
**Tickets:** projects using the [[PIPELINE]] (architect/builder/coder) get a `tickets/` subfolder, one file per ticket (`TICK-NNN.yaml`, from `templates/ticket.yaml`). Ticket detail stays local to the project; [[TICKET_INDEX]] holds the cross-project status view.

## 02-Areas

**Belongs:** ongoing responsibilities without an end date. Team management, a practice area, study, finances, health. Concept notes accumulate here under their area.
**Does not belong:** anything with a deadline or deliverable (that is a project).
**Naming:** subfolder per area, lowercase. Concept notes use `templates/concept.md`.
**Lifecycle:** permanent. Weekly review scans for drift.

## 03-Resources

**Belongs:** papers, docs, saved articles, cheat sheets, regulatory citations. Output of `ingest-url` lands here using `templates/resource.md`.
**Does not belong:** original thinking (that goes to Areas or Projects and links here).
**Naming:** `source-title-slug.md`. Frontmatter carries `source:` URL and `ingested:` date.
**Lifecycle:** permanent. `dedupe` flags near-duplicates.

## 04-Archives

**Belongs:** closed projects, dormant notes, superseded material. Moved here, never deleted.
**Does not belong:** anything active.
**Naming:** keeps original name, prefixed with the closing date folder `YYYY/` where volume demands.
**Lifecycle:** read-only. Never modified unless the owner explicitly reopens.

## 05-Journal

**Belongs:** daily entries (`YYYY-MM-DD.md` from `templates/daily.md`), weekly reviews (`YYYY-Www-review.md`), session summaries.
**Does not belong:** concept notes or project material (link to them instead).
**Naming:** ISO dates only. `2026-07-01.md`, `2026-W27-review.md`.
**Lifecycle:** append-only. Janitor logs session summaries here.

## 99-Meta

**Belongs:** START_HERE, FOUNDATION, this file, USER_PROFILE, BOUNDARIES, SKILL_MAP, SKILL_INDEX, TICKET_INDEX, PIPELINE, FLOWCHARTS, MODEL_SELECTOR, HOW_TO_BRIEF, Brain-Health, TICKET_BOARD, templates/, agents/ (and agents/proposed/), skills/ (vault workflow skills, and skills/proposed/).
**Does not belong:** content notes of any kind.
**Naming:** UPPERCASE for canonical docs, lowercase for skills and templates.
**Lifecycle:** FOUNDATION and BOUNDARIES are the owner-edited only. The rest updates through the skills that own them.

## Routing rules (for the Navigator)

1. Unclassifiable or in a hurry: `00-Inbox/`.
2. Has a deadline or deliverable: `01-Projects/<project>/`.
3. Ongoing domain knowledge: `02-Areas/<area>/`.
4. External material summarized: `03-Resources/`.
5. About today or this week: `05-Journal/`.
6. About the system itself: propose a `99-Meta/` change, do not apply without approval.

## Links

- [[FOUNDATION]]
- [[SKILL_MAP]]
- [[navigator]]

## Related

- [[README|README]]

## 99-Meta operating-layer structure

The operating layer is sub-structured so it stays navigable:

- `99-Meta/skills/<group>/`: skills grouped by domain: `vault/` (capture, journal, hygiene, linking, onboarding), `workflow/` (reporting, research, decisions, continuity), `coding/` (review, debugging, worktrees), plus any sub-brain groups you add.
- `99-Meta/generated/` — machine-written files (TICKET_STATUS, TICKET_BOARD, Brain-Health), kept separate from hand-edited law.
- `99-Meta/agents/` — all agents (flat until it grows past about 15).
- Constitution and maps (FOUNDATION, BOUNDARIES, USER_PROFILE, MODEL_SELECTOR, VAULT_MAP, SKILL_MAP, SKILL_INDEX, TICKET_INDEX, PIPELINE) stay at 99-Meta root.

Growth rule (for FOUNDATION): any skill group exceeding ~10 files gets a subfolder; generated files never sit next to hand-edited law; root holds only README and CLAUDE.md. Wikilinks resolve by basename, so moving a skill between groups does not break `[[links]]`.

