# ===============================
# SISTEMA DE INVENTARIO Y VENTAS
# ===============================

# Estructura del inventario
# clave -> nombre del producto
# valor -> diccionario con precio y stock
inventario = {
    "manzana": {"precio": 5.0, "stock": 20},
    "banana ": {"precio": 3.0, "stock": 30},
    "naranja": {"precio": 4.0, "stock": 15}
}

ventas_totales = 0.0


# -------------------------------
# FUNCIONES
# -------------------------------

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Vender producto")
    print("4. Eliminar producto")
    print("5. Ver total de ventas")
    print("6. Salir")


def mostrar_inventario():
    print("\n--- INVENTARIO ---")
    if not inventario:
        print("Inventario vacío")
        return

    for producto, datos in inventario.items():
        print(f"{producto.capitalize()} | Precio: L.{datos['precio']} | Stock: {datos['stock']}")


def agregar_producto():
    nombre = input("Nombre del producto: ").lower()

    if nombre in inventario:
        print("❌ El producto ya existe")
        return

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
    except ValueError:
        print("❌ Datos inválidos")
        return

    inventario[nombre] = {
        "precio": precio,
        "stock": stock
    }

    print("✅ Producto agregado correctamente")


def vender_producto():
    global ventas_totales

    nombre = input("Producto a vender: ").lower()

    if nombre not in inventario:
        print("❌ Producto no encontrado")
        return

    try:
        cantidad = int(input("Cantidad a vender: "))
    except ValueError:
        print("❌ Cantidad inválida")
        return

    if cantidad <= 0:
        print("❌ La cantidad debe ser mayor que cero")
        return

    if inventario[nombre]["stock"] < cantidad:
        print("❌ Stock insuficiente")
        return

    total = inventario[nombre]["precio"] * cantidad
    inventario[nombre]["stock"] -= cantidad
    ventas_totales += total

    print(f"✅ Venta realizada | Total: L.{total}")

    if inventario[nombre]["stock"] == 0:
        print(f"⚠️ ALERTA: {nombre} se quedó sin stock")


def eliminar_producto():
    nombre = input("Producto a eliminar: ").lower()

    if nombre not in inventario:
        print("❌ Producto no existe")
        return

    confirmacion = input("¿Seguro? (s/n): ").lower()

    if confirmacion == "s":
        del inventario[nombre]
        print("✅ Producto eliminado")
    else:
        print("❌ Operación cancelada")


def ver_ventas():
    print(f"\n💰 Ventas totales: L.{ventas_totales}")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        vender_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        ver_ventas()
    elif opcion == "6":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida")