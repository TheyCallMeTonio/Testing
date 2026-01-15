# ===============================
# MINI RPG EN CONSOLA
# ===============================

import random

# -------------------------------
# CLASES
# -------------------------------

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inventario = []

    def esta_vivo(self):
        return self.vida > 0

    def recibir_danio(self, danio):
        danio_real = max(0, danio - self.defensa)
        self.vida -= danio_real
        return danio_real

    def atacar(self, enemigo):
        danio = random.randint(self.ataque - 2, self.ataque + 2)
        return enemigo.recibir_danio(danio)

    def curarse(self):
        if "pocion" in self.inventario:
            self.vida = min(self.vida + 20, self.vida_max)
            self.inventario.remove("pocion")
            print("🧪 Usaste una poción (+20 vida)")
        else:
            print("❌ No tienes pociones")


class Enemigo(Personaje):
    pass


# -------------------------------
# FUNCIONES
# -------------------------------

def crear_enemigo(nivel):
    nombres = ["Goblin", "Orco", "Lobo", "Bandido"]
    nombre = random.choice(nombres)
    vida = random.randint(20, 30) + nivel * 5
    ataque = random.randint(5, 8) + nivel
    defensa = random.randint(1, 3) + nivel // 2
    return Enemigo(nombre, vida, ataque, defensa)


def mostrar_estado(jugador, enemigo):
    print("\n--- ESTADO ---")
    print(f"{jugador.nombre}: ❤️ {jugador.vida}/{jugador.vida_max}")
    print(f"{enemigo.nombre}: 💀 {enemigo.vida}/{enemigo.vida_max}")


def combate(jugador, enemigo):
    print(f"\n⚔️ ¡Un {enemigo.nombre} salvaje aparece!")

    while jugador.esta_vivo() and enemigo.esta_vivo():
        mostrar_estado(jugador, enemigo)

        print("\n1. Atacar")
        print("2. Usar poción")
        print("3. Huir")

        opcion = input("Elige una acción: ")

        if opcion == "1":
            danio = jugador.atacar(enemigo)
            print(f"🗡️ Atacaste e hiciste {danio} de daño")

        elif opcion == "2":
            jugador.curarse()

        elif opcion == "3":
            if random.random() < 0.5:
                print("🏃 Lograste huir")
                return False
            else:
                print("❌ No pudiste escapar")

        else:
            print("❌ Opción inválida")
            continue

        if enemigo.esta_vivo():
            danio = enemigo.atacar(jugador)
            print(f"💥 {enemigo.nombre} te atacó e hizo {danio} de daño")

    return jugador.esta_vivo()


def recompensa(jugador):
    oro = random.randint(5, 15)
    print(f"💰 Ganaste {oro} monedas")

    if random.random() < 0.4:
        jugador.inventario.append("pocion")
        print("🧪 Encontraste una poción")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

print("🧙 Bienvenido al Mini RPG")

nombre = input("Nombre de tu héroe: ")
jugador = Personaje(nombre, vida=50, ataque=10, defensa=3)

nivel = 1

while jugador.esta_vivo():
    print(f"\n🌟 NIVEL {nivel}")
    enemigo = crear_enemigo(nivel)

    victoria = combate(jugador, enemigo)

    if not victoria:
        print("💀 Has sido derrotado...")
        break

    print(f"🏆 Venciste al {enemigo.nombre}")
    recompensa(jugador)

    nivel += 1

    jugador.vida = min(jugador.vida + 5, jugador.vida_max)
    print("❤️ Recuperaste un poco de vida")

print("\n🎮 FIN DEL JUEGO")
print(f"Llegaste hasta el nivel {nivel}")
