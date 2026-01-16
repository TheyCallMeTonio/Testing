# =====================================
# ORGANIZADOR DE ARCHIVOS AUTOMÁTICO
# =====================================

import os
import shutil
from collections import defaultdict

# -------------------------------
# CONFIGURACIÓN
# -------------------------------

RUTA = "./archivos"  # carpeta a organizar

EXTENSIONES = {
    "Imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
    "Comprimidos": [".zip", ".rar"],
    "Codigo": [".py", ".js", ".html", ".css"]
}

# -------------------------------
# FUNCIONES
# -------------------------------

def crear_carpetas():
    for carpeta in EXTENSIONES.keys():
        ruta_carpeta = os.path.join(RUTA, carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

    os.makedirs(os.path.join(RUTA, "Otros"), exist_ok=True)


def obtener_categoria(extension):
    for categoria, extensiones in EXTENSIONES.items():
        if extension in extensiones:
            return categoria
    return "Otros"


def organizar_archivos():
    movimientos = defaultdict(int)

    for archivo in os.listdir(RUTA):
        ruta_archivo = os.path.join(RUTA, archivo)

        if os.path.isfile(ruta_archivo):
            _, extension = os.path.splitext(archivo)
            categoria = obtener_categoria(extension.lower())

            destino = os.path.join(RUTA, categoria, archivo)
            shutil.move(ruta_archivo, destino)
            movimientos[categoria] += 1

    return movimientos


def mostrar_reporte(movimientos):
    print("\n📊 REPORTE DE ORGANIZACIÓN")
    total = 0
    for categoria, cantidad in movimientos.items():
        print(f"{categoria}: {cantidad} archivos")
        total += cantidad
    print(f"TOTAL: {total} archivos organizados")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

print("📁 ORGANIZADOR DE ARCHIVOS")
print(f"Ruta objetivo: {RUTA}")

if not os.path.exists(RUTA):
    print("❌ La carpeta no existe")
else:
    crear_carpetas()
    movimientos = organizar_archivos()
    mostrar_reporte(movimientos)
    print("\n✅ Organización completada")
