from main import getHist
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img = Image.open('fig_00.jpg')

r, g, b = img.split()
l = img.convert('L')

histR = getHist(r)
histG = getHist(g)
histB = getHist(b)

fig, ax = plt.subplots(1, 3, figsize=(10, 4))

plt.subplots_adjust(wspace=0.5, hspace=1)

ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title('Imagen')


ax[1].plot(range(256), getHist(r), color='red')
ax[1].plot(range(256), getHist(g), color='green')
ax[1].plot(range(256), getHist(b), color='blue')
ax[2].plot(range(256), getHist(l), color='black')
ax[2].set_ylim(0, 4000)

ax[1].set_ylabel('Histograma RGB ')
ax[1].set_xlabel('Valores Posibles')

ax[2].set_ylabel('Histograma Intensidad ')
ax[2].set_xlabel('Valores Posibles')

print("La tonalidad que más se repite en R es: ", histR.argmax())
print("La tonalidad que más se repite en G es: ", histG.argmax())
print("La tonalidad que más se repite en B es: ", histB.argmax())

plt.show()
