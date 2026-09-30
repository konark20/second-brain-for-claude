---
name: deck-builder
version: 1.0.0
model: fable
trigger: The owner needs a slide deck built or substantially revised — academic, professional, or trading register
inputs: purpose, audience, register, time slot, source material (paper draft, project notes, tracker, JD-equivalent brief), existing deck if revising
outputs: slide-by-slide outline (approved before build), built .pptx, QA report
depends_on: deck-standards, pptx (built-in), research-documentation, professional-writing, trading skills (performance-analysis, retrospective-writer, strategy-builder) when register is trading, application-tailoring when the deck is job/application-adjacent, self-correction
---

# Deck Builder

## Purpose

Owns the deck lifecycle end to end: intake, outline, content draft, design, build, QA. Coordinator role: the discipline is: read the standards before writing a single slide, get the outline approved before building, run QA before calling it done. Runs on fable because register selection, argument structuring, and content-vs-appendix calls are judgment, not mechanical execution (MODEL_SELECTOR rule 2).

## When to use

- Any request to build slides, a deck, a pitch, or a presentation.
- Revising an existing deck that isn't landing (weak argument, topic-label titles, cluttered slides).

## When NOT to use

- A single ad-hoc chart or one-slide export with no argument to structure — that's the pptx skill directly, no need to route through here.
- The owner explicitly wants design-forward/visual-narrative mode for a public or non-specialist talk — note it and hand off to the pptx skill's own defaults; deck-standards' communication-first rules do not apply there.

## Procedure

1. **Intake.** Confirm purpose, audience, register (academic / professional / trading — see [[deck-standards]]), and time slot if it's a live talk. If any of these is genuinely unclear, ask; don't guess the register, it drives everything downstream.
2. **Gather source material.** Pull from the vault first — project hub, tracker, `04-Archives/` retrospectives, `01-Projects/` notes — before asking the owner to restate what's already written down.
3. **Read [[deck-standards]] in full** before drafting anything. It is the format authority for argument structure, action titles, exhibit discipline, and design rules by register.
4. **Content inventory (structure analysis, before any fixed template is applied).** List every raw content element the owner has given: findings, limitations, graphs/exhibits available, what the data showed, lessons learned, business value/impact, architecture or process detail, work remaining, future opportunities, methodology, bottlenecks, references. For each element, decide:
   - **Audience weight** — does it lead, support, or move to appendix? Rule of thumb: the more senior/non-technical the room, the more "so what" (findings, business value, recommendation) leads and the more mechanism (architecture internals, methodology detail) compresses to one simplified slide or moves to appendix, available if asked.
   - **Narrative slot** — which part of the chosen spine (situation/complication/resolution, or answer-first for a senior/time-pressured room) does this element serve? An element that doesn't clearly serve the argument is an appendix candidate, not a main slide.
   - **One slide, one job** — split any element that's really two ideas (e.g. "architecture" often splits into one high-level diagram slide plus a separate bottleneck/limitation slide).
   This step produces the deck's actual structure — it is generated fresh from what this specific project has to say, not pulled from a fixed slide-type list. Only the underlying rules (action titles, one exhibit per slide, ghost deck test, design standards) come from [[deck-standards]]; the structure itself is bespoke per deck.
5. **Draft the outline** from the inventory: slide-by-slide, action title + exhibit type + appendix/main placement. Run the ghost deck test on the outline yourself before showing it.
6. **Get the outline approved** by the owner before building the file, always past ~10 slides. Cheap to redirect an outline; expensive to redirect a built deck.
7. **Draft content**, dispatching by register:
   - Academic or otherwise formal prose: [[research-documentation]] for tone and structure.
   - Trading decks: pull structure and numbers from the trading pack skills if installed, or the live strategy plan — never invent a number, trace every figure to the tracker or a broker data pull.
   - Job/application-adjacent decks (e.g. portfolio walkthrough for an interview): [[application-tailoring]] for framing, [[professional-writing]] for tone.
   - Technical project readouts where real metrics live on a machine this agent can't reach (e.g. internal company systems): build the slide with the action title, layout, and a clearly labeled placeholder box (exhibit type, suggested axis/legend, target dimensions) instead of a fake chart. Never fabricate a stand-in graph with invented numbers — an empty labeled placeholder is correct; a plausible-looking fake one is not.
8. **Build the file** using the built-in pptx skill for mechanics, applying deck-standards' design rules (white background, one font, max three colors, 16:9, left-aligned body, figure-left/interpretation-right) unless the owner specifies a different palette/theme for this deck.
9. **Run the QA checklist** from deck-standards section 13, plus the pptx skill's own technical QA (markitdown content check, visual check on rendered slide images if available), plus: every placeholder exhibit is clearly labeled as a placeholder, not mistakable for a finished chart.
10. **Self-correction pass** ([[self-correction]]) on all slide text before presenting the build.
11. **Report back in three lines**: structure used and why, argument in one sentence, anything flagged (placeholders needing real graphs, an appendix item cut for time, a QA item that didn't fully pass).

## Style rules

- No em dashes, no AI-sounding language on any slide, consistent with the rest of the vault.
- Never fabricate a number or finding. If source material doesn't support a claim the outline wants to make, flag it and ask rather than smoothing over the gap.
- One argument per deck (deck-standards rule). If the owner's ask is really two arguments, say so before drafting an outline that tries to force both in.

## Links

- [[deck-standards]]
- [[research-documentation]]
- [[MODEL_SELECTOR]]
- [[BOUNDARIES]]
