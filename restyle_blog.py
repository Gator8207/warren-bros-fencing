"""
Warren Bros — bold restyle for the 9 blog pages (blog/index + 8 posts).

Reuses the inner-page bold CSS from restyle_inner.py and adds blog-specific rules
(.post-card, .breadcrumb, table.cost, .related/.answer-band callouts, .note).
Swaps each page's <style> block + adds fonts; markup/content/SEO/schema untouched.
Runs on the served ./site folder.

Run:  python restyle_blog.py
"""
import os
import re
from restyle_inner import CSS as BASE_CSS, FONT_LINK, SITE

BLOG_PAGES = [
    "blog/index.html",
    "blog/privacy-fence-cost-wichita.html",
    "blog/fence-permit-wichita.html",
    "blog/cedar-fence-lifespan-kansas.html",
    "blog/fence-repair-cost-wichita.html",
    "blog/fence-replacement-cost-wichita.html",
    "blog/fence-installation-timeline-wichita.html",
    "blog/best-time-to-install-fence-kansas.html",
    "blog/cedar-vs-treated-pine-fence.html",
]

BLOG_CSS = BASE_CSS + """
  /* ===== Blog ===== */
  .breadcrumb { font-family: var(--sans); font-size: .9rem; color: var(--muted); padding-top: 28px; }
  .breadcrumb a { color: var(--muted); } .breadcrumb a:hover { color: var(--orange); }
  .post-list { display: grid; gap: 22px; }
  .post-card { background:#fff; border:1px solid var(--line); border-left:4px solid var(--orange); border-radius:var(--radius); padding:28px 30px; box-shadow:var(--shadow-sm); transition:transform .3s var(--ease),box-shadow .3s var(--ease); }
  .post-card:hover { transform:translateY(-5px); box-shadow:var(--shadow); }
  .post-card h3 { font-size:1.45rem; color:var(--ink); margin-bottom:10px; line-height:1.25; }
  .post-card h3 a { color:var(--ink); } .post-card h3 a:hover { color:var(--orange); text-decoration:none; }
  .post-card p { margin-bottom:14px; color:var(--muted); }
  .post-card .read { font-family:var(--sans); font-weight:700; color:var(--orange); }
  table.cost { width:100%; border-collapse:collapse; margin:24px 0; background:#fff; border:1px solid var(--line); border-radius:var(--radius); overflow:hidden; font-size:1rem; }
  table.cost th { background:var(--ink); color:#fff; font-family:var(--sans); font-weight:700; text-align:left; padding:14px 18px; }
  table.cost td { padding:13px 18px; border-top:1px solid var(--line); color:var(--text); }
  table.cost tr:nth-child(even) td { background:var(--cream); }
  .related, .answer-band { background:var(--orange-soft); border:1px solid rgba(232,95,42,.25); border-left:4px solid var(--orange); border-radius:var(--radius); padding:24px 28px; margin:26px 0; font-size:1.05rem; line-height:1.6; }
  .related strong, .answer-band strong { color:var(--ink); }
  .related a, .answer-band a { color:var(--orange); font-weight:700; }
  .note { background:var(--cream-2); border:1px solid var(--line); border-radius:var(--radius); padding:20px 24px; margin:22px 0; color:var(--text); font-size:.98rem; }
"""

def main():
    for rel in BLOG_PAGES:
        p = os.path.join(SITE, rel)
        if not os.path.exists(p):
            print("MISSING:", rel); continue
        html = open(p, encoding="utf-8").read()
        new_html, n = re.subn(r"<style>.*?</style>", lambda m: "<style>\n" + BLOG_CSS + "\n</style>",
                              html, count=1, flags=re.S)
        if n == 0:
            print("NO <style> FOUND:", rel); continue
        if "fonts.googleapis.com" not in new_html:
            new_html = new_html.replace("</title>", "</title>\n" + FONT_LINK, 1)
        open(p, "w", encoding="utf-8").write(new_html)
        print("restyled:", rel)

if __name__ == "__main__":
    main()
