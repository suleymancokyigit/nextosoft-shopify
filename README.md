# nextosoft-shopify

Nextosoft dijital hizmet paketleri için Shopify mağazası.

- `products.csv` — 10 hizmet paketi, Shopify ürün içe aktarma formatı (Products > Import). Kargo kapalı, stok takibi yok.
- `urunler/NXT-xx.jpg` — 1200x1200 ürün kapakları. `python gorsel_uret.py` ile yeniden üretilir.
- `sayfalar/*.html` — Hakkımızda, İptal/İade, Mesafeli Satış, KVKK (Online Store > Pages'e yapıştır; Settings > Policies'e de aynıları).
- `kaynak/` — nextosoft.com'dan çekilen metin, logo ve görseller.

## Kurulum sırası
1. Shopify mağazası aç (sahip: Nextosoft hesabı), para birimi TRY, ülke Türkiye.
2. Products > Import > `products.csv`; ardından her ürüne `urunler/` görselini ekle.
3. Online Store > Pages: `sayfalar/` içeriğini ekle; Settings > Policies'e iade/mesafeli satış/KVKK.
4. Tema: Dawn; renkler navy #2d2e3d, mavi #478ecc, font Manrope. Tema kodu `tema/` altında tutulacak (Shopify CLI).
5. Settings > Shipping: kargo profili yok (dijital ürün). Settings > Checkout: telefon zorunlu.
6. Ödeme: iyzico veya PayTR; banka havalesi manuel ödeme olarak.
