from PIL import ImageFont
import datetime
from ..find_font import find_font
from ..drawer import Drawer

class DayDrawer(Drawer):
    def draw(self, red_draw, black_draw, config):
        today = datetime.date.today()
        dayfont = ImageFont.truetype(find_font('Roboto:style=Bold'), self.f(120))
        red_draw.text((self.f(50), self.f(-2)), str(today.day).zfill(2), font=dayfont)
