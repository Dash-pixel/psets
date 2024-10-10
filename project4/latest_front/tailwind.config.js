/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/*.{js,jsx,ts,tsx}",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'active-blue': 'rgb(43,226,218)',
        'dark-bg': 'rgb(12,19,34)',
        'light-bg': 'rgb(17,28,48)',
        'light-txt': 'rgb(251,255,253)',
        'dark-txt': 'rgb(107,127,159)',
        'my-red': 'rgb(236,47,110)',
        'my-orange': 'rgb(252,146,120)',
        'my-blue': 'rgb(6,49,104)',
      },
      fontFamily: {
        'outfit': ['Outfit', 'sans-serif'], //
        'inter': ['Inter', 'sans-serif'], // SemiBold 600 for titles of posts?
        'poppins': ['Poppins', 'sans-serif'], 
        'raleway': ['Raleway', 'sans-serif'], // fancy Bold 700 Italic
      }
    },
  },
  plugins: [],
}

