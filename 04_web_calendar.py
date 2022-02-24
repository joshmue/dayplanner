from PIL import Image, ImageDraw, ImageFont
import datetime
import arrow
import calendar
import locale
import icalendar
import recurring_ical_events
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import yaml
import pytz

locale.setlocale(locale.LC_ALL, "")

black_img = Image.open("pics/black.bmp")
black_img.load()
red_img = Image.open("pics/red.bmp")
red_img.load()

black_draw = ImageDraw.Draw(black_img)
red_draw = ImageDraw.Draw(red_img)

today = datetime.date.today()

factor = 1.0

def f(i):
    return int(factor * i)

###
# LAYOUT
###
headlinefont = ImageFont.truetype("/usr/share/fonts/google-roboto/Roboto-Bold.ttf", f(28))
red_draw.text((f(235), f(16)), "Today".upper(), font=headlinefont)
red_draw.text((f(455), f(16)), "Tomorrow".upper(), font=headlinefont)
check_o = "\uf096"
check = "\uf046"
del headlinefont

itemfont = ImageFont.truetype("/usr/share/fonts/google-roboto/Roboto-Bold.ttf", f(24))
timefont = ImageFont.truetype("/usr/share/fonts/google-roboto/Roboto-Thin.ttf", f(16))
fontawesome = ImageFont.truetype("/opt/fontawesome-free-5.15.2-desktop/otfs/Font Awesome 5 Free-Solid-900.otf", f(45))
black_draw.line((f(200), 0, f(200), black_img.size[1]))
black_draw.line((f(200), f(48), black_img.size[0], f(48)))
black_draw.line((f(200), f(305), black_img.size[0], f(305)))
black_draw.line((f(420), 0, f(420), black_img.size[1]))

def trim_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

###
# EVENTS
###

local = pytz.timezone("Europe/Berlin")

class SortableEvent:
    def __init__(self, ics_event):
        self.ics_event = ics_event
    def __lt__(self, other):
        if "DTSTART" in self.ics_event and "DTSTART" in other.ics_event:
            return arrow.get(self.ics_event.decoded("DTSTART")) < arrow.get(other.ics_event.decoded("DTSTART"))
        else:
            return True


def draw_events(x, cal, delta):
    t1 = arrow.now().shift(days=delta).replace(hour=0, minute=0)
    t2 = arrow.now().shift(days=delta).replace(hour=23, minute=59)
    events = []
    for comp in cal.walk():
        events.append(SortableEvent(comp))

    events = sorted(events)
    i = 0
    for comp in events:
        if not isinstance(comp.ics_event, icalendar.cal.Event):
            continue
        icon = comp.ics_event['ICON']
        start = comp.ics_event.decoded("DTSTART") if "DTSTART" in comp.ics_event else None
        end = comp.ics_event.decoded("DTEND") if "DTEND" in comp.ics_event else None
        overlapping = False
        if arrow.get(start)<t1 and arrow.get(end)>t2:
            overlapping = True
        if not (arrow.get(start).is_between(t1, t2) or overlapping):
            continue
        timestr = ""
        if overlapping:
            timestr = "all day"
        elif start and end:
            timestr = "%s - %s" % (start.astimezone(local).strftime("%H:%M"), end.astimezone(local).strftime("%H:%M"))
        elif start:
            timestr = start.astimezone(local).strftime("%H:%M")
        else:
            timestr = "9 to 5"
        iconstartx = x + ((f(50) - fontawesome.getsize(icon)[0]) // 2)
        black_draw.text((iconstartx, f(60 + 64 * i)), icon, font=fontawesome)
        description = ''
        for char in trim_prefix(str(comp.ics_event["SUMMARY"]), comp.ics_event["PREFIX"]):
            if itemfont.getsize(description + char + "…")[0] <= f(220-65):
                description += char
            else:
                description = description + "…"
                break
        black_draw.text((x + f(55), f(56 + 64 * i)), description, font=itemfont)
        black_draw.text((x + f(55), f(84 + 64 * i)), timestr, font=timefont)
        i+=1

all_ics = []
ncal = icalendar.Calendar()

session = requests.Session()
session.mount('https://', HTTPAdapter(max_retries=Retry(
    total=5, backoff_factor=0.2, raise_on_status=True
)))

for calendar in yaml.load(open('config.yaml'), yaml.Loader)['calendars']:
    resp = session.get(calendar['url'])
    resp.raise_for_status()
    raw_cal = icalendar.Calendar.from_ical(resp.text)
    all_ics.append(resp.text)
    t1 = arrow.get(datetime.datetime.now()).replace(hour=0, minute=0).naive
    t2 = arrow.get(datetime.datetime.now()).shift(days=1).replace(hour=23, minute=59).naive
    for raw_event in recurring_ical_events.of(raw_cal).between(t1, t2):
        raw_event['ICON'] = calendar['icon'].decode()
        raw_event['PREFIX'] = calendar['trimPrefix']
        ncal.add_component(raw_event)
draw_events(f(210), ncal, 0)
draw_events(f(430), ncal, 1)

# Save to file
with open("pics/black.bmp", "wb") as f:
    black_img.save(f, "BMP")
with open("pics/red.bmp", "wb") as f:
    red_img.save(f, "BMP")
