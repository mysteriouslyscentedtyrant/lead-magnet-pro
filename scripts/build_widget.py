#!/usr/bin/env python3
"""Builds frontend/widget.html (the snippet pasted into systeme.io) from frontend/page.template.html.

Usage:
  python3 scripts/build_widget.py <commit-sha>          # pinned release (jsDelivr + integrity hashes)
  python3 scripts/build_widget.py --local <out.html>    # local test page (relative files, mock answers, demo key lmp_demo)
  python3 scripts/build_widget.py --live <out.html>     # local page that talks to the REAL API (use your own access key)

The commit must contain the same frontend/app.css and frontend/app.js as your working copy,
otherwise the integrity hashes won't match and the browser will refuse to load the tool.
"""
import base64, hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FRONT = ROOT / "frontend"
REPO = "mysteriouslyscentedtyrant/lead-magnet-pro"


def sri(path):
    return "sha384-" + base64.b64encode(hashlib.sha384(path.read_bytes()).digest()).decode()


def version():
    m = re.search(r"var VERSION = '([0-9.]+)';", (FRONT / "app.js").read_text(encoding="utf-8"))
    return "v" + m.group(1)


def build(cdn, css_sri, js_sri):
    t = (FRONT / "page.template.html").read_text(encoding="utf-8")
    for k, v in {"{{CDN}}": cdn, "{{CSS_SRI}}": css_sri, "{{JS_SRI}}": js_sri, "{{VERSION}}": version()}.items():
        t = t.replace(k, v)
    assert "{{" not in t, "unfilled placeholder"
    return t


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] in ("--local", "--live"):
        html = build(str(FRONT), "", "").replace(' integrity=""', "").replace(' integrity="" crossorigin="anonymous"', "")
        html = re.sub(r'(app\.(?:css|js)") crossorigin="anonymous"', r'\1', html)
        # One self-contained file (CSS and JS inlined) so it can be opened from anywhere.
        css = (FRONT / "app.css").read_text(encoding="utf-8")
        js = (FRONT / "app.js").read_text(encoding="utf-8")
        assert "</script" not in js.lower() and "</style" not in css.lower()
        html = re.sub(r'<link rel="stylesheet" href="[^"]*app\.css"[^>]*>', lambda m: "<style>" + css + "</style>", html, count=1)
        html = re.sub(r'<script src="[^"]*app\.js"[^>]*>\s*</script>', lambda m: "<script>" + js + "</script>", html, count=1)
        assert "<style>" in html and 'src="' not in html.split("</section>")[-1].split("<script>")[0][-200:]
        if sys.argv[1] == "--local":
            html = html.replace(' data-pdf="server"', ' data-pdf="server" data-mock="1"')
        pathlib.Path(sys.argv[2]).write_text("<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'></head><body style='margin:0'>" + html + "</body></html>", encoding="utf-8")
        print("local page:", sys.argv[2])
    elif len(sys.argv) == 2 and re.fullmatch(r"[0-9a-f]{40}", sys.argv[1]):
        cdn = f"https://cdn.jsdelivr.net/gh/{REPO}@{sys.argv[1]}/frontend"
        (FRONT / "widget.html").write_text(build(cdn, sri(FRONT / "app.css"), sri(FRONT / "app.js")), encoding="utf-8")
        print("widget.html pinned to", sys.argv[1], version())
    else:
        sys.exit(__doc__)
