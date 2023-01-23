import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import { createVuetify } from "vuetify/lib/framework.mjs";

import "vuetify/styles";

// Container colors are not used, but still keep for future.
// Color palettes are calculated with MD3 Theme builder.
// https://m3.material.io/theme-builder#/custom
// Primary: 5C7A89
// Secondary: 7f949f
// Tertiary: 87CEEB
// Neutral: 8f9193

const light = {
  dark: false,
  colors: {
    primary: "#006684",
    "on-primary": "#ffffff",
    "primary-container": "#bee9ff",
    "on-primary-container": "#001f2a",
    secondary: "#4d616c",
    "on-secondary": "#ffffff",
    "secondary-container": "#d0e6f2",
    "on-secondary-container": "#081e27",
    tertiary: "#006781",
    "on-tertiary": "#ffffff",
    "tertiary-container": "#baeaff",
    "on-tertiary-container": "#001f29",
    // "info": "#2196F3",
    // "success": "#4CAF50",
    // "warning": "#FB8C00",
    error: "#ba1a1a",
    "on-error": "#ffffff",
    "error-container": "#ffdad6",
    "on-error-container": "#410002",
    background: "#fbfcfe",
    "on-background": "#191c1e",
    surface: "#fbfcfe",
    "on-surface": "#191c1e",
    "surface-variant": "#dce4e9",
    "on-surface-variant": "#40484c",
  },
  variables: {
    "border-color": "#70787d",
    // "theme-kbd": "#212529",
    // "theme-on-kbd": "#FFFFFF",
    // "theme-code": "#F5F5F5",
    // "theme-on-code": "#000000"
  },
};

const dark = {
  dark: true,
  colors: {
    primary: "#69d3ff",
    "on-primary": "#003546",
    "primary-container": "#004d64",
    "on-primary-container": "#bee9ff",
    secondary: "#b4cad6",
    "on-secondary": "#1f333d",
    "secondary-container": "#354a54",
    "on-secondary-container": "#d0e6f2",
    tertiary: "#5fd4fe",
    "on-tertiary": "#003544",
    "tertiary-container": "#004d62",
    "on-tertiary-container": "#baeaff",
    // "info": "#2196F3",
    // "success": "#4CAF50",
    // "warning": "#FB8C00",
    error: "#ffb4ab",
    "on-error": "#690005",
    "error-container": "#93000a",
    "on-error-container": "#ffdad6",
    background: "#191c1e",
    "on-background": "#e1e2e5",
    surface: "#191c1e",
    "on-surface": "#e1e2e5",
    "surface-variant": "#40484c",
    "on-surface-variant": "#c0c8cd",
  },
  variables: {
    "border-color": "#8a9297",
    // "theme-kbd": "#212529",
    // "theme-on-kbd": "#FFFFFF",
    // "theme-code": "#F5F5F5",
    // "theme-on-code": "#000000"
  },
};

const vuetify = createVuetify({
  components,
  directives,
  theme: { themes: { light, dark } },
  icons: { defaultSet: "mdi", aliases, sets: { mdi } },
});

export default defineNuxtPlugin((nuxtApp) => nuxtApp.vueApp.use(vuetify));
