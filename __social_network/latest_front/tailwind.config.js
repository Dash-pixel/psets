/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/*.{js,jsx,ts,tsx}",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        colors: {
          'light-gray': '#BDBDBD',
          'dark-gray': '#333',
          'medium-gray': '#ACACAC',
          'black': '#000',
          'off-white': '#ECE1D9',
          'brown': '#423838',
          'dark-red': '#581622',
          'white': '#fff',
          'deep-red': '#7A002B',
          'deep-burgundy': '#491E1E',
          'rose-red': '#B73947',
          'charcoal': '#363940',
          'light-black': '#666',
          'medium-black': '#555',
          'light-rose': '#ad003d',
          'red-contrast': '#9F1C36',
          'gray': '#999'
        }
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

