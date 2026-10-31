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
        f'<td><a href="{html.escape(quote(rel))}">{html.escape(rel)}</a></td>'
        f"<td>{html.escape(kind(rel))}</td>"
        f"<td>{p.stat().st_size / 1024:.1f} КБ</td>"
        '<td><input class="u" readonly aria-label="Прямая ссылка"> '
        '<button type="button">Копировать</button></td>'
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
  :root {{ color-scheme: light dark; }}
  body {{ font: 16px/1.5 system-ui, sans-serif; margin: 0 auto; padding: 16px; max-width: 60rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid #8884; vertical-align: top; }}
  .u {{ width: min(28rem, 100%); font: inherit; }}
</style>
</head>
<body>
<h1>Файлы</h1>
<p>В приложении вставляйте <b>прямую ссылку</b> на файл (колонка справа), а не адрес этой страницы.</p>
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
