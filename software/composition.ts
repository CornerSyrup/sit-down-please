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

export const useStatus = () => {
  const status = ref<{ seat: number; leave: number }>();

  const updateStatus = () =>
    fetch("localhost:3000/api")
      .then((res) => res.json())
      .then((data) => (status.value = data));

  onMounted(updateStatus);
  const interval = setInterval(updateStatus, 250);
  onBeforeUnmount(() => clearInterval(interval));

  return { status };
};
