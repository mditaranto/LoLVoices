import os
import json

# Ruta del directorio principal donde están las carpetas de campeones
directorio_principal = "Voces"

# Función para generar la lista de archivos de audio de un campeón
def generar_lista_audios(campeon):
    lista_audios = []
    ruta_campeon = os.path.join(directorio_principal, campeon)
    for archivo in os.listdir(ruta_campeon):
        if archivo.endswith(".wav"):
            nombre_archivo = os.path.splitext(archivo)[0]  # Nombre del archivo sin extensión
            url_audio = f"https://github.com/mditaranto/LoLVoices/raw/main/{ruta_campeon}/{archivo}"
            lista_audios.append({"nombre": nombre_archivo, "url": url_audio})
    return lista_audios

# Función para obtener la URL de la imagen de un campeón
def obtener_imagen(campeon):
    nombre_imagen = f"{campeon}.jpg"
    ruta_imagen = os.path.join(directorio_principal, campeon, nombre_imagen)
    if os.path.exists(ruta_imagen):
        url_imagen = f"https://github.com/mditaranto/LoLVoices/raw/main/{ruta_imagen}"
        return url_imagen
    else:
        return None

# Función para generar el JSON con la lista de campeones, sus archivos de audio y sus imágenes
def generar_json():
    lista_campeones = []
    for campeon in os.listdir(directorio_principal):
        if os.path.isdir(os.path.join(directorio_principal, campeon)):
            lista_audios = generar_lista_audios(campeon)
            url_imagen = obtener_imagen(campeon)
            campeon_data = {"nombre": campeon, "audios": lista_audios}
            if url_imagen:
                campeon_data["imagen"] = url_imagen
            lista_campeones.append(campeon_data)

    # Guardar la lista de campeones, audios e imágenes en un archivo JSON
    with open("campeones_audios.json", "w") as f:
        json.dump(lista_campeones, f, indent=2)

if __name__ == "__main__":
    generar_json()
