# Open this project in Bolt.new

This repo is a **multi-page static HTML site**, not a React app.

## Import again (required)

1. In Bolt, start a **new** project from GitHub.
2. Choose `DACDConsulting/grpr-interim-preview` branch **main**.
3. Wait until `npm install` and `npm run dev` finish.
4. Preview should open `index.html` — Influence the policy. *Own* the story.

If Bolt scaffolds React (`src/App.tsx`) instead, paste the prompt below.

## Prompt to paste into Bolt

```
This repo is already a finished multi-page static website. Do NOT convert it to React, Next.js, or Tailwind.

Keep these files exactly:
- index.html and the other *.html pages at the repo root
- css/site.css
- js/site.js
- package.json and vite.config.js (Vite MPA so the preview works)

Run: npm install && npm run dev
The preview must load index.html.
Do not create src/App.tsx. Do not replace the stylesheet. Do not change copy, layout, or colors.
If the preview is blank, point Vite at the root index.html and restart the dev server.
```
