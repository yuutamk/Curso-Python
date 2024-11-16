class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        objetivo.vida -= self.ataque
        print(f"{self.nombre} ataca a {objetivo.nombre} ¡-{self.ataque} de vida!")

# Funciones CRUD para Personajes
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

# Actualizar los atributos de un personaje
personaje1.vida = 120
personaje1.ataque = 25
print("\n¡Atributos actualizados del personaje!")
mostrar_informacion(personaje1)

# Borrar un personaje (simulación)
del personaje1
print("\n¡Personaje eliminado!")
