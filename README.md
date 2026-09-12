# Motosaka Detailing — site revamp

A rebuild of the Motosaka Detailing landing page on the structure and motion system of the
Framer template **"Platform® — Modular Landing Page"** (`plat-form.framer.ai`), re-skinned to a
strictly **black → white** palette and filled with Motosaka's real content.

Plain static HTML/CSS/JS. No build step required to *serve* it — `index.html` is the deliverable.

---

## Run it

Just open `index.html`, or serve the folder:

```bash
python3 -m http.server 9701 --directory "$HOME/Desktop/Motosaka Revamp"
```

## Edit the content

All copy, prices, images and links live in **`content.py`**. Change a value there, then:

```bash
python3 build.py
```

That regenerates `index.html`. Nothing else needs touching for a copy or price change.

---

## Structure

Numbered sections follow the template's editorial rail (label · index · headline · body).

| # | Section | Source of content |
|---|---|---|
| — | Hero (sticky, particle canvas) | "Refined care for bikes of distinction" |
| — | Intro (per-character scroll reveal) | "Quiet precision, considered care…" |
| 001 | Our Work — bento gallery | gallery photos from the current site |
| 002 | Our Process — 4 expanding panels | Assessment / Cleanse / Refine / Protect |
| 003 | Exhaust Revival — scroll-stacking cards | the three exhaust video sets |
| 004 | Behind The Work — reel marquee | reel videos |
| 005 | Packages — 6 cards | real prices RM50 → RM1200 |
| 006 | Questions & Answers — accordion | the 8 existing FAQs |
| 007 | Meet the Team — stacking cards | **placeholder** (see below) |
| 008 | Google Reviews — two opposed rails | the 9 real reviews, verbatim |
| 009 | Aftercare & Loyalty | care kit + loyalty card |
| — | Let's talk (pinned) + footer | real phone, email, address |

### What changed from the template

**Repurposed** rather than dropped, because Motosaka had real content for the slot:
- The template's *Analytics dashboard* (charts, uptime %, API metrics) → **Exhaust Revival** before/after.
- The template's *Blog teaser* → **Aftercare & Loyalty**.

**Removed** — nothing in the business maps to them:
- The monthly/yearly pricing toggle (Motosaka prices are per session, not subscriptions).
- The "integration partners" / AI-model widgets.
- The Framer template promo chrome ("New Template!" / "Buy Template").
- The white wordmark ticker band, dropped on request.

---

## Colour

Strictly black → white, per brief. The template's orange accent became **pure white** — white slabs
with near-black text, which is what carries the "accent" role now (menu, open process panel,
primary buttons, prices).

```
--bg        #0B0B0B      --accent     #FFFFFF   (was #FA6E43)
--surface   #141414      --on-accent  #0B0B0B
--surface-2 #1C1C1C      --text       #F1F1F1
--surface-3 #242424      --text-2     #B9B9B9
--line      rgba(255,255,255,.08)     --text-3  #8A8A8A
--line-2    rgba(255,255,255,.16)     --text-4  #5E5E5E
```

**Photography is in full colour.** Only the interface is monochrome — the bikes, the metalwork
and the product shots all keep their own colour.

Type is **Inter** at the template's exact scale and tracking (-0.05em on display sizes).

---

## Motion

Ported from the template, measured off the original rather than guessed:

- **Entry choreography** — staggered appear timeline: background fades `0.001 → 1` over 2000ms;
  slogan lines slide in from `x −230px` at 300/400ms; headline rises from `y 60px` at 500ms;
  CTA lockup from `x −260px` at 700/900ms; stats at 1000/1100ms. Easings
  `cubic-bezier(0,1.03,.56,1)` and `(.6,0,.38,1.01)` are the template's own values.
- **Smooth wheel** — lerp 0.1, matching the template's Lenis config. Desktop only; touch keeps
  native momentum scrolling.
- **Per-character scroll reveal** — the intro paragraph is split into `.word > .char` and each
  character scrubs `opacity 0.1 → 1` against scroll position. This is exactly how the original does it.
- **Hero particles** — canvas starfield with soft bokeh, drifts away from the cursor, particle
  count scales down on small screens, and the loop stops when the hero leaves the viewport.
- **Sticky stacking cards** — Exhaust Revival and the team both stack on scroll instead of using
  prev/next buttons. On the team stack each card, as it is overtaken, scales down and slides out to
  the left; the exhaust cards simply settle back. No tapping required.
- **Process panels expand, they do not fade** — the open panel animates its width from ~130px to
  ~960px over 820ms, the body is revealed by an unrolling clip-path and the copy slides in behind it.
  On mobile the same panel unfolds by height (`0fr → 1fr`), so it still reads as opening.
- **Two review rails** running in opposite directions (−26 and +22 px/sec), pausing on hover.
  Cards are 274×230 with the quote clamped to seven lines, so both rows sit on screen at once.
- Scroll-into-view reveals with per-sibling stagger, count-up stats, parallax orbs.

### On mobile and tablet

Everything above stays on, as asked. Verified running at 390px and 1024px:
per-character scrub, hero particles, the reels marquee, both review rails, the sticky stacks,
reveals, count-ups, and autoplaying video. The only deliberate differences:

- Smooth-wheel is off on touch (native momentum feels better and avoids scroll-jacking).
- Particle count is capped lower on small screens.
- The process panels become a vertical accordion that unfolds by height instead of width.
- Hover-only affordances (the square arrow buttons) are always visible.
- `prefers-reduced-motion` disables the lot and shows everything in its final state.

---

## Images

All images are **WebP**, resized for web (39 files, ~2.4 MB total). Videos are H.264 MP4,
720px wide, muted (12 files, ~7.9 MB). Source material came from the current site's `img/`
folder; the larger media zip was mostly `.mov` and Instagram screenshots and wasn't needed.

The MOTOSAKA wordmark and the three illustrated badges were recoloured to white with their
transparency preserved.

---

### Navigation

Desktop (≥1200px) shows the logo, the nav links and a Book Appointment button — no menu button,
since the links are already there.

Below 1200px they give way to a **motorcycle icon** instead of a hamburger: a hand-drawn inline SVG
with an engine block, tank and exhaust, sitting bare in the bar with no button chrome around it. Its wheels roll on hover, and when the menu is open the bike
leans forward and puffs **smoke out of the exhaust** on a loop. The header sits above the open menu
so the icon stays visible as the toggle — there is no separate close button. The menu itself floods
open on a clip-path circle grown from the icon, with the links staggering in behind it.

A back-to-top button appears bottom-right once you are past the first screen.

## Needs client input

1. **The team section is placeholder.** Six members with lorem ipsum text and blank grey profile
   avatars (`assets/img/team1–6.webp`), as requested. Swap the names, roles, bios and photos in
   `content.py → TEAM` when the real details arrive.
2. **Stats in the hero** — "5.0 Google rating" and "RM50 starting price" are taken from the
   existing site. Confirm the review count you want shown, if any.
3. **Every enquiry goes to WhatsApp on +60 12-405 8765.** The contact form carries the name, email,
   bike and the treatment chosen from its dropdown; each package's own "Reserve" button opens
   WhatsApp already naming that package with its listed price and duration. The newsletter field
   does the same. If you want real form submissions instead, they need a backend or a form service.
4. **Instagram handle** is assumed to be `instagram.com/motosakadetailing` — confirm.
5. The gallery "19 / 19" counter reflects the 19 photos carried over.

---

## Reference

`_reference/` (kept locally, not in this repo) holds the teardown of the source template — the extracted entry-animation config
(`appear-animations.json`), its full CSS, per-section DOM dumps with computed styles, and
screenshot sheets of both the original and this build. Not needed to run the site; keep it if you
want to check a detail against the original.
