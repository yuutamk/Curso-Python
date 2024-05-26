# Aprendiendo Programación Orientada a Objetos en Python

¡Bienvenidos al maravilloso mundo de la programación orientada a objetos (POO) en Python! La POO es como un lienzo en blanco para los artistas de la programación, y en este blog, te enseñaremos cómo pintar tu obra maestra con objetos, atributos y métodos en Python.

## La POO en Python: La Habilidad Artística de la Programación

La programación es un arte, y como en cualquier forma de arte, elegir las herramientas adecuadas es esencial. La programación orientada a objetos en Python es una de esas habilidades imprescindibles. Aprenderla te permitirá crear código eficiente, modular y hermoso. En este blog, te guiaremos a través de los fundamentos de la POO en Python de una manera creativa y fácil de entender.

## ¿Por Dónde Empezar?

Antes de sumergirte en la programación orientada a objetos, es importante tener un conocimiento básico de Python. Si estás familiarizado con los siguientes conceptos, estás listo para continuar:

- **Variable**: Un nombre simbólico que apunta a un objeto específico.
- **Operadores aritméticos**: Suma (+), resta (-), multiplicación (*), división (/), división entera (//), módulo (%).
- **Tipos de datos incorporados**: Numéricos (enteros, flotantes, complejos), secuencias (cadenas, listas, tuplas), booleanos (Verdadero, Falso), diccionarios y conjuntos.
- **Expresiones booleanas**: Expresiones en las que el resultado es True o False.
- **Condicional**: Evaluación de una expresión booleana y ejecución de un proceso en función del resultado (if/else).
- **Bucle**: Ejecución repetida de bloques de código (for o while).
- **Funciones**: Bloques de código organizados y reutilizables definidos con la palabra clave `def`.
- **Argumentos**: Objetos que se pasan a una función, como `sum([1, 2, 4])`.

Ahora que tienes estos conceptos claros, ¡estás listo para sumergirte en la programación orientada a objetos en Python!

## ¿Qué es la Programación Orientada a Objetos en Python?

La programación orientada a objetos, o POO, es un paradigma de programación que nos permite abordar problemas complejos pensando en ellos como objetos. Un objeto en Python es una colección única de datos (atributos) y comportamiento (métodos). Puedes imaginar objetos como cosas reales que te rodean, como calculadoras o automóviles.

¿Por qué debemos utilizar la POO en Python? Aquí hay algunas ventajas clave:

### 1. Reutilización de Código
La POO te permite reutilizar el código mediante la implementación de la abstracción. Esto hace que tu código sea más conciso y legible, lo que es crucial para cualquier proyecto a largo plazo.

### 2. Evita el "Código Espagueti"
La programación orientada a objetos te ayuda a evitar el "código espagueti". Con la POO, puedes organizar la lógica en objetos, lo que evita largas cadenas de condicionales anidados.

### 3. Mejora el Análisis
Una vez que entiendas la POO, podrás pensar en los problemas como objetos específicos y pequeños, lo que acelera el desarrollo del proyecto.

## Programación Estructurada Vs. Programación Orientada a Objetos

La programación estructurada es el enfoque más común para principiantes, ya que es una forma sencilla de construir programas pequeños. Se trata de ejecutar un programa Python de forma secuencial. Sin embargo, este enfoque tiene sus desventajas cuando los proyectos crecen y se vuelven más complejos.

Imagina que estás en el emocionante mundo de la programación, listo para crear un programa para una cafetería. Tu misión: hacer que los clientes ingresen su presupuesto y mostrarles qué café pueden comprar. Parece una tarea sencilla, ¿verdad? Sin embargo, la elección de tu enfoque de programación puede hacer que esta tarea sea un paseo por el parque o una aventura laberíntica. Aquí es donde entran en juego dos enfoques diferentes: la programación estructurada y la programación orientada a objetos.

**La Programación Estructurada:**

Este enfoque es como la bicicleta de entrenamiento de los programadores principiantes. Comenzamos de manera sencilla, escribiendo líneas de código una tras otra. Aquí tienes un vistazo a cómo podría verse el código de una cafetería en un mundo estructurado:

```python
small = 2
regular = 5
big = 6

user_budget = input('¿Cuál es tu presupuesto? ')

try:
    user_budget = int(user_budget)
except:
    print('Por favor, introduce un número')
    exit()

if user_budget > 0:
    if user_budget >= big:
        print('Puedes comprar el café grande')
        if user_budget == big:
            print('Es exacto')
        else:
            print('Tu cambio es', user_budget - big)
    elif user_budget == regular:
        print('Puedes comprar el café regular')
        print('Es exacto')
    elif user_budget >= small:
        print('Puedes comprar el café pequeño')
        if user_budget == small:
            print('Es exacto')
        else:
            print('Tu cambio es', user_budget - small)
```

¡Funciona! Pero, oh, tiene mucho condicional anidado y lógica repetida. Modificarlo en el futuro podría ser un dolor de cabeza.

**La Programación Orientada a Objetos (POO):**

Ahora, piensa en la POO como tu máquina de café de alta gama. Es elegante, eficiente y personalizable. En lugar de escribir líneas y líneas de código, puedes organizar todo en una "caja" ordenada. Mira cómo funciona:

```python
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print('Ingresa un número o decimal')
            exit()
        if budget < 0:
            print('Lo siento, no tienes dinero')
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'Puedes comprar el café {self.name}')
            if budget == self.price:
                print('Es exacto')
            else:
                print(f'Aquí tienes tu cambio: {self.get_change(budget)}$')
            exit('Gracias por tu compra')
```

Este código luce diferente, ¿verdad? Hemos creado una "clase" llamada "Coffee" que contiene toda la información y lógica relacionada con el café. La belleza de esto es que podemos crear múltiples tipos de café sin lío.

Entonces, ¿cómo lo usamos? Simple, creamos objetos de café y los vendemos:

```python
small = Coffee('Pequeño', 2)
regular = Coffee('Regular', 5)
big = Coffee('Grande', 6)

try:
    user_budget = float(input('¿Cuál es tu presupuesto? '))
except ValueError:
    exit('Por favor, introduce un número')

for coffee in [big, regular, small]:
    coffee.sell(user_budget)
```

Ambos enfoques nos llevan al mismo resultado, pero la POO es como tener un equipo de baristas expertos que trabajan juntos de manera organizada y elegante. Es especialmente útil cuando tu proyecto crece y necesitas más funcionalidades. ¡Así que levanta tu taza de café y da la bienvenida a la programación orientada a objetos en tu vida!

## Todo en Python es un Objeto

Una característica destacada de Python es que todo es un objeto. Desde números, cadenas y listas hasta funciones y clases, todos ellos son objetos. Esto significa que todos los objetos tienen atributos y métodos que puedes utilizar.

Para acceder a los atributos y métodos de un objeto, utilizamos la notación de puntos. Por ejemplo, puedes convertir una cadena en mayúsculas con el método `upper()` o comprobar su tipo con `type()`.

```
my_string = "Hola, soy una cadena"
print(my_string.upper())  # Imprime la cadena en mayúsculas
print(type(my_string))  #

 Imprime el tipo de objeto
```

## Definiendo una Clase

En POO, una clase es un plano o plantilla para crear objetos. Los objetos son instancias de una clase. Para definir una clase en Python, utilizamos la palabra clave `class`. Aquí hay un ejemplo simple:

```python
class MiClase:
    pass
```

La palabra clave `pass` se usa aquí para indicar que la clase está vacía. Puedes agregar atributos y métodos a la clase más adelante.

## Creando un Objeto

Una vez que has definido una clase, puedes crear objetos (instancias) de esa clase. Para hacerlo, simplemente llama a la clase como si fuera una función. Por ejemplo:

```python
mi_objeto = MiClase()  # Crea una instancia de MiClase
```

¡Ahora tienes un objeto `mi_objeto` de la clase `MiClase`!

## Atributos de Clase

Los atributos son variables que almacenan datos relacionados con un objeto. Puedes pensar en ellos como características que un objeto posee. Puedes definir atributos de clase en la definición de la clase o dentro de los métodos de la clase. Por ejemplo:

```python
class MiClase:
    atributo = 42
```

Para acceder a los atributos de clase, utilizamos la notación de puntos. Por ejemplo:

```python
print(mi_objeto.atributo)  # Imprime 42
```

## Métodos de Clase

Los métodos son funciones definidas dentro de una clase que pueden realizar acciones relacionadas con el objeto. Los métodos pueden acceder a los atributos del objeto y modificarlos. Aquí hay un ejemplo:

```python
class MiClase:
    def mi_metodo(self):
        print("¡Hola desde el método!")

mi_objeto = MiClase()
mi_objeto.mi_metodo()  # Imprime "¡Hola desde el método!"
```

Ten en cuenta que todos los métodos de clase deben tener `self` como su primer parámetro, que se refiere al objeto actual.

## ¡Más Por Venir!

Este blog es solo el comienzo de tu viaje en la programación orientada a objetos en Python. En futuras publicaciones, te guiaré a través de conceptos más avanzados como herencia, encapsulación y polimorfismo. La POO es un concepto poderoso, y dominarla te hará un programador más eficiente y capaz.

Mantente atento a las próximas publicaciones para seguir aprendiendo. ¡La programación orientada a objetos puede ser desafiante, pero es increíblemente gratificante una vez que la dominas!