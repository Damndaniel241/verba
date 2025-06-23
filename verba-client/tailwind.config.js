/** @type {import('tailwindcss').Config} */
export default {
    content: ["./index.html", "./src/**/*.{js,ts,vue}"],
    theme: {
      extend: {
        colors: {
          // accent: "#307f98",
          accent: "#0d49ce",
          fill: "#f7f7f7",
          fillHard: "#eaebee",
          softText: "#656b77",
          hardText: "#1b1d21",
          stroke: "#eaebee",
        },
        fontFamily:{
          sans: ['Inter', ...fontFamily.sans],
        },
      },
    },
    plugins: [],
  };