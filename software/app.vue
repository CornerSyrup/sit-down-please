<template>
  <v-app :theme="theme ? 'light' : 'dark'">
    <v-app-bar color="primary" density="compact" title="Sit Down Please">
      <template #prepend>
        <v-app-bar-nav-icon @click="rail = !rail" />
      </template>

      <template #append>
        <v-menu open-on-hover>
          <template v-slot:activator="{ props }">
            <v-btn icon="mdi:mdi-dots-vertical" v-bind="props" />
          </template>

          <v-list>
            <v-list-item
              :prepend-icon="`mdi:mdi-weather-${theme ? 'night' : 'sunny'}`"
              @click="theme = !theme"
            >
              Theme
            </v-list-item>
            <v-list-item
              prepend-icon="mdi:mdi-translate"
              @click="setLocale(locale == 'en' ? 'ja' : 'en')"
            >
              Language
            </v-list-item>
          </v-list>
        </v-menu>
      </template>
    </v-app-bar>

    <v-main>
      <v-container fluid class="fill-height">
        <nuxt-page />
      </v-container>
    </v-main>

    <v-footer :app="true">
      <span class="text-caption text-center w-100">
        &copy; 2023 Klein Chiu
      </span>
    </v-footer>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from "vue";

import { useI18n } from "#imports";

const { locale, setLocale } = useI18n();

const rail = ref(true);

const theme = ref(true);
</script>

<style>
html {
  overflow-y: auto;
}
</style>
