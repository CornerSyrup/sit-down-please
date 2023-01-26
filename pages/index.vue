<template>
  <sdp-clock-card :temp="temp" :humid="humid" />
  <sdp-occupied-card :occupied="occupied" />
</template>

<script setup lang="ts">
import { ref } from "vue";

import SdpClockCard from "~~/components/SdpClockCard.vue";
import SdpOccupiedCard from "~~/components/SdpOccupiedCard.vue";

const temp = ref(36);
const humid = ref(60);

const occupied = ref(true);
</script>
