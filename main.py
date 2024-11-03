from PIL import Image, ImageDraw
import locale, yaml
from src.drawerlist import drawers

locale.setlocale(locale.LC_ALL, "")

def main():
    black_img = Image.new("1", (640, 384), 0xFF)
    red_img = Image.new("1", (640, 384), 0xFF)

    black_draw = ImageDraw.Draw(black_img)
    red_draw = ImageDraw.Draw(red_img)

    config = yaml.load(open('config.yaml'), yaml.Loader)

    for drawer in drawers:
        drawer().draw(red_draw, black_draw, config)

    # Save to file
    with open("pics/black.bmp", "wb") as f:
        black_img.save(f, "BMP")
    with open("pics/red.bmp", "wb") as f:
        red_img.save(f, "BMP")

if __name__ == "__main__":
    main()