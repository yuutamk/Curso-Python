### **Práctica 1: Juego de Rol con Clases y CRUD**

#### Paso 1: Definición de la Clase Personaje

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

#### Paso 2: Implementación del CRUD

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

---

### **Práctica 2: Simulación de una Tienda Online con CRUD**

#### Paso 1: Definición de la Clase Producto

Definimos la clase `Producto` que representa productos en una tienda online.

```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para mostrar la información del producto
    def mostrar_info(self):
        print(f"Producto: {self.nombre}\nPrecio: ${self.precio}\nStock disponible: {self.stock}")
```

#### Paso 2: Implementación del CRUD para Productos

Agregamos funciones para las operaciones CRUD en la clase Producto.

```python
def crear_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    stock = int(input("Ingresa el stock disponible: "))
    return Producto(nombre, precio, stock)

def actualizar_stock(producto, cantidad):
    producto.stock += cantidad

def eliminar_producto(producto):
    del producto

# Crear un producto
producto1 = crear_producto()
producto1.mostrar_info()

# Actualizar stock de un producto
actualizar_stock(producto1, 10)
print("\n¡Stock actualizado!")
producto1.mostrar_info()

# Eliminar un producto (simulación)
eliminar_producto(producto1)
print("\n¡Producto eliminado!")
```

---

### **Práctica 3: Sistema de Gestión de Biblioteca con CRUD**

#### Paso 1: Definición de la Clase Libro

Definimos la clase `Libro` que representa libros en una biblioteca.

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    # Métodos para prestar y devolver un libro
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print(f"Se ha prestado el libro '{self.titulo}'.")
        else:
            print(f"El libro '{self.titulo}' no está disponible en este momento.")

    def devolver_libro(self):
        self.disponible = True
        print(f"Se ha devuelto el libro '{self.titulo}'.")
```

#### Paso 2: Implementación del CRUD para Libros

Agregamos funciones para realizar operaciones CRUD en la clase Libro.

```python
def crear_libro():
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el nombre del autor del libro: ")
    return Libro(titulo, autor)

def prestar_devolver(libro):
    libro.prestar_libro()
    libro.devolver_libro()

# Crear un libro
libro1 = crear_libro()
print(f"\nInformación del libro:")
print(f"Título: {libro1.titulo}\nAutor: {libro1.autor}")

# Prestar y devolver un libro
prestar_devolver(libro1)
```

---

Estas prácticas muestran cómo implementar operaciones CRUD (Crear, Leer, Actualizar, Borrar) en Python utilizando objetos y clases, permitiendo al usuario interactuar con los datos de manera dinámica.