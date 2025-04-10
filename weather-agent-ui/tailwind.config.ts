import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",       // app router
    "./pages/**/*.{js,ts,jsx,tsx}",     // optional, if using pages
    "./components/**/*.{js,ts,jsx,tsx}" // optional, reusable components
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

export default config;
