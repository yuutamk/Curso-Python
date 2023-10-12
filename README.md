<details>
<summary><h3>MENÚ PYTHON</h3></summary>

1. [Python](#python)
2. [Configuración del Entorno de Desarrollo](#install-py)
3. [Elige un Editor de Texto](#editor)
4. [¡Comienza a Programar!](#primer-programa)
5. [Variables](#variables)
6. [Tipos de datos](#tipos-datos)
7. [Operadores](#operadores)
8. [Estructuras de Control](#estructuras)
9. [Condicionales (if)](#estructura-if)
10. [Bucle (for)](#ciclo-for)
11. [Bucle (while)](#ciclo-while)
12. [Funciones](#funciones)
13. [Módulos](#modulos)
14. [Excepciones](#excepciones)
15. [Listas en Python](#listas)
16. [Tuplas](#tuplas)
17. [Diccionarios en Python](#diccionario)
18. [Conjuntos en Python](#conjuntos)
<!-- 19. [Elementos Multimedia](#multimedia)
20. [Scripts](#scripts) -->
<!-- 10. [Elemento 10](#elemento-10) -->


</details>

# PYTHON
![python logo](/src/img/Python-Logo.png)

¡Hola a todos los futuros programadores y programadoras! En este emocionante viaje hacia el mundo de la programación, hoy vamos a explorar un lenguaje de programación súper versátil y poderoso llamado Python. Pero antes de sumergirnos en la magia de la codificación, necesitamos entender que es python y preparar nuestro entorno de desarrollo.



## ¿Qué es Python?<a name="python"></a>

Python es un lenguaje de programación que se ha vuelto extremadamente popular en todo el mundo. ¿Sabías que es el lenguaje detrás de aplicaciones web como Instagram y YouTube? ¡Increíble, verdad?

Python es un lenguaje de programación de alto nivel, interpretado y generalmente fácil de aprender. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Desde entonces, ha evolucionado y madurado hasta convertirse en uno de los lenguajes de programación más populares y utilizados en todo el mundo.

¿Sabías que Python comenzó como un proyecto de hobby? Su creador, Guido van Rossum, era un apasionado de la programación y quería crear un lenguaje que fuera fácil de entender y poderoso. En diciembre de 1989, mientras buscaba un proyecto para mantenerse ocupado, decidió crear un intérprete para un nuevo lenguaje de scripting que había estado ideando. ¿Sabes qué le inspiró para nombrarlo "Python"? ¡Su amor por el grupo de comedia Monty Python! Así que, aunque parezca extraño, este lenguaje debe su nombre a un grupo de comediantes británicos.

### La Versatilidad de Python

Una de las razones por las que Python se ha vuelto tan popular es su versatilidad. Puedes usar Python para muchas cosas diferentes. Aquí hay algunos ejemplos:

- **Desarrollo Web**: Python se utiliza para crear sitios web. Maneja tareas como el envío y procesamiento de datos, la comunicación con bases de datos y la seguridad.

- **Desarrollo de Software**: En el desarrollo de software, Python puede ayudar en el control de construcción, seguimiento de errores y automatización de pruebas.

- **Ciencia de Datos**: Python es una herramienta esencial en el análisis de datos. Puede manejar grandes conjuntos de datos y realizar análisis complejos.

- **Automatización de Procesos**: Python puede automatizar tareas repetitivas, lo que lo hace útil en la industria para ahorrar tiempo y recursos.

- **Inteligencia Artificial y Aprendizaje Automático**: Gracias a su ecosistema de bibliotecas, Python es perfecto para proyectos de inteligencia artificial y aprendizaje automático.

- **Desarrollo de Juegos**: Incluso se usa en la creación de videojuegos populares como Los Sims 4 y Battlefield 2.

![aplicaciones](/src/img/campos-de-aplicacion.jpg)

### Razones para Aprender Python

Ahora, te preguntarás por qué deberías aprender Python. Bueno, aquí tienes algunas razones:

- **Fácil de Leer**: Python se enorgullece de tener una sintaxis fácil de entender, lo que lo hace perfecto para principiantes.

- **Código Abierto y Gratuito**: ¡Puedes usar Python de forma gratuita! Incluso para proyectos comerciales.

- **Gran Comunidad**: Si te encuentras con un problema, es probable que alguien más ya lo haya resuelto. La comunidad de Python es enorme y solidaria.

- **Portabilidad**: Puedes escribir código Python en una plataforma y ejecutarlo en otra sin problemas.

![razones](/src/img/razones-python.png)

Python es un lenguaje de programación fascinante que se ha convertido en una herramienta esencial en el mundo de la tecnología. Grandes empresas como NASA, Google, Netflix y Spotify confían en Python para impulsar sus servicios y productos.

Así que, si estás pensando en aprender programación, Python es un excelente lugar para empezar. ¡Es una habilidad con un gran futuro y una demanda creciente en la industria!

## Configuración del Entorno de Desarrollo<a name="install-py"></a>

Ahora, hablemos sobre la configuración de tu "entorno de desarrollo". Esto suena un poco complicado, ¡pero no te preocupes! Básicamente, es el lugar donde escribirás, probarás y ejecutarás tu código Python. 

Configurar un entorno de desarrollo de Python es el primer paso esencial para cualquier programador que quiera comenzar a trabajar con este versátil lenguaje de programación. Ya sea que estés planeando desarrollar aplicaciones web, explorar la inteligencia artificial o simplemente aprender a programar, la configuración adecuada del entorno te ayudará a empezar de manera efectiva. En este apartado, te guiaré a través de los pasos iniciales para configurar tu entorno de desarrollo de Python.



### 1. Instala Python

Imagina que Python es como una pluma antes de comenzar a escribir en el mundo de la programación. Es una herramienta fundamental que necesitas tener en tu caja de herramientas informáticas. Afortunadamente, instalar Python en tu computadora es un proceso sencillo y esencial para cualquier aspirante a programador.

#### **Paso 1: Descarga Python**

El primer paso es obtener el software Python en tu computadora. Para hacerlo, simplemente visita el sitio web oficial de Python en [python.org](https://www.python.org/downloads/). Allí encontrarás la última versión disponible para descargar.

![Descargar python](/src/img/py-download.png)

#### **Paso 2: Instalación en Sistemas Unix (Linux o macOS)**

Si estás utilizando un sistema operativo basado en Unix, como Linux o macOS, es posible que ya tengas una versión de Python preinstalada. Sin embargo, te recomendamos encarecidamente que utilices la última versión disponible desde el sitio web oficial.

Una vez que hayas descargado el archivo de instalación, ejecútalo siguiendo las instrucciones. Esto asegurará que estás utilizando la versión más actualizada de Python.

#### **Paso 3: Instalación en Windows**

Para los usuarios de Windows, también puedes descargar Python desde el sitio web oficial. Durante la instalación, asegúrate de marcar la casilla que dice "Agregar Python X.X a PATH" (donde "X.X" es la versión de Python). Esto es importante porque permite que Python sea fácilmente accesible desde la línea de comandos de Windows.

![Alt text](/src/img/install-check.png)

Una vez que hayas completado estos pasos, habrás instalado Python en tu sistema. Ahora estás listo para aventurarte en el emocionante mundo de la programación.

### 2. Elige un Editor de Texto<a name="editor"></a>


El siguiente paso es elegir un editor de código o un IDE que te ayude a escribir y depurar código de Python de manera eficiente. Algunas opciones populares incluyen:

- **Visual Studio Code (VSCode)**: Es un editor de código gratuito y altamente personalizable que ofrece una excelente experiencia para programar en Python. Puedes instalar extensiones como "Python" y "Pylance" para mejorar aún más la funcionalidad.

- **PyCharm**: Es un IDE específicamente diseñado para Python. La versión Community es gratuita y ofrece una gran cantidad de características útiles para los desarrolladores de Python.

- **Jupyter Notebook**: Es una herramienta fantástica para la exploración de datos y el desarrollo interactivo de Python. Viene preinstalado en Anaconda, una distribución de Python que es popular en el ámbito de la ciencia de datos.

![IDE vs Editor](/src/img/Editor_vs_IDE.png)

### Paso 3: Instalar Bibliotecas y Dependencias

La mayoría de los proyectos de Python requerirán bibliotecas y dependencias adicionales. Puedes utilizar la herramienta `pip` para instalar paquetes de Python. Por ejemplo, para instalar la popular biblioteca NumPy, simplemente ejecuta:

```bash
pip install numpy
```

Recuerda que si estás utilizando un entorno virtual, debes activarlo antes de usar `pip` para asegurarte de que las bibliotecas se instalen en el entorno correcto.

![bibliotecas](/src/img/librrerias-python.jpg)

## Paso 5: ¡Comienza a Programar!<a name="primer-programa"></a>

¡Ahora que has configurado tu entorno de desarrollo de Python, estás listo para empezar a programar! Puedes escribir código Python en tu editor de elección, ejecutarlo y ver los resultados. Python es un lenguaje versátil con una amplia comunidad y recursos en línea, por lo que siempre encontrarás ayuda y documentación disponibles cuando la necesites.

#### 3. ¡Hola, Mundo!

Ahora que todo está configurado, es hora de hacer tu primer programa Python. Abre tu editor de texto y escribe lo siguiente:

```python
print("¡Hola, Mundo!")
```

Luego, guarda el archivo con una extensión ".py", por ejemplo, "mi_primer_programa.py". Esto le dice a tu computadora que es un programa de Python.

#### 4. Ejecuta tu Programa

Abre tu línea de comandos (si usas Windows, es el "Símbolo del sistema" o "CMD"; en Mac o Linux, es la "Terminal"). Navega a la ubicación donde guardaste tu archivo ".py" y escribe:

```
python mi_primer_programa.py
```

¡Y listo! Verás la frase "¡Hola, Mundo!" en la pantalla. ¡Has escrito y ejecutado tu primer programa Python!



Ahora tienes Python en tu computadora y estás listo para comenzar tu emocionante viaje en el mundo de la programación. No te preocupes si al principio todo parece un poco confuso, ¡todos empezamos desde algún lugar!

# Variables<a name="variables"></a>

Ahora vamos a adentrarnos en el emocionante mundo de Python y explorar un concepto fundamental: las variables. No te preocupes si esto suena un poco técnico, ¡lo explicaremos de manera sencilla y divertida!

### ¿Qué son las Variables en Python?

Imagina que una variable es como una caja mágica donde puedes guardar cosas. Cada vez que pones algo en la caja, le das un nombre para recordar lo que contiene. En Python, una variable es como esa caja mágica. Es un lugar donde puedes guardar datos y darles un nombre. ¿Por qué son importantes? Porque permiten que tu programa recuerde información y realice tareas inteligentes.

![variables](/src/img/variables.png)

Por ejemplo, si quieres guardar tu edad en Python, puedes hacerlo así:

```python
edad = 12
```
### Nombres de Variables en Python

Puedes darles cualquier nombre a tus variables, pero hay algunas reglas que debes seguir:

- El nombre de la variable no puede comenzar con un número.
- Debe comenzar con una letra o un guión bajo.
- Puedes usar letras, números y guiones bajos en el nombre de la variable.
- Python distingue entre mayúsculas y minúsculas. "edad" y "Edad" serían dos variables diferentes.


#### Crear una Variable

En Python, crear una variable es súper fácil. Solo tienes que pensar en un nombre para tu variable y decirle a Python qué hay dentro. Por ejemplo:

```python
edad = 12
nombre = "Luis"
```

Aquí, hemos creado dos variables. "edad" guarda el número 12 y "nombre" guarda la palabra "Luis".

#### 2. Usar una Variable

Una vez que tienes una variable, puedes usarla en tu programa. Por ejemplo, podemos imprimir el valor de "edad" y "nombre" en la pantalla:

```python
print("Mi nombre es", nombre)
print("Tengo", edad, "años")
```

Cuando ejecutes este código, verás que Python toma el valor de las variables y lo muestra en la pantalla.

¡Las variables también pueden usarse en operaciones matemáticas!



### Cambiando el Valor de una Variable

Las variables pueden cambiar de valor. Por ejemplo, si celebramos un cumpleaños, podemos aumentar la edad en 1:

```python
edad = edad + 1
print("¡Feliz cumpleaños! Ahora tengo", edad, "años")
```

¡Ves cómo la variable "edad" cambia su valor?



# Tipos de datos<a name="tipos-datos"></a>

### Tipos de Datos en Variables

Imagina que tienes una caja mágica (sí, otra vez) y quieres guardar cosas en ella, pero esta vez quieres separarlas según lo que sean: números, palabras, etc. Los tipos de datos en Python son como etiquetas que te ayudan a organizar y trabajar con diferentes tipos de información.

Veamos algunos de los tipos de datos más comunes en Python:

- **Enteros (int)**: Guardan números enteros, como la edad en nuestro ejemplo.
- **Cadenas de Texto (str)**: Guardan palabras o frases, como el nombre.
- **Decimales (float)**: Guardan números con decimales, como 3.14.
- **Booleanos (bool)**: Guardan valores verdaderos o falsos, como True o False.

#### 1. Enteros (int)

Los números enteros son como tu edad, ¡números sin decimales! Por ejemplo:

```python
mi_edad = 12
```

En este caso, "mi_edad" es una variable de tipo entero que almacena el valor 12.

#### 2. Flotantes (float)

Los números flotantes son números con decimales. Por ejemplo:

```python
altura = 1.75
```

La variable "altura" es un flotante y contiene el valor 1.75.

#### 3. Cadenas de Texto (str)

Las cadenas de texto son como palabras o frases. Por ejemplo:

```python
nombre = "Ana"
```

La variable "nombre" es una cadena de texto que contiene el nombre "Ana".

#### 4. Booleanos (bool)

Los booleanos son como interruptores que pueden estar encendidos (True) o apagados (False). Por ejemplo:

```python
es_mayor_de_edad = False
```

La variable "es_mayor_de_edad" es un booleano y está configurada como False en este caso.

### ¿Por qué son Importantes los Tipos de Datos?

Los tipos de datos son esenciales porque determinan cómo se almacena y se maneja la información en Python. Por ejemplo, no querrías sumar una cadena de texto a un número, ¿verdad? Los tipos de datos te ayudan a evitar errores y a hacer que tu programa funcione de manera correcta.

### Ejemplos Prácticos

Veamos algunos ejemplos más interesantes:

```python
# Números
num1 = 10
num2 = 5
suma = num1 + num2
print("La suma de", num1, "y", num2, "es igual a", suma)

# Cadenas de Texto
saludo = "¡Hola, "
nombre = "María!"
mensaje = saludo + nombre
print(mensaje)

# Booleanos
es_mayor_de_edad = edad >= 18
print("¿Es mayor de edad?", es_mayor_de_edad)
```

¡Bien hecho! Ahora sabes lo que son las variables y cómo usarlas en Python. Son como cajas mágicas donde puedes guardar información importante. Recuerda darles nombres descriptivos para que puedas recordar fácilmente lo que contienen.

# Operadores en Python<a name="operadores"></a>

En programación, los operadores son herramientas que nos permiten realizar tareas como cálculos matemáticos, comparar valores y tomar decisiones. Vamos a ver los tipos de operadores más comunes en Python.

#### 1. Operadores Aritméticos

Los operadores aritméticos se utilizan para realizar cálculos matemáticos. Aquí tienes algunos ejemplos:

```python
# Suma
resultado_suma = 5 + 3
print("Suma:", resultado_suma)

# Resta
resultado_resta = 10 - 7
print("Resta:", resultado_resta)

# Multiplicación
resultado_multiplicacion = 4 * 6
print("Multiplicación:", resultado_multiplicacion)

# División
resultado_division = 12 / 3
print("División:", resultado_division)

# Módulo (resto de la división)
resultado_modulo = 10 % 3
print("Módulo:", resultado_modulo)
```
- Suma (+): `3 + 5` da como resultado `8`.
- Resta (-): `10 - 7` da como resultado `3`.
- Multiplicación (*): `4 * 6` da como resultado `24`.
- División (/): `12 / 3` da como resultado `4.0` (¡un flotante!).
- Módulo (%): `10 % 3` da como resultado `1` (el resto de la división).

#### 2. Operadores de Comparación

Los operadores de comparación se utilizan para comparar valores y devuelven un valor booleano (True o False). Aquí tienes ejemplos:

```python
# Igual
igual = 5 == 5
print("Igual:", igual)

# No igual
no_igual = 5 != 3
print("No igual:", no_igual)

# Mayor que
mayor_que = 7 > 3
print("Mayor que:", mayor_que)

# Menor que
menor_que = 4 < 2
print("Menor que:", menor_que)

# Mayor o igual que
mayor_o_igual_que = 6 >= 6
print("Mayor o igual que:", mayor_o_igual_que)

# Menor o igual que
menor_o_igual_que = 9 <= 8
print("Menor o igual que:", menor_o_igual_que)
```
- Igual (==): `5 == 5` da como resultado `True`.
- No igual (!=): `5 != 3` da como resultado `True`.
- Mayor que (>): `7 > 3` da como resultado `True`.
- Menor que (<): `4 < 2` da como resultado `False`.
- Mayor o igual que (>=): `6 >= 6` da como resultado `True`.
- Menor o igual que (<=): `9 <= 8` da como resultado `False`.

#### 3. Operadores Lógicos

Los operadores lógicos se utilizan para combinar condiciones y tomar decisiones. Aquí tienes ejemplos:

```python
# Y (and)
condicion_and = True and False
print("Y (and):", condicion_and)

# O (or)
condicion_or = True or False
print("O (or):", condicion_or)

# No (not)
condicion_not = not True
print("No (not):", condicion_not)
```
- Y (and): `True and False` da como resultado `False`.
- O (or): `True or False` da como resultado `True`.
- No (not): `not True` da como resultado `False`.

### **Ejemplo 1: Operaciones Aritméticas**

```python
edad = 12
altura = 1.5
suma = edad + altura

print("Edad:", edad)
print("Altura:", altura)
print("Resultado de la suma:", suma)
```

En este ejemplo, hemos utilizado el operador de suma `+` para sumar la variable `edad` y la variable `altura`. Luego, imprimimos los valores de `edad`, `altura` y el resultado de la suma utilizando la función `print()`.

### **Ejemplo 2: Operadores de Comparación**

```python
temperatura = 28
es_caluroso = temperatura > 30

print("Temperatura:", temperatura)
print("¿Es un día caluroso?", es_caluroso)
```

En este caso, hemos usado el operador de comparación "mayor que" (`>`) para verificar si la variable `temperatura` es mayor que 30. Luego, imprimimos el valor de `temperatura` y la variable `es_caluroso` que almacena el resultado de la comparación.

### **Ejemplo 3: Operadores Lógicos**

```python
es_dia_laboral = True
tengo_clases = True
puedo_ir_al_parque = es_dia_laboral and not tengo_clases

print("¿Es día laboral?", es_dia_laboral)
print("¿Tengo clases?", tengo_clases)
print("¿Puedo ir al parque?", puedo_ir_al_parque)
```

En este tercer ejemplo, hemos utilizado operadores lógicos. Primero, definimos las variables `es_dia_laboral` y `tengo_clases`. Luego, usamos el operador `and` para verificar si ambas condiciones son verdaderas y el operador `not` para negar la segunda condición. Finalmente, imprimimos los valores de las variables y el resultado de la operación lógica.

### Estructuras de Control en Python<a name="estructuras"></a>

Las estructuras de control son como las herramientas que nos permiten tomar decisiones y repetir acciones en nuestros programas. Imagina que eres un director de orquesta y tienes que dirigir a los músicos para que toquen en armonía. Las estructuras de control en Python son como tu batuta mágica que te permite dirigir el flujo de un programa. Te ayudan a tomar decisiones y repetir acciones según sea necesario.

Vamos a conocer dos tipos principales de estructuras de control en Python:

#### 1. Condicionales (if)<a name="estructura-if"></a>

Imagina que tienes un interruptor en tu habitación que enciende o apaga una luz. Las sentencias "if" en Python son como ese interruptor; te permiten tomar decisiones en tus programas. Puedes decirle a tu programa qué hacer si se cumple una condición y qué hacer si no.

Vamos a profundizar en cómo funcionan las sentencias "if" en Python:

#### Sintaxis de la Sentencia "if":

```python
if condición:
    # Código a ejecutar si la condición es verdadera
else:
    # Código a ejecutar si la condición es falsa
```

Las sentencias "if" se utilizan para evaluar si una condición es verdadera o falsa. Si la condición es verdadera, se ejecuta el bloque de código debajo del "if". Si es falsa, se ejecuta el bloque de código bajo el "else" (si está presente).

La estructura de control condicional (if) te permite tomar decisiones en tu programa. Aquí tienes unos ejemplos prácticos:

#### Ejemplo 1: Evaluando una Edad

```python
edad = 12

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
```

En este caso, el programa verifica si la edad es menor de 18 y muestra un mensaje adecuado.

#### Ejemplo 2: Verificando un Número Par

```python
numero = 7

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
```

Aquí, el programa verifica si un número es par o impar y muestra un mensaje en consecuencia.

¡Magnífico! Ahora conoces las sentencias "if" en Python y cómo usarlas para tomar decisiones en tus programas. Estas sentencias son como las instrucciones que das a tu programa para que tome caminos diferentes según las condiciones.

#### 2. Estructura de Control de Bucle (for)<a name="ciclo-for"></a>

Imagina que tienes una lista de tareas y quieres realizar una acción para cada elemento de la lista. El bucle "for" en Python es como tu asistente personal que te ayuda a recorrer y realizar acciones en cada elemento de una secuencia, como una lista o una cadena de texto.

Vamos a adentrarnos en cómo funciona el bucle "for" en Python:

#### Sintaxis del Bucle "for":

```python
for elemento in secuencia:
    # Código a ejecutar para cada elemento
```

El bucle "for" se utiliza para iterar a través de una secuencia (como una lista) y ejecutar un bloque de código para cada elemento en esa secuencia.

La estructura de control de bucle (for) te permite repetir acciones un número específico de veces. Por ejemplo:
#### Ejemplo 1: Iterando a través de una Lista

```python
nombres = ["Alice", "Bob", "Charlie", "David"]

for nombre in nombres:
    print("Hola,", nombre)
```

En este caso, el bucle "for" recorre la lista de nombres y saluda a cada persona.

#### Ejemplo 2: Contando Hasta un Número

```python
numero_limite = 5

for numero in range(numero_limite):
    print("Número:", numero)
```

Aquí, el bucle "for" cuenta desde 0 hasta el número límite.

¡Fantástico! Ahora conoces el bucle "for" en Python y cómo usarlo para recorrer secuencias y realizar acciones en cada elemento. El bucle "for" es como un explorador que te guía a través de un mapa de datos.

#### 3. Estructura de Control de Bucle (while)<a name="ciclo-while"></a>

Imagina que estás buscando un tesoro y sigues buscando hasta que encuentras una "X" en el mapa. El bucle "while" en Python es como tu búsqueda de tesoro; te permite repetir una acción mientras se cumpla una condición.

Vamos a explorar cómo funciona el bucle "while" en Python:

#### Sintaxis del Bucle "while":

```python
while condición:
    # Código a ejecutar mientras se cumpla la condición
```

El bucle "while" se utiliza para repetir un bloque de código mientras una condición sea verdadera. Si la condición se vuelve falsa en algún momento, el bucle se detiene.


#### Ejemplo 1: Contando Hasta un Número

```python
numero = 1

while numero <= 5:
    print("Número:", numero)
    numero += 1
```

En este caso, el bucle "while" cuenta desde 1 hasta 5 y muestra los números.

#### Ejemplo 2: Adivinando un Número

```python
numero_secreto = 7
intentos = 0

while True:
    intento = int(input("Adivina el número secreto: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Correcto! ¡Lo adivinaste en", intentos, "intentos!")
        break
```

Aquí, el bucle "while" permite adivinar un número secreto y se detiene cuando se adivina correctamente.

¡Increíble! Ahora conoces el bucle "while" en Python y cómo usarlo para repetir acciones mientras se cumple una condición. El bucle "while" es como una búsqueda emocionante que continúa hasta que se alcanza el objetivo.

# Funciones<a name="funciones"></a>

Las funciones son bloques de código reutilizable que te ayudan a organizar y simplificar tu programa.

Imagina que tienes un libro de recetas y cada receta es una serie de pasos para cocinar un delicioso platillo. Las funciones en Python son como esas recetas; te permiten agrupar un conjunto de instrucciones en un solo lugar y darle un nombre. Esto hace que tu programa sea más organizado y fácil de entender.

Vamos a descubrir cómo funcionan las funciones en Python:

#### Sintaxis de una Función en Python:

```python
def nombre_de_la_funcion(parametro1, parametro2):
    # Código a ejecutar
    resultado = parametro1 + parametro2
    return resultado
```

- `def`: Esta palabra clave se utiliza para definir una función en Python.
- `nombre_de_la_funcion`: Es el nombre que eliges para tu función.
- `parametro1` y `parametro2`: Son valores que puedes pasar a la función para que los use en su interior.
- `return`: Es la palabra clave que se utiliza para devolver un valor desde la función.

#### Ejemplo 1: Función que Saluda

```python
def saludar(nombre):
    mensaje = "¡Hola, " + nombre + "!"
    return mensaje

nombre_usuario = "Alice"
saludo = saludar(nombre_usuario)
print(saludo)
```

En este caso, creamos una función llamada `saludar` que toma un nombre como parámetro y devuelve un mensaje de saludo.

#### Ejemplo 2: Función que Calcula el Cuadrado

```python
def calcular_cuadrado(numero):
    cuadrado = numero * numero
    return cuadrado

numero_ingresado = 5
resultado = calcular_cuadrado(numero_ingresado)
print("El cuadrado de", numero_ingresado, "es", resultado)
```

Aquí, creamos una función llamada `calcular_cuadrado` que toma un número como parámetro y devuelve su cuadrado.

¡Excelente trabajo! Ahora conoces las funciones en Python y cómo usarlas para agrupar y reutilizar código. Las funciones son como herramientas que puedes utilizar una y otra vez en diferentes partes de tu programa.

# Módulos<a name="modulos"></a>

Imagina que estás construyendo una ciudad y necesitas diferentes tipos de edificios: escuelas, hospitales, y más. Los módulos en Python son como esos edificios especializados que puedes agregar a tu ciudad de Python. Cada módulo contiene funciones y variables que puedes utilizar en tu programa.

Vamos a descubrir cómo funcionan los módulos en Python:

#### Importando un Módulo:

```python
import nombre_del_modulo
```

Para usar un módulo en Python, primero debes importarlo. Esto te permite acceder a las funciones y variables que contiene.

#### Ejemplo 1: Usando el Módulo "math"

```python
import math

# Calculando la raíz cuadrada
numero = 25
raiz = math.sqrt(numero)
print("La raíz cuadrada de", numero, "es", raiz)

# Calculando el seno
angulo = 45
seno = math.sin(math.radians(angulo))
print("El seno de", angulo, "grados es", seno)
```

En este caso, importamos el módulo "math" y utilizamos sus funciones para calcular la raíz cuadrada y el seno de un número.

#### Ejemplo 2: Usando el Módulo Personalizado

Supongamos que tienes un archivo llamado "mi_modulo.py" con el siguiente contenido:

```python
# mi_modulo.py

def saludar(nombre):
    return "¡Hola, " + nombre + "!"

def doble(numero):
    return numero * 2
```

Ahora, puedes usar este módulo personalizado en tu programa principal:

```python
import mi_modulo

nombre = "Alice"
saludo = mi_modulo.saludar(nombre)
print(saludo)

numero = 5
resultado = mi_modulo.doble(numero)
print("El doble de", numero, "es", resultado)
```

Aquí, importamos el módulo personalizado "mi_modulo.py" y utilizamos sus funciones en nuestro programa principal.

¡Fantástico! Ahora conoces los módulos en Python y cómo usarlos para aprovechar funciones y variables adicionales. Los módulos son como tesoros de código que puedes agregar a tu programa para hacerlo más poderoso.
# Excepciones<a name="excepciones"></a>

Imagina que estás cocinando tu plato favorito y te das cuenta de que te falta un ingrediente importante. Las excepciones en Python son como esos momentos inesperados en la programación donde algo sale mal, y necesitas manejar la situación de manera elegante.

Vamos a descubrir cómo funcionan las excepciones en Python:

#### Uso de `try` y `except`:

```python
try:
    # Código que podría generar una excepción
except TipoDeExcepcion:
    # Código a ejecutar si se produce una excepción del tipo especificado
```

- `try`: Este bloque contiene el código que podría generar una excepción.
- `except`: Si ocurre una excepción del tipo especificado, este bloque se ejecuta para manejarla.

#### Ejemplo 1: Manejando una División por Cero

```python
try:
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")
else:
    print("El resultado es:", resultado)
```

En este caso, utilizamos `try` y `except` para manejar una posible excepción cuando intentamos dividir por cero.

#### Ejemplo 2: Manejando un Valor no Numérico

```python
try:
    entrada = input("Ingresa un número: ")
    numero = float(entrada)
except ValueError:
    print("¡Error! Debes ingresar un número válido.")
else:
    print("El número ingresado es:", numero)
```

Aquí, usamos `try` y `except` para manejar la posibilidad de que el usuario ingrese un valor que no sea numérico.

¡Excelente trabajo! Ahora conoces cómo manejar excepciones en Python utilizando `try` y `except`. Esto te permite lidiar con situaciones inesperadas de manera controlada y elegante en tus programas.

Con esto, completamos nuestra primera semana de aprendizaje de Python. ¡Esperamos que estos conceptos te ayuden a dar tus primeros pasos en la programación con Python! En la próxima semana, continuaremos explorando más elementos emocionantes de Python, como listas, diccionarios y más.

¡Mantente atento y sigue aprendiendo! 🐍🚀

---

¡Hola, jóvenes entusiastas de Python! Hoy vamos a adentrarnos en un tema emocionante y esencial: las listas en Python.

### ¿Qué son las Listas en Python?<a name="listas"></a>

Imagina que tienes una caja de LEGO con diferentes piezas. Las listas en Python son como esa caja; te permiten almacenar una colección de elementos en un solo lugar. Puedes pensar en ellas como un conjunto de elementos ordenados que puedes modificar, agregar o eliminar según tus necesidades.

Vamos a adentrarnos en cómo funcionan las listas en Python:

#### Creación de una Lista:

```python
mi_lista = [1, 2, 3, 4, 5]
```

Las listas se crean utilizando corchetes `[]` y los elementos se separan por comas.

#### Ejemplo 1: Creando una Lista de Nombres

```python
nombres = ["Alice", "Bob", "Charlie", "David"]
```

Aquí, creamos una lista de nombres. Puedes acceder a cada nombre por su posición en la lista.

#### Ejemplo 2: Modificando una Lista

```python
colores = ["rojo", "verde", "azul"]
colores[1] = "amarillo"
```

En este caso, cambiamos el segundo elemento de la lista de "verde" a "amarillo".

En Python, las listas utilizan indexación basada en cero, lo que significa que el primer elemento de la lista tiene un índice de 0, el segundo elemento tiene un índice de 1, el tercer elemento tiene un índice de 2 y así sucesivamente. Por lo tanto, cuando se cambia el valor en la posición 1 de la lista, se está haciendo referencia al segundo elemento de la lista.

La lista `colores` contiene tres elementos:

- El elemento en la posición 0 es "rojo".
- El elemento en la posición 1 es "verde".
- El elemento en la posición 2 es "azul".

Al ejecutar la línea `colores[1] = "amarillo"`, estás reemplazando el valor en la posición 1 (que es "verde") por "amarillo". Por lo tanto, el segundo elemento de la lista cambia de "verde" a "amarillo", y la lista resultante es `["rojo", "amarillo", "azul"]`.

Es importante recordar que la indexación basada en cero es una característica común en muchos lenguajes de programación y puede requerir cierta familiarización para trabajar con listas y otros tipos de secuencias en Python.

#### Ejemplo 3: Agregando y Eliminando Elementos

```python
frutas = ["manzana", "banana", "cereza"]
frutas.append("uva")  # Agregar un elemento al final
frutas.insert(1, "naranja")  # Insertar un elemento en una posición específica
frutas.remove("banana")  # Eliminar un elemento por valor
```

Aquí, mostramos cómo agregar elementos al final o en una posición específica, y cómo eliminar elementos de la lista.


1. **Agregar un elemento al final de la lista:**
   
   La línea `frutas.append("uva")` agrega la cadena "uva" al final de la lista `frutas`. Como resultado, la lista `frutas` se verá así:

   ```python
   ["manzana", "banana", "cereza", "uva"]
   ```

   La función `append()` agrega el elemento al final de la lista sin importar la posición anterior de los elementos.

2. **Insertar un elemento en una posición específica:**

   La línea `frutas.insert(1, "naranja")` inserta la cadena "naranja" en la posición 1 de la lista `frutas`. Esto desplaza el elemento anterior en esa posición hacia la derecha. La lista resultante será:

   ```python
   ["manzana", "naranja", "banana", "cereza", "uva"]
   ```

   La función `insert()` toma dos argumentos: la posición en la que se desea insertar el elemento y el elemento en sí.

3. **Eliminar un elemento por valor:**

   La línea `frutas.remove("banana")` elimina el elemento "banana" de la lista `frutas`. Después de esta operación, la lista se verá de la siguiente manera:

   ```python
   ["manzana", "naranja", "cereza", "uva"]
   ```

   La función `remove()` busca el valor especificado y elimina la primera ocurrencia de ese valor en la lista. Si hubiera múltiples "banana" en la lista, solo se eliminaría la primera.

Estas operaciones son esenciales para manipular listas en Python. Puedes agregar elementos al final o en posiciones específicas, y también eliminar elementos según su valor. Es importante tener en cuenta que las listas en Python son flexibles y permiten una amplia gama de operaciones para administrar datos.

¡Fantástico! Ahora conoces las listas en Python y cómo utilizarlas para organizar colecciones de elementos. Las listas son como contenedores versátiles que te permiten trabajar con datos de manera eficiente.

### ¿Qué son las Tuplas en Python?<a name="tuplas"></a>

Imagina que tienes una caja de joyas con piedras preciosas que no puedes modificar. Las tuplas en Python son como esas cajas; te permiten almacenar una colección de elementos, pero a diferencia de las listas, las tuplas son inmutables, lo que significa que no puedes cambiar su contenido una vez que se crean.

Vamos a adentrarnos en cómo funcionan las tuplas en Python:

#### Creación de una Tupla:

```python
mi_tupla = (1, 2, 3, 4, 5)
```

Las tuplas se crean utilizando paréntesis `()` y los elementos se separan por comas.

#### Ejemplo 1: Creando una Tupla de Coordenadas

```python
coordenadas = (3, 4)
```

Aquí, creamos una tupla que representa las coordenadas (3, 4).Esto puede ser útil, por ejemplo, en geometría para representar puntos en un plano.

#### Ejemplo 2: Intentando Modificar una Tupla

```python
mi_tupla = (1, 2, 3)
mi_tupla[1] = 5  # ¡Esto generará un error!
```

En este caso, intentamos modificar el segundo elemento de la tupla, pero como mencioné antes, las tuplas son inmutables, por lo que generará un error.

#### Ejemplo 3: Usando Tuplas en Funciones

```python
def dividir_y_redondear(numero1, numero2):
    cociente = numero1 / numero2
    resto = numero1 % numero2
    return (cociente, resto)

resultado = dividir_y_redondear(10, 3)
print("Cociente:", resultado[0])
print("Resto:", resultado[1])
```

En este último ejemplo, hemos definido una función llamada `dividir_y_redondear` que toma dos números como entrada, realiza una división y cálculo de resto, y devuelve una tupla con los resultados. Luego, llamamos a la función con los valores 10 y 3, y almacenamos la tupla resultante en la variable `resultado`. Finalmente, imprimimos el cociente y el resto accediendo a los elementos de la tupla utilizando la indexación, es decir, `resultado[0]` para el cociente y `resultado[1]` para el resto. Las tuplas son útiles para devolver múltiples valores desde una función.

### ¿Qué son los Diccionarios en Python?<a name="diccionario"></a>

Imagina que tienes un cuaderno donde puedes anotar definiciones de palabras junto con sus significados. Los diccionarios en Python son como ese cuaderno; te permiten almacenar pares de "palabra" (clave) y "definición" (valor). Los diccionarios son una forma eficiente de gestionar datos estructurados.

Vamos a adentrarnos en cómo funcionan los diccionarios en Python:

#### Creación de un Diccionario:

```python
mi_diccionario = {"manzana": "una fruta roja y deliciosa", "coche": "un vehículo de cuatro ruedas"}
```

Los diccionarios se crean utilizando llaves `{}` y los pares clave-valor se separan por comas.

#### Ejemplo 1: Accediendo a un Valor por Clave

```python
mi_diccionario = {"manzana": "una fruta roja y deliciosa", "coche": "un vehículo de cuatro ruedas"}
print("Significado de 'manzana':", mi_diccionario["manzana"])
```

En este ejemplo, hemos creado un diccionario llamado `mi_diccionario` con dos pares clave-valor. La clave "manzana" se asocia con el valor "una fruta roja y deliciosa", y la clave "coche" se asocia con el valor "un vehículo de cuatro ruedas".

Para acceder al valor asociado con una clave específica, utilizamos la sintaxis de corchetes y proporcionamos la clave. En este caso:

```python
print("Significado de 'manzana':", mi_diccionario["manzana"])
```

La línea de código anterior imprime el significado de la palabra "manzana" en nuestro "diccionario". En otras palabras, estamos accediendo al valor asociado con la clave "manzana" en el diccionario `mi_diccionario`.

Este enfoque es muy útil cuando necesitas buscar información asociada con una clave específica en un conjunto de datos, como definiciones en un diccionario o datos en una base de datos. Los diccionarios son una de las estructuras de datos más versátiles en Python y se utilizan ampliamente en la programación para el almacenamiento y recuperación eficiente de información.

#### Ejemplo 2: Agregando o Modificando Elementos
En Python, los diccionarios son estructuras de datos flexibles que permiten almacenar pares clave-valor. Puedes agregar nuevos elementos a un diccionario o modificar los valores existentes asociados con una clave específica. 

```python
mi_diccionario = {"manzana": "una fruta roja y deliciosa", "coche": "un vehículo de cuatro ruedas"}
mi_diccionario["bicicleta"] = "un vehículo de dos ruedas"
mi_diccionario["coche"] = "un vehículo de transporte motorizado"
```

#### **Agregando un Elemento:**

```python
mi_diccionario["bicicleta"] = "un vehículo de dos ruedas"
```

En esta línea, estamos agregando un nuevo elemento al diccionario. La clave es "bicicleta" y el valor asociado es "un vehículo de dos ruedas". El diccionario ahora contendrá tres elementos.

#### **Modificando un Elemento:**

```python
mi_diccionario["coche"] = "un vehículo de transporte motorizado"
```

Aquí, estamos modificando el valor asociado con la clave "coche". Originalmente, "coche" estaba relacionado con "un vehículo de cuatro ruedas", pero hemos actualizado el valor a "un vehículo de transporte motorizado".

Después de estas operaciones, el diccionario `mi_diccionario` se verá así:

```python
{
    "manzana": "una fruta roja y deliciosa",
    "coche": "un vehículo de transporte motorizado",
    "bicicleta": "un vehículo de dos ruedas"
}
```

Este ejemplo ilustra cómo los diccionarios en Python te permiten agregar nuevas entradas o actualizar los valores existentes con facilidad. Las claves deben ser únicas en un diccionario, pero los valores pueden ser cualquier tipo de dato. Los diccionarios son una herramienta poderosa para organizar y manipular datos en programas Python.

#### Ejemplo 3: Recorriendo un Diccionario

```python
mi_diccionario = {"manzana": "una fruta roja y deliciosa", "coche": "un vehículo de cuatro ruedas"}

for clave, valor in mi_diccionario.items():
    print("La", clave, "es", valor)
```

En este caso, recorremos el diccionario y mostramos todas las claves y sus respectivos valores.


En este fragmento de código, hemos utilizado un bucle `for` para recorrer el diccionario `mi_diccionario`. La función `items()` se usa para obtener pares clave-valor del diccionario. En cada iteración del bucle, la variable `clave` toma el valor de una clave y la variable `valor` toma el valor asociado con esa clave.

Dentro del bucle, estamos imprimiendo una oración que describe el par clave-valor. Por ejemplo, en la primera iteración, el bucle imprime "La manzana es una fruta roja y deliciosa". En la segunda iteración, imprimirá "El coche es un vehículo de cuatro ruedas".

Este enfoque es útil cuando necesitas realizar una acción o procesamiento en cada elemento del diccionario. Puedes acceder tanto a las claves como a los valores de forma individual y realizar tareas específicas en cada uno de ellos. Los bucles `for` junto con el método `items()` hacen que trabajar con diccionarios sea muy conveniente en Python.

¡Fantástico! Ahora conoces los diccionarios en Python y cómo utilizarlos para organizar datos estructurados de manera eficiente. Los diccionarios son como tu propio libro de definiciones personal.

### ¿Qué son los Conjuntos en Python?<a name="conjuntos"></a>

Imagina que tienes una colección de gemas preciosas y quieres asegurarte de que no haya duplicados. Los conjuntos en Python son como esa colección; te permiten almacenar elementos únicos y no duplicados. Son una excelente opción cuando necesitas mantener una lista de elementos distintos.

Vamos a adentrarnos en cómo funcionan los conjuntos en Python:

#### Creación de un Conjunto:

```python
mi_conjunto = {1, 2, 3, 4, 5}
```

Los conjuntos se crean utilizando llaves `{}` y los elementos se separan por comas.

#### Ejemplo 1: Creando un Conjunto de Colores

```python
colores = {"rojo", "verde", "azul"}
```

Aquí, creamos un conjunto de colores. Los elementos en un conjunto no tienen un orden específico.

#### Ejemplo 2: Agregando y Eliminando Elementos

```python
frutas = {"manzana", "banana", "cereza"}
frutas.add("uva")  # Agregar un elemento al conjunto
frutas.remove("banana")  # Eliminar un elemento del conjunto
```

En este caso, mostramos cómo agregar elementos al conjunto y cómo eliminar elementos del conjunto.

#### Ejemplo 3: Realizando Operaciones de Conjuntos

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A | B  # Unión de conjuntos
interseccion = A & B  # Intersección de conjuntos
diferencia = A - B  # Diferencia de conjuntos

print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
```

En este ejemplo, realizamos operaciones de conjuntos como unión, intersección y diferencia.

¡Excelente trabajo! Ahora conoces los conjuntos en Python y cómo utilizarlos para mantener una colección de elementos únicos. Los conjuntos son como cofres de tesoros que no permiten duplicados.