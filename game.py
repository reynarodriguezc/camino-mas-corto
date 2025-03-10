import random

def adivina_el_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 10)
    intentos = 0

    # Imprimir el mensaje de bienvenida y las instrucciones del juego
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número entre 1 y 10.")

    # Bucle principal del juego
    while True:
        # Solicitar al usuario que introduzca su adivinanza
        adivinanza = int(input("Introduce tu adivinanza: "))
        intentos += 1

        # Comparar la adivinanza del usuario con el número secreto
        if adivinanza < numero_secreto:
            # La adivinanza es demasiado baja
            print("Demasiado bajo. Intenta nuevamente.")
        elif adivinanza > numero_secreto:
            # La adivinanza es demasiado alta
            print("Demasiado alto. Intenta nuevamente.")
        else:
            # El usuario ha adivinado el número correctamente
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Llamar a la función para iniciar el juego
adivina_el_numero()
