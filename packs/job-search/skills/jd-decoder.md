---
name: jd-decoder
version: 1.0.0
trigger: a new job description enters the pipeline
inputs: raw JD text or link
outputs: a structured JD profile used by project-organiser, application-tailoring and bullet-writer
depends_on: PROJECT_BANK buckets, RESUME_RULES, your keyword bank
---

# JD Decoder

One job: turn a JD into a structured profile so tailoring becomes mechanical.

## Output (stored with the tracker entry)

- role_type: one of your PROJECT_BANK buckets, plus a secondary bucket
- seniority: intern, entry, mid, senior, and the years of experience asked
- hard requirements: degree, skills, certifications, authorizations explicitly required
- keywords: exact phrases from the JD (tools, methods, domain terms), ranked by frequency and position, cross-checked against your keyword bank for that bucket
- preset: which coursework or skills block variant to use
- boxes: which PROJECT_BANK boxes fit, and the lead angle for each
- flags: work-authorization question present, unusual application fields, deadline

## Rules

- Keywords are copied verbatim, never paraphrased. Applicant tracking systems match strings.
- Work-authorization and sponsorship questions are flagged, never answered by the brain.
- Read seniority honestly. If the JD asks for a different graduation year or level, flag the fit rather than hide it.

## When NOT to use

- Choosing wording or numbers (bullet-writer, number-miner).
- Answering anything on an application form.
