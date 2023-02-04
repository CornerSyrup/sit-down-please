import { onMounted, onBeforeUnmount, ref } from "vue";

export const useStatus = () => {
  const status = ref<{ seat: number; leave: number }>();

  const updateStatus = () =>
    fetch("http://localhost:5000/api")
      .then((res) => res.json())
      .then((data) => (status.value = data));

  onMounted(updateStatus);
  const interval = setInterval(updateStatus, 250);
  onBeforeUnmount(() => clearInterval(interval));

  return { status };
};
