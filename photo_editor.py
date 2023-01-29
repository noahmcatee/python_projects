from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os

path = 'C:\\Users\\noahm\\Pictures\\pyImages'
pathOut = "C:\\Users\\noahm\\Pictures\\modPyImages"

text_font = (ImageFont.FreeTypeFont)

for filename in os.listdir(path):
    img = Image.open(f"{path}\{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    text_edit = ImageDraw.Draw(edit)
    text_edit.text((100, 100), "Bob Burger", ("black"))

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}\{clean_name}_edited.jpg')