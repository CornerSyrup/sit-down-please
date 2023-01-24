<template>
  <sdp-time-card :room="1" membership="60475a5b" :temp="temp" :humid="humid" />
</template>

<script setup lang="ts">
import { ref } from "vue";

import SdpTimeCard from "../components/SdpTimeCard.vue";

const temp = ref(36);
const humid = ref(60);
</script>
