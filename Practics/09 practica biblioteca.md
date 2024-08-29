### Paso 1: Definición de la Clase Libro

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