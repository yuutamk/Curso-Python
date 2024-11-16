## Registro y Análisis de Ventas Diarias

Vamos a crear un programa que registre y analice las ventas diarias de varios vendedores. ¿Estás listo para empezar? ¡Vamos allá!

### Paso 1: Configuración Inicial

**Primero, necesitamos configurar nuestro entorno de trabajo.**

* **Crea un nuevo archivo en tu editor de texto o entorno de desarrollo (IDE) favorito. Llámalo** `ventas_diarias.py`.


### Paso 2: Comprendiendo el Código

**Vamos a desglosar el código para entender mejor cada sección.**

#### 1. **Listas para almacenar datos**

```python
# Lista para almacenar las ventas y nombres de los vendedores
ventas_diarias = []
nombres_vendedores = []
```
Aquí, `ventas_diarias` guardará las ventas diarias y `nombres_vendedores` guardará los nombres de los vendedores.

#### 2. **Solicitar el número de días**

```python
# Solicitar la cantidad de días a registrar
dias = int(input("Ingrese el número de días a registrar ventas: "))
```
Pedimos al usuario que ingrese el número de días para los cuales desea registrar las ventas.

#### 3. **Recolectar datos del usuario**

```python
# Recolectar datos del usuario
for dia in range(dias):
    nombre = input(f"Ingrese el nombre del vendedor para el día {dia + 1}: ")
    venta = float(input(f"Ingrese la venta del día {dia + 1}: "))
    nombres_vendedores.append(nombre)
    ventas_diarias.append(venta)
```
Usamos un bucle `for` para recolectar los nombres y ventas diarias de los vendedores.

***** La **f** en este código de Python se utiliza para **formatear** una cadena de texto. En este caso, la expresión `f"Ingrese el nombre del vendedor para el día {dia + 1}:"` crea una cadena de texto que incluye el valor de la variable `dia` más 1 dentro de la cadena. Por ejemplo, si `dia` tiene un valor de 2, la cadena resultante sería "Ingrese el nombre del vendedor para el día 3:". Esto facilita la creación de mensajes personalizados y dinámicos. 😊

#### 4. **Mostrar ventas diarias y calcular el total de ventas**

```python
# Mostrar las ventas diarias y calcular el total de ventas
total_ventas = 0
print("\nVentas diarias:")
for i in range(len(ventas_diarias)):
    print(f"Día {i + 1} - Vendedor: {nombres_vendedores[i]}, Venta: ${ventas_diarias[i]:.2f}")
    total_ventas += ventas_diarias[i]
print("Total de ventas:", total_ventas)
```
Aquí, imprimimos cada venta diaria con el nombre del vendedor y calculamos el total de ventas.


* **`\n`**: Este es un **carácter de escape** que representa una **nueva línea**. Cuando se encuentra en una cadena de texto, se utiliza para crear un salto de línea. En este caso, se coloca antes del texto "Ventas diarias:", lo que hace que la siguiente línea se imprima en una nueva línea.

* **`.2f`**: Esto es una **especificación de formato** para números de punto flotante (números decimales). La parte antes del punto (`.`) indica la cantidad de dígitos que se mostrarán después del punto decimal. En este caso, `.2f` significa que se mostrarán **dos dígitos** después del punto decimal. Por ejemplo, si `ventas_diarias[i]` tiene un valor de `123.456`, se mostrará como `123.46`.


#### 5. **Determinar el vendedor con mayores ventas**

```python
# Determinar el vendedor con mayores ventas
max_venta = ventas_diarias[0]
mejor_vendedor = nombres_vendedores[0]
for i in range(1, len(ventas_diarias)):
    if ventas_diarias[i] > max_venta:
        max_venta = ventas_diarias[i]
        mejor_vendedor = nombres_vendedores[i]
print(f"El vendedor con mayores ventas es {mejor_vendedor} con una venta de ${max_venta:.2f}")
```
Buscamos al vendedor con la venta más alta y mostramos su nombre y venta.

* la función **`len()`** se utiliza para obtener la **longitud** de una secuencia, como una lista o una cadena de texto.

 **`len(ventas_diarias)`**: Esto devuelve la cantidad de elementos en la lista `ventas_diarias`. En el bucle `for`, se utiliza para iterar sobre los elementos de la lista desde el segundo elemento hasta el último. El primer elemento (índice 0) ya se ha asignado a las variables `max_venta` y `mejor_vendedor`.


#### 6. **Contar los días con ventas superiores a $1000**

```python
# Contar los días con ventas superiores a $1000
dias_ventas_altas = 0
for venta in ventas_diarias:
    if venta > 1000:
        dias_ventas_altas += 1
print("Días con ventas superiores a $1000:", dias_ventas_altas)
```
Contamos y mostramos el número de días con ventas superiores a $1000.

#### 7. **Ventas incrementadas en un 10%**

```python
# Crear una lista con las ventas incrementadas en un 10%
ventas_incrementadas = []
for venta in ventas_diarias:
    ventas_incrementadas.append((venta * 10/ 100) + venta)
print("Ventas incrementadas en un 10%:", ventas_incrementadas)
```
Calculamos un aumento del 10% en cada venta y mostramos los resultados.

#### 8. **Filtrar ventas menores a $500**

```python
# Filtrar las ventas menores a $500
ventas_bajas = []
for venta in ventas_diarias:
    if venta < 500:
        ventas_bajas.append(venta)
print("Ventas menores a $500:", ventas_bajas)
```
Creamos una lista con ventas menores a $500 y las mostramos.


### Reflexiona sobre el Código

1. **¿Qué hace cada parte del código?**:
    - La primera parte configura listas y pide el número de días.
    - El bucle `for` recolecta datos para cada día.
    - Luego, el código imprime las ventas diarias y calcula el total.
    - A continuación, encuentra al vendedor con mayores ventas y cuenta los días con ventas superiores a $1000.
    - Finalmente, muestra las ventas incrementadas en un 10% y filtra las ventas menores a $500.

2. **Modificaciones sugeridas**:
    - ¿Qué pasa si añades un vendedor para un día adicional? 
    - ¿Cómo cambiarías el programa para calcular el promedio de ventas?

### Experimenta

1. **Prueba con diferentes cantidades de días y ventas**.
2. **Modifica el código** para añadir nuevas funcionalidades, como calcular el promedio de ventas diarias.


**así queda el codigo final revisa tu codigo para que no haya errores**:

```python
# Lista para almacenar las ventas y nombres de los vendedores
ventas_diarias = []
nombres_vendedores = []

# Solicitar la cantidad de días a registrar
dias = int(input("Ingrese el número de días a registrar ventas: "))

# Recolectar datos del usuario
for dia in range(dias):
    nombre = input(f"Ingrese el nombre del vendedor para el día {dia + 1}: ")
    venta = float(input(f"Ingrese la venta del día {dia + 1}: "))
    nombres_vendedores.append(nombre)
    ventas_diarias.append(venta)

# Mostrar las ventas diarias y calcular el total de ventas
total_ventas = 0
print("\nVentas diarias:")
for i in range(len(ventas_diarias)):
    print(f"Día {i + 1} - Vendedor: {nombres_vendedores[i]}, Venta: ${ventas_diarias[i]:.2f}")
    total_ventas += ventas_diarias[i]
print("Total de ventas:", total_ventas)

# Determinar el vendedor con mayores ventas
max_venta = ventas_diarias[0]
mejor_vendedor = nombres_vendedores[0]
for i in range(1, len(ventas_diarias)):
    if ventas_diarias[i] > max_venta:
        max_venta = ventas_diarias[i]
        mejor_vendedor = nombres_vendedores[i]
print(f"El vendedor con mayores ventas es {mejor_vendedor} con una venta de ${max_venta:.2f}")

# Contar los días con ventas superiores a $1000
dias_ventas_altas = 0
for venta in ventas_diarias:
    if venta > 1000:
        dias_ventas_altas += 1
print("Días con ventas superiores a $1000:", dias_ventas_altas)

# Crear una lista con las ventas incrementadas en un 10%
ventas_incrementadas = []
for venta in ventas_diarias:
    ventas_incrementadas.append((venta *10 / 100) + venta)
print("Ventas incrementadas en un 10%:", ventas_incrementadas)

# Filtrar las ventas menores a $500
ventas_bajas = []
for venta in ventas_diarias:
    if venta < 500:
        ventas_bajas.append(venta)
print("Ventas menores a $500:", ventas_bajas)
```