#!/usr/bin/env python3
"""
Generates the Traditional Chinese (zh) mirror of the site into zh/.
Content sourced from the official Shopify "Translate and Adapt" CSV
export wherever available (page bodies, product copy, FAQ answers,
the blog post, nav labels). A handful of small connective UI strings
(button labels, form field names, review quotes) weren't part of that
export, so they're translated directly here — flagged in the README.
Run: python3 build_zh.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "zh")

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">' \
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' \
        '<link href="https://fonts.googleapis.com/css2?family=Quattrocento+Sans:wght@400;700&family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">'

NAV_ITEMS = [
    ("首頁", "index.html", "home"),
    ("購買", "shop.html", "shop"),
    ("預訂", "pre-order.html", "preorder"),
    ("我們的理念", "our-mission.html", "mission"),
    ("常見問題", None, "faq"),
    ("博客", "blog.html", "blog"),
    ("關於我們", "about-us.html", "about"),
    ("聯絡", "contact.html", "contact"),
]

FAQ_SUB = [
    ("一般問題", "faq-general.html"),
    ("產品資訊", "faq-product-information.html"),
]


def nav_html(base, active):
    parts = []
    for label, href, key in NAV_ITEMS:
        cls = " active" if key == active else ""
        if key == "faq":
            faq_active = " active" if active in ("faq", "faq-general", "faq-product") else ""
            sub = "".join('<a href="{}{}">{}</a>'.format(base, h, l) for l, h in FAQ_SUB)
            parts.append(
                '<li class="has-dropdown"><a href="#" class="{}" aria-haspopup="true">常見問題</a>'
                '<div class="dropdown">{}</div></li>'.format(faq_active.strip() or "faq-link", sub)
            )
        else:
            parts.append('<li><a href="{}{}" class="{}">{}</a></li>'.format(base, href, cls, label))
    return "".join(parts)


def render(title, description, base, active, body, switch_href, extra_head=""):
    asset_base = base + "../"
    return """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — DrinKo Cafe</title>
<meta name="description" content="{description}">
{fonts}
<link rel="stylesheet" href="{asset_base}css/style.css">
<style>body {{ font-family: "Quattrocento Sans", "Noto Sans TC", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}</style>
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">跳至主要內容</a>
<div class="announce">我們目前所有產品都已售罄，非常感謝您的支持！</div>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{base}index.html">DrinKo Cafe</a>
    <button class="nav-toggle" aria-expanded="false" aria-label="切換選單">&#9776;</button>
    <nav class="primary-nav">
      <ul>{nav}</ul>
    </nav>
    <a class="lang-switch" href="{switch_href}">English</a>
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
      <p style="max-width:280px">自家製港式奶茶，一直以來的味道，現在更簡單。</p>
      <div class="social-row">
        <a href="https://facebook.com/drinko" target="_blank" rel="noopener">Facebook</a>
        <a href="https://instagram.com/drinko" target="_blank" rel="noopener">Instagram</a>
        <a href="https://youtube.com/drinko" target="_blank" rel="noopener">YouTube</a>
        <a href="https://pinterest.com/drinko" target="_blank" rel="noopener">Pinterest</a>
      </div>
    </div>
    <div class="newsletter">
      <div class="eyebrow">聯繫我們</div>
      <p>請訂閱我們來獲得最新消息和新產品發佈資訊。</p>
      <form data-mailto="info@drinkocafe.com" data-subject="Newsletter signup (zh)">
        <input type="email" name="email" placeholder="電子郵件" required>
        <button class="btn" type="submit">訂閱</button>
      </form>
    </div>
  </div>
  <p class="foot-fine">&copy; 2026, DrinKo Cafe</p>
</footer>
<script src="{asset_base}js/main.js"></script>
</body>
</html>""".format(
        title=title, description=description, base=base, asset_base=asset_base,
        nav=nav_html(base, active), body=body, fonts=FONTS, extra_head=extra_head,
        switch_href=switch_href
    )


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote zh/" + path)


# ---------------------------------------------------------------
# Products - titles/descriptions from the official CSV export;
# review quotes are my own direct translation (not in the export).
# ---------------------------------------------------------------
PRODUCTS = [
    dict(
        slug="hong-kong-milk-tea",
        name="經典港式奶茶茶包 (8杯份量)",
        img="product-tea-bags.jpg",
        price="20.99", was="24.99",
        desc="高級香港奶茶茶包 - 共24個茶包，可沖泡8杯奶茶。",
        includes=[],
        reviews=[
            ("Ann", "味道不錯", "味道很好，但沖泡過程有點麻煩。如果是茶包形式，可以分開加奶，會比用爐子煮更方便。"),
            ("Mandy Lin", None, "經典港式奶茶茶包 (8杯份量)"),
            ("Stephen", None, "非常正宗的港式奶茶！"),
            ("Nic", None, "我喝過最好喝的奶茶！"),
        ],
    ),
    dict(
        slug="hong-kong-milk-tea-evaporated-milk",
        name="經典港式奶茶茶包 (8杯份量) + 淡奶",
        img="product-tea-evap.jpg",
        price="23.99", was="30.99",
        desc="",
        includes=[
            "高級香港奶茶茶包 - 共24個茶包，可沖泡8杯奶茶",
            "1罐金裝黑白淡奶 (12 fl oz / 354mL)",
        ],
        reviews=[
            ("KP", "好東西", "希望 Drinko 未來能推出適合16oz和20oz隨行保溫杯份量的茶包。"),
            ("Aaron Lai", "出色的港式奶茶", "值得一提的是，包裝中的特濃奶並非零售市面上找到的產品，是只有這裡才能買到的。茶包的茶葉配搭也調配得很好。真的是濃郁出色的港式奶茶！"),
            ("Raymond Chow", "正宗味道", "如果你是香港人，沒辦法回港喝奶茶，這款一定能讓你重新嚐到那個味道。"),
        ],
    ),
    dict(
        slug="hong-kong-milk-tea-evaporated-condensed-milk",
        name="經典港式奶茶茶包 (8杯份量) + 淡奶 + 煉奶",
        img="product-tea-evap-condensed.jpg",
        price="27.99", was="35.99",
        desc="",
        includes=[
            "高級香港奶茶茶包 - 共24個茶包，可沖泡8杯奶茶",
            "1罐金裝黑白淡奶 (12 fl oz / 354mL)",
            "1瓶黑白煉奶 (15.8 oz / 448g)",
        ],
        reviews=[
            ("愛茶人士", "獨特難尋的好茶", "特濃奶（兩款奶品）加上特製茶包，令這款奶茶格外獨特美味。"),
        ],
    ),
    dict(
        slug="black-white-cup-saucer",
        name="黑白奶茶杯套裝",
        img="product-cup-saucer-1.jpg",
        img2="product-cup-saucer-2.jpg",
        price="30.00", was=None,
        desc="經典黑白奶茶杯 (8 fl oz / 240mL) 連碟",
        includes=[],
        reviews=[],
    ),
]


def product_card(p, base):
    was_html = '<span class="price-strike">${} USD</span>'.format(p["was"]) if p["was"] else ""
    return """
<a class="ticket-card" href="{base}products/{slug}.html">
  <span class="stamp">售罄</span>
  <div class="thumb"><img src="{base}images/{img}" alt="{name}"></div>
  <div class="info">
    <h3>{name}</h3>
    <div class="price-row">{was}<span class="price-now">${price} USD</span></div>
  </div>
</a>""".format(base=base, slug=p["slug"], img=p["img"], name=p["name"], was=was_html, price=p["price"])


def page_home():
    cards = "".join(product_card(p, "") for p in PRODUCTS[:3])
    body = """
<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow">齊來品嚐</div>
    <h1>正宗濃郁港式奶茶</h1>
    <p>隨時隨地在家自製一杯正宗的香港奶茶。</p>
    <a class="btn solid" href="shop.html">了解更多</a>
  </div>
  <img src="images/hero-home.jpg" alt="香港奶茶">
</section>

<section class="section">
  <div class="section-head">
    <div class="eyebrow">推介</div>
    <h2>我們的奶茶包系列</h2>
  </div>
  <div class="grid-products">{cards}</div>
</section>

<div class="feature-panel">
  <div class="eyebrow">輕鬆製作香港奶茶！</div>
  <h2>在家輕鬆沖泡</h2>
  <p style="max-width:520px;margin:0 auto 18px">
    煮沸、浸泡、加入淡奶和煉奶——大約十分鐘即可完成。
    歡迎瀏覽我們的 <a href="https://instagram.com/drinko" style="color:#fff;text-decoration:underline">Instagram</a>
    觀看完整教學，或參閱產品資訊常見問題的詳細步驟。
  </p>
  <a class="btn" href="faq-product-information.html">查看步驟</a>
</div>

<section class="section">
  <div class="section-head">
    <div class="eyebrow">顧客意見</div>
    <h2>顧客怎麼說</h2>
  </div>
  <div class="testimonials">
    <div class="testimonial"><h3>濃郁茶香</h3><p>&ldquo;我真的很喜歡這茶香氣和味道有多濃郁，聞起來和喝起來都很棒。&rdquo; &ndash; Jennifer</p></div>
    <div class="testimonial"><h3>非常道地</h3><p>&ldquo;真的很好喝，是我最近喝過最好的其中一款。&rdquo; &ndash; Jessica</p></div>
    <div class="testimonial"><h3>想起香港</h3><p>&ldquo;品質一如既往地優質，讓我想起香港的茶餐廳。&rdquo; &ndash; Stephen</p></div>
  </div>
</section>

<div class="gallery-strip">
  <img src="images/gallery-1.jpg" alt="香港奶茶相片集">
  <img src="images/gallery-2.jpg" alt="香港奶茶相片集">
  <img src="images/gallery-3.jpg" alt="香港奶茶相片集">
  <img src="images/gallery-4.jpg" alt="香港奶茶相片集">
</div>
""".format(cards=cards)
    write("index.html", render(
        "自家製香港奶茶", "隨時隨地在家自製一杯正宗的香港奶茶", "", "home", body, "../index.html"
    ))


def page_shop():
    cards = "".join(product_card(p, "") for p in PRODUCTS)
    body = """
<div class="section">
  <div class="section-head">
    <div class="eyebrow">產品系列</div>
    <h1>我們的產品</h1>
    <p>共 4 件產品</p>
  </div>
  <div class="grid-products">{cards}</div>
</div>
""".format(cards=cards)
    write("shop.html", render("我們的產品", "選購 DrinKo Cafe 的港式奶茶系列", "", "shop", body, "../shop.html"))


def page_product(p):
    was_html = '<span class="price-strike">${} USD</span>'.format(p["was"]) if p["was"] else ""
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
                who, "<strong>{}</strong><br>".format(title) if title else "", body
            ) for who, title, body in p["reviews"]
        )
        review_count = "{} 則評論".format(len(p["reviews"]))
    else:
        review_html = "<p>成為第一位撰寫評論的人。</p>"
        review_count = "暫無評論"

    body = """
<div class="product-detail">
  <div class="gallery">{gallery}</div>
  <div class="info">
    <div class="vendor">DrinKo</div>
    <h1>{name}</h1>
    {includes}
    <p style="font-size:0.85rem">{review_count}</p>
    <div class="price-row">{was}<span class="price-now">${price} USD</span></div>
    <button class="btn disabled" disabled>售罄</button>
    <div class="form-note">此產品目前已售罄，商店暫停營業。請追蹤
      <a href="https://instagram.com/drinko" target="_blank" rel="noopener">Instagram 上的 @drinko</a>
      以獲取補貨消息，或前往<a href="../contact.html">「聯絡」</a>頁面與我們聯繫。</div>
  </div>
</div>
<div class="section" style="padding-top:0">
  <h2>顧客評論</h2>
  {review_html}
</div>
""".format(gallery=gallery_html, name=p["name"], includes=includes_html,
           review_count=review_count, was=was_html, price=p["price"], review_html=review_html)
    write("products/{}.html".format(p["slug"]), render(
        p["name"], p["name"], "../", "shop", body, "../../products/{}.html".format(p["slug"])
    ))


def page_preorder():
    body = """
<div class="prose">
  <div class="eyebrow">預訂</div>
  <h1>獨家預訂！</h1>
  <p>您是否曾經想過，能否不用花時間去準備，便能享用我們的獨特香港奶茶呢？現在夢想成真了！我們很高興地告訴大家，我們計劃擴大我們香港奶茶體驗，希望很快便可以和大家分享我們的樽裝香港奶茶！</p>
  <p>請填寫一份簡單的表格來加入我們的預售清單。當樽裝奶茶上市時，您還可以享用我們的獨家優惠！</p>
  <p><a class="btn solid" href="https://docs.google.com/forms/d/e/1FAIpQLScTNoTmYPSjW3Un0SRfl9dMmyL9ScK2uvTjb4YoSEoiJ7SgCA/viewform" target="_blank" rel="noopener">填寫表格</a></p>
  <img class="feature" src="images/preorder-bottle.jpg" alt="樽裝奶茶預訂">
</div>
"""
    write("pre-order.html", render("預訂", "加入我們的樽裝港式奶茶預售名單", "", "preorder", body, "../pre-order.html"))


def page_mission():
    body = """
<div class="prose">
  <div class="eyebrow">我們的理念</div>
  <h1>我們的理念</h1>
  <p>作為在美國生活的香港人，我們深知思鄉之苦。在市面上我們找了很久，但都找不到好喝的香港奶茶。我們便決定自己親自動手來解決，希望將正宗的香港奶茶帶到美國家中。</p>
  <p>我們花了很多的時間去測試不同的茶葉、牛奶和沖泡方法，經過不斷的試驗和改良，我們終於找到了一個完美的配方，能夠把我們童年的香港奶茶味道再一次呈現眼前。我們自製的香港奶茶使用優質的紅茶，加入了淡奶和煉奶，最終是一杯香濃、芬芳且風味豐富的港式奶茶。這不僅能讓人回味當年繁華的茶餐廳香港奶茶，而且還可以在家中隨時隨地製作。</p>
  <p>我們很樂意與欣賞奶茶的人分享我們的家鄉和文化，期待與您一起踏上這個旅程！</p>
</div>
"""
    write("our-mission.html", render("我們的理念", "DrinKo Cafe 成立的初衷", "", "mission", body, "../our-mission.html"))


def faq_item(q, a):
    return """<div class="faq-item"><button class="faq-q">{}<span class="icon">+</span></button><div class="faq-a">{}</div></div>""".format(q, a)


def page_faq_general():
    items = [
        ("1) 你們的奶茶與市面上的即溶奶茶有甚麼不同的地方？",
         "<p>我們覺得市面上的很多即溶港式奶茶都不正宗，大部份都使用非乳製奶精，很多時候味道都強差人意，無法達到我們的期望。由於我們的目標是要做到香港餐茶廳的水準，我們非常注重品質。我們的茶包都是使用優質茶葉，以確保「原汁原味」。經過多次試驗後，我們在製作正宗港式奶茶的複雜過程和在家製作的便利之間取得了平衡，您現在能在家中輕鬆製作出一杯美味的港式奶茶。</p>"),
        ("2) 製作一杯港式奶茶需要多長時間？",
         '<p>按照我們的沖調方法，您可以在10分鐘的時間內品嚐到美味的港式奶茶。詳情請參閱<a href="faq-product-information.html">這裡</a>。</p>'),
        ("3) 我的訂單需要多久處理？",
         "<p>請給予24至48個工作小時來處理您的訂單。</p>"),
        ("4) 運送是多少？",
         "<p>目前我們為所有美國境內的目的地提供免費的標準運送。通常標準運送訂單將於3-5個工作日內送達。此外，我們還提供通過USPS優先郵件快遞運送的選擇，需要支付一小筆額外費用，一般在2個工作日內送達。</p>"),
        ("5) 你們的退換貨政策是什麼？",
         '<p>我們會根據具體情況處理退/換貨事宜，讓我們的顧客滿意。如有任何問題或疑慮，請聯繫<a href="mailto:info@drinkocafe.com">info@drinkocafe.com</a>。</p>'),
    ]
    body = """
<div class="prose">
  <div class="eyebrow">常見問題</div>
  <h1>一般問題</h1>
  {items}
</div>
""".format(items="".join(faq_item(q, a) for q, a in items))
    write("faq-general.html", render("一般問題", "關於訂購與運送的常見問題", "", "faq-general", body, "../faq-general.html"))


def page_faq_product():
    body = """
<div class="prose">
  <div class="eyebrow">常見問題</div>
  <h1>產品資訊</h1>

  <div class="faq-item open">
    <button class="faq-q">1) 如何沖製一杯美味的港式奶茶？<span class="icon">+</span></button>
    <div class="faq-a">
      <p>來看<a href="https://www.instagram.com/reel/CvdBTytNmaa/" target="_blank" rel="noopener">影片</a>吧！如果你喜歡讀文字的，我們都為你準備了以下的說明！</p>
      <p><strong>熱港式奶茶</strong></p>
      <ul>
        <li>將1杯（240毫升）水煮沸。</li>
        <li>將3個茶包加入沸水中，轉至中火煮沸3分鐘（不要蓋上鍋蓋）。</li>
        <li>關火。蓋上鍋蓋，將鍋子從爐子上拿開。等待3分鐘。</li>
        <li>重新加熱至沸騰，倒入裝有3湯匙（45毫升）淡奶和1湯匙（15毫升）煉奶（或適量砂糖）的杯子中。</li>
        <li>即可享用。<strong>注意：熱飲！</strong></li>
      </ul>
      <p><strong>凍港式奶茶</strong></p>
      <ul>
        <li>將1杯（240毫升）水煮沸。</li>
        <li>將3個茶包加入沸水中，轉至中火煮沸3分鐘（不要蓋上鍋蓋）。</li>
        <li>關火。蓋上鍋蓋，將鍋子從爐子上拿開。等待3分鐘。</li>
        <li>倒入裝有3湯匙（45毫升）淡奶和1湯匙（15毫升）煉奶（或適量砂糖或糖漿）的杯子中。</li>
        <li>放入冰箱冷藏1-2小時，即可享用。</li>
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
        q2=faq_item("2) 製作這些飲品還需要哪些材料？",
                     "<ul><li>有蓋小鍋</li><li>量匙和量杯</li><li>玻璃杯或茶杯</li>"
                     "<li>淡奶（如果沒有購買）</li><li>煉奶（如需要）</li><li>砂糖（如需要）</li></ul>"),
        q3=faq_item("3) 如何使茶的味道更濃或更淡？",
                     "<p>您可以稍微延長茶包的浸泡時間，使茶的味道更濃，或者縮短時間以獲得更淡的口味。</p>"),
        q4=faq_item("4) 如何調節飲品的甜度？",
                     "<p>根據個人口味，您可以根據糖和/或煉奶的用量進行調整，增加或減少甜度。</p>"),
        q5=faq_item("5) 每種產品的主要成分是甚麼？",
                     "<ul><li>茶：紅茶</li><li>淡奶：牛奶、大豆</li><li>煉奶：牛奶、糖</li></ul>"),
        q6=faq_item("6) 怎樣可以有效地保存淡奶？",
                     "<p>您可以先將淡奶倒入密封容器中保存。建議不要使用湯匙取出淡奶，而是直接從容器中倒出所需的份量。這樣可以減少與餐具接觸，有助於保存淡奶品質。</p>"),
    )
    write("faq-product-information.html", render(
        "產品資訊", "在家沖泡港式奶茶的熱飲及凍飲做法", "", "faq-product", body, "../faq-product-information.html"
    ))


def page_about():
    body = """
<div class="prose">
  <div class="eyebrow">關於我們</div>
  <h1>關於我們</h1>
  <p>歡迎光臨！我們很高興可以與您分享我們對香港奶茶的熱愛！</p>
  <p>我們小時候在香港長大，基本上隨時隨地都能喝到港式奶茶。這個深受大家喜愛的飲品幾乎能在每間餐廳和咖啡店都能找到，的而且確是香港文化的重要一部分。雖然我們現在離開了香港，在美國定居，我們很多時候都會想念着兒時在香港喝到的港式奶茶。</p>
  <p>我們在市面上嘗試了各種即沖港式奶茶後，先不要說有沒有一款能比得上香港的質素，很多時候沖出來的味道都不是那回事。我們於是便決定親手來製作自家港式奶茶 ––– 我們嘗試了不同的茶葉、比例和沖泡方法，直到最終找到了完美的配方。成品是一杯奶香濃郁、口感豐富的港式奶茶，就像我們在香港茶餐廳可以品嚐到的！</p>
  <p>我們與親朋好友分享我們的製成品，他們都十分驚訝可以在家中喝到能媲美香港茶餐廳的港式奶茶。這個時候我們想到肯定有其他同好渴望喝到高質素的港式奶茶，所以我們便決定開設這個網店，希望與大家分享我們對港式奶茶的熱愛，更希望與在香港以外生活的朋友提供一個能在家中隨時隨地都能享受到一杯美味港式奶茶的機會。</p>
</div>
"""
    write("about-us.html", render("關於我們", "DrinKo Cafe 港式奶茶的故事", "", "about", body, "../about-us.html"))


def page_contact():
    body = """
<div class="prose" style="max-width:600px">
  <div class="eyebrow">聯絡</div>
  <h1>聯絡</h1>
  <p>我們非常樂意聽取您的意見！如果您對我們的港式奶茶或網店有任何問題或反饋，請隨時與我們聯繫。您可以通過電子郵件或電話與我們聯繫，我們將盡快回覆您。感謝您考慮選購我們自家製作的港式奶茶，我們期待著能夠為您提供服務！</p>

  <form data-mailto="info@drinkocafe.com" data-subject="來自 drinkocafe.com 聯絡表格的訊息 (zh)">
    <div class="form-field"><label for="name">姓名</label><input id="name" name="Name" type="text"></div>
    <div class="form-field"><label for="email">電子郵件 *</label><input id="email" name="Email" type="email" required></div>
    <div class="form-field"><label for="phone">電話號碼</label><input id="phone" name="Phone" type="tel"></div>
    <div class="form-field"><label for="comment">留言</label><textarea id="comment" name="Comment"></textarea></div>
    <button class="btn solid" type="submit">傳送</button>
  </form>
  <div class="form-note">此表格會開啟您的電子郵件應用程式並預先填寫訊息內容——本網站沒有後端伺服器可直接接收表單。如果您想直接發送電郵，請寫信至
  <a href="mailto:info@drinkocafe.com">info@drinkocafe.com</a>。</div>
</div>
"""
    write("contact.html", render("聯絡", "與 DrinKo Cafe 聯繫", "", "contact", body, "../contact.html"))


def page_blog():
    body = """
<div class="section">
  <div class="section-head">
    <div class="eyebrow">博客</div>
    <h1>專題文章</h1>
  </div>
  <div class="blog-grid">
    <a class="blog-card" href="blog/history-and-culture-of-hong-kong-milk-tea.html">
      <img src="images/blog-history.jpg" alt="香港奶茶的歷史文化">
      <span class="dateline">2023年7月29日</span>
      <h3>香港奶茶的歷史文化</h3>
      <p>香港奶茶是一款深受喜愛的飲品，起源於英國統治時期的殖民地時代。這款獨特的茶品有著引人入勝的發展歷程。</p>
    </a>
  </div>
</div>
"""
    write("blog.html", render("專題文章", "DrinKo Cafe 博客：關於香港奶茶的故事", "", "blog", body, "../blog.html"))


def page_blog_post():
    body = """
<div class="prose">
  <img class="feature" src="../images/blog-history.jpg" alt="香港奶茶的歷史文化">
  <div class="eyebrow">博客</div>
  <h1>香港奶茶的歷史文化</h1>
  <span class="dateline">2023年7月29日</span>

  <p data-mce-fragment="1">相信大家都知道香港曾是英國殖民地，而香港奶茶的起源可以追溯到英國統治時期的殖民地時代。1842年香港開埠後，英國人將英式奶茶引進了香港。但是他們使用昂貴的印度阿薩姆紅茶，這對一般白領和普通市民來說是很難負擔得起，因此並不受本地人歡迎。</p>

  <p data-mce-fragment="1">1952年後，由於香港人口急劇增長，許多大排檔開始在市面出現，吸引顧客品嘗奶茶。然而，這不是昂貴的「英式奶茶」，而是由香港本地人創造的創新和改良的香港式奶茶。這種獨特的香港奶茶不僅更適合本地口味，而且風味更加濃郁。這款獨特的香港奶茶使用多種紅茶混合而成，通過自製細網茶包過濾茶渣。過濾所用的白布茶包在多次使用後變得沾滿茶漬，類似絲襪的外觀，因此被俗稱為「絲襪奶茶」。這些大排檔還開始使用淡奶而非鮮奶來製作奶茶，徹底改變了英式奶茶，形成了獨特的香港式奶茶。</p>

  <p data-mce-fragment="1">隨著時間發展，雖然香港出現了越來越多種類的餐館，但「香港式奶茶」仍然是這些餐館的其中一個很多人點的飲品。它很自然地成為香港人生活和飲食文化的一部分。直至今日，香港奶茶不僅是本地的飲品，更是香港的文化象徵。它被認為是一種原創的本地飲品，融入了當地文化，並在許多地方廣泛供應。</p>

  <p data-mce-fragment="1">香港奶茶從最初誕生於忙碌的生計之中，意外地成為香港文化的一部分，經受住時間的考驗，並迅速在海外享負盛名，成為來自不同地區人們追求的美味佳餚，也成為香港人的驕傲。2014年，製作香港奶茶的工藝成為香港無形文化遺產的一部分。2017年，香港政府正式將製作香港奶茶的工藝納入香港無形文化遺產名錄。這些舉措將日常生活的形象提升為高雅的文化形象。</p>

  <p><a href="../blog.html">&larr; 返回博客</a></p>
</div>
"""
    write("blog/history-and-culture-of-hong-kong-milk-tea.html", render(
        "香港奶茶的歷史文化", "香港奶茶的歷史文化——一段源自殖民地時代的故事",
        "../", "blog", body, "../../blog/history-and-culture-of-hong-kong-milk-tea.html"
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
    print("zh build complete.")
