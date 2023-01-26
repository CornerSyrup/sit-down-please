<template>
  <sdp-clock-card :temp="temp" :humid="humid" />
  <sdp-occupied-card :occupied="occupied" />
  <sdp-time-elapsed-card :since="since" />
</template>

<script setup lang="ts">
import { ref } from "vue";

import SdpClockCard from "~~/components/SdpClockCard.vue";
import SdpOccupiedCard from "~~/components/SdpOccupiedCard.vue";
import SdpTimeElapsedCard from "~~/components/SdpTimeElapsedCard.vue";

const temp = ref(36);
const humid = ref(60);

const occupied = ref(true);

const since = ref(new Date("2023/01/26 07:00").getTime() / 1000);
</script>
