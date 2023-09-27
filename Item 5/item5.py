from PIL import Image
import numpy as np

# Abre la imagen
imagen_original = Image.open("fig_05.jpg")

# Separa los colores RGB
canal_r, canal_g, canal_b = imagen_original.split()

# Crea imagenes RGB separadas para cada canal
imagen_r = Image.merge("RGB", (canal_r, Image.new("L", canal_r.size, 0), Image.new("L", canal_r.size, 0)))
imagen_g = Image.merge("RGB", (Image.new("L", canal_g.size, 0), canal_g, Image.new("L", canal_g.size, 0)))
imagen_b = Image.merge("RGB", (Image.new("L", canal_b.size, 0), Image.new("L", canal_b.size, 0), canal_b))

# Guarda las imagenes separadas
imagen_r.save("canal_r.jpg")
imagen_g.save("canal_g.jpg")
imagen_b.save("canal_b.jpg")

# Abre las imagenes separadas
imagen_r = Image.open("canal_r.jpg")
imagen_g = Image.open("canal_g.jpg")
imagen_b = Image.open("canal_b.jpg")

# Convierte las imagenes en matrices de NumPy
matriz_r = np.array(imagen_r)
matriz_g = np.array(imagen_g)
matriz_b = np.array(imagen_b)

# Calcula el area ocupada por los pixeles de cada canal
area_r = np.sum(matriz_r > 0)
area_g = np.sum(matriz_g > 0)
area_b = np.sum(matriz_b > 0)

print("Area ocupada por el plano R es de :", area_r, "pixeles")
print("Area ocupada por el plano G es de:", area_g, "pixeles")
print("Area ocupada por el plano B es de:", area_b, "pixeles")

# Cierra las imagenes
imagen_r.close()
imagen_g.close()
imagen_b.close()

# Cierra la imagen original
imagen_original.close()
