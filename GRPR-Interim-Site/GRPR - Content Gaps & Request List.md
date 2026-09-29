# GRPR Interim Site: Content Gaps & Request List
grprpublicaffairs.com · September 28, 2026

## 1. What's built

There are 12 pages, all plain HTML. They're mobile-tested from 320 to 768 px wide.

| Page | File | Status |
|---|---|---|
| Home | `index.html` | Built. A hero slider (GA + PR together, then Government Affairs, then Public Relations, with pencil-sketch images), then services, stats, integrated solutions, sample engagements, latest insights, team, testimonial and a call to action. **Stats, engagements and the testimonial are mocked.** |
| Government Affairs | `government-affairs.html` | 3 of 5 capabilities are real. **2 are placeholders.** |
| Public Relations | `public-relations.html` | 3 of 5 capabilities are real. **2 are placeholders.** |
| Crisis Command | `crisis-command.html` | **Complete.** Full content adapted from the grayreed.com crisis page, with the GRPR disclaimer. |
| GRIDS | `grids.html` | **Complete.** Full content adapted from the grayreed.com Data Centers page: G-R-I-D-S sections, 9 matters and the disclaimer. |
| Our Team | `team.html` | 4 real people, plus 1 placeholder. **No headshots or bio links yet.** |
| Insights | `insights.html` | 9 real items linking to grayreed.com: 5 articles and 4 press releases. **3 placeholder videos.** |
| Video pages | `video-rylander-01/02/03.html` | Template is ready. **The videos, titles, summaries and transcripts are all missing.** |
| Why GRPR | `why-grpr.html` | Built from your page. It's now first in the navigation on every page. **Needs:** confirmation of the client mix in "Who we are", recognition beyond Capitol Inside 2025 (C4), and headshots and bio links (A1, A2). |
| Contact | `contact.html` | Layout is done. **The form doesn't submit yet, and the offices are placeholders.** |

---

## 2. Content to send

These are grouped by who will likely have them. The priority column says what should be in place before launch.

### A. People — Marc / Adam / marketing
| # | Item | Where it appears | Priority |
|---|---|---|---|
| A1 | Headshots, ideally 4:5 portrait, for Adam Leggett, Alyssa Villarreal, Marc Rylander and Charlie Rose | Home, Team, service pages, Crisis Command, GRIDS | **Must** |
| A2 | Bio link or bio text for each person | Same | **Must** |
| A3 | Third PR team member, for example Elizabeth Scott: name, title, email, phone, headshot. If there isn't one, I'll remove the card. | Team | **Must** |
| A4 | Titles and headshots for the Crisis Command attorneys J.J. Hardig, Gabe T. Vick and Chris Davis. They currently show as just "Gray Reed." | Crisis Command | Should |
| A5 | Emails, phone numbers and headshots for Stephen Cooney and Ned Crady | GRIDS | Should |
| A6 | Optional v4 profile fields for each person: "What clients hire me to do," industries served, representative engagements, media and speaking | Team (future profile pages) | Later |

### B. Service copy — Adam (GA) and Marc (PR)
| # | Item | Current placeholder text | Priority |
|---|---|---|---|
| B1 | Government Affairs, **Regulatory & Agency Engagement** (2–3 sentences) | "representation before state agencies, boards and commissions…" | **Must** |
| B2 | Government Affairs, **Coalitions & Stakeholders** (2–3 sentences) | "building and managing coalitions, associations and allied voices…" | **Must** |
| B3 | Public Relations, **Executive Visibility** (2–3 sentences) | "thought leadership, speaking, bylines…" | **Must** |
| B4 | Public Relations, **Digital & Social** (2–3 sentences). If this isn't offered yet, I'll remove it. | "social strategy, content calendars…" | **Must** |
| B5 | Review the existing GA and PR copy, which came from the current GRPR site, and the hero slide headlines | All pages | Should |

### C. Proof points — Marc / Adam
| # | Item | Where | Priority |
|---|---|---|---|
| C1 | **Four real stats.** The current ones are illustrative: 20+ years of public service, 15+ years of legislative tracking, 100+ engagements, 50+ clients. | Home | **Must**, or remove the block |
| C2 | **Three client stories**, one line each for Challenge, Strategy and Outcome. They can be anonymized, for example "Statewide trade association." The current placeholders are a public university, a trade association and a critical infrastructure operator. | Home | **Must**, or remove the block |
| C3 | **One testimonial**, with the client's approval | Home | Should, or remove |
| C4 | Recognition beyond Capitol Inside 2025, such as awards or legislative recognition | Why GRPR (Recognition) | Should |
| C5 | Legislative wins and regulatory success stories. The v4 doc calls this "the most important missing section." | Government Affairs | Later (Phase 2) |

### D. Insights and video — Marc / marketing
| # | Item | Priority |
|---|---|---|
| D1 | **The Marc Rylander videos.** For each: YouTube (or other) link or ID, title, date, 1–2 sentence summary, and ideally 3 takeaways and a transcript. **I couldn't find these on grayreed.com.** The Videos section there only lists Andy Landry and AI in Agriculture, and site search for "Rylander" returns only the Crisis and Data Centers pages. | **Must**, or hide the video block |
| D2 | Any GRPR-authored articles, policy alerts or media appearances beyond the 5 articles already linked | Should |
| D3 | Confirm the 9 linked items are the right set. Articles: TWDB water-use directive; From HR Problem to PR Crisis; Data Centers and Water Collide; Governor's data center policy shift; Legislature targets data center growth. Press releases: GRIDS launch; Capitol Inside 2025; Adam Leggett joins; Marc Rylander / GRPR launch. | Should |

### E. Contact and legal — marketing / GC
| # | Item | Priority |
|---|---|---|
| E1 | Office addresses to show: Austin? Dallas? Houston? | **Must** |
| E2 | General inquiry email and phone | **Must** |
| E3 | Where form submissions go: a HubSpot form embed code, or an email address | **Must** |
| E4 | Privacy Policy and Disclaimer: URLs, or text for GRPR's own pages | **Must** |
| E5 | GRPR LinkedIn URL | **Must** |
| E6 | **Compliance sign-off** on Crisis Command and GRIDS. These pages describe Gray Reed legal services and matters on the GRPR domain, and include the GRPR privilege disclaimer. | **Must** |

---

## 3. Decisions for you

1. **GRIDS letter G.** The April press release says "Government Relations." The current Data Centers page says "Government Affairs & Public Relations." I used the Data Centers wording.
2. **Blocks to remove if content isn't ready.** Stats, sample engagements, the testimonial and videos. Launching without them is cleaner than launching with placeholders.
3. **How much of v4 to include in the interim site** (see §5). "Why GRPR" is now built. My recommendation: leave the rest for the full rebuild.

---

## 4. Launch items (technical)

| Item | Note |
|---|---|
| Logos | They currently load from the old WordPress site. **Download `grpr-logo-color.svg`, the Gray Reed Advisory logo and the Gray Reed logo into `/assets`** before WordPress is retired. The README lists exact URLs. |
| Hero photos | Three Unsplash photos (free license): Austin skyline, Texas Capitol, Dallas bridge. Download them into `/assets/img` or swap in firm photography. |
| Font | License the Gibson web font for grprpublicaffairs.com. Figtree is the fallback until then. |
| Redirects | 301-redirect the old WordPress URLs, for example `/government-affairs/` and `/public-relations/`, to the new pages to keep search rankings. |
| Analytics | GA4 and/or the HubSpot tracking code. |
| SEO | Titles and descriptions are set. Still to add: social share image, `sitemap.xml`, `robots.txt`. |

---

## 5. Interim site vs. the v4 GRPR structure (for the full rebuild)

| v4 section | Interim site today |
|---|---|
| Home (hero, Challenge Navigator, Why GRPR, Experience, Industries, Intelligence Center, Team, CTA) | Home covers the hero, services, why-style messaging, sample experience, insights, team and CTA. **Not built: Challenge Navigator and Industries.** |
| Why GRPR (Who We Are, Leadership, Recognition) | ✔ `why-grpr.html` |
| What We Help Clients Achieve (6 outcome pages) | Not built (Phase 1 in v4) |
| Solutions: Government Affairs | ✔ |
| Solutions: Public Affairs, Strategic Communications, Reputation Management | Covered inside Public Relations |
| Solutions: Crisis Communications | ✔ Crisis Command |
| Solutions: Legislative Monitoring | Covered inside Government Affairs |
| Industries (6), with Technology & Data Centers as the flagship | Data centers is covered by **GRIDS**. The other industries aren't built. |
| Experience database | Not built. Needs C2 and C5. |
| Team profiles | ✔ Cards. Full profile pages not built. |
| Insights by theme | ✔ Insights, with topic filters |
| Texas Public Affairs Intelligence Center™ | Not built (Phase 3) |
