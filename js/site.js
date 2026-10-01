/* Shared type and header scale — same on every page */
(function () {
  var head = document.head;
  if (!document.querySelector('link[href*="Figtree"]')) {
    var font = document.createElement('link');
    font.rel = 'stylesheet';
    font.href = 'https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;600&display=swap';
    head.appendChild(font);
  }
  ['css/mobile-nav.css', 'css/consistent.css'].forEach(function (href) {
    if (document.querySelector('link[href="' + href + '"]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    head.appendChild(link);
  });
})();

/* Interim site behaviour */
(function () {
  var body = document.body;
  var toggle = document.querySelector('.menu-toggle');
  var check = document.getElementById('nav-toggle');
  function setOpen(open) {
    body.classList.toggle('nav-open', !!open);
    if (check) check.checked = !!open;
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (check) check.addEventListener('change', function () { setOpen(check.checked); });
  else if (toggle) toggle.addEventListener('click', function (e) { e.preventDefault(); setOpen(!body.classList.contains('nav-open')); });
  document.querySelectorAll('.nav a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
  document.querySelectorAll('.nav .has-dd > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (window.innerWidth > 960) return;
      var open = btn.parentElement.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
  setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 600);
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

(function () {
  document.querySelectorAll('a[href="government-affairs.html"], a[href="./government-affairs.html"]').forEach(function (a) {
    a.setAttribute('href', 'government-relations.html');
  });
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT), node;
  while ((node = walker.nextNode())) {
    if (!node.nodeValue || (node.nodeValue.indexOf('Government Affairs') === -1 && node.nodeValue.indexOf('government affairs') === -1)) continue;
    var parent = node.parentElement;
    if (parent && parent.closest && parent.closest('option, select, script, textarea')) continue;
    node.nodeValue = node.nodeValue.replace(/Government Affairs/g, 'Government Relations').replace(/government affairs/g, 'government relations');
  }
})();

(function () {
  document.querySelectorAll('[data-slider]').forEach(function (root) {
    var copies = root.querySelectorAll('.slide-copy');
    var media = root.querySelectorAll('.slide-media');
    var tabs = root.querySelectorAll('.slider-tab');
    var cur = 0;
    function go(n) {
      cur = (n + tabs.length) % tabs.length;
      [copies, media, tabs].forEach(function (list) {
        list.forEach(function (el, i) { el.classList.toggle('is-active', i === cur); });
      });
    }
    tabs.forEach(function (t, i) { t.addEventListener('click', function () { go(i); }); });
  });
})();

(function () {
  var grid = document.querySelector('[data-insights]');
  if (!grid) return;
  var chips = document.querySelectorAll('.chip[data-filter]');
  var empty = document.querySelector('[data-empty]');
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.toggle('is-on', x === c); });
      var f = c.getAttribute('data-filter'), shown = 0;
      grid.querySelectorAll('.ins-card').forEach(function (card) {
        var ok = f === '*' || (f.indexOf('type:') === 0 && card.getAttribute('data-type') === f.slice(5)) || (f.indexOf('tag:') === 0 && (card.getAttribute('data-tags') || '').indexOf('|' + f.slice(4) + '|') > -1);
        card.hidden = !ok; if (ok) shown++;
      });
      if (empty) empty.hidden = shown > 0;
    });
  });
})();

(function () {
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.video-poster');
    if (!btn) return;
    var frame = btn.closest('.video-frame');
    if (!frame) return;
    var id = frame.getAttribute('data-yt');
    if (!id) return;
    e.preventDefault();
    frame.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1&playsinline=1" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>';
  }, true);
})();
