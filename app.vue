<template>
  <v-app>
    <v-app-bar color="primary" density="compact" title="Sit Down Please">
      <template #prepend>
        <v-app-bar-nav-icon @click="rail = !rail" />
      </template>

      <template #append>
        <v-btn icon="mdi-dots-vertical" />
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

const rail = ref(true);
</script>

<style>
html {
  overflow-y: auto;
}
</style>
