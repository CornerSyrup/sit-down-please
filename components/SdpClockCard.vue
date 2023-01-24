<template>
  <v-card class="mx-auto" min-width="350">
    <v-card-item title="Current Time" />
    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col class="text-h2 text-secondary" cols="8">
          {{ now.getHours().toString().padStart(2, "0") }} :
          {{ now.getMinutes().toString().padStart(2, "0") }}
        </v-col>

        <v-col class="text-center" cols="4">
          <v-icon
            color="secondary"
            icon="mdi-clock-time-four-outline"
            size="88"
          />
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
  </v-card>
</template>

<script setup lang="ts">
import { useCurrentTime } from "../composition";

defineProps<{
  temp: number;
  humid: number;
}>();

const { currentTime: now } = useCurrentTime();
</script>
