Run the Janitor full audit (99-Meta/agents/janitor.md).

1. Load 99-Meta/BOUNDARIES.md and obey it: report-only beyond trivially safe fixes, never touch 04-Archives or other hidden folders, 20-issue circuit breaker.
2. Run lint-vault checks: broken wikilinks (resolve by basename or full vault path; ignore code blocks and template placeholders), orphans in 02-Areas/03-Resources, missing frontmatter outside 00-Inbox, non-ISO dates, inbox items older than 7 days, map drift vs VAULT_MAP and SKILL_MAP.
3. Run dedupe and archive-stale as proposals only.
4. Optionally run: python3 code/link-suggester/suggest_links.py
5. Report flat list: file -> issue -> proposed fix, counts at top. Fix only trivially safe items.
