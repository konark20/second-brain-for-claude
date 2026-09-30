---
name: sentinel
version: 1.0.0
model: sonnet
trigger: before any git commit/push, before any file leaves the vault (GitHub, Drive, email, any external service), and on explicit /sentinel
inputs: the set of files about to be committed, pushed, or shared
outputs: pass/block verdict, quarantine actions, alert to the owner
depends_on: BOUNDARIES.md, .gitignore
---

# Sentinel

## Purpose

Identity-document firewall. The owner's vault and connected services may accidentally pick up scans or numbers from their core identity documents. If any of that is about to be committed, pushed, or shared, Sentinel flushes it out before it leaves the machine. Nothing on the blocklist ever reaches GitHub, Claude memory, or any external service, even a private repo.

## Blocklist (what counts as an identity document)

Numbers, scans, photos, or PDFs of:

- Passport (any country)
- Aadhaar card (12 digits, often spaced 4-4-4)
- US Social Security Number (XXX-XX-XXXX)
- PAN card (5 letters, 4 digits, 1 letter)
- Driver's license, state/national ID, voter ID
- Visa stamps, I-20, I-94, EAD, green card, any immigration document
- Bank account / routing numbers, credit or debit card numbers
- Any credential: API keys, tokens, passwords (already covered by BOUNDARIES, enforced here too)

Detection patterns (grep, case-insensitive, filenames and content):

```
filenames: passport|aadhaar|adhaar|ssn|social.?security|pan.?card|驾照|license|visa|i-?20|i-?94|ead|green.?card|dl.?scan
aadhaar:   \b[2-9][0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}\b
ssn:       \b[0-9]{3}-[0-9]{2}-[0-9]{4}\b
pan:       \b[A-Z]{5}[0-9]{4}[A-Z]\b
passport:  \b[A-Z][0-9]{7,8}\b   (verify context before flagging; high false-positive rate)
cards:     \b(?:[0-9][ -]?){15,16}\b  (Luhn-check before flagging)
secrets:   (api[_-]?key|token|secret|password)\s*[:=]\s*\S+ ; github_pat_[A-Za-z0-9_]+ ; -----BEGIN .*PRIVATE KEY
```

Image/PDF files cannot be grepped: any image or PDF whose filename or containing folder matches the filename patterns is treated as a hit without opening it.

## Procedure

1. Enumerate the exact file set about to leave (git staged files, or the files named in the share request).
2. Run the detection patterns over filenames and text content.
3. On any hit:
   a. BLOCK the commit/push/share. No exceptions, no "it's private so it's fine."
   b. Move the offending file to `_local-only/` at vault root (gitignored, never synced). Numbers embedded inside an otherwise-fine note: redact the number in place, show the owner the diff.
   c. If the file is already in git history, purge it from history before any push.
   d. Alert the owner: file, pattern matched, action taken. One line each.
   e. Never copy the matched content into memory, logs, journal entries, or this report beyond the filename and pattern name. The value itself is never quoted anywhere.
4. On zero hits: stay silent. Do not prompt or announce; just let the operation proceed. (Silent-when-clean, per BOUNDARIES 2026-07-28: the scan still runs every time, it only speaks when it finds something. A one-line "sentinel: clean, N files" may go to the journal/log but not to the owner as a prompt.)
5. Deletion policy: Sentinel quarantines by default rather than hard-deleting, so the owner never loses their only copy of a document. If the owner says "delete it" on an alert, delete it. To make hard-delete the default, they flip `on_hit: quarantine` to `on_hit: delete` below.

```yaml
on_hit: quarantine   # quarantine | delete
```

## When NOT to use

- Not a general secrets manager. It does not store or rotate credentials.
- Does not scan `04-Archives/` or hidden folders at rest (BOUNDARIES). It scans anything from those locations only if it is about to leave the machine.
- The owner's name, email, phone, education, and work history are resume data, not identity documents. Sentinel does not block those; the private-repo boundary handles them.

## Hard limits

- Sentinel can never be skipped for speed. A push without a sentinel pass does not happen.
- False positives get shown to the owner, never silently unblocked.
- Sentinel itself never writes any matched value into any file, including quarantine logs.

## Links

- [[BOUNDARIES]]
- [[SKILL_MAP]]
- [[janitor]]
