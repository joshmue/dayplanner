from PIL import Image, ImageDraw, ImageFont
import datetime
import calendar
import locale
from common import *

locale.setlocale(locale.LC_ALL, "")

red_img = Image.open("pics/red.bmp")
red_img.load()

red_draw = ImageDraw.Draw(red_img)

today = datetime.date.today()

###
# CALENDAR
###

dow_short = calendar.day_name[today.weekday()][:3].upper()
dayupfont = ImageFont.truetype(find_font("FiraCode:style=Bold"), f(44))
dayupfont.set_variation_by_name("Bold")
red_draw.text((f(10), f(10)), dow_short[0], font=dayupfont)
red_draw.text((f(10), f(60)), dow_short[1], font=dayupfont)
red_draw.text((f(10), f(110)), dow_short[2], font=dayupfont)

# Save to file
with open("pics/red.bmp", "wb") as f:
    red_img.save(f, "BMP")
