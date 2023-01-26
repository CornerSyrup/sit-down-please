<template>
  <v-card class="mx-auto" min-width="350" min-height="200">
    <v-card-item title="Status" />
    <v-card-text class="py-0">
      <v-row align="center" justify="center" no-gutters>
        <v-col class="text-h3 text-secondary" cols="8">
          {{ occupied ? "Occupied" : "Available" }}
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
const props = defineProps<{
  occupied: boolean;
}>();

const icon = computed(() =>
  props.occupied ? "mdi:mdi-sofa-single" : "mdi:mdi-sofa-single-outline"
);
</script>
