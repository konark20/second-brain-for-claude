---
tags: [skill, writing]
name: professional-writing
version: 1.0.0
description: Use this skill whenever writing or replying to emails, messages, or other professional/academic correspondence — whether drafting from scratch or replying to a pasted-in email, for work contexts (colleagues, recruiters, managers) or academic contexts (professors, university administration). Make sure to trigger this whenever the user asks to "write an email," "reply to this," "draft a message to," "respond to my professor/manager/recruiter," or pastes in an email and asks what to say back, even if they don't explicitly mention tone or formatting. Produces polite, neutral, human-sounding correspondence that avoids common AI-writing tells (em dashes, emoji, excessive hedging, bullet-point overuse, flowery language).
---

# Professional Writing

This skill helps draft and reply to professional and academic correspondence in a tone that reads as genuinely human: polite, neutral, direct, and appropriately brief. The core failure mode this skill exists to prevent is correspondence that is technically fine but reads as obviously AI-generated — over-hedged, overly structured, or stuffed with phrasing patterns that don't show up in how people actually write to each other.

## Before drafting: resolve ambiguity first

Don't draft on a guess if something material is missing or unclear. Ask first when:
- The relationship/seniority isn't clear (e.g. is this person a peer, a superior, a professor, a recruiter?) and it would change the tone
- The ask itself is ambiguous (e.g. "reply to this" but it's not clear what the reply should actually say or commit to)
- There's a factual gap only the user can fill (a date, a number, a decision)

Don't ask about things that don't matter much, like exact phrasing preference or whether to say "Hi" vs "Hello" — just make a reasonable call per the rules below. One good clarifying question beats a drafted email that has to be redone.

## Tone

Default tone is polite, neutral, and non-confrontational, matching how the owner prefers to communicate professionally: humble rather than self-promotional, direct rather than padded, and never pushy.

This applies whether the email is to a colleague, a manager, a recruiter, or a professor. The formality level shifts with context (see Greetings and signoffs below) but the underlying voice — calm, courteous, to the point — doesn't change.

## Length

Match the email to what it actually needs to say. Most professional and academic emails should run short to medium: long enough to be complete and clear, short enough that the reader isn't doing work to extract the point. Don't pad a two-sentence request into five paragraphs, and don't compress something that genuinely needs context into a single clipped line.

A useful check: if a sentence could be cut without losing information, cut it.

## Greetings and signoffs

Vary by context rather than using one fixed template:

**Academic (professors, university administration, advisors)**
- Slightly more formal greeting: "Dear Professor [Last Name]," or "Hi Professor [Last Name],"
- Signoff: "Best regards," or "Thank you," followed by full name

**Work (colleagues, managers, recruiters, industry contacts)**
- Greeting matches the relationship: "Hi [First Name]," is the safe default; use "Hello [First Name]," for a first-touch or more senior/external contact
- Signoff: "Best," or "Thanks," followed by name — keep it short

If the email being replied to gives a clear signal (the other person signed off casually, or very formally), match that register rather than defaulting blindly.

## What to avoid

These are the specific patterns that make writing read as AI-generated. Avoid all of them by default:

**Em dashes.** Never use them. Use a period, comma, or "and"/"but" to join the thought instead. If a sentence seems to need an em dash, it usually means the sentence should be split into two.

**Emoji.** Never use them in professional or academic correspondence, regardless of how casual the relationship is.

**Hedging openers.** Avoid throat-clearing phrases that delay the actual point: "I just wanted to reach out and...", "I hope this email finds you well", "I wanted to circle back regarding...". Open with the actual content. If a pleasantry is warranted (e.g. first message to a professor, or after time has passed), one short, genuine line is enough — not a formula.

**Bullet-point overuse.** Most emails should be written in prose, not lists. Reach for bullets only when there are genuinely 3+ parallel items that are easier to scan as a list (e.g. listing several available times, or several discrete questions). A two- or three-sentence email does not need bullets.

**Flowery or inflated language.** Avoid words and phrasing that sound performative rather than plain: "I am thrilled to...", "I would be delighted to...", "please don't hesitate to...". Say the plain version instead: "I'd like to...", "happy to...", "let me know if...".

**Over-structuring.** Don't add headers, bold section labels, or numbered structure to something that's just a short message between two people. Save structure for genuinely long or multi-part academic/report writing, not everyday correspondence.

**Generic closing filler.** Avoid closing lines that exist only to pad length, like "Thank you for your time and consideration" tacked onto every email regardless of fit, or "Looking forward to hearing from you" when there's nothing specific being awaited.

## Drafting from scratch vs. replying

**Replying to a pasted-in email:** Read what's actually being asked or said before drafting. Address it directly and in the order it matters, not necessarily the order it was raised. Don't restate the entire original email back to the sender; they already know what they wrote.

**Drafting from scratch:** Confirm the goal of the email in one line to yourself before writing (what does the owner want the reader to know, decide, or do after reading this), then write toward that directly.

## Output

Present the drafted email in plain text, ready to send as-is. Don't wrap it in unnecessary preamble like "Here's a draft:" beyond a brief one-line lead-in — the owner wants something they can copy directly. If something was ambiguous and a judgment call was made, note the assumption briefly after the draft rather than before it, so the email itself isn't preceded by clutter.

## De-slop pass

Before delivering, run the scored de-slop pass in [[ai-writing-tells]] (03-Resources): cut the banned phrases and structural cliches, then rate the 5 dimensions. Do not ship prose scoring under 35/50. Cite the score rather than asserting it reads clean.
