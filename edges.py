from PIL import Image, ImageFilter

before =Image.open("bride.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")