import os

# Directorio donde se encuentran los archivos de audio
directorio = "Voces/Braum"

# Lista todos los archivos en el directorio
archivos = os.listdir(directorio)

# Calcula el tamaño de cada archivo y crea una lista de tuplas (nombre_archivo, tamaño_archivo)
archivos_con_tamano = [(archivo, os.path.getsize(os.path.join(directorio, archivo))) for archivo in archivos]

# Ordena la lista de archivos por tamaño en orden descendente
archivos_ordenados_por_tamano = sorted(archivos_con_tamano, key=lambda x: x[1], reverse=True)

# Conserva solo los 70 archivos con los tamaños más grandes
archivos_a_conservar = archivos_ordenados_por_tamano[:100]

# Elimina los archivos que no están en la lista de los 70 más grandes
for archivo, _ in archivos_con_tamano:
    if (archivo, _) not in archivos_a_conservar:
        ruta_archivo = os.path.join(directorio, archivo)
        os.remove(ruta_archivo)
        print(f"Se eliminó el archivo {archivo}.")