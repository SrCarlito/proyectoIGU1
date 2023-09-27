from PIL import Image,ImageDraw
from numpy import array

def Image2PixL(img):
    i = img.convert('L')
    w,h = i.size
    data =i.getdata()           #Devuelve una lista de vectores que representan los valores de cada píxel
    img = array(data,float)     
    img = img.reshape((h,w))  #Se transforma la lista en una matriz con 3 canales
    return img



# Función de Momento
def Momento(imgRoute,p,q):
    imageArray = Image2PixL(Image.open(imgRoute))

    momento = 0
    for u in range(len(imageArray)):
        for  v in range(len(imageArray[u])):
            if(imageArray[u][v] != 255):
                momento += (u**p) * (v**q) * (imageArray[u][v]) 

    return momento


# Área mediante momento
def Area(imgRoute):
    return Momento(imgRoute,0,0)


# Centroide mediante momento
def Centroide(imgRoute):
    print(Momento(imgRoute,1,0))
    print(Momento(imgRoute,0,0))
    x_ = Momento(imgRoute,1,0) / Momento(imgRoute,0,0)
    y_ = Momento(imgRoute,0,1) / Momento(imgRoute,0,0)

    return (x_,y_)

def PintaCentroide(imgRoute):
    center_x,center_y = Centroide(imgRoute)
    imagen = Image.open(imgRoute)
    draw = ImageDraw.Draw(imagen)
    
    # Longitud de las líneas de la X
    line_length = 3

    # Dibujar la primera línea de la X
    draw.line([(center_x - line_length, center_y - line_length),
        (center_x + line_length, center_y + line_length)], 
        fill=(0, 0, 0), width=1)

    # Dibujar la segunda línea de la X
    draw.line([(center_x + line_length, center_y - line_length), 
               (center_x - line_length, center_y + line_length)], 
               fill=(0, 0, 0), width=1)
    imagen.show()



# Momento Central
def MomentoCentral(imgRoute,p,q):

    imageArray = Image2PixL(Image.open(imgRoute))
    x_,y_ = Centroide(imgRoute)

    momento = 0
    for u in range(len(imageArray)):
        for  v in range(len(imageArray[u])):
            if(imageArray[u][v] != 255):
                momento += ((u - x_)**p) * ((v - y_)**q) * (imageArray[u][v]) 
    return momento


# Momento Central Normalizado
def MomentoCentralNormalizado(imgRoute,p,q):
    return  MomentoCentral(imgRoute,p,q)  *  (
            ( 1/ MomentoCentral(imgRoute,0,0) )**  ((p+q+2)/2))

# Momento De Hu 1
def MomentoDeHu_1(imgRoute):
    return (MomentoCentralNormalizado(imgRoute,2,0) 
        +   MomentoCentralNormalizado(imgRoute,0,2))


# Momento De Hu 2
def MomentoDeHu_2(imgRoute):
    return ((MomentoCentralNormalizado(imgRoute,2,0) 
            + MomentoCentralNormalizado(imgRoute,0,2))**2
         + 4*(MomentoCentralNormalizado(imgRoute,1,1) **2))


# Momento De Hu 3
def MomentoDeHu_3(imgRoute):
    return ((MomentoCentralNormalizado(imgRoute,3,0) - 
             3*MomentoCentralNormalizado(imgRoute,1,2))**2
             +
            (3*MomentoCentralNormalizado(imgRoute,2,1) - 
               MomentoCentralNormalizado(imgRoute,0,3))**2)
 
PintaCentroide('a.png')