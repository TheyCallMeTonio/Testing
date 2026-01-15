# ===============================
# SISTEMA DE GESTIÓN DE ESTUDIANTES
# ===============================

# Diccionario principal
# clave: nombre del estudiante
# valor: diccionario con info
estudiantes = {}

# -------------------------------
# FUNCIONES
# -------------------------------

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Registrar calificación")
    print("3. Mostrar estudiante")
    print("4. Mostrar todos")
    print("5. Mostrar promedio")
    print("6. Salir")


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre in estudiantes:
        print("❌ Estudiante ya existe")
        return
    estudiantes[nombre] = {
        "edad": int(input("Edad: ")),
        "calificaciones": []
    }
    print("✅ Estudiante agregado")


def registrar_calificacion():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre not in estudiantes:
        print("❌ Estudiante no encontrado")
        return
    try:
        nota = float(input("Calificación (0-100): "))
        if nota < 0 or nota > 100:
            raise ValueError
        estudiantes[nombre]["calificaciones"].append(nota)
        print("✅ Calificación registrada")
    except ValueError:
        print("❌ Nota inválida")


def mostrar_estudiante():
    nombre = input("Nombre del estudiante: ").strip()
    if nombre not in estudiantes:
        print("❌ Estudiante no encontrado")
        return
    info = estudiantes[nombre]
    print(f"\n--- {nombre} ---")
    print(f"Edad: {info['edad']}")
    print(f"Calificaciones: {info['calificaciones']}")
    if info['calificaciones']:
        promedio = sum(info['calificaciones']) / len(info['calificaciones'])
        print(f"Promedio: {promedio:.2f}")
    else:
        print("Promedio: N/A")


def mostrar_todos():
    if not estudiantes:
        print("❌ No hay estudiantes registrados")
        return
    for nombre, info in estudiantes.items():
        print(f"\n--- {nombre} ---")
        print(f"Edad: {info['edad']}")
        print(f"Calificaciones: {info['calificaciones']}")


def mostrar_promedio_general():
    total = 0
    cuenta = 0
    for info in estudiantes.values():
        if info["calificaciones"]:
            total += sum(info["calificaciones"])
            cuenta += len(info["calificaciones"])
    if cuenta == 0:
        print("❌ No hay calificaciones registradas")
        return
    promedio_general = total / cuenta
    print(f"\n📊 Promedio general de todos los estudiantes: {promedio_general:.2f}")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        registrar_calificacion()
    elif opcion == "3":
        mostrar_estudiante()
    elif opcion == "4":
        mostrar_todos()
    elif opcion == "5":
        mostrar_promedio_general()
    elif opcion == "6":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida")
