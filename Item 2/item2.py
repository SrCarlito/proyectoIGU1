from PIL import Image
import matplotlib.pyplot as plt


def calcular_histo(imagen):
    # Abre la imagen
    img = Image.open(imagen)

    # Separa los canales de color
    r, g, b = img.split()

    # Calcula los histogramas para cada canal
    r_histogram = r.histogram()
    g_histogram = g.histogram()
    b_histogram = b.histogram()

    # Rango de valores para el eje x
    valores_x = list(range(256))

    # Grafica los histogramas a cada canal de color
    plt.figure(figsize=(8, 6))
    plt.title('Histograma')
    plt.xlabel('Valor de Pixel')
    plt.ylabel('Frecuencia')
    plt.bar(valores_x, r_histogram, color='red', alpha=0.7, label='Rojo')
    plt.bar(valores_x, g_histogram, color='green',
            alpha=0.7, label='Verde', bottom=r_histogram)
    plt.bar(valores_x, b_histogram, color='blue', alpha=0.7, label='Azul',
            bottom=[i+j for i, j in zip(r_histogram, g_histogram)])
    plt.legend()
    plt.show()


calcular_histo('mono.png')
