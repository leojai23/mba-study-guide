# -*- coding: utf-8 -*-
"""Scans every HTML page in the site and builds search-index.json at the repo root."""
import os, re, json, glob

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

SUBJECT_LABELS = {
    "Strategic-Management": "Strategic Management",
    "Banking-and-Financial-Services": "Banking and Financial Services",
}

def extract_title(html):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        raw = m.group(1)
        raw = re.sub(r'<span[^>]*>.*?</span>', '', raw, flags=re.DOTALL)
        raw = re.sub(r'<[^>]+>', '', raw).strip()
        raw = raw.replace('&amp;', '&').replace('&mdash;', '—').replace('&rsquo;', '’')
        if raw:
            return raw
    m = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    if m:
        return m.group(1).split('|')[0].strip()
    return None

def main():
    entries = []
    for path in sorted(glob.glob("**/*.html", recursive=True)):
        posix_path = path.replace(os.sep, "/")
        if posix_path.startswith("build-scripts/"):
            continue
        html = open(path, encoding="utf-8", errors="replace").read()
        title = extract_title(html)
        if not title:
            continue
        top = posix_path.split("/")[0]
        subject = SUBJECT_LABELS.get(top, "Home")
        entries.append({"t": title, "u": posix_path, "s": subject})

    with open("search-index.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    print(f"Wrote search-index.json with {len(entries)} entries")

if __name__ == "__main__":
    main()
