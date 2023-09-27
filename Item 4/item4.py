from PIL import Image, ImageFilter

# Cargar las imagenes
figura_00 = Image.open("fig_00.jpg")
figura_01 = Image.open("fig_01.jpg")
figura_02 = Image.open("fig_02.jpg")
figura_03 = Image.open("fig_03.jpg")
figura_04 = Image.open("fig_04.jpg")

plantilla_01 = Image.open("pla_01.jpg")
plantilla_02 = Image.open("pla_02.jpg")
plantilla_03 = Image.open("pla_03.jpg")
plantilla_04 = Image.open("pla_04.jpg")

#---------------------------------------------------------------
# Redimensionar size de las figuras
figura_00 = figura_00.resize(figura_01.size)
plantilla_01 = plantilla_01.resize(figura_01.size)

figura_00 = figura_00.resize(figura_02.size)
plantilla_02 = plantilla_02.resize(figura_02.size)

figura_00 = figura_00.resize(figura_03.size)
plantilla_03 = plantilla_03.resize(figura_03.size)

figura_00 = figura_00.resize(figura_04.size)
plantilla_04 = plantilla_04.resize(figura_04.size)

#--------------------------------------------------------------
# Crear una mascara a partir de la plantilla
plantilla_01 = plantilla_01.convert("L")
plantilla_01 = plantilla_01.point(lambda x: x > 128 and 255)

plantilla_02 = plantilla_02.convert("L")
plantilla_02 = plantilla_02.point(lambda x: x > 128 and 255)

plantilla_03 = plantilla_03.convert("L")
plantilla_03 = plantilla_03.point(lambda x: x > 128 and 255)

plantilla_04 = plantilla_04.convert("L")
plantilla_04 = plantilla_04.point(lambda x: x > 128 and 255)

#--------------------------------------------------------------
# Aplicar filtro difuminado
plantilla_01 = plantilla_01.filter(ImageFilter.GaussianBlur(3))
plantilla_02 = plantilla_02.filter(ImageFilter.GaussianBlur(3))
plantilla_03 = plantilla_03.filter(ImageFilter.GaussianBlur(3))
plantilla_04 = plantilla_04.filter(ImageFilter.GaussianBlur(3))

#--------------------------------------------------------------
# Combina las imagenes de cada figura con su respectiva plantilla
resultado1 = Image.new("RGB", figura_01.size)
resultado1.paste(figura_01, (0, 0))
resultado1.paste(figura_00, (0, 0), plantilla_01)

resultado2 = Image.new("RGB", figura_02.size)
resultado2.paste(figura_02, (0, 0))
resultado2.paste(figura_00, (0, 0), plantilla_02)

resultado3 = Image.new("RGB", figura_03.size)
resultado3.paste(figura_03, (0, 0))
resultado3.paste(figura_00, (0, 0), plantilla_03)

resultado4 = Image.new("RGB", figura_04.size)
resultado4.paste(figura_04, (0, 0))
resultado4.paste(figura_00, (0, 0), plantilla_04)

#------------------------------------------------------
# Guardar la imagen resultante en formato JPEG
resultado1.save("resultado1.jpg", "JPEG")
resultado2.save("resultado2.jpg", "JPEG")
resultado3.save("resultado3.jpg", "JPEG")
resultado4.save("resultado4.jpg", "JPEG")

# Muestra resultados
resultado1.show()
resultado2.show()
resultado3.show()
resultado4.show()

