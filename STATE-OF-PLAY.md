# Warren Bros Fencing — State of Play

**Last updated:** 2026-06-01 (Local Search Audit run + acted on; all pages indexing-requested; Citation Builder cost decision made; location-pages decision)
**Single source of truth for Warren Bros operational state.** Updated automatically by Claude as changes happen. If something's not in here, it's not load-bearing.

---

## Business basics

- **Legal entity:** Warren Bros Fencing LLC (Kansas single-member LLC, Grant Warren sole owner — brother Alex Warren is labor partner on installs, NOT on the LLC)
- **Founded:** 2021
- **Domain:** warrenbrosfencing.com
- **Phone:** (316) 285-9172 (Quo / OpenPhone, port from prior carrier COMPLETE as of 2026-05-26)
- **Canonical address:** 9562 W Brookridge Circle, Wichita, KS **67205** (5-digit ZIP — dropped the +4 on 2026-05-30; ZIP+4 adds nothing for NAP/SEO and the goal is to match GBP, which shows 5-digit. Street is "Brookridge Circle" spelled out to match GBP/BrightLocal live — no drift alert fired on it. Older notes said "W BROOKRIDGE CIR / 67205-1439"; superseded.)
- **Email:** grant@warrenbrosfencing.com (Resend + Gmail Send-Mail-As configured)
- **Primary categories:** Fence contractor, fencing installation, fence repair, gate installation
- **Service area:** Wichita, Derby, Andover, Bel Aire, Maize, Park City, Goddard, Haysville, Valley Center, Rose Hill, Augusta, Kechi, Mulvane, Colwich
- **Pricing reference:** $40-$55 per linear foot installed for 6-foot cedar privacy fence
- **Gate pricing (CONFIRMED 2026-05-27):** $650-$950 installed, depending on whether it's a standalone gate job or built into a full fence install
- **Install duration (CONFIRMED 2026-05-27):** Standard residential fence installs take 2-3 days. Larger jobs (200+ linear feet, multiple gates, slope work, tear-out) can take 3-5 days.
- **Hours (CONFIRMED 2026-05-27, verified from GBP):** Open 7 days a week (Sunday through Saturday), 7:00 AM - 5:00 PM. This has always been the operating schedule. The Mon-Sat-closed-Sunday text I had on the site previously was wrong — corrected 2026-05-27. **Don't ask about hours again; this is the canonical schedule.**

---

## Playbook phase status

### Confirmed DONE

| Phase | Item | Notes |
|---|---|---|
| 1-3 | Discovery, market research, brand identity | Logo, colors, tagline locked |
| 4 | Domain purchase | warrenbrosfencing.com via GoDaddy |
| 5 | Website cloned + adapted | Single-page site currently |
| 6 | Cloudflare DNS, Pages, apex→www Bulk Redirect | Account-level bulk redirect rule live |
| 6.5 | Google Search Console + sitemap | Sitemap submitted, indexed |
| 6.6 | GA4 + Cloudflare Web Analytics | Both active |
| 7 | Web3Forms quote form | Active on site |
| **8** | **Resend outbound + Gmail Send Mail As** | **Done for @warrenbrosfencing.com (confirmed 2026-05-26)** |
| 9 | Quo phone (316) 285-9172 | Live, carrier port COMPLETE (2026-05-26) |
| 13 | EIN obtained | Confirmed 2026-05-26 |
| 10 | Facebook Business Page | Active |
| 10 | Instagram | Active |
| 10 | Nextdoor Business | Active |
| 11 | Google Business Profile claimed + optimized | 4 reviews, 5.0 stars, USPS-canonical address |
| **11.3** | **GBP weekly Posts cadence — calendar reminders set** | **Confirmed 2026-05-26** |
| 11.7 | **Looker Studio monthly reporting dashboard** | **Built — confirmed 2026-05-26** |
| 11.10 | Semrush MCP integration | Connected to Claude |
| 11.11 (partial) | AI search optimization | llms.txt + Content-Signal robots + schema deployed |
| 12 | **QR code + business cards** | **Printed — confirmed 2026-05-26** |
| 13 | LLC formation | Warren Bros Fencing LLC, Kansas |
| — | Apple Business Connect | Confirmed visible/managed |
| — | Bing Webmaster Tools | Confirmed managed |
| — | Yelp profile | Manually created by Grant in prior session; photos added 2026-05-26 |
| — | Houzz free profile | Built 2026-05-26 (partial — logo, NAP, Cathy Conn project, business description) |
| — | BBB free profile | Live 2026-05-25 (needs enhancement — see pending) |

### DEFERRED (waiting on something)

| Phase | Item | Blocked by |
|---|---|---|
| — | (Previously: BrightLocal — now UNBLOCKED 2026-05-26 as phone port complete; see Pending section) | — |

### Confirmed PENDING (work to do)

| Phase | Item | Effort | Priority |
|---|---|---|---|
| 11.4 | **More Google reviews** (now **6** → target **30**) | Text past customers, ~30 min | **#1 LEVER, confirmed by 01 Jun Local Search Audit** (zero prereqs). Audit GBP pack: Warren Bros has 5.0★ + 59 photos but only **6 reviews** while every Map-Pack competitor has 20–220 (Midwest 220, Glenn 111, Bob's 85, Fencing Wichita 83). This single gap is why we're >50 in the pack. Recency already reset (review 2026-05-29). Target 30. |
| 11.5 | **BrightLocal/Whitespark citation push** — phone port complete, unblocked 2026-05-26 | 2-4 hours setup + 2-4 weeks propagation | **HIGH — newly unblocked** |
| 11.8 | **Blog content** — long-tail Q&A posts. STRICTLY requires `/blog/` directory with individual post sub-pages (each post needs its own URL to be indexed + share-able). Does NOT strictly require the full multi-page rebuild. | First post setup: 2-3 hrs (template + first post). Each additional post: 1-2 hrs. | High |
| ~~Service-specific pages~~ | **BUILT 2026-05-27** — generated via `build_pages.py`: `/services/cedar-privacy-fence.html`, `/services/fence-repair.html`, `/services/gate-installation.html`, `/services/fence-removal.html`, plus `/services/index.html` overview. Sitemap updated. **Pending: deploy to Cloudflare + replace Web3Forms placeholder key in contact.html.** |
| ~~Standard internal pages~~ | **BUILT 2026-05-27** — `/about.html` and `/contact.html` generated. Awaiting deploy. |
| ~~Replace Web3Forms placeholder key~~ | **DONE 2026-05-30** — contact.html now carries a real key (`3457639e-cfb1-4a69-8945-7bfb44c09b44`), verified live. Test submit 2026-05-30 confirmed lead delivery to gowarren88@gmail.com — form fully working. | — |
| ~~Deploy 7 new HTML files + sitemap~~ | **DONE 2026-05-30** — Grant redeployed; contact.html + homepage verified live. | — |
| — | **(Optional) Update index.html nav** to link to new pages instead of in-page anchors | 10 min | Low — footer links work too |
| 11.6 | **Wichita Regional Chamber of Commerce** | $250-400/yr | Medium (good backlink + referrals) |
| — | **BBB free profile enhancement** (claim today, fill in next session — task #40) | 15-30 min | Low |
| — | Verify Apple Business Connect is fully optimized (vs. just visible) | 10 min | Low |
| — | Verify Bing Places business listing is fully optimized (vs. just Webmaster Tools) | 10 min | Low |
| ~~AI Overview check for "warren bros fencing"~~ | DONE 2026-05-26 — Grant screenshot Googled from Wichita; Warren Bros own site at position 1 organically, GBP knowledge panel at position 0, no AI Overview brand-collision problem. Same pattern verified for Cowtown and Baker. Brand reclamation NOT NEEDED across any of the three service businesses. |
| 11.6 | BNI chapter membership (optional) | ~$650/yr | Low |
| 11.6 | Supplier preferred-contractor page submissions | Per supplier, free | Low |

### Status UNKNOWN (need to verify or capture next time it comes up)

| Item | Why unknown |
|---|---|
| **General liability insurance** | **PENDING — not yet bound. Required for fence installs. Confirmed pending 2026-05-26.** |
| Workers comp insurance | NOT PURSUING — Grant's call 2026-05-26. Don't raise unless Grant brings it up. |
| Bookkeeping system | **TABLED 2026-05-26** — revisit later |

---

## Decisions locked (rules of operation)

- **Paid marketing philosophy:** Aggregator pay-to-rank is OUT (Angi Pro, HomeAdvisor leads, Houzz Pro, etc.). When ready for paid marketing, use LSA → Google Ads → Meta Ads in that order.
- **Citation work deferred until phone port complete.** No BrightLocal until port is confirmed by both carriers.
- **No self-serving aggregateRating in JSON-LD schema.** GBP rating already feeds Google via the GBP listing — duplicating in schema gets flagged.
- **Reviews are the actual AI-citation unlock.** Submission to aggregators is necessary but not sufficient.
- **Brand voice is "I" / "we" — brothers Grant and Alex.** Public marketing says family-owned; LLC paperwork is Grant solo.

---

## What got corrected (so we don't repeat)

- **Brand reclamation lever (2026-05-26):** Initially flagged as a major gap based on Semrush position 34-38 for "baker tree service" type queries. Debunked same day — Grant's localized Google search showed Warren Bros at position 1 organically with knowledge panel at 0. The Semrush data was non-localized desktop, not what local customers actually see. **No brand reclamation work needed for Warren Bros.**
- **Aggregator submission scope (2026-05-26):** Initial audit recommended 8 aggregator submissions including Houzz Pro, Expertise.com, Angi, HomeAdvisor. Reduced to organic-functional only (Yelp, GBP, Apple Business, Bing, Nextdoor, Facebook, BBB free) after live verification that the rest are pay-to-rank.
- **Yelp listing origin (2026-05-26):** Initially assumed the existing Yelp listing was auto-scraped by Yelp's data ingestion. Wrong — Grant manually created it in a prior session. The lesson: don't assume the origin of a stub listing; ask.

---

## Semrush organic baseline (as of 2026-05-26)

Use as the baseline for measuring lift from future content + review work.

| Keyword | Position | Search vol | Estimated traffic |
|---|---|---|---|
| fence installation wichita | 28 | 50/mo | 0% (page 3) |
| fence companies in wichita kansas | 34 | 140/mo | 0% (page 4) |

No other keywords ranking in Google's top 100 currently. Branded queries ("warren bros fencing") rank position 1 with knowledge panel — confirmed via Grant's localized search 2026-05-26.

---

## Related docs

- **Full AI Search Audit:** `Projects/Playbook/AI-SEARCH-AUDIT-2026-05-26.md` — has detailed findings + recommendations across all 3 Grant service businesses
- **Master Launch Playbook:** `Projects/Playbook/LAUNCH-PLAYBOOK.md` — methodology source of truth
- **Ebook update queue:** `Projects/.shared-memory/pending_ebook_updates.md` — pending Trade Up book integrations

---

## Citation history

- **Yelp listing** — Manually created by Grant in a prior session (NOT auto-scraped, NOT BrightLocal). NAP, categories, hours, specialties description all filled in by Grant previously. Photos added 2026-05-26.
- **BBB listing** — Auto-generated free profile went live 2026-05-25. Grant has portal access (BBB ID 1000082401). Not yet enhanced — see task #40.
- **BrightLocal mass citation push** — NEVER RUN. Deferred until phone port complete. Once port confirms, this is the next major lever.
- **Whitespark** — Not run. Same defer.

---

## Recent activity log

- **2026-06-05:** **B&B Lumber material pricing captured + cost calculator built.** Grant uploaded B&B Lumber Quote **#2606-664566** (created 06/05/2026, expired 06/08/2026, Wichita KS) — a 17-item cedar price sheet (per-unit, pre-tax). Built `Warren-Bros-Fence-Cost-Calculator.xlsx` (Calculator + Price List + Notes tabs): dropdown-driven material takeoff from linear feet/height → pickets, rails, posts, optional kickboard, +waste +7.5% tax, plus an optional quote estimator. Verified math (100 lf 6' privacy default = 176 pickets, 42 rails, 14 posts, **$2,074 total material ≈ $20.74/lf**). Key B&B prices on file: pickets 1x8x6' $4.72–6.36 / 1x8x8' $7.25–9.60; rails 2x4x8' $6.96 (S4S fence rail); posts metal U-8' $36.98 / terminal 2-3/8"x8' $18.75. **Also added Home Depot prices** (Grant's call 06/05): 4x4 cedar posts $11.98 (8') / $18.38 (10') / $21.68 (12'), Quikrete fast-set $4.68 (60 lb) / $6.24 (80 lb) — wired into the calculator (post dropdown + new concrete line @ ~2 bags/post). Note B&B quoted **no wood 4x4s**, only metal posts. **Prices are date-stamped — re-verify before bidding.** (B&B is Grant's named favorite supplier — see 11.6 preferred-installer pitch in backlink toolkit.)
  - **2026-06-05 (later):** **Bid Builder added** to the calculator (replaced the simple estimator). Proper cost+overhead+margin pricing: inputs for labor rate/crew/productivity, overhead %, target margin %, gates, and site adders (tear-out, rock/slope). Outputs labor cost, overhead, total cost, BID PRICE = cost/(1-margin), profit, bid/lf, and effective markup-vs-materials. At defaults (100 lf, 2-crew @ $60/hr, 25% OH, 30% margin) it lands at **$4,354.86 = $43.55/lf** (in the $35-50/lf Wichita benchmark), 2.37x materials. Notes tab documents the method. Sourced from web research (Angi/Jobber/FieldCamp) + eBook Ch5/Ch6. **Possible eBook addition:** explicit bid formula (materials+labor+overhead)/(1-margin) — eBook covers margins & secret-shopping but not the build-up formula. Offered to Grant.
  - **2026-06-05 (later 2):** **Branded quote PDF created** → `Warren-Bros-Fencing-Quote.pdf` in the Warren Bros folder. One-page, logo + slate(#3F485B)/orange(#E15204) brand palette (sampled from logo), fill-in customer/job-site fields, scope-of-work line items, $1,100 firm total, terms (30-day validity, change-order clause for bad footings, 1-yr workmanship warranty, 50% deposit option), acceptance signature block. Built for a sample repair job: remove 2 existing 4x4x10 concrete-set posts + install 2 new + reattach a large fence section. Generator: `outputs/build_quote.py` (reportlab). **Quoting-software shortlist given to Grant** (research Angi/Jobber/QuoteIQ/etc.): free/simple = Square Invoices / Joist / FieldFuze ($0, ~2.9% card fees); all-in-one = **Jobber ~$39/mo** or Housecall Pro; fence-specific = **QuoteIQ ~$30/mo** (AI estimator + map measure, Good/Better/Best) or Fence Cloud ~$99/mo. Recommended starting with Jobber or QuoteIQ. **Cross-business asset** — branded-quote template + quoting-tool shortlist apply to Baker, Cowtown, Wichita Well too; playbook has no quoting-tools section yet (gap to fill).
  - **Gotcha (build script - CONFIRMED RECURRING):** BOTH the Write AND Edit tools truncate files at ~13.6 KB, cutting off mid-line, every time the openpyxl build script grew past that size. Hit it 3x. Fix: after any Write/Edit on a large generator, run `ast.parse` to verify and repair the tail via a bash heredoc (heredoc writes don't truncate). Prefer building large files in chunks via bash rather than one big Write/Edit.
  - **Gotcha (calculator usage):** the Qty column (C24:C28) are live formulas. Grant typed a constant into the Posts Qty cell, which replaced the formula and stopped it updating with post-spacing changes. Symptom "formula won't update" = cell was overwritten with a value. Fix: re-enter Posts `=ROUNDUP($C$5/$C$11,0)+1`, Concrete `=ROUNDUP($C$14*C26,0)`. Tell Grant to only edit yellow input cells / dropdowns, not the white Qty column.
- **2026-06-01:** **Local Search Audit run in BrightLocal + acted on.** Scores: On-Site SEO **Good** (100/100 speed, 0 errors, 0 broken links, clean titles/desc/OG/schema, mobile 97 — site is excellent, leave it alone), GBP **OK**, Links & Authority **Poor**, Rank Tracker **Poor**. Three quantified gaps now in `RANK-ACTION-PLAN.md`: (1) **reviews 6 vs pack 20–220** = #1 lever; (2) **only 4 of 18 pages indexed** by Google (competitor avg 11); (3) **backlinks 5 links/4 domains vs 151/31, DA 4 vs 8.8** = weakest area. Note: this supersedes the 5/30 decision to "skip Local Search Audit" — running it once was worthwhile and confirmed the strategy. (Address-on-pages flagged red = intentional SAB hidden-address, not a problem.)
  - **Indexing FIXED (in progress):** root cause of 4/18 was inspecting/relying on auto-crawl. Grant ran **URL Inspection → Request Indexing on all pages** today (everything now indexed or requested). **Gotcha learned:** inspecting the **apex** (`https://warrenbrosfencing.com/`) shows "URL is not on Google → Page with redirect" + "No referring sitemaps detected" — CORRECT (apex 301s to www, sitemap lists www), inspect the **www** version. Captured to runbook Step 10 + eBook ch13. Recheck GSC Indexing→Pages in ~1 week; expect count well past 4.
  - **Citation Builder cost decision (real numbers now):** campaign screen = **35 Manual Submissions $112** (specific named directories, owned forever) + **All Aggregators $127.50** (−15%, upstream data networks → hundreds of downstream + voice/AI/GPS, 12-mo feed) + **Remove Duplicates $22.40**. All three = $261.90; manual+dupes only = **$134.40**. **DECISION: do the $134.40 core now, SKIP the $127.50 aggregators** until reviews/GBP built and citations proven. Toggle "Don't show address publicly" ON (SAB). Standard turnaround. (Supersedes the 5/30 ~$96/$60-credit estimate — these are the actual screen prices. NAP validation lockout from 5/30 has cleared — Grant reached the payment screen.)
  - **Location pages decision:** Warren Bros has **NONE**. Build **2-3 strong town pages** (Derby first, then Andover/Maize/Goddard — real demand + actual jobs only), mirroring WWP pattern, ⚠️ each genuinely unique (doorway-page trap = penalty), **AFTER reviews+indexing+citations** (organic is a smaller lever than Map Pack). Captured as new "Location pages" play in eBook ch24 + action plan Priority 2.
- **2026-05-30 (later 15):** **Backlink outreach PARKED for later** (Grant's call). Toolkit is fully built and ready at `backlink-outreach-toolkit.md` — nothing more to prep. **RESUME LATER:** (1) Grant sends the B&B Lumber preferred-installer pitch + a filled-in case study, (2) turn the storm-damage checklist into a 1-page PDF, pitch ~10 HOAs/PMs, (3) set up the Wichita Regional Chamber listing. This is the 11.6 local-backlink lever (top-5 ranking factor) — high value, just deferred, not dropped. When Grant's ready to do outreach, pick up from the toolkit.
- **2026-05-30 (later 14):** **Backlink outreach toolkit built** (`backlink-outreach-toolkit.md`) — kicks off the 11.6 local-backlink lever (top-5 ranking factor, previously untouched). Includes: (1) ready-to-send **B&B Lumber** preferred-installer pitch (Grant's named favorite supplier) + a one-page case-study template, (2) reusable HOA/property-manager email + the **"Storm-Damage Fence: First 48 Hours" checklist** content carrot, (3) news/HARO pitch template, (4) a backlink tracker table. Grant's next actions: fill the case study with a real job + send to B&B, pitch ~10 HOAs/PMs, set up the Chamber listing. Also flagged for ebook (Ch on backlinks) — the content-carrot pattern + storm checklist are reusable across Cowtown/Baker.
- **2026-05-30 (later 13):** **All 9 GBP posts done** (per Grant) — Post 1 live 5/30, Posts 2–9 scheduled on consecutive Mondays 8am through **Jul 20, 2026** (each promotes a blog guide via Learn More, except Post 9 = free-quote). GBP weekly cadence (11.3) now locked through late July, zero ongoing effort. After the queue runs out, rotate the 11.3 content mix (job photos, before/after, review screenshots) — noted in gbp-posts-queue.md. (Optional: Grant can screenshot "Your posts" if he wants the scheduled dates double-checked.)
- **2026-05-30 (later 12):** **GBP Post 1 PUBLISHED** (privacy fence cost guide, w/ cedar photo + "Learn more" → blog) via walkthrough — weekly GBP posting cadence (11.3) now ACTIVE. 8 posts left in `gbp-posts-queue.md`, ~1/week. Offered Grant a recurring weekly reminder to keep the cadence.
- **2026-05-30 (later 11):** **GBP Posts queue built** (`gbp-posts-queue.md`) — 9 ready-to-paste weekly GBP "Update" posts (Playbook 11.3 format: ≤300 char captions, CTA button, NO phone in text). 8 promote the new blog guides via Learn More buttons (drives traffic + freshness); 1 is a free-quote conversion post. Activates the weekly cadence that was set up 5/26. **Decision: SKIP competitor name complaints (11.4.i)** per Grant 2026-05-30 — don't re-raise. Grant to work the queue ~1/week (or walk through publishing the first live).
- **2026-05-30 (later 10):** **Redeploy DONE** — all 8 blog posts, the `/blog/` index, the "Guides" nav link on all 9 main pages, and the updated sitemap are now LIVE. Blog phase (11.8) complete. (Still deferred: fold blog + Guides nav into `build_pages.py` so a future regen doesn't wipe them — waiting on sandbox/VM.) Post-deploy: re-ping sitemap in GSC + request indexing on the new blog URLs.
- **2026-05-30 (later 9):** **7-day hours cross-platform sync CONFIRMED** (per Grant — "confirmed I believe"). The 5/27 open item ("update GBP + Yelp + Apple + Bing + BBB + Facebook to Open daily 7am-5pm") is closed. Website footer already showed the correct 7-day schedule. (Slight residual: Grant's "I believe" — a 30-sec GBP/Yelp spot-check could firm it to certain if it ever matters, but treating as done.)
- **2026-05-30 (later 8):** **3rd blog batch built — blog now = 8 posts.** Added `fence-installation-timeline-wichita.html` (2-3 day timeline + HOA-approval-is-the-real-wait), `best-time-to-install-fence-kansas.html` (seasonal, year-round, off-season scheduling), `cedar-vs-treated-pine-fence.html` (material comparison, expertise-based). Chosen to be distinct/non-cannibalizing (validated against `phrase_questions` for "fence installation" + "wood fence" — confirmed remaining topics are mostly DIY/other-materials, so picked evergreen expertise angles). All 3 with BlogPosting + FAQPage schema, cross-linked. Index (cards + schema) + sitemap updated. **Content base now comprehensive — 8 buyer-intent/expertise guides; honest call is this is a natural stopping point (further topics thin out into DIY/redundant).** ALL of batch 2+3 (5 posts) + Guides nav + index/sitemap PENDING ONE REDEPLOY to go live (first 3 posts already live).
- **2026-05-30 (later 7):** **2 more blog posts built** (`fence-repair-cost-wichita.html` $250-$800, `fence-replacement-cost-wichita.html` ~$4,500-$6,500/100ft) — data-validated from `phrase_questions`, consistent with the fence-repair + cedar service pages, each with BlogPosting + FAQPage schema. Added both to the blog index (cards + Blog schema) and sitemap. **Blog now = 5 posts.** Also added the "Guides" nav link to all 9 main pages earlier. **PENDING DEPLOY:** these 2 posts + index/sitemap updates + the Guides nav additions all need a redeploy to go live (the first 3 posts are already live). Next blog candidates in blog-content-plan.md.
- **2026-05-30 (later 6):** **AI Visibility baseline captured (free) + paywall hit.** Semrush AI → Visibility Overview for `warrenbrosfencing.com` returned **"Your brand isn't present on AI platforms yet"** = zero AI presence. That's the useful $0 "before" baseline on record (as predicted). Going to **Prompt Research threw a $199/mo "Semrush One Starter" upgrade paywall** — the trial does NOT include it. **Decision: did NOT pay.** Not worth $199/mo to measure near-zero AI presence while we build it; the levers that move it (citations Monday, reviews, the new blog) are already in flight, and blog-topic question data comes free from the `phrase_questions` keyword API. Revisit paid AI Visibility tracker in a few months once there's real AI presence to track. (Playbook note corrected — I'd assumed the toolkit was trial-usable.)
- **2026-05-30 (later 5):** **Blog launched (built, pending deploy).** Created `/blog/` = index + 3 long-tail Q&A posts matching the site template (header/footer/CSS/GA/schema): `privacy-fence-cost-wichita.html`, `fence-permit-wichita.html` (built on VERIFIED Wichita permit rules — web-searched: no city permit for ≤6ft back / ≤4ft front, over 6ft needs one, no good-neighbor requirement, HOA may be stricter), `cedar-fence-lifespan-kansas.html`. Each has BlogPosting + FAQPage schema. Topics from Semrush `phrase_questions` (cost ~2,400/mo; permit ~590/mo LOW competition 0.06; cedar lifespan ~320/mo). Added 4 URLs to `deploy/sitemap.xml`. Files live in `deploy/blog/`. Plan + next-batch topics in `blog-content-plan.md`. **OPEN FOLLOW-UPS:** (1) Grant deploys updated `deploy/` to Cloudflare (same as today's redeploy); (2) ⚠️ **`build_pages.py` does NOT include the blog yet** — re-running it would overwrite `deploy/` and DROP the blog; integrate the blog into the generator before any future regen (deferred — sandbox/VM was down); (3) add a **"Guides" nav link to the EXISTING pages** (index/services/about/contact/faq) — currently only the blog pages carry it, so the blog isn't reachable from the main site nav yet; (4) post-deploy: re-ping sitemap in GSC + run Google Rich Results Test on the 3 post URLs to confirm FAQPage/Article schema. (5) Couldn't run automated HTML/JSON parser (VM down) — integrity confirmed manually (no truncation), schema authored to match proven service-page pattern.
- **2026-05-30 (later 4):** GBP **"Fix product details" card = IRRELEVANT for Warren Bros (gotcha).** The Warren Bros GBP shows a generic "Fix product details — make fixes in Merchant Center so customers can find your products" suggestion card. Warren Bros is a service business with NO Google Shopping product feed, so Merchant Center doesn't apply — ignore/dismiss it. Clicking it opens Grant's existing Merchant Center account = **The MMA Mystic Marketplace** (ID 5747422399), whose feed issues (Missing color ×56, Missing age group ×28 on apparel) belong to a SEPARATE business. Don't mistake those for a Warren Bros task. (The MMA Mystic feed issues are real + worth fixing in that project — they hurt Shopping visibility for the shirts.)
- **2026-05-30 (later 3):** **ThreeBestRated — SKIPPED (decision).** Their new-listing form is a 4-step wizard requiring a PUBLIC physical address; Warren Bros is a SAB that hides the home address (GBP service-area mode), so submitting `9562 W Brookridge Circle` would expose it publicly. Combined with low odds (they handpick only top 3 per city via 50-point inspection; Warren Bros has 5 reviews vs established competitors), Grant chose to skip for now — revisit after the review count climbs. HomeGuide (pay-per-lead, free-profile-only) remains optional/unstarted. Pivoting to Semrush AI Visibility blog research.
- **2026-05-30 (later 2):** Grant started a **Semrush One free trial** — confirmed via screenshot, the AI Visibility toolkit is now accessible (AI Analysis: Visibility Overview / Competitor Research / Prompt Research; Brand Performance: Perception / Narrative Drivers / Questions; Boost & Monitor: Site Audit / Prompt Tracking / Content Creation). **Time-limited trial → will convert to paid (~7 days, card on file) — Grant to watch the renewal date / cancel if not keeping.** Use while live for: (a) AI-visibility BASELINE for Warren Bros (measure lift later), (b) **Prompt Research / Questions to source the long-tail blog Q&A topics** (data-driven topic selection instead of guessing — feeds the blog-content workstream). Directly advances the standing AI-search-ranking priority.
- **2026-05-30 (later):** Grant got a new Google review → **now 5 total**; key point is it resets the recency signal (prior most-recent was ~10 months old — the bigger penalty). Grant **redeployed the site** — verified live via browser: contact.html live with a REAL Web3Forms key (`3457639e-cfb1-4a69-8945-7bfb44c09b44`, placeholder resolved → contact-form blocker closed); homepage live. **Schema ZIP+4 follow-up RESOLVED** — homepage schema uses city/state-only PostalAddress (Wichita, KS, no ZIP), correct for a SAB; no stale +4. Contact form **CONFIRMED WORKING 2026-05-30** — Grant ran a live test submit; lead arrived in gowarren88@gmail.com ("[WARRENBROS] New quote request"), so the form delivers leads correctly. Contact form fully closed out (deployed + real key + verified delivery).
  - **GSC /home 404 CONFIRMED FIXED 2026-05-30:** checked live — `warrenbrosfencing.com/home` now 301-redirects to `/` (homepage), and GSC Page Indexing shows the "Not found (404)" reason with Validation = **Started** (recheck in progress). No action needed; it'll clear / reclassify as a benign "page with redirect." Supersedes the 5/29 note that listed the redirect as a TODO — it was already done. (The other two 5/29 reasons — "Alternate page w/ canonical tag" ×2 and "Page with redirect" ×1 — also show Validation Started; both benign.)
- **2026-05-30:** Grant confirmed he wants BrightLocal actively running NAP consistency + monitoring (incl. pushing on the Apple connection, not leaving it manual). BrightLocal support email (Rhea Mae Manulat, ticket **721854**, 2026-05-29) confirms the **Apple Maps connection is failing with no specific error**; Location Manager config reviewed as correct; **escalated to their Technical Team**. This is the same SAB silent-fail diagnosed 2026-05-27 — set expectation honestly that Apple likely stays manual (Apple doesn't support SAB connections; direct ABC listing is authoritative + live). **Outstanding to fully satisfy "BrightLocal does the NAP thing":** Citation Builder mass push (NEVER RUN — now unblocked, the real NAP lever) + Citation Tracker monitoring. Active Sync already live for GBP/Facebook/Bing (3/5).
  - **Session progress 2026-05-30:** Cleared all 8 Location Change Alerts (per-row: Accepted description [fixed an OLD phone (316) 974-1813 stored in BrightLocal's description → corrected to canonical (316) 285-9172], opening date, English attribute; Rejected the rest to keep canonical https + branded social URLs). **Canonical ZIP changed +4 → 5-digit `67205`** to match GBP (decision logged in canonical files). Filled missing **Bing categories** (primary Fence Contractor + 1 additional). Clicked Save and Sync → **NAP validation lockout triggered (yellow banner, 2026-05-30 05:08)** — all Location Manager toggles greyed, no further update requests allowed until BrightLocal validates. **Citation Builder DEFERRED until validation clears** (don't push citations with NAP pending validation; took ~1-3 days to clear after the 5/27 lockout). RESUME: when validation clears (toggles green again / BrightLocal email), run Citation Builder (aggregators + top 25-30 dirs, ~$96 card / ~$60 credits — Grant pays) → then Citation Tracker → set +30/+60-90 day re-audit reminder. Also pending: check site schema for leftover ZIP+4 (site files not in this session).
  - **BrightLocal module decisions 2026-05-30 (so we don't re-litigate):** USING — Location Manager, Rankings/Rank Tracker, AI Insights, Citations (Builder+Tracker, pending validation), and Reputation/reviews is the one optional high-value module still open (reviews = Warren Bros' #1 ranking lever). SKIPPING — GBP Post Scheduler (Grant already runs GBP posts on his own calendar cadence, redundant), GBP Audit / Local Search Audit (one-off, overlap AI Insights + Citation Tracker), Google Analytics connect (low value), White-label Settings (agency/client-reporting only, N/A for own businesses).
- **2026-05-29:** Warren Bros GSC Page Indexing review. 4 not-indexed pages flagged across 3 issue types: (1) Alternate page with proper canonical tag (2 pages — usually correct behavior), (2) Not found 404 = `warrenbrosfencing.com/home` first detected 9/3/24 (~2-year-old stale URL from prior template/link), (3) Page with redirect (1 page — likely apex→www artifact). **Fix for the 404:** add Cloudflare Redirect Rule `/home → /` then click Validate Fix in GSC. Other two issues likely benign; verify after deep-dive.
- **2026-05-28 (BrightLocal continuation):** Rank Tracker configured with 15 local-intent keywords (cedar fence installation wichita, fence repair wichita, gate installation wichita, etc. — match service pages + GBP services + AI Insights recs). HTTPS URL canonical. Weekly auto-scan. Old generic-keyword data was misleading (avg 46.1) — new baseline will reflect actual local performance. **Local Search Grid baseline established: "fence installation" avg map rank 13.2 in Wichita on 2026-05-28** (was 15.3 day before — noise). Most of map is RED (Warren Bros invisible from most search points). Top competitors all have 25-220 reviews vs Warren Bros' 4 — review gap is biggest single ranking lever. Trial limits prevent scanning more keywords on the grid; revisit post-trial if paying for Manage tier.
- **2026-05-27 (later 5):** BrightLocal Location Manager setup partial. Connected + Active Sync turned on for GBP + Facebook + Bing (3/5 Connected, 3/5 Active Sync). Apple Maps Connect SILENT FAIL — Apple Business Connect listing exists and is live, but BrightLocal can't connect; likely because Warren Bros is a Service-Area Business and Apple Maps doesn't support SAB connections (verified via research). Apple stays manual. Yelp gated to paid Active Sync Plus. Canonical NAP entered (9562 W BROOKRIDGE CIR, WICHITA KS 67205-1439, (316) 285-9172, https://, 02/2022 opening, Fence Contractor primary). Save and Sync clicked — **BrightLocal validation in progress** (yellow banner: "Changes to Name, Address, Phone, Primary Category or Website URL require additional validation"). All Location Manager toggles greyed during validation lockout. 4 Location Change Alerts still pending — will clear when validation completes. **Tomorrow: revisit BrightLocal — Citations / Citation Tracker / Citation Builder / Reputation / GBP module / Local Search Audit / Google Analytics / White-label Settings / Rankings.** Wrong phone number in GBP description was fixed directly on GBP earlier (canonical is (316) 285-9172).
- **2026-05-27 (later 4):** GBP services audit + cleanup. Was ~50 entries (cross-business pollution from Cowtown: Dumpster Rentals, Junk Removal, Lawn Care; services Grant doesn't offer: vinyl, chain link, iron, wrought iron, metal, pressure washing, painting, staining; ~15 junk/vague/duplicate/typo entries: Fence Type, Fence Posts, Personalized Solutions, Fence Repair Repairing, etc.). Pruned to **7 clean services**, all with 250-290 char descriptions: Fence installation, Privacy fence installation, Wood fence installation, Cedar Privacy Fence, Fence removal, **Gate Installation (new)**, **Emergency Fence Repair (new)**. Pending Google review (~1 day). Discovered via BrightLocal AI Insights scrape. **Playbook §11.4.d + ebook Ch 19 updated in real time with corrected guidance** — previous advice was "toggle ON every Google-suggested service" which is exactly what created the bloat. **Same audit needed for Cowtown + Baker — task #57 created.**
- **2026-05-27 (later 3):** BrightLocal free trial started + AI Insights scraped via Chrome MCP. 5 recommendations identified: REVIEWS (PRIORITY — 4 reviews, last 10 months ago), CONTENT (suburb pages + emergency-fence-repair-wichita page), BACKLINKS (8-12 quality local links), CITATIONS (60.53% of general directories show no listing), GBP (report competitor "Fencing Wichita KS" for keyword-stuffed name via Google Business Redressal).
- **2026-05-27 (later 2):** Hours changed to open 7 days/week 7am-5pm (was Mon-Sat 7am-5pm, closed Sunday). Site footer + contact page updated. **Grant still needs to update GBP + Yelp + Apple Business + Bing Places + BBB + Facebook hours to match the new 7-day schedule.**
- **2026-05-27 (later):** Service pages rebuilt with full SEO optimization after Semrush keyword research + Grant clarifications. All 4 service-page H1s now include "Wichita, KS" (previously missing on 3). Cedar pricing corrected to $40-$55/linear foot. Repair pricing corrected to $250-$800. Storm damage section added to fence repair with Baker Tree Service partnership link (Option A — direct partnership at (316) 409-1144). Driveway gates removed entirely from gate page (Grant doesn't do these). HOA section added to cedar privacy fence (provides specs only, doesn't submit paperwork). Per-job pricing language for fence removal. FAQPage schema added to all 4 service pages with 5 FAQs each. Pages regenerated via build_pages.py. **Pending: redeploy to Cloudflare.**
- **2026-05-27 (initial):** 7 new HTML pages built + deployed to Cloudflare (about, contact, services overview, 4 individual service pages). Sitemap.xml updated with all 8 URLs. Contact form uses existing Web3Forms key. Site is now multi-page architecture (previously single-page index.html only).
- **2026-05-26 (late evening):** Phone port confirmed COMPLETE → BrightLocal now unblocked. EIN confirmed obtained. General liability insurance confirmed pending (not yet bound). Bookkeeping system tabled.
- **2026-05-26:** Yelp photos uploaded. Houzz free profile created (partial). BBB free profile live. AI search audit completed. Semrush MCP-based organic data pulled. Brand reclamation lever debunked.
- **2026-05-25:** BBB free profile auto-generated and went live.
- **Earlier:** GBP optimization, Apple Business Connect, Bing Webmaster, llms.txt deployment, Cloudflare Bulk Redirect setup.

---

## Open questions Claude has

These are gaps in Claude's knowledge that someone (Grant or future-Claude) should fill in next time the topic comes up:

1. ~~Phone port status~~ — COMPLETE confirmed 2026-05-26
2. ~~EIN obtained~~ — CONFIRMED 2026-05-26
3. General liability insurance carrier + coverage? — still PENDING, not yet bound
4. ~~Workers comp~~ — NOT pursuing per Grant's call 2026-05-26. Removed from open questions.
5. BrightLocal has never been run. Now UNBLOCKED — when does Grant want to schedule?
6. Bookkeeping system — TABLED, revisit later.
