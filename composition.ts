import { onMounted, onBeforeUnmount, ref } from "vue";

export const useCurrentTime = () => {
  const currentTime = ref(new Date());
  let timer;
  onMounted(
    () => (timer = setInterval(() => (currentTime.value = new Date()), 1000))
  );
  onBeforeUnmount(() => clearInterval(timer));

  return { currentTime };
};
