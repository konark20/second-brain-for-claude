---
name: resume-layout
version: 1.0.0
trigger: any resume compiled or edited, before it is marked ready or published
inputs: the compiled resume PDF and its .tex
outputs: a pass/fail layout report and fixes, so no space is wasted and nothing wraps badly
depends_on: RESUME_RULES, job-coordinator
---

# Resume Layout (the space-wastage guard)

One job: no wasted space, no ugly wraps. Every resume passes this before it ships. This is the enforcement layer for RESUME_RULES 10-15 and 11a-11e.

## BUDGET THE LINES BEFORE WRITING (added 2026-09-20, do this first)

Measuring after compiling catches overflow too late. On 2026-09-20 a single build overflowed to two pages four separate times because content was added and then measured. Budget first.

Usable text height at 0.7in margins, 10pt Times: **~57 lines**. Allocate before writing:

| Block | Lines |
|---|---|
| Header (name + contact) | 3 |
| Section header (each) | 2 |
| Education entry (heading + coursework) | 2 each |
| Experience entry heading | 1 each |
| Bullet | 2 (assume two lines; a one-line bullet is a bonus, never a plan) |
| Project entry (heading + 2 bullets) | 5 |
| Skills line | 1-2 |

Sum the plan. If it exceeds 57, cut before writing, not after. Then compile and verify with the command below. A build that needs more than one re-fit round means the budget was skipped.

## VERIFY THE WORD FILE TOO (added 2026-09-20)

The PDF passing is not the resume passing. A two-page .docx with collapsed dates shipped on 2026-09-20 because only the PDF was checked.

```
libreoffice --headless --convert-to pdf --outdir /tmp/check resume.docx
pdfinfo /tmp/check/resume.pdf | grep Pages
```

Word must be one page, and every date must right-align to the same x-coordinate as the PDF. The tab stop is derived from text width (8.5in − 2×margin), never a hardcoded DXA constant.

## MEASURE the bottom gap, do not eyeball it (added 2026-07-22)

Whitespace at the bottom is the #1 recurring defect. Measure it every time with pdfplumber, do not judge by eye:

```
python3 -c "import pdfplumber; p=pdfplumber.open('resume.pdf').pages[0]; m=max(w['bottom'] for w in p.extract_words()); print('gap lines:', round(((p.height-40)-m)/12,1))"
```

Target: bottom gap under ~3 lines. If larger, FILL before shipping, in this order: (a) give every project a second bullet, (b) add a 4th/5th relevant project, (c) add the next-best experience bullet, (d) deepen the lead role. A resume with 5+ lines of bottom gap and one-bullet projects is a fail, not a pass. Prefer 4 projects with 2 bullets over 5 projects with 1 bullet (fewer, better-explained).

## Checks (run pdftotext -layout on the compiled PDF)

1. **Page count.** Tailored resume is exactly 1 page. Master may be 2-3. Over by a few lines: tighten bullets or drop the weakest project. Under-filled: fill per the gap rule above, never leave a half-empty page.
2. **Orphan lines.** No bullet, coursework, or skills line ends with 1-3 words stranded on their own line. Flag any line with <=3 words that is a wrap continuation, then reword (shorten to fit, or lengthen so the last line is full).
3. **Fill density.** Target the master's first-page density. Each skills line fills ~85% of the width. Coursework lines are full or collapse to one clean line.
4. **Heading lines.** One-line headings (Company, Country | Role ... Date) must not wrap; shorten the role/title if they do.
5. **Uniformity.** Experience ordered most-relevant-first then reverse-chronological, consistently within the resume.
6. **Bottom balance.** Top and bottom margins visually even, content reaches near the bottom without spilling.

## Output

A short report: page count, any orphan lines with the offending text, fill assessment, and the specific fix applied. If a fix can't hold one page, escalate to job-coordinator to rebalance experience vs projects.

## Note

Compile gotcha: if the section-title font trips microtype ("auto expansion is only possible with scalable fonts"), load microtype with `expansion=false` (no visual change). If a synced folder serves a stale or truncated .tex, rewrite it via a heredoc before compiling.

## When NOT to use

- Content decisions (which bullets, what wording) belong to bullet-writer and the organiser; this skill only judges layout and fill.
