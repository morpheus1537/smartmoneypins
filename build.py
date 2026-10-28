#!/usr/bin/env python3
"""Builds the Smart Money Pins static site. Run: python3 build.py"""
import os, re, datetime
BASE = os.environ.get("SITE_URL", "https://morpheus1537.github.io/smartmoneypins").rstrip("/")
PIN = "https://www.pinterest.com/smartmoneypinsco/"
NAME = "Smart Money Pins"
DISC = "Some posts may contain affiliate links. If you buy through them we may earn a small commission at no extra cost to you."
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;600&display=swap" rel="stylesheet">'
def page(title, desc, body, path, image="assets/logo.jpg", depth=0, kind="website"):
    r = "../" * depth
    url = f"{BASE}/{path}".replace("/index.html", "/")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {NAME}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><link rel="icon" href="{r}assets/favicon.png">
<meta property="og:type" content="{kind}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/{image}">
<meta name="twitter:card" content="summary_large_image">{FONTS}
<link rel="stylesheet" href="{r}assets/style.css">
<script async defer data-pin-hover="true" data-pin-tall="true" src="https://assets.pinterest.com/js/pinit.js"></script>
</head><body><header class="site"><a class="brand" href="{r}index.html"><img src="{r}assets/logo.jpg" alt="{NAME} logo" width="44" height="44"><span>{NAME}</span></a>
<nav><a href="{r}index.html">Home</a><a href="{r}about.html">About</a><a href="{PIN}" target="_blank" rel="noopener">Pinterest</a></nav></header>
<main>{body}</main>
<footer><p class="disc">{DISC}</p><p><a href="{PIN}" target="_blank" rel="noopener">Follow us on Pinterest</a> · <a href="{r}affiliate-disclosure.html">Affiliate Disclosure</a> · <a href="{r}privacy.html">Privacy Policy</a> · <a href="{r}about.html">About</a></p>
<p>Content is for general education and is not financial advice.</p><p>&copy; {datetime.date.today().year} {NAME}</p></footer></body></html>"""

from posts import POSTS
pages, cards = {}, ""
for p in POSTS:
    body = p["body"]
    print(p["slug"], len(re.sub("<[^>]+>", " ", body).split()), "words")
    art = f"""<article class="post"><p class="kicker">Smart Money Basics</p><h1>{p['title']}</h1><p class="meta">Updated {p['date']}</p>
<figure class="pinwrap"><img class="hero" src="../{p['image']}" alt="{p['title']}" width="1000" height="1500" data-pin-description="{p['title']} | {NAME}" data-pin-url="{BASE}/posts/{p['slug']}.html">
<figcaption><a class="btn pin" href="https://www.pinterest.com/pin/create/button/?url={BASE}/posts/{p['slug']}.html&amp;media={BASE}/{p['image']}&amp;description={p['title']}" target="_blank" rel="noopener">Pin it for later</a></figcaption></figure>
{body}
<p class="pin-cta"><a class="btn pin" href="https://www.pinterest.com/pin/create/button/?url={BASE}/posts/{p['slug']}.html&amp;media={BASE}/{p['image']}&amp;description={p['title']}" target="_blank" rel="noopener">Save this guide to Pinterest</a></p></article>"""
    pages[f"posts/{p['slug']}.html"] = page(p["title"], p["desc"], art, f"posts/{p['slug']}.html", p["image"], 1, "article")
    cards += f"""<a class="card" href="posts/{p['slug']}.html"><img src="{p['image']}" alt="" loading="lazy" width="1000" height="1500"><div><h3>{p['title']}</h3><p>{p['desc']}</p></div></a>"""

pages["index.html"] = page("Simple Money Tips for Real Life", "Beginner-friendly budgeting, saving and side hustle guides with free printables.",
 f"""<section class="intro"><img src="assets/logo.jpg" alt="" width="110" height="110"><h1>Simple money moves for real life</h1>
<p>Smart Money Pins shares beginner-friendly guides to budgeting, saving and earning a little extra, without jargon, hype or guilt. Free printables included.</p>
<p><a class="btn" href="{PIN}" target="_blank" rel="noopener">Follow on Pinterest</a></p></section>
<h2 class="sec">Latest guides</h2><div class="grid">{cards}</div>""", "index.html")
pages["about.html"] = page("About", f"About {NAME}.", f"""<article class="post"><h1>About {NAME}</h1>
<p>{NAME} is for people who want to feel calmer about money, not people who already have it all figured out. We write plain-English guides to the basics: making a budget you can stick to, building savings from zero, paying down debt and finding realistic ways to earn extra income.</p>
<p>We keep things practical. No get-rich-quick promises, no made-up numbers, and no shame. When we mention a figure, we tell you where it comes from or how to check it yourself.</p>
<p>Our guides are general education, not personalized financial advice. For decisions about taxes, investing or debt in your specific situation, consider a qualified professional.</p>
<p>Find new ideas every day on <a href="{PIN}" target="_blank" rel="noopener">our Pinterest</a>.</p></article>""", "about.html")
pages["affiliate-disclosure.html"] = page("Affiliate Disclosure", f"How {NAME} earns money.", f"""<article class="post"><h1>Affiliate Disclosure</h1>
<p>{NAME} may include affiliate links in some posts and pins. If you click one and make a purchase or sign up, we may earn a commission at no extra cost to you. Affiliate links are marked as sponsored.</p>
<p>If we join the Amazon Associates Program: As an Amazon Associate we earn from qualifying purchases.</p>
<p>Commissions never decide what we recommend. We only point to products and services we believe are genuinely useful for beginners. Terms, prices and rates change often; always check the provider's current details before signing up.</p>
<p>Questions? Message us through <a href="{PIN}" target="_blank" rel="noopener">Pinterest</a>.</p></article>""", "affiliate-disclosure.html")
pages["privacy.html"] = page("Privacy Policy", f"Privacy policy for {NAME}.", f"""<article class="post"><h1>Privacy Policy</h1><p class="meta">Last updated {datetime.date.today():%B %d, %Y}</p>
<p>This site does not ask you to create an account, does not run its own analytics, and does not collect your name, email, or payment details.</p>
<h2>Third parties</h2><ul><li><strong>Hosting:</strong> our host (GitHub Pages) may keep standard server logs (IP address, browser, pages requested) for security and reliability.</li>
<li><strong>Google Fonts:</strong> fonts are loaded from Google, which receives your IP address under <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google's privacy policy</a>.</li>
<li><strong>Pinterest:</strong> the Pinterest Save button loads a script from Pinterest, which may set cookies under <a href="https://policy.pinterest.com/privacy-policy" target="_blank" rel="noopener">Pinterest's privacy policy</a>.</li>
<li><strong>Affiliate partners:</strong> if you click an affiliate link, the partner may use cookies to credit the referral.</li></ul>
<h2>Your choices</h2><p>You can block or delete cookies in your browser settings. Residents of California and other US states with privacy laws can contact us through Pinterest with any request; we don't sell personal information because we don't collect it.</p>
<h2>Children</h2><p>This site is not directed at children under 13.</p></article>""", "privacy.html")
rows = lambda n: "".join("<tr><td></td><td></td></tr>" for _ in range(n))
pages["printable-50-30-20.html"] = page("Free 50/30/20 Budget Printable", "A free one-page 50/30/20 budget worksheet to print or fill in.", f"""<article class="post printable"><h1>My 50/30/20 Budget</h1>
<p class="noprint"><button class="btn" onclick="window.print()">Print this worksheet</button> <a href="posts/50-30-20-budget-made-simple.html">Back to the guide</a></p>
<p>Month: ____________ &nbsp; Take-home pay: $__________</p>
<table class="ws"><tr><th>Needs target (×0.50)</th><th>Wants target (×0.30)</th><th>Savings &amp; debt target (×0.20)</th></tr><tr><td>$</td><td>$</td><td>$</td></tr></table>
<h2>Needs (50%)</h2><table class="ws"><tr><th>Item</th><th>Amount</th></tr>{rows(8)}<tr><th>Total</th><td>$</td></tr></table>
<h2>Wants (30%)</h2><table class="ws"><tr><th>Item</th><th>Amount</th></tr>{rows(7)}<tr><th>Total</th><td>$</td></tr></table>
<h2>Savings &amp; Debt (20%)</h2><table class="ws"><tr><th>Item</th><th>Amount</th></tr>{rows(5)}<tr><th>Total</th><td>$</td></tr></table>
<p>One change I'll make next month: ____________________________________________</p><p class="meta">smartmoneypins · Smart Money Pins</p></article>""", "printable-50-30-20.html")

for path, html in pages.items():
    open(path, "w").write(html)
today = datetime.date.today().isoformat()
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
 "".join(f"  <url><loc>{BASE}/{p.replace('index.html','')}</loc><lastmod>{today}</lastmod></url>\n" for p in pages) + "</urlset>\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(".nojekyll", "w").write("")
CUSTOM_DOMAIN = None  # set "digitalprofitreview.com" (and SITE_URL) to switch back
if CUSTOM_DOMAIN: open("CNAME", "w").write(CUSTOM_DOMAIN + "\n")
