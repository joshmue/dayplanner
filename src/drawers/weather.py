from PIL import ImageFont
import requests
from ..find_font import find_font
from ..drawer import Drawer

class WeatherDrawer(Drawer):
    def draw(self, red_draw, black_draw, config):
        config = config['openWeather']

        resp = requests.get('https://api.openweathermap.org/data/3.0/onecall', params={
            'appid': config['apiKey'],
            'lat': config['coordinates']['latitude'],
            'lon': config['coordinates']['longitude'],
            'exclude': 'current,minutely,hourly,alerts',
            'units': 'metric'
        })
        resp.raise_for_status()
        weather = resp.json()
        weather_today = weather['daily'][0]
        weather_tomorrow = weather['daily'][1]

        fontawesome = ImageFont.truetype(find_font('Font Awesome 6 Free Solid:style=Solid'), self.f(60))
        fontawesome_small = ImageFont.truetype(find_font('Font Awesome 6 Free Solid:style=Solid'), self.f(32))
        temp_font = ImageFont.truetype(find_font("FiraCode"), self.f(32))
        temp_font.set_variation_by_name("Bold")

        def get_fa_icon(condition_id):
            if condition_id > 800:
                return "\uf6c4"
            mapping = {
                2: "\uf72e", # Thunderstorm
                3: "\uf743", # Drizzle
                5: "\uf73d", # Rain
                6: "\uf2dc", # Snow
                7: "\uf75f", # Atmosphere
                8: "\uf185"  # Clear
            }
            return mapping.get(condition_id // 100, "\uf753")


        def format_temperature(orig):
            temp = f"{orig:.0f}"
            while len(temp) < 3:
                temp = " " + temp
            return temp
        def draw_weather(x, weather):
            # Icon
            icon = get_fa_icon(weather['weather'][0]['id'])
            print(repr(icon))
            iconstartx = self.f(x) + ((self.f(75) - fontawesome.getlength(icon)) // 2)
            black_draw.text((iconstartx, self.f(315)), icon, font=fontawesome)
            # Up-down icons
            black_draw.text((self.f(x + 175), self.f(310)), "\uf062", font=fontawesome_small)
            black_draw.text((self.f(x + 175), self.f(350)), "\uf063", font=fontawesome_small)
            # Temperatures
            black_draw.text((self.f(x + 75), self.f(310)), f"{format_temperature(weather['temp']['max'])}°C", font=temp_font)
            black_draw.text((self.f(x + 75), self.f(350)), f"{format_temperature(weather['temp']['min'])}°C", font=temp_font)

        draw_weather(205, weather_today)
        draw_weather(425, weather_tomorrow)