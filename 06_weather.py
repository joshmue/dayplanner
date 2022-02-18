from PIL import Image, ImageDraw, ImageFont
import requests, yaml

black_img = Image.open("pics/black.bmp")
black_img.load()

black_draw = ImageDraw.Draw(black_img)

factor = 1

def f(i):
    return int(factor * i)

config = yaml.load(open('config.yaml'), yaml.Loader)['openWeather']

resp = requests.get('https://api.openweathermap.org/data/2.5/onecall', params={
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

fontawesome = ImageFont.truetype("/opt/fontawesome-free-5.15.2-desktop/otfs/Font Awesome 5 Free-Solid-900.otf", f(60))
fontawesome_small = ImageFont.truetype("/opt/fontawesome-free-5.15.2-desktop/otfs/Font Awesome 5 Free-Solid-900.otf", f(32))
temp_font = ImageFont.truetype("/usr/share/fonts/opentype/firacode/FiraCode-Bold.otf", f(32))

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
    iconstartx = f(x) + ((f(75) - fontawesome.getsize(icon)[0]) // 2)
    black_draw.text((iconstartx, f(315)), icon, font=fontawesome)
    # Up-down icons
    black_draw.text((f(x + 175), f(310)), "\uf062", font=fontawesome_small)
    black_draw.text((f(x + 175), f(350)), "\uf063", font=fontawesome_small)
    # Temperatures
    black_draw.text((f(x + 75), f(310)), f"{format_temperature(weather['temp']['max'])}°C", font=temp_font)
    black_draw.text((f(x + 75), f(350)), f"{format_temperature(weather['temp']['min'])}°C", font=temp_font)

draw_weather(205, weather_today)
draw_weather(425, weather_tomorrow)

# Save to file
with open("pics/black.bmp", "wb") as f:
    black_img.save(f, "BMP")
