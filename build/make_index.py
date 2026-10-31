#!/usr/bin/env python3
"""Build a minimal index.html listing every file in a folder (default: public)."""
import html
import sys
from pathlib import Path
from urllib.parse import quote

root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")

# Какая колонка «куда вставлять» соответствует расширению
KINDS = [
    (".m3u8", "Плейлист каналов (M3U)"),
    (".m3u", "Плейлист каналов (M3U)"),
    (".xml.gz", "Программа передач (XMLTV/EPG)"),
    (".xml.xz", "Программа передач (XMLTV/EPG)"),
    (".xml", "Программа передач (XMLTV/EPG)"),
    (".xspf", "Плейлист (XSPF, для VLC)"),
]


def kind(name):
    low = name.lower()
    for ext, label in KINDS:
        if low.endswith(ext):
            return label
    return "Файл"


files = sorted(
    p for p in root.rglob("*") if p.is_file() and p.relative_to(root).as_posix() != "index.html"
)

rows = []
for p in files:
    rel = p.relative_to(root).as_posix()
    rows.append(
        "<tr>"
        f'<td class="name"><a href="{html.escape(quote(rel))}">{html.escape(rel)}</a></td>'
        f'<td class="type">{html.escape(kind(rel))}</td>'
        f'<td class="size">{p.stat().st_size / 1024:.1f} КБ</td>'
        '<td class="linkcell"><div class="copy">'
        '<input class="u" readonly aria-label="Прямая ссылка">'
        '<button type="button">Копировать</button>'
        '</div></td>'
        "</tr>"
    )

if not rows:
    rows.append('<tr><td colspan="4">Файлов пока нет.</td></tr>')

page = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Файлы</title>
<style>
  :root {{ color-scheme: light dark; --accent: #3b82f6; --muted: #8888; --line: #8884; }}
  * {{ box-sizing: border-box; }}
  body {{ font: 16px/1.5 system-ui, sans-serif; margin: 0 auto; padding: 20px; max-width: 64rem; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 .25rem; }}
  .hint {{ color: var(--muted); margin: 0 0 1.5rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th {{ font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); text-align: left; padding: 8px; }}
  td {{ padding: 12px 8px; border-bottom: 1px solid var(--line); vertical-align: middle; }}
  tr:last-child td {{ border-bottom: 0; }}
  .name {{ font-weight: 550; word-break: break-all; }}
  .name a {{ color: inherit; text-decoration: none; }}
  .name a:hover {{ color: var(--accent); text-decoration: underline; }}
  .type {{ color: var(--muted); font-size: .9rem; }}
  .size {{ color: var(--muted); font-size: .85rem; white-space: nowrap; }}
  .copy {{ display: flex; gap: 8px; max-width: 34rem; }}
  .u {{ flex: 1 1 auto; min-width: 0; font: .85rem/1.4 ui-monospace, SFMono-Regular, Menlo, monospace;
        padding: 9px 12px; border: 1px solid var(--line); border-radius: 10px; color: inherit;
        background: transparent; text-overflow: ellipsis; }}
  button {{ flex: 0 0 auto; font: inherit; font-size: .9rem; padding: 9px 16px; border: 0;
            border-radius: 10px; background: var(--accent); color: #fff; cursor: pointer; white-space: nowrap; }}
  button:hover {{ filter: brightness(1.08); }}
  button:active {{ transform: translateY(1px); }}
  :focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
  @media (max-width: 720px) {{
    body {{ padding: 14px; }}
    thead {{ display: none; }}
    table, tbody, tr, td {{ display: block; }}
    tr {{ padding: 14px 0; border-bottom: 1px solid var(--line); }}
    td {{ border: 0; padding: 3px 0; }}
    .copy {{ max-width: none; flex-direction: column; }}
    .u {{ width: 100%; }}
    button {{ width: 100%; }}
  }}
</style>
</head>
<body>
<h1>Файлы</h1>
<p class="hint">В приложении вставляйте <b>прямую ссылку</b> на файл (колонка справа), а не адрес этой страницы.</p>
<table>
<thead><tr><th>Файл</th><th>Куда вставлять</th><th>Размер</th><th>Прямая ссылка</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
<script>
  document.querySelectorAll("tbody tr").forEach(function (tr) {{
    var a = tr.querySelector("a"), input = tr.querySelector("input"), btn = tr.querySelector("button");
    if (!a || !input) return;
    input.value = a.href;
    btn.addEventListener("click", function () {{
      input.select();
      var done = function () {{ btn.textContent = "Скопировано"; setTimeout(function () {{ btn.textContent = "Копировать"; }}, 1500); }};
      if (navigator.clipboard) {{ navigator.clipboard.writeText(input.value).then(done, function () {{ document.execCommand("copy"); done(); }}); }}
      else {{ document.execCommand("copy"); done(); }}
    }});
    input.addEventListener("focus", function () {{ input.select(); }});
  }});
</script>
</body>
</html>
"""

(root / "index.html").write_text(page, encoding="utf-8")
print(f"index.html: {len(files)} files")
