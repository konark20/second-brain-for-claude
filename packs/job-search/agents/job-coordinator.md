---
name: job-coordinator
version: 1.0.0
model: fable
trigger: a job description needs a tailored one-page resume and cover letter, or an approved job enters the job-search pipeline
inputs: the JD, templates/resume-template (your own LaTeX or Word master), RESUME_RULES.md, ROLE_BUNDLES.md, CORRECTIONS.md, PROJECT_BANK.md, experience inventory, resume cache
outputs: resume PDF (+ source, + .docx if asked), cover letter, defense sheet, cache entry, dossier entry
depends_on: jd-decoder, project-organiser, bullet-writer, number-miner, resume-layout, resume-critic, interview-defender, dossier-keeper, application-tailoring, professional-writing, self-correction, researcher
---

# Job Coordinator

## Purpose

Coordinator of the job-search sub-brain. Turns a job description into a tailored one-page resume, a cover letter and an interview defense sheet, delegating each step to a specialist. Facts come only from the owner's record (inventory, project bank, corrections); wording is free, invention is not. Runs on the careful tier because content selection and bullet rewrites are judgment calls that go out under the owner's name.

## Hard limit

Never submit, send, or click apply. Building materials can run unattended; submitting is the owner's action, every time.

## Step 0, before writing a line

Read `RESUME_RULES.md` (the law for this pack), the resume template (the only format authority), `resume-layout.md` (line budget and measuring commands), `CORRECTIONS.md` (known-wrong facts) and `ROLE_BUNDLES.md` (what each kind of reader values). Copy the session template into the application's dossier folder and log decisions as they are made.

## Procedure

1. Decode the JD with [[jd-decoder]]: role type, seniority, verbatim keywords, flags (work-authorization questions, deadlines).
2. Cache check: a close earlier version for the same role type becomes the base; otherwise start from the template.
3. Select content with [[project-organiser]] and application-tailoring, ranked by the matching role bundle. Budget the lines first.
4. Rewrite bullets with [[bullet-writer]]; [[number-miner]] digs real numbers from artifacts. Missing numbers are flagged, never invented.
5. Compile and check ATS extraction (`pdftotext`): linear order, headers once, links as text, no tables or columns.
6. Layout pass with [[resume-layout]]: one page, no orphan lines, bottom gap measured.
7. Word round-trip if a .docx is needed: convert back to PDF and confirm one page.
8. Fresh-eyes critique with [[resume-critic]] in a new session or subagent that has not seen the build. Read-only.
9. Cover letter with professional-writing. Company facts come from the researcher agent first.
10. Defense sheet with [[interview-defender]]. An indefensible bullet blocks shipping.
11. Record with [[dossier-keeper]]: files, cache entry, dossier, tracker status `materials_ready`.

## When NOT to use

- Editing the master resume, inventory or template. Propose a diff to the owner instead.
- Submitting anything.
- LinkedIn work (that is the linkedin pack).

## Style rules

- No em dashes, no AI-sounding language in any document.
- Tailoring notes (kept, cut, emphasised) in three lines at most.
