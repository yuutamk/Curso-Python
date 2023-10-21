1. Inicializamos un diccionario llamado `inventario` para almacenar detalles de los productos.

    ```python
    # Inicializa un diccionario para almacenar el inventario.
    inventario = {}
    ```

2. Definimos la función `agregar_producto()` para agregar un producto al inventario, y comprobamos si el producto ya existe en el inventario antes de agregarlo.

    ```python
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
    ```

3. La función `actualizar_producto()` permite actualizar el precio o el stock de un producto existente. Se verifica si el producto existe antes de realizar la actualización.

    ```python
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
    ```

4. La función `eliminar_producto()` permite eliminar un producto del inventario si se encuentra en la lista.

    ```python
    # Función para eliminar un producto del inventario.
    def eliminar_producto():
        nombre = input("Ingresa el nombre del producto que deseas eliminar: ")
        if nombre in inventario:
            del inventario[nombre]
            print("Producto eliminado del inventario.")
        else:
            print("Producto no encontrado en el inventario.")
    ```

5. La función `listar_inventario()` muestra todos los productos en el inventario junto con sus detalles.

    ```python
    # Función para listar el inventario.
    def listar_inventario():
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto, detalles in inventario.items():
                print(f"{producto} - Precio: {detalles['precio']}, Stock: {detalles['stock']}")
    ```

6. Implementamos un menú principal con un bucle `while True` que permite al usuario elegir entre agregar, actualizar, eliminar, listar o salir del programa.

    ```python
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
    ```

7. Dependiendo de la opción seleccionada por el usuario, llamamos a la función correspondiente.

8. El bucle continúa hasta que el usuario elija la opción de salir (opción 5).
