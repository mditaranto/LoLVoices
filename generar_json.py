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
            url_audio = f"https://github.com/tu_usuario/tu_repositorio/raw/main/{ruta_campeon}/{archivo}"
            lista_audios.append({"nombre": nombre_archivo, "url": url_audio})
    return lista_audios

# Función para generar el JSON con la lista de campeones y sus archivos de audio
def generar_json():
    lista_campeones = []
    for campeon in os.listdir(directorio_principal):
        if os.path.isdir(os.path.join(directorio_principal, campeon)):
            lista_audios = generar_lista_audios(campeon)
            lista_campeones.append({"nombre": campeon, "audios": lista_audios})

    # Guardar la lista de campeones y audios en un archivo JSON
    with open("campeones_audios.json", "w") as f:
        json.dump(lista_campeones, f, indent=2)

if __name__ == "__main__":
    generar_json()
