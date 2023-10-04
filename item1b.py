from sources import *
from main import Image2PixL


# Función de Momento
def Momento(imgRoute, p, q):
    BACKGROUND = 255
    imgGs = Image.open(imgRoute).convert("L")
    img = imgGs.load()
    w, h = imgGs.size
    momento = 0
    for u in range(w):
        for v in range(h):
            if (img[u, v] != BACKGROUND):
                momento += (u**p) * (v**q) 
    return momento


# Momento Central
def MomentoCentral(imgRoute, p, q):
    BACKGROUND = 255
    imgGs = Image.open(imgRoute).convert("L")
    img = imgGs.load()
    w, h = imgGs.size
    x_ = Momento(imgRoute, 1, 0) / Momento(imgRoute, 0, 0)
    y_ = Momento(imgRoute, 0, 1) / Momento(imgRoute, 0, 0)
    momento = 0
    for u in range(w):
        for v in range(h):
            if (img[u, v] != BACKGROUND):
                momento += ((u - x_)**p) * ((v- y_)**q)
    return momento


# Momento Central Normalizado
def MomentoCentralNormalizado(imgRoute, p, q):
    m00 = Momento(imgRoute, 0, 0)
    norm = m00 ** ((p+q)/2 + 1)
    return MomentoCentral(imgRoute, p, q) / norm


def printMoments(image):
    print("Momento: ", str(Momento(image, 2, 3)))
    print("Momento Central: ", str(MomentoCentral(image, 2, 3)))
    print("Momento Central Normalizado: ",  str(
        MomentoCentralNormalizado(image, 2, 3)))


printMoments('b.png')
