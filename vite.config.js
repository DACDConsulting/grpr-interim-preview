import { defineConfig } from 'vite'

export default defineConfig({
  appType: 'mpa',
  publicDir: false,
  server: {
    host: true,
    port: 5173,
    strictPort: false
  }
})
