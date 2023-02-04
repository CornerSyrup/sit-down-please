<template>
  <sdp-clock-card :temp="36" :humid="60" />
  <sdp-occupied-card :occupied="occupied" />
  <sdp-time-elapsed-card :since="status?.seat ?? Date.now()" />
</template>

<script setup lang="ts">
import SdpClockCard from "~~/components/SdpClockCard.vue";
import SdpOccupiedCard from "~~/components/SdpOccupiedCard.vue";
import SdpTimeElapsedCard from "~~/components/SdpTimeElapsedCard.vue";

import logo from "assets/logo.png";

const { status } = useStatus();

const occupied = computed(() =>
  !!status.value ? status.value.seat > status.value.leave : false
);

onMounted(() => {
  if (!!Notification && Notification.permission == "default") {
    Notification.requestPermission();
  }
});

watch(occupied, (nowOccupied) =>
  nowOccupied
    ? new Notification("Sit Down Please!", {
        body: "Focus on your work!",
        icon: logo,
      })
    : new Notification("Sit Down Please!", {
        body: `You has been focused for ${new Date(
          (Date.now() / 1000 - (status.value?.leave ?? Date.now() / 1000)) *
            1000
        ).toLocaleTimeString()}`,
        icon: logo,
      })
);
</script>
