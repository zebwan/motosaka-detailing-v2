# -*- coding: utf-8 -*-
"""Generates index.html from content.py.  Run:  python3 build.py"""
import html, re
from content import (BRAND, NAV, HERO, INTRO, WORK, PROCESS, EXHAUST, REELS,
                     PACKAGES, FAQ, TEAM, REVIEWS, AFTERCARE, CONTACT, FOOTER)

e = lambda s: html.escape(str(s), quote=True)
from urllib.parse import quote

WA_BASE = f"https://wa.me/{BRAND['phone_raw']}?text="
WA = WA_BASE + quote(BRAND['wa_text'])


def WA_PKG(name, price, duration):
    """Booking link that tells the studio exactly which treatment was tapped."""
    msg = (f"Hi Motosaka, I'd like to book the {name} package.\n"
           f"Listed price: {price}\n"
           f"Listed duration: {duration}\n"
           f"My bike: ")
    return e(WA_BASE + quote(msg))


def chars(text):
    """Split into .word > .char spans for the scroll-scrubbed opacity reveal."""
    out = []
    for w in text.split(' '):
        cs = ''.join(f'<span class="char">{e(c)}</span>' for c in w)
        out.append(f'<span class="word">{cs}</span>')
    return ' '.join(out)


def accent(text):
    """*word* -> accent span."""
    return re.sub(r'\*(.+?)\*', lambda m: f'<em>{e(m.group(1))}</em>', e(text)).replace('*', '')


def head_rail(label, index, headline, body, note=None, counter=None, anchor=None):
    aid = f' id="{anchor}"' if anchor else ''
    return f'''
  <div class="rail reveal"{aid}>
    <div class="rail-l"><span class="rail-label">{e(label)}</span><span class="rail-index">{e(index)}</span></div>
    <div class="rail-m"><h2 class="h2">{e(headline)}</h2></div>
    <div class="rail-r">
      <p class="body">{e(body)}</p>
      {f'<p class="micro-note">{e(note)}</p>' if note else ''}
      {f'<span class="counter">{e(counter)}</span>' if counter else ''}
    </div>
  </div>'''


ARROW = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
         '<path d="M5 12h13M12 5l7 7-7 7" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def status_link(text, href):
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'''
  <a class="status-link reveal" href="{e(href)}"{ext}>
    <span>{e(text)}</span><span class="round-btn">{ARROW}</span>
  </a>'''


# ══════════════════════════════════════════════════════════════════ NAV
nav_links = ''.join(f'<a href="{e(h)}">{e(t)}</a>' for t, h in NAV)
menu_links = ''.join(
    f'<a href="{e(h)}" class="menu-link" style="--i:{i}"><span>{e(t)}</span>'
    f'<i>{str(i + 1).zfill(2)}</i></a>' for i, (t, h) in enumerate(NAV))

BIKE_SVG = '''<svg class="bike" viewBox="0 0 62 32" fill="none" aria-hidden="true">
  <g class="bike-smoke">
    <circle cx="9" cy="24.4" r="1.7"/><circle cx="5.4" cy="21.4" r="2.3"/><circle cx="2.6" cy="17.6" r="1.6"/>
  </g>
  <g class="bike-body" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="16" cy="21.5" r="7.6"/>
    <circle cx="48" cy="21.5" r="7.6"/>
    <path d="M12.6 26 L22 24.2"/>
    <path d="M16 21.5 H27"/>
    <path d="M42.5 12.8 L48 21.5"/>
    <path d="M42.5 12.8 L45.5 8.2"/>
    <path d="M41.5 7.4 H49"/>
  </g>
  <g class="bike-body-fill" fill="currentColor">
    <rect x="25.4" y="16.8" width="10.4" height="6.6" rx="2.1"/>
    <path d="M17.6 13.4 h8.9 l4.6 -3.7 h7.4 l3.4 3.9 -8.4 2.2 -6.6 1.1 -6.6 0 a2 2 0 0 1 -2.7 -3.5 z"/>
  </g>
</svg>'''


PHONE_SVG = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 '
             '19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 '
             '0 1 2 1.7c.1 1 .3 1.9.6 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 '
             '2.1-.4c.9.3 1.8.5 2.8.6a2 2 0 0 1 1.7 2z" stroke="currentColor" stroke-width="1.7" '
             'stroke-linecap="round" stroke-linejoin="round"/></svg>')

NAVBAR = f'''
<div class="scroll-progress"><i></i></div>
<header class="site-head" id="siteHead">
  <div class="site-head-in">
    <a class="site-head-logo" href="#top" aria-label="{e(BRAND['full'])} home">
      <img src="assets/img/logo.webp" alt="{e(BRAND['name'])}" width="150" height="58">
    </a>
    <nav class="site-nav" aria-label="Primary">{nav_links}</nav>
    <a class="btn btn-accent site-head-cta" href="{WA}" target="_blank" rel="noopener">
      {PHONE_SVG}<span>Book Appointment</span></a>
    <button class="site-burger" id="burger" type="button" aria-label="Open menu"
            aria-expanded="false" aria-controls="menu">{BIKE_SVG}</button>
  </div>
</header>
<div class="site-menu" id="menu" hidden>
  <nav class="site-menu-links">{menu_links}</nav>
  <div class="site-menu-foot">
    <div><span class="micro">Studio</span><p>{e(BRAND['address_l1'])}<br>{e(BRAND['address_l2'])}</p></div>
    <div><span class="micro">Contact</span><p><a href="tel:+{e(BRAND['phone_raw'])}">{e(BRAND['phone_display'])}</a><br>
      <a href="mailto:{e(BRAND['email'])}">{e(BRAND['email'])}</a></p></div>
    <a class="btn btn-accent" href="{WA}" target="_blank" rel="noopener">{PHONE_SVG}<span>Book Appointment</span></a>
  </div>
</div>'''

# ═════════════════════════════════════════════════════════════════ HERO
stats = ''.join(f'''
      <div class="stat" data-appear="{'stat1' if i == 0 else 'stat2'}">
        <span class="stat-num" data-count="{e(n)}">{e(n)}</span><span class="stat-suffix">{e(suf)}</span>
        <span class="stat-rule"></span>
        <span class="stat-lock"><b>{e(l1)}</b><i>{e(l2)}</i></span>
      </div>''' for i, (n, suf, l1, l2) in enumerate(HERO['stats']))

HERO_HTML = f'''
<section class="hero" id="top">
  <div class="hero-bg" data-appear="bg">
    <picture>
      <source media="(max-width:809px)" srcset="assets/img/hero-m1.webp">
      <img src="assets/img/hero1.webp" alt="" fetchpriority="high" width="1920" height="1279">
    </picture>
    <canvas class="hero-particles" aria-hidden="true"></canvas>
    <div class="hero-veil"></div>
  </div>
  <div class="hero-content">
    <div class="hero-wrap">
      <div class="hero-slogan">
        <span data-appear="s1">{e(HERO['slogan_1'])}</span>
        <span data-appear="s2"><b>{e(HERO['slogan_2'])}</b></span>
      </div>
      <div class="hero-main">
        <h1 class="hero-h1" data-appear="h1">{accent(HERO['headline'])}</h1>
        <div class="hero-cta">
          <div class="hero-lock">
            <p class="hero-cta-title" data-appear="ct">{e(HERO['cta_title'])}</p>
            <p class="hero-cta-sub" data-appear="cs">{e(HERO['cta_sub'])}</p>
          </div>
          <span class="hero-rule" data-appear="rule"></span>
          <a class="btn btn-accent" data-appear="btn" href="{WA}" target="_blank" rel="noopener">
            <span class="btn-ico">{ARROW}</span><span>{e(HERO['cta_label'])}</span></a>
        </div>
        <div class="hero-stats">{stats}</div>
      </div>
      <a class="hero-card" data-appear="card" href="#packages">
        <div class="hero-card-media">
          <video src="{e(HERO['card_video'])}" autoplay muted loop playsinline preload="metadata"></video>
        </div>
        <div class="hero-card-foot">
          <div><b>{e(HERO['card_title'])}</b><i>{e(HERO['card_sub'])}</i></div>
          <span class="round-btn sm">{ARROW}</span>
        </div>
      </a>
    </div>
  </div>
</section>'''

# ════════════════════════════════════════════════════════════════ INTRO
INTRO_HTML = f'''
<section class="intro" id="intro">
  <div class="intro-text"><p class="scrub">{chars(INTRO)}</p></div>
  <div class="intro-orbs" aria-hidden="true">
    <span class="orb o1" data-speed="0.18"></span><span class="orb o2" data-speed="-0.12"></span>
    <span class="orb o3" data-speed="0.26"></span><span class="orb o4" data-speed="-0.2"></span>
  </div>
  <div class="dots" aria-hidden="true">{''.join('<i></i>' for _ in range(7))}</div>
</section>'''

# ═══════════════════════════════════════════════════════════════ 001 WORK
tiles = ''.join(f'''
    <a class="w-tile reveal" href="#work" style="--d:{i * 60}ms">
      <img src="{e(src)}" alt="{e(t)}" loading="lazy" width="760" height="1000">
      <span class="w-tag">{e(t)}</span><span class="sq-btn">{ARROW}</span>
    </a>''' for i, (t, src) in enumerate(WORK['tiles']))

WORK_HTML = f'''
<section class="sec" id="work-sec">
{head_rail(WORK['label'], WORK['index'], WORK['headline'], WORK['body'], WORK['note'], WORK['counter'], 'work')}
  <div class="w-grid">
    <a class="w-feature reveal" href="#packages">
      <img src="{e(WORK['feature']['img'])}" alt="{e(WORK['feature']['title'])}" loading="lazy" width="760" height="1000">
      <div class="w-feature-body">
        <span class="micro">{e(WORK['feature']['kicker'])}</span>
        <h3 class="h3">{e(WORK['feature']['title'])}</h3>
        <p class="small">{e(WORK['feature']['body'])}</p>
      </div>
      <span class="sq-btn">{ARROW}</span>
    </a>
    <div class="w-wide reveal">
      <img src="{e(WORK['wide']['img'])}" alt="{e(WORK['wide']['title'])}" loading="lazy" width="760" height="1000">
      <div class="w-wide-body">
        <span class="micro">{e(WORK['wide']['kicker'])}</span>
        <h3 class="h3">{e(WORK['wide']['title'])}</h3>
        <p class="small">{e(WORK['wide']['body'])}</p>
      </div>
    </div>
    {tiles}
  </div>
  <div class="marquee mini reveal" aria-hidden="true"><div class="mq-track" data-speed="38">
    {''.join(f'<span>{e(WORK["marquee"])}</span><span class="mq-dot"></span>' for _ in range(8))}
  </div></div>
{status_link(*WORK['cta'])}
</section>'''

# ════════════════════════════════════════════════════════════ 002 PROCESS
panels = ''.join(f'''
    <article class="panel{' is-open' if i == 0 else ''}" data-panel="{i}">
      <button class="panel-head" aria-expanded="{'true' if i == 0 else 'false'}">
        <span class="panel-num">{e(num)}</span>
        <span class="panel-arrow">{ARROW}</span>
      </button>
      <div class="panel-body">
        <div class="panel-inner">
          <div class="panel-text">
            <h3 class="panel-title">{e(title)}</h3>
            <p class="panel-copy">{e(body)}</p>
          </div>
          <div class="panel-img"><img src="{e(img)}" alt="{e(title)}" loading="lazy" width="760" height="1000"></div>
        </div>
      </div>
      <span class="panel-label">{e(title)}</span>
    </article>''' for i, (num, title, body, img) in enumerate(PROCESS['panels']))

foot = ''.join(f'<div><b>{e(a)}</b><i>{e(b)}</i></div>' for a, b in PROCESS['footnote'])

PROCESS_HTML = f'''
<section class="sec" id="process-sec">
{head_rail(PROCESS['label'], PROCESS['index'], PROCESS['headline'], PROCESS['body'], PROCESS['note'], PROCESS['counter'], 'process')}
  <div class="panels reveal">{panels}</div>
  <div class="proc-foot reveal">{foot}</div>
{status_link(*PROCESS['cta'])}
</section>'''

# ════════════════════════════════════════════════════════════ 003 EXHAUST
ex_cards = ''.join(f'''
    <article class="stack-card" style="--i:{i};--n:{len(EXHAUST['sets'])}">
      <div class="stack-inner">
        <div class="ex-pair">
          <figure><video src="{e(b)}" muted loop playsinline preload="none"></video><figcaption>Before</figcaption></figure>
          <figure><video src="{e(a)}" muted loop playsinline preload="none"></video><figcaption>After</figcaption></figure>
        </div>
        <div class="ex-meta">
          <span class="stack-count">{str(i + 1).zfill(2)} <i>/</i> {str(len(EXHAUST['sets'])).zfill(2)}</span>
          <h3 class="h3">{e(name)}</h3>
          <p class="body">{e(desc)}</p>
        </div>
      </div>
    </article>''' for i, (name, desc, b, a) in enumerate(EXHAUST['sets']))

spec = ''.join(f'<div><b>{e(a)}</b><i>{e(b)}</i></div>' for a, b in EXHAUST['spec'])

EXHAUST_HTML = f'''
<section class="sec" id="exhaust-sec">
{head_rail(EXHAUST['label'], EXHAUST['index'], EXHAUST['headline'], EXHAUST['body'], anchor='exhaust')}
  <div class="stack" data-stack="exhaust">{ex_cards}</div>
  <div class="proc-foot reveal">{spec}</div>
{status_link(*EXHAUST['cta'])}
</section>'''

# ══════════════════════════════════════════════════════════════ 004 REELS
clips = ''.join(f'''
      <div class="reel" style="--d:{i * 70}ms">
        <video src="{e(c)}" autoplay muted loop playsinline preload="none"></video>
      </div>''' for i, c in enumerate(REELS['clips']))

REELS_HTML = f'''
<section class="sec" id="reels-sec">
{head_rail(REELS['label'], REELS['index'], REELS['headline'], REELS['body'], anchor='reels')}
  <div class="reels-marquee reveal" aria-hidden="true">
    <div class="mq-track" data-speed="26">{clips}{clips}</div>
  </div>
{status_link(*REELS['cta'])}
</section>'''

# ═══════════════════════════════════════════════════════════ 005 PACKAGES
plans = ''
for i, p in enumerate(PACKAGES['plans']):
    feats = ''.join(f'<li>{e(f)}</li>' for f in p['features'])
    plans += f'''
    <article class="plan{' is-featured' if p['featured'] else ''} reveal" style="--d:{(i % 3) * 80}ms">
      <div class="plan-media">
        <img src="{e(p['img'])}" alt="{e(p['name'])}" loading="lazy" width="1100" height="887">
        <span class="plan-kicker">{e(p['kicker'])}</span>
      </div>
      <div class="plan-body">
        <h3 class="plan-name">{e(p['name'])}</h3>
        <p class="plan-blurb">{e(p['blurb'])}</p>
        <div class="plan-price">
          {f'<span class="plan-prefix">{e(p["prefix"])}</span>' if p['prefix'] else ''}
          <span class="plan-amt">{e(p['price'])}</span>
          <span class="plan-dur">{e(p['duration'])}</span>
        </div>
        <ul class="plan-feats">{feats}</ul>
        <a class="btn {'btn-accent' if p['featured'] else 'btn-ghost'} plan-cta"
           href="{WA_PKG(p['name'], p['price'], p['duration'])}" target="_blank" rel="noopener">
          <span>{e(p['cta'])}</span>{ARROW}</a>
      </div>
    </article>'''

PACKAGES_HTML = f'''
<section class="sec" id="packages-sec">
{head_rail(PACKAGES['label'], PACKAGES['index'], PACKAGES['headline'], PACKAGES['body'], PACKAGES['note'], anchor='packages')}
  <div class="plans">{plans}</div>
{status_link(*PACKAGES['cta'])}
</section>'''

# ════════════════════════════════════════════════════════════════ 006 FAQ
faqs = ''.join(f'''
      <div class="faq-item" data-faq>
        <button class="faq-q" aria-expanded="false"><span>{e(q)}</span><span class="faq-ico"><i></i><i></i></span></button>
        <div class="faq-a"><p>{e(a)}</p></div>
      </div>''' for q, a in FAQ['items'])

FAQ_HTML = f'''
<section class="sec" id="faq-sec">
{head_rail(FAQ['label'], FAQ['index'], FAQ['headline'], FAQ['body'], anchor='faq')}
  <div class="faq-grid">
    <div class="faq-col reveal">{faqs}</div>
    <aside class="faq-aside reveal">
      <h3 class="h3">{e(FAQ['aside']['title'])}</h3>
      <p class="body">{e(FAQ['aside']['body'])}</p>
      <a class="btn btn-accent" href="{WA}" target="_blank" rel="noopener">
        <span>{e(FAQ['aside']['cta'])}</span>{ARROW}</a>
    </aside>
  </div>
  <div class="marquee big reveal" aria-hidden="true"><div class="mq-track" data-speed="46">
    {''.join(f'<span>{e(FAQ["marquee"])}</span>' for _ in range(8))}
  </div></div>
</section>'''

# ═══════════════════════════════════════════════════════════════ 007 TEAM
members = ''.join(f'''
    <article class="stack-card tm-card" style="--i:{i};--n:{len(TEAM['members'])}">
      <div class="tm-inner">
        <div class="tm-photo"><img src="{e(img)}" alt="" loading="lazy" width="800" height="800"></div>
        <div class="tm-body">
          <span class="stack-count">{str(i + 1).zfill(2)} <i>/</i> {str(len(TEAM['members'])).zfill(2)}</span>
          <h3 class="h3">{e(name)}</h3>
          <p class="tm-role">{e(role)}</p>
          <p class="body">{e(bio)}</p>
          <span class="micro tm-note">{e(TEAM['placeholder_note'])}</span>
        </div>
      </div>
    </article>''' for i, (name, role, bio, img) in enumerate(TEAM['members']))

TEAM_HTML = f'''
<section class="sec" id="team-sec">
{head_rail(TEAM['label'], TEAM['index'], TEAM['headline'], TEAM['body'], anchor='team')}
  <div class="stack tm-stack" data-stack="team">{members}</div>
{status_link(*TEAM['cta'])}
</section>'''

# ════════════════════════════════════════════════════════════ 008 REVIEWS
def rv_card(nm, ago, txt):
    return (f'<article class="rv-card"><span class="rv-mark">&rdquo;</span>'
            f'<p class="rv-quote">{e(txt)}</p>'
            f'<div class="rv-by"><span class="rv-av">{e(nm[0].upper())}</span>'
            f'<span class="rv-meta"><b>{e(nm)}</b><i>{e(ago)} &middot; Google</i></span>'
            f'</div></article>')


_half = (len(REVIEWS['items']) + 1) // 2
row_a = ''.join(rv_card(*r) for r in REVIEWS['items'][:_half])
row_b = ''.join(rv_card(*r) for r in REVIEWS['items'][_half:])

REVIEWS_HTML = f'''
<section class="sec" id="reviews-sec">
{head_rail(REVIEWS['label'], REVIEWS['index'], REVIEWS['headline'], REVIEWS['body'], anchor='reviews')}
  <div class="rv-rating reveal">
    <b>{e(REVIEWS['rating'])}</b>
    <span class="rv-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
    <span class="micro">Rated by riders who value finish, care, and attention to detail.</span>
  </div>
  <div class="rv-rails">
    <div class="rv-rail"><div class="mq-track" data-speed="26">{row_a}{row_a}</div></div>
    <div class="rv-rail"><div class="mq-track" data-speed="-22">{row_b}{row_b}</div></div>
  </div>
{status_link(*REVIEWS['cta'])}
</section>'''

# ══════════════════════════════════════════════════════════ 009 AFTERCARE
cards = ''
for i, c in enumerate(AFTERCARE['cards']):
    meta = ''.join(f'<div><span>{e(a)}</span><b>{e(b)}</b></div>' for a, b in c['meta'])
    pts = ''.join(f'<li>{e(p)}</li>' for p in c['points'])
    cards += f'''
    <article class="ac-card reveal" style="--d:{i * 90}ms">
      <div class="ac-stage"><img src="{e(c['img'])}" alt="{e(c['title'])}" loading="lazy"></div>
      <div class="ac-body">
        <span class="micro">{e(c['kicker'])}</span>
        <h3 class="h3">{e(c['title'])}</h3>
        <p class="ac-lede">{e(c['lede'])}</p>
        <p class="small">{e(c['body'])}</p>
        <div class="ac-meta">{meta}</div>
        <ul class="ac-points">{pts}</ul>
      </div>
    </article>'''

AFTERCARE_HTML = f'''
<section class="sec" id="aftercare-sec">
{head_rail(AFTERCARE['label'], AFTERCARE['index'], AFTERCARE['headline'], AFTERCARE['body'], anchor='aftercare')}
  <div class="ac-grid">{cards}</div>
{status_link(*AFTERCARE['cta'])}
</section>'''

# ════════════════════════════════════════════════════════════════ CONTACT
fields = ''.join(f'''
        <label class="field"><span class="sr-only">{e(ph)}</span>
          <input type="{t}" name="{n}" placeholder="{e(ph)}"{' required' if req else ''}></label>'''
                 for n, t, ph, req in CONTACT['form_fields'])

pkg_opts = ''.join(
    f'<option value="{e(p["name"])} — {e(p["prefix"] + " " if p["prefix"] else "")}{e(p["price"])} '
    f'({e(p["duration"])})">{e(p["name"])} — {e(p["prefix"] + " " if p["prefix"] else "")}{e(p["price"])}</option>'
    for p in PACKAGES['plans'])

offers = ''.join(f'<li>{e(o)}</li>' for o in CONTACT['offers'])
socials = ''.join(f'<a href="{e(h)}" target="_blank" rel="noopener">{e(t)}</a>'
                  for t, h in CONTACT['socials'])

CONTACT_HTML = f'''
<section class="contact" id="contact">
  <div class="ct-inner">
    <div class="ct-l">
      <span class="micro">{e(CONTACT['label'])}</span>
      <h2 class="ct-h">{e(CONTACT['headline'])}</h2>
      <p class="body ct-body">{e(CONTACT['body'])}</p>
      <div class="ct-social"><span class="micro">Follow us</span><div>{socials}</div></div>
      <div class="ct-offer"><span class="micro">{e(CONTACT['offer_title'])}</span><ul>{offers}</ul></div>
    </div>
    <div class="ct-r">
      <p class="ct-kicker">{e(CONTACT['kicker'])}</p>
      <form class="ct-form" novalidate>
        {fields}
        <label class="field">
          <span class="sr-only">{e(CONTACT['package_label'])}</span>
          <select name="package" aria-label="{e(CONTACT['package_label'])}">
            <option value="">{e(CONTACT['package_default'])}</option>
            {pkg_opts}
          </select>
        </label>
        <label class="field"><span class="sr-only">{e(CONTACT['form_message'])}</span>
          <textarea name="message" rows="4" placeholder="{e(CONTACT['form_message'])}"></textarea></label>
        <button class="btn btn-accent ct-submit" type="submit"><span>{e(CONTACT['submit'])}</span>{ARROW}</button>
        <p class="ct-legal">{e(CONTACT['legal'])} It opens WhatsApp to {e(BRAND['phone_display'])} with your details filled in.</p>
      </form>
    </div>
  </div>
</section>'''

# ═════════════════════════════════════════════════════════════════ FOOTER
cols = ''.join(
    f'''<div class="ft-col"><span class="micro">{e(t)}</span>
        {''.join(f'<a href="{e(h)}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{e(n)}</a>' for n, h in ls)}
      </div>''' for t, ls in FOOTER['cols'])

FOOTER_HTML = f'''
<footer class="footer">
  <div class="ft-top">
    <div class="ft-brand">
      <img src="assets/img/logo.webp" alt="{e(BRAND['name'])}" width="220" height="86">
      <p class="small">{e(FOOTER['blurb'])}</p>
    </div>
    {cols}
    <div class="ft-col ft-contact">
      <span class="micro">Studio</span>
      <a href="tel:+{e(BRAND['phone_raw'])}">{e(BRAND['phone_display'])}</a>
      <a href="mailto:{e(BRAND['email'])}">{e(BRAND['email'])}</a>
      <p class="small">{e(BRAND['address_l1'])}<br>{e(BRAND['address_l2'])}<br>{e(BRAND['address_l3'])}</p>
    </div>
    <div class="ft-news">
      <span class="micro">{e(FOOTER['newsletter_title'])}</span>
      <p class="small">{e(FOOTER['newsletter_body'])}</p>
      <form class="ft-form" novalidate>
        <input type="email" name="email" placeholder="Your Email" aria-label="Your Email">
        <button class="round-btn sm" type="submit" aria-label="Subscribe">{ARROW}</button>
      </form>
    </div>
  </div>
  <div class="ft-word" aria-hidden="true"><img src="assets/img/logo-lg.webp" alt="" width="2000" height="777"></div>
  <div class="ft-bar"><span>{e(FOOTER['copyright'])}</span><a href="#top">Back to top {ARROW}</a></div>
</footer>'''

# ══════════════════════════════════════════════════════════════════ PAGE
PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(BRAND['title'])}</title>
<meta name="description" content="{e(BRAND['description'])}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(BRAND['title'])}">
<meta property="og:description" content="{e(BRAND['description'])}">
<meta property="og:image" content="assets/img/hero1.webp">
<meta name="theme-color" content="#0B0B0B">
<link rel="icon" href="assets/img/logo.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#work">Skip to content</a>
{NAVBAR}
<main>
{HERO_HTML}
{INTRO_HTML}
{WORK_HTML}
{PROCESS_HTML}
{EXHAUST_HTML}
{REELS_HTML}
{PACKAGES_HTML}
{FAQ_HTML}
{TEAM_HTML}
{REVIEWS_HTML}
{AFTERCARE_HTML}
</main>
{CONTACT_HTML}
{FOOTER_HTML}
<button class="to-top" id="toTop" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"
    stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script src="assets/js/main.js"></script>
</body>
</html>'''

if __name__ == '__main__':
    import io, os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write(PAGE)
    print(f'wrote {out}  ({len(PAGE):,} bytes)')
