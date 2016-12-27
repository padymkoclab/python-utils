"""Utils for working with files."""

import random

from PIL import Image, ImageDraw, ImageFont


def generateImage(text=None, path='.'):
    """Generate random image."""

    width = 500
    height = 255
    img = Image.new('RGB', (width, height), '#fff')

    pixels = img.load()
    k = random.randint(0, 200)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, k)

    if text:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 20)
        draw.text((width / 2.75, height / 2), text, (255, 255, 255), font)

    img.show()
