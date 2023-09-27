from main import Image2PixL
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np


def getHist(image):
    hist = np.zeros(256)

    data = Image2PixL(image)
    for x in range(len(data)):
        for y in range(len(data[x])):
            hist[int(data[x][y])] += 1

    return hist


img = Image.open('flores.png')

r, g, b = img.split()
l = img.convert('L')


fig, ax = plt.subplots(2, 2, figsize=(8, 5)) 
plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Gap_subplots

ax[0][0].plot(range(256), getHist(r), color='red')
ax[0][0].set_title('Histograma canal rojo')

ax[0][1].plot(range(256), getHist(g), color='green')
ax[0][1].set_title('Histograma canal verde')

ax[1][0].plot(range(256), getHist(b), color='blue')
ax[1][0].set_title('Histograma canal azul')


ax[1][1].imshow(l, cmap='gray')
ax[1][1].set_title('Escala de grises')
ax[1][1].axis('off')


#plt.show()


# Item 7
img2 = Image.open('sea.jpg')

colored = ImageOps.colorize(img2,
                            black='blue',
                            white='white')

colored.show()
