# DrinKo Cafe — static archive site

A hand-built, framework-free copy of drinkocafe.com's content and pages
("tabs"), meant to keep the site online and looking right after you turn
off Shopify. It's plain HTML/CSS/JS — no monthly platform fee, no build
step required to run it.

## What's included (every tab from the live nav)

- Home (`index.html`)
- Shop (`shop.html`) + all 4 product detail pages (`products/`)
- Pre-order (`pre-order.html`)
- Our Mission (`our-mission.html`)
- FAQ → General Questions & Product Information (`faq-general.html`, `faq-product-information.html`)
- Blog + the "History and Culture of Hong Kong Milk Tea" post (`blog.html`, `blog/`)
- About Us (`about-us.html`)
- Contact (`contact.html`)

All copy, prices, reviews, and the FAQ/product instructions are pulled
directly from the live site as of today.

## What's deliberately different from the Shopify version

Shopify features that need a live backend don't exist on a static site,
so I either removed them or replaced them with something that still works:

- **Cart / checkout** — removed. Every product is already marked "Sold out"
  on the live site anyway, so nothing is actually purchasable right now.
- **Customer log-in / accounts** — removed (no backend to authenticate against).
- **Currency & country switcher** — removed; the store only ever sold in USD.
- **Language switcher (English / 繁體中文)** — not included. The live pages
  only exposed English text to me, so I didn't want to guess at Chinese
  copy and risk getting it wrong. If you have the Chinese text (or want me
  to draft it), I can add a second set of pages.
- **Contact form & newsletter signup** — these can't submit to Shopify
  anymore, so both now open the visitor's email app pre-filled with their
  message (via `mailto:info@drinkocafe.com`). It works with zero backend,
  but if you'd rather have submissions land in an inbox without that popup,
  a free form service like **Formspree** or **Getform** takes about 10
  minutes to wire in — say the word and I'll do it.
- **Search** — removed; with only 4 products it wasn't worth faking.

Nothing else about the shopping experience needs to change, since the
store isn't taking orders at the moment regardless.

## Before you disable Shopify: grab the real photos

I couldn't download your actual product/site photos into this project —
they're only reachable from drinkocafe.com's own CDN, which my sandbox
can't reach. **Placeholder images are in `images/` right now as stand-ins**
so you can preview the site's layout immediately.

To swap in the real ones:

1. Do this **before** you cancel/downgrade Shopify — once the storefront
   is deactivated these CDN URLs stop resolving.
2. On your own computer (this needs a normal internet connection, not
   this chat), run:
   ```
   chmod +x download-images.sh
   ./download-images.sh
   ```
   It fetches all 12 real photos straight from the live CDN links and
   drops them into `images/`, overwriting the placeholders.
3. The homepage "how to make it" video is intentionally not auto-downloaded
   (it's a large file). Its URL is printed at the end of the script if you
   want to grab it manually with the same `curl` pattern, or just leave the
   thumbnail image as a static substitute.

## Previewing locally

No install needed — just open `index.html` in a browser. Or, for paths to
resolve exactly like a real server:

```
cd drinkocafe-site
python3 -m http.server 8000
```
then visit `http://localhost:8000`.

## Hosting it once the domain is on Porkbun

Since this is a static site, you have several good, cheap options:

- **Porkbun Static Hosting** (their own product, ~$3/mo billed yearly) —
  upload via FTP or connect a GitHub repo for auto-deploys. Since the
  domain's already moving to Porkbun, this keeps everything in one place.
- **GitHub Pages / Cloudflare Pages / Netlify** — all free for a static
  site this size, and all let you point drinkocafe.com at them via DNS
  once the transfer settles.

Whichever you pick, you'll just upload the contents of this folder
(minus `build.py` and `download-images.sh`, which are dev tools, not
site files) and point drinkocafe.com's DNS at the new host.

## Editing content later

`build.py` regenerates every HTML page from the data at the top of the
file (product info, FAQ text, mission copy, etc.) plus the shared
header/footer. Edit the Python, then run:
```
python3 build.py
```
to rebuild all pages consistently. You don't need this to just host the
site — it's only for making future edits easier than hunting through 14
separate HTML files.
