import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  typescript: {
    strict: true,
    tsConfig: {
      compilerOptions: {
        types: ["vuetify"],
      },
    },
  },
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://cdn.jsdelivr.net/npm/@mdi/font@5.x/css/materialdesignicons.min.css",
        },
      ],
    },
  },
  build: {
    transpile: ["vuetify"],
  },
});
