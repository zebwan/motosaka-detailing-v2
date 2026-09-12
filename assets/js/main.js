/* ════════════════════════════════════════════════════════════════════════
   MOTOSAKA — behaviour layer. No dependencies.
   Smooth wheel · hero particles · scroll-scrubbed reveal · marquees ·
   panels · carousels · accordion · counters · menu
   ════════════════════════════════════════════════════════════════════════ */
(() => {
  'use strict';

  const RM = window.matchMedia('(prefers-reduced-motion: reduce)');
  const reduced = () => RM.matches;
  const isTouch = window.matchMedia('(hover: none)').matches;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ───────────────────────────────── smooth wheel (Lenis-style lerp 0.1) */
  const smooth = (() => {
    if (isTouch || reduced()) return null;           // native scroll on touch
    let target = window.scrollY, current = target, running = false, raf = 0;

    const limit = () => document.documentElement.scrollHeight - window.innerHeight;

    function tick() {
      current += (target - current) * 0.1;
      if (Math.abs(target - current) < 0.4) { current = target; running = false; }
      window.scrollTo(0, current);
      if (running) raf = requestAnimationFrame(tick); else raf = 0;
    }
    function start() { if (!running) { running = true; raf = requestAnimationFrame(tick); } }

    window.addEventListener('wheel', (e) => {
      if (e.ctrlKey) return;
      if (document.body.classList.contains('menu-open')) return;
      // let genuinely scrollable inner elements keep native behaviour
      for (let n = e.target; n && n !== document.body; n = n.parentElement) {
        const s = getComputedStyle(n);
        if (/(auto|scroll)/.test(s.overflowY) && n.scrollHeight > n.clientHeight + 2) return;
      }
      e.preventDefault();
      if (!running) current = window.scrollY;
      target = clamp(target + e.deltaY, 0, limit());
      start();
    }, { passive: false });

    // keep target in sync when scroll comes from elsewhere (keys, bar, anchors)
    window.addEventListener('scroll', () => { if (!running) target = current = window.scrollY; }, { passive: true });
    window.addEventListener('resize', () => { target = current = window.scrollY; });

    return {
      to(y) {
        target = clamp(y, 0, limit());
        if (!running) current = window.scrollY;
        start();
      }
    };
  })();

  /* ─────────────────────────────────────────────── anchors (offset by nav) */
  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (!id || id === '#') return;
      const t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      closeMenu();
      const y = t.getBoundingClientRect().top + window.scrollY - (id === '#top' ? 0 : 76);
      if (smooth && !reduced()) smooth.to(y);
      else window.scrollTo({ top: y, behavior: reduced() ? 'auto' : 'smooth' });
    });
  });

  /* ────────────────────────────────────────────────────────────── the menu */
  const menu = $('#menu'), burger = $('#burger');
  const head = $('#siteHead');

  function openMenu() {
    document.body.classList.add('menu-open');
    menu.hidden = false;
    requestAnimationFrame(() => menu.classList.add('is-open'));
    burger.setAttribute('aria-expanded', 'true');
    burger.setAttribute('aria-label', 'Close menu');
    head?.classList.add('is-over-menu');
    startClock();
  }
  function closeMenu() {
    if (!document.body.classList.contains('menu-open')) return;
    document.body.classList.remove('menu-open');
    menu.classList.remove('is-open');
    menu.hidden = true;
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', 'Open menu');
    head?.classList.remove('is-over-menu');
    stopClock();
  }
  burger.addEventListener('click', () =>
    document.body.classList.contains('menu-open') ? closeMenu() : openMenu());
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenu(); });

  /* Local clock in the menu. Uses the viewer's own IANA time zone, which the
     browser already knows — no permission prompt, no IP lookup, nothing leaves
     the page. Falls back to the studio's city if the zone is unusable. */
  const clock = $('.site-menu-clock');
  const place = $('.site-menu-place');
  let clockTimer = 0;
  let zone = clock?.dataset.tz || 'Asia/Kuala_Lumpur';

  (function resolveZone() {
    if (!place) return;
    let tz = '';
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch { /* keep fallback */ }
    // "Asia/Kuala_Lumpur" -> "Kuala Lumpur". Zones without a city part
    // (UTC, Etc/GMT+8, a bare offset) tell us nothing, so leave the studio name.
    const city = tz.includes('/') ? tz.split('/').pop().replace(/_/g, ' ') : '';
    if (!city || /^GMT|^UTC/i.test(city)) return;
    zone = tz;
    place.textContent = city;
  })();

  function tickClock() {
    if (!clock) return;
    try {
      clock.textContent = new Intl.DateTimeFormat('en-US', {
        timeZone: zone, hour: 'numeric', minute: '2-digit', hour12: true,
      }).format(new Date());
    } catch { clock.textContent = ''; }
  }
  function startClock() { tickClock(); clearInterval(clockTimer); clockTimer = setInterval(tickClock, 15000); }
  function stopClock() { clearInterval(clockTimer); clockTimer = 0; }

  /* ──────────────────────────────────────────────────────── back to top */
  const toTop = $('#toTop');
  toTop?.addEventListener('click', () => {
    if (smooth && !reduced()) smooth.to(0);
    else window.scrollTo({ top: 0, behavior: reduced() ? 'auto' : 'smooth' });
  });

  /* ─────────────────────────────────────────────────── hero entry + canvas */
  requestAnimationFrame(() => document.body.classList.add('hero-ready'));

  const cv = $('.hero-particles');
  if (cv && !reduced()) {
    const ctx = cv.getContext('2d', { alpha: true });
    let W = 0, H = 0, dots = [], dpr = 1, rafId = 0, alive = true;
    const pointer = { x: -1e4, y: -1e4 };

    function build() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      // fewer, cheaper particles on small screens
      const n = Math.round(clamp((W * H) / 9000, 40, W < 810 ? 80 : 190));
      dots = Array.from({ length: n }, () => {
        const big = Math.random() < 0.16;
        return {
          x: Math.random() * W, y: Math.random() * H,
          r: big ? 4 + Math.random() * 16 : 0.4 + Math.random() * 1.3,
          a: big ? 0.05 + Math.random() * 0.11 : 0.2 + Math.random() * 0.6,
          blur: big, vx: (Math.random() - 0.5) * 0.11, vy: -0.03 - Math.random() * 0.14,
          tw: Math.random() * Math.PI * 2, ts: 0.005 + Math.random() * 0.02,
        };
      });
    }

    function frame() {
      if (!alive) return;
      ctx.clearRect(0, 0, W, H);
      for (const d of dots) {
        d.x += d.vx; d.y += d.vy; d.tw += d.ts;
        if (d.y < -30) { d.y = H + 20; d.x = Math.random() * W; }
        if (d.x < -30) d.x = W + 20; else if (d.x > W + 30) d.x = -20;

        // gentle drift away from the cursor
        const dx = d.x - pointer.x, dy = d.y - pointer.y;
        const dist = Math.hypot(dx, dy);
        let px = d.x, py = d.y;
        if (dist < 170) { const f = (1 - dist / 170) * 22; px += (dx / dist) * f; py += (dy / dist) * f; }

        const a = d.a * (0.65 + 0.35 * Math.sin(d.tw));
        ctx.beginPath();
        if (d.blur) {
          const g = ctx.createRadialGradient(px, py, 0, px, py, d.r);
          g.addColorStop(0, `rgba(255,255,255,${a})`);
          g.addColorStop(1, 'rgba(255,255,255,0)');
          ctx.fillStyle = g;
        } else ctx.fillStyle = `rgba(255,255,255,${a})`;
        ctx.arc(px, py, d.r, 0, Math.PI * 2);
        ctx.fill();
      }
      rafId = requestAnimationFrame(frame);
    }

    build(); frame();
    addEventListener('resize', build);
    if (!isTouch) addEventListener('pointermove', (e) => {
      const r = cv.getBoundingClientRect();
      pointer.x = e.clientX - r.left; pointer.y = e.clientY - r.top;
    }, { passive: true });

    // stop burning frames once the hero is well out of view
    new IntersectionObserver(([en]) => {
      if (en.isIntersecting && !alive) { alive = true; frame(); }
      else if (!en.isIntersecting && alive) { alive = false; cancelAnimationFrame(rafId); }
    }, { rootMargin: '100px' }).observe(cv);
  }

  /* ───────────────────────────────── scroll-scrubbed per-character reveal */
  const scrub = $('.scrub');
  const scrubChars = scrub ? $$('.char', scrub) : [];

  /* ───────────────────────────────────────────────────── parallax orbs */
  const orbs = $$('.orb');

  /* ──────────────────────────────────────────────────── scroll progress */
  const progress = $('.scroll-progress i');

  const heroContent = $('.hero-content');
  const stacks = $$('[data-stack]').map((el) => ({
    el, cards: $$('.stack-card', el), team: el.dataset.stack === 'team',
  }));

  function onScroll() {
    const y = window.scrollY;

    /* header condenses once you leave the hero */
    if (head) head.classList.toggle('is-stuck', y > 40);
    if (toTop) toTop.classList.toggle('is-on', y > window.innerHeight * 1.2);

    /* sticky stacks — a card that is being overtaken shrinks and, on the team
       stack, slides away to the left. Driven off the NEXT card's position. */
    for (const st of stacks) {
      const { cards, team } = st;
      for (let i = 0; i < cards.length; i++) {
        const card = cards[i], next = cards[i + 1];
        if (!next) { card.style.transform = ''; card.style.opacity = ''; continue; }
        const cardTop = card.getBoundingClientRect().top;
        const nextTop = next.getBoundingClientRect().top;
        const travel = Math.max(next.offsetTop - card.offsetTop, 1);
        const p = clamp((cardTop - nextTop + travel) / travel, 0, 1);
        if (team) {
          card.style.transform =
            `translate3d(${-p * 34}%, ${-p * 26}px, 0) scale(${1 - p * 0.22})`;
          card.style.opacity = String(1 - p * 0.72);
        } else {
          card.style.transform = `translate3d(0, ${-p * 18}px, 0) scale(${1 - p * 0.08})`;
          card.style.opacity = String(1 - p * 0.35);
        }
      }
    }

    /* hero content dissolves as the intro rides over the pinned hero,
       the starfield stays behind it (as in the reference template) */
    if (heroContent) {
      const p = clamp(y / (window.innerHeight * 0.72), 0, 1);
      heroContent.style.opacity = String(1 - p);
      heroContent.style.transform = `translate3d(0,${-p * 70}px,0)`;
      heroContent.style.pointerEvents = p > 0.85 ? 'none' : '';
    }

    if (progress) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = `${max > 0 ? (y / max) * 100 : 0}%`;
    }

    if (scrubChars.length && scrub) {
      const r = scrub.getBoundingClientRect();
      // runs from "text enters the lower third" to "text sits above centre"
      const start = window.innerHeight * 0.86;
      const end = window.innerHeight * 0.18;
      const p = clamp((start - r.top) / (start - end), 0, 1);
      const lit = p * scrubChars.length;
      for (let i = 0; i < scrubChars.length; i++) {
        const o = clamp(lit - i, 0, 1);
        scrubChars[i].style.opacity = (0.1 + o * 0.9).toFixed(3);
      }
    }

    for (const o of orbs) {
      const sp = parseFloat(o.dataset.speed || '0');
      const r = o.parentElement.getBoundingClientRect();
      const p = (window.innerHeight - r.top) / (window.innerHeight + r.height);
      o.style.transform = `translate3d(0,${(p - 0.5) * sp * 320}px,0) rotate(${(p - 0.5) * sp * 90}deg)`;
    }
  }

  let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { onScroll(); ticking = false; });
  }, { passive: true });
  addEventListener('resize', onScroll);
  onScroll();

  /* ─────────────────────────────────────────────── reveal on scroll-in */
  const revealables = $$('.reveal');
  revealables.forEach((el, i) => {
    if (!el.style.getPropertyValue('--d')) {
      const sibs = [...(el.parentElement?.children || [])].filter((c) => c.classList.contains('reveal'));
      if (sibs.length > 1) el.style.setProperty('--d', `${sibs.indexOf(el) * 70}ms`);
    }
  });
  if (reduced()) revealables.forEach((el) => el.classList.add('in'));
  else {
    const io = new IntersectionObserver((ents) => {
      ents.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealables.forEach((el) => io.observe(el));
  }

  /* ──────────────────────────────────────────────────── count-up stats */
  $$('[data-count]').forEach((el) => {
    const raw = el.dataset.count;
    const m = raw.match(/^([^\d]*)([\d.]+)(.*)$/);
    if (!m || reduced()) return;
    const [, pre, numStr, post] = m;
    const target = parseFloat(numStr);
    const dec = (numStr.split('.')[1] || '').length;
    let done = false;
    new IntersectionObserver((ents, ob) => {
      if (!ents[0].isIntersecting || done) return;
      done = true; ob.disconnect();
      const t0 = performance.now(), dur = 1400;
      const run = (t) => {
        const p = clamp((t - t0) / dur, 0, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + (target * eased).toFixed(dec) + post;
        if (p < 1) requestAnimationFrame(run);
      };
      el.textContent = pre + (0).toFixed(dec) + post;
      requestAnimationFrame(run);
    }, { threshold: 0.5 }).observe(el);
  });

  /* ────────────────────────────────────────────────────────── marquees */
  $$('.mq-track').forEach((track) => {
    const speed = parseFloat(track.dataset.speed || '40');   // px per second
    if (reduced()) return;
    // duplicate until the strip is at least twice the viewport, for a seamless wrap
    const original = [...track.children];
    let guard = 0;
    while (track.scrollWidth < window.innerWidth * 2 && guard++ < 8) {
      original.forEach((c) => track.appendChild(c.cloneNode(true)));
    }
    const half = track.scrollWidth / 2;
    // a negative speed runs the row right-to-left instead; start it pre-shifted
    // so there is always content entering from the left edge
    let x = speed < 0 ? -half : 0;
    let last = performance.now(), running = true;

    const step = (now) => {
      if (!running) { last = now; requestAnimationFrame(step); return; }
      const dt = Math.min((now - last) / 1000, 0.05);
      last = now;
      x -= speed * dt;
      if (x <= -half) x += half;
      else if (x >= 0) x -= half;
      track.style.transform = `translate3d(${x}px,0,0)`;
      requestAnimationFrame(step);
    };
    requestAnimationFrame(step);

    // pause when off-screen (and on hover, for the reels)
    new IntersectionObserver(([en]) => { running = en.isIntersecting; },
      { rootMargin: '150px' }).observe(track);
    const wrap = track.parentElement;
    if (wrap && (wrap.classList.contains('reels-marquee') || wrap.classList.contains('rv-rail'))) {
      wrap.addEventListener('pointerenter', () => { running = false; });
      wrap.addEventListener('pointerleave', () => { running = true; });
    }
  });

  /* ───────────────────────────────────────────── process panels (002) */
  const panels = $$('.panel');
  panels.forEach((p) => {
    const head = $('.panel-head', p);
    const open = () => {
      if (p.classList.contains('is-open')) return;
      panels.forEach((o) => {
        o.classList.toggle('is-open', o === p);
        $('.panel-head', o)?.setAttribute('aria-expanded', String(o === p));
      });
    };
    head.addEventListener('click', open);
    if (!isTouch) p.addEventListener('pointerenter', open);
  });

  /* ─────────────────────────────────────────────────────── carousels */
  $$('[data-carousel]').forEach((wrap) => {   // (none left — stacks replaced them)
    const slides = $$('[data-slide]', wrap);
    const bars = $$('[data-bar]', wrap);
    if (!slides.length) return;
    let i = 0;

    function go(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
      bars.forEach((b, k) => b.classList.toggle('is-active', k === i));
      // only play the visible clips
      $$('video', wrap).forEach((v) => {
        const on = v.closest('[data-slide]')?.classList.contains('is-active');
        if (on) v.play?.().catch(() => {}); else v.pause?.();
      });
    }

    $$('[data-dir]', wrap).forEach((b) =>
      b.addEventListener('click', () => go(i + parseInt(b.dataset.dir, 10))));
    bars.forEach((b, k) => { if (b.tagName === 'BUTTON') b.addEventListener('click', () => go(k)); });

    // keyboard
    wrap.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') go(i + 1);
      if (e.key === 'ArrowLeft') go(i - 1);
    });

    // swipe
    let sx = 0, sy = 0, tracking = false;
    wrap.addEventListener('touchstart', (e) => {
      sx = e.touches[0].clientX; sy = e.touches[0].clientY; tracking = true;
    }, { passive: true });
    wrap.addEventListener('touchend', (e) => {
      if (!tracking) return;
      tracking = false;
      const dx = e.changedTouches[0].clientX - sx;
      const dy = e.changedTouches[0].clientY - sy;
      if (Math.abs(dx) > 46 && Math.abs(dx) > Math.abs(dy)) go(i + (dx < 0 ? 1 : -1));
    }, { passive: true });

    go(0);
  });

  /* ───────────────────────────────────────────────────── FAQ accordion */
  $$('[data-faq]').forEach((item) => {
    const q = $('.faq-q', item);
    q.addEventListener('click', () => {
      const open = item.classList.toggle('is-open');
      q.setAttribute('aria-expanded', String(open));
    });
  });

  /* ──────────────────────────────────────────────── forms → WhatsApp */
  const wa = (msg) =>
    `https://wa.me/60124058765?text=${encodeURIComponent(msg)}`;

  $('.ct-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const f = e.target;
    const get = (n) => (f.elements[n]?.value || '').trim();
    const name = get('name'), email = get('email');
    if (!name || !email) {
      (name ? f.elements.email : f.elements.name).focus();
      return;
    }
    const pkg = get('package');
    const msg = [
      "Hi Motosaka, I'd like to make an enquiry.",
      '',
      `Name: ${name}`,
      `Email: ${email}`,
      get('bike') && `Bike: ${get('bike')}`,
      `Treatment: ${pkg || 'Not sure yet — please advise'}`,
      get('message') && '',
      get('message') && `Details: ${get('message')}`,
    ].filter((l) => l !== false && l !== undefined).join('\n');
    window.open(wa(msg), '_blank', 'noopener');
  });

  $('.ft-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const v = (e.target.elements.email?.value || '').trim();
    if (!v) { e.target.elements.email.focus(); return; }
    window.open(wa(`Hi Motosaka, please add me to your updates list: ${v}`), '_blank', 'noopener');
    e.target.reset();
  });

  /* ────────────────────────── play videos in view, pause them when not.
     Autoplay attributes alone are unreliable, so drive playback directly. */
  const vids = $$('video');
  if (vids.length) {
    const inactive = (v) => {
      const slide = v.closest('[data-slide]');
      return slide && !slide.classList.contains('is-active');
    };
    const vio = new IntersectionObserver((ents) => {
      ents.forEach((en) => {
        const v = en.target;
        if (en.isIntersecting && !inactive(v)) {
          v.muted = true;                      // required for programmatic autoplay
          v.play?.().catch(() => {});
        } else {
          v.pause?.();
        }
      });
    }, { rootMargin: '260px' });
    vids.forEach((v) => vio.observe(v));
  }
})();
