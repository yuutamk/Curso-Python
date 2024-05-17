### Paso 1: Definición de la Clase Producto

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

### Paso 2: Implementación del CRUD para Productos

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