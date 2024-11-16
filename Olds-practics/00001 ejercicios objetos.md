### Paso 1: Definición de la Clase Personaje

Primero, creamos la clase `Personaje` que representa a los personajes del juego de rol.

```python
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    # Método para atacar a otro personaje
    def atacar(self, objetivo):
        objetivo.vida -= self.ataque
        print(f"{self.nombre} ataca a {objetivo.nombre} ¡-{self.ataque} de vida!")
```

### Paso 2: Implementación del CRUD

A continuación, creamos funciones para el CRUD (Crear, Leer, Actualizar, Borrar) de Personajes.

```python
def crear_personaje():
    nombre = input("Ingresa el nombre del personaje: ")
    vida = int(input("Ingresa la vida del personaje: "))
    ataque = int(input("Ingresa el valor de ataque del personaje: "))
    return Personaje(nombre, vida, ataque)

def mostrar_informacion(personaje):
    print(f"Nombre: {personaje.nombre}\nVida: {personaje.vida}\nAtaque: {personaje.ataque}")

# Crear un personaje
personaje1 = crear_personaje()
mostrar_informacion(personaje1)

# Actualizar atributos de un personaje
personaje1.vida = 120
personaje1.ataque = 25
print("\n¡Atributos actualizados del personaje!")
mostrar_informacion(personaje1)

# Borrar un personaje (simulación)
del personaje1
print("\n¡Personaje eliminado!")
```