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


img = Image.open('fig_00.jpg')

r, g, b = img.split()
l = img.convert('L')


fig, ax = plt.subplots(2,1,figsize=(8, 5))
# Gap_subplots

ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title('Imagen')


ax[1].plot(range(256), getHist(r), color='red')
ax[1].plot(range(256), getHist(g), color='green')
ax[1].plot(range(256), getHist(b), color='blue')

ax[1].set_ylabel('Histograma RGB')
ax[1].set_xlabel('Valores Posibles')


plt.show()
