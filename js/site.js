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

/* Interim site behaviour: mobile menu, mobile dropdowns, reveal-on-scroll, footer year */
(function () {
  var body = document.body;
  var toggle = document.querySelector('.menu-toggle');
  var check = document.getElementById('nav-toggle');
  function setOpen(open) {
    body.classList.toggle('nav-open', !!open);
    if (check) check.checked = !!open;
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (check) {
    check.addEventListener('change', function () { setOpen(check.checked); });
  } else if (toggle) {
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      setOpen(!body.classList.contains('nav-open'));
    });
  }
  document.querySelectorAll('.nav a').forEach(function (a) {
    a.addEventListener('click', function () { setOpen(false); });
  });
  document.querySelectorAll('.nav .has-dd > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (window.innerWidth > 960) return;
      var li = btn.parentElement;
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }
  setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 600);
  var y = document.querySelectorAll('[data-year]');
  y.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

/* Site-wide name: Government Relations */
(function () {
  document.querySelectorAll('a[href="government-affairs.html"], a[href="./government-affairs.html"]').forEach(function (a) {
    a.setAttribute('href', 'government-relations.html');
  });
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  var node;
  while ((node = walker.nextNode())) {
    if (!node.nodeValue || node.nodeValue.indexOf('Government Affairs') === -1 && node.nodeValue.indexOf('government affairs') === -1) continue;
    var parent = node.parentElement;
    if (parent && parent.closest && parent.closest('option, select, script, textarea')) continue;
    node.nodeValue = node.nodeValue.replace(/Government Affairs/g, 'Government Relations').replace(/government affairs/g, 'government relations');
  }
})();
