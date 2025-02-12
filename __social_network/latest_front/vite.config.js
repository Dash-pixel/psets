import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import svgr from "vite-plugin-svgr";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svgr(), react()],
  build: {
    //minify: false,  // Disables minification
    outDir: '../network/static/network',
    //sourcemap: true,
    rollupOptions: {
      input: 'src/main.jsx',
      output: {
      entryFileNames: 'main.js'
      },
    }
  },
  server: {
    origin: 'http:localhost:5173',
    proxy: {
      '/api': 'http://localhost:8000', // Django
    }
  }
})