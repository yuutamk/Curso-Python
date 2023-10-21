# Inicializa un diccionario para almacenar el inventario.
inventario = {}

# Función para agregar un producto al inventario.
def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    stock = int(input("Ingresa la cantidad en stock: "))
    
    if nombre not in inventario:
        inventario[nombre] = {"precio": precio, "stock": stock}
        print("Producto agregado al inventario.")
    else:
        print("El producto ya existe en el inventario.")

# Función para actualizar un producto en el inventario.
def actualizar_producto():
    nombre = input("Ingresa el nombre del producto que deseas actualizar: ")
    if nombre in inventario:
        opcion = input("¿Deseas actualizar el precio (P) o el stock (S)? ").lower()
        if opcion == "p":
            nuevo_precio = float(input("Ingresa el nuevo precio: "))
            inventario[nombre]["precio"] = nuevo_precio
        elif opcion == "s":
            nuevo_stock = int(input("Ingresa la nueva cantidad en stock: "))
            inventario[nombre]["stock"] = nuevo_stock
        else:
            print("Opción no válida.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para eliminar un producto del inventario.
def eliminar_producto():
    nombre = input("Ingresa el nombre del producto que deseas eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado del inventario.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para listar el inventario.
def listar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto, detalles in inventario.items():
            print(f"{producto} - Precio: {detalles['precio']}, Stock: {detalles['stock']}")

# Menú principal
while True:
    print("\n-- Administrador de Inventario --")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Listar inventario")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        listar_inventario()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
