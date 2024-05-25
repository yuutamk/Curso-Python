import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "inteligencia"]
    return random.choice(palabras)

def jugar():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []
    palabra_mostrada = "_ " * len(palabra_secreta)
    print("¡Bienvenido al Juego de Adivinar la Palabra!")
    while intentos > 0 and "_ " in palabra_mostrada:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        intento = input("Ingresa una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Ingresa una sola letra válida.")

        elif intento in letras_adivinadas:
            print("Ya has intentado con esa letra.")

        elif intento not in palabra_secreta:
            intentos -= 1     

        else:
            letras_adivinadas .append(intento)
            palabra_mostrada = "".join(letra 
                if letra in letras_adivinadas 
                else "_ " for letra in palabra_secreta)
    
    if palabra_mostrada == palabra_mostrada:
        print("¡Ganaste! La palabra es:", palabra_secreta)

    elif intentos == 0:
        print("¡Perdiste! La palabra era:", palabra_secreta)

jugar()