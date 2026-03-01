self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('xcare-v1').then((cache) => cache.addAll(['/', '/manifest.json', '/logo.png'])));
});

self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request)));
});
