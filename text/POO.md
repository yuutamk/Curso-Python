**Blog Creativo: Programación Estructurada Vs. Programación Orientada a Objetos**

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