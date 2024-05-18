## Calculadora con Menú de Opciones

**Paso 1:** Inicio del programa.
Crea un nuevo archivo llamado "Calculadora_con_Menu.py".

```python
while opcion != '5':
```
- Creamos un bucle `while` que se ejecutará indefinidamente siempre y cuando el usuario no seleccione la opción 5 de salir.

**Paso 2:** Mostrar un menú de opciones al usuario.

```python
    print("Menú de Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
```
- Imprimimos un menú en pantalla para que el usuario pueda seleccionar una operación matemática o salir del programa.

**Paso 3:** Solicitar al usuario que seleccione una opción.

```python
    opcion = input("Selecciona una opción (1/2/3/4/5): ")
```
- Utilizamos `input` para obtener la opción elegida por el usuario y la almacenamos en la variable `opcion`.

**Paso 4:** Manejar la opción seleccionada por el usuario.

```python
    try:
        if '0' < opcion < '5':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
``` 
- Usamos `try` para manejar posibles excepciones al ingresar números. 
- Definimos la condicional donde `opcion` sea mayor a 0 y menor a 5 para que solicite los números al usuario y se ejecuten las operaciones.
- Convertimos la entrada del usuario en números de punto flotante (`float`) para permitir operaciones con decimales.

**Paso 5:** Realizar la operación seleccionada.

```python
        if opcion == '1':
            resultado = num1 + num2
        elif opcion == '2':
            resultado = num1 - num2
        elif opcion == '3':
            resultado = num1 * num2
        elif opcion == '4':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 / num2
```
- Dependiendo de la opción seleccionada por el usuario, realizamos la operación matemática correspondiente.
- En el caso de la división, verificamos si el segundo número es cero para evitar la división por cero y lanzar una excepción en caso de que ocurra.

**Paso 6:** Mostrar el resultado de la operación.

```python
        print("Resultado:", resultado)
```
- Imprimimos el resultado de la operación en pantalla.

**Paso 7** Mostrar mensaje de error en caso de que el usuario seleccione una opcion que no se encuentra en el menu

```python
    elif opcion != '5' :
            print("Opción no válida. Por favor, selecciona una opción válida.")
```
- Declaramos la condicional si opción es diferente a 5, el programa mostrara un mensaje de opción no valida, al usar elif a la misma altura if '0' < opcion < '5' el programa no validara ambas condiciones por que si la opcion elegida es valida no se imprimira el mensaje aunque sea diferente de 5

**Paso 8:** Manejar excepciones.

```python
    except ValueError:
        print("Error: Debes ingresar números válidos.")
    except ZeroDivisionError as e:
        print("Error:", e)
```
- Usamos bloques `except` para manejar dos tipos de excepciones: `ValueError` (cuando el usuario no ingresa números válidos) y `ZeroDivisionError` (cuando se intenta dividir por cero).
- Mostramos mensajes de error apropiados en caso de excepción.

Este programa de calculadora con menú de opciones permite al usuario realizar operaciones matemáticas, manejar excepciones y salir del programa cuando lo desee. Cada línea de código se agrega para cumplir una función específica y facilitar la interacción del usuario con la calculadora.