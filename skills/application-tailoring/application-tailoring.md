---
tags: [skill, writing]
name: application-tailoring
version: 1.0.0
description: "Use this skill whenever the user is filling out an internship, job, or program application — answering free-text application questions, writing tailored experience descriptions, drafting cover-letter-style responses, or structuring answers around what a specific company/program is looking for. Trigger for requests like 'help me fill out this internship application,' 'tailor my answer to this question,' 'how do I answer why are you interested in X,' 'what should I write for work experience,' or any application question with a word limit and a specific company/role in mind. Works in any domain (law, finance, tech, consulting, academia). Combines a master experience inventory + ATS keyword optimization + role-specific tailoring + authentic-sounding prose. Designed to work alongside the professional-writing skill (tone, no AI tells) and self-correction (quality review)."
---

# Application Tailoring

This skill helps draft answers to application questions for internships, jobs, and programs. The core problem it solves: most applicants either write generic answers that get filtered out by ATS systems and bored human reviewers, or they over-optimize for ATS and produce keyword-stuffed responses that obviously read as AI-generated. This skill threads that needle — answers that satisfy the keyword/structure requirements humans and ATS systems look for, while still reading as genuine, specific, and human-written.

This skill works with the `professional-writing` skill (which governs tone — no em dashes, no AI tells, no hedging) and `self-correction` (which reviews output quality before presenting). It does not replace either; it adds application-specific workflow on top.

## The honest tension this skill manages

Two real forces pull in opposite directions, and the skill has to handle both:

- **ATS systems and busy reviewers** want clear signals: specific keywords from the job description, recognizable action verbs, structured answers that map cleanly to what was asked.
- **Human readers (especially at competitive firms)** screen *against* AI-written content. Answers that sound formulaic, over-polished, or stuffed with corporate buzzwords get rejected. They want a real person's voice, specific examples with concrete detail, and genuine reflection.

The way to satisfy both: keywords appear *naturally* inside specific stories with concrete detail. "Drafted 40 legal notices including RERA applications and arbitration notices under Section 21" hits the same keywords as "Possesses strong legal drafting skills" but reads as written by a real person who actually did the work.

## Step 1: Build or update the master inventory

Before answering any application question, the user needs a structured inventory of everything they could possibly draw from. This file persists across applications and gets updated as new experiences happen.

**Format:** YAML, saved as `application_inventory.yaml` in the user's working directory.

Structure:
```yaml
candidate:
  name: <full name>
  domain: <law, finance, tech, etc.>
  education:
    - institution: <name>
      degree: <degree, year>
      gpa: <if relevant>
      notable_coursework: <list>

experiences:
  - id: <short slug, e.g. "snk-chambers-2025">
    type: <internship | full_time | project | volunteer | competition>
    organization: <name>
    role: <title>
    dates: <e.g. "July 2025, 4 weeks">
    location: <city>
    description: <plain prose, what they actually did>
    quantified_outputs: <specific numbers — "drafted 40 legal notices," "presented to 50 attendees">
    skills_demonstrated: <list — drafting, research, client communication, etc.>
    tags: <list — for matching against JDs, e.g. "litigation," "real estate," "drafting">

skills:
  - skill: <name>
    proficiency: <how strong — concrete, not "expert">
    evidence: <which experience(s) show this>

certifications:
  - name: <full title>
    issuer: <organization>
    date: <when>
    relevance: <which kinds of roles this matters for>

publications_research:
  - title: <full title>
    venue: <journal / conference / publication>
    date: <when>
    summary: <one-line what it's about>

extracurriculars:
  - activity: <name>
    role: <position if any>
    dates: <when>
    note: <anything reviewer-worthy>

answer_bank:
  # Optional cache of past answers, added when user explicitly asks to save one for reuse
  - question_type: <e.g. "why_this_firm" | "work_experience" | "topic_of_interest">
    company: <if specific>
    answer: <the actual text>
    notes: <why this worked, or what to adapt for next time>
```

**Filling it in:** the inventory should hold *everything* — experiences that won't go on every application, courses that might be relevant to one role and not another, certifications that may or may not matter. The tailoring step picks what to use per application; the inventory just has to be complete.

When a user provides their resume and additional context (separate documents, notes, things they forgot to mention), parse all of it into the inventory. Don't trim — capture everything, even things the user might think aren't "professional enough." Volunteer work, competitions, sports achievements, study-abroad trips all matter for certain questions.

## Step 2: Analyze the application

Before writing any answer, get clear on what's actually being asked:

1. **Read the full application context** — the company/firm, the role, the specific questions, the word limits, any explicit instructions ("we want structure and succinctness," "your answer doesn't need to be related to law").
2. **Get and analyze the actual job description.** Don't draft from the question text alone. Ask the user for the JD and any firm/company links if they aren't already provided. The JD is where the keywords, the valued attributes, and the role's actual priorities live.
3. **Research the company before any "why this firm" answer (mandatory).** A "why this firm" answer drafted without real research will always come out generic, which is the single most common reason these answers fail. Before drafting one:
   - Web-search the company for recent, specific developments (mergers, notable matters, new practice areas, recent news from multiple sources, not just the firm's own site)
   - Identify what makes this firm specifically different from its competitors, not what's true of every firm in the sector
   - Ask the user what specifically drew them to this firm, so the answer reflects genuine interest, not researched-but-hollow praise
   - If real research isn't possible (no JD, no web access, no user input), do not draft a generic answer and present it as finished. Tell the user the answer needs real firm research first and what specifically to provide.
4. **Identify the question type.** Common application question categories:
   - **Why this company/firm/program** — tests genuine research and fit
   - **Work experience / what you've done** — tests substance and quantified output
   - **Skills and qualities you'd bring** — tests self-awareness and fit to role
   - **Tell us about a topic / personal interest** — tests communication, curiosity, depth (note: these are deliberately *not* role-related to see how the candidate thinks)
   - **Challenge / failure / proudest moment** — tests reflection and growth
   - **Hypothetical / what would you do** — tests judgment
5. **Extract keywords from the JD/company materials.** Look at the JD carefully and pull the language *they* use for the role (titles, skills, attributes they explicitly value). Those are the keywords worth threading into answers naturally.
6. **Note constraints:** word limit (count strictly), required structure ("full prose," "bullet points OK"), any forbidden topics, and crucially, multi-part questions (see Step 3.5).

## Step 3: Ask before drafting (always)

Don't draft an answer without first asking the user what they want to highlight, even if the inventory has obvious matches. People know their own stories better than any inventory can capture. Ask:

- Which experience(s) from the inventory do they want this answer to draw from? (Offer 2-3 reasonable candidates from the inventory if it's not obvious.)
- Is there a specific angle or detail they want emphasized?
- For "why this firm" type questions: what specifically draws them to this firm? (Don't draft generic answers; the user has a reason, the skill's job is to surface it.)
- For "topic of interest" questions: which topic do they want to use? (Offer suggestions from their inventory — research papers, courses, volunteer projects — but let them pick.)

This step is non-negotiable. Drafting before asking produces answers that miss the user's actual story, even when they look fine on paper.

## Step 3.5: Map themes across all questions before drafting any

When an application has multiple related questions (common: "why this firm" + "skills you'd bring" + "topic of interest" all in one application), do not draft them one at a time in isolation. That produces repetition, where the same experience or strength gets used to answer three different questions, which wastes the candidate's limited space and bores the reviewer.

Instead, map first, draft second:

1. **List all the questions** in the application and what each one is actually testing.
2. **List the candidate's strongest assets** (key experiences, skills, achievements, interests) from the inventory.
3. **Assign each asset to exactly one question** where it lands hardest. A drafting achievement might be strongest under "skills you'd bring"; a specific firm-relevant matter might be strongest under "why this firm"; a research paper might be strongest under "topic of interest." Once an asset is assigned to one question, it does not reappear in another.
4. **Draft each answer using only its assigned assets**, so the application as a whole covers maximum ground with zero repetition.

**The work experience question is the exception.** It is the one comprehensive, exhaustive answer: it should cover every relevant role (legal and non-legal, internships and volunteer work), each one elaborated with what was actually done. The no-repeat rule does not constrain it, because work experience is a complete record, not a selective highlight. Everything *else* draws selectively.

So the rule is twofold:
- **Work experience answer:** comprehensive. Every role, elaborated, including volunteer and non-legal work where relevant.
- **Every other answer:** selective. Pick the few strongest points that fit that specific question, present them well, and don't try to cram in everything. Depth on the right few beats shallow coverage of many.

## Step 4: Draft using STAR-or-equivalent structure, naturally

For experience-based answers, use a loose STAR structure (Situation, Task, Action, Result) but don't make it visible. The reader should not see "S: ... T: ... A: ... R: ...". The structure should be invisible scaffolding under natural prose.

For "why this firm" answers: open with a specific reason grounded in real research (a practice area, a recent matter or development found through actual web research, a value the firm publicly holds and that genuinely connects to the candidate). Connect it to a concrete element of the candidate's own work or interest. Close with what they hope to contribute or gain. No generic admiration that any applicant could write, and no information overload that just restates the work-experience answer. Keep it lean, specific, and driven by strong verbs. The research must be specific enough that a reviewer can tell this candidate actually looked into the firm, not just swapped the firm's name into a template.

For "topic of interest" answers: pick a topic with genuine depth in the candidate's background, lead with what's interesting about it, give one specific concrete detail that shows real knowledge, and explain why it matters to *them* (not just objectively important).

**Answer every part of a multi-part question.** Many application questions secretly contain two or three asks in one sentence. "Introduce us to a topic you know about and explain why it interests you" has two parts: the topic, AND why it interests the candidate personally. "What skills would you bring and why" has two parts. Identify every distinct ask in the question before drafting, and make sure the final answer addresses each one. A common failure is answering the first half thoroughly and forgetting the second; the "why" or the personal-connection part is often the part the reviewer cares about most, since it reveals the person rather than the fact.

**Action verbs.** Use strong, specific verbs aligned with what was actually done, not generic ones. For legal work: drafted, researched, briefed, argued, negotiated, structured, advised, reviewed. For finance: modeled, executed, hedged, calibrated, structured, analyzed. Match the verb to the actual action — don't say "led" if "contributed to" is honest.

**Quantification.** Whenever possible, include numbers: "drafted 40 legal notices," "presented to 50 attendees at NLU Lucknow," "secured 34/50 in the credit course." Numbers make answers stick in a reviewer's memory and signal substance.

**ATS keyword integration.** The keywords identified in Step 2 should appear in the answer, but only inside specific concrete claims — never in isolated phrases that look added on. Bad: "I have strong legal drafting skills, research skills, and litigation skills." Good: "Drafted 40+ legal notices and Section 21 arbitration notices during my internship at SNK Chambers."

## Step 5: Word count and structure check

Match the word limit strictly. "300 words" means 290-300, not 250 and not 320. Reviewers do count, especially at firms with high application volume.

Confirm any explicit structure requirement (full prose vs. bullets, paragraphs vs. a single block). "Full prose" means no bullet points, no headers, no list formatting.

## Step 6: Self-review (deferring to self-correction skill)

Before presenting the answer, do the standard self-correction checks: does it actually answer what was asked, is it the right length, does it sound like the candidate or like AI, do the claims match the inventory (no fabrication). Flag anything that doesn't fit.

Add one application-specific check: would a busy human reviewer reading 200 of these in one day remember this answer? If the answer is generic enough to swap with another candidate's, it needs more specific detail.

## Step 7: Offer to cache the answer (only if reusable)

After the answer is finalized, ask the user whether to save it to the `answer_bank` section of the inventory. Only suggest this for genuinely reusable answer types:

- "Why this firm" answers (adaptable for similar firms)
- "Topic of interest" answers (the same topic can be reused)
- "Skills you'd bring" answers (adaptable across similar roles)

Don't suggest caching one-off answers (e.g. "describe a specific case at this firm") that can't be reused.

If the user opts in, save it with notes about why it worked or what to change for similar applications. If they say no, just move on. The decision is theirs every time.

## What to avoid

- **Don't fabricate experiences.** Only use what's in the inventory. If the question asks about something the user hasn't done, ask them whether they have a real example to share or want to handle the question differently.
- **Don't keyword-stuff.** Every keyword should be inside a concrete claim, not floating in a list of attributes.
- **Don't write generic "passionate about" / "deeply interested in" openers.** Specific concrete reasons, not abstract enthusiasm.
- **Don't pad to hit word limits.** A 280-word answer that says everything is better than a 300-word answer that says the same thing slower.
- **Don't ignore explicit instructions.** "We want structure and succinctness" is a real signal — the firm is telling you they'll downrank rambling. "Your answer doesn't need to be related to law" means they actually want to see something off-topic, not a forced law connection.
