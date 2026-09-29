# GRPR Interim Site

Plain HTML, CSS and JavaScript. There's no build step, framework or CMS. Upload the contents of `site/` to the web root of **grprpublicaffairs.com**. To preview, open `site/index.html` in a browser.

## Pages

| File | Page |
|---|---|
| why-grpr.html | Why GRPR (first item in the navigation) |
| index.html | Home. Hero slider: GA + PR together, then Government Affairs, then Public Relations |
| government-affairs.html | Government Affairs |
| public-relations.html | Public Relations |
| crisis-command.html | Crisis Command (with Gray Reed) |
| grids.html | GRIDS: Texas data centers |
| team.html | Our Team |
| insights.html | Insights: articles, news, videos |
| video-rylander-0X.html | Video pages (template, 3 placeholders) |
| contact.html | Contact |

See **GRPR - Content Gaps & Request List.md** for everything still needed.

## Before launch

1. **Logos.** For the mockup, the logos load from the current live sites (the GRPR WordPress uploads and grayreed.com). Download these three files into `assets/`. Then find and replace the URLs in every page:
   - `https://www.grprpublicaffairs.com/wp-content/uploads/sites/895/2023/08/Gray-Reed-Advisory-Services-LLC-logo-1.svg` → `assets/logo-gray-reed-advisory.svg`
   - `https://www.grprpublicaffairs.com/wp-content/uploads/sites/895/2023/08/grpr-logo-color.svg` → `assets/logo-grpr.svg`
   - `https://www.grayreed.com/templates/site/images/logo.png` → `assets/logo-gray-reed.png`

   Do this **before** the GRPR WordPress site is taken down. Otherwise the logo links will break.
2. **Hero photos.** Only the home page has hero imagery. Each has a slider with one slide per service (Government Affairs + Public Relations together, then each on its own). Slides advance every 7 seconds (`--slide-dur` in `css/site.css`), pause on hover, and can be picked from the tabs. Slide copy and images are set in `source/build.py` (`hero_slider`). Images are shown as colored-pencil sketches (`.sketch.color`). The browser draws the sketch effect with CSS (`.sketch` in `css/site.css`); to show the plain photos, remove the `sketch` class from `.hero-media`. The photos are free-license images from Unsplash (unsplash.com/license: free for commercial use, no credit required). For now they load from images.unsplash.com. The slide photos are listed in `source/build.py` under `IMG`. Before launch, download them into `assets/img/`, or swap in Gray Reed's own photography.
3. **Fonts.** grayreed.com uses **Gibson** (a licensed Monotype web font). The stylesheet already lists Gibson first. Until the Gibson kit is licensed for these domains, pages fall back to **Figtree** from Google Fonts.
4. **Placeholders to replace.** Search the pages for `EDIT:`, `Placeholder`, `[`, `Sample engagement`, `Illustrative` and `000.000.0000`:
   - Headshots and bio links. To add a photo, put `<img src="assets/people/name.jpg" alt="Name">` inside the `.photo` div.
   - Stats, sample engagements and the testimonial. These are mocked for now.
   - Office addresses and general inquiry email and phone.
   - Privacy Policy, Disclaimer and Sitemap links. The LinkedIn URL.
   - Sub-service copy marked "Placeholder —".
5. **Contact form.** It doesn't submit yet. Replace the `<form>` block in `contact.html` with your HubSpot embed, or point `action=` at your form handler.

## Insights (articles, news, videos)

The site has `insights.html`, which you can filter by type and topic. The home page, the service pages, Crisis Command and GRIDS each show the three most recent related items.

- **Articles and news** link to the full piece on grayreed.com.
- **Videos** get their own page on the site: `video-<slug>.html`. Each page has the embedded video, a summary, takeaways, a transcript area and "more videos".

**To add an item:** add an entry to `INSIGHTS` in `source/build.py`, then run `python3 build.py`. For a video, set `youtube` to the video ID and give it a `slug`. Remove `ph=True` once the entry is real. Placeholder entries only show in the Video Series block.

**Without Python:** copy an existing `video-*.html` file, change the title, date, summary and YouTube ID, and copy one card inside `insights.html`.

## Mobile

The site is responsive. They were checked at 320, 375, 414 and 768 px widths, with no sideways scrolling and no undersized tap targets.

- On phones the home slider puts the image first, with numbered slide tabs under it. Visitors can swipe to change slides.
- The header shrinks to 68 px and the menu opens full-screen.

## Styling

Every visual setting lives in `css/site.css`. Brand tokens are at the top (`:root`):

- Logo red `#A91D37`
- Charcoal `#2B2E34`
- Hairline gray `#E4E4E4`

The Gray Reed Advisory interim site uses the same stylesheet, so keep the two in sync.
