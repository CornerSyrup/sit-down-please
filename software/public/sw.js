/// <reference lib="WebWorker"  />

if (!(self instanceof ServiceWorkerGlobalScope)) {
    throw
}

self.addEventListener("fetch", () => {});
