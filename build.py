#!/usr/bin/env python3
"""
Generates the static DrinKo Cafe site from shared partials.
Run: python3 build.py
Output: flat, self-contained HTML files ready to upload to any static host.
Edit the CONTENT below and re-run any time you need to update copy.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">' \
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' \
        '<link href="https://fonts.googleapis.com/css2?family=Quattrocento+Sans:wght@400;700&display=swap" rel="stylesheet">'

NAV_ITEMS = [
    ("Home", "index.html", "home"),
    ("Shop", "shop.html", "shop"),
    ("Pre-order", "pre-order.html", "preorder"),
    ("Our Mission", "our-mission.html", "mission"),
    ("FAQ", None, "faq"),
    ("Blog", "blog.html", "blog"),
    ("About Us", "about-us.html", "about"),
    ("Contact", "contact.html", "contact"),
]

FAQ_SUB = [
    ("General Questions", "faq-general.html"),
    ("Product Information", "faq-product-information.html"),
]


def nav_html(base, active):
    parts = []
    for label, href, key in NAV_ITEMS:
        cls = " active" if key == active else ""
        if key == "faq":
            faq_active = " active" if active in ("faq", "faq-general", "faq-product") else ""
            sub = "".join(
                '<a href="{}{}">{}</a>'.format(base, h, l) for l, h in FAQ_SUB
            )
            parts.append(
                '<li class="has-dropdown"><a href="#" class="{}" aria-haspopup="true">FAQ</a>'
                '<div class="dropdown">{}</div></li>'.format(faq_active.strip() or "faq-link", sub)
            )
        else:
            parts.append('<li><a href="{}{}" class="{}">{}</a></li>'.format(base, href, cls, label))
    return "".join(parts)


def render(title, description, base, active, body, extra_head="", switch_href=None):
    switch_link = '<a class="lang-switch" href="{}">中文</a>'.format(switch_href) if switch_href else ""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — DrinKo Cafe</title>
<meta name="description" content="{description}">
{fonts}
<link rel="stylesheet" href="{base}css/style.css">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="announce">We are completely sold out of all products at the moment. Thank YOU so much for your support!</div>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{base}index.html">DrinKo Cafe</a>
    <button class="nav-toggle" aria-expanded="false" aria-label="Toggle menu">&#9776;</button>
    <nav class="primary-nav">
      <ul>{nav}</ul>
    </nav>
    {switch_link}
  </div>
</header>
<main id="main">
{body}
</main>
<div class="mesh-divider" aria-hidden="true"></div>
<footer class="site-footer">
  <div class="footer-wrap">
    <div>
      <div class="eyebrow">DrinKo Cafe</div>
      <p style="max-width:280px">Home-made Hong Kong milk tea, made the way it's always been made — just easier.</p>
      <div class="social-row">
        <a href="https://facebook.com/drinko" target="_blank" rel="noopener">Facebook</a>
        <a href="https://instagram.com/drinko" target="_blank" rel="noopener">Instagram</a>
        <a href="https://youtube.com/drinko" target="_blank" rel="noopener">YouTube</a>
        <a href="https://pinterest.com/drinko" target="_blank" rel="noopener">Pinterest</a>
      </div>
    </div>
    <div class="newsletter">
      <div class="eyebrow">Stay connected</div>
      <p>Subscribe for product launches, discounts, and more.</p>
      <form data-mailto="info@drinkocafe.com" data-subject="Newsletter signup">
        <input type="email" name="email" placeholder="Email" required>
        <button class="btn" type="submit">Subscribe</button>
      </form>
    </div>
  </div>
  <p class="foot-fine">&copy; 2026, DrinKo Cafe</p>
</footer>
<script src="{base}js/main.js"></script>
</body>
</html>""".format(
        title=title, description=description, base=base,
        nav=nav_html(base, active), body=body, fonts=FONTS, extra_head=extra_head,
        switch_link=switch_link
    )


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# ---------------------------------------------------------------
# Reusable product card data
# ---------------------------------------------------------------
PRODUCTS = [
    dict(
        slug="hong-kong-milk-tea",
        name="Classic Hong Kong Milk Tea Bags (8 servings)",
        img="product-tea-bags.jpg",
        price="20.99", was="24.99",
        desc="Premium Hong Kong milk tea bags — 24 tea bags for 8 cups of milk tea.",
        includes=["Premium Hong Kong milk tea bags - 24 tea bags for 8 cups of milk tea"],
        reviews=[
            ("Ann", "Good taste", "The flavor is there but the process in putting it together is a bit inconvenient. If it was a tea bag and we can add milk separately, it will be better than boiling it on stovetop."),
            ("Mandy Lin", None, "Classic Hong Kong Milk Tea Bags (8 servings)"),
            ("Stephen", None, "Very authentic HK milk tea!"),
            ("Nic", None, "Best milk tea i have ever tasted!"),
        ],
    ),
    dict(
        slug="hong-kong-milk-tea-evaporated-milk",
        name="Classic Hong Kong Milk Tea Bags (8 servings) with Extra Creamy Evaporated Milk",
        img="product-tea-evap.jpg",
        price="23.99", was="30.99",
        desc="Premium Hong Kong milk tea bags plus a can of extra creamy evaporated milk.",
        includes=[
            "Premium Hong Kong milk tea bags - 24 tea bags for 8 cups of milk tea",
            "1 Black &amp; White Extra Creamy Evaporated Milk (12 fl oz / 354mL)",
        ],
        reviews=[
            ("KP", "good stuff", "hope Drinko make tea bags for 16oz. and 20oz travel thermos cup size in the very near future"),
            ("Aaron Lai", "Great HK style milk tea", "It should note that the extra creamy milk from the packages are not found in retail and thus this is what you can get only from them. The tea bags are also very good with the right mix of leaves. Just great and strong HK style milk tea!"),
            ("Raymond Chow", "Authentic taste", "If you are from Hong Kong and couldn't go back for milk tea, this will remind you the taste"),
        ],
    ),
    dict(
        slug="hong-kong-milk-tea-evaporated-condensed-milk",
        name="Classic Hong Kong Milk Tea Bags (8 servings) with Extra Creamy Evaporated Milk &amp; Sweetened Condensed Milk",
        img="product-tea-evap-condensed.jpg",
        price="27.99", was="35.99",
        desc="The full set: tea bags, evaporated milk, and sweetened condensed milk.",
        includes=[
            "Premium Hong Kong milk tea bags - 24 tea bags for 8 cups of milk tea",
            "1 Black &amp; White Extra Creamy Evaporated Milk (12 fl oz / 354mL)",
            "1 Black &amp; White Sweetened Condensed Milk (15.8 oz / 448g)",
        ],
        reviews=[
            ("Tea drinker", "Great tea and not available elsewhere", "The extra creamy (both types of milk), in addition to the special tea bags, actually make them unique and tasty."),
        ],
    ),
    dict(
        slug="black-white-cup-saucer",
        name="Black &amp; White Cup and Saucer",
        img="product-cup-saucer-1.jpg",
        img2="product-cup-saucer-2.jpg",
        price="30.00", was=None,
        desc="Classic Black &amp; White 8 fl oz (240mL) cup with saucer.",
        includes=[],
        reviews=[],
    ),
]


def product_card(p, base):
    was_html = ""
    if p["was"]:
        was_html = '<span class="price-strike">${} USD</span>'.format(p["was"])
    return """
<a class="ticket-card" href="{base}products/{slug}.html">
  <span class="stamp">Sold<br>Out</span>
  <div class="thumb"><img src="{base}images/{img}" alt="{name}"></div>
  <div class="info">
    <h3>{name}</h3>
    <div class="price-row">{was}<span class="price-now">${price} USD</span></div>
  </div>
</a>""".format(base=base, slug=p["slug"], img=p["img"], name=p["name"], was=was_html, price=p["price"])


# ---------------------------------------------------------------
# HOME
# ---------------------------------------------------------------
def page_home():
    cards = "".join(product_card(p, "") for p in PRODUCTS[:3])
    body = """
<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow">Welcome</div>
    <h1>Discover the Rich and Authentic Flavors of Hong Kong Milk Tea</h1>
    <p>Make your own authentic Hong Kong Milk Tea anytime and anywhere.</p>
    <a class="btn solid" href="shop.html">Learn More</a>
  </div>
  <img src="images/hero-home.jpg" alt="Hong Kong milk tea">
</section>

<section class="section">
  <div class="section-head">
    <div class="eyebrow">Feature Collection</div>
    <h2>Our Milk Tea Bag Sets</h2>
  </div>
  <div class="grid-products">{cards}</div>
</section>

<div class="feature-panel">
  <div class="eyebrow">Enjoy easy Hong Kong Milk Tea making!</div>
  <h2>How to make it at home</h2>
  <p style="max-width:520px;margin:0 auto 18px">
    Boil, steep, pour over evaporated and condensed milk — ready in about ten minutes.
    See the full walkthrough on our <a href="pages_bridge" style="color:#fff;text-decoration:underline">Instagram</a>
    or read the step-by-step on the Product Information FAQ.
  </p>
  <a class="btn" href="faq-product-information.html">Read the steps</a>
</div>

<section class="section">
  <div class="section-head">
    <div class="eyebrow">Testimonials</div>
    <h2>What people are saying</h2>
  </div>
  <div class="testimonials">
    <div class="testimonial"><h3>Strong Tea flavor</h3><p>&ldquo;I really love how strong the tea aroma and flavor is. It smells and tastes great.&rdquo; &ndash; Jennifer</p></div>
    <div class="testimonial"><h3>So Authentic</h3><p>&ldquo;Very good indeed. One of the best ones I had recently.&rdquo; &ndash; Jessica</p></div>
    <div class="testimonial"><h3>Remind me of Hong Kong</h3><p>&ldquo;Premium quality, as always. It reminds me of those Cha Chan Teng in Hong Kong.&rdquo; &ndash; Stephen</p></div>
  </div>
</section>

<div class="gallery-strip">
  <img src="images/gallery-1.jpg" alt="Hong Kong milk tea gallery">
  <img src="images/gallery-2.jpg" alt="Hong Kong milk tea gallery">
  <img src="images/gallery-3.jpg" alt="Hong Kong milk tea gallery">
  <img src="images/gallery-4.jpg" alt="Hong Kong milk tea gallery">
</div>
""".replace("pages_bridge", "https://instagram.com/drinko").format(cards=cards)
    write("index.html", render(
        "Home-made Hong Kong Milk Tea",
        "Make your own authentic Hong Kong Milk Tea anytime and anywhere",
        "", "home", body, switch_href="zh/index.html"
    ))


# ---------------------------------------------------------------
# SHOP
# ---------------------------------------------------------------
def page_shop():
    cards = "".join(product_card(p, "") for p in PRODUCTS)
    body = """
<div class="section">
  <div class="section-head">
    <div class="eyebrow">Collection</div>
    <h1>All Products</h1>
    <p>4 products</p>
  </div>
  <div class="grid-products">{cards}</div>
</div>
""".format(cards=cards)
    write("shop.html", render("All Products", "Shop DrinKo Cafe's Hong Kong milk tea collection", "", "shop", body, switch_href="zh/shop.html"))


# ---------------------------------------------------------------
# PRODUCT DETAIL PAGES
# ---------------------------------------------------------------
def page_product(p):
    was_html = ""
    if p["was"]:
        was_html = '<span class="price-strike">${} USD</span>'.format(p["was"])
    includes_html = ""
    if p["includes"]:
        includes_html = "<ul>" + "".join("<li>{}</li>".format(i) for i in p["includes"]) + "</ul>"
    else:
        includes_html = "<p>{}</p>".format(p["desc"])

    gallery_imgs = ['<img src="../images/{}" alt="{}">'.format(p["img"], p["name"])]
    if p.get("img2"):
        gallery_imgs.append('<img src="../images/{}" alt="{}">'.format(p["img2"], p["name"]))
    gallery_html = "".join(gallery_imgs)

    if p["reviews"]:
        review_html = "".join(
            """<div class="review"><div class="who">{}</div>{}<p>{}</p></div>""".format(
                who, "<strong>{}</strong>".format(title) + "<br>" if title else "", body
            ) for who, title, body in p["reviews"]
        )
        review_count = "{} review{}".format(len(p["reviews"]), "" if len(p["reviews"]) == 1 else "s")
    else:
        review_html = "<p>Be the first to write a review.</p>"
        review_count = "No reviews yet"

    body = """
<div class="product-detail">
  <div class="gallery">{gallery}</div>
  <div class="info">
    <div class="vendor">DrinKo</div>
    <h1>{name}</h1>
    <p>{desc}</p>
    {includes}
    <p style="font-size:0.85rem">{review_count}</p>
    <div class="price-row">{was}<span class="price-now">${price} USD</span></div>
    <button class="btn disabled" disabled>Sold Out</button>
    <div class="form-note">This product is currently sold out and the shop is on pause. Follow
      <a href="https://instagram.com/drinko" target="_blank" rel="noopener">@drinko</a> on Instagram
      for restock updates, or reach out on the <a href="../contact.html">Contact</a> page.</div>
  </div>
</div>
<div class="section" style="padding-top:0">
  <h2>Customer Reviews</h2>
  {review_html}
</div>
""".format(gallery=gallery_html, name=p["name"], desc=p["desc"], includes=includes_html,
           review_count=review_count, was=was_html, price=p["price"], review_html=review_html)
    write("products/{}.html".format(p["slug"]), render(p["name"], p["desc"], "../", "shop", body, switch_href="../zh/products/{}.html".format(p["slug"])))


# ---------------------------------------------------------------
# PRE-ORDER
# ---------------------------------------------------------------
def page_preorder():
    body = """
<div class="prose">
  <div class="eyebrow">Pre-Order</div>
  <h1>Exclusive Pre-Order Opportunity &amp; More!</h1>
  <p>Ever wished you could enjoy our signature blend with zero prep time? Well, dreams do come true!
  We're thrilled to announce the plan to expand our unique Hong Kong Milk Tea experience! Indulge in
  the authentic taste of Hong Kong, soon in a convenient bottle!</p>
  <p>Join our pre-launch excitement by filling out a simple form. You will also unlock an exclusive
  discount when our bottled milk tea becomes available!</p>
  <p><a class="btn solid" href="https://docs.google.com/forms/d/e/1FAIpQLScTNoTmYPSjW3Un0SRfl9dMmyL9ScK2uvTjb4YoSEoiJ7SgCA/viewform" target="_blank" rel="noopener">Order Interest Form</a></p>
  <img class="feature" src="images/preorder-bottle.jpg" alt="Pre-order bottled milk tea">
</div>
"""
    write("pre-order.html", render(
        "Pre-order", "Join the pre-launch list for bottled Hong Kong milk tea", "", "preorder", body, switch_href="zh/pre-order.html"
    ))


# ---------------------------------------------------------------
# OUR MISSION
# ---------------------------------------------------------------
def page_mission():
    body = """
<div class="prose">
  <div class="eyebrow">Our Mission</div>
  <h1>Our Mission</h1>
  <p>We're passionate about bringing the authentic taste of Hong Kong Milk Tea to homes across the US.
  As Hong Kongers living in the US, we understand the struggle of missing the taste of home. We couldn't
  find any good places that served Hong Kong Milk Tea, so we took matters into our own hands.</p>
  <p>We spent countless hours testing and experimenting with different tea leaves, milk, and brewing
  methods until we finally found the perfect recipe that resembles the taste of the Hong Kong Milk Tea we
  grew up with. Our homemade Hong Kong Milk Tea is made with a blend of premium black tea leaves, brewed
  to perfection and mixed with our secret ingredient, a touch of condensed milk. The result is a creamy,
  aromatic and flavorful beverage that is not only reminiscent of the traditional Hong Kong milk tea found
  in bustling Cha Chan Teng, but also very easy to make at home.</p>
  <p>We would love to share the taste of our home and culture with anyone who appreciates a good cup of
  milk tea. Love to have you on this journey with us, and we can't wait for you to taste the difference
  in every sip of our homemade Hong Kong Milk Tea.</p>
</div>
"""
    write("our-mission.html", render(
        "Our Mission", "Why DrinKo Cafe exists and what we're building toward", "", "mission", body, switch_href="zh/our-mission.html"
    ))


# ---------------------------------------------------------------
# FAQ pages
# ---------------------------------------------------------------
def faq_item(q, a):
    return """<div class="faq-item"><button class="faq-q">{}<span class="icon">+</span></button><div class="faq-a">{}</div></div>""".format(q, a)


def page_faq_general():
    items = [
        ("1) What sets your milk tea apart from the instant options available on the market?",
         "<p>We recognized that the instant Hong Kong Milk Tea available on the market often lacks authenticity, "
         "with an artificial and unsatisfactory taste. This motivated us to take matters into our own hands. Unlike "
         "many instant milk teas that use non-dairy creamer and fail to deliver the desired tea flavor, we place a "
         "strong emphasis on quality. Our tea bags are crafted using premium tea leaves to ensure an authentic and "
         "delightful experience. After undergoing numerous trials, we are able to strike a perfect balance between "
         "the intricate process of making authentic Hong Kong Milk Tea and the convenience of preparing it at home, "
         "enabling you to effortlessly prepare a delicious cup of Hong Kong Milk Tea in the comfort of your own home.</p>"),
        ("2) How long does it take to prepare a cup of homemade Hong Kong Milk Tea?",
         '<p>By following our instructions, you can enjoy a cup of delicious Hong Kong Milk Tea in no more than 10 '
         'minutes. See instructions <a href="faq-product-information.html">here</a>.</p>'),
        ("3) How long will my order take to process?",
         "<p>Please allow 24-48 business hours for your order to process.</p>"),
        ("4) How much is shipping?",
         "<p>At present, we're pleased to extend complimentary standard shipping to all destinations within the "
         "U.S. Our standard shipping method typically ensures delivery within 3-5 business days. Additionally, we "
         "offer the choice to expedite shipping through USPS Priority Mail, which generally delivers within 2 "
         "business days for a nominal fee.</p>"),
        ("5) What is your return policy?",
         '<p>We handle returns on a case-by-case basis with the ultimate objective of making our customers happy. '
         'We stand behind our products and want customers to be satisfied with them. For any inquiries or concerns, '
         'please reach out to <a href="mailto:info@drinkocafe.com">info@drinkocafe.com</a>.</p>'),
    ]
    body = """
<div class="prose">
  <div class="eyebrow">FAQ</div>
  <h1>General Questions</h1>
  {items}
</div>
""".format(items="".join(faq_item(q, a) for q, a in items))
    write("faq-general.html", render("General Questions", "Frequently asked questions about ordering and shipping", "", "faq-general", body, switch_href="zh/faq-general.html"))


def page_faq_product():
    body = """
<div class="prose">
  <div class="eyebrow">FAQ</div>
  <h1>Product Information</h1>

  <div class="faq-item open">
    <button class="faq-q">1) How to prepare a good cup of Hong Kong Milk Tea?<span class="icon">+</span></button>
    <div class="faq-a">
      <p>If you're a reader, we've prepared the instructions below for you!</p>
      <p><strong>Hot Hong Kong Milk Tea</strong></p>
      <ul>
        <li>Bring 1 cup (240mL) water to boil.</li>
        <li>Add 3 tea bags to the boiling water and turn to medium heat to boil for 3 minutes (without a lid).</li>
        <li>Turn off the heat. Put lid on and remove pot from stove. Wait for 3 minutes.</li>
        <li>Reheat to boil again and pour into a cup with 3 tablespoon (45mL) evaporated milk and 1 tablespoon (15mL) condensed milk (or appropriate amount of sugar).</li>
        <li>Ready to serve. <strong>CAUTION: HOT!</strong></li>
      </ul>
      <p><strong>Cold Hong Kong Milk Tea</strong></p>
      <ul>
        <li>Bring 1 cup (240mL) water to boil.</li>
        <li>Add 3 tea bags to the boiling water and turn to medium heat to boil for 3 minutes (without a lid).</li>
        <li>Turn off the heat. Put lid on and remove pot from stove. Wait for 3 minutes.</li>
        <li>Pour into a cup with 3 tablespoon (45mL) evaporated milk and 1 tablespoon (15mL) condensed milk (or appropriate amount of sugar or syrup).</li>
        <li>Put in a refrigerator for 1-2 hours and ready to serve.</li>
      </ul>
    </div>
  </div>

  {q2}
  {q3}
  {q4}
  {q5}
  {q6}
</div>
""".format(
        q2=faq_item("2) What else will I need to make these drinks?",
                     "<ul><li>Small pot with lid</li><li>Measuring spoons and measuring cups</li>"
                     "<li>Drinking glasses or cups</li><li>Evaporated milk (if not purchased)</li>"
                     "<li>Condensed milk (if needed)</li><li>Sugar (if needed)</li></ul>"),
        q3=faq_item("3) What are ways to make the tea flavor stronger or less strong?",
                     "<p>You can brew the tea bags for a little longer for a stronger tea flavor or shorter for a less strong taste.</p>"),
        q4=faq_item("4) How can I change the level of sweetness for my drink?",
                     "<p>You can adjust more or less by the amount of sugar and/or condensed milk according to your taste.</p>"),
        q5=faq_item("5) What are the main ingredients of each product?",
                     "<ul><li>Tea: Black tea</li><li>Evaporated milk: Milk, soybean</li><li>Condensed milk: Milk, sugar</li></ul>"),
        q6=faq_item("6) What is the best way to preserve the freshness of evaporated milk?",
                     "<p>You can transfer the evaporated milk to an airtight container. Instead of using a spoon to "
                     "extract the milk, it's advisable to pour out the desired amount directly from the container. "
                     "This minimizes contact with utensils and helps preserve its quality.</p>"),
    )
    write("faq-product-information.html", render(
        "Product Information", "How to prepare Hong Kong milk tea at home, hot or cold", "", "faq-product", body, switch_href="zh/faq-product-information.html"
    ))


# ---------------------------------------------------------------
# ABOUT US
# ---------------------------------------------------------------
def page_about():
    body = """
<div class="prose">
  <div class="eyebrow">About Us</div>
  <h1>About Us</h1>
  <p>Welcome to our store featuring our homemade Hong Kong Milk Tea. We're excited to share the story of
  how our love for this classic beverage turned into a passion project.</p>
  <p>Growing up in Hong Kong, we were exposed to the aroma of Hong Kong Milk Tea from an early age. This
  beloved beverage is an essential part of our culture and is served in nearly every local restaurant and
  caf&eacute;. However, as we moved away from our hometown and started our lives elsewhere, we found
  ourselves missing the taste of our childhood.</p>
  <p>After trying various instant milk tea mixes on the market, we realized that none of them could
  compare to the authentic taste of Hong Kong Milk Tea. So we decided to take matters into our own hands.
  We started experimenting with different teas, ratios, and brewing methods until we finally hit upon the
  perfect recipe. The result was a creamy, rich, and full-bodied Hong Kong Milk Tea that tasted just like
  the ones we used to have back home.</p>
  <p>We shared our creation with family and friends, who were amazed at how authentic and delicious it
  tasted. That's when we realized that there must be many others out there who were also craving a taste
  of home. And that's why we decided to start this online store, to share our love of Hong Kong Milk Tea
  with everyone in the US who wants to enjoy a cup of authentic and delicious tea anytime and anywhere.</p>
</div>
"""
    write("about-us.html", render("About Us", "The story behind DrinKo Cafe's Hong Kong milk tea", "", "about", body, switch_href="zh/about-us.html"))


# ---------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------
def page_contact():
    body = """
<div class="prose" style="max-width:600px">
  <div class="eyebrow">Contact</div>
  <h1>Contact</h1>
  <p>We'd love to hear from you! If you have any questions or feedback about our Hong Kong Milk Tea or
  our online store, please don't hesitate to reach out to us. You can contact us by email, and we'll do
  our best to get back to you as soon as possible. Thank you for considering our homemade Hong Kong milk
  tea, and we look forward to serving you soon!</p>

  <form data-mailto="info@drinkocafe.com" data-subject="Message from drinkocafe.com contact form">
    <div class="form-field"><label for="name">Name</label><input id="name" name="Name" type="text"></div>
    <div class="form-field"><label for="email">Email *</label><input id="email" name="Email" type="email" required></div>
    <div class="form-field"><label for="phone">Phone number</label><input id="phone" name="Phone" type="tel"></div>
    <div class="form-field"><label for="comment">Comment</label><textarea id="comment" name="Comment"></textarea></div>
    <button class="btn solid" type="submit">Send</button>
  </form>
  <div class="form-note">This form opens your email app with the message pre-filled &mdash; the site has no
  backend to receive submissions directly. If you'd rather email us straight away, write to
  <a href="mailto:info@drinkocafe.com">info@drinkocafe.com</a>.</div>
</div>
"""
    write("contact.html", render("Contact", "Get in touch with DrinKo Cafe", "", "contact", body, switch_href="zh/contact.html"))


# ---------------------------------------------------------------
# BLOG
# ---------------------------------------------------------------
def page_blog():
    body = """
<div class="section">
  <div class="section-head">
    <div class="eyebrow">Blog</div>
    <h1>Feature Articles</h1>
  </div>
  <div class="blog-grid">
    <a class="blog-card" href="blog/history-and-culture-of-hong-kong-milk-tea.html">
      <img src="images/blog-history.jpg" alt="History and Culture of Hong Kong Milk Tea">
      <span class="dateline">July 29, 2023</span>
      <h3>History and Culture of Hong Kong Milk Tea</h3>
      <p>Discover the captivating history and culture of Hong Kong Milk Tea, a beloved beverage that
      originated during the colonial era under British rule.</p>
    </a>
  </div>
</div>
"""
    write("blog.html", render("Feature Articles", "DrinKo Cafe blog: stories about Hong Kong milk tea", "", "blog", body, switch_href="zh/blog.html"))


def page_blog_post():
    body = """
<div class="prose">
  <img class="feature" src="../images/blog-history.jpg" alt="History and Culture of Hong Kong Milk Tea">
  <div class="eyebrow">Blog</div>
  <h1>History and Culture of Hong Kong Milk Tea</h1>
  <span class="dateline">July 29, 2023</span>

  <p>Hong Kong was once a British colony, and the origin of Hong Kong-style milk tea can be traced back
  to the colonial period under British rule. After the opening of Hong Kong in 1842, the British
  introduced English-style milk tea to Hong Kong. However, they used expensive Indian Assam black tea,
  which was unaffordable for white-collar workers and ordinary citizens, so it did not become popular
  among the local population.</p>

  <p>After 1952, due to the rapid increase in Hong Kong's population, many Dai Pai Dong's (street food
  stalls) appeared on the market, attracting customers with milk tea. However, this was not the expensive
  "English-style milk tea," but rather the innovative and modified Hong Kong-style milk tea created by the
  locals. It was not only more suitable for the local taste but also more robust in flavor. This unique
  Hong Kong-style milk tea used a blend of multiple types of black tea, filtered through homemade fine
  mesh tea bags to remove tea residue. The white cloth bags used for filtering became stained with tea
  after repeated use, resembling women's silk stockings, hence commonly known as &ldquo;silk-stocking&rdquo;
  milk tea or &ldquo;pantyhose&rdquo; milk tea. These Dai Pai Dong's also started using evaporated milk
  instead of fresh milk to make milk tea, completely transforming the English-style milk tea into a
  unique Hong Kong-style milk tea.</p>

  <p>As time went by, while an increasing number of restaurants offering a wide variety of food emerged
  in Hong Kong, "Hong Kong-style milk tea" remained the highlight of these eateries without the need for
  special promotion or emphasis on its availability. It naturally became a part of Hong Kong people's
  lives and culinary culture. To this day, Hong Kong-style milk tea is not only a local beverage but also
  a cultural symbol of Hong Kong.</p>

  <p>Originally born out of the hustle and bustle of making a living, it unexpectedly became a part of
  Hong Kong's culture, enduring the test of time and quickly gaining fame as a beverage enjoyed overseas
  &ndash; a sought-after delicacy for people from different regions and a source of pride for Hong Kong
  people. In 2014, the craftsmanship of making Hong Kong-style milk tea was recognized as an intangible
  cultural heritage in Hong Kong. In 2017, the Hong Kong government officially included the craftsmanship
  of making Hong Kong-style milk tea on the list of Hong Kong's intangible cultural heritage.</p>

  <p><a href="../blog.html">&larr; Back to blog</a></p>
</div>
"""
    write("blog/history-and-culture-of-hong-kong-milk-tea.html", render(
        "History and Culture of Hong Kong Milk Tea",
        "Uncover the history and culture of Hong Kong milk tea, a colonial-era creation",
        "../", "blog", body, switch_href="../zh/blog/history-and-culture-of-hong-kong-milk-tea.html"
    ))


if __name__ == "__main__":
    page_home()
    page_shop()
    for p in PRODUCTS:
        page_product(p)
    page_preorder()
    page_mission()
    page_faq_general()
    page_faq_product()
    page_about()
    page_contact()
    page_blog()
    page_blog_post()
    print("Build complete.")
