"""products.csv'den 1200x1200 ürün kapakları üretir -> urunler/<SKU>.jpg"""
import csv, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "urunler"; OUT.mkdir(exist_ok=True)
BG = {"Web": "story-software", "Yazılım": "story-software", "AI": "story-ai", "İş Sistemleri": "story-ai", "Veri": "story-ai"}
NAVY, BLUE, PURPLE, SOFT, MUTED = "#2d2e3d", "#478ecc", "#765ebe", "#f5f7fa", "#b8bfcc"
def font(size, w="Bold"):
    f = ImageFont.truetype(str(ROOT / "kaynak/font/Manrope-Bold.ttf"), size); f.set_variation_by_name(w); return f
def wrap(d, text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]
for r in csv.DictReader(open(ROOT / "products.csv", encoding="utf-8")):
    S = 1200
    bg = Image.open(ROOT / "kaynak/gorsel" / (BG.get(r["Type"], "story-growth") + ".png")).convert("RGB")
    h = bg.height; bg = bg.crop(((bg.width - h) // 2 + (150 if "growth" in BG.get(r["Type"], "growth") else 0), 0, (bg.width - h) // 2 + h + (150 if "growth" in BG.get(r["Type"], "growth") else 0), h)).resize((S, S), Image.LANCZOS)
    # alt yarıyı karart
    grad = Image.new("L", (1, S)); gp = grad.load()
    for y in range(S): gp[0, y] = int(min(255, max(0, (y - 420) / (S - 420) * 235)))
    bg = Image.composite(Image.new("RGB", (S, S), NAVY), bg, grad.resize((S, S)))
    d = ImageDraw.Draw(bg)
    n = r["Variant SKU"].split("-")[1]; title = r["Title"]; price = f"₺{int(r['Variant Price']):,}".replace(",", ".")
    dur = [t for t in r["Tags"].split(", ")][-1]
    d.text((80, 620), f"{n}  ·  {r['Type'].upper()}", font=font(30, "SemiBold"), fill=BLUE)
    y = 680
    for ln in wrap(d, title, font(84), S - 160): d.text((80, y), ln, font=font(84), fill=SOFT); y += 96
    d.text((80, y + 24), f"Başlangıç {price}", font=font(44, "SemiBold"), fill=SOFT)
    d.text((80, y + 92), f"Tahmini teslim: {dur}", font=font(32, "Medium"), fill=MUTED)
    logo = Image.open(ROOT / "kaynak/gorsel/nextosoft-logo-dark.png").convert("RGBA")
    logo = logo.resize((260, int(logo.height * 260 / logo.width)), Image.LANCZOS)
    bg.paste(logo, (S - 80 - logo.width, S - 80 - logo.height), logo)
    bg.save(OUT / f"{r['Variant SKU']}.jpg", quality=90)
    print(r["Variant SKU"], title)
