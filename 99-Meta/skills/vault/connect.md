---
name: connect
version: 1.0.0
trigger: a note feels orphaned; after ingest-url; after process-inbox files to Areas or Resources
inputs: one target note, the vault's existing notes
outputs: proposed wikilinks, applied on approval
depends_on: 99-Meta/VAULT_MAP.md
---

# Connect

## Purpose

A note nobody links to is a note nobody finds. Given one note, this skill finds genuinely related notes and proposes wikilinks in both directions.

## Procedure

1. Extract the target note's key terms: title, headings, frontmatter tags, distinctive phrases. For a vault-wide similarity pass, run `python3 code/link-suggester/suggest_links.py` instead (writes suggestions to `00-Inbox/`).
2. Search `01-Projects/`, `02-Areas/`, `03-Resources/` for notes sharing those terms or covering adjacent concepts.
3. Keep only real relationships: same concept, prerequisite, contrast, application. Drop keyword coincidences.
4. Propose: `target note <-> candidate: why`. Maximum 5 proposals per run.
5. On approval, insert wikilinks in a Links section on both notes. Do not rewrite surrounding prose.

## When NOT to use

- Mass auto-linking across the whole vault. One note per run.
- Linking for the sake of graph density. A wrong link is worse than no link.

## Style rules

- The "why" for each proposal is one clause, not a paragraph.

## Links

- [[SKILL_MAP]]
- [[VAULT_MAP]]
- [[ingest-url]]
- [[process-inbox]]
