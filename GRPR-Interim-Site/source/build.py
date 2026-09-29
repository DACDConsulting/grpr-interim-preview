#!/usr/bin/env python3
"""Static builder for the interim GRPR and Gray Reed Advisory sites.
Outputs plain HTML/CSS/JS (no framework) into ./dist/<site>/.
"""
import os, shutil, textwrap

OUT = os.environ.get("OUT", "dist")

# --- Official logo files (hot-linked from the current live sites for the mockup).
# Before launch: download these into each site's /assets folder and point these at "assets/...".
GRAS_LOGO = "https://www.grprpublicaffairs.com/wp-content/uploads/sites/895/2023/08/Gray-Reed-Advisory-Services-LLC-logo-1.svg"
GRPR_LOGO = "https://www.grprpublicaffairs.com/wp-content/uploads/sites/895/2023/08/grpr-logo-color.svg"
GR_LOGO   = "https://www.grayreed.com/templates/site/images/logo.png"

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect x='4' y='4' width='16' height='56' fill='%23A91D37'/%3E%3Crect x='24' y='4' width='16' height='56' fill='%23A91D37'/%3E"
           "%3Crect x='44' y='4' width='16' height='56' fill='%23A91D37'/%3E%3C/svg%3E")

GRAS_URL = "https://www.grayreedadvisory.com"
GRPR_URL = "https://www.grprpublicaffairs.com"
GR_URL = "https://www.grayreed.com"
CRISIS_GR = "https://www.grayreed.com/Practices/Litigation/Crisis-Readiness-Response-Recovery"
GRIDS_PR = "https://www.grayreed.com/NewsResources/Press-Releases/282502/Gray-Reed-Launches-GRIDS-Initiative-to-Serve-Texas-Data-Center-Market"

# ----------------------------------------------------------------------------- people
# EDIT: replace "#" bio links and add headshots (set "img": "assets/people/name.jpg").
P = {
  "leggett":   dict(name="Adam Leggett", title="Managing Director of Government Affairs", practice="Government Affairs",
                    email="aleggett@grprpublicaffairs.com", phone="512.650.6109"),
  "villarreal":dict(name="Alyssa Villarreal", title="Government Affairs Coordinator", practice="Government Affairs",
                    email="avillarreal@grayreedadvisory.com", phone="713.986.7160"),
  "rylander":  dict(name="Marc Rylander", title="Chief Communications Officer", practice="Public Relations",
                    email="mrylander@grprpublicaffairs.com", phone="214.954.4135"),
  "rose":      dict(name="Charlie Rose", title="Director of Strategic Communication", practice="Public Relations",
                    email="crose@grprpublicaffairs.com", phone="469.320.6027"),
  "pr3":       dict(name="Team Member Name", title="Title — placeholder", practice="Public Relations",
                    email="name@grprpublicaffairs.com", phone="000.000.0000", ph=True),
  "rc1":       dict(name="Practice Leader Name", title="Leader, Risk & Compliance", practice="Risk & Compliance",
                    email="name@grayreedadvisory.com", phone="000.000.0000", ph=True),
  "rc2":       dict(name="Team Member Name", title="Title — placeholder", practice="Risk & Compliance",
                    email="name@grayreedadvisory.com", phone="000.000.0000", ph=True),
  "pro1":      dict(name="Practice Leader Name", title="Leader, Procurement", practice="Procurement",
                    email="name@grayreedadvisory.com", phone="000.000.0000", ph=True),
  "lead1":     dict(name="Leader Name", title="President, Gray Reed Advisory Services", practice="Leadership",
                    email="name@grayreedadvisory.com", phone="000.000.0000", ph=True),
  "lead2":     dict(name="Leader Name", title="Director of Marketing & Business Development", practice="Leadership",
                    email="name@grayreedadvisory.com", phone="000.000.0000", ph=True),
  "hardig":    dict(name="J.J. Hardig", title="Gray Reed", practice="Crisis Command"),
  "vick":      dict(name="Gabe T. Vick", title="Gray Reed", practice="Crisis Command"),
  "davis":     dict(name="Chris Davis, JD, CPA", title="Gray Reed", practice="Crisis Command"),
  "cooney":    dict(name="Stephen Cooney", title="Partner, Gray Reed", practice="GRIDS"),
  "crady":     dict(name="Ned Crady", title="Partner, Gray Reed", practice="GRIDS"),
}

def initials(n):
    parts = [w for w in n.replace(",", "").split() if w[0].isalpha() and w not in ("JD", "CPA")]
    return (parts[0][0] + parts[-1][0]).upper() if len(parts) > 1 else parts[0][:2].upper()

def person_card(key):
    p = P[key]
    photo = f'<img src="{p["img"]}" alt="{p["name"]}">' if p.get("img") else f'<span>{initials(p["name"])}</span>'
    contact = ""
    if p.get("email"):
        contact = f'''<div class="contact">
          <a href="mailto:{p["email"]}">{p["email"]}</a>
          <a href="tel:{p["phone"].replace(".", "")}">{p["phone"]}</a>
          <a class="bio" href="#">Full bio <span class="arrow"></span></a><!-- EDIT: bio link -->
        </div>'''
    return f'''<article class="person reveal">
      <div class="photo">{photo}</div>
      <div class="practice">{p["practice"]}</div>
      <h3>{p["name"]}</h3>
      <div class="title">{p["title"]}</div>
      {contact}
    </article>'''

def mini(key):
    p = P[key]
    return f'''<a class="mini" href="#"><div class="av">{initials(p["name"])}</div><div><b>{p["name"]}</b><small>{p["title"]}</small></div></a>'''

# ----------------------------------------------------------------------------- shared content blocks
SERVICES = {
  "government-affairs": dict(
    title="Government Affairs", grpr=True,
    short="Legislative and regulatory strategy, advocacy and monitoring across every branch of Texas government.",
    lead="We develop and execute advocacy plans aligned to your policy goals — and give you the intelligence to act before the landscape shifts.",
    intro="Well-connected, session-tested and focused on outcomes. Our team identifies, cultivates and leverages relationships with key decision makers across all branches of Texas government, and steers clients through dynamic regulatory and legislative processes.",
    caps=[
      ("Strategy", "With a comprehensive understanding of the regulatory and parliamentary process, we develop a plan tailored to each client’s regulatory or policy goals."),
      ("Advocacy", "Meaningful engagement with policymakers and staff is key to legislative success. We approach each meeting with focus — articulating why legislation matters to your business, your industry and the state of Texas."),
      ("Legislative Monitoring", "Thousands of bills and amendments are filed every session. We use technology and disciplined tracking to monitor legislation, hearings and rule-making during session and the interim."),
      ("Regulatory & Agency Engagement", "Placeholder — representation before state agencies, boards and commissions on permitting, rule-making and compliance matters."),
      ("Coalitions & Stakeholders", "Placeholder — building and managing coalitions, associations and allied voices that strengthen a policy position."),
    ],
    steps=[("Assess", "Map the issue, the decision makers and the calendar."), ("Engage", "Build the case and put it in front of the right people."), ("Monitor", "Track every move and adjust in real time.")],
    people=["leggett", "villarreal"],
  ),
  "public-relations": dict(
    title="Public Relations", grpr=True,
    short="Strategic communications, crisis communication and media training that protect and advance your reputation.",
    lead="We help organizations navigate shifts in public opinion — protecting brand equity, polishing executive profiles and turning challenges into opportunities.",
    intro="Our communicators pair deep media relationships with disciplined, targeted content to advance brand positioning, reinforce the right messages, counter negativity and protect corporate standing.",
    caps=[
      ("Strategic Communications", "We leverage media relationships and targeted content development to advance brand positioning, reinforce messaging, counter negativity and protect corporate standing."),
      ("Crisis Communication", "We rapidly deploy media relations, community engagement, executive visibility and targeted content to minimize disruption, protect brand equity and rebuild stakeholder trust."),
      ("Media Training", "Customized training that prepares spokespeople for any interview — delivering key messages, bridging to priority topics and handling tough questions."),
      ("Executive Visibility", "Placeholder — thought leadership, speaking, bylines and profile-building for executives and leadership teams."),
      ("Digital & Social", "Placeholder — social strategy, content calendars and community management."),
    ],
    steps=[("Listen", "Understand audiences, sentiment and risk."), ("Position", "Sharpen the message and the messengers."), ("Amplify", "Earn attention where it counts.")],
    people=["rylander", "rose"],
  ),
  "risk-compliance": dict(
    title="Risk & Compliance", grpr=False,
    short="Fractional CIO leadership, cybersecurity and regulatory compliance programs that hold up under scrutiny.",
    lead="We help clients understand their exposure, fix their gaps and demonstrate accountability to regulators, boards and stakeholders.",
    intro="Attorneys advise on compliance. We operationalize it — building the systems, processes and documentation that turn legal guidance into day-to-day practice.",
    caps=[
      ("Advisory & Fractional CIO", "Executive-level technology leadership without the full-time cost: fractional and interim CIO/CTO, IT strategy and roadmaps, M&A IT due diligence and post-merger integration, and technology value creation for PE portfolios."),
      ("Cybersecurity", "Security assessments and gap analysis, virtual CISO programs, IT and operational technology security for critical infrastructure, penetration testing, incident readiness and cyber incident response."),
      ("Compliance", "NERC CIP and SOC 2 readiness and audit support, NIST CSF and CMMC certification readiness, data privacy programs (GDPR, CCPA, Texas) and cyber-insurance and enterprise risk management."),
    ],
    steps=[("Assess", "Measure exposure against the standards that apply to you."), ("Remediate", "Close gaps with practical, prioritized fixes."), ("Sustain", "Build programs that stay audit-ready.")],
    people=["rc1", "rc2"],
    triggers=[
      ("M&A diligence or integration", "IT gaps and compliance exposure surface fast after a deal closes."),
      ("A security incident", "Organizations need structure, not just legal defense."),
      ("A regulatory mandate", "CMMC, SEC cyber disclosure and privacy deadlines are non-negotiable."),
      ("Cyber-insurance renewal", "Insurers are raising the bar on required controls."),
      ("Customer security demands", "Enterprise buyers want SOC 2 proof before they sign."),
    ],
  ),
  "procurement": dict(
    title="Procurement", grpr=False,
    short="Procurement strategy, solicitations, vendor selection and contract management for public entities and businesses.",
    lead="We help municipalities, school districts and businesses buy smarter — with defensible processes and contracts that deliver what was promised.",
    intro="From the first requirement to the final invoice, we bring structure and accountability to how organizations source, select and manage the vendors they depend on.",
    caps=[
      ("Procurement Strategy", "Placeholder — category strategy, sourcing plans and procurement policy aligned to your budget cycle and compliance requirements."),
      ("Solicitations & RFP Management", "Placeholder — drafting, issuing and evaluating RFPs, RFQs and bids with a transparent, defensible process."),
      ("Vendor Selection & Management", "Placeholder — objective evaluation, negotiation support and ongoing vendor performance management."),
      ("Contract Management", "Placeholder — contract administration, obligation tracking, renewals and performance against terms."),
    ],
    steps=[("Plan", "Define needs, budget and timeline."), ("Source", "Run a competitive, compliant process."), ("Manage", "Hold vendors to what they promised.")],
    people=["pro1"],
  ),
}

SOLUTIONS = {
  "crisis-command": dict(
    title="Crisis Command", kicker="Integrated solution · with Gray Reed",
    short="Legal counsel and crisis communications working as one team — before, during and after a high-stakes event.",
    lead="Organizations don’t fail during a crisis because they lack capable people. They fail because critical decisions were never resolved before the pressure hit.",
    pills=["Readiness", "Response", "Recovery"],
    phases=[
      ("Readiness", "Build capability before an incident occurs.", ["Crisis assessments and gap analysis", "Communications planning and spokesperson training", "Incident response protocols", "Government investigation preparedness", "Tabletop exercises and simulations", "Board and executive training"]),
      ("Response", "Coordinated action the moment an incident occurs.", ["Legal guidance and investigation coordination", "Government agency engagement", "Media relations and communications management", "Regulatory response and stakeholder coordination", "Cyber incident response"]),
      ("Recovery", "Long-term resilience after the headlines fade.", ["Root-cause analysis and remediation", "Governance enhancements", "Reputation restoration", "Policy improvements and future preparedness"]),
    ],
    pull="One coordinated approach. Not five vendors.",
    people=["hardig", "vick", "davis", "rylander"],
    source=CRISIS_GR, source_label="Crisis Command on grayreed.com",
  ),
  "grids": dict(
    title="GRIDS", kicker="Integrated solution · Texas data centers",
    short="Government Relations, Real Estate, Infrastructure, Development and Security — one team for the Texas data center market.",
    lead="A dedicated effort serving landowners, investors, developers and operators in the Texas data center market — combining legal experience with legislative, regulatory, cybersecurity and data privacy capabilities.",
    pills=["Landowners", "Investors", "Developers", "Operators"],
    letters=[
      ("G", "Government Relations", "Legislative and regulatory strategy and advocacy from GRPR’s top-ranked government affairs team."),
      ("R", "Real Estate", "Site acquisition, land use and water rights from board-certified real estate counsel."),
      ("I", "Infrastructure", "Energy, power and infrastructure transactions and agreements."),
      ("D", "Development", "Construction, tax, M&A and the development work that gets projects built."),
      ("S", "Security (Cyber & Data)", "Cybersecurity and data privacy readiness for facilities and operators."),
    ],
    people=["cooney", "crady", "leggett"],
    source=GRIDS_PR, source_label="Read the GRIDS announcement",
  ),
}

INDUSTRIES = ["Higher Education", "Local Government & K-12", "Energy & Utilities", "Data Centers & Digital Infrastructure",
              "Construction", "Manufacturing", "Healthcare", "Financial Services", "Private Equity Portfolio Companies", "Trade Associations"]

# ----------------------------------------------------------------------------- site config
SITES = {
  "gray-reed-advisory": dict(
    name="Gray Reed Advisory", legal="Gray Reed Advisory Services LLC", logo=GRAS_LOGO, logo_alt="Gray Reed Advisory Services",
    brand_cls="brand", base=GRAS_URL,
    utility_left="Business advisory backed by Gray Reed, a full-service Texas law firm",
    services=["government-affairs", "public-relations", "risk-compliance", "procurement"],
    solutions=["crisis-command", "grids"],
    tagline="Focused advisory for business leaders facing high-stakes decisions — delivered alongside Gray Reed’s attorneys.",
  ),
  "grpr": dict(
    name="GRPR", legal="Gray Reed Advisory Services LLC", logo=GRPR_LOGO, logo_alt="GRPR — Gray Reed Public Relations & Government Affairs",
    brand_cls="brand grpr", base=GRPR_URL,
    utility_left="Public Relations &amp; Government Affairs · A division of Gray Reed Advisory Services",
    services=["government-affairs", "public-relations"],
    solutions=["crisis-command", "grids"],
    tagline="Government relations and strategic communications for organizations navigating evolving political and public landscapes.",
  ),
}


# ----------------------------------------------------------------------------- imagery
# Free-license photos from Unsplash (unsplash.com/license — free for commercial use, no attribution required).
# Hot-linked for the mockup; before launch download into assets/img/ and update these paths.
U = "https://images.unsplash.com/"
IMG = {
  "home-gras":          (U + "photo-1634064735992-266742efd9d4", "Dallas skyline and the Margaret Hunt Hill Bridge"),
  "grpr-combined":      (U + "photo-1666969565832-b55bf42a900d", "Aerial view of the downtown Austin skyline"),
  "home-grpr":          (U + "photo-1568807697609-e8aacc588ad9", "Texas State Capitol framed by trees"),
  "government-affairs": (U + "photo-1602364438008-9aa4242284b8", "Texas State Capitol dome"),
  "public-relations":   (U + "photo-1758518730037-a16581a040e8", "Team meeting in a bright conference room"),
  "risk-compliance":    (U + "photo-1682562031269-58a59c81432c", "Clean, modern technology facility"),
  "procurement":        (U + "photo-1503423571797-2d2bb372094a", "Minimal white conference room"),
  "crisis-command":     (U + "photo-1431540015161-0bf868a2d407", "Sunlit boardroom"),
  "grids":              (U + "photo-1762163516269-3c143e04175c", "Data center server racks"),
  "team":               (U + "photo-1563219125-60d10ffe8877", "Aerial view of downtown Dallas"),
  "contact":            (U + "photo-1640704599116-34fa80fe31cb", "Downtown Dallas skyline"),
}
def img(key, w=1600, color=False):
    """Pencil-sketch treatment: the photo is rendered twice — a grayscale base and an inverted,
    blurred copy blended with color-dodge — which the browser turns into a graphite drawing.
    To show the plain photo instead, remove the "sketch" class from .hero-media."""
    u, alt = IMG[key]
    src = f"{u}?auto=format&fit=crop&w={w}&q=80"
    srcset = f"{u}?auto=format&fit=crop&w={w//2}&q=80 {w//2}w, {src} {w}w"
    sizes = "(max-width: 960px) 100vw, 46vw"
    out = (f'<img class="base" src="{src}" srcset="{srcset}" sizes="{sizes}" alt="{alt} ({"colored " if color else ""}pencil sketch)">'
           f'<img class="dodge" src="{src}" srcset="{srcset}" sizes="{sizes}" alt="" aria-hidden="true">')
    if color:  # colored-pencil: recolor the drawing (wash) plus a soft light fill (bleed)
        out += (f'<img class="wash" src="{src}" srcset="{srcset}" sizes="{sizes}" alt="" aria-hidden="true">'
                f'<img class="bleed" src="{src}" srcset="{srcset}" sizes="{sizes}" alt="" aria-hidden="true">')
    return out

def page_hero(crumbs, eyebrow, title, lead, extra, key=None):
    # Interior pages: text-only hero (hero imagery is used on the home pages only).
    return f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs">{crumbs}</div>
    <div class="ph-grid">
      <div><div class="eyebrow">{eyebrow}</div><h1>{title}</h1>{extra}</div>
      <p class="lead">{lead}</p>
    </div>
  </div>
</section>'''


def hero_slider(slides, label, color=False):
    """Home hero slider. Each slide = (service label, IMG key, headline html, lead, link, link label)."""
    copies, media, tabs = [], [], []
    for i, slide in enumerate(slides):
        name, key, h1, lead, href, cta_label = slide[:6]
        tab_label = slide[6] if len(slide) > 6 else name
        act = " is-active" if i == 0 else ""
        tag = "h1" if i == 0 else "h2"
        copies.append(f'''<div class="slide-copy{act}" id="slide-{i}" role="tabpanel" aria-roledescription="slide" aria-label="{i+1} of {len(slides)}: {name}"{"" if i == 0 else ' aria-hidden="true"'}>
        <div class="eyebrow">{name}</div>
        <{tag} class="slide-title">{h1}</{tag}>
        <p class="lead">{lead}</p>
        <div class="actions"><a class="btn" href="{href}"{"" if i == 0 else ' tabindex="-1"'}>{cta_label} <span class="arrow"></span></a><a class="btn ghost" href="contact.html"{"" if i == 0 else ' tabindex="-1"'}>Talk to Our Team</a></div>
      </div>''')
        media.append(f'<div class="slide-media{act}">{img(key, color=color)}</div>')
        tabs.append(f'<button type="button" class="slider-tab{act}" role="tab" aria-label="{tab_label}" aria-selected="{"true" if i == 0 else "false"}" aria-controls="slide-{i}"><span class="t-num">{i+1:02d}</span><span class="t-label">{tab_label}</span><span class="t-bar"><i></i></span></button>')
    return f'''<section class="hero with-img slider" data-slider aria-roledescription="carousel" aria-label="{label}">
  <div class="wrap">
    <div class="hero-copy">
      <div class="slides-copy" aria-live="polite">
      {"".join(copies)}
      </div>
      <div class="slider-tabs" role="tablist" aria-label="Choose a service" style="--n:{len(slides)}">{"".join(tabs)}</div>
    </div>
  </div>
  <div class="hero-media sketch{" color" if color else ""} slides-media">{"".join(media)}</div>
</section>'''

def facts(items):
    return '<section class="facts"><div class="wrap"><ul class="facts-row">' + "".join(f'<li><span class="k">{k}</span><span class="v">{v}</span></li>' for k, v in items) + '</ul></div></section>'

# ----------------------------------------------------------------------------- chrome
def head(site, title, desc):
    s = SITES[site]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- Fallback font. Replace with the licensed Gibson web-font kit used on grayreed.com when available. -->
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(site, active):
    s = SITES[site]
    if active.startswith("video-"): active = "insights"
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    svc_active = active in s["services"]
    sol_active = active in s["solutions"]
    dd_sol = "".join(f'<li><a href="{k}.html">{SOLUTIONS[k]["title"]}<small>{SOLUTIONS[k]["kicker"].split("·")[1].strip()}</small></a></li>' for k in s["solutions"])
    if site == "grpr":
        items = (a("why-grpr.html", "Why GRPR", "why-grpr")
                 + a("government-affairs.html", "Government Affairs", "government-affairs")
                 + a("public-relations.html", "Public Relations", "public-relations")
                 + f'<li class="has-dd{" active" if sol_active else ""}"><button type="button" aria-expanded="false">Solutions <i class="chev"></i></button><ul class="dropdown">{dd_sol}</ul></li>'
                 + a("team.html", "Our Team", "team")
                 + a("insights.html", "Insights", "insights"))
        util = f'<a href="{GRAS_URL}">Gray Reed Advisory</a><a href="{GR_URL}">Gray Reed</a><a href="https://www.linkedin.com/" aria-label="LinkedIn">LinkedIn</a>'
    else:
        dd_svc = ('<li class="dd-label">Core services</li>'
                  + "".join(f'<li><a href="{k}.html">{SERVICES[k]["title"]}<small>{"Delivered by GRPR" if SERVICES[k]["grpr"] else "Gray Reed Advisory"}</small></a></li>' for k in s["services"]))
        items = (f'<li class="has-dd{" active" if svc_active else ""}"><button type="button" aria-expanded="false">Services <i class="chev"></i></button><ul class="dropdown">{dd_svc}</ul></li>'
                 + f'<li class="has-dd{" active" if sol_active else ""}"><button type="button" aria-expanded="false">Solutions <i class="chev"></i></button><ul class="dropdown">{dd_sol}</ul></li>'
                 + a("team.html", "Our Team", "team")
                 + a("insights.html", "Insights", "insights")
                 + a(GRPR_URL, "GRPR", "grpr-ext"))
        util = f'<a href="{GRPR_URL}">GRPR</a><a href="{GR_URL}">Gray Reed</a><a href="https://www.linkedin.com/" aria-label="LinkedIn">LinkedIn</a>'
    return f'''<div class="utility"><div class="wrap"><span class="u-left">{s["utility_left"]}</span><span class="u-links">{util}</span></div></div>
<header class="site-header">
  <div class="wrap">
    <a class="{s["brand_cls"]}" href="index.html"><img src="{s["logo"]}" alt="{s["logo_alt"]}"></a>
    <nav class="nav" aria-label="Primary">
      <ul>{items}</ul>
      <a class="btn sm nav-cta" href="contact.html">Contact Us</a>
    </nav>
    <button class="menu-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
'''

def footer(site):
    s = SITES[site]
    svc = "".join(f'<li><a href="{k}.html">{SERVICES[k]["title"]}</a></li>' for k in s["services"])
    sol = "".join(f'<li><a href="{k}.html">{SOLUTIONS[k]["title"]}</a></li>' for k in s["solutions"])
    fam = (f'<li><a href="{GR_URL}">Gray Reed (law firm)</a></li>'
           + (f'<li><a href="{GRPR_URL}">GRPR</a></li>' if site != "grpr" else f'<li><a href="{GRAS_URL}">Gray Reed Advisory</a></li>')
           + ('<li><a href="why-grpr.html">Why GRPR</a></li>' if site == "grpr" else '')
           + '<li><a href="team.html">Our Team</a></li><li><a href="insights.html">Insights</a></li><li><a href="contact.html">Contact</a></li>')
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="f-top">
      <div class="f-brand"><img src="{s["logo"]}" alt="{s["logo_alt"]}"><p>{s["tagline"]}</p></div>
      <div class="f-col"><h5>Services</h5><ul>{svc}</ul></div>
      <div class="f-col"><h5>Solutions</h5><ul>{sol}</ul></div>
      <div class="f-col"><h5>Gray Reed</h5><ul>{fam}</ul></div>
    </div>
    <div class="f-bottom">
      <div class="f-parent"><a href="{GR_URL}"><img src="{GR_LOGO}" alt="Gray Reed"></a><span>Copyright © <span data-year>2026</span>, {s["legal"]}. All Rights Reserved.</span></div>
      <nav><a href="#">Privacy Policy</a><a href="#">Disclaimer</a><a href="#">Sitemap</a></nav><!-- EDIT: legal links -->
    </div>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
'''

def cta(site, pre="Facing a high-stakes", word="decision?", text=None):
    heading = f'{pre} <em class="cta-em">{word}</em>'
    text = text or "Tell us what’s at stake. We’ll bring the right people from across Gray Reed to the table."
    return f'''<section class="cta">
  <div class="wrap">
    <div><div class="eyebrow light">Start a conversation</div><h2>{heading}</h2></div>
    <div><p>{text}</p><div class="actions"><a class="btn white" href="contact.html">Contact Us <span class="arrow"></span></a><a class="btn ghost" style="color:#fff;border-color:rgba(255,255,255,.4)" href="team.html">Meet the Team</a></div></div>
  </div>
</section>'''

def family(site):
    cards = [(GR_URL, GR_LOGO, "Gray Reed", "Full-service Texas law firm"),
             (GRAS_URL, GRAS_LOGO, "Gray Reed Advisory", "Business advisory services"),
             (GRPR_URL, GRPR_LOGO, "GRPR", "Public relations &amp; government affairs")]
    return '<div class="family">' + "".join(
        f'<a href="{u}"><img src="{l}" alt="{alt}"><span>{d} <span class="arrow" style="margin-left:6px"></span></span></a>' for u, l, alt, d in cards) + '</div>'

def svc_link(site, key):
    return f"{key}.html"

# ----------------------------------------------------------------------------- sample proof points
SAMPLE_CASES = [
  ("Public university", "Reputation &amp; issues management", "Ongoing strategic communications counsel through leadership transitions, campus issues and a statewide media spotlight.", "<b>[Outcome]</b> — e.g., coverage sentiment, response time, audiences reached"),
  ("Statewide trade association", "Legislative session advocacy", "Session strategy, testimony preparation and stakeholder engagement to protect members from a costly regulatory change.", "<b>[Outcome]</b> — e.g., bill amended, provision removed, rule withdrawn"),
  ("Critical infrastructure operator", "Cyber readiness &amp; compliance", "Gap assessment, remediation roadmap and tabletop exercise ahead of a regulatory audit and insurance renewal.", "<b>[Outcome]</b> — e.g., audit passed, controls implemented, premium impact"),
]

def cases_html():
    return '<div class="cases">' + "".join(f'''<article class="case reveal"><div class="ct">Sample engagement · {c}</div><h3>{t}</h3><p>{d}</p><div class="res">{r}</div></article>''' for c, t, d, r in SAMPLE_CASES) + '</div><p class="note">Representative engagements shown as placeholders — replace with approved client stories before launch.</p>'

def stats_html(items):
    return '<div class="stats">' + "".join(f'<div class="stat reveal"><div class="n">{n}<sup>{sup}</sup></div><div class="l">{l}</div></div>' for n, sup, l in items) + '</div><p class="note">Illustrative figures — confirm or replace before launch.</p>'

QUOTE = '''<div class="quote reveal"><blockquote>Placeholder testimonial. A short, specific client quote about outcomes and partnership belongs here — two sentences at most.</blockquote><cite><b>Client Name</b> · Title, Organization</cite></div>'''

# ----------------------------------------------------------------------------- pages
def page(site, key, title, desc, body):
    html = head(site, title, desc) + header(site, key) + body + footer(site)
    path = os.path.join(OUT, site, f"{key}.html" if key != "home" else "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)

def services_grid(site, keys):
    cls = {4: "", 3: " three", 2: " two"}[len(keys)]
    out = []
    for i, k in enumerate(keys, 1):
        s = SERVICES[k]
        tag = '' if site == "grpr" else ('<div class="tag">Delivered by GRPR</div>' if s["grpr"] else '<div class="tag">&nbsp;</div>')
        lis = "".join(f"<li>{c[0]}</li>" for c in s["caps"][:3])
        out.append(f'''<article class="svc reveal"><div class="num">0{i}</div>{tag}<h3>{s["title"]}</h3><p>{s["short"]}</p><ul>{lis}</ul><a class="link" href="{svc_link(site,k)}">Explore <span class="arrow"></span></a></article>''')
    return f'<div class="services{cls}">' + "".join(out) + "</div>"

def solutions_grid(site):
    out = []
    for k in SITES[site]["solutions"]:
        s = SOLUTIONS[k]
        pills = "".join(f"<span>{p}</span>" for p in s["pills"])
        out.append(f'''<article class="sol reveal"><div class="kicker">{s["kicker"]}</div><h3>{s["title"]}</h3><p>{s["short"]}</p><div class="pills">{pills}</div><a class="link" href="{k}.html">Learn more <span class="arrow"></span></a></article>''')
    return '<div class="solutions">' + "".join(out) + "</div>"

def home_gras():
    site = "gray-reed-advisory"
    body = f'''
{hero_slider([
  ("Gray Reed Advisory Services", "contact", "Clear direction for <em>high-stakes</em> decisions.", "Four focused advisory services — government affairs, public relations, risk &amp; compliance and procurement — delivered alongside Gray Reed’s attorneys, so policy, reputation and risk are handled as one strategy.", "#services", "Our Services", "All Services"),
  ("Government Affairs", "home-grpr", "Be heard at the <em>Capitol.</em>", SERVICES["government-affairs"]["lead"], "government-affairs.html", "Government Affairs"),
  ("Public Relations", "home-gras", "Own the story before it <em>owns you.</em>", SERVICES["public-relations"]["lead"], "public-relations.html", "Public Relations"),
  ("Risk &amp; Compliance", "risk-compliance", "Know your exposure. <em>Close</em> the gaps.", SERVICES["risk-compliance"]["lead"], "risk-compliance.html", "Risk &amp; Compliance"),
  ("Procurement", "procurement", "Buy smarter. Contract with <em>confidence.</em>", SERVICES["procurement"]["lead"], "procurement.html", "Procurement"),
], "Gray Reed Advisory services")}
{facts([("04", "Focused services. Depth, not breadth — each led by senior practitioners."), ("01", "Coordinated team. Advisors and attorneys working from the same plan."), ("TX", "Relationships from the Capitol to the boardroom, across every major Texas market.")])}

<section class="section" id="services">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">What we deliver</div><h2>Four services. <br>One coordinated team.</h2></div><p>We’ve sharpened our focus to the work where an advisory team backed by a law firm creates the most value for our clients.</p></div>
    {services_grid(site, SITES[site]["services"])}
  </div>
</section>

<section class="section wash">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Integrated solutions</div><h2>When the stakes cross <br>disciplines.</h2></div><p>Our most complex challenges don’t fit in one practice. These solutions bring Gray Reed’s attorneys and our advisors together from day one.</p></div>
    {solutions_grid(site)}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <div class="eyebrow">Why Gray Reed Advisory</div>
      <h2>Backed by a law firm. <br>Built to execute.</h2>
      <p class="pull">Attorneys advise on compliance. We operationalize it.</p>
    </div>
    <ul class="points">
      <li class="reveal"><span class="pn">01</span><div><h4>Law-firm backing</h4><p>Every engagement is supported by Gray Reed, a full-service Texas law firm with deep litigation and transactional bench strength.</p></div></li>
      <li class="reveal"><span class="pn">02</span><div><h4>One coordinated approach</h4><p>Legal, communications, government affairs and technology risk working from a single plan — not five vendors.</p></div></li>
      <li class="reveal"><span class="pn">03</span><div><h4>Depth, not breadth</h4><p>Four services, each led by senior practitioners with the relationships and experience to deliver.</p></div></li>
      <li class="reveal"><span class="pn">04</span><div><h4>Texas relationships</h4><p>Recognized in Capitol Inside’s 2025 Texas Lobby Power Rankings, with access across all branches of Texas government.</p></div></li>
    </ul>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    {stats_html([("20", "+", "Years of senior public-service experience on our bench"), ("15", "+", "Years of legislative tracking experience"), ("100", "+", "Communications and crisis engagements"), ("150", "+", "Gray Reed attorneys to draw on")])}
  </div>
</section>

<section class="section wash">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Our work</div><h2>Representative engagements</h2></div><p>A snapshot of how we help clients protect their position and move forward.</p></div>
    {cases_html()}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Industries</div><h2>Where we work</h2></div><p>We serve public entities and private companies where regulation, reputation and risk intersect.</p></div>
    <div class="chips">{"".join(f"<span>{i}</span>" for i in INDUSTRIES)}</div>
  </div>
</section>

<section class="section wash">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Leadership</div><h2>Practice leaders</h2></div><p><a class="link" href="team.html">View the full team <span class="arrow"></span></a></p></div>
    <div class="people">{"".join(person_card(k) for k in ["leggett", "rylander", "rc1", "pro1"])}</div>
  </div>
</section>

{latest_insights(site)}
<section class="section">
  <div class="wrap">{QUOTE}</div>
</section>

<section class="section tight flush" style="padding-top:0">
  <div class="wrap">{family(site)}</div>
</section>
{cta(site)}
'''
    page(site, "home", "Gray Reed Advisory | Government Affairs, Public Relations, Risk & Compliance, Procurement",
         "Gray Reed Advisory Services: focused advisory for business leaders facing high-stakes decisions.", body)

def home_grpr():
    site = "grpr"
    body = f'''
{hero_slider([
  ("Government Affairs + Public Relations", "grpr-combined", "Influence the policy. <em>Own</em> the story.", "GRPR offers government relations and strategic communications support to help organizations navigate evolving political and public landscapes — from the Texas Capitol to the front page.", "#services", "What We Do", "GA + PR"),
  ("Government Affairs", "home-grpr", "Be heard at the <em>Capitol.</em>", SERVICES["government-affairs"]["lead"], "government-affairs.html", "Government Affairs"),
  ("Public Relations", "home-gras", "Own the story before it <em>owns you.</em>", SERVICES["public-relations"]["lead"], "public-relations.html", "Public Relations"),
], "GRPR services", color=True)}


<section class="section" id="services">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">What we do</div><h2>Two disciplines. <br>One strategy.</h2></div><p>Policy outcomes and public perception are rarely separate problems. We plan them together, so every message and every meeting pulls in the same direction.</p></div>
    {services_grid(site, SITES[site]["services"])}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <div class="eyebrow">Why GRPR</div>
      <h2>The Capitol and the headline. One team.</h2>
      <p class="pull">We built GRPR so you never have to coordinate your advisors in the middle of a fight.</p>
      <p style="margin-top:28px"><a class="link" href="why-grpr.html">Why clients choose GRPR <span class="arrow"></span></a></p>
    </div>
    <ul class="points"><li class="reveal"><span class="pn">01</span><div><h4>One plan, two disciplines</h4><p>Government affairs and public relations sit on the same team and work from the same strategy. Every meeting at the Capitol and every message in the market pulls in the same direction.</p></div></li><li class="reveal"><span class="pn">02</span><div><h4>Session-tested at the Texas Capitol</h4><p>Our government affairs practice is led by a former Texas Senate chief of staff and was recognized in Capitol Inside’s 2025 Texas Lobby Power Rankings. We know the process, the people and the calendar.</p></div></li><li class="reveal"><span class="pn">03</span><div><h4>A law firm down the hall</h4><p>GRPR is part of Gray Reed Advisory Services, affiliated with Gray Reed, a full-service Texas law firm. When an issue carries legal exposure, the right attorneys join early, not after the damage is done.</p></div></li><li class="reveal"><span class="pn">04</span><div><h4>Built for the hardest moments</h4><p>Through Crisis Command, our communicators and Gray Reed’s attorneys handle readiness, response and recovery as one team, starting in the first 15 minutes.</p></div></li></ul>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    {stats_html([("20", "+", "Years of senior public-service experience"), ("15", "+", "Years of legislative tracking experience"), ("100", "+", "Communications and crisis engagements"), ("50", "+", "Clients across Texas")])}
  </div>
</section>

<section class="section wash">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Integrated solutions</div><h2>With Gray Reed, <br>from day one.</h2></div><p>For the moments that are legal, political and public all at once, GRPR works hand in hand with Gray Reed’s attorneys.</p></div>
    {solutions_grid(site)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Our work</div><h2>Representative engagements</h2></div><p>How we help clients win on policy and protect their reputation.</p></div>
    {cases_html()}
  </div>
</section>

<section class="section wash">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Our team</div><h2>Main contacts</h2></div><p><a class="link" href="team.html">View the full team <span class="arrow"></span></a></p></div>
    <div class="people">{"".join(person_card(k) for k in ["leggett", "villarreal", "rylander", "rose"])}</div>
  </div>
</section>

{latest_insights(site)}
<section class="section">
  <div class="wrap">{QUOTE}</div>
</section>

<section class="section tight flush" style="padding-top:0">
  <div class="wrap">{family(site)}</div>
</section>
{cta(site, "Need to be heard in", "Austin?", "Whether it’s a bill, a rule or a headline, we’ll help you shape the outcome.")}
'''
    page(site, "home", "GRPR | Public Relations & Government Affairs",
         "GRPR provides government relations and strategic communications for organizations navigating evolving political and public landscapes.", body)

def service_page(site, key):
    s = SERVICES[key]
    caps = "".join(f'<li class="reveal"><span class="cn">{i:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(s["caps"], 1))
    steps = "".join(f'<div class="step"><div class="sn">{i:02d}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(s["steps"], 1))
    triggers = ""
    if s.get("triggers"):
        triggers = '<h2>When clients call us</h2><ul class="caps">' + "".join(f'<li><span class="cn">→</span><div><h3>{t}</h3><p>{d}</p></div></li>' for t, d in s["triggers"]) + "</ul>"
    badge = ""
    if s["grpr"] and site != "grpr":
        badge = f'<a class="badge" href="{GRPR_URL}">Delivered by <b>GRPR</b> <span class="arrow"></span></a>'
    others = [k for k in SITES[site]["services"] if k != key] + SITES[site]["solutions"]
    rel = "".join(f'<a href="{k}.html">{(SERVICES.get(k) or SOLUTIONS.get(k))["title"]} <span class="arrow"></span></a>' for k in others)
    home_label = SITES[site]["name"]
    body = f'''
{page_hero(f'<a href="index.html">{home_label}</a><span>/</span>Services<span>/</span>{s["title"]}', "Services", s["title"], s["lead"], badge, key)}
<section class="section">
  <div class="wrap detail">
    <div class="prose">
      <!-- EDIT: service overview copy -->
      <p class="intro">{s["intro"]}</p>
      <h2>What we do</h2>
      <ul class="caps">{caps}</ul>
      <h2>How we work</h2>
      <div class="steps">{steps}</div>
      {triggers}
    </div>
    <aside class="aside">
      <div class="card"><h4>Contacts</h4>{"".join(mini(k) for k in s["people"])}</div>
      <div class="card red"><h4>Get in touch</h4><p>Let’s talk about what’s at stake for your organization.</p><a class="btn white sm" href="contact.html">Contact Us <span class="arrow"></span></a></div>
      <div class="card related"><h4>Related</h4>{rel}</div>
    </aside>
  </div>
</section>
{related_insights(site, [s["title"]])}
{cta(site)}
'''
    page(site, key, f'{s["title"]} | {SITES[site]["name"]}', s["short"], body)

def solution_page(site, key):
    s = SOLUTIONS[key]
    home_label = SITES[site]["name"]
    if key == "crisis-command":
        main = '<div class="services three">' + "".join(
            f'<article class="svc reveal"><div class="num">0{i}</div><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></article>'
            for i, (t, d, items) in enumerate(s["phases"], 1)) + "</div>"
        extra = f'''<section class="section wash"><div class="wrap split"><div><div class="eyebrow">The difference</div><h2>Legal risk and public risk, <br>handled together.</h2></div><div><p class="pull" style="margin-top:0">{s["pull"]}</p><p style="margin-top:28px;color:var(--slate)">Crisis Command integrates Gray Reed’s legal counsel directly with GRPR’s communications team, so legal strategy and public messaging move together from the first hour.</p></div></div></section>'''
    else:
        main = '<ul class="caps" style="border-top-color:var(--ink)">' + "".join(
            f'<li class="reveal"><span class="cn" style="font-family:var(--font-light);font-size:40px;letter-spacing:0;line-height:1;padding:0">{l}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
            for l, t, d in s["letters"]) + "</ul>"
        extra = f'''<section class="section wash"><div class="wrap split"><div><div class="eyebrow">Who we serve</div><h2>Built for every seat <br>at the table.</h2></div><div><div class="chips">{"".join(f"<span>{p}</span>" for p in s["pills"])}</div><p style="margin-top:28px;color:var(--slate)">Data centers are the emerging story in Texas. GRIDS brings the legislative, regulatory, real estate, infrastructure and security work behind them into one coordinated team.</p></div></div></section>'''
    body = f'''
{page_hero(f'<a href="index.html">{home_label}</a><span>/</span>Solutions<span>/</span>{s["title"]}', s["kicker"], s["title"], s["lead"], f'<a class="badge" href="{s["source"]}">{s["source_label"]} <span class="arrow"></span></a>', key)}
<section class="section">
  <div class="wrap">
    {main}
  </div>
</section>
{extra}
<section class="section">
  <div class="wrap">
    <div class="s-head"><div><div class="eyebrow">Contacts</div><h2>Who to call</h2></div><p>A coordinated team across Gray Reed and GRPR.</p></div>
    <div class="people{' three' if len(s['people'])==3 else ''}">{"".join(person_card(k) for k in s["people"])}</div>
  </div>
</section>
{cta(site)}
'''
    page(site, key, f'{s["title"]} | {SITES[site]["name"]}', s["short"], body)

def team_page(site):
    if site == "grpr":
        groups = [("Government Affairs", ["leggett", "villarreal"]), ("Public Relations", ["rylander", "rose", "pr3"])]
        intro = "Former legislative staff, agency leaders and seasoned communicators — working as one team."
    else:
        groups = [("Leadership", ["lead1", "lead2"]), ("Government Affairs", ["leggett", "villarreal"]), ("Public Relations", ["rylander", "rose", "pr3"]),
                  ("Risk & Compliance", ["rc1", "rc2"]), ("Procurement", ["pro1"])]
        intro = "Senior practitioners in government affairs, communications, technology risk and procurement — backed by Gray Reed."
    sections = ""
    for i, (g, keys) in enumerate(groups):
        cls = "section wash" if i % 2 else "section"
        sections += f'''<section class="{cls}"><div class="wrap"><div class="s-head"><div><div class="eyebrow">{g}</div><h2>{g}</h2></div><p></p></div><div class="people">{"".join(person_card(k) for k in keys)}</div></div></section>'''
    body = f'''
{page_hero(f'<a href="index.html">{SITES[site]["name"]}</a><span>/</span>Our Team', "Our Team", "The people behind the work.", intro, "", "team")}
<!-- EDIT: headshots, bios and bio links. Placeholder cards are marked "Team Member Name" / "Practice Leader Name". -->
{sections}
{cta(site)}
'''
    page(site, "team", f'Our Team | {SITES[site]["name"]}', intro, body)

def contact_page(site):
    opts = "".join(f"<option>{SERVICES[k]['title']}</option>" for k in SITES[site]["services"]) + "".join(f"<option>{SOLUTIONS[k]['title']}</option>" for k in SITES[site]["solutions"])
    body = f'''
{page_hero(f'<a href="index.html">{SITES[site]["name"]}</a><span>/</span>Contact', "Contact", "Let’s talk.", "Tell us a little about your organization and what’s at stake. The right member of our team will follow up promptly.", "", "contact")}
<section class="section">
  <div class="wrap detail">
    <!-- EDIT: point this form at your form handler (e.g., replace with the HubSpot embed code). -->
    <form class="form" action="#" method="post" onsubmit="event.preventDefault(); this.querySelector('.form-foot small').textContent='Thank you — this demo form does not submit yet.';">
      <div class="form-grid">
        <div class="field"><label for="fn">First name</label><input id="fn" name="first_name" autocomplete="given-name" required></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" name="last_name" autocomplete="family-name" required></div>
        <div class="field"><label for="em">Email</label><input id="em" type="email" name="email" autocomplete="email" required></div>
        <div class="field"><label for="ph">Phone</label><input id="ph" type="tel" name="phone" autocomplete="tel"></div>
        <div class="field"><label for="org">Organization</label><input id="org" name="organization" autocomplete="organization"></div>
        <div class="field"><label for="int">Area of interest</label><select id="int" name="interest"><option value="">Select…</option>{opts}<option>Other</option></select></div>
        <div class="field full"><label for="msg">How can we help?</label><textarea id="msg" name="message"></textarea></div>
      </div>
      <div class="form-foot"><small>Please don’t include confidential information. Submitting this form does not create an attorney-client or advisory relationship.</small><button class="btn" type="submit">Send Message <span class="arrow"></span></button></div>
    </form>
    <aside class="aside">
      <div class="card"><h4>Offices</h4>
        <div class="offices" style="border-top:0">
          <div class="office" style="padding-top:0"><b>Dallas</b><span>[Street address]</span><span>[City, State ZIP]</span></div>
          <div class="office"><b>Houston</b><span>[Street address]</span><span>[City, State ZIP]</span></div>
          <div class="office" style="border-bottom:0"><b>Austin</b><span>[Street address]</span><span>[City, State ZIP]</span></div>
        </div>
      </div>
      <div class="card"><h4>General inquiries</h4><p style="margin:0;font-size:15px">[info@{"grprpublicaffairs" if site == "grpr" else "grayreedadvisory"}.com]<br>[000.000.0000]</p></div>
    </aside>
  </div>
</section>
'''
    page(site, "contact", f'Contact | {SITES[site]["name"]}', "Contact our team.", body)

# ============================================================================ EXTENDED CONTENT
# Crisis Command + GRIDS full on-site content (adapted from grayreed.com practice/industry pages),
# and the Insights library (articles, news and videos).

GR_TL = "https://www.grayreed.com/NewsResources/"

P.update({
  "hardig":  dict(name="J.J. Hardig", title="Gray Reed", practice="Crisis Command", email="jhardig@grayreed.com", phone="713.986.7225"),
  "vick":    dict(name="Gabe T. Vick", title="Gray Reed", practice="Crisis Command", email="gvick@grayreed.com", phone="713.986.7148"),
  "davis":   dict(name="Chris Davis, JD, CPA", title="Gray Reed", practice="Crisis Command", email="cdavis@grayreed.com", phone="469.320.6215"),
  "cooney":  dict(name="Stephen Cooney", title="Partner, Gray Reed · Real Estate &amp; Water Law", practice="GRIDS"),
  "crady":   dict(name="Ned Crady", title="Partner, Gray Reed · Energy &amp; Infrastructure", practice="GRIDS"),
})

SOLUTIONS["crisis-command"].update(
  short="Gray Reed’s integrated crisis readiness, response and recovery offering — attorneys and GRPR working as one team from the first call.",
  lead="Your crisis plan should be built before the call comes. We make sure it is.",
  pills=["Readiness", "The First 15", "The Next 48", "Response", "Recovery"],
)
SOLUTIONS["grids"].update(
  short="Government Affairs &amp; Public Relations, Real Estate, Infrastructure, Development and Security — one coordinated team for the Texas data center market.",
  lead="Texas is in the middle of a data center gold rush. GRIDS brings every discipline a project needs — legal, legislative, community and cyber — under one coordinated team.",
  pills=["Landowners", "Investors", "Developers", "Operators"],
)

GRPR_DISCLAIMER = ("GRPR is a separate public affairs and strategic communications firm affiliated with Gray Reed. GRPR professionals "
                   "are not lawyers and do not provide legal advice. Communications with GRPR personnel outside the direction of Gray Reed "
                   "legal counsel may not be protected by attorney-client privilege. Legal services are provided exclusively by Gray Reed attorneys.")

def checklist(items, cols=2):
    return f'<ul class="checklist cols-{cols}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def section(inner, cls="section", sid=""):
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="{cls}"{idattr}><div class="wrap">{inner}</div></section>'

def shead(eyebrow, title, text=""):
    return f'<div class="s-head"><div><div class="eyebrow">{eyebrow}</div><h2>{title}</h2></div><p>{text}</p></div>'

def jumpnav(items):
    return '<nav class="jumpnav" aria-label="On this page"><div class="wrap">' + "".join(f'<a href="#{i}">{t}</a>' for i, t in items) + "</div></nav>"

# ----------------------------------------------------------------------------- Crisis Command
def crisis_page(site):
    s = SOLUTIONS["crisis-command"]
    home = SITES[site]["name"]
    hero = page_hero(f'<a href="index.html">{home}</a><span>/</span>Solutions<span>/</span>Crisis Command',
                     "Integrated solution · with Gray Reed", "Crisis Command", s["lead"],
                     '<div class="badge">Readiness <b>·</b> Response <b>·</b> Recovery</div>')
    nav = jumpnav([("approach", "Our Approach"), ("readiness", "Readiness"), ("first-15", "The First 15"), ("next-48", "The Next 48"),
                   ("response", "Response"), ("recovery", "Recovery"), ("industries", "Industries"), ("contacts", "Contacts")])
    intro = section(f'''<div class="split">
      <div><div class="eyebrow">Why it matters</div><h2>Preparation decides <br>the outcome.</h2></div>
      <div class="prose">
        <p class="intro">Organizations don’t fail during a crisis because they lack capable people. They fail because the critical decisions — who’s in charge, what gets preserved, who talks to the media, when legal counsel engages — were never resolved before the pressure hit.</p>
        <p>Crisis Command is Gray Reed’s integrated crisis readiness, response and recovery offering. We help you build the structures, plans and capabilities your organization needs to navigate high-stakes events — before they happen, so you’re ready when they do.</p>
        <p>Whether you’re facing an industrial accident, a cybersecurity breach, executive misconduct allegations, a regulatory investigation, workforce disruptions or a reputational threat, one thing determines whether your organization emerges intact: preparation.</p>
      </div></div>''')
    approach = section(f'''{shead("Our approach", "One coordinated approach. <br>Not five vendors.", "In most crisis engagements, organizations scramble to coordinate legal counsel, a PR firm, government affairs consultants and technical experts — none of whom have worked together before. That model fails precisely when it matters most: the first hours.")}
      <div class="split" style="align-items:start">
        <div class="prose"><p>Gray Reed attorneys work in close coordination with GRPR — the public affairs and strategic communications division of Gray Reed Advisory — from day one. Not as separate vendors introduced during chaos. Not as firms exchanging emails while the clock runs.</p>
        <p>The team includes experienced litigators, labor and employment attorneys, government investigations counsel and cybersecurity advisors, integrated with GRPR’s crisis communications and government relations professionals — all aligned under one strategy.</p></div>
        <ul class="points">
          <li><span class="pn">01</span><div><h4>Both risks, evaluated together</h4><p>A legally sound decision can create reputational consequences. A public statement can create legal exposure. We evaluate both — in real time — so you don’t solve one problem by creating another.</p></div></li>
          <li><span class="pn">02</span><div><h4>A team that already knows your plan</h4><p>One strategy that accounts for legal risk, regulatory scrutiny, workforce concerns, public perception and stakeholder expectations simultaneously.</p></div></li>
          <li><span class="pn">03</span><div><h4>No gaps. No conflicting advice.</h4><p>No wasted hours getting outside advisors “up to speed” while the situation escalates.</p></div></li>
        </ul>
      </div>''', "section wash", "approach")
    track = section(f'''{shead("Track record", "Guidance through the hardest moments.", "Crisis Command professionals have guided organizations through some of the most challenging situations they will ever face — and helped them use the experience to build more resilient operations.")}
      {checklist(["Industrial accidents and catastrophic incidents", "OSHA, DOJ, SEC, DOL, EEOC, IRS and DOT investigations", "Cybersecurity and data breach events", "Workplace fatalities", "Executive misconduct investigations", "Public entity and school district crises", "High-profile litigation matters", "Mass-casualty incidents", "Reputation recovery efforts", "Long-term governance and compliance transformations"], 2)}''')
    readiness = section(f'''{shead("Crisis readiness", "Build the capability <br>before you need it.", "When a crisis hits, your leadership team must make decisions in minutes — not hours. We don’t hand you a binder. We build your team’s ability to perform under real pressure.")}
      {checklist(["Crisis readiness assessments and gap analysis", "Risk and exposure evaluations tailored to your industry", "Crisis communications planning and spokesperson preparation", "Incident response protocols and activation procedures", "Government investigation and regulatory preparedness", "Cybersecurity readiness reviews", "Workforce incident planning", "Tabletop exercises and live simulations", "Board and executive crisis training"], 3)}
      <p class="cta-line">Every organization’s risk profile is different. <a class="link" href="contact.html">Talk to us about a readiness engagement <span class="arrow"></span></a></p>''', "section", "readiness")
    first15 = f'''<section class="band-dark" id="first-15"><div class="wrap">
      <div class="band-grid">
        <div><div class="eyebrow light">Framework</div><h2 class="band-title">The First 15</h2>
          <p class="band-lead">The earliest minutes of a crisis determine the trajectory of everything that follows. The First 15 is Crisis Command’s framework for establishing command, preserving critical information, coordinating decision-makers and maintaining control during the opening stage of an incident.</p>
          <p class="band-note">The objective: clarity, discipline and control — before competing narratives and external pressures begin to dictate the conversation.</p></div>
        <ol class="numbered light">{"".join(f"<li>{x}</li>" for x in ["Activate leadership and crisis response teams", "Establish clear decision authority", "Preserve evidence and critical records", "Confirm known facts and identify information gaps", "Evaluate immediate legal and regulatory obligations", "Coordinate internal and external messaging", "Prepare for government, regulator or media engagement", "Align legal, communications and operational decision-making"])}</ol>
      </div></div></section>'''
    next48 = section(f'''{shead("Signature simulation", "The Next 48: test your team before a real crisis does.", "Most organizations have a crisis plan. Far fewer have tested it. The Next 48 is a rigorous, scenario-based executive simulation built around your specific operational, legal, workforce and reputational risks — beginning with First 15 activation and running through the first two days of a simulated crisis.")}
      <div class="two-col-cards">
        <div class="card-plain"><h4>Participants experience</h4>{checklist(["Breaking news coverage and media inquiries", "Social media escalation", "Employee concerns and workforce disruptions", "Government investigations and regulator engagement", "Stakeholder demands and board-level pressure", "Legal and operational decisions under time constraints"], 1)}</div>
        <div class="card-plain"><h4>Every engagement delivers</h4>{checklist(["First 15 activation procedures customized to your organization", "Crisis governance and decision-authority recommendations", "Communications playbook guidance", "Response improvement priorities", "Recovery planning considerations", "Long-term risk mitigation recommendations"], 1)}</div>
      </div>
      <p class="cta-line">This is not a conference room presentation. <a class="link" href="contact.html">Schedule a Next 48 simulation <span class="arrow"></span></a></p>''', "section wash", "next-48")
    response = section(f'''<div class="split" style="align-items:start">
      <div><div class="eyebrow">Crisis response</div><h2>When the call comes.</h2>
        <p style="color:var(--slate);margin-top:22px">No matter how prepared you are, the call will come. When an incident occurs, Crisis Command activates immediately to manage the legal, communications, operational and regulatory pressures that emerge — often simultaneously — while maintaining confidence among employees, regulators, customers, investors, governing bodies and the public.</p>
        <div class="card red" style="margin-top:28px"><h4>In a crisis now?</h4><p>Reach out for an immediate, confidential conversation.</p><a class="btn white sm" href="contact.html">Contact Us <span class="arrow"></span></a></div></div>
      {checklist(["Crisis communications and media relations", "Government investigations and enforcement matters", "Internal investigations", "Labor and employment issues", "Executive and witness preparation", "Regulatory response and agency engagement", "Cyber incident response and breach management", "Litigation risk assessment and early case evaluation", "Stakeholder and investor communications", "Coordination of technical consultants and outside experts"], 1)}</div>''', "section", "response")
    recovery = section(f'''<div class="split" style="align-items:start">
      <div><div class="eyebrow">Recovery</div><h2>Emerge stronger <br>than before.</h2>
        <p style="color:var(--slate);margin-top:22px">A crisis doesn’t end when media attention fades. Recovery means addressing the underlying issues, rebuilding trust with stakeholders, strengthening governance and improving future preparedness.</p>
        <p class="pull">Our goal is not simply helping you recover. It is helping your organization emerge stronger and more prepared than it was before.</p></div>
      {checklist(["Root-cause analysis and remediation planning", "Regulatory compliance improvements", "Litigation management and resolution strategy", "Reputation restoration and stakeholder outreach", "Governance enhancements and leadership development", "Policy and procedure improvements", "Future readiness planning and ongoing monitoring"], 1)}</div>''', "section wash", "recovery")
    inds = [("Energy, Petrochemical &amp; Industrial Operations", "Industrial incidents, workplace safety events, environmental matters, regulatory investigations and business continuity challenges — where scrutiny is immediate and unforgiving."),
            ("Construction &amp; Infrastructure", "Workplace fatalities, OSHA investigations, contractor disputes, project disruptions and workforce issues across complex multi-party relationships."),
            ("Healthcare", "Cybersecurity incidents, patient safety concerns, regulatory investigations, workforce challenges and reputation management — with public trust and patient impact on the line."),
            ("Municipalities &amp; Public Entities", "Public trust events, emergency response failures, workforce issues, officer-involved incidents, policy controversies and media scrutiny."),
            ("Public Companies, Family Offices &amp; Closely Held Businesses", "Leadership transitions, executive misconduct allegations, employment disputes, governance matters and reputational threats — where business and personal reputation often merge."),
            ("Financial Services", "Data breaches, cyberattacks, fraud investigations, compliance failures, regulatory inquiries and customer-facing incidents, where confidence and oversight are inseparable.")]
    industries = section(f'''{shead("Industries we serve", "Where the stakes <br>are highest.", "We work across industries where regulatory scrutiny is intense, public trust is essential and a single incident can escalate into an enterprise-wide challenge.")}
      <div class="ind-grid">{"".join(f'<article class="ind reveal"><h3>{t}</h3><p>{d}</p></article>' for t, d in inds)}</div>''', "section", "industries")
    paths = [("Building readiness", "We start with a focused assessment, identify gaps and priorities, and design a readiness program tailored to your industry, leadership structure and risk environment.", "Most assessments complete within 6 weeks"),
             ("In crisis", "We activate immediately. Our team is structured to deploy coordinated legal, communications and operational guidance from the first call forward.", "Immediate activation"),
             ("In recovery", "We help you move from response mode to long-term resilience — addressing root causes, rebuilding stakeholder trust and strengthening your organization.", "Long-term resilience")]
    how = section(f'''{shead("How we work", "Every engagement starts with a confidential conversation.", "About your organization’s current state of readiness, risk profile and objectives.")}
      <div class="services three">{"".join(f'<article class="svc reveal"><div class="num">0{i}</div><h3>{t}</h3><p>{d}</p><div class="tag" style="margin:auto 0 0;padding-top:18px;color:var(--red)">{m}</div></article>' for i, (t, d, m) in enumerate(paths, 1))}</div>''', "section wash")
    contacts = section(f'''{shead("Contacts", "Who to call", "A coordinated team across Gray Reed and GRPR.")}
      <div class="people">{"".join(person_card(k) for k in s["people"])}</div>
      <p class="disclaimer">{GRPR_DISCLAIMER}</p>''', "section", "contacts")
    body = hero + nav + intro + approach + track + readiness + first15 + next48 + response + recovery + industries + how + contacts + related_insights(site, ["Crisis"]) + cta(site, "Ready before", "the call comes?", "Whether you’re building readiness or navigating a crisis right now, Crisis Command is ready.")
    page(site, "crisis-command", f"Crisis Command | {SITES[site]['name']}", s["short"], body)

# ----------------------------------------------------------------------------- GRIDS
def grids_page(site):
    s = SOLUTIONS["grids"]
    home = SITES[site]["name"]
    hero = page_hero(f'<a href="index.html">{home}</a><span>/</span>Solutions<span>/</span>GRIDS',
                     "Integrated solution · Texas data centers", "GRIDS", s["lead"],
                     '<div class="badge">Gray Reed <b>+</b> GRPR <b>+</b> Gray Reed Advisory</div>')
    nav = jumpnav([("overview", "Overview"), ("g", "G"), ("r", "R"), ("i", "I"), ("d", "D"), ("s", "S"), ("experience", "Experience"), ("difference", "Why GRIDS"), ("team", "Team")])
    overview = section(f'''<div class="split">
      <div><div class="eyebrow">Overview</div><h2>Data center development is not a single-practice matter.</h2></div>
      <div class="prose">
        <p class="intro">A project that starts as a land acquisition quickly involves water rights, construction contracts, power agreements, tax incentives and, increasingly, regulatory and legislative strategy — as well as how the project is perceived by the communities where it is being built.</p>
        <p>Gray Reed’s GRIDS Initiative brings each of those disciplines together under one coordinated team: Gray Reed attorneys, the government relations and public relations expertise of GRPR, and the cybersecurity and data privacy capabilities of Gray Reed Advisory — serving landowners, investors, developers and operators.</p>
      </div></div>
      <div class="acronym">{"".join(f'<a href="#{l.lower()}"><b>{l}</b><span>{t}</span></a>' for l, t in [("G", "Government Affairs &amp; Public Relations"), ("R", "Real Estate"), ("I", "Infrastructure"), ("D", "Development"), ("S", "Security (Cyber &amp; Data)")])}</div>''', "section", "overview")

    def letter(l, title, sub, content, cls="section"):
        return f'''<section class="{cls} letter-sec" id="{l.lower()}"><div class="wrap"><div class="letter-grid">
          <div class="letter-head"><span class="big-letter">{l}</span><div><div class="eyebrow">{sub}</div><h2>{title}</h2></div></div>
          <div class="prose">{content}</div></div></div></section>'''

    g = letter("G", "Government Affairs &amp; Public Relations", "Delivered by GRPR", f'''
      <p class="intro">Texas legislators and regulators are deciding right now on water use, permitting, tax incentives and power infrastructure that will shape the data center industry for decades. At the same time, communities are forming strong opinions — welcoming the investment in some areas and pushing back hard in others.</p>
      <h3>Government Affairs</h3>
      <p>GRPR builds tailored advocacy strategies, gets clients in front of the right decision makers and monitors the thousands of bills and amendments filed each session. The team is led by Austin-based Adam Leggett, recognized in Capitol Inside’s 2025 Texas Lobby Power Rankings, with a record on infrastructure, technology, natural resources and utilities issues.</p>
      <h3>Public Relations</h3>
      <p>Led by Marc Rylander, our public relations team helps clients shape how data center projects are understood by communities, stakeholders and policymakers — monitoring sentiment, anticipating emerging issues and telling the full story, from economic benefits to building the community support needed to move projects forward.</p>''', "section wash letter-sec")
    r = letter("R", "Real Estate", "Gray Reed attorneys", f'''
      <h3>Land Acquisition &amp; Leaseholds</h3>
      <p>Our real estate team — including three attorneys board-certified in commercial real estate law and recognized in the Chambers USA 2025 guide — handles every aspect of site work: land acquisition and options, title, easements, land use, entitlements, financing and disposition, as well as real estate disputes.</p>
      <h3>Water Law</h3>
      <p>Water supply and water resources are key issues for Texas data centers. We advise on:</p>
      {checklist(["Groundwater ownership, the Rule of Capture and Groundwater Conservation District regulation", "Severed groundwater estates, Surface Use Agreements and title due diligence", "Surface water rights and TCEQ permitting", "Brackish groundwater and produced water as alternative industrial supplies", "Water rights reservations in deeds and acquisition documents", "Water supply, transport, recycling and disposal agreements"], 1)}''')
    i_ = letter("I", "Infrastructure", "Gray Reed attorneys", f'''
      <h3>Energy &amp; Power Transactions</h3>
      <p>For landowners, we help position property to be as attractive as possible to developers before a deal is struck — surface use waivers from mineral owners, natural gas availability, access and easement arrangements, and title issues that could complicate site selection, option, sale or lease.</p>
      <p>For developers and operators, we advise on the full range of power-related legal work large-scale facilities require:</p>
      {checklist(["ERCOT large-load interconnection requirements and the Large Load Interconnection Process (LLIP)", "Power purchase agreements and direct energy contracts", "EPC agreements for power generation facilities and related O&amp;M agreements", "Transmission, distribution and grid interconnection matters", "Natural gas supply and transportation for onsite generation", "Surface use and facilities agreements", "Regulatory compliance and reporting obligations"], 1)}
      <h3>Construction Law</h3>
      <p>Our construction team handles the full lifecycle of complex industrial builds — contracts, claims, liens, scheduling and delays, defective work and OSHA matters — for owners, contractors, subcontractors and suppliers. The practice received national and metropolitan recognition in Best Lawyers’ 2026 “Best Law Firms” ranking.</p>''', "section wash letter-sec")
    d = letter("D", "Development", "Gray Reed attorneys", f'''
      <h3>Corporate / Mergers &amp; Acquisitions</h3>
      <p>Recognized by Chambers USA and Best Lawyers and ranked sixth in deal volume by The Texas Lawbook, our M&amp;A team advises buyers, sellers, investors and private equity sponsors on data center development, project financing, joint ventures, recapitalizations and divestitures.</p>
      <h3>Tax Planning</h3>
      <p>Our tax team, which includes several former Big Four professionals, advises on economic development agreements, ad valorem exemptions, entity structuring, sale-leaseback arrangements, opportunity zones and federal energy tax credits.</p>''')
    s_ = letter("S", "Security (Cyber &amp; Data)", "Delivered by Gray Reed Advisory", f'''
      <p class="intro">Cybersecurity and data privacy planning begin well before the first shovel hits the dirt.</p>
      <p>From site selection and contract drafting through construction, commissioning and ongoing operations, Gray Reed Advisory’s cybersecurity and data privacy team helps clients build and operate data centers that meet the security and compliance standards required by customers, counterparties and regulators:</p>
      {checklist(["Certification planning", "Compliance with Texas, U.S. and international data privacy laws", "NERC audit preparedness", "Data breach prevention and response", "Vendor and cloud agreement management"], 2)}''', "section wash letter-sec")
    exp = ["Represent landowners in joint venture and co-investment planning for data center development.",
           "Represent a data center developer negotiating equity funding from a private equity sponsor.",
           "Represent investors, developers and landowners in complex tax planning, special allocations of depreciation and project exit planning.",
           "Secure local tax incentives for a data center developer.",
           "Represent a developer in a complex payment dispute with the general contractor on a large-scale data center.",
           "Negotiate construction contracts for subcontractors and suppliers on data center projects.",
           "Represent a capital provider funding natural gas pipeline development for a co-located power plant within a large data center project.",
           "Represent a large landowner negotiating land use and co-investment with a developer planning on-site gas, generation and transmission infrastructure.",
           "Provide comprehensive public relations and communications for a Colorado-based operator developing three Texas facilities — community engagement, stakeholder and elected-official outreach, media relations, social media and issues readiness. <em class=\"tagline\">Services provided by GRPR</em>"]
    experience = section(f'''{shead("Our data center experience", "Representative matters", "")}
      <ol class="matters">{"".join(f"<li>{x}</li>" for x in exp)}</ol>''', "section", "experience")
    diff = [("Power at scale", "Our energy team has structured and closed some of the most complex power transactions in the Americas — directly relevant as developers pursue dedicated power outside the traditional grid."),
            ("Texas-specific depth", "Careers spent in Texas water, real estate, energy and construction law and regulatory politics — the frameworks every data center project depends on."),
            ("Early-lifecycle focus", "We work with landowners, developers and investors before sites are under contract, permits are pulled or power agreements are signed."),
            ("Legislative reach", "Through GRPR, clients have a voice in the policy conversations shaping the industry, led by a former Texas Senate chief of staff."),
            ("Community &amp; public affairs", "GRPR helps clients shape how projects are understood by communities, elected officials and media — getting ahead of opposition or navigating it."),
            ("Built for what’s coming", "Water regulation, interconnection rules and tax incentives are all in flux. We track these developments in real time.")]
    difference = section(f'''{shead("What sets us apart", "Why GRIDS", "")}
      <div class="ind-grid">{"".join(f'<article class="ind reveal"><h3>{t}</h3><p>{x}</p></article>' for t, x in diff)}</div>''', "section wash", "difference")
    team = section(f'''{shead("Key initiative members", "Who to call", "Gray Reed attorneys working alongside GRPR and Gray Reed Advisory.")}
      <div class="people">{"".join(person_card(k) for k in ["cooney", "crady", "leggett", "rylander"])}</div>
      <p class="disclaimer">{GRPR_DISCLAIMER}</p>''', "section", "team")
    body = hero + nav + overview + g + r + i_ + d + s_ + experience + difference + team + related_insights(site, ["GRIDS"]) + cta(site, "Planning a Texas", "data center?", "Talk with the GRIDS team early — before sites are under contract and permits are pulled.")
    page(site, "grids", f"GRIDS | {SITES[site]['name']}", s["short"], body)

# ----------------------------------------------------------------------------- Insights library
# To add an item: append a dict. type = Article | Video | News. For videos, give "youtube" (the video ID)
# and a "slug"; a page video-<slug>.html is generated. sites = which sites list it.
INSIGHTS = [
  dict(type="Article", date="2026-09-17", tags=["GRIDS", "Government Affairs"], sites=["grpr", "gray-reed-advisory"],
       title="Governor Abbott Directs TWDB to Enforce Water Use Reporting Requirements Against Data Centers and Major Water Users",
       byline="Gray Reed’s GRIDS Initiative · Legal alert in collaboration with GRPR",
       summary="What the Governor’s directive on water-use reporting — and coordination with ERCOT’s interconnection audit — means for data center developers and other large water users.",
       url=GR_TL + "Thought-Leadership/291202/Governor-Abbott-Directs-TWDB-to-Enforce-Water-Use-Reporting-Requirements-Against-Data-Centers-and-Major-Water-Users-Orders-Coordination-with-ERCOT-Interconnection-Audit"),
  dict(type="Article", date="2026-09-08", tags=["Crisis", "Public Relations"], sites=["grpr", "gray-reed-advisory"],
       title="From HR Problem to PR Crisis: Why Serious Workplace Issues Demand a Joint Legal and Communications Response",
       byline="Marcus Fettinger, Gray Reed · Charlie Rose, GRPR",
       summary="The six mistakes companies make when a serious workplace complaint turns into a reputational threat — and why legal counsel and communications need to move together.",
       url=GR_TL + "Thought-Leadership/290802/From-HR-Problem-to-PR-Crisis-Why-Serious-Workplace-Issues-Demand-a-Joint-Legal-and-Communications-Response"),
  dict(type="Article", date="2026-07-28", tags=["GRIDS", "Government Affairs"], sites=["grpr", "gray-reed-advisory"],
       title="Data Centers and Water Collide in Texas",
       byline="Gray Reed legal alert in collaboration with GRPR",
       summary="Why water supply has become one of the defining policy and permitting questions for Texas data center projects.",
       url=GR_TL + "Thought-Leadership/287602/Data-Centers-and-Water-Collide-in-Texas"),
  dict(type="Article", date="2026-06-10", tags=["GRIDS", "Government Affairs"], sites=["grpr", "gray-reed-advisory"],
       title="Governor Abbott Directs Major Shift in Texas Data Center Policy",
       byline="Gray Reed’s GRIDS Initiative · in collaboration with GRPR",
       summary="A look at the Governor’s policy direction on data centers and what developers, operators and landowners should watch next.",
       url=GR_TL + "Thought-Leadership/285502/Governor-Abbott-Directs-Major-Shift-in-Texas-Data-Center-Policy"),
  dict(type="Article", date="2026-04-14", tags=["GRIDS", "Government Affairs"], sites=["grpr", "gray-reed-advisory"],
       title="Texas Legislature Targets Data Center Growth: What Industry Stakeholders Need to Know",
       byline="Gray Reed legal alert in collaboration with GRPR",
       summary="The legislative activity aimed at data center growth in Texas and how industry stakeholders can prepare.",
       url=GR_TL + "Thought-Leadership/282102/Texas-Legislature-Targets-Data-Center-Growth-What-Industry-Stakeholders-Need-to-Know"),
  dict(type="News", date="2026-04-21", tags=["GRIDS", "Firm News"], sites=["grpr", "gray-reed-advisory"],
       title="Gray Reed Launches GRIDS Initiative to Serve Texas Data Center Market",
       byline="Press release", summary="Gray Reed attorneys, GRPR and Gray Reed Advisory come together to serve landowners, investors, developers and operators.",
       url=GR_TL + "Press-Releases/282502/Gray-Reed-Launches-GRIDS-Initiative-to-Serve-Texas-Data-Center-Market"),
  dict(type="News", date="2025-02-20", tags=["Government Affairs", "Firm News"], sites=["grpr", "gray-reed-advisory"],
       title="GRPR Recognized in 2025 Capitol Inside Texas Lobby Power Rankings",
       byline="Press release", summary="GRPR earns a place among the top lobbyists in Texas in Capitol Inside’s 2025 rankings.",
       url=GR_TL + "Press-Releases/263405/GRPR-Recognized-in-2025-Capitol-Inside-Texas-Lobby-Power-Rankings"),
  dict(type="News", date="2024-03-20", tags=["Government Affairs", "Firm News"], sites=["grpr", "gray-reed-advisory"],
       title="Gray Reed Advisory Welcomes Government Affairs Leader",
       byline="Press release", summary="Austin-based Adam Leggett joins to lead the expansion of GRPR’s government affairs practice.",
       url=GR_TL + "Press-Releases/244002/Gray-Reed-Advisory-Welcomes-Government-Affairs-Leader"),
  dict(type="News", date="2024-01-09", tags=["Public Relations", "Firm News"], sites=["grpr", "gray-reed-advisory"],
       title="Gray Reed Announces Expansion of Gray Reed Advisory Services with Public Affairs Division",
       byline="Press release", summary="Marc Rylander joins to lead GRPR, Gray Reed Advisory’s strategic communications division.",
       url=GR_TL + "Press-Releases/241301/Gray-Reed-Announces-Expansion-of-Gray-Reed-Advisory-Services-with-Public-Affairs-Division"),
  # ---- Video series: Marc Rylander (PR). EDIT: paste each video's YouTube ID, title, date and summary.
  dict(type="Video", date="2026-09-01", tags=["Public Relations", "Crisis"], sites=["grpr", "gray-reed-advisory"], slug="rylander-01", youtube="",
       title="Video title — Marc Rylander on crisis communications", byline="Marc Rylander, Chief Communications Officer, GRPR",
       summary="Placeholder — one or two sentences on what the video covers.", url=GR_TL + "Videos", ph=True,
       takeaways=["Placeholder takeaway one", "Placeholder takeaway two", "Placeholder takeaway three"]),
  dict(type="Video", date="2026-08-15", tags=["Public Relations"], sites=["grpr", "gray-reed-advisory"], slug="rylander-02", youtube="",
       title="Video title — Marc Rylander on reputation management", byline="Marc Rylander, Chief Communications Officer, GRPR",
       summary="Placeholder — one or two sentences on what the video covers.", url=GR_TL + "Videos", ph=True,
       takeaways=["Placeholder takeaway one", "Placeholder takeaway two", "Placeholder takeaway three"]),
  dict(type="Video", date="2026-08-01", tags=["Public Relations"], sites=["grpr", "gray-reed-advisory"], slug="rylander-03", youtube="",
       title="Video title — Marc Rylander on media training", byline="Marc Rylander, Chief Communications Officer, GRPR",
       summary="Placeholder — one or two sentences on what the video covers.", url=GR_TL + "Videos", ph=True,
       takeaways=["Placeholder takeaway one", "Placeholder takeaway two", "Placeholder takeaway three"]),
]

import datetime
def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B ") + str(d.day) + d.strftime(", %Y")

def site_insights(site, tags=None, types=None):
    items = [x for x in INSIGHTS if site in x["sites"]]
    if tags: items = [x for x in items if set(tags) & set(x["tags"])]
    if types: items = [x for x in items if x["type"] in types]
    return sorted(items, key=lambda x: x["date"], reverse=True)

def insight_card(x):
    tags = "|" + "|".join(x["tags"]) + "|"
    if x["type"] == "Video":
        href, ext = f'video-{x["slug"]}.html', ""
        thumb = (f'<div class="ins-thumb"><img src="https://i.ytimg.com/vi/{x["youtube"]}/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></div>'
                 if x.get("youtube") else '<div class="ins-thumb ph"><span class="play"></span><small>Video</small></div>')
    else:
        href, ext, thumb = x["url"], ' target="_blank" rel="noopener"', ""
    src = '<span class="ins-src">grayreed.com <span aria-hidden="true">↗</span></span>' if x["type"] != "Video" else '<span class="ins-src">Watch <span class="arrow"></span></span>'
    return f'''<a class="ins-card reveal{' is-ph' if x.get('ph') else ''}" href="{href}"{ext} data-tags="{tags}" data-type="{x['type']}">
      {thumb}<div class="ins-meta"><span class="ins-type">{x['type']}</span><span>{fmt_date(x['date'])}</span></div>
      <h3>{x['title']}</h3><p>{x['summary']}</p><div class="ins-by">{x['byline']}</div>{src}</a>'''

def related_insights(site, tags, title="Related insights"):
    items = [x for x in site_insights(site, tags) if not x.get("ph")][:3]
    if not items: return ""
    return section(f'''{shead("Insights", title, '<a class="link" href="insights.html">All insights <span class="arrow"></span></a>')}
      <div class="ins-grid">{"".join(insight_card(x) for x in items)}</div>''', "section wash")

def insights_page(site):
    items = [x for x in site_insights(site) if not x.get("ph")]
    tags = []
    for x in items:
        for t in x["tags"]:
            if t not in tags: tags.append(t)
    chips = '<button type="button" class="chip is-on" data-filter="*">All</button>' + \
            "".join(f'<button type="button" class="chip" data-filter="type:{t}">{lbl}</button>' for t, lbl in [("Article", "Articles"), ("Video", "Videos"), ("News", "News")] if any(x["type"] == t for x in items)) + \
            '<span class="chip-sep"></span>' + "".join(f'<button type="button" class="chip" data-filter="tag:{t}">{t}</button>' for t in tags)
    videos = site_insights(site, types=["Video"])
    vid_sec = section(f'''{shead("Video series", "Marc Rylander on communications", "Short conversations on crisis communications, reputation and media — with more episodes added over time.")}
      <div class="ins-grid">{"".join(insight_card(x) for x in videos)}</div>''', "section wash", "videos") if videos else ""
    body = page_hero(f'<a href="index.html">{SITES[site]["name"]}</a><span>/</span>Insights', "Insights", "Insights &amp; perspectives.",
                     "Analysis, alerts and video from GRPR, Gray Reed Advisory and Gray Reed attorneys on policy, reputation, crisis and risk.", "")
    body += vid_sec
    body += section(f'''<div class="filters" role="toolbar" aria-label="Filter insights">{chips}</div>
      <div class="ins-grid" data-insights>{"".join(insight_card(x) for x in items)}</div>
      <p class="note" data-empty hidden>No items match this filter yet.</p>''', "section", "all")
    body += cta(site, "Want our perspective", "on your issue?", "Talk with the team behind these insights.")
    page(site, "insights", f"Insights | {SITES[site]['name']}", "Insights from GRPR and Gray Reed Advisory.", body)

def video_page(site, x):
    embed = (f'<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/{x["youtube"]}?rel=0" title="{x["title"]}" loading="lazy" '
             f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>') if x.get("youtube") else \
            '<div class="video-frame ph"><span class="play"></span><small>Video embed — add the YouTube ID in the INSIGHTS list (or paste the embed code here)</small></div>'
    more = [v for v in site_insights(site, types=["Video"]) if v is not x][:3]
    body = f'''<section class="page-hero video-hero"><div class="wrap">
      <div class="crumbs"><a href="index.html">{SITES[site]["name"]}</a><span>/</span><a href="insights.html">Insights</a><span>/</span>Video</div>
      <div class="eyebrow">Video · {fmt_date(x["date"])}</div><h1 class="video-title">{x["title"]}</h1>
      {embed}</div></section>
<section class="section"><div class="wrap detail">
  <div class="prose">
    <!-- EDIT: video summary, takeaways and transcript -->
    <p class="intro">{x["summary"]}</p>
    <h2>Key takeaways</h2>
    <ul class="caps">{"".join(f'<li><span class="cn">{i:02d}</span><div><p style="color:var(--ink);font-size:17px">{t}</p></div></li>' for i, t in enumerate(x.get("takeaways", []), 1))}</ul>
    <h2>Transcript</h2>
    <details class="transcript"><summary>Show transcript</summary><p>Placeholder — paste the video transcript here. Transcripts help search engines and AI answer engines understand the video.</p></details>
  </div>
  <aside class="aside">
    <div class="card"><h4>Featuring</h4>{mini("rylander")}</div>
    <div class="card red"><h4>Talk with GRPR</h4><p>Facing a communications challenge?</p><a class="btn white sm" href="contact.html">Contact Us <span class="arrow"></span></a></div>
    <div class="card related"><h4>Topics</h4>{"".join(f'<a href="insights.html#all">{t} <span class="arrow"></span></a>' for t in x["tags"])}</div>
  </aside>
</div></section>'''
    if more:
        body += section(f'''{shead("More videos", "Keep watching", '<a class="link" href="insights.html#videos">All videos <span class="arrow"></span></a>')}
          <div class="ins-grid">{"".join(insight_card(v) for v in more)}</div>''', "section wash")
    body += cta(site)
    page(site, f"video-{x['slug']}", f"{x['title']} | {SITES[site]['name']}", x["summary"], body)

def latest_insights(site):
    items = [x for x in site_insights(site) if not x.get("ph")][:3]
    return section(f'''{shead("Insights", "Latest thinking", '<a class="link" href="insights.html">All insights <span class="arrow"></span></a>')}
      <div class="ins-grid">{"".join(insight_card(x) for x in items)}</div>''', "section wash")

def build_insights(site):
    insights_page(site)
    for x in site_insights(site, types=["Video"]):
        video_page(site, x)


def why_grpr_page():
    site = "grpr"
    body = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "why_grpr_body.html")).read()
    body += related_insights(site, ["Government Affairs", "Public Relations", "Crisis", "GRIDS"])
    body += cta(site, "Put policy and perception", "on one plan.", "Tell us what’s at stake. We’ll bring the right people from GRPR and Gray Reed to the table.")
    page(site, "why-grpr", "Why GRPR | GRPR", "Why organizations choose GRPR: government affairs and strategic communications on one plan, backed by Gray Reed.", body)

def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    for site in SITES:
        os.makedirs(os.path.join(OUT, site, "css"), exist_ok=True)
        os.makedirs(os.path.join(OUT, site, "js"), exist_ok=True)
        os.makedirs(os.path.join(OUT, site, "assets"), exist_ok=True)
        shutil.copy("site.css", os.path.join(OUT, site, "css", "site.css"))
        shutil.copy("site.js", os.path.join(OUT, site, "js", "site.js"))
        for k in SITES[site]["services"]:
            service_page(site, k)
        crisis_page(site)
        grids_page(site)
        build_insights(site)
        team_page(site)
        contact_page(site)
    home_gras()
    home_grpr()
    why_grpr_page()

if __name__ == "__main__":
    build()
    for root, _, files in os.walk(OUT):
        for f in sorted(files):
            print(os.path.join(root, f))
