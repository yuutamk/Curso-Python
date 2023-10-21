1. Creamos nuestro nuevo archivo con el nombre ListaDeTareas.py Inicializamos la lista `tareas` para almacenar las tareas y un diccionario `estado_tareas` para rastrear su estado (completadas o no).

    ```python
    # Inicializa una lista para almacenar las tareas.
    tareas = []
    # Inicializa un diccionario para rastrear el estado de las tareas (completadas o no).
    estado_tareas = {}
    ```
2. Definimos la función `agregar_tarea()` para agregar una tarea a la lista. Al agregar una tarea, también actualizamos el diccionario de estado.

    ```python
    # Función para agregar una tarea.
    def agregar_tarea():
        tarea = input("Escribe la tarea que deseas agregar: ")
        tareas.append(tarea)
        estado_tareas[tarea] = False  # Inicialmente, la tarea no está completada.
    ```

3. La función `marcar_completada()` permite marcar una tarea como completada. Aquí, se busca la tarea en el diccionario de estado y se actualiza su estado.

    ```python
    # Función para marcar una tarea como completada.
    def marcar_completada():
        tarea = input("Ingresa la tarea completada: ")
        if tarea in estado_tareas:
            estado_tareas[tarea] = True
            print("Tarea marcada como completada.")
        else:
            print("Tarea no encontrada en la lista.")
    ```

4. La función `eliminar_tarea()` permite eliminar una tarea de la lista. También eliminamos la entrada correspondiente en el diccionario de estado.

    ```python
    # Función para eliminar una tarea.
    def eliminar_tarea():
        tarea = input("Ingresa la tarea a eliminar: ")
        if tarea in estado_tareas:
            tareas.remove(tarea)
            del estado_tareas[tarea]
            print("Tarea eliminada.")
        else:
            print("Tarea no encontrada en la lista.")
    ```

5. La función `listar_tareas()` muestra todas las tareas y sus estados. Comprobamos si la lista de tareas está vacía antes de listarlas.

    ```python
    # Función para listar todas las tareas.
    def listar_tareas():
        if len(tareas) == 0:
            print("No hay tareas en la lista.")
        else:
            print("Lista de tareas:")
            for i, tarea in enumerate(tareas):
                estado = "Completada" if estado_tareas[tarea] else "Pendiente"
                print(f"{i + 1}. {tarea} ({estado})")
    ```

6. Implementamos un menú principal con un bucle `while True` que permite al usuario elegir entre agregar, marcar, eliminar, listar o salir del programa.

    ```python
    # Menú principal
    while True:
        print("\n-- Administrador de Tareas --")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Listar tareas")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            marcar_completada()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            listar_tareas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

    ```
    
7. Dependiendo de la opción seleccionada por el usuario, llamamos a la función correspondiente.

8. El bucle continúa hasta que el usuario elija la opción de salir (opción 5).
