"""Graph intelligence for the vault link-suggester.

Mined from nashsu/llm_wiki (the 4-signal relevance model, Louvain community
detection, and knowledge-gap detection), reimplemented as pure-local Python.
Nothing leaves the machine. networkx is used when available for Louvain and
gives a cleaner result; without it, a connected-components fallback runs so
the script never hard-fails.

Signals (combined with the TF-IDF cosine from suggest_links.py):
    direct link   x3.0   an existing [[wikilink]] between the two notes
    source overlap x4.0   shared frontmatter sources[]; falls back to shared
                          folder + shared tags when sources[] is absent
    Adamic-Adar   x1.5   shared neighbors in the wikilink graph, rarer
                          shared neighbors weighted higher
    type affinity x1.0   same frontmatter `type:` (concept<->concept, etc.)
"""

import os
import re
import math
from collections import defaultdict

W_DIRECT = 3.0
W_SOURCE = 4.0
W_ADAMIC = 1.5
W_TYPE = 1.0


def _name(path):
    return os.path.splitext(os.path.basename(path))[0].lower()


def _frontmatter(text):
    """Return (type, tags set, sources list) from YAML frontmatter, best-effort."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return "", set(), []
    fm = m.group(1)
    typ = (re.search(r"^type:\s*(.+)$", fm, re.M) or [None, ""])[1].strip()
    tags = set()
    tm = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
    if tm:
        tags = {t.strip().strip('"\'') for t in tm.group(1).split(",") if t.strip()}
    sources = []
    sm = re.search(r"^sources:\s*\[(.*?)\]", fm, re.M)
    if sm:
        sources = [s.strip().strip('"\'') for s in sm.group(1).split(",") if s.strip()]
    return typ, tags, sources


def build_graph(notes):
    """Return per-note metadata and the undirected wikilink adjacency."""
    meta = {}
    for p, t in notes.items():
        typ, tags, sources = _frontmatter(t)
        meta[p] = {
            "name": _name(p),
            "folder": p.split("/")[0] if "/" in p else "(root)",
            "type": typ,
            "tags": tags,
            "sources": set(sources),
            "links": set(re.findall(r"\[\[([^\]|#]+)", t)),
        }
    name_to_path = {meta[p]["name"]: p for p in notes}
    adj = defaultdict(set)
    for p in notes:
        for raw in meta[p]["links"]:
            tgt = name_to_path.get(_name(raw))
            if tgt and tgt != p:
                adj[p].add(tgt)
                adj[tgt].add(p)
    return meta, adj, name_to_path


def signal_score(a, b, meta, adj):
    """Weighted 4-signal relevance between notes a and b (paths)."""
    ma, mb = meta[a], meta[b]
    score = 0.0
    if b in adj[a]:
        score += W_DIRECT
    # source overlap, with folder+tag fallback when no sources[] frontmatter
    if ma["sources"] and mb["sources"]:
        if ma["sources"] & mb["sources"]:
            score += W_SOURCE
    else:
        if ma["folder"] == mb["folder"] and (ma["tags"] & mb["tags"]):
            score += W_SOURCE * 0.4  # weaker proxy, flagged in the note
    # Adamic-Adar over the wikilink graph
    common = adj[a] & adj[b]
    aa = sum(1.0 / math.log(len(adj[n])) for n in common if len(adj[n]) > 1)
    score += W_ADAMIC * aa
    if ma["type"] and ma["type"] == mb["type"]:
        score += W_TYPE
    return score


def communities(notes, adj):
    """Louvain clusters via networkx if present, else connected components.
    Returns {community_id: [paths]} and a cohesion score per community."""
    try:
        import networkx as nx
        g = nx.Graph()
        g.add_nodes_from(notes)
        for a in adj:
            for b in adj[a]:
                g.add_edge(a, b)
        try:
            parts = nx.community.louvain_communities(g, seed=42)
        except Exception:
            parts = list(nx.connected_components(g))
    except ImportError:
        # stdlib connected-components fallback
        seen, parts = set(), []
        for start in notes:
            if start in seen:
                continue
            stack, comp = [start], []
            while stack:
                n = stack.pop()
                if n in seen:
                    continue
                seen.add(n)
                comp.append(n)
                stack.extend(adj[n] - seen)
            parts.append(set(comp))

    result, cohesion = {}, {}
    for i, comp in enumerate(parts):
        comp = list(comp)
        result[i] = comp
        n = len(comp)
        if n < 2:
            cohesion[i] = 0.0
            continue
        cset = set(comp)
        internal = sum(len(adj[x] & cset) for x in comp) / 2
        possible = n * (n - 1) / 2
        cohesion[i] = round(internal / possible, 3) if possible else 0.0
    return result, cohesion


def knowledge_gaps(notes, adj, comm, cohesion):
    """Isolated notes (degree<=1), sparse communities (cohesion<0.15, >=3),
    and bridge notes (linking 3+ communities)."""
    node_comm = {p: cid for cid, members in comm.items() for p in members}
    isolated = sorted(p for p in notes if len(adj[p]) <= 1)
    sparse = sorted(
        (cid for cid, c in cohesion.items() if c < 0.15 and len(comm[cid]) >= 3),
        key=lambda cid: cohesion[cid],
    )
    # Bridge notes connect many distinct clusters. With few clusters this is
    # only informational, so require touching a majority of clusters (min 3),
    # then rank by count and let the caller cap the list.
    n_clusters = sum(1 for m in comm.values() if len(m) >= 2)
    min_touch = max(3, (n_clusters + 1) // 2)
    bridges = []
    for p in notes:
        touched = {node_comm[n] for n in adj[p] if n in node_comm}
        if len(touched) >= min_touch:
            bridges.append((p, len(touched)))
    bridges.sort(key=lambda x: -x[1])
    return isolated, sparse, bridges
