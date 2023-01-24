<template>
  <sdp-clock-card :temp="temp" :humid="humid" />
</template>

<script setup lang="ts">
import { ref } from "vue";

import SdpClockCard from "../components/SdpClockCard.vue";

const temp = ref(36);
const humid = ref(60);
</script>
