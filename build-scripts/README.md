# Build scripts

Static-site generators for the Strategic Management subject's topic pages, using plain Python (no dependencies).

- `build_unit1.py` — shared page shell: inline CSS, sidebar nav generator, `page()` template function, `write()` helper. Import this from a per-unit content script.
- `build_unit1_content.py` — content data for Unit 1's topics 2–6 (topic 1 was hand-written directly as the template reference; the rest are generated). Run with `python build_unit1_content.py` from this folder.

**Pattern for future units:** copy `build_unit1.py`'s shell/CSS/`page()`/`write()` functions (update `BASE` and the `TOPICS` list for the new unit), then write a `build_unitN_content.py` with each topic's `overview`/`notes` (raw HTML string)/`terms` (list of tuples)/`examprep` (list of bullet strings)/`questions` (list of question/answer tuples), calling `B.write(...)` per topic.

Run from this directory: `python build_unitN_content.py`.
