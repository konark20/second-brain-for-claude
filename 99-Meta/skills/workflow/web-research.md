---
name: web-research
version: 1.0.0
trigger: any task needing facts from the live web beyond a single URL ingest (company research, market data, tool comparisons, current events, documentation lookups)
inputs: the research question, quality bar (quick answer vs sourced brief), destination (chat answer, project note, resource note)
outputs: findings with source URLs, optionally a 03-Resources/ note
depends_on: 99-Meta/skills/ingest-url.md, skills/self-correction/self-correction.md
---

# Web Research

> Fills the `research` slot BOUNDARIES.md already permits web search for ("Web search is allowed for the `ingest-url` and `research` skills"). ingest-url handles one known URL; this skill handles open questions where the sources must be found first. Created 2026-07-16 on the owner's instruction after weak search-and-extract performance was flagged.

## Purpose

Search results are not research. The failure mode this skill exists to kill: run one query, skim snippets, answer from the snippets. Snippets are truncated, stale, and often contradict the page behind them. This skill forces the loop: query wide, open the actual pages, extract with citations, cross-check, and only then write.

## When to use

- A project or question needs current facts (prices, deadlines, versions, people, firms, APIs, regulations).
- Comparing tools, services, or approaches before a build decision.
- Company or role research for application or client materials.
- Anything where "I think I know this" is not good enough to ship.

## When NOT to use

- The owner handed over a specific URL: that is `ingest-url`.
- The answer is stable knowledge (math, syntax, concepts): answer directly.
- Vault-internal questions: search the vault, not the web.

## Procedure

1. **Decompose before searching.** Split the question into the 2-5 specific sub-questions that would together answer it. Each sub-question gets its own query. One vague query is the root of most weak research.
2. **Query wide, then narrow.** For each sub-question run at least one broad and one specific query (site:, exact phrases, year qualifiers). If results look thin, rephrase with different vocabulary before concluding the information does not exist.
3. **Open the pages. Never answer from snippets.** Fetch the top 2-3 promising results per sub-question in full. If a fetched page comes back as a shell, spinner text, or "enable JavaScript", it is client-rendered: escalate to Chrome browser tools to get the real content instead of guessing from the fragment.
4. **Extract with provenance.** For every fact kept, record: the claim, the exact source URL, and the page's date if visible. Undated claims on fast-moving topics get flagged as such.
5. **Cross-check anything load-bearing.** A number, deadline, or policy the work will rest on needs two independent sources or an explicit "single-source, unverified" flag. Two pages citing the same original count as one source.
6. **Say what was not found.** If a sub-question came up empty after real rephrasing, report that as a finding. Never paper over a gap with a plausible guess (BOUNDARIES: no fabrication).
7. **Land the output.** Quick answer: findings + sources inline. Durable research: write a `03-Resources/` note using the resource template, cross-link to the requesting project's hub, add to the day's journal line.
8. **Close with self-correction.** Re-read the findings against the original question: does every claim have a URL, does anything contradict, did snippet-language leak in?

## Style rules

- Every non-obvious claim carries its source URL. No orphaned facts.
- Findings in prose, dense and direct. No padded "overview of the landscape" sections.
- Distinguish clearly: verified (2+ sources) / single-source / not found.

## Example

Weak (before): "What ATS do quant firms use?" -> one query, answer assembled from three snippets, no URLs, two of the claims stale.

Strong (after): decomposed into (a) which ATS platforms dominate finance hiring, (b) which specific firms on the target list use which, (c) known parsing quirks per platform. Six queries, nine pages opened, one JS-walled page escalated to browser. Output: per-firm table with URLs, two claims marked single-source, one sub-question honestly reported as not publicly documented.

## Links

- [[ingest-url]]
- [[self-correction]]
- [[researcher]]
- [[BOUNDARIES]]
