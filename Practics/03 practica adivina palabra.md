## Adivina la parabra secreta
#### Paso 1: Creación del archivo "adivina_la_palabra.py".

#### Paso 2: Definición de funciones para el juego:

- Se importa el módulo `random` para seleccionar una palabra al azar.

```python
import random
```

- Se define la función `seleccionar_palabra()` que elige una palabra al azar de una lista de palabras.

```python
def seleccionar_palabra():
    palabras = ["python", "programación", "desarrollo", "inteligencia"]
    return random.choice(palabras)
```

- Se define la función `jugar()` que contiene la lógica principal del juego.

```python
def jugar():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []

    print("¡Bienvenido al Juego de Adivinar la Palabra!")
```

#### Paso 3: Inicio del juego y configuración inicial:

- Se establece la palabra secreta seleccionada por el programa.

```python
    palabra_secreta = seleccionar_palabra()
```

- Se configura el número de intentos disponibles (`intentos`) y una lista para almacenar las letras adivinadas (`letras_adivinadas`).

```python
    intentos = 6
    letras_adivinadas = []
```

- Se muestra un mensaje de bienvenida al usuario.

```python
    print("¡Bienvenido al Juego de Adivinar la Palabra!")
```

#### Paso 4: Bucle principal del juego:

- Se inicia un bucle `while` que continúa hasta que el jugador gane o agote todos los intentos (`intentos > 0`).

```python
    while intentos > 0:
```

- Se muestra la palabra oculta con "_" para las letras no adivinadas y las letras adivinadas en su lugar.

```python
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_ "
```

- Se muestra la cantidad de intentos restantes.

```python
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
```

- Se solicita al usuario que ingrese una letra (`intento`).

```python
        intento = input("Ingresa una letra: ").lower()
```

#### Paso 5: Validación del input del usuario:

- Se verifica si el input del usuario es una sola letra válida.

```python
        if len(intento) != 1 or not intento.isalpha():
            print("Ingresa una sola letra válida.")
            continue
```

- Se comprueba si la letra ingresada ya ha sido intentada antes.

```python
        if intento in letras_adivinadas:
            print("Ya has intentado con esa letra.")
            continue
```

#### Paso 6: Actualización de las letras adivinadas:

- Si la letra es válida y no se ha intentado antes, se agrega a la lista de `letras_adivinadas`.

```python
        letras_adivinadas.append(intento)
```

#### Paso 7: Actualización de intentos:

- Si la letra no está en la palabra secreta, se reduce el número de intentos disponibles (`intentos -= 1`).

```python
        if intento not in palabra_secreta:
            intentos -= 1
```

#### Paso 8: Comprobación de victoria o derrota:

- Si la palabra oculta (`palabra_mostrada`) coincide con la palabra secreta, el jugador gana y se muestra un mensaje de victoria.

```python
        if palabra_secreta == palabra_mostrada:
            print("¡Ganaste! La palabra es:", palabra_secreta)
            break
```

- Si se agotan los intentos, el jugador pierde y se muestra la palabra secreta.

```python
    if intentos == 0:
        print("¡Perdiste! La palabra era:", palabra_secreta)
```

#### Paso 9: Ejecuta el archivo y juega al juego de adivinar la palabra.

Este código crea un juego interactivo en el que el programa elige una palabra al azar y el usuario intenta adivinarla letra por letra. El juego utiliza funciones para organizar la lógica del juego y se ejecuta al final del script.