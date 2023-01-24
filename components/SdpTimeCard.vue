<template>
  <v-card class="mx-auto" min-width="350">
    <v-card-item :title="`Room ${room}`">
      <template #subtitle> Membership: {{ membership }} </template>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col class="text-h2" cols="7">
          {{ now.getHours() }} :
          {{ now.getMinutes().toString().padStart(2, "0") }}
        </v-col>

        <v-col class="text-center" cols="5">
          <v-icon color="error" icon="mdi-clock-time-four-outline" size="88" />
        </v-col>
      </v-row>
    </v-card-text>

    <div class="d-flex py-3 justify-space-around">
      <v-list-item density="compact" prepend-icon="mdi-thermometer">
        {{ temp }}&deg;C
      </v-list-item>

      <v-list-item density="compact" prepend-icon="mdi-water-percent">
        {{ humid }}&percnt;
      </v-list-item>
    </div>

    <v-card-actions>
      <v-btn disabled> ASK FOR HELP </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup lang="ts">
import { VCard, VBtn } from "vuetify/components";

import { useCurrentTime } from "../composition";

defineProps<{
  room: number;
  membership: string;
  temp: number;
  humid: number;
}>();

const { currentTime: now } = useCurrentTime();
</script>
