from sources import *
# Item 7
img2 = Image.open('sea.jpg')
print("colorizando...")
colored = ImageOps.colorize(img2,
                            black='blue',
                            white='white')
print("colorizado con exito!")
colored.show()
