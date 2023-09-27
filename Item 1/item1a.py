from PIL import Image, ImageDraw

def area_centroide(imagen):
    # Carga imagen con PIL
    img = Image.open(imagen)

    # Convertir la imagen a gris
    img_gris = img.convert("L")

    # Objeto para dibujar
    draw = ImageDraw.Draw(img)

    # Contornos
    contorno = []
    for x in range(img.width):
        for y in range(img.height):
            if img_gris.getpixel((x, y)) < 255:
                contorno.append((x, y))

    # Calcular area
    area = len(contorno)

    # Calcular centroide
    cx = sum(x for x, _ in contorno) // area
    cy = sum(y for _, y in contorno) // area

    # Dibuja una cruz en el centroide
    draw.line([(cx - 10, cy - 10), (cx + 10, cy + 10)], fill="black", width=3)
    draw.line([(cx - 10, cy + 10), (cx + 10, cy - 10)], fill="black", width=3)

    # Guarda imagen con la cruz
    img.save("img_centroide.png")
    #img.show()

    # Calcular centroide mediante momentos
    momento_m00 = area
    momento_m10 = sum(x for x, _ in contorno)
    momento_m01 = sum(y for _, y in contorno)

    cx_momento = momento_m10 / momento_m00
    cy_momento = momento_m01 / momento_m00

    return area, (cx, cy), (cx_momento, cy_momento)


image = "a.png"

area, centroide, centroide_moments = area_centroide(image)
print("Area de la figura: ", area, "pixeles cuadrados")
print("Centroide: ", centroide)
print("Centroide mediante momentos: ", centroide_moments)
