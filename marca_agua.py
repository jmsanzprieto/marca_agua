import os

from PIL import Image, ImageDraw, ImageFont

def agregar_marca_de_agua(imagen_path, marca_de_agua_texto, salida_path, transparencia=0, tamano_fuente=50):
    # Abrir la imagen
    imagen = Image.open(imagen_path).convert("RGBA")

    # Crear un objeto ImageDraw
    draw = ImageDraw.Draw(imagen)

    # Cargar una fuente
    fuente = ImageFont.truetype("arial.ttf", tamano_fuente)

    # Configurar el color y la transparencia de la marca de agua
    color_marca_de_agua = (0, 0, 0, transparencia)

    # Calcular la posición para la esquina inferior izquierda
    ancho, alto = imagen.size
    margen = 10
    posicion = (margen, alto - tamano_fuente - margen)

    # Agregar la marca de agua a la imagen
    draw.text(posicion, marca_de_agua_texto, font=fuente, fill=color_marca_de_agua)

    # Guardar la imagen resultante
    imagen.save(salida_path, "PNG")

def procesar_carpeta(input_folder, output_folder, marca_de_agua_texto):
    # Verificar y crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Listar archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):  # Filtrar solo imágenes
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Aplicar la marca de agua a cada imagen
            agregar_marca_de_agua(input_path, marca_de_agua_texto, output_path)

if __name__ == "__main__":
    # Rutas de la carpeta de entrada y salida
    carpeta_fotos = r"ruta/carpeta/fotos"
    carpeta_salida = r"ruta/carpeta/fotos/marcadas"

    # Marca de agua
    marca_de_agua_texto = "TEXTO_DE_LA_MARCA_DE_AGUA"

    # Procesar la carpeta
    procesar_carpeta(carpeta_fotos, carpeta_salida, marca_de_agua_texto)
