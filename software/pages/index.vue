<template>
  <sdp-clock-card :temp="36" :humid="60" />
  <sdp-occupied-card
    :occupied="!!status ? status.seat > status.leave : false"
  />
  <sdp-time-elapsed-card :since="status?.seat ?? Date.now()" />
</template>

<script setup lang="ts">
import SdpClockCard from "~~/components/SdpClockCard.vue";
import SdpOccupiedCard from "~~/components/SdpOccupiedCard.vue";
import SdpTimeElapsedCard from "~~/components/SdpTimeElapsedCard.vue";
import { useStatus } from "../composition";

const { status } = useStatus();
</script>
