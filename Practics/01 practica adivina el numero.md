## Juego de Adivinar el Número Aleatorio:

**Paso 1:** 
Crea un nuevo archivo llamado "Numero_Aleatorio.py".

Importación del módulo random.

```python
import random
```

Se importa el módulo `random` para generar números aleatorios, lo cual es necesario para seleccionar el número secreto.

**Paso 2:** Generación del número secreto y variables de control.

```python
numero_secreto = random.randint(1, 100)
intentos = 0
```

- Se utiliza `random.randint(1, 100)` para generar un número aleatorio entre 1 y 100 y se almacena en la variable `numero_secreto`.
- La variable `intentos` se inicializa en 0 para llevar un registro de cuántos intentos ha realizado el usuario.

**Paso 3:** Mensaje de bienvenida.

```python
print("Bienvenido al juego de adivinar el número secreto (entre 1 y 100).")
```

Se imprime un mensaje de bienvenida para informar al usuario sobre el tipo de juego que están a punto de jugar y el rango de números válidos.

**Paso 4:** Bucle while principal.

```python
while True:
```

Se crea un bucle `while` que se ejecutará indefinidamente hasta que el usuario adivine el número secreto y rompa el bucle con la instrucción `break`.

**Paso 5:** Captura del intento del usuario.

```python
    intento = int(input("Ingresa tu suposición: "))
    intentos += 1
```

- Se solicita al usuario que ingrese su suposición (un número) y se almacena en la variable `intento`.
- Se incrementa la variable `intentos` en 1 para llevar un registro de los intentos realizados.

**Paso 6:** Comparación y mensajes.

```python
    if intento == numero_secreto:
        print("¡Correcto! ¡Adivinaste el número secreto (", numero_secreto, ") en", intentos, "intentos!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
```

- Se compara el número ingresado por el usuario (`intento`) con el número secreto (`numero_secreto`).
- Si son iguales, se muestra un mensaje de felicitación, se revela el número secreto y se muestra el número de intentos. Luego, el bucle se rompe con `break`.
- Si el `intento` es menor que el `numero_secreto`, se informa al usuario que el número secreto es mayor.
- Si el `intento` es mayor que el `numero_secreto`, se informa al usuario que el número secreto es menor.

Este juego continúa hasta que el usuario adivina el número secreto. Cada paso se explica detalladamente para comprender cómo funciona el juego de adivinar el número aleatorio.