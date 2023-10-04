import cv2
import numpy as np

# Carga la imagen RGB
imagen_rgb = cv2.imread('b.png')

# Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2GRAY)

# Crea una máscara binaria donde los píxeles 150 se establecen en 1 y los píxeles 255 se establecen en 0
imagen_binaria = np.where(imagen_gris == 150, 1, 0).astype(np.uint8)

# Calcula los momentos de la imagen binaria
momentos = cv2.moments(imagen_binaria)

# Calcula el momento de orden p=2 y q=3 (M23) manualmente
x_bar = momentos['m10'] / momentos['m00']  # Centroide en dirección x
y_bar = momentos['m01'] / momentos['m00']  # Centroide en dirección y

M23 = 0.0
filas, columnas = imagen_binaria.shape

for x in range(filas):
    for y in range(columnas):
        if imagen_binaria[x, y] == 1:  # Asegurarse de que el píxel sea 1 (valor que se estableció para 150)
            M23 += ((x - x_bar) ** 2) * ((y - y_bar) ** 3)

print("M23 (Momento de segundo orden en dirección x y tercer orden en dirección y):", M23)
