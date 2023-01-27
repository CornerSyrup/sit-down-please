<template>
  <sdp-clock-card :temp="36" :humid="60" />
  <sdp-occupied-card :occupied="occupied" />
  <sdp-time-elapsed-card :since="status?.seat ?? 0" />
</template>

<script lang="ts">
const workIcon = "https://cdn-icons-png.flaticon.com/512/9390/9390783.png";
</script>

<script setup lang="ts">
import SdpClockCard from "~~/components/SdpClockCard.vue";
import SdpOccupiedCard from "~~/components/SdpOccupiedCard.vue";
import SdpTimeElapsedCard from "~~/components/SdpTimeElapsedCard.vue";
import { useStatus } from "../composition";

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
        body: "死ぬ気で働け！",
        icon: workIcon,
      })
    : new Notification("Sit Down Please!", {
        body: "座って働け！",
        icon: workIcon,
      })
);
</script>
