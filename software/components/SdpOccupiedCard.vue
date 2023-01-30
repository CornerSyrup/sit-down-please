<template>
  <v-card class="mx-auto" min-width="350" min-height="200">
    <v-card-item :title="t('component.status.title')" />
    <v-card-text class="py-0">
      <v-row align="center" justify="center" no-gutters>
        <v-col class="text-h3 text-secondary" cols="8">
          {{
            t(
              occupied
                ? "component.status.status.occupied"
                : "component.status.status.available"
            )
          }}
        </v-col>

        <v-col class="text-center" cols="4">
          <v-icon
            :color="occupied ? 'error' : 'success'"
            :icon="icon"
            size="88"
          />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { useI18n } from "#imports";

import { MessageSchema } from "assets/locales";

const props = defineProps<{
  occupied: boolean;
}>();

const { t } = useI18n<{ message: MessageSchema }>();

const icon = computed(() =>
  props.occupied ? "mdi:mdi-sofa-single" : "mdi:mdi-sofa-single-outline"
);
</script>
