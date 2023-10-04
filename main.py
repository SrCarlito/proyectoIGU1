from sources import *



def toBin(img, bg):
    i = img.convert("L")
    w, h = i.size
    # Devuelve una lista de vectores que representan los valores de cada píxel
    data = i.getdata()
    img = array(data, float)
    # Se transforma la lista en una matriz con 3 canales
    img = img.reshape((h, w))
    for i in img:
        if (i!= bg):
            i = 1
        else:
            i = 0

    return img
    
def Image2PixL(img, mode='RGB'):
    i = img.convert(mode)
    w, h = i.size
    # Devuelve una lista de vectores que representan los valores de cada píxel
    data = i.getdata()
    img = array(data, float)
    # Se transforma la lista en una matriz con 3 canales
    img = img.reshape((h, w))
    return img


def getHist(image):
    hist = np.zeros(256)
    data = Image2PixL(image, "L")
    for x in range(len(data)):
        for y in range(len(data[x])):
            hist[int(data[x][y])] += 1
    return hist






# def PintaCentroide(imgRoute):
#     center_x, center_y = Centroide(imgRoute)
#     imagen = Image.open(imgRoute)
#     draw = ImageDraw.Draw(imagen)

#     # Longitud de las líneas de la X
#     line_length = 3

#     # Dibujar la primera línea de la X
#     draw.line([(center_x - line_length, center_y - line_length),
#                (center_x + line_length, center_y + line_length)],
#               fill=(0, 0, 0), width=1)

#     # Dibujar la segunda línea de la X
#     draw.line([(center_x + line_length, center_y - line_length),
#                (center_x - line_length, center_y + line_length)],
#               fill=(0, 0, 0), width=1)
#     imagen.show()





