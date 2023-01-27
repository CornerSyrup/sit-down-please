<template>
  <sdp-clock-card :temp="36" :humid="60" />
  <sdp-occupied-card :occupied="occupied" />
  <sdp-time-elapsed-card :since="status?.seat ?? Date.now()" />
</template>

<script lang="ts">
const workIcon =
  "https://cdn-icons-png.flaticon.com/512/1256/1256723.png?w=740&t=st=1674800504~exp=1674801104~hmac=7c27f722d29c5ad6ad6e8d7bc5dc605b97657f3615af6009b572bcbcdd5685b7";
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
