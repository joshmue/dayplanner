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
daysubfont = ImageFont.truetype(find_font('Roboto:style=Bold'), f(28))
red_draw.text((f(55), f(118)), "%s %s" % (calendar.month_abbr[today.month].upper(), today.year), font=daysubfont)

# Save to file
with open("pics/red.bmp", "wb") as f:
    red_img.save(f, "BMP")
