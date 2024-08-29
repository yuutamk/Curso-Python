import random

def seleccionar_palabra():
    palabras = ["python", "programación", "desarrollo", "inteligencia"]
    return random.choice(palabras)

def jugar():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []

    print("¡Bienvenido al Juego de Adivinar la Palabra!")

    while intentos > 0:
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "

        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        intento = input("Ingresa una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if intento in letras_adivinadas:
            print("Ya has intentado con esa letra.")
            continue

        letras_adivinadas.append(intento)

        if intento not in palabra_secreta:
            intentos -= 1

        if palabra_secreta == palabra_mostrada:
            print("¡Ganaste! La palabra es:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Perdiste! La palabra era:", palabra_secreta)

jugar()
