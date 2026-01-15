# ===============================
# SISTEMA BANCARIO EN CONSOLA
# ===============================

# Base de datos simple
# clave: número de cuenta
# valor: diccionario con datos
cuentas = {}
contador_cuentas = 1001


# -------------------------------
# FUNCIONES
# -------------------------------

def mostrar_menu():
    print("\n===== BANCO MALDO'S =====")
    print("1. Crear cuenta")
    print("2. Ver cuenta")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Transferir")
    print("6. Mostrar todas las cuentas")
    print("7. Salir")


def crear_cuenta():
    global contador_cuentas

    nombre = input("Nombre del titular: ")
    saldo = float(input("Saldo inicial: "))

    numero = contador_cuentas
    cuentas[numero] = {
        "nombre": nombre,
        "saldo": saldo
    }

    contador_cuentas += 1
    print(f"✅ Cuenta creada | Número: {numero}")


def ver_cuenta():
    numero = int(input("Número de cuenta: "))
    if numero not in cuentas:
        print("❌ Cuenta no encontrada")
        return

    cuenta = cuentas[numero]
    print("\n--- DATOS DE LA CUENTA ---")
    print(f"Titular: {cuenta['nombre']}")
    print(f"Saldo: L.{cuenta['saldo']}")


def depositar():
    numero = int(input("Número de cuenta: "))
    if numero not in cuentas:
        print("❌ Cuenta no encontrada")
        return

    monto = float(input("Monto a depositar: "))
    if monto <= 0:
        print("❌ Monto inválido")
        return

    cuentas[numero]["saldo"] += monto
    print("✅ Depósito realizado")


def retirar():
    numero = int(input("Número de cuenta: "))
    if numero not in cuentas:
        print("❌ Cuenta no encontrada")
        return

    monto = float(input("Monto a retirar: "))
    if monto <= 0:
        print("❌ Monto inválido")
        return

    if cuentas[numero]["saldo"] < monto:
        print("❌ Saldo insuficiente")
        return

    cuentas[numero]["saldo"] -= monto
    print("✅ Retiro exitoso")


def transferir():
    origen = int(input("Cuenta origen: "))
    destino = int(input("Cuenta destino: "))

    if origen not in cuentas or destino not in cuentas:
        print("❌ Cuenta inválida")
        return

    monto = float(input("Monto a transferir: "))
    if monto <= 0:
        print("❌ Monto inválido")
        return

    if cuentas[origen]["saldo"] < monto:
        print("❌ Saldo insuficiente")
        return

    cuentas[origen]["saldo"] -= monto
    cuentas[destino]["saldo"] += monto

    print("🔁 Transferencia realizada")


def mostrar_todas():
    if not cuentas:
        print("❌ No hay cuentas registradas")
        return

    print("\n--- LISTADO DE CUENTAS ---")
    for numero, datos in cuentas.items():
        print(f"Cuenta {numero} | {datos['nombre']} | Saldo: L.{datos['saldo']}")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        ver_cuenta()
    elif opcion == "3":
        depositar()
    elif opcion == "4":
        retirar()
    elif opcion == "5":
        transferir()
    elif opcion == "6":
        mostrar_todas()
    elif opcion == "7":
        print("👋 Gracias por usar el banco")
        break
    else:
        print("❌ Opción inválida")
