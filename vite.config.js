import { defineConfig } from 'vite';
import { readdirSync, cpSync, existsSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve('.');
const htmlPages = readdirSync(root).filter((f) => f.endsWith('.html'));
const input = Object.fromEntries(
  htmlPages.map((f) => [f.replace(/\.html$/, ''), resolve(root, f)])
);

const MENU_SCRIPT = `<script>
document.addEventListener("click",function(e){
  var t=e.target.closest&&e.target.closest(".menu-toggle");
  if(!t)return;
  if(t.tagName==="LABEL")return;
  var on=document.body.classList.toggle("nav-open");
  t.setAttribute("aria-expanded",on?"true":"false");
});
</script>`;

export default defineConfig({
  appType: 'mpa',
  publicDir: false,
  server: { host: true, port: 5173 },
  build: {
    rollupOptions: { input }
  },
  plugins: [
    {
      name: 'grpr-mpa',
      transformIndexHtml(html) {
        if (html.includes('body.classList.toggle("nav-open")')) return html;
        return html.replace('</body>', MENU_SCRIPT + '\n</body>');
      },
      closeBundle() {
        if (!existsSync('dist')) mkdirSync('dist');
        htmlPages.forEach((f) => {
          if (!existsSync(`dist/${f}`) && existsSync(f)) cpSync(f, `dist/${f}`);
        });
        if (existsSync('js')) cpSync('js', 'dist/js', { recursive: true });
        if (existsSync('css')) cpSync('css', 'dist/css', { recursive: true });
        if (existsSync('assets')) cpSync('assets', 'dist/assets', { recursive: true });
        if (existsSync('_redirects')) cpSync('_redirects', 'dist/_redirects');
        if (existsSync('netlify.toml')) cpSync('netlify.toml', 'dist/netlify.toml');
      }
    }
  ]
});
