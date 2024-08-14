from PIL import Image, ImageDraw, ImageFont
import datetime
import locale
from common import *

locale.setlocale(locale.LC_ALL, "")

black_img = Image.new("1", (640, 384), 0xFF)
red_img = Image.new("1", (640, 384), 0xFF)

black_draw = ImageDraw.Draw(black_img)
red_draw = ImageDraw.Draw(red_img)

today = datetime.date.today()

###
# CALENDAR
###
dayfont = ImageFont.truetype(find_font('Roboto:style=Bold'), f(120))
red_draw.text((f(50), f(-2)), str(today.day).zfill(2), font=dayfont)

# Save to file
with open("pics/black.bmp", "wb") as f:
    black_img.save(f, "BMP")
with open("pics/red.bmp", "wb") as f:
    red_img.save(f, "BMP")
