import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Bienvenido al juego de adivinar el número secreto (entre 1 y 100).")

while True:
    intento = int(input("Ingresa tu suposición: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Correcto! ¡Adivinaste el número secreto (", numero_secreto, ") en", intentos, "intentos!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
