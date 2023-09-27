from PIL import Image, ImageOps
import matplotlib.pyplot as plt

img = Image.open('flores.png')

r,g,b = img.split()
l = img.convert('L')

fig, ax = plt.subplots(2,2)

ax[0][0].imshow(r,'Reds')
ax[0][1].imshow(g,'Greens')
ax[1][0].imshow(b,cmap='Blues')
ax[1][1].imshow(l,cmap='gray')

plt.show()

#Item 7

img2 = Image.open('sea.jpg')

colored = ImageOps.colorize(img2,
                            black='blue',
                            white='white') 

colored.show()
