# -*- coding: utf-8 -*-
import os

BASE = r"G:\Leo-Workspace\MBA-Study-Guide\Strategic-Management\units\unit1"

CSS = """
:root{--accent:#0f6e6e;--accent-dark:#0a4f4f;--accent-light:#e4f4f2;--ink:#1f2937;--ink-soft:#4b5563;--bg:#fff;--bg-soft:#f7fafa;--border:#d9e6e4;--card-shadow:0 1px 3px rgba(15,110,110,.12);--radius:10px;--warn-bg:#fff8e6;--warn-border:#f0d58c}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg-soft);color:var(--ink);line-height:1.6}
a{color:var(--accent-dark);text-decoration:none}a:hover{text-decoration:underline}
.layout{display:flex;max-width:1200px;margin:0 auto;min-height:100vh}
.sidebar{width:260px;flex-shrink:0;background:var(--bg);border-right:1px solid var(--border);padding:20px 16px}
.sidebar h3{font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-soft);margin:18px 0 8px}
.sidebar h3:first-child{margin-top:0}
.sidebar ol,.sidebar ul{list-style:none;margin:0 0 6px;padding:0}
.sidebar li{margin:2px 0}
.sidebar a{display:block;padding:7px 10px;border-radius:8px;color:var(--ink);font-size:.92rem}
.sidebar a:hover{background:var(--accent-light);text-decoration:none}
.sidebar a.active{background:var(--accent);color:#fff;font-weight:600}
.sidebar .home-link{display:inline-flex;align-items:center;gap:8px;font-weight:700;color:var(--accent-dark);margin-bottom:14px;font-size:1.02rem}
.content{flex:1;padding:28px 36px 60px;min-width:0}
.breadcrumb{font-size:.82rem;color:var(--ink-soft);margin-bottom:10px}
.breadcrumb a{color:var(--ink-soft)}
h1{font-size:1.7rem;color:var(--accent-dark);margin:0 0 6px}
h1 .unit-tag{display:inline-block;font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;background:var(--accent);color:#fff;padding:3px 9px;border-radius:999px;vertical-align:middle;margin-right:10px}
.subtitle{color:var(--ink-soft);margin-bottom:26px}
h2{font-size:1.22rem;color:var(--accent-dark);margin:34px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--accent-light)}
h3{font-size:1.02rem;color:var(--ink);margin:20px 0 8px}
.card{background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--card-shadow);padding:18px 20px;margin:14px 0}
.callout{background:var(--accent-light);border-left:4px solid var(--accent);border-radius:8px;padding:12px 16px;margin:16px 0;font-size:.94rem}
.callout.source{font-style:italic;color:var(--ink-soft)}
dl.term-list{margin:0}dl.term-list dt{font-weight:700;color:var(--accent-dark);margin-top:14px}
dl.term-list dd{margin:3px 0 0 0;color:var(--ink-soft)}
ol.q-list{padding-left:22px}ol.q-list li{margin:10px 0}
details.answer-reveal{margin-top:6px}
details.answer-reveal summary{cursor:pointer;color:var(--accent-dark);font-size:.86rem;font-weight:600;user-select:none}
details.answer-reveal .answer-box{background:var(--accent-light);border-radius:8px;padding:10px 14px;margin-top:6px;font-size:.92rem}
table.compare{width:100%;border-collapse:collapse;margin:14px 0;font-size:.9rem}
table.compare th,table.compare td{border:1px solid var(--border);padding:8px 10px;text-align:left;vertical-align:top}
table.compare th{background:var(--accent-light);color:var(--accent-dark)}
.topic-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin:18px 0}
.topic-card{display:block;background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--card-shadow);padding:16px 18px;color:var(--ink)}
.topic-card:hover{border-color:var(--accent);text-decoration:none}
.topic-card .n{font-size:.72rem;color:var(--accent);font-weight:700;text-transform:uppercase}
.topic-card .t{font-size:1.02rem;font-weight:600;margin-top:4px}
.page-nav{display:flex;justify-content:space-between;margin-top:40px;padding-top:16px;border-top:1px solid var(--border);font-size:.9rem}
@media (max-width:800px){.layout{flex-direction:column}.sidebar{width:auto;border-right:none;border-bottom:1px solid var(--border)}.content{padding:20px}}
"""

TOPICS = [
    ("topic1-strategy-and-strategic-management.html", "Strategy &amp; Strategic Management"),
    ("topic2-stakeholders.html", "Stakeholders in Business"),
    ("topic3-intent-vision-mission.html", "Strategic Intent, Vision &amp; Mission"),
    ("topic4-purpose-and-business-definition.html", "Purpose &amp; Business Definition"),
    ("topic5-goals-and-objectives.html", "Goals &amp; Objectives"),
    ("topic6-governance-and-csr.html", "Corporate Governance &amp; CSR"),
]

def sidebar(active_file):
    items = []
    for i, (fname, title) in enumerate(TOPICS, start=1):
        cls = ' class="active"' if fname == active_file else ''
        items.append(f'<li><a{cls} href="{fname}">{i}. {title}</a></li>')
    return f"""
    <a class="home-link" href="../../index.html">&#8962; MBA Study Guide</a>
    <h3>Strategic Management</h3>
    <ul><li><a href="../../index.html">Course Home</a></li></ul>
    <h3>Unit 1 &middot; Strategy &amp; Process</h3>
    <ol>
      {''.join(items)}
    </ol>
    """

def page(active_file, idx, title, overview, notes, terms, examprep, questions, prev_link, next_link):
    terms_html = "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in terms)
    examprep_html = "".join(f"<li>{b}</li>" for b in examprep)
    q_html = ""
    for q, a in questions:
        q_html += f'<li>{q}<details class="answer-reveal"><summary>Show model answer</summary><div class="answer-box">{a}</div></details></li>'
    nav = '<div class="page-nav">'
    nav += f'<a href="{prev_link[0]}">&larr; {prev_link[1]}</a>' if prev_link else '<span></span>'
    nav += f'<a href="{next_link[0]}">{next_link[1]} &rarr;</a>' if next_link else '<span></span>'
    nav += '</div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} | MBA Study Guide</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">{sidebar(active_file)}</nav>
  <main class="content">
    <div class="breadcrumb"><a href="../../index.html">Strategic Management</a> &rsaquo; <a href="index.html">Unit 1</a> &rsaquo; Topic {idx}</div>
    <h1><span class="unit-tag">Unit 1</span>{title}</h1>
    <p class="subtitle">Book: <em>Strategic Management</em> (BA4301, Anna University MBA Sem III) &mdash; Dr. G. Pandi Selvi &amp; Dr. M. Hemalatha, Thakur Publication</p>

    <h2>1. Overview</h2>
    <div class="card"><p>{overview}</p></div>

    <h2>2. Detailed Notes</h2>
    {notes}

    <h2>3. Key Terms</h2>
    <dl class="term-list">{terms_html}</dl>

    <h2>4. Exam-Prep Summary</h2>
    <div class="callout"><ul>{examprep_html}</ul></div>

    <h2>5. Practice Questions</h2>
    <ol class="q-list">{q_html}</ol>

    <p class="callout source">Grounded in Unit 1 ("Strategy and Process") of the course textbook &mdash; Strategic Management (BA4301), Dr. G. Pandi Selvi &amp; Dr. M. Hemalatha, Thakur Publication.</p>

    {nav}
  </main>
</div>
</body>
</html>
"""

def write(fname, content):
    path = os.path.join(BASE, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)
