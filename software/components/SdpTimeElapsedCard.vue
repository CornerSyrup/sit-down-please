<template>
  <v-card class="mx-auto" min-width="350" min-height="200">
    <v-card-item :title="t('component.time-elapsed.title')" />
    <v-card-text class="py-0">
      <v-row align="center" justify="center" no-gutters>
        <v-col class="text-h3 text-secondary" cols="8">
          {{ elapse.getHours().toString().padStart(2, "0") }} :
          {{ elapse.getMinutes().toString().padStart(2, "0") }}
        </v-col>

        <v-col class="text-center" cols="4">
          <v-icon color="secondary" icon="mdi:mdi-timer-sand" size="88" />
        </v-col>
      </v-row>
    </v-card-text>

    <div class="d-flex py-3 justify-space-around">
      <v-list-item density="compact" prepend-icon="mdi:mdi-clock-start">
        {{ new Date(since * 1000).toLocaleTimeString() }}
      </v-list-item>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { useI18n } from "#imports";

import { MessageSchema } from "assets/locales";
import { useCurrentTime } from "~~/composition";

const props = defineProps<{
  since: number;
}>();

const { t } = useI18n<{ message: MessageSchema }>();

const { currentTime } = useCurrentTime();
const elapse = computed(
  () => new Date(currentTime.value.getTime() - props.since * 1000)
);
</script>
