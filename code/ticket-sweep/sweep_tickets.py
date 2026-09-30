"""Ticket and task sweep for the SecondaryBrainForClaude vault.

Scans every TICK-*.yaml under 01-Projects/*/tickets/ and every markdown
checkbox task under 01-Projects/, then writes a generated status report to
99-Meta/generated/TICKET_STATUS.md: what's done, in progress, and left, per project,
plus drift against the hand-maintained TICKET_INDEX.md.

Read-only over tickets and notes; the only file written is TICKET_STATUS.md.
TICKET_INDEX.md stays canonical and hand-maintained (Architect's job); this
report flags drift, it never edits the index.

Usage (from vault root): python3 code/ticket-sweep/sweep_tickets.py
"""

import os
import re
import glob
from datetime import date

DONE_STATUSES = {"done", "archived"}
ACTIVE_STATUSES = {"specced", "coding", "review", "in-progress"}  # in progress
LEFT_STATUSES = {"draft"}

def read(p):
    with open(p, encoding="utf-8", errors="ignore") as f:
        return f.read()

def scan_tickets():
    """Parse id/project/title/status from every ticket yaml."""
    tickets = []
    for p in sorted(glob.glob("01-Projects/*/tickets/TICK-*.yaml")):
        t = read(p)
        get = lambda k: (re.search(rf"^{k}:\s*(.+)$", t, re.M) or [None, ""])[1]
        tickets.append({
            "id": get("id").strip() or os.path.basename(p).replace(".yaml", ""),
            "project": get("project").strip(),
            "title": get("title").strip(),
            "status": get("status").split("#")[0].strip(),
            "path": p,
        })
    return tickets

def scan_checkboxes():
    """Collect - [ ] / - [x] tasks from markdown under 01-Projects/."""
    tasks = []
    for p in sorted(glob.glob("01-Projects/**/*.md", recursive=True)):
        for line in read(p).splitlines():
            m = re.match(r"\s*- \[( |x|X)\]\s+(.*)", line)
            if m:
                tasks.append({
                    "done": m.group(1).lower() == "x",
                    "text": m.group(2).strip(),
                    "file": p,
                })
    return tasks

def index_drift(tickets):
    """Tickets whose status disagrees with TICKET_INDEX.md, or missing a row.

    Rows are matched on id AND project: ticket ids are only unique within a
    project (TICK-008 and TICK-009 each exist in two projects), so matching on
    id alone takes whichever row comes first and compares the wrong ticket.
    """
    idx = read("99-Meta/TICKET_INDEX.md")
    done_section = idx.split("## Done")[-1]
    drift = []
    for tk in tickets:
        pat = rf"\|\s*{re.escape(tk['id'])}\s*\|\s*{re.escape(tk['project'])}\s*\|[^\n]*"
        row = re.search(pat, idx)
        name = f"{tk['id']} ({tk['project']})"
        if not row:
            drift.append(f"{name}: no row in TICKET_INDEX.md")
        elif tk["status"] in DONE_STATUSES and not re.search(pat, done_section):
            drift.append(f"{name}: status {tk['status']} but not in the Done section")
        elif tk["status"] not in DONE_STATUSES and tk["status"] not in row.group(0):
            drift.append(f"{name}: yaml says {tk['status']}, index row disagrees")
    return drift

def main():
    tickets = scan_tickets()
    tasks = scan_checkboxes()
    drift = index_drift(tickets)
    today = date.today().isoformat()

    by = lambda ss: [t for t in tickets if t["status"] in ss]
    done, active, left = by(DONE_STATUSES), by(ACTIVE_STATUSES), by(LEFT_STATUSES)
    known = DONE_STATUSES | ACTIVE_STATUSES | LEFT_STATUSES
    other = [t for t in tickets if t["status"] not in known]  # never drop a ticket silently
    t_done = [t for t in tasks if t["done"]]
    t_open = [t for t in tasks if not t["done"]]

    out = [
        "---", "type: meta", "status: generated",
        f"updated: {today}",
        "generator: code/ticket-sweep/sweep_tickets.py", "---", "",
        "# Ticket Status (generated, do not hand-edit)",
        "",
        f"> Generated {today}. Canonical index: [[TICKET_INDEX]]. Live board: [[TICKET_BOARD]].",
        "",
        f"**Tickets:** {len(tickets)} total: {len(done)} done, {len(active)} in progress, "
        f"{len(left)} left (draft), {len(other)} unbucketed",
        f"**Checkbox tasks (01-Projects):** {len(t_done)} done, {len(t_open)} open",
        "",
    ]
    for label, group in (("In progress", active), ("Left (draft)", left), ("Done", done),
                         ("Unbucketed (status matches no bucket)", other)):
        out.append(f"## {label}")
        out.append("")
        if not group:
            out.append("none")
        for t in group:
            out.append(f"- {t['id']} ({t['project']}): {t['title']} [{t['status']}]")
        out.append("")

    out.append("## Open checkbox tasks by file")
    out.append("")
    cur = None
    for t in t_open:
        if t["file"] != cur:
            cur = t["file"]
            out.append(f"**{cur}**")
        out.append(f"- [ ] {t['text']}")
    out.append("")
    out.append("## Index drift")
    out.append("")
    out.extend([f"- {d}" for d in drift] or ["none"])
    out.append("")

    with open("99-Meta/generated/TICKET_STATUS.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"tickets: {len(tickets)} total: {len(done)} done, {len(active)} in progress, "
          f"{len(left)} draft, {len(other)} unbucketed; "
          f"tasks: {len(t_open)} open; drift: {len(drift)} -> 99-Meta/generated/TICKET_STATUS.md")

if __name__ == "__main__":
    main()
