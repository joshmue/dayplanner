from PIL import Image, ImageDraw, ImageFont
import datetime
import locale
import random

locale.setlocale(locale.LC_ALL, "")

black_img = Image.open("pics/black.bmp")
black_img.load()
red_img = Image.open("pics/red.bmp")
red_img.load()

black_draw = ImageDraw.Draw(black_img)
red_draw = ImageDraw.Draw(red_img)

today = datetime.date.today()

factor = 1

def f(i):
    return int(factor * i)

fontawesome = ImageFont.truetype("/opt/fontawesome-free-6.5.2-desktop/otfs/Font Awesome 6 Free-Solid-900.otf", f(160))
niceicon = random.choice([
    "\uf786", # fa-candy-cane
    "\uf1e3", # fa-football
    "\uf7bf", # fa-satellite
    "\uf45f", # fa-volleyball
    "\uf535", # fa-kiwi-bird
    "\uf700", # fa-otter
    "\uf434", # fa-basketball-ball
    "\uf780", # fa-biohazard
    "\uf51a", # fa-broom
    "\uf64f", # fa-city
    "\uf5d2", # fa-atom
    "\uf7a2", # fa-globe-europe
    "\uf7ae", # fa-igloo
    "\uf83e", # fa-wave-square
    "\uf12b", # fa-superscript
])
print("Picked", repr(niceicon))
startx = (200 - fontawesome.getsize(niceicon)[0]) // 2
black_draw.text((f(startx), f(200)), niceicon, font=fontawesome)

# Save to file
with open("pics/black.bmp", "wb") as f:
    black_img.save(f, "BMP")
with open("pics/red.bmp", "wb") as f:
    red_img.save(f, "BMP")
