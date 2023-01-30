import { defineNuxtConfig } from "nuxt/config";

import messages from "./assets/locales";

export default defineNuxtConfig({
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://cdn.jsdelivr.net/npm/@mdi/font@5.x/css/materialdesignicons.min.css",
        },
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp",
        },
        { href: "manifest.webmanifest", rel: "manifest" },
      ],
      script: [{ src: "index.js" }],
    },
  },
  build: {
    transpile: ["vuetify"],
  },
  modules: ["@nuxtjs/i18n"],
  i18n: {
    vueI18n: {
      legacy: false,
      locale: "ja",
      fallbackLocale: "en",
      messages,
    },
  },
});
