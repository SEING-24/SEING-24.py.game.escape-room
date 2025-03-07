
import time
"""
Este script es un juego de Escape Room en el que el jugador debe resolver acertijos y encontrar objetos para escapar de una habitación misteriosa dentro de un límite de tiempo.

Variables globales:
- inventario: Lista que almacena los objetos recogidos por el jugador.
- tiempo_limite: Tiempo límite en segundos para completar el juego.
- inicio_tiempo: Marca de tiempo cuando el temporizador comienza.

Funciones:
- mostrar_introduccion(): Muestra la introducción del juego y las instrucciones iniciales.
- iniciar_temporizador(): Inicia el temporizador del juego.
- tiempo_restante(): Calcula y devuelve el tiempo restante para completar el juego.
- verificar_tiempo(): Verifica si el tiempo se ha agotado y muestra un mensaje si es así.
- mostrar_inventario(): Muestra el contenido del inventario del jugador.
- sala_principal(): Lógica de la Sala Principal donde el jugador puede examinar una mesa, abrir una puerta, revisar el inventario o pedir una pista.
- sala_acertijo(): Lógica de la Sala del Acertijo donde el jugador debe ingresar un código numérico para avanzar.
- sala_final(): Lógica de la Sala Final donde el jugador debe ingresar una palabra clave para escapar.
- juego_escape_room(): Función principal que controla el flujo del juego, llamando a las funciones de las diferentes salas en orden.

Ejemplo de uso:
Para iniciar el juego, simplemente ejecuta el script. El jugador interactuará con el juego a través de la consola, ingresando comandos para realizar acciones.
"""

# Variables globales
inventario = []
tiempo_limite = 300  # 5 minutos en segundos
inicio_tiempo = None


def mostrar_introduccion():
    print("\n¡Bienvenido al Escape Room!")
    print("Estás atrapado en una habitación misteriosa.")
    print("Debes resolver acertijos y encontrar objetos para escapar.")
    print(f"Tienes {tiempo_limite // 60} minutos para salir.")
    input("\nPresiona Enter para comenzar...")


def iniciar_temporizador():
    global inicio_tiempo
    inicio_tiempo = time.time()


def tiempo_restante():
    tiempo_transcurrido = time.time() - inicio_tiempo
    return max(0, tiempo_limite - int(tiempo_transcurrido))


def verificar_tiempo():
    if tiempo_restante() <= 0:
        print("\n¡Se acabó el tiempo! No lograste escapar.")
        return False
    return True


def mostrar_inventario():
    if inventario:
        print("\nInventario:", ', '.join(inventario))
    else:
        print("\nInventario vacío.")


def sala_principal():
    print("\nEstás en la Sala Principal. Hay una puerta cerrada y una mesa.")
    while True:
        if not verificar_tiempo():
            return False

        comando = input("\n¿Qué quieres hacer? (examinar mesa / abrir puerta / inventario / pista): ").strip().lower()

        if comando == "examinar mesa":
            print("Sobre la mesa hay una llave.")
            if "llave" not in inventario:
                print("Has tomado la llave.")
                inventario.append("llave")
        elif comando == "abrir puerta":
            if "llave" in inventario:
                print("Usas la llave para abrir la puerta. ¡Has avanzado a la siguiente sala!")
                return True
            else:
                print("La puerta está cerrada con llave.")
        elif comando == "inventario":
            mostrar_inventario()
        elif comando == "pista":
            print("Tal vez deberías revisar cuidadosamente la mesa...")
        else:
            print("Comando no reconocido. Intenta de nuevo.")


def sala_acertijo():
    print("\nHas entrado a la Sala del Acertijo. Hay un código numérico en la pared.")
    codigo_correcto = "1234"

    while True:
        if not verificar_tiempo():
            return False

        comando = input("\nIngresa el código para abrir la siguiente puerta: ").strip()

        if comando == codigo_correcto:
            print("¡Código correcto! Has avanzado a la siguiente sala.")
            return True
        else:
            print("Código incorrecto. Intenta de nuevo.")


def sala_final():
    print("\nEstás en la última sala. Hay una caja fuerte cerrada.")
    while True:
        if not verificar_tiempo():
            return False

        comando = input("\n¿Qué quieres hacer? (examinar caja / inventario / pista): ").strip().lower()

        if comando == "examinar caja":
            print("La caja tiene un panel para ingresar una palabra clave.")
            clave = input("Ingresa la palabra clave: ").strip().lower()
            if clave == "escape":
                print("\n¡Felicidades! Has escapado de la habitación.")
                return True
            else:
                print("Palabra incorrecta.")
        elif comando == "inventario":
            mostrar_inventario()
        elif comando == "pista":
            print("La clave es algo que quieres hacer...")
        else:
            print("Comando no reconocido.")


def juego_escape_room():
    mostrar_introduccion()
    iniciar_temporizador()

    if not sala_principal():
        return
    if not sala_acertijo():
        return
    if not sala_final():
        return

    print("\n¡Juego terminado! Gracias por jugar.")


if __name__ == "__main__":
    juego_escape_room()
