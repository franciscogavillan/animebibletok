"""Make an episode end-card overlay (1080x1920 transparent PNG) matching the Episode 1 card.

Usage: python3 tools/make_endcard.py <label> <TITLE> "<Genesis ref (KJV)>" "<Next title>" <out.png>
  e.g. python3 tools/make_endcard.py 2A "THE HEAVENS" "Genesis 1:6–8 (KJV)" "The Dry Land" ep02a_endcard.png

The logo block is copied pixel-for-pixel from the approved Ep 01 card; text is set in DejaVu Serif
(condensed, assets/fonts) at the Ep 01 sizes, color (38,32,27) at ~92% opacity. Design it to sit over a bright plate
(the series end-card background is the golden mist of Ep 01 S09; see tools/render_episode.py).
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "episodes", "ep01-in-the-beginning", "ep01_endcard_overlay_1080x1920.webp")
BOLD = os.path.join(ROOT, "assets", "fonts", "DejaVuSerifCondensed-Bold.ttf")
BOOK = os.path.join(ROOT, "assets", "fonts", "DejaVuSerifCondensed.ttf")
INK = (38, 32, 27, 235)
GREY = (70, 64, 58, 215)

def spaced(draw, y, text, font, spacing, fill):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = (1080 - total) / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + spacing

def centered(draw, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text(((1080 - w) / 2, y), text, font=font, fill=fill)

def make(label, title, ref, nxt, out):
    base = Image.open(SRC).convert("RGBA")
    card = Image.new("RGBA", base.size, (0, 0, 0, 0))
    card.paste(base.crop((0, 380, 1080, 1000)), (0, 380))          # logo block, untouched
    d = ImageDraw.Draw(card)
    spaced(d, 1026, f"GENESIS · EPISODE {label}", ImageFont.truetype(BOLD, 31), 10, INK)
    f_title = ImageFont.truetype(BOLD, 64)
    while d.textlength(title, font=f_title) > 940:                  # keep long titles inside the frame
        f_title = ImageFont.truetype(BOLD, f_title.size - 2)
    centered(d, 1079, title, f_title, INK)
    centered(d, 1158, ref, ImageFont.truetype(BOOK, 32), INK)
    centered(d, 1250, f"Next — {nxt}", ImageFont.truetype(BOOK, 30), GREY)
    centered(d, 1318, "@AnimeBibleTok", ImageFont.truetype(BOLD, 37), INK)
    card.save(out)

if __name__ == "__main__":
    make(*sys.argv[1:6])
