"""Capability scan for the SecondaryBrainForClaude vault.

The sensor half of the capability-auditor agent. Reads every agent, skill,
portable skill, slash command, and proposed draft, then reports what the files
alone can prove: catalog drift, reference graph, usage evidence, conformance,
and overlap. It judges nothing. The auditor agent reads this and decides.

Read-only over the vault. Stdlib only. Writes one file only when --out is given.

Usage (from anywhere): python3 code/capability-audit/scan.py [--out PATH]
"""

import glob
import math
import os
import re
import sys
from collections import Counter
from datetime import date

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(ROOT)

ACTIVE = ("agent", "skill", "portable")
STOP = set("""the and for with that this from into when will each not are but you its per one any all
can has have use used using only their then than them they what which who how why also more most other
such over out via was were been being does did done make made""".split())
EMOJI = re.compile("[\U0001F300-\U0001FAFF✅❌✨]")
AI_WORDS = ("delve", "landscape", "moreover", "in essence", "seamless", "leverage")


def read(p):
    with open(p, encoding="utf-8", errors="ignore") as f:
        return f.read().replace("\r\n", "\n")


def norm(p):
    return p.replace("\\", "/")


def frontmatter(t):
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            if k.strip() and not line.startswith((" ", "-", "#")):
                fm[k.strip()] = v.strip()
    return fm


def wikilinks(t):
    t = t.replace("\\|", "|")
    return {m.split("|")[0].split("#")[0].strip().rsplit("/", 1)[-1] for m in re.findall(r"\[\[([^\]]+)\]\]", t)}


def collect():
    caps = []

    def add(kind, p):
        p = norm(p)
        t = read(p)
        fm = frontmatter(t)
        stem = os.path.splitext(os.path.basename(p))[0]
        caps.append(dict(kind=kind, stem=stem, name=fm.get("name") or stem, path=p, fm=fm, text=t))

    for p in sorted(glob.glob("99-Meta/agents/*.md")):
        add("agent", p)
    for p in sorted(glob.glob("99-Meta/agents/proposed/*.md")):
        add("proposed", p)
    for p in sorted(glob.glob("99-Meta/skills/**/*.md", recursive=True)):
        add("proposed" if "/proposed/" in norm(p) else "skill", p)
    for p in sorted(glob.glob("skills/*/*.md")):
        add("portable", p)
    for p in sorted(glob.glob(".claude/commands/*.md")):
        add("command", p)
    return caps


def all_stems():
    s = {}
    for dp, dns, fns in os.walk("."):
        dns[:] = [d for d in dns if not d.startswith(".") and d not in ("node_modules", "__pycache__", "_local-only")]
        for f in fns:
            if f.endswith(".md"):
                s.setdefault(os.path.splitext(f)[0], []).append(norm(os.path.join(dp, f))[2:])
    return s


def dated_docs():
    docs = []
    for p in glob.glob("05-Journal/*.md"):
        m = re.match(r"(\d{4}-\d\d-\d\d)", os.path.basename(p))
        if m:
            docs.append(("journal", norm(p), read(p), m.group(1)))
    for p in glob.glob("01-Projects/**/runs/**/*", recursive=True):
        if os.path.isfile(p) and p.endswith((".md", ".yaml", ".yml")):
            m = re.search(r"(\d{4}-\d\d-\d\d)", p)
            docs.append(("run", norm(p), read(p), m.group(1) if m else ""))
    for p in glob.glob("01-Projects/*/tickets/*.yaml"):
        t = read(p)
        ds = re.findall(r"\d{4}-\d\d-\d\d", t)
        docs.append(("ticket", norm(p), t, max(ds) if ds else ""))
    return docs


def drift(caps, st):
    maps = read("99-Meta/SKILL_MAP.md") + "\n" + read("99-Meta/SKILL_INDEX.md")
    linked = wikilinks(maps)
    sel = wikilinks(read("99-Meta/MODEL_SELECTOR.md"))
    out = {}
    out["on disk, not in SKILL_MAP or SKILL_INDEX"] = [c["path"] for c in caps if c["kind"] in ACTIVE and c["stem"] not in linked and c["name"] not in linked]
    out["agents missing from MODEL_SELECTOR roster"] = [c["stem"] for c in caps if c["kind"] == "agent" and c["stem"] not in sel]
    rows = set(re.findall(r"^\|\s*\[\[([^\]|\\]+)", maps, re.M))
    out["catalog row points at no file"] = sorted(r for r in rows if r not in st)
    out["catalog row points at an archived file"] = sorted(r for r in rows if r in st and all(x.startswith("04-Archives/") for x in st[r]))
    out["slash commands with no catalog mention"] = [c["stem"] for c in caps if c["kind"] == "command" and "/" + c["stem"] not in maps]
    return out


def usage(caps, docs):
    rows = {}
    for c in caps:
        n = re.escape(c["stem"])
        ex = re.compile(r"(?:\[\[|`|/)" + n + r"(?![\w-])")
        pl = re.compile(r"(?<![\w-])" + n + r"(?![\w-])", re.I)
        jd, rf, plain, last = 0, 0, 0, ""
        for kind, p, t, d in docs:
            if p == c["path"]:
                continue
            if ex.search(t):
                if kind == "journal":
                    jd += 1
                else:
                    rf += 1
                if d and d > last:
                    last = d
            plain += len(pl.findall(t))
        refs = 0
        for o in caps:
            if o["path"] == c["path"]:
                continue
            if c["stem"] in wikilinks(o["text"]) or c["stem"] in o["fm"].get("depends_on", ""):
                refs += 1
        rows[c["path"]] = dict(journal_days=jd, run_files=rf, plain=plain, last=last, refs_in=refs)
    return rows


def conformance(caps, st):
    issues = []
    for c in caps:
        t, fm, p = c["text"], c["fm"], c["path"]
        if c["kind"] in ("agent", "skill", "proposed"):
            miss = [k for k in ("name", "trigger") if not fm.get(k)]
            if miss:
                issues.append((p, "frontmatter missing " + ", ".join(miss)))
            if "when not" not in t.lower():
                issues.append((p, "no 'When NOT to use' section"))
        if c["kind"] == "portable" and not (fm.get("trigger") or fm.get("description")):
            issues.append((p, "portable skill has no description"))
        em = t.count("—")
        if em:
            issues.append((p, "%d em dash(es)" % em))
        if EMOJI.search(t):
            issues.append((p, "emoji present"))
        ai = [w for w in AI_WORDS if w in t.lower()]
        if ai and c["kind"] != "command":
            issues.append((p, "AI-sounding word: " + ", ".join(ai)))
        if len(t) > 8000 and c["kind"] in ("agent", "skill"):
            issues.append((p, "long (%d bytes), check the one-job rule" % len(t)))
        bad = sorted(l for l in wikilinks(re.sub(r"```.*?```", "", t, flags=re.S)) if l not in st and l and not re.search(r"[\s]", l))
        if bad:
            issues.append((p, "unresolved wikilink(s): " + ", ".join(bad[:4])))
    return issues


def toks(s):
    return [w for w in re.findall(r"[a-z][a-z\-]{3,}", s.lower()) if w not in STOP]


def desc(c):
    m = re.search(r"##\s*Purpose\s*\n+(.{0,700})", c["text"], re.S)
    return " ".join([c["name"], c["fm"].get("trigger", "") or c["fm"].get("description", ""), m.group(1) if m else ""])


def overlap(caps, top=12):
    pool = [c for c in caps if c["kind"] in ACTIVE]
    docs = [Counter(toks(desc(c))) for c in pool]
    df = Counter(w for d in docs for w in d)
    n = len(pool)
    vecs = []
    for d in docs:
        v = {w: (1 + math.log(k)) * math.log(n / df[w]) for w, k in d.items()}
        vecs.append((v, math.sqrt(sum(x * x for x in v.values())) or 1))
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            a, na = vecs[i]
            b, nb = vecs[j]
            s = sum(a[w] * b.get(w, 0) for w in a) / (na * nb)
            ci, cj = pool[i], pool[j]
            linked = cj["stem"] in wikilinks(ci["text"]) or ci["stem"] in wikilinks(cj["text"])
            pairs.append((s, ci, cj, linked))
    pairs.sort(key=lambda x: -x[0])
    return pairs[:top]


def render(caps, st):
    docs = dated_docs()
    dr, us, cf, ov = drift(caps, st), usage(caps, docs), conformance(caps, st), overlap(caps)
    o = ["# Capability scan %s" % date.today().isoformat(), ""]
    o.append("Sensor output only, no judgment. Generated by code/capability-audit/scan.py. `explicit` counts marked references ([[x]], `x`, /x); `plain` counts bare word hits and is noisy for common words. File mtimes are unreliable on this vault (sync resets them), so dates come from filenames and note content.")
    o += ["", "## Counts", ""]
    for k, v in sorted(Counter(c["kind"] for c in caps).items()):
        o.append("- %s: %d" % (k, v))
    o += ["", "## Catalog drift", ""]
    for k, v in dr.items():
        o.append("- %s: %s" % (k, ", ".join(v) if v else "none"))
    o += ["", "## Usage and references", "", "| Capability | Kind | Refs in | Journal days | Run/ticket files | Plain hits | Last seen | Flags |", "|---|---|---|---|---|---|---|---|"]
    for c in caps:
        u = us[c["path"]]
        fl = []
        if c["kind"] in ACTIVE and u["refs_in"] == 0:
            fl.append("no-refs")
        if c["kind"] in ("agent", "skill") and u["journal_days"] + u["run_files"] == 0:
            fl.append("no-usage-evidence")
        o.append("| %s | %s | %d | %d | %d | %d | %s | %s |" % (c["stem"], c["kind"], u["refs_in"], u["journal_days"], u["run_files"], u["plain"], u["last"] or "-", " ".join(fl)))
    o += ["", "## Conformance", ""]
    o += ["- %s: %s" % (p, m) for p, m in cf] or ["none"]
    o += ["", "## Overlap (top pairs by trigger and purpose similarity)", "", "| Score | A | B | Already linked |", "|---|---|---|---|"]
    for s, a, b, ln in ov:
        o.append("| %.2f | %s (%s) | %s (%s) | %s |" % (s, a["stem"], a["kind"], b["stem"], b["kind"], "yes" if ln else "NO"))
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    out = render(collect(), all_stems())
    if "--out" in sys.argv:
        path = sys.argv[sys.argv.index("--out") + 1]
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        print("wrote", path)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(out)
