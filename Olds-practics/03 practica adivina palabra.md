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
    palabras = ["python", "programacion", "desarrollo", "inteligencia"]
    return random.choice(palabras)
```

- Se define la función `jugar()` que contiene la lógica principal del juego.

```python
def jugar():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    letras_adivinadas = []
    palabra_mostrada = "_ " * len(palabra_secreta)
    print("¡Bienvenido al Juego de Adivinar la Palabra!")
```

#### Paso 3: Inicio del juego y configuración inicial:

- Se establece la palabra secreta seleccionada por el programa.

```python
    palabra_secreta = seleccionar_palabra()
```

- Se configura el número de intentos disponibles (`intentos`) y una lista para almacenar las letras adivinadas (`letras_adivinadas`).
- Se declara la variable `palabra_mostrada` donde se repetirá el símbolo `_` con un espacio por la cantidad de caracteres que tiene la palabra secreta

```python
    intentos = 6
    letras_adivinadas = []
    palabra_mostrada = "_ " * len(palabra_secreta)
```

- Se muestra un mensaje de bienvenida al usuario.

```python
    print("¡Bienvenido al Juego de Adivinar la Palabra!")
```

#### Paso 4: Bucle principal del juego:

- Se inicia un bucle `while` que continúa hasta que el jugador agote todos los intentos (`intentos > 0`) o la palabra mostrada se quede sin `_`.

```python
    while intentos > 0 and "_" in palabra_mostrada:
```

- Se muestra la `palabra_mostrada` con las letras encontradas y `_` las letras que aun están ocultas y la cantidad de intentos restantes.

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
```

- Se comprueba si la letra ingresada ya ha sido intentada antes.

```python
        elif intento in letras_adivinadas:
            print("Ya has intentado con esa letra.")
```

#### Paso 6: Actualización de intentos:

- Si la letra no está en la palabra secreta, se reduce el número de intentos disponibles (`intentos -= 1`).

```python
        elif intento not in palabra_secreta:
            intentos -= 1
```

#### Paso 7: Actualización de las letras adivinadas:

- Si la letra es válida y no se ha intentado antes, se agrega a la lista de `letras_adivinadas`.
- Se utiliza append para agregar la letra de `intento` a `letras adivinadas`
- Se utiliza `.join` para recorre cada uno de los caracteres en la `palabra_secreta` si esta coincide se agregara a la posición en `palabra_mostrada` en caso de que no se encuentre
en la `palabra_secreta` se remplazara por una `_`.

```python
        else:
            letras_adivinadas .append(intento)
            palabra_mostrada = "".join(letra
            if letra in letras_adivinadas 
            else "_" for letra in palabra_secreta)
```

#### Paso 8: Comprobación de victoria o derrota:

- Si la palabra oculta es igual a la `palabra_secreta`, el jugador gana y se muestra un mensaje de victoria.

```python
        if palabra_mostrada == palabra_mostrada:
        print("¡Ganaste! La palabra es:", palabra_secreta)
```

- Si se agotan los intentos, el jugador pierde y se muestra la palabra secreta.

```python
    elif intentos == 0:
        print("¡Perdiste! La palabra era:", palabra_secreta)
```

#### Paso 9: Ejecuta el archivo y juega al juego de adivinar la palabra.

Este código crea un juego interactivo en el que el programa elige una palabra al azar y el usuario intenta adivinarla letra por letra. El juego utiliza funciones para organizar la lógica del juego y se ejecuta al final del script.