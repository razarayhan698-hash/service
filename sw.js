const CACHE_NAME = 'xcare-v2'; // ভার্সন পরিবর্তন করা হয়েছে যাতে ক্যাশ ক্লিয়ার হয়
const urlsToCache = [
  '/',
  '/manifest.json',
  '/logo.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
      .then(() => self.skipWaiting()) // নতুন ভার্সন সাথে সাথে একটিভ হবে
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name)) // পুরনো ক্যাশ ডিলিট করবে
      );
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
