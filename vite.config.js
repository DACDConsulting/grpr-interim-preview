import { defineConfig } from 'vite'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = dirname(fileURLToPath(import.meta.url))

const pages = [
  'index',
  'why-grpr',
  'government-affairs',
  'public-relations',
  'crisis-command',
  'grids',
  'team',
  'insights',
  'contact',
  'video-rylander-01',
  'video-rylander-02',
  'video-rylander-03',
]

export default defineConfig({
  appType: 'mpa',
  server: {
    host: true,
    port: 5173,
    open: '/index.html',
  },
  build: {
    rollupOptions: {
      input: Object.fromEntries(
        pages.map((name) => [name, resolve(root, `${name}.html`)])
      ),
    },
  },
})
