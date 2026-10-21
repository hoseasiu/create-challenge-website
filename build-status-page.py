#!/usr/bin/env python3
"""Render website-update-status.md as a readable website-update-status.html.

The markdown file stays the source of truth (edited per CLAUDE.md's
Local-to-Live Sync Workflow); re-run this script after editing it:

    python build-status-page.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "website-update-status.md"
OUT = ROOT / "website-update-status.html"

STATUS_CLASS = {"Synced": "ok", "Needs sync": "stale", "Unknown": "unknown"}


def inline(text):
    """Minimal markdown inline renderer (code, links, bold, italic, strike)."""
    codes = []

    def stash(m):
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)

    def link(m):
        label, url = m.group(1), m.group(2)
        ext = ' target="_blank" rel="noreferrer noopener"' if url.startswith("http") else ""
        return f'<a href="{url}"{ext}>{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"~~(.+?)~~", r"<s>\1</s>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def plain(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[`*~]", "", text)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def status_badge(cell):
    label = re.sub(r"^[^\w~]+", "", cell).strip()
    cls = STATUS_CLASS.get(label, "none")
    return f'<span class="badge badge--{cls}">{inline(cell)}</span>', cls


def latest_note(notes):
    plain_text = plain(notes)
    first = re.split(r"\s\*\*|\s(?=\d{4}-\d\d-\d\d,)", plain_text.strip(), maxsplit=1)[0]
    first = first.strip()
    return first if len(first) <= 200 else first[:197].rsplit(" ", 1)[0] + "…"


def render_table(rows, kind):
    header, body = rows[0], rows[2:]
    out = []
    if kind in ("main", "drafts"):
        out.append('<div class="rows">')
        for r in map(split_row, body):
            if len(r) == 4:  # drafts table: status is the first thing in the Notes cell
                file_, url, edit, notes = r
                m = re.match(r"(✅|🔄|❓)\s*\**(Synced|Needs sync|Unknown)\**[^—]*—?\s*", notes)
                status = f"{m.group(1)} {m.group(2)}" if m else "—"
                notes = notes[m.end():] if m else notes
                synced = "—"
            elif len(r) == 6:
                file_, url, edit, status, synced, notes = r
            else:
                continue
            badge, cls = status_badge(status)
            out.append(
                f'<article class="row" data-status="{cls}">'
                f'<div class="row__head"><h3 class="row__file">{inline(file_)}</h3>{badge}</div>'
                f'<p class="row__url">{inline(url)}</p>'
                f'<dl class="row__meta"><div><dt>Last local edit</dt><dd>{inline(edit)}</dd></div>'
                f'<div><dt>Last synced</dt><dd>{inline(synced)}</dd></div></dl>'
                f'<details class="row__notes"><summary><span class="row__latest">{html.escape(latest_note(notes))}</span>'
                f'<span class="row__more">Full history</span></summary><p>{inline(notes)}</p></details>'
                f"</article>"
            )
        out.append("</div>")
    else:
        heads = split_row(header)
        out.append('<div class="table-wrap"><table><thead><tr>')
        out.extend(f"<th>{html.escape(h)}</th>" for h in heads)
        out.append("</tr></thead><tbody>")
        for r in map(split_row, body):
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        out.append("</tbody></table></div>")
    return "\n".join(out)


def render_blocks(lines, table_kind=None):
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            out.append(f"<h{level}>{inline(line[level:].strip())}</h{level}>")
            i += 1
        elif line.strip() == "---":
            out.append("<hr>")
            i += 1
        elif line.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            out.append(render_table(lines[i:j], table_kind))
            i = j
        elif line.startswith("- "):
            j = i
            while j < len(lines) and lines[j].startswith("- "):
                j += 1
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lines[i:j]) + "</ul>")
            i = j
        else:
            j = i
            while j < len(lines) and lines[j].strip() and not re.match(r"(\||- |#|---$)", lines[j]):
                j += 1
            out.append(f"<p>{inline(' '.join(l.strip() for l in lines[i:j]))}</p>")
            i = j
    return "\n".join(out)


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()

    # Split into top-level sections at "## " headings (+ the trailing log after "---").
    sections, cur = [], ("intro", [])
    for ln in lines:
        if ln.startswith("## "):
            sections.append(cur)
            cur = (ln[3:].strip(), [])
        else:
            cur[1].append(ln)
    sections.append(cur)

    counts = {"ok": 0, "stale": 0, "unknown": 0}
    for ln in lines:
        m = re.match(r"\| \[[^\]]+\]\([^)]*\) \| .* \| .* \| (✅ Synced|🔄 Needs sync|❓ Unknown) \|", ln)
        if m:
            counts[STATUS_CLASS[re.sub(r"^\S+\s", "", m.group(1))]] += 1

    for ln in lines:
        m = re.match(r"\| \[[^\]]+\]\([^)]*\) \| .* \| .* \| (✅|🔄|❓)\s*\**(Synced|Needs sync|Unknown)", ln)
        if m and not re.search(r"\| (✅|🔄|❓) (Synced|Needs sync|Unknown) \| \S+ \|", ln):
            counts[STATUS_CLASS[m.group(2)]] += 1

    body = []
    for title, sec in sections:
        if title == "intro":
            # drop H1 (rendered in the header) and render the rest
            sec = [l for l in sec if not l.startswith("# ")]
            body.append(f'<section class="card prose">{render_blocks(sec)}</section>')
        elif title == "Pages with a local HTML embed":
            body.append(
                '<section id="pages"><h2>Pages with a local HTML embed</h2>'
                '<div class="filters" role="group" aria-label="Filter by sync status">'
                '<button type="button" data-filter="all" aria-pressed="true">All</button>'
                '<button type="button" data-filter="stale" aria-pressed="false">🔄 Needs sync</button>'
                '<button type="button" data-filter="unknown" aria-pressed="false">❓ Unknown</button>'
                '<button type="button" data-filter="ok" aria-pressed="false">✅ Synced</button></div>'
                + render_blocks(sec, "main")
                + "</section>"
            )
        elif title.startswith("Local drafts"):
            intro = [l for l in sec if not l.startswith("|")]
            tbl = [l for l in sec if l.startswith("|")]
            body.append(
                f'<section class="card prose"><h2>{html.escape(title)}</h2>{render_blocks(intro, "plain")}</section>'
                f'<section>{render_blocks(tbl, "drafts")}</section>'
            )
        elif title.startswith("Not yet converted"):
            cut = sec.index("---")
            body.append(f'<section class="card prose"><h2>{html.escape(title)}</h2>{render_blocks(sec[:cut], "plain")}</section>')
            body.append(
                '<details class="card prose log"><summary>Change log</summary>'
                + render_blocks(sec[cut + 1:], "plain") + "</details>"
            )
        elif title == "How to read the table":
            body.append(f'<section class="card prose"><h2>{html.escape(title)}</h2>{render_blocks(sec, "plain")}</section>')
        else:
            body.append(f'<section class="card prose"><h2>{html.escape(title)}</h2>{render_blocks(sec, "plain")}</section>')

    # The change log is the tail after the "---" that follows the backlog list.
    page = TEMPLATE.replace("{{BODY}}", "\n".join(body)).replace(
        "{{COUNTS}}",
        f'<div class="stat stat--stale"><b>{counts["stale"]}</b> 🔄 Needs sync</div>'
        f'<div class="stat stat--unknown"><b>{counts["unknown"]}</b> ❓ Unknown</div>'
        f'<div class="stat stat--ok"><b>{counts["ok"]}</b> ✅ Synced</div>',
    )
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT.name}: {counts}")


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Website Update Status</title>
<style>
:root {
  --yellow: #ffce10; --mit-dark: #1a1a1a; --mit-gray: #555; --mit-light: #f5f5f5;
  --border: #e0e0e0; --white: #ffffff; --link: #7a5500;
  --ok-bg: #e3f4e6; --ok-fg: #14532d; --stale-bg: #fff1c2; --stale-fg: #6b4a00;
  --unk-bg: #e9e9ee; --unk-fg: #333;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Arial, sans-serif; font-size: 1rem; line-height: 1.65;
  color: var(--mit-dark); background: var(--mit-light); }
a { color: var(--link); }
a:focus-visible, button:focus-visible, summary:focus-visible { outline: 3px solid var(--mit-dark); outline-offset: 2px; }
header { background: var(--mit-dark); border-bottom: 4px solid var(--yellow); color: var(--white); padding: 36px 24px; }
header > div, main { max-width: 960px; margin: 0 auto; }
header h1 { margin: 0 0 6px; font-size: clamp(1.4rem, 3.5vw, 2rem); font-weight: 800; line-height: 1.2; }
header p { margin: 0; color: rgba(255,255,255,0.8); }
.stats { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }
.stat { background: var(--white); color: var(--mit-dark); border-radius: 8px; padding: 8px 16px; border-left: 4px solid; }
.stat b { font-size: 1.4rem; margin-right: 4px; }
.stat--stale { border-color: var(--yellow); } .stat--ok { border-color: #2e7d32; } .stat--unknown { border-color: #888; }
main { padding: 32px 24px 60px; }
section { margin-bottom: 32px; }
h2 { font-size: clamp(1.3rem, 3vw, 1.6rem); font-weight: 800; line-height: 1.2; margin: 0 0 16px; }
h3 { margin: 0; font-size: 1rem; }
.card { background: var(--white); border: 1px solid var(--border); border-radius: 8px; padding: 24px; }
.prose p, .prose ul, .prose li { color: var(--mit-gray); }
.prose p:first-child, .prose h2 + p { margin-top: 0; }
.prose ul { padding-left: 1.3em; }
.prose h2:not(:first-child) { margin-top: 1.4em; }
code { background: var(--mit-light); border: 1px solid var(--border); border-radius: 4px; padding: 0 4px; font-size: 0.875em; word-break: break-word; }
.table-wrap { overflow-x: auto; margin: 12px 0; }
table { border-collapse: collapse; width: 100%; font-size: 0.9rem; }
th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
th { background: var(--mit-light); }
.filters { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.filters button { font: inherit; font-size: 0.9rem; font-weight: 600; padding: 6px 14px; border-radius: 999px;
  border: 2px solid var(--mit-dark); background: var(--white); color: var(--mit-dark); cursor: pointer; }
.filters button[aria-pressed="true"] { background: var(--mit-dark); color: var(--yellow); }
.rows { display: grid; gap: 12px; }
.row { background: var(--white); border: 1px solid var(--border); border-left: 4px solid var(--border); border-radius: 0 8px 8px 0; padding: 16px 20px; }
.row[data-status="stale"] { border-left-color: var(--yellow); }
.row[data-status="ok"] { border-left-color: #2e7d32; }
.row__head { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
.row__url { margin: 2px 0 8px; font-size: 0.875rem; color: var(--mit-gray); word-break: break-word; }
.row__meta { display: flex; gap: 28px; margin: 0 0 8px; font-size: 0.875rem; }
.row__meta dt { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--link); }
.row__meta dd { margin: 0; }
.badge { display: inline-block; font-size: 0.8rem; font-weight: 700; padding: 2px 10px; border-radius: 999px; white-space: nowrap; }
.badge--ok { background: var(--ok-bg); color: var(--ok-fg); } .badge--stale { background: var(--stale-bg); color: var(--stale-fg); }
.badge--unknown, .badge--none { background: var(--unk-bg); color: var(--unk-fg); }
.row__notes summary { cursor: pointer; list-style: none; display: flex; justify-content: space-between; gap: 16px; font-size: 0.875rem; color: var(--mit-gray); }
.row__notes summary::-webkit-details-marker { display: none; }
.row__more { flex: none; color: var(--link); font-weight: 600; }
.row__more::after { content: " ▾"; } .row__notes[open] .row__more::after { content: " ▴"; }
.row__notes[open] .row__latest { display: none; }
.row__notes p { font-size: 0.875rem; color: var(--mit-gray); margin: 8px 0 0; }
.log summary { cursor: pointer; font-weight: 800; font-size: 1.2rem; color: var(--mit-dark); }
[hidden] { display: none !important; }
@media (max-width: 600px) { .row__meta { flex-direction: column; gap: 4px; } }
</style>
</head>
<body>
<header><div>
<h1>Website Update Status</h1>
<p>Which local HTML embeds are in sync with the live Google Site.</p>
<div class="stats">{{COUNTS}}</div>
</div></header>
<main>
{{BODY}}
</main>
<script>
document.querySelectorAll('.filters button').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var f = btn.dataset.filter;
    document.querySelectorAll('.filters button').forEach(function (b) { b.setAttribute('aria-pressed', b === btn); });
    document.querySelectorAll('.row').forEach(function (r) { r.hidden = f !== 'all' && r.dataset.status !== f; });
  });
});
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
