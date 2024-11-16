class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print(f"Se ha prestado el libro '{self.titulo}'.")
        else:
            print(f"El libro '{self.titulo}' no está disponible en este momento.")

    def devolver_libro(self):
        self.disponible = True
        print(f"Se ha devuelto el libro '{self.titulo}'.")

# Funciones CRUD para Libros
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
