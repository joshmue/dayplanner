from PIL import ImageFont
import datetime
import calendar
from ..find_font import find_font
from ..drawer import Drawer

class DayOfWeekDrawer(Drawer):
    def draw(self, red_draw, black_draw, config):
        today = datetime.date.today()
        dow_short = calendar.day_name[today.weekday()][:3].upper()
        dayupfont = ImageFont.truetype(find_font("FiraCode:style=Bold"), self.f(44))
        dayupfont.set_variation_by_name("Bold")
        red_draw.text((self.f(10), self.f(10)), dow_short[0], font=dayupfont)
        red_draw.text((self.f(10), self.f(60)), dow_short[1], font=dayupfont)
        red_draw.text((self.f(10), self.f(110)), dow_short[2], font=dayupfont)
