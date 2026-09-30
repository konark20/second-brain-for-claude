---
name: deck-standards
version: 1.0.0
trigger: any request to build or improve a slide deck/presentation/pitch (academic, professional, or trading), before a single slide is drafted
inputs: purpose, audience, register (academic / professional / trading), time slot, source material (paper, project writeup, tracker, JD-equivalent context)
outputs: a slide-by-slide outline (action title + exhibit per slide) for approval, then content/design rules applied during build
depends_on: pptx (built-in, handles file mechanics), research-documentation (academic/formal prose), trading skills (performance-analysis, retrospective-writer for trading decks), self-correction
---

# Deck Standards

## Purpose

Communication-first content and design rules for any deck built in this vault, so slides are structured as an argument rather than a topic dump. Adapted from Gabberflast's `academic-pptx-skill` (MIT, github.com/Gabberflast/academic-pptx-skill) and generalized to three registers: academic, professional, and trading. This skill governs content and structure; the built-in `pptx` skill handles the actual `.pptx` file mechanics — always used together, this one first.

## When to use

- Any "make slides / build a deck / pitch this" request, regardless of register.
- Improving or restructuring an existing deck that reads as a topic dump rather than an argument.

## When NOT to use

- A single static image or one-off chart export — that's just the pptx skill, no argument to structure.
- The owner explicitly asks for design-forward / visual-narrative mode (public talk, non-specialist audience) — defer to the pptx skill's design-forward defaults instead; note it here and skip the rules below.

## Procedure

1. **Pick the register** (ask if unclear):

   | Register | Use for | Priority order |
   |---|---|---|
   | Academic | Conference talk, thesis defense, seminar, grant briefing | Argument -> evidence -> layout -> aesthetics |
   | Professional | Internship readout, project presentation, work pitch, client-facing deck | Argument -> evidence -> layout -> polish |
   | Trading | Strategy pitch, competition retrospective, performance review deck | Argument -> data -> layout -> aesthetics |

2. **State the one argument.** One claim the deck exists to make, in the language of that register (research question / project outcome / thesis-vs-plan verdict). Do not try to present everything — the rest goes in an appendix.

3. **Choose a narrative spine** and apply it consistently:
   - **SCR** (Situation / Complication / Resolution) — default for academic and most professional decks.
   - **Funnel** (broad context -> gap -> approach -> findings -> implications) — long-form academic or deep-dive professional.
   - **Answer-first** (conclusion, then support) — senior/time-pressured audiences: a manager readout, a grant panel, a trading committee.

4. **Write action titles, not topic labels.** Every content slide title is a complete sentence stating the takeaway. "Results" becomes "Sharpe improved 0.4 after adding the vol filter." One to two lines, 24-28pt bold.

5. **Ghost deck test before building anything.** List every proposed action title in sequence. Read them alone. They must tell the complete argument. If they don't, fix the outline — do not proceed to slides yet.

6. **Outline and confirm.** Produce the slide-by-slide outline (title, action title, exhibit type, register) and get the owner's approval before creating the file, always for decks over ~10 slides or complex content. Cheap to fix an outline; expensive to fix a built deck.

7. **Exhibit discipline.** One exhibit per slide (chart/table/diagram/screenshot). Must directly support the action title — cover the exhibit, does the title still stand alone? Annotate the key finding directly on the chart (arrow, highlight, callout), don't make the audience hunt. Figure left, interpretation right. Rebuild figures at presentation resolution; never paste a print-resolution chart.

8. **Text discipline.** ~40 words max body text per slide. Three to five bullets, one idea each. Telegraphic language is fine (drop articles, filler). Body text floor: 20pt — if it doesn't fit at 20pt, cut content, don't shrink the font.

9. **Citations (academic and any deck borrowing external figures/data).** In-slide citation on anything not original, 12-14pt muted, bottom of slide. References slide at the end, before the appendix. Professional/trading decks: cite data sources the same way if the audience wasn't in the room when the data was pulled (broker API pull date, Bloomberg, etc.) — lighter touch than academic but still real.

10. **Deck architecture by register:**

    - **Academic**: Title -> Motivation/Context -> Research Question (own slide) -> Methods -> Results (one finding per slide) -> Discussion/Limitations -> Conclusions (stays up for Q&A) -> References -> Appendix (Q&A prep, robustness checks).
    - **Professional**: Title -> Context/Problem -> Approach -> Key Results/Findings (one per slide) -> Recommendation or Next Steps -> Conclusions/Ask (stays up for Q&A) -> Appendix (backup detail, data sources).
    - **Trading**: Title -> Thesis/Setup -> Data/Backtest or Live Results -> Risk (drawdown, sizing, tripwires) -> Verdict vs Plan -> Next Steps/Ask -> Appendix (trade log detail).
    - Never end on "Thank You" or a blank slide in any register — end on the conclusions/recommendation slide, it stays on screen through Q&A.

11. **Design standards (communication-first, overrides pptx skill's design-forward defaults):**
    - White background, one sans-serif font throughout (Arial/Calibri), max three colors (one primary, one accent, one for emphasis). No decorative icons, no accent lines under titles, no stock imagery, no gradient palettes.
    - 16:9 widescreen default.
    - Left-align body text; center titles and axis labels only. Consistent grid, minimum 0.5" margins.
    - White space is a signal of clarity, not something to fill.

12. **Timing.** One slide per minute max. 10-min talk: 8-10 content slides. 15-min: 12-14. 20-min: 15-18. Mark cuttable slides in advance for time pressure.

13. **QA checklist before shipping** (run alongside the pptx skill's own QA):
    - Every content slide has an action title.
    - Ghost deck test passes.
    - One exhibit per slide, each annotated with the "so what."
    - Every borrowed figure/data point cited; References slide present if academic or citing external data.
    - Ends on conclusions/recommendation slide, not "Thank You."
    - Body text >= 20pt, titles >= 24pt.
    - No decorative elements that don't carry content.

## Style rules

- No em dashes, no AI-sounding language on any slide.
- One argument per deck. If the request is trying to cover two arguments, that's two decks or a main deck plus an appendix, not one sprawling deck.
- Outline gets the owner's approval before the file is built, every time past ~10 slides.

## Example

Academic deck request: "results" as a slide title becomes the action title "Treatment effect is significant across all three cohorts," with the effect-size chart on the left, a one-line interpretive bullet on the right, and the p-value cited at the bottom if drawn from someone else's replication data.

Professional deck request: "Q3 findings" becomes "Reconciliation backlog dropped 40% after the batch-job fix," with the before/after chart on the left and the root-cause bullet on the right.

## Links

Source: Gabberflast, `academic-pptx-skill`, MIT license, github.com/Gabberflast/academic-pptx-skill — academic register ported near-verbatim from `content_guidelines.md`; professional and trading registers generalized from it, unverified in production, revise after the first real deck.
