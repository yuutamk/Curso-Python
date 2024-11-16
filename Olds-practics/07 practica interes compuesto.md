## Calculadora de Intereses Compuestos:

**Paso 1:** 
Crea un nuevo archivo llamado "Interes_compuesto.py".

Definición de la función `calcular_interes_compuesto`.

```python
def calcular_interes_compuesto(capital, tasa, años):
    monto_final = capital * (1 + tasa / 100) ** años
    return monto_final
```

- Se define una función llamada `calcular_interes_compuesto` que toma tres argumentos: `capital`, `tasa`, y `años`.
- Dentro de la función, se calcula el monto final utilizando la fórmula de interés compuesto y se devuelve el resultado.

**Paso 2:** Manejo de excepciones.

```python
try:
```

Se utiliza `try` para manejar posibles excepciones que puedan ocurrir durante la ejecución del programa.

**Paso 3:** Captura de datos del usuario.

```python
    capital_inicial = float(input("Ingresa el capital inicial: "))
    tasa_anual = float(input("Ingresa la tasa de interés anual (%): "))
    años = int(input("Ingresa el período de inversión en años: "))
```

- Se solicita al usuario que ingrese el capital inicial, la tasa de interés anual y el período de inversión en años, y se almacenan en las variables correspondientes.
- Los valores ingresados se convierten en números de punto flotante o enteros según corresponda.

**Paso 4:** Validación de valores negativos.

```python
    if capital_inicial < 0 or tasa_anual < 0 or años < 0:
        raise ValueError("Los valores no pueden ser negativos.")
```

- Se verifica si alguno de los valores ingresados es negativo. Si alguno de ellos es negativo, se lanza una excepción `ValueError` con un mensaje de error personalizado.

**Paso 5:** Cálculo del monto total.

```python
    monto_total = calcular_interes_compuesto(capital_inicial, tasa_anual, años)
```

- Se llama a la función `calcular_interes_compuesto` con los valores ingresados por el usuario para calcular el monto total.
- El resultado se almacena en la variable `monto_total`.

**Paso 6:** Impresión del resultado.

```python
    print("El monto total después de", años, "años será de:", round(monto_total, 2))
```

- Se imprime el resultado del cálculo del monto total después del período de inversión especificado por el usuario.
- Se utiliza `round` para redondear el monto a dos decimales.

**Paso 7:** Manejo de excepciones (continuación).

```python
except ValueError as e:
    print("Error:", e)
```

- Si se produce una excepción `ValueError`, se captura y se muestra un mensaje de error personalizado que indica que los valores no pueden ser negativos.

Este programa permite a los usuarios calcular el monto total de una inversión con interés compuesto. Se asegura de que los valores ingresados sean válidos y no negativos antes de realizar el cálculo.