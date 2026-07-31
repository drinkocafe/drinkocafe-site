#!/bin/bash
# ============================================================
# Run this on YOUR OWN computer (not on Shopify, not in this
# sandbox) WHILE the Shopify store is still live — these URLs
# stop working once the store/CDN is deactivated.
#
# Usage:
#   chmod +x download-images.sh
#   ./download-images.sh
#
# It saves the real photos into images/, overwriting the
# placeholder squares that ship with this project.
# ============================================================
set -e
cd "$(dirname "$0")/images"

curl -L "https://drinkocafe.com/cdn/shop/files/C870E3C8-29D8-4ED5-990A-39E5D38E7DC5.jpg?v=1690258006" -o hero-home.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/DBF51065-A57D-40D3-987A-54D273268652_92cf211c-5775-42e6-bb61-410b09b6d7c4.jpg?v=1690258752" -o product-tea-bags.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/C92DB638-E4AC-4BE7-B1CB-E526EEA04751_62ebb764-f4ac-45f5-a9ae-979fca0ca27c.jpg?v=1690258505" -o product-tea-evap.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/2055EBA4-3F61-41A3-B2C0-F6303646461A_0669e7d1-b9f9-4ffa-aae0-1c053e5a39e2.jpg?v=1690258558" -o product-tea-evap-condensed.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/IMG_4722.jpg?v=1716400739" -o product-cup-saucer-1.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/IMG_4716.jpg?v=1716400739" -o product-cup-saucer-2.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/HK4.jpg?v=1684027004" -o gallery-1.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/HK5.jpg?v=1684027005" -o gallery-2.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/HK3.jpg?v=1684027004" -o gallery-3.jpg
curl -L "https://drinkocafe.com/cdn/shop/files/HK2.jpg?v=1684027003" -o gallery-4.jpg
curl -L "https://cdn.shopify.com/s/files/1/0756/0003/6151/files/IMG_1748_480x480.jpg?v=1709952980" -o preorder-bottle.jpg
curl -L "https://drinkocafe.com/cdn/shop/articles/10408D96-B5FD-47B3-B81E-DAE421369CAE.jpg?v=1690675670" -o blog-history.jpg

echo ""
echo "Done. Real photos saved into images/, replacing the placeholders."
echo "Optional: the homepage 'how to make it' video is at:"
echo "https://drinkocafe.com/cdn/shop/videos/c/vp/9bcdc171dc8340cea5ec9ec66752708b/9bcdc171dc8340cea5ec9ec66752708b.HD-1080p-2.5Mbps-17523626.mp4"
echo "Download it manually if you want to keep it (it's a large file, ~tens of MB, so it's not fetched automatically here)."
