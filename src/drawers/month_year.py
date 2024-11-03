from PIL import ImageFont
import datetime
import calendar
from ..find_font import find_font
from ..drawer import Drawer

class MonthYearDrawer(Drawer):
    def draw(self, red_draw, black_draw, config):
        today = datetime.date.today()
        daysubfont = ImageFont.truetype(find_font('Roboto:style=Bold'), self.f(28))
        red_draw.text((self.f(55), self.f(118)), "%s %s" % (calendar.month_abbr[today.month].upper(), today.year), font=daysubfont)