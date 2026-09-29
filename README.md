# GRPR interim site preview

Working static preview of the GRPR interim website for Gray Reed attorney and marketing review (Pastel).

**Live site (after Pages is on):** https://dacdconsulting.github.io/grpr-interim-preview/

**Repo:** https://github.com/DACDConsulting/grpr-interim-preview

## Turn on GitHub Pages

1. Open [Settings → Pages](https://github.com/DACDConsulting/grpr-interim-preview/settings/pages)
2. Source: **GitHub Actions**
3. Re-run the **Deploy GitHub Pages** workflow if it has not published yet

Alternatively: Source **Deploy from a branch**, branch `gh-pages`, folder `/`.

## Local preview

```bash
# from this repo, after the site files are on main:
python3 -m http.server 8000
# open http://127.0.0.1:8000
```

Or unzip `GRPR-Interim-Site_3.zip` and open `GRPR-Interim-Site/site/index.html`.

## Pages

| File | Page |
|---|---|
| `index.html` | Home — GA + PR slider |
| `why-grpr.html` | Why GRPR |
| `government-affairs.html` | Government Affairs |
| `public-relations.html` | Public Relations |
| `crisis-command.html` | Crisis Command |
| `grids.html` | GRIDS |
| `team.html` | Our Team |
| `insights.html` | Insights |
| `video-rylander-0X.html` | Video templates |
| `contact.html` | Contact |

Stack: plain HTML, `css/site.css`, `js/site.js`. No framework.
