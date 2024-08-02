import { fileURLToPath, URL } from 'node:url'; // Import Node.js utilities for handling file URLs
import { defineConfig } from 'vite'; // Import Vite configuration function
import vue from '@vitejs/plugin-vue';  // Import Vite plugin for Vue.js

export default defineConfig({
    // Configuration for Vite
  plugins: [vue()], // Use the Vue.js plugin for handling .vue files
  resolve: {
    alias: {
      // Create an alias for '@' to refer to the 'src' directory
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
     // Proxy requests to the Flask backend
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // Flask backend URL
        changeOrigin: true, // Change the origin of the request to the target URL
        rewrite: (path) => path.replace(/^\/api/, ''), 
      }
    }
  }
});

