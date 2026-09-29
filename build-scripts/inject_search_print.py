# -*- coding: utf-8 -*-
"""Injects a shared search + print floating-button UI into every HTML page.
Idempotent: re-running just replaces the previously-injected block.
Run this LAST, after any content rebuild, then commit."""
import os, re, glob

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

MARKER_START = "<!-- MBA-SG:FEATURES:START -->"
MARKER_END = "<!-- MBA-SG:FEATURES:END -->"

CSS = """
<style>
.mba-fab{position:fixed;bottom:22px;width:46px;height:46px;border-radius:50%;background:var(--accent,#0f6e6e);color:#fff;border:none;box-shadow:0 2px 8px rgba(0,0,0,.25);cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:9998;transition:transform .15s}
.mba-fab:hover{transform:scale(1.08)}
.mba-fab svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:2}
#mbaSearchBtn{right:22px}
#mbaPrintBtn{right:78px}
.mba-overlay{position:fixed;inset:0;background:rgba(15,20,25,.55);z-index:9999;display:none;align-items:flex-start;justify-content:center;padding:8vh 16px}
.mba-overlay.open{display:flex}
.mba-search-box{background:var(--bg,#fff);border-radius:12px;max-width:640px;width:100%;max-height:72vh;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 12px 40px rgba(0,0,0,.3)}
.mba-search-input-row{padding:14px 16px;border-bottom:1px solid var(--border,#ddd)}
.mba-search-input-row input{width:100%;font-size:1.05rem;padding:10px 12px;border:1px solid var(--border,#ddd);border-radius:8px;outline:none;box-sizing:border-box}
.mba-search-results{overflow-y:auto;padding:8px}
.mba-result{display:block;padding:10px 14px;border-radius:8px;color:var(--ink,#222);text-decoration:none}
.mba-result:hover,.mba-result.active{background:var(--accent-light,#eef)}
.mba-result .rt{font-weight:600}
.mba-result .rs{font-size:.78rem;color:var(--ink-soft,#666);margin-top:2px}
.mba-empty{padding:20px;text-align:center;color:var(--ink-soft,#666);font-size:.9rem}
@media print{
  .mba-fab,.mba-overlay{display:none !important}
  .sidebar,.breadcrumb,.page-nav{display:none !important}
  .content{padding:0 !important}
  .layout{display:block !important}
  body{background:#fff !important}
}
</style>
"""

HTML_SNIPPET = """
<button id="mbaPrintBtn" class="mba-fab" title="Print this page" onclick="window.print()">
  <svg viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
</button>
<button id="mbaSearchBtn" class="mba-fab" title="Search (press /)">
  <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
</button>
<div id="mbaOverlay" class="mba-overlay">
  <div class="mba-search-box">
    <div class="mba-search-input-row"><input id="mbaSearchInput" type="text" placeholder="Search all topics..." autocomplete="off"></div>
    <div id="mbaResults" class="mba-search-results"></div>
  </div>
</div>
"""

def make_script(root_prefix):
    return f"""
<script>
(function(){{
  var ROOT = "{root_prefix}";
  var btn = document.getElementById('mbaSearchBtn');
  var overlay = document.getElementById('mbaOverlay');
  var input = document.getElementById('mbaSearchInput');
  var results = document.getElementById('mbaResults');
  var IDX = null, activeIdx = -1;

  function ensureIndex(cb) {{
    if (IDX) return cb();
    fetch(ROOT + 'search-index.json').then(function(r){{return r.json();}}).then(function(data){{
      IDX = data; cb();
    }}).catch(function(){{ IDX = []; cb(); }});
  }}

  function render(query) {{
    var q = query.trim().toLowerCase();
    activeIdx = -1;
    if (!q) {{ results.innerHTML = '<div class="mba-empty">Type to search across all subjects and topics.</div>'; return; }}
    var matches = IDX.filter(function(e){{ return e.t.toLowerCase().indexOf(q) !== -1; }}).slice(0, 30);
    if (!matches.length) {{ results.innerHTML = '<div class="mba-empty">No matches.</div>'; return; }}
    results.innerHTML = matches.map(function(e){{
      return '<a class="mba-result" href="' + ROOT + e.u + '"><div class="rt">' + e.t + '</div><div class="rs">' + e.s + '</div></a>';
    }}).join('');
  }}

  function open() {{
    overlay.classList.add('open');
    ensureIndex(function(){{ render(''); input.value=''; input.focus(); }});
  }}
  function close() {{ overlay.classList.remove('open'); }}

  btn.addEventListener('click', open);
  overlay.addEventListener('click', function(e){{ if (e.target === overlay) close(); }});
  document.addEventListener('keydown', function(e){{
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && !overlay.classList.contains('open')) {{
      e.preventDefault(); open();
    }} else if (e.key === 'Escape' && overlay.classList.contains('open')) {{
      close();
    }} else if (overlay.classList.contains('open')) {{
      var items = results.querySelectorAll('.mba-result');
      if (e.key === 'ArrowDown') {{ e.preventDefault(); activeIdx = Math.min(activeIdx+1, items.length-1); items.forEach(function(it,i){{it.classList.toggle('active', i===activeIdx);}}); if(items[activeIdx]) items[activeIdx].scrollIntoView({{block:'nearest'}}); }}
      else if (e.key === 'ArrowUp') {{ e.preventDefault(); activeIdx = Math.max(activeIdx-1, 0); items.forEach(function(it,i){{it.classList.toggle('active', i===activeIdx);}}); if(items[activeIdx]) items[activeIdx].scrollIntoView({{block:'nearest'}}); }}
      else if (e.key === 'Enter' && activeIdx >= 0 && items[activeIdx]) {{ window.location.href = items[activeIdx].href; }}
    }}
  }});
  input.addEventListener('input', function(){{ render(input.value); }});
}})();
</script>
"""

def process(path):
    html = open(path, encoding="utf-8").read()
    # strip previous injection if present
    html = re.sub(re.escape(MARKER_START) + r'.*?' + re.escape(MARKER_END), '', html, flags=re.DOTALL)

    depth = path.count(os.sep)
    root_prefix = "../" * depth

    block = MARKER_START + CSS + HTML_SNIPPET + make_script(root_prefix) + MARKER_END

    if "</body>" in html:
        html = html.replace("</body>", block + "\n</body>", 1)
    else:
        html = html + block

    open(path, "w", encoding="utf-8").write(html)

def main():
    count = 0
    for path in glob.glob("**/*.html", recursive=True):
        if path.startswith("build-scripts" + os.sep):
            continue
        process(path)
        count += 1
    print(f"Injected search+print into {count} pages")

if __name__ == "__main__":
    main()
