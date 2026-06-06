"""
Warren Bros Fencing — multi-page generator.

Generates: about.html, contact.html, services/index.html, and 4 service pages.
All share a header + footer + brand CSS. Each page has its own schema, content, and FAQ.

Run from project root:  python3 build_pages.py
"""
import os
import json

BASE = "/sessions/relaxed-gallant-johnson/mnt/Warren Bros Fencing/deploy"

# ─────────────────────────────────────────────────────────────────────────────
# Site-wide constants
# ─────────────────────────────────────────────────────────────────────────────

SITE = {
    "name": "Warren Bros Fencing",
    "phone": "(316) 285-9172",
    "phone_tel": "+13162859172",
    "email": "quote@warrenbrosfencing.com",
    "address_city": "Wichita",
    "address_state": "KS",
    "url": "https://www.warrenbrosfencing.com",
    "founded": "2021",
    "ga4": "G-086XBCVMTJ",
    "gbp_review_link": "https://maps.app.goo.gl/HaVjmXLtprgsLasB8",
    "facebook": "https://www.facebook.com/profile.php?id=61590232738773",
    "instagram": "https://www.instagram.com/warrenbrosfencing",
    "nextdoor": "https://nextdoor.com/pages/warren-bros-fencing-wichita-ks/",
    "baker_phone": "(316) 409-1144",
    "baker_url": "https://www.bakertreeserviceict.com",
}

# ─────────────────────────────────────────────────────────────────────────────
# Shared CSS (brand-matched to index.html)
# ─────────────────────────────────────────────────────────────────────────────

CSS = """
  :root {
    --orange: #e85f2a;
    --orange-dark: #c14d20;
    --green-dark: #3d4a5c;
    --green-darker: #2a3543;
    --cream: #faf2e0;
    --text: #2a2a2a;
    --muted: #6b6258;
    --wheat: var(--orange);
    --sky-dark: var(--green-darker);
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; overflow-x: clip; }
  body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: var(--text);
    background: var(--cream);
    line-height: 1.65;
    font-size: 18px;
    overflow-x: clip;
  }
  a { color: var(--sky-dark); text-decoration: none; }
  a:hover { text-decoration: underline; }
  .container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
  .container-narrow { max-width: 780px; margin: 0 auto; padding: 0 24px; }

  /* Header */
  header {
    background: #fff;
    border-bottom: 4px solid var(--orange);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }
  .nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 22px 40px; max-width: 1500px; margin: 0 auto;
    gap: 20px; flex-wrap: nowrap;
  }
  .logo { display: flex; align-items: center; gap: 14px; }
  .logo img { height: 56px; width: auto; }
  .logo-text small {
    display: block; letter-spacing: 0.15em; font-size: 0.75rem;
    color: var(--muted); text-transform: uppercase;
  }
  .nav-right { display: flex; align-items: center; gap: 28px; flex-wrap: nowrap; }
  .nav-phone {
    display: inline-flex; align-items: center; gap: 10px; font-weight: 800;
    color: var(--orange) !important; font-size: 1.3rem; white-space: nowrap;
  }
  .nav-phone:hover { color: var(--orange-dark) !important; text-decoration: none; }
  .nav-phone-icon {
    width: 40px; height: 40px; border-radius: 50%;
    background: var(--orange); color: #fff; display: inline-flex;
    align-items: center; justify-content: center;
  }
  .nav-phone-icon svg { width: 20px; height: 20px; fill: #fff; }
  nav#mainNav > ul { list-style: none; display: flex; gap: 28px; align-items: center; }
  /* Dropdown menu (Services) */
  nav li.has-dropdown { position: relative; }
  nav li.has-dropdown > a::after {
    content: " ▾";
    font-size: 0.85em;
    color: var(--muted);
  }
  nav li.has-dropdown .dropdown {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 260px;
    background: #fff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    border-radius: 8px;
    border-top: 3px solid var(--orange);
    padding: 8px 0;
    list-style: none;
    z-index: 200;
    flex-direction: column;
    gap: 0;
    align-items: stretch;
  }
  nav li.has-dropdown:hover .dropdown,
  nav li.has-dropdown:focus-within .dropdown,
  nav li.has-dropdown.open .dropdown {
    display: flex;
  }
  nav li.has-dropdown .dropdown li { width: 100%; }
  nav li.has-dropdown .dropdown a {
    display: block;
    padding: 10px 22px;
    font-size: 1rem;
    color: var(--text);
    white-space: nowrap;
  }
  nav li.has-dropdown .dropdown a:hover {
    background: var(--cream);
    color: var(--orange);
    text-decoration: none;
  }
  @media (max-width: 900px) {
    nav li.has-dropdown .dropdown {
      position: static;
      box-shadow: none;
      border-top: none;
      border-left: 3px solid var(--orange);
      padding: 0 0 0 14px;
      margin: 8px 0;
      min-width: 0;
    }
    nav li.has-dropdown:hover .dropdown { display: none; }
    nav li.has-dropdown.open .dropdown { display: flex; }
  }
  nav#mainNav a {
    color: var(--green-dark); font-weight: 600; font-size: 1rem;
    text-transform: none; padding: 8px 0;
  }
  nav#mainNav a:hover { color: var(--orange); text-decoration: none; }
  .cta-btn {
    background: var(--orange); color: #fff !important; padding: 12px 22px;
    border-radius: 6px; font-weight: 700;
  }
  .cta-btn:hover { background: var(--orange-dark); text-decoration: none; }
  .menu-toggle {
    display: none; background: none; border: none; font-size: 28px;
    color: var(--green-dark); cursor: pointer;
  }

  /* Hero section per page */
  .page-hero {
    background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-darker) 100%);
    color: #fff; padding: 70px 0 60px; text-align: center;
  }
  .page-hero .kicker {
    color: var(--orange); letter-spacing: 0.18em; text-transform: uppercase;
    font-size: 0.85rem; font-weight: 700; margin-bottom: 16px;
  }
  .page-hero h1 { font-size: clamp(2rem, 5vw, 3.4rem); line-height: 1.15; margin-bottom: 16px; }
  .page-hero p.lede { font-size: 1.15rem; max-width: 720px; margin: 0 auto; opacity: 0.92; }
  .page-hero .cta-row { margin-top: 28px; display: inline-flex; gap: 14px; flex-wrap: wrap; justify-content: center; }
  .page-hero .cta-row a {
    background: var(--orange); color: #fff; padding: 14px 26px; border-radius: 6px;
    font-weight: 700; font-size: 1.05rem;
  }
  .page-hero .cta-row a.secondary {
    background: transparent; border: 2px solid #fff;
  }
  .page-hero .cta-row a:hover { background: var(--orange-dark); text-decoration: none; }
  .page-hero .cta-row a.secondary:hover { background: rgba(255,255,255,0.1); }

  /* Body content */
  main section { padding: 64px 0; }
  main section.alt { background: #fff; }
  main h2 {
    font-size: clamp(1.6rem, 3vw, 2.2rem); color: var(--green-dark);
    margin-bottom: 18px; line-height: 1.25;
  }
  main h3 {
    font-size: 1.3rem; color: var(--green-dark); margin: 28px 0 12px;
  }
  main p { margin-bottom: 16px; }
  main ul, main ol { margin: 0 0 18px 22px; }
  main ul li, main ol li { margin-bottom: 8px; }
  main strong { color: var(--green-dark); }
  .pillars { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 28px; margin-top: 28px; }
  .pillar { background: var(--cream); border-left: 4px solid var(--orange); padding: 22px 24px; border-radius: 4px; }
  .pillar h3 { margin-top: 0; }
  .price-band {
    background: var(--cream); border: 1px solid #e5dec9; border-radius: 8px;
    padding: 22px 26px; margin: 26px 0;
  }
  .price-band strong { color: var(--orange); font-size: 1.15rem; }

  /* FAQ */
  .faq-item { background: #fff; border: 1px solid #e5dec9; border-radius: 6px; padding: 22px 26px; margin-bottom: 14px; }
  .faq-item h3 { margin-top: 0; margin-bottom: 8px; color: var(--green-dark); }
  .faq-item p { margin-bottom: 0; }

  /* Contact form */
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; }
  .contact-form { background: #fff; padding: 32px; border-radius: 8px; border: 1px solid #e5dec9; }
  .contact-form label { display: block; font-weight: 600; margin-bottom: 6px; color: var(--green-dark); }
  .contact-form input, .contact-form textarea {
    width: 100%; padding: 12px 14px; border: 1px solid #ccc; border-radius: 4px;
    font-family: inherit; font-size: 1rem; margin-bottom: 18px;
  }
  .contact-form textarea { min-height: 130px; resize: vertical; }
  .contact-form button {
    background: var(--orange); color: #fff; border: none; padding: 14px 28px;
    border-radius: 6px; font-size: 1.05rem; font-weight: 700; cursor: pointer; width: 100%;
  }
  .contact-form button:hover { background: var(--orange-dark); }
  .contact-info dl { display: grid; grid-template-columns: max-content 1fr; gap: 12px 18px; }
  .contact-info dt { font-weight: 700; color: var(--green-dark); }

  /* Final CTA */
  .cta-band {
    background: var(--green-dark); color: #fff; padding: 56px 0; text-align: center;
  }
  .cta-band h2 { color: #fff; }
  .cta-band p { font-size: 1.1rem; margin-bottom: 24px; opacity: 0.92; }
  .cta-band a {
    background: var(--orange); color: #fff !important; padding: 14px 28px;
    border-radius: 6px; font-weight: 700; font-size: 1.05rem;
  }
  .cta-band a:hover { background: var(--orange-dark); text-decoration: none; }

  /* Footer */
  footer {
    background: var(--green-darker); color: #c7bfb3; padding: 56px 0 28px;
  }
  .footer-grid {
    display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 44px;
  }
  footer h4 { color: #fff; font-size: 1.05rem; margin-bottom: 14px; letter-spacing: 0.06em; text-transform: uppercase; }
  footer ul { list-style: none; padding: 0; margin: 0; }
  footer ul li { margin-bottom: 8px; }
  footer a { color: #c7bfb3; }
  footer a:hover { color: var(--orange); text-decoration: none; }
  .footer-logo img { height: 64px; margin-bottom: 14px; }
  .footer-bottom {
    border-top: 1px solid #4a5a72; margin-top: 36px; padding-top: 24px;
    text-align: center; color: #8a8a8a; font-size: 0.9rem;
  }

  @media (max-width: 900px) {
    .contact-grid { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: 1fr 1fr; gap: 28px; }
  }
  @media (max-width: 700px) {
    .nav { padding: 16px 20px; gap: 14px; }
    .logo img { height: 44px; }
    .nav-phone { font-size: 1.1rem; }
    .nav-phone-icon { width: 32px; height: 32px; }
    nav#mainNav { display: none; position: absolute; top: 100%; right: 0; background: #fff; box-shadow: 0 2px 12px rgba(0,0,0,0.12); padding: 14px 20px; }
    nav#mainNav.open { display: block; }
    nav#mainNav ul { flex-direction: column; gap: 14px; align-items: flex-start; }
    .menu-toggle { display: inline-block; }
    .footer-grid { grid-template-columns: 1fr; }
  }
"""

# ─────────────────────────────────────────────────────────────────────────────
# Header (shared across all pages — sticky nav, logo, phone, links)
# ─────────────────────────────────────────────────────────────────────────────

def make_header(path_prefix=""):
    """path_prefix is empty for root-level pages, '../' for services/* pages."""
    return f"""
<header>
  <div class="nav">
    <a href="{path_prefix}index.html" class="logo">
      <img src="{path_prefix}logo.png" alt="Warren Bros Fencing logo">
      <div class="logo-text"><small>WICHITA, KS · SINCE 2021</small></div>
    </a>
    <div class="nav-right">
      <a href="tel:{SITE['phone_tel']}" class="nav-phone">
        <span class="nav-phone-icon"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
        <span>{SITE['phone']}</span>
      </a>
      <nav id="mainNav">
        <ul>
          <li class="has-dropdown">
            <a href="{path_prefix}services/" onclick="if(window.innerWidth<=900){{event.preventDefault();this.parentElement.classList.toggle('open');}}">Services</a>
            <ul class="dropdown">
              <li><a href="{path_prefix}services/cedar-privacy-fence.html">Cedar Privacy Fence Installation</a></li>
              <li><a href="{path_prefix}services/fence-repair.html">Fence Repair</a></li>
              <li><a href="{path_prefix}services/gate-installation.html">Gate Installation</a></li>
              <li><a href="{path_prefix}services/fence-removal.html">Fence Removal &amp; Tear-Out</a></li>
            </ul>
          </li>
          <li><a href="{path_prefix}faq.html">FAQ</a></li>
          <li><a href="{path_prefix}about.html">About</a></li>
          <li><a href="{path_prefix}contact.html">Contact</a></li>
          <li><a href="{path_prefix}contact.html" class="cta-btn">Get a Free Quote</a></li>
        </ul>
      </nav>
      <button class="menu-toggle" onclick="document.getElementById('mainNav').classList.toggle('open')">☰</button>
    </div>
  </div>
</header>"""


# ─────────────────────────────────────────────────────────────────────────────
# Footer (shared)
# ─────────────────────────────────────────────────────────────────────────────

def make_footer(path_prefix=""):
    return f"""
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="{path_prefix}logo.png" alt="Warren Bros Fencing logo">
        <h4>Warren Bros Fencing</h4>
        <p style="margin-top: 6px;">Family-owned cedar fence company in Wichita, KS. Built by brothers Grant and Alex Warren since 2021.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="{path_prefix}services/cedar-privacy-fence.html">Cedar Privacy Fence</a></li>
          <li><a href="{path_prefix}services/fence-repair.html">Fence Repair</a></li>
          <li><a href="{path_prefix}services/gate-installation.html">Gate Installation</a></li>
          <li><a href="{path_prefix}services/fence-removal.html">Fence Removal</a></li>
          <li><a href="{path_prefix}services/">All Services</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{SITE['address_city']}, {SITE['address_state']}</li>
          <li><a href="{path_prefix}faq.html">FAQ</a></li>
          <li>Open daily 7am-5pm</li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul>
          <li><a href="{SITE['gbp_review_link']}" target="_blank" rel="noopener">Google Reviews</a></li>
          <li><a href="{SITE['facebook']}" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="{SITE['nextdoor']}" target="_blank" rel="noopener">Nextdoor</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; 2026 Warren Bros Fencing &middot; Wichita, KS &middot; Family-owned since 2021
    </div>
  </div>
</footer>"""


# ─────────────────────────────────────────────────────────────────────────────
# Page builder — wraps the head + body content in shared chrome
# ─────────────────────────────────────────────────────────────────────────────

def build_page(filename, title, meta_description, canonical_url, h1, h1_kicker,
               hero_lede, hero_cta_primary, hero_cta_secondary, body_html,
               schema_json, og_image_path="logo.png", path_prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={SITE['ga4']}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{SITE['ga4']}');
</script>

<title>{title}</title>
<meta name="description" content="{meta_description}">
<link rel="canonical" href="{canonical_url}">
<link rel="icon" type="image/png" href="{path_prefix}logo.png">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:site_name" content="Warren Bros Fencing">
<meta property="og:image" content="{SITE['url']}/{og_image_path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_description}">

<meta name="geo.region" content="US-KS">
<meta name="geo.placename" content="Wichita">
<meta name="robots" content="index, follow">

<script type="application/ld+json">
{schema_json}
</script>

<style>{CSS}</style>
</head>
<body>

{make_header(path_prefix)}

<section class="page-hero">
  <div class="container-narrow">
    <div class="kicker">{h1_kicker}</div>
    <h1>{h1}</h1>
    <p class="lede">{hero_lede}</p>
    <div class="cta-row">
      <a href="tel:{SITE['phone_tel']}">{hero_cta_primary}</a>
      <a href="{path_prefix}contact.html" class="secondary">{hero_cta_secondary}</a>
    </div>
  </div>
</section>

<main>
{body_html}
</main>

<section class="cta-band">
  <div class="container-narrow">
    <h2>Ready for a free in-person estimate?</h2>
    <p>We come out, walk your property, and give you a written quote on the spot — usually within one business day. No deposits, no pressure.</p>
    <a href="tel:{SITE['phone_tel']}">Call or Text {SITE['phone']}</a>
  </div>
</section>

{make_footer(path_prefix)}

</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# Page content
# ─────────────────────────────────────────────────────────────────────────────

# --- ABOUT PAGE ---
ABOUT_BODY = """
<section>
  <div class="container-narrow">
    <h2>Built by brothers. Built for Kansas.</h2>
    <p>Warren Bros Fencing is a family-owned cedar fence company in Wichita, Kansas, founded in 2021 by brothers Grant and Alex Warren. We install cedar privacy fences, wood fences, gates, and handle fence repair and old fence tear-out across Wichita and the surrounding metro.</p>
    <p>When you call us, you're talking to one of the brothers — not a sales rep, not a call center, not an assistant. We come out, walk your property with you, and give you a written quote on the spot. No deposits up front. No pressure to sign anything. Free in-person estimates, usually within one business day of your call.</p>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>How we work</h2>
    <p>Every fence we build follows the same approach: pressure-treated posts set in concrete, full cedar pickets graded for durability, galvanized hardware for Kansas weather. Standard install for a 6-foot cedar privacy fence runs roughly $30 to $50 per linear foot, all materials and labor included.</p>
    <div class="pillars">
      <div class="pillar">
        <h3>Hands-on every job</h3>
        <p>Grant and Alex personally show up to every install. Quality control isn't delegated.</p>
      </div>
      <div class="pillar">
        <h3>Free written quotes</h3>
        <p>In-person estimates, on the spot, with a written quote you can hold. No back-and-forth pricing games.</p>
      </div>
      <div class="pillar">
        <h3>Built for Kansas weather</h3>
        <p>Proper post depth, concrete footings, hardware rated for our wind. Most installs outlast their warranty.</p>
      </div>
      <div class="pillar">
        <h3>No deposits, no pressure</h3>
        <p>We don't take money up front. You pay when the fence is done and you're happy with it.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container-narrow">
    <h2>What we install</h2>
    <ul>
      <li><strong>Cedar privacy fences</strong> — 6-foot and 8-foot heights, solid-board construction, the most common request.</li>
      <li><strong>Picket and shadowbox fences</strong> — traditional spaced-picket cedar fencing.</li>
      <li><strong>Wood fence installation</strong> — standard board-on-board and other wood styles.</li>
      <li><strong>Fence repair</strong> — leaning posts, broken pickets, sagging gates, storm damage.</li>
      <li><strong>Gate installation</strong> — single and double cedar gates, hardware included.</li>
      <li><strong>Old fence removal and tear-out</strong> — typically bundled with a new install.</li>
    </ul>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>Service area</h2>
    <p>We serve Wichita and the surrounding metro:</p>
    <p><strong>Wichita · Derby · Andover · Bel Aire · Maize · Park City · Goddard · Haysville · Valley Center · Rose Hill · Augusta · Kechi · Mulvane · Colwich</strong></p>
    <p>If you're nearby and don't see your town listed, give us a call — we probably still cover you.</p>
  </div>
</section>
"""

# --- CONTACT PAGE ---
CONTACT_BODY = f"""
<section>
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <h2>Get a free in-person estimate</h2>
        <p>Call or text us. We'll set up a quick property visit — usually within one business day — and give you a written quote on the spot.</p>
        <dl>
          <dt>Phone</dt><dd><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></dd>
          <dt>Email</dt><dd><a href="mailto:{SITE['email']}">{SITE['email']}</a></dd>
          <dt>Service area</dt><dd>Wichita, Derby, Andover, Bel Aire, Maize, Park City, Goddard, Haysville, Valley Center, Rose Hill, Augusta, Kechi, Mulvane, Colwich</dd>
          <dt>Hours</dt><dd>Open 7 days a week, 7am-5pm (including Sunday)</dd>
        </dl>
        <div class="price-band">
          <strong>Typical pricing:</strong><br>
          6-foot cedar privacy fence: ~$30-50 per linear foot installed<br>
          Fence repair: typically $150-800 depending on scope<br>
          Free in-person estimates always
        </div>
      </div>
      <form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="3457639e-cfb1-4a69-8945-7bfb44c09b44">
        <input type="hidden" name="subject" value="Quote request — Warren Bros Fencing">
        <input type="hidden" name="from_name" value="Warren Bros Fencing Website">
        <h2>Request a quote</h2>
        <label for="name">Your name</label>
        <input type="text" id="name" name="name" required>
        <label for="phone">Phone (best for quote callbacks)</label>
        <input type="tel" id="phone" name="phone" required>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
        <label for="address">Property address (where the fence work is needed)</label>
        <input type="text" id="address" name="address">
        <label for="message">What kind of fence work are you looking for?</label>
        <textarea id="message" name="message" placeholder="New cedar privacy fence, fence repair, gate install, tear-out — whatever you need."></textarea>
        <button type="submit">Request my free estimate</button>
        <p style="font-size: 0.85rem; color: var(--muted); margin-top: 12px; margin-bottom: 0;">We'll text or call you back within one business day, usually faster.</p>
      </form>
    </div>
  </div>
</section>
"""

# --- SERVICES OVERVIEW ---
SERVICES_INDEX_BODY = """
<section>
  <div class="container">
    <h2 style="text-align: center; margin-bottom: 12px;">Cedar fence services in Wichita and the surrounding metro</h2>
    <p style="text-align: center; max-width: 720px; margin: 0 auto 36px; color: var(--muted);">Built by brothers Grant and Alex Warren. Hands-on every job. Free in-person estimates.</p>
    <div class="pillars">
      <div class="pillar">
        <h3><a href="cedar-privacy-fence.html">Cedar Privacy Fence Installation</a></h3>
        <p>6-foot and 8-foot solid-cedar privacy fences. Pressure-treated posts in concrete, full cedar pickets, galvanized hardware. ~$30-50 per linear foot installed.</p>
      </div>
      <div class="pillar">
        <h3><a href="fence-repair.html">Fence Repair</a></h3>
        <p>Leaning posts, broken pickets, sagging gates, storm-snapped sections, post rot. Most repairs $150-800. Often same- or next-day across the metro.</p>
      </div>
      <div class="pillar">
        <h3><a href="gate-installation.html">Gate Installation</a></h3>
        <p>Single and double cedar gates. With or without hardware. New installs or replacement of failed gates on existing fences.</p>
      </div>
      <div class="pillar">
        <h3><a href="fence-removal.html">Fence Removal &amp; Tear-Out</a></h3>
        <p>Pull failing wood, chain-link, or vinyl fences — posts, concrete footings, and debris included. Often bundled with a new install.</p>
      </div>
    </div>
  </div>
</section>
"""

# --- SERVICE: CEDAR PRIVACY FENCE ---
CEDAR_BODY = """
<section>
  <div class="container-narrow">
    <h2>How much does a cedar privacy fence cost in Wichita?</h2>
    <p>The most common question we get, and the honest answer: <strong>$40 to $55 per linear foot installed</strong> for a standard 6-foot cedar privacy fence. That's materials, labor, post setting, and basic site cleanup all in. A typical residential job (~100 linear feet) lands in the $4,000-$5,500 range.</p>
    <p>What moves the price within that range: length, height (6-foot is standard, 8-foot is more), gate count, slope work, and whether an old fence needs tear-out first. Every yard is different, so the written quote happens on-site after we walk the property with you.</p>
    <div class="price-band">
      <strong>$40-$55 per linear foot installed</strong><br>
      Includes materials, labor, post setting, basic cleanup. Free in-person estimates &middot; written quote on the spot &middot; no deposits.
    </div>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>What's included in a cedar privacy fence install</h2>
    <ul>
      <li>Site walk and final design choice (height, gate placement, picket style)</li>
      <li>Pressure-treated 4x4 posts, set in concrete to proper depth for the Kansas frost line</li>
      <li>Full-length cedar pickets, properly graded — no chipped, knotted, or split boards</li>
      <li>Three horizontal rails per 6-foot section (four for 8-foot)</li>
      <li>Galvanized fasteners throughout (no rust streaks two years in)</li>
      <li>Standard cleanup — we don't leave you with a pile of scraps</li>
    </ul>
    <h2>Why cedar holds up to Kansas weather</h2>
    <p>Cedar is naturally rot-resistant and naturally repellent to most insects — both of which matter in Kansas where the freeze-thaw cycle, the humidity in summer, and the wind year-round all eat lower-grade wood fences alive. A properly-installed cedar fence built for our weather (full pickets, pressure-treated posts in concrete, galvanized hardware) typically outlasts its 15-20 year service-life estimate. We've never had to come back on a fence we built.</p>
  </div>
</section>

<section>
  <div class="container-narrow">
    <h2>HOA fence approval in Wichita — how it works</h2>
    <p>A lot of Wichita-area HOAs require approval before you build or replace a fence. The exact rules vary by HOA, but the typical requirements: height limits (usually 6 feet maximum at the property line), material restrictions (cedar is almost always allowed; some HOAs prohibit certain wood treatments or vinyl), setback rules, gate placement, and sometimes color or stain restrictions.</p>
    <p><strong>What we handle:</strong> we provide you with the fence specifications, materials, dimensions, and reference photos you need to submit your HOA application — the technical details that prove the fence meets their standards.</p>
    <p><strong>What we don't handle:</strong> we don't fill out or submit the HOA paperwork for you. That's between you and your HOA board. We've found from experience that HOAs strongly prefer to deal with the homeowner directly, and the approval process typically takes 30-60 days from submission. Plan your fence project around that timeline.</p>
    <p>Once you have HOA approval in hand, we schedule the build. Most installs take 2-3 days; larger jobs (over 200 linear feet, multiple gates, slope work, tear-out) can take 3-5 days. Weather delays are rare in Kansas spring/summer/fall.</p>
  </div>
</section>
"""

# --- SERVICE: FENCE REPAIR ---
REPAIR_BODY = """
<section>
  <div class="container-narrow">
    <h2>How much does fence repair cost in Wichita?</h2>
    <p>Most fence repairs land between <strong>$250 and $800</strong>, depending on what failed and how much of the run needs work. Single broken picket: low end. Multiple sister posts plus rail replacement: mid range. Storm-down section requiring partial rebuild: higher end. We give you a written quote on site after we see the damage.</p>
    <p>Not every job needs a full tear-out and rebuild. Most fence issues — leaning posts, broken pickets, sagging gates, storm-snapped sections, post rot — can be repaired without replacing the whole run. We do same- or next-day repair work across the Wichita metro when scheduling allows.</p>
    <div class="price-band">
      <strong>$250-$800 typical repair range</strong><br>
      Free in-person assessment &middot; written quote on the spot &middot; same- or next-day service when scheduling allows
    </div>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>Common fence repairs we handle in Wichita</h2>
    <ul>
      <li><strong>Leaning posts</strong> — pulled out and re-set in concrete, or sistered if the post itself is sound</li>
      <li><strong>Broken or split pickets</strong> — replaced with matching cedar from current stock</li>
      <li><strong>Sagging gates</strong> — re-hung, re-leveled, hardware replaced if needed</li>
      <li><strong>Storm-snapped sections</strong> — partial section rebuild, integrated with the existing run</li>
      <li><strong>Post rot at ground level</strong> — pulled and replaced; concrete footings re-poured</li>
      <li><strong>Loose or missing hardware</strong> — galvanized replacements throughout</li>
    </ul>
    <p style="margin-top: 24px;">If a section's been down for a while or the whole run is past its useful life, we'll tell you straight — sometimes a full replacement is the better call than chasing repairs across an aging fence. Free in-person assessment either way.</p>
  </div>
</section>

<section>
  <div class="container-narrow">
    <h2>Storm damage fence repair in Wichita</h2>
    <p>Kansas weather doesn't ask permission. Storm cells, straight-line wind, hail, and the occasional tornado all leave fence damage in their wake — snapped pickets, leaning posts, sections flattened by a fallen tree, gates twisted off their hinges. We prioritize storm-damage repairs and try to be on-site within a business day or two of your call.</p>
    <p><strong>For tree removal and storm cleanup, we partner with Baker Tree Service</strong> — when a tree comes down across your fence, it usually needs to come off the fence before we can rebuild. Baker has been doing tree work in Wichita since 2006 and handles the tree removal cleanly. Call Baker direct for tree work:</p>
    <p style="text-align: center; padding: 14px 0;"><a href="https://www.bakertreeserviceict.com" target="_blank" rel="noopener" style="color: var(--orange); font-weight: 700; font-size: 1.1rem;">Baker Tree Service &middot; (316) 409-1144 &middot; bakertreeserviceict.com</a></p>
    <p>Once the tree is clear, we handle the fence rebuild on the same property — no second contractor to coordinate, no scheduling gaps.</p>
  </div>
</section>
"""

# --- SERVICE: GATE INSTALLATION (PEDESTRIAN ONLY — no driveway/vehicle gates) ---
GATE_BODY = """
<section>
  <div class="container-narrow">
    <figure style="margin: 0 0 32px;">
      <img src="../photo-cedar-gate.jpg" alt="Cedar walk-through gate installed in a Wichita backyard fence with heavy-duty black hardware" style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);">
      <figcaption style="font-size: 0.9rem; color: var(--muted); margin-top: 8px; text-align: center;">Cedar single walk-through gate &middot; Wichita backyard install</figcaption>
    </figure>
    <h2>Cedar pedestrian gate installation in Wichita</h2>
    <p>Single walk-through gates and double-leaf yard gates built to match your existing fence — no obvious patch jobs. We focus on pedestrian access gates (yard, garden, side-yard, fence-line walk-throughs); we do not install driveway or vehicle gates.</p>
    <p>Most homeowners need either a single 3-4 foot walk-through gate or a double-leaf 6-8 foot wide-yard gate for mower or equipment access. Hardware (heavy-duty hinges, latch, optional drop rod for double gates) included.</p>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>What we install</h2>
    <ul>
      <li><strong>Single pedestrian gates</strong> — 3-4 feet wide, the standard backyard access gate</li>
      <li><strong>Double-leaf yard gates</strong> — 6-8 feet total, two leaves that swing open for lawn mowers, zero-turns, or yard equipment</li>
      <li><strong>Custom widths</strong> — wider walk-throughs for specific equipment or accessibility needs</li>
      <li><strong>Hardware upgrades</strong> — heavy-duty hinges, drop rods, magnetic latches, lockable handles</li>
      <li><strong>Replacement gates</strong> — when an existing gate has failed but the fence is fine, we replace just the gate</li>
    </ul>
    <p style="margin-top: 24px; padding: 14px 18px; background: #fff; border-left: 3px solid var(--orange);"><strong>Note:</strong> we don't install driveway gates, electric gates, or vehicle gates. If that's what you need, we can recommend a contractor who specializes in that work — just ask when you call.</p>
    <h2>Why gates fail (and how we build to last)</h2>
    <p>Most failed gates we replace had the same problem: undersized hinges, unsupported posts, or gate frames built too lightly for the picket weight. Our gates use heavier-gauge hinges than most installs, with the gate post set deeper in concrete than standard fence posts to handle the swing load. The cost difference at install is small; the difference five years in is significant.</p>
  </div>
</section>
"""

# --- SERVICE: FENCE REMOVAL ---
REMOVAL_BODY = """
<section>
  <div class="container-narrow">
    <h2>Fence removal and tear-out in Wichita</h2>
    <p>Old wood fence past its useful life? Chain-link from a previous owner that doesn't match the property? Failed vinyl section? We pull failing fences, posts, concrete footings, and debris — leaving the property ready for the next step.</p>
    <p>Most fence removals get bundled with a new install (we tear out the old fence, build the new one on the same line, single job). But we also do removal-only jobs if you're just trying to clear the line for landscaping, equipment access, or sale prep.</p>
    <div class="price-band">
      <strong>Removal pricing: per job</strong><br>
      Every removal is different — fence type, post type, concrete footings, total length, disposal needs, and access for our truck all factor in. We quote on-site after walking the property. Often bundled at a discount when paired with a new install on the same line.
    </div>
  </div>
</section>

<section class="alt">
  <div class="container-narrow">
    <h2>What's included in a tear-out</h2>
    <ul>
      <li>Pulling all pickets, panels, and rails</li>
      <li>Removing all fence posts (cedar, treated wood, chain-link, vinyl) — including the concrete footings</li>
      <li>Hauling away the demoed material — we don't leave a pile in your yard</li>
      <li>Ground-level cleanup so the line is ready for the new fence (or just clear for landscaping)</li>
    </ul>
    <h2>Common reasons to remove an old fence</h2>
    <ul>
      <li><strong>Past its useful life</strong> — leaning posts, rotted pickets, multiple failure points — repair is no longer the right call</li>
      <li><strong>Storm-flattened section</strong> — particularly common after Kansas straight-line wind events</li>
      <li><strong>Property purchase or sale prep</strong> — a failing fence is a visible negative; either remove cleanly or replace</li>
      <li><strong>Switching materials</strong> — chain-link out, cedar in, on a single property visit</li>
      <li><strong>Equipment or vehicle access</strong> — sometimes the fence just has to go for a few days during a bigger project</li>
    </ul>
    <p style="margin-top: 24px;">Some HOAs require approval before fence removal too — particularly if you're not replacing it. Check your HOA rules before scheduling the tear-out.</p>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Schema generators
# ─────────────────────────────────────────────────────────────────────────────

def about_schema():
    return """{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "url": "https://www.warrenbrosfencing.com/about.html",
  "name": "About Warren Bros Fencing",
  "description": "Family-owned cedar fence company in Wichita, KS. Founded in 2021 by brothers Grant and Alex Warren.",
  "about": {
    "@type": "FenceContractor",
    "name": "Warren Bros Fencing",
    "url": "https://www.warrenbrosfencing.com/",
    "foundingDate": "2021",
    "founders": [
      {"@type": "Person", "name": "Grant Warren"},
      {"@type": "Person", "name": "Alex Warren"}
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Wichita",
      "addressRegion": "KS",
      "addressCountry": "US"
    },
    "telephone": "(316) 285-9172"
  }
}"""

def contact_schema():
    return """{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "url": "https://www.warrenbrosfencing.com/contact.html",
  "name": "Contact Warren Bros Fencing",
  "description": "Get a free in-person estimate for cedar fence installation, repair, gate installation, or fence removal in Wichita, KS."
}"""

def faq_html(faqs):
    """Generate visible FAQ HTML section from a list of (question, answer) tuples."""
    items = "\n".join([
        f'      <div class="faq-item">\n        <h3>{q}</h3>\n        <p>{a}</p>\n      </div>'
        for q, a in faqs
    ])
    return f"""
<section class="alt">
  <div class="container-narrow">
    <h2>Frequently asked questions</h2>
{items}
  </div>
</section>"""


def service_schema_with_faq(service_name, service_url, description, faqs):
    """Combined Service + FAQPage schema using @graph."""
    faq_items = ",\n      ".join([
        f'{{\n        "@type": "Question",\n        "name": {json.dumps(q)},\n        "acceptedAnswer": {{\n          "@type": "Answer",\n          "text": {json.dumps(a)}\n        }}\n      }}'
        for q, a in faqs
    ])
    return f"""{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Service",
      "@id": "{service_url}#service",
      "name": "{service_name}",
      "url": "{service_url}",
      "description": "{description}",
      "provider": {{
        "@type": "FenceContractor",
        "name": "Warren Bros Fencing",
        "url": "https://www.warrenbrosfencing.com/",
        "telephone": "(316) 285-9172",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "Wichita",
          "addressRegion": "KS",
          "addressCountry": "US"
        }}
      }},
      "areaServed": [
        {{"@type": "City", "name": "Wichita"}},
        {{"@type": "City", "name": "Derby"}},
        {{"@type": "City", "name": "Andover"}},
        {{"@type": "City", "name": "Bel Aire"}},
        {{"@type": "City", "name": "Maize"}},
        {{"@type": "City", "name": "Park City"}},
        {{"@type": "City", "name": "Goddard"}},
        {{"@type": "City", "name": "Haysville"}},
        {{"@type": "City", "name": "Valley Center"}}
      ]
    }},
    {{
      "@type": "FAQPage",
      "@id": "{service_url}#faq",
      "mainEntity": [
        {faq_items}
      ]
    }}
  ]
}}"""


def service_schema(service_name, service_url, description):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "{service_url}#service",
  "name": "{service_name}",
  "url": "{service_url}",
  "description": "{description}",
  "provider": {{
    "@type": "FenceContractor",
    "name": "Warren Bros Fencing",
    "url": "https://www.warrenbrosfencing.com/",
    "telephone": "(316) 285-9172",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Wichita",
      "addressRegion": "KS",
      "addressCountry": "US"
    }}
  }},
  "areaServed": [
    {{"@type": "City", "name": "Wichita"}},
    {{"@type": "City", "name": "Derby"}},
    {{"@type": "City", "name": "Andover"}},
    {{"@type": "City", "name": "Bel Aire"}},
    {{"@type": "City", "name": "Maize"}},
    {{"@type": "City", "name": "Park City"}},
    {{"@type": "City", "name": "Goddard"}},
    {{"@type": "City", "name": "Haysville"}},
    {{"@type": "City", "name": "Valley Center"}}
  ]
}}"""

def services_index_schema():
    return """{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "url": "https://www.warrenbrosfencing.com/services/",
  "name": "Cedar fence services in Wichita, KS",
  "description": "All services from Warren Bros Fencing — cedar privacy fence installation, fence repair, gate installation, fence removal."
}"""


# ─────────────────────────────────────────────────────────────────────────────
# FAQ page — standalone /faq.html with 13 Q&As + FAQPage JSON-LD schema
# ─────────────────────────────────────────────────────────────────────────────

FAQS_DATA = [
    ("How much does a cedar privacy fence cost in Wichita?",
     "A standard 6-foot cedar privacy fence runs $40 to $55 per linear foot installed, all materials and labor included. A typical 100-foot residential job lands in the $4,000–$5,500 range. What moves the price within that band: total length, height (6-foot is standard, 8-foot is more), gate count, slope work, and whether an old fence needs tear-out first. Every yard is different — we walk the property with you and hand you a written quote on the spot at the in-person estimate. No phone quotes, no surprises after the fact."),

    ("How much does fence repair cost?",
     "Most repairs land between $250 and $800. Smaller jobs (a single leaning post, a few broken pickets, one sagging gate) are at the low end. Larger jobs (multiple sections, post rot at ground line, storm damage across a long run) are at the high end. Repairs over $800 usually mean the fence is closer to needing replacement than repair — we'll tell you that honestly during the assessment instead of selling you a repair that won't last. Free in-person assessment, written quote on the spot."),

    ("How much does a gate cost?",
     "Cedar gates run $650 to $950 installed, depending on whether it's a standalone gate job or built into a full fence install. We do single walk-through gates (3–4 feet wide, standard backyard access) and double-leaf yard gates (6–8 feet total, two leaves that swing open for mower or equipment access). Heavy-duty hinges, latch, and optional drop rod for double gates are included. We do not install driveway or vehicle gates — those require specialized hardware and a different contractor."),

    ("How long does a cedar fence installation take?",
     "Most residential installs take 2 to 3 days from start to finish. Larger jobs (over 200 linear feet, multiple gates, slope work, full tear-out of an old fence) can take 3 to 5 days. We aim to start and finish within a single visit — no leaving a half-built fence sitting in your yard between trips. Weather delays in Kansas spring/summer/fall are rare; storm season can push schedules."),

    ("What does the estimate process look like?",
     "You call or text (316) 285-9172. We schedule a free in-person walkthrough at your property, usually within a few days. On-site we measure, talk through height/style/gate placement, and write you a quote on the spot — typically before we leave the property. No high-pressure sales, no \"today only\" pricing, no quote in three days by email. You get the number while we're standing in your yard with you."),

    ("What's included in your price?",
     "Everything: materials (cedar pickets, posts, rails, concrete, hardware), labor for the full crew, post-hole digging, concrete setting, full assembly, hardware installation, and jobsite cleanup. We haul away the old fence debris if there was a tear-out. We don't add fees for \"fuel surcharge\" or \"disposal\" or other line items at the end. The number on your written quote is the number you pay."),

    ("How long does a cedar fence last in Kansas?",
     "Properly built and maintained, a Western red cedar fence lasts 15 to 25 years in Kansas. The variables that determine where in that range you land: cedar grade (we use properly graded Western red cedar, not the cheaper rot-prone alternatives), post depth (we set posts at full frost-line depth in concrete with gravel for drainage), and homeowner maintenance (annual cleaning, occasional staining if you want to preserve the color). Cedar is naturally rot- and insect-resistant — even untreated, it outlasts pine by a wide margin."),

    ("What grade of cedar do you use?",
     "We use Western red cedar, properly graded — the same grade specified for premium fence work across the region. Cheaper cedar grades (knottier, less rot-resistant heartwood content) save the contractor a few dollars per board and cost the homeowner years of fence life. We don't run that math. The cedar we install is what we'd use on our own properties."),

    ("Do you install driveway gates or electric gates?",
     "No. We specialize in pedestrian gates only — single walk-through gates and double-leaf yard gates for mower or equipment access. Driveway gates, electric gates, and vehicle gates require specialized hardware, motors, and code considerations we don't work in. If that's what you need, we can recommend a contractor who specializes in that work — just ask when you call."),

    ("Do I need HOA approval for a fence in Wichita?",
     "Most Wichita-area HOAs require approval before you build or replace a fence. The exact rules vary by HOA, but typical requirements include: height limits (usually 6 feet maximum at the property line), material restrictions (cedar is almost always allowed), setback rules, gate placement, and sometimes color or stain restrictions. We provide you with the specs you need for your HOA submission — materials, height, layout drawing — but the homeowner submits the paperwork to their HOA. Most Wichita HOAs respond in 30–60 days. Once you have approval in hand, we schedule the build."),

    ("What about storm damage to my existing fence?",
     "Kansas weather doesn't ask permission. Storm cells, straight-line wind, hail, and the occasional tornado all leave fence damage in their wake — snapped pickets, leaning posts, sections flattened by a fallen tree, gates twisted off their hinges. We prioritize storm-damage repairs and aim to be on-site within a business day or two of your call. If a tree came down on your fence, we partner with Baker Tree Service (316-409-1144) to handle the tree removal first so we can get to the fence work."),

    ("Are you licensed and insured?",
     "Wichita doesn't require a contractor's license for residential fence installation work — that's a regional regulatory gap, not us cutting corners. We carry general liability insurance that protects your property during the job. Warren Bros Fencing is a registered Kansas LLC (founded 2022). We can provide our Certificate of Insurance on request before any work begins."),

    ("Who's responsible for fence repair between neighbors?",
     "In Kansas, fences directly on the property line are generally shared responsibility between neighbors — both benefit from the fence, so both typically share costs for installation, repair, and replacement. Fences set back from the property line on one homeowner's property are that homeowner's responsibility. The honest answer is most fence disputes between neighbors come down to whoever cares more about how the fence looks paying more of the cost. If you're trying to figure out who should pay for what, the cleanest path is a written agreement with your neighbor before the work starts — we can build whatever you both agree to."),
]


FAQ_BODY = """
<section>
  <div class="container-narrow">
    <p style="font-size: 1.15rem; line-height: 1.6;">Below are the questions we get most often from homeowners across Wichita and the surrounding metro — Derby, Andover, Goddard, Maize, Haysville, Augusta, Park City, Bel Aire, and Valley Center. If you don't see your question here, call or text us at <a href="tel:+13162859172"><strong>(316) 285-9172</strong></a> and we'll answer it directly.</p>
  </div>
</section>
""" + faq_html(FAQS_DATA)


def faq_page_schema(faqs):
    """Standalone FAQPage schema for the /faq.html page."""
    faq_items = ",\n      ".join([
        f'{{\n        "@type": "Question",\n        "name": {json.dumps(q)},\n        "acceptedAnswer": {{\n          "@type": "Answer",\n          "text": {json.dumps(a)}\n        }}\n      }}'
        for q, a in faqs
    ])
    return f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://www.warrenbrosfencing.com/faq.html#faq",
  "mainEntity": [
    {faq_items}
  ]
}}"""


# ─────────────────────────────────────────────────────────────────────────────
# Build all pages
# ─────────────────────────────────────────────────────────────────────────────

PAGES = [
    {
        "filename": "about.html",
        "path_prefix": "",
        "title": "About Warren Bros Fencing — Family-Owned Cedar Fence Company in Wichita, KS",
        "meta": "Warren Bros Fencing is a family-owned cedar fence company in Wichita, KS. Founded 2021 by brothers Grant and Alex Warren. Built for Kansas weather. Free in-person estimates.",
        "canonical": "https://www.warrenbrosfencing.com/about.html",
        "h1": "About Warren Bros Fencing",
        "h1_kicker": "Built by brothers. Built for Kansas.",
        "lede": "Family-owned cedar fence company in Wichita, founded in 2021. When you call, you're talking to one of the brothers.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Request a free estimate",
        "body": ABOUT_BODY,
        "schema": about_schema(),
    },
    {
        "filename": "contact.html",
        "path_prefix": "",
        "title": "Contact Warren Bros Fencing — Free Estimates in Wichita, KS",
        "meta": "Get a free in-person estimate for cedar fence installation, repair, gate installation, or fence removal in Wichita, KS. Call or text Warren Bros at (316) 285-9172.",
        "canonical": "https://www.warrenbrosfencing.com/contact.html",
        "h1": "Get a free in-person estimate",
        "h1_kicker": "No deposits · No pressure · No callcenter",
        "lede": "Call or text us. We'll set up a property visit within one business day and give you a written quote on the spot.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Text us a photo",
        "body": CONTACT_BODY,
        "schema": contact_schema(),
    },
    {
        "filename": "services/index.html",
        "path_prefix": "../",
        "title": "Cedar Fence Services in Wichita, KS — Warren Bros Fencing",
        "meta": "Cedar privacy fence installation, fence repair, gate installation, and fence removal in Wichita, KS. Family-owned. Free in-person estimates. Built by brothers Grant and Alex Warren.",
        "canonical": "https://www.warrenbrosfencing.com/services/",
        "h1": "Cedar fence services in Wichita and the metro",
        "h1_kicker": "Built by brothers · Free estimates · Written quotes on the spot",
        "lede": "Installation, repair, gates, and removal — handled by the same two people who build the fence.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Request a free estimate",
        "body": SERVICES_INDEX_BODY,
        "schema": services_index_schema(),
    },
    {
        "filename": "services/cedar-privacy-fence.html",
        "path_prefix": "../",
        "title": "Cedar Privacy Fence Installation in Wichita, KS — Cost &amp; Free Quote | Warren Bros Fencing",
        "meta": "Cedar privacy fence installation in Wichita, KS — typical cost $40-$55 per linear foot installed. 6-foot and 8-foot solid-board cedar. Free in-person estimates.",
        "canonical": "https://www.warrenbrosfencing.com/services/cedar-privacy-fence.html",
        "h1": "Cedar Privacy Fence Installation in Wichita, KS",
        "h1_kicker": "$40-$55/ft &middot; 6ft &amp; 8ft &middot; Free estimates",
        "lede": "The most common request we get. Solid-board cedar privacy fence, built for Kansas weather, with a written quote on the spot.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Get a written quote",
        "body": CEDAR_BODY + faq_html([
            ("How much does a cedar privacy fence cost in Wichita?",
             "A standard 6-foot cedar privacy fence runs $40 to $55 per linear foot installed, all materials and labor included. A typical 100-foot residential job lands in the $4,000-$5,500 range. The exact price depends on length, height, gate count, slope, and whether an old fence needs tear-out first. We give you a written quote on the spot at the in-person estimate."),
            ("Is cedar a good choice for privacy fencing in Kansas?",
             "Yes. Cedar is naturally rot-resistant, naturally insect-repellent, and weathers to a clean silver-gray over time. Properly installed (pressure-treated posts set in concrete, full cedar pickets, galvanized hardware), a cedar privacy fence typically outlasts its 15-20 year service-life estimate even in Kansas weather. Cedar is the most common privacy fence material in Wichita for these reasons."),
            ("How long does a cedar privacy fence last in Kansas weather?",
             "15-20 years is the typical service-life estimate for a properly-built cedar privacy fence in Kansas. The freeze-thaw cycle, summer humidity, and year-round wind are hard on lower-grade installs, but cedar handles them well when paired with proper post depth, concrete footings, and galvanized hardware."),
            ("Do I need HOA approval before installing a fence in Wichita?",
             "Most Wichita-area HOAs require approval before you build or replace a fence. We can provide the fence specs, dimensions, and reference photos you need for your HOA application, but you submit the paperwork to your HOA yourself — they prefer to deal with the homeowner directly. Plan for a 30-60 day HOA review window before the actual install."),
            ("Do I need a permit to build a fence in Wichita?",
             "For most residential fences within standard height limits (6 feet at the property line) in Wichita, no city permit is required, but your HOA may have its own approval process. Tall fences (over 8 feet), corner-lot fences near intersections, and commercial-zone fences may require permits. We flag any permit concerns at the estimate."),
        ]),
        "schema": service_schema_with_faq(
            "Cedar Privacy Fence Installation",
            "https://www.warrenbrosfencing.com/services/cedar-privacy-fence.html",
            "Cedar privacy fence installation in Wichita, KS. 6-foot and 8-foot solid-board cedar, pressure-treated posts in concrete, galvanized hardware. $40-$55 per linear foot installed.",
            [
                ("How much does a cedar privacy fence cost in Wichita?",
                 "A standard 6-foot cedar privacy fence runs $40 to $55 per linear foot installed, all materials and labor included. A typical 100-foot residential job lands in the $4,000-$5,500 range. Exact price depends on length, height, gate count, slope, and whether an old fence needs tear-out first."),
                ("Is cedar a good choice for privacy fencing in Kansas?",
                 "Yes. Cedar is naturally rot-resistant, naturally insect-repellent, and weathers to a clean silver-gray over time. Properly installed, a cedar privacy fence typically outlasts its 15-20 year service-life estimate even in Kansas weather."),
                ("How long does a cedar privacy fence last in Kansas weather?",
                 "15-20 years is the typical service-life estimate for a properly-built cedar privacy fence in Kansas, when built with pressure-treated posts in concrete, full cedar pickets, and galvanized hardware."),
                ("Do I need HOA approval before installing a fence in Wichita?",
                 "Most Wichita-area HOAs require approval before you build or replace a fence. We provide the fence specs and reference photos you need for your HOA application, but you submit the paperwork to your HOA yourself. Plan for a 30-60 day HOA review window before the actual install."),
                ("Do I need a permit to build a fence in Wichita?",
                 "For most residential fences within standard height limits (6 feet at the property line) in Wichita, no city permit is required, but your HOA may have its own approval process."),
            ]
        ),
    },
    {
        "filename": "services/fence-repair.html",
        "path_prefix": "../",
        "title": "Fence Repair in Wichita, KS — Emergency &amp; Storm Damage | Warren Bros Fencing",
        "meta": "Wood fence repair in Wichita, KS — leaning posts, broken pickets, sagging gates, storm damage. Most repairs $250-$800. Same- or next-day service. Free written quotes.",
        "canonical": "https://www.warrenbrosfencing.com/services/fence-repair.html",
        "h1": "Fence Repair in Wichita, KS",
        "h1_kicker": "$250-$800 typical &middot; Same- or next-day &middot; Storm damage",
        "lede": "Most fence issues can be repaired without replacing the whole run. We do same- or next-day repair work across the Wichita metro, and we partner with Baker Tree Service for storm cleanup that involves tree damage.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Text us a photo",
        "body": REPAIR_BODY + faq_html([
            ("How much does fence repair cost in Wichita?",
             "Most fence repairs run between $250 and $800 depending on what failed and how much of the run needs work. A single broken picket is at the low end; multiple sister posts plus rail replacement lands mid-range; a storm-down section requiring partial rebuild reaches the higher end. We give you a written quote on site after seeing the damage."),
            ("Who pays for fence repair between neighbors in Kansas?",
             "In Kansas, fence-repair responsibility generally depends on who owns the fence (which neighbor it's on their side of the property line), and what your local jurisdiction or HOA rules say. There's no automatic 50/50 split. Many neighbors split costs voluntarily when both yards benefit, but legally the owner is responsible unless an agreement says otherwise. Check your plat or property survey to confirm whose property the fence sits on."),
            ("Can a leaning fence post be repaired or does it need replacement?",
             "Depends on whether the post itself is structurally sound or rotted. If the post is fine but the concrete footing has shifted, we can often dig it out and re-set in fresh concrete. If the post has rot at ground level or has split, it needs to be pulled and replaced entirely. We tell you which one your situation is at the estimate."),
            ("How long does it take to repair a fence after storm damage?",
             "Single-section storm repairs are typically same- or next-day jobs when our schedule allows. After a major storm event (when many fences across Wichita are down at once), we prioritize by severity and try to get every storm-damage call assessed within 2-3 business days. For tree-on-fence damage, see the storm damage section above — we partner with Baker Tree Service for tree removal before we rebuild."),
            ("Do you offer emergency or same-day fence repair?",
             "When scheduling allows, yes. We aim for same- or next-day service for urgent situations (dog containment failure, security concerns, storm damage to a yard with kids or pets). Call us at (316) 285-9172 — text a photo if you can — and we tell you honestly whether we can get there today, tomorrow, or what the wait looks like."),
        ]),
        "schema": service_schema_with_faq(
            "Fence Repair",
            "https://www.warrenbrosfencing.com/services/fence-repair.html",
            "Cedar fence repair in Wichita, KS. Leaning posts, broken pickets, sagging gates, storm damage. Most repairs $250-$800. Same- or next-day service.",
            [
                ("How much does fence repair cost in Wichita?",
                 "Most fence repairs run between $250 and $800 depending on what failed and how much of the run needs work."),
                ("Who pays for fence repair between neighbors in Kansas?",
                 "Responsibility depends on who owns the fence and what local rules say. No automatic 50/50 split. Many neighbors split voluntarily, but legally the owner is responsible unless an agreement says otherwise."),
                ("Can a leaning fence post be repaired or does it need replacement?",
                 "Sound posts with shifted footings can often be re-set. Rotted or split posts need to be pulled and replaced."),
                ("How long does it take to repair a fence after storm damage?",
                 "Single-section storm repairs are typically same- or next-day. After major storms with many fences down, we prioritize by severity and assess every call within 2-3 business days."),
                ("Do you offer emergency or same-day fence repair?",
                 "When scheduling allows, yes — for urgent situations like dog containment failures or storm damage. Call (316) 285-9172."),
            ]
        ),
    },
    {
        "filename": "services/gate-installation.html",
        "path_prefix": "../",
        "title": "Cedar Pedestrian Gate Installation in Wichita, KS — Warren Bros Fencing",
        "meta": "Cedar pedestrian gate installation in Wichita, KS — single walk-through gates, double-leaf yard gates, custom widths. Heavy-duty hinges and hardware. Free in-person estimates.",
        "canonical": "https://www.warrenbrosfencing.com/services/gate-installation.html",
        "h1": "Cedar Pedestrian Gate Installation in Wichita, KS",
        "h1_kicker": "Walk-through gates &middot; Yard gates &middot; Hardware upgrades",
        "lede": "Single walk-through gates and double-leaf yard gates built to match your existing fence. Pedestrian access only — we don't install driveway or vehicle gates.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Request a quote",
        "body": GATE_BODY + faq_html([
            ("How much does a fence gate cost installed?",
             "Cedar gates run $650 to $950 installed, depending on whether it's a standalone gate job or built into a full fence install. Heavy-duty hinges, latch, and optional drop rod for double gates are included. Single walk-through (3-4 ft) or double-leaf yard gates (6-8 ft) for mower or equipment access."),
            ("Single walk-through or double-leaf yard gate — which one?",
             "Single 3-4 ft walk-through covers normal yard access. Double-leaf 6-8 ft makes sense if you need to get a mower, zero-turn, or wheelbarrow through. Most properties have one of each."),
            ("How wide should a gate be for a riding mower?",
             "Most riding mowers fit a 5-6 ft single gate; zero-turns with wider decks may need a 6-8 ft double-leaf. Confirmed at the in-person estimate."),
            ("Can you replace just a gate without the whole fence?",
             "Yes — common job. We match the new gate to your existing fence's picket style and stain. Gate post often needs reinforcement too."),
            ("Do you install driveway or electric gates?",
             "No — pedestrian gates only. We can refer a contractor who specializes in driveway and electric gates."),
        ]),
        "schema": service_schema_with_faq(
            "Cedar Pedestrian Gate Installation",
            "https://www.warrenbrosfencing.com/services/gate-installation.html",
            "Cedar pedestrian gate installation in Wichita, KS. $650-$950 installed.",
            [
                ("Cost?", "Cedar gates $650-$950 installed."),
                ("Single or double?", "Single walk-through for pedestrian; double-leaf for equipment."),
                ("Width for mower?", "5-6 ft single or 6-8 ft double."),
                ("Replace just a gate?", "Yes — matched to existing fence."),
                ("Driveway/electric?", "No — pedestrian only."),
            ]
        ),
    },
    {
        "filename": "services/fence-removal.html",
        "path_prefix": "../",
        "title": "Fence Removal &amp; Tear-Out in Wichita, KS — Per-Job Pricing | Warren Bros Fencing",
        "meta": "Fence removal and tear-out in Wichita, KS. Pull failing wood, chain-link, or vinyl fences — posts, concrete footings, debris included.",
        "canonical": "https://www.warrenbrosfencing.com/services/fence-removal.html",
        "h1": "Fence Removal and Tear-Out in Wichita, KS",
        "h1_kicker": "Per-job pricing &middot; Bundled with new install",
        "lede": "Pull out the old fence — posts, concrete footings, and debris. Often bundled at a discount with a new install on the same line.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Get a written quote",
        "body": REMOVAL_BODY + faq_html([
            ("How much does old fence removal cost in Wichita?",
             "Priced per job. Factors: fence type, post type, linear footage, concrete footings, disposal needs, truck access. Quoted on-site. Often bundled at a discount with a new install."),
            ("Do I need a permit to remove a fence in Wichita?",
             "Most residential removals don't require a city permit, but your HOA may have rules. Check before scheduling."),
            ("Can you remove chain-link or vinyl fence too?",
             "Yes. Cedar, treated wood, chain-link, vinyl, and wrought-iron fences."),
            ("What happens to the old fence material?",
             "We haul it away. Wood to construction debris, metal to scrap recycling, vinyl to disposal."),
            ("Do you remove the concrete footings?",
             "Yes. Concrete footings are part of the standard removal scope."),
        ]),
        "schema": service_schema_with_faq(
            "Fence Removal and Tear-Out",
            "https://www.warrenbrosfencing.com/services/fence-removal.html",
            "Fence removal and tear-out in Wichita, KS.",
            [
                ("Cost?", "Priced per job, quoted on-site."),
                ("Permit?", "Usually no city permit; HOA may apply."),
                ("Chain-link or vinyl?", "Yes — all common materials."),
                ("Material disposal?", "We haul it away."),
                ("Footings?", "Yes, included in standard scope."),
            ]
        ),
    },
    {
        "filename": "faq.html",
        "path_prefix": "",
        "title": "Fence FAQ — Cost, HOA, Gates, Repair &amp; More | Warren Bros Fencing, Wichita KS",
        "meta": "Common questions about cedar fence installation, repair, gates, HOA approval, pricing, and timelines in Wichita, KS.",
        "canonical": "https://www.warrenbrosfencing.com/faq.html",
        "h1": "Frequently asked questions",
        "h1_kicker": "Honest answers to what Wichita homeowners ask us most",
        "lede": "Cost, HOA approval, gates, repair, storm damage, timelines — the questions we field over and over, answered straight.",
        "cta_primary": "Call (316) 285-9172",
        "cta_secondary": "Request a free estimate",
        "body": FAQ_BODY,
        "schema": faq_page_schema(FAQS_DATA),
    },
]


def main():
    os.makedirs(os.path.join(BASE, "services"), exist_ok=True)
    for page in PAGES:
        html = build_page(
            filename=page["filename"],
            title=page["title"],
            meta_description=page["meta"],
            canonical_url=page["canonical"],
            h1=page["h1"],
            h1_kicker=page["h1_kicker"],
            hero_lede=page["lede"],
            hero_cta_primary=page["cta_primary"],
            hero_cta_secondary=page["cta_secondary"],
            body_html=page["body"],
            schema_json=page["schema"],
            path_prefix=page["path_prefix"],
        )
        out_path = os.path.join(BASE, page["filename"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"OK {out_path}  ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
