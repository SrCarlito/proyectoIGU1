

from main import getHist
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np




img = Image.open('flores.png')

r, g, b = img.split()
l = img.convert('L')

fig = plt.figure(figsize=(6, 7))


plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Gap_subplots

ax1 = plt.subplot2grid((3, 2), (0, 0))
ax2 = plt.subplot2grid((3, 2), (0, 1))
ax3 = plt.subplot2grid((3, 2), (1, 0))
ax4 = plt.subplot2grid((3, 2), (1, 1))
ax5 = plt.subplot2grid((3, 2), (2, 0), colspan=2)

ax1.plot(range(256), getHist(r), color='red')
ax1.set_title('Histograma canal rojo')

ax2.plot(range(256), getHist(g), color='green')
ax2.set_title('Histograma canal verde')

ax3.plot(range(256), getHist(b), color='blue')
ax3.set_title('Histograma canal azul')


ax4.imshow(l, cmap='gray')
ax4.set_title('Escala de grises')
ax4.axis('off')

ax5.imshow(img)
ax5.set_title('Imagen original')
ax5.axis('off')

plt.show()
