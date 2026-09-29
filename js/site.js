/* Interim site behaviour: mobile menu, mobile dropdowns, reveal-on-scroll, footer year */
(function () {
  var body = document.body;
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
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
  var y = document.querySelectorAll('[data-year]');
  y.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

/* Home hero slider: auto-advances when each tab's progress bar finishes; pauses on hover/focus. */
(function () {
  document.querySelectorAll('[data-slider]').forEach(function (root) {
    var copies = root.querySelectorAll('.slide-copy');
    var media = root.querySelectorAll('.slide-media');
    var tabs = root.querySelectorAll('.slider-tab');
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var cur = 0;
    if (reduce) root.classList.add('static');
    function go(n) {
      cur = (n + tabs.length) % tabs.length;
      [copies, media, tabs].forEach(function (list) {
        list.forEach(function (el, i) { el.classList.toggle('is-active', i === cur); });
      });
      copies.forEach(function (el, i) {
        var on = i === cur;
        if (on) el.removeAttribute('aria-hidden'); else el.setAttribute('aria-hidden', 'true');
        el.querySelectorAll('a').forEach(function (a) { if (on) a.removeAttribute('tabindex'); else a.setAttribute('tabindex', '-1'); });
      });
      tabs.forEach(function (t, i) {
        t.setAttribute('aria-selected', i === cur ? 'true' : 'false');
        var bar = t.querySelector('.t-bar i');
        bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = '';
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { go(i); });
      t.querySelector('.t-bar i').addEventListener('animationend', function () { if (i === cur) go(cur + 1); });
    });
    root.addEventListener('mouseenter', function () { root.classList.add('paused'); });
    root.addEventListener('mouseleave', function () { root.classList.remove('paused'); });
    root.addEventListener('focusin', function (e) {
      var kb = true; try { kb = e.target.matches(':focus-visible'); } catch (err) {}
      if (kb) root.classList.add('paused');
    });
    root.addEventListener('focusout', function () { root.classList.remove('paused'); });
    var sx = null, sy = null;
    root.addEventListener('touchstart', function (e) { var t = e.touches[0]; sx = t.clientX; sy = t.clientY; }, { passive: true });
    root.addEventListener('touchend', function (e) {
      if (sx === null) return;
      var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) go(cur + (dx < 0 ? 1 : -1));
      sx = sy = null;
    }, { passive: true });
    root.addEventListener('keydown', function (e) {
      if (e.target.classList.contains('slider-tab')) {
        if (e.key === 'ArrowRight') { go(cur + 1); tabs[cur].focus(); }
        if (e.key === 'ArrowLeft') { go(cur - 1); tabs[cur].focus(); }
      }
    });
  });
})();

/* Insights filters */
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
        var ok = f === '*' ||
          (f.indexOf('type:') === 0 && card.getAttribute('data-type') === f.slice(5)) ||
          (f.indexOf('tag:') === 0 && (card.getAttribute('data-tags') || '').indexOf('|' + f.slice(4) + '|') > -1);
        card.hidden = !ok; if (ok) { shown++; card.classList.add('in'); }
      });
      if (empty) empty.hidden = shown > 0;
    });
  });
})();
