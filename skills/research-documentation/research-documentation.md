---
tags: [skill, writing]
name: research-documentation
version: 1.0.0
description: Use this skill whenever writing or structuring a research paper, academic report, business report, or finance/analysis report — any formal written document rather than a short message. Covers quantitative and trading/finance reports involving formulas, theoretical background, or supporting data (e.g. derivatives pricing writeups, futures spread analysis, strategy reports). Trigger for "write a report on," "draft a research paper about," "document my findings on," "put together an analysis of," coursework writeups, internship/work reports, or any structured multi-section document, even without an explicit formatting request. Produces professionally structured documents in a tone that reads as genuinely human, avoiding AI-writing tells (em dashes, emoji, hedging, filler transitions, generic conclusions). Does not handle charts, tables, or visual design — that's a separate task; this skill covers structure and prose only.
---

# Research & Report Documentation

This skill structures and writes formal documents: academic research papers, course writeups, and business or finance reports. It is the longer-form counterpart to everyday professional writing. The same anti-AI-tell standards apply (see "What to avoid"), but the job here is different: the priority is correct, logical structure for a document the reader will navigate section by section, not just a clean paragraph.

This skill does not produce charts, tables, or visual formatting. If the document would benefit from a chart or table, note where it should go and what it should show, and treat producing it as a separate task.

## Step 1: Identify the document type

Before doing anything else, work out which of these the request actually is, since they use different skeletons:

- **Academic research paper / coursework writeup** — has an argument or analysis to support, typically needs an abstract or intro framing the question, a methodology or approach section, findings/analysis, and a conclusion. Usually needs citations.
- **Business / finance report** — has a decision or recommendation to support, typically needs an executive summary, context/background, analysis or findings, and a recommendation or conclusion. Citations are less common; sourcing (if any) is usually informal (linked or named, not formatted in a citation style).

If it's genuinely unclear which one applies, ask. Don't guess and build the wrong skeleton, since restructuring later costs more than asking up front.

**Check whether the report is quantitative.** Many of the reports this skill will be used for (trading strategy writeups, derivatives or futures analysis, financial models) are quantitative regardless of which skeleton above applies. For these, also work out up front:

- **Theoretical/background grounding** — does the report need to establish the underlying concept before analyzing it (e.g. what a calendar spread is and why basis behaves the way it does, what a Greek measures, what the relevant market mechanics are)? If so, this becomes its own section, not a sentence buried in the analysis.
- **Equations and formulas** — does the analysis rely on specific formulas (pricing models, payoff equations, statistical tests, the actual math behind a strategy)? If so, these need a dedicated place in the structure, not just prose description. Equations should be written out properly (not just described in words) and defined: state what each variable means when a formula is first introduced.
- **Test cases / supporting data** — is there data, a backtest, a worked numerical example, or scenario analysis that supports the claims? If so, this needs its own section (e.g. "Data and Methodology" or "Supporting Analysis") rather than being asserted without evidence.

Ask about these up front rather than assuming none apply. A report that should have had a formulas section but didn't is a much bigger rewrite than a quick question at the start.

## Step 2: Propose structure before writing

For any report or paper beyond a couple of pages, don't go straight to a full draft. Propose the section structure first (section names, roughly what each will cover, and an estimate of length if useful) and get confirmation before writing the full thing. This is the single highest-leverage step: a wrong section structure caught at the outline stage takes one message to fix; caught after a full draft, it means rewriting most of the document.

When the report is quantitative, the proposed structure should explicitly show where background/theory, formulas, and supporting data each live — don't fold them invisibly into "analysis." For example, for a trading strategy report this might look like: Executive Summary → Background & Mechanics → Methodology & Formulas → Data/Supporting Analysis → Findings → Recommendation. Naming these as distinct sections up front is what lets the user catch a missing piece before the draft is written, not after.

If formulas are involved, all math is written in LaTeX (see "Equations and formulas" under Step 3). Knowing the final output format matters here since it changes how that LaTeX actually gets delivered, so settle the output format at this stage rather than after the draft is written.

For short reports (roughly one page or less, like a brief internal memo or short writeup), this step can be skipped and the draft can go straight to the user, since there's not much structure to get wrong.

**For academic papers specifically:** also confirm the citation style (APA, MLA, Chicago, or whatever the course uses) at this stage if it isn't already stated, since this affects formatting decisions throughout and is awkward to retrofit. Also ask whether a table of contents and section numbering are expected.

**For business/finance reports:** a table of contents is optional. Ask only if the report is long enough (multi-section, several pages) that navigation would actually help; don't ask for a one-page memo.

## Step 3: Write the document

Once structure is confirmed, write section by section. A few standing rules:

**Lead with substance, not setup.** Avoid an introduction paragraph that just restates the section structure ("This report will first discuss X, then Y, then Z"). Get into the actual content. Save explicit signposting for genuinely long, multi-part documents where the reader benefits from orientation.

**Every section should earn its place.** Don't include a section just because the template usually has one. If a "limitations" or "background" section doesn't have real content for this particular paper, fold it into another section or cut it rather than padding it out.

**Conclusions should say something, not just summarize.** A conclusion that only restates what was already said reads as filler. End on the actual implication, recommendation, or open question, not a recap.

**Citations (academic only):** Use the confirmed style consistently. Don't fabricate sources or page numbers. If a claim needs a citation and none is available, flag it rather than inventing one.

**Equations and formulas:** Write every formula in proper LaTeX notation, not plain-text approximations (use `\frac{a}{b}`, `\sigma^2`, `\int`, `\sum`, subscripts/superscripts, etc. rather than "a/b", "sigma^2", or spelling things out in words). Define every variable the first time it appears. Walk through what the formula means in plain terms immediately after presenting it, since a formula alone doesn't tell the reader why it matters here.

How the LaTeX gets delivered depends on the destination format, so confirm the output format (Step 2 already asks this) before writing equations, and handle each case correctly:
- **Markdown or in-chat response:** write LaTeX directly using `$...$` for inline math and `$$...$$` for display equations. This is the default delimiter convention for this skill, and it renders natively in Claude.ai and most Markdown.
- **Word document (.docx):** raw LaTeX source doesn't render as math in Word, it needs to become an actual equation object. Write the LaTeX form here (still using `$...$` / `$$...$$`) for review, then defer to the docx skill for how to convert it into a native Word equation rather than pasting LaTeX as literal text.
- **PDF:** if the PDF is being built from LaTeX source (via the pdf skill), `$...$` / `$$...$$` is exactly right and carries through directly. If the PDF is being built some other way (e.g. converted from Markdown or a docx), the same conversion concern as above applies, check with the pdf skill on which path is being used.

If unsure which case applies, ask rather than guessing, since a formula that displays as raw backslashes and curly braces in the final document is worse than no formula at all.

**Test cases and supporting data:** Claims that rest on data, a backtest, or a worked example need that evidence shown, not just asserted. If real data isn't available, say so explicitly rather than presenting a plausible-looking number as if it were computed. A worked numerical example (even a simplified one) is often the clearest way to make an abstract formula concrete, use one where it helps.

## What to avoid

The same core anti-AI-tell rules from professional writing apply here, plus a few that are specific to longer documents:

**Em dashes.** Never use them.

**Emoji.** Never use them.

**Hedging and filler transitions.** Avoid "It is important to note that...", "It should be mentioned that...", "In today's world...", "Overall, it is clear that...". These phrases pad length without adding content. State the point directly.

**Generic, recap-only conclusions.** Covered above, worth repeating: don't close a section or the document by just restating what was already said.

**Formulaic paragraph structure.** Avoid mechanically opening every paragraph with a topic sentence that restates the section heading. Vary structure the way real academic and professional writing does.

**Overqualified claims.** Avoid stacking hedges ("It could perhaps be argued that it may potentially suggest..."). Make the claim, then qualify it once if genuinely needed, not three times.

**Inflated transitions between sections.** Avoid "Building on the above, we now turn to...", "Having established X, it is now necessary to examine Y." A simple section break with a clear heading does this job better.

## Output

Ask which file format is needed if it isn't already clear (Word doc, PDF, Markdown, or just text in the conversation) before producing the final file. If a Word document is requested, defer to the docx skill for the actual file mechanics (the structure and prose decided here are what gets put into it). If a PDF is requested, defer to the pdf skill similarly. This skill governs what the document says and how it's organized; the format-specific skills govern how that gets built into the actual file.

## De-slop pass

Before delivering, run the scored de-slop pass in [[ai-writing-tells]] (03-Resources): cut the banned phrases and structural cliches, then rate the 5 dimensions. Do not ship prose scoring under 35/50. Cite the score rather than asserting it reads clean.
