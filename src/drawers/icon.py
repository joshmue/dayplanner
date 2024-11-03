from PIL import ImageFont
import datetime
import random
from ..find_font import find_font
from ..drawer import Drawer

class IconDrawer(Drawer):
    def draw(self, red_draw, black_draw, config):
        today = datetime.date.today()

        fontawesome = ImageFont.truetype(find_font('Font Awesome 6 Free Solid:style=Solid'), self.f(160))
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
        startx = (200 - fontawesome.getlength(niceicon)) // 2
        black_draw.text((self.f(startx), self.f(200)), niceicon, font=fontawesome)