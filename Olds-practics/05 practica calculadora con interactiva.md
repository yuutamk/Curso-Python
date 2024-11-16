## Calculadora con funciones

#### Paso 1: Creación del archivo "calculadora_interactiva.py".

#### Paso 2: Definición de funciones para operaciones matemáticas:

```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b
```

- Se definen cuatro funciones (`suma`, `resta`, `multiplicacion`, y `division`) que realizan las operaciones matemáticas respectivas. La función `division` verifica si el divisor es cero para evitar la división por cero.

#### Paso 2 (continuación): Mostrar el menú y obtener la selección del usuario:

```python
print("Calculadora Interactiva")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Selecciona una operación (1/2/3/4): ")
```

- Se muestra un mensaje de bienvenida y se presenta un menú de operaciones al usuario.
- Se utiliza `input` para obtener la selección de operación del usuario, que se almacena en la variable `operacion`.

#### Paso 2 (continuación): Obtener los números del usuario:

```python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
```

- Se solicita al usuario que ingrese dos números, que se almacenan en las variables `num1` y `num2`.
- Los valores ingresados se convierten en números de punto flotante (`float`) para permitir operaciones con decimales.

#### Paso 2 (continuación): Realizar la operación seleccionada:

```python
if operacion == '1':
    resultado = suma(num1, num2)
elif operacion == '2':
    resultado = resta(num1, num2)
elif operacion == '3':
    resultado = multiplicacion(num1, num2)
elif operacion == '4':
    resultado = division(num1, num2)
else:
    resultado = "Operación no válida"
```

- Dependiendo de la operación seleccionada por el usuario, se llama a la función correspondiente (`suma`, `resta`, `multiplicacion`, o `division`) para realizar la operación.
- Si el usuario selecciona una operación no válida, se asigna un mensaje de error a la variable `resultado`.

#### Paso 2 (continuación): Mostrar el resultado:

```python
print("Resultado:", resultado)
```

- Finalmente, se muestra el resultado de la operación en pantalla.

Este código crea una calculadora interactiva que permite al usuario realizar operaciones matemáticas básicas seleccionando la operación deseada y proporcionando dos números.