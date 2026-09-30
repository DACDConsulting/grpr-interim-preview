import { defineConfig } from 'vite';
import { cpSync, existsSync, mkdirSync } from 'node:fs';

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
  plugins: [
    {
      name: 'grpr-mobile-menu',
      transformIndexHtml(html) {
        if (html.includes('body.classList.toggle("nav-open")')) return html;
        return html.replace('</body>', MENU_SCRIPT + '\n</body>');
      },
      closeBundle() {
        if (!existsSync('dist')) mkdirSync('dist');
        if (existsSync('js')) cpSync('js', 'dist/js', { recursive: true });
        if (existsSync('css')) cpSync('css', 'dist/css', { recursive: true });
        if (existsSync('assets')) cpSync('assets', 'dist/assets', { recursive: true });
      }
    }
  ]
});
