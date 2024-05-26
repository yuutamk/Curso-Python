Práctica 3: Creación de un Gestor de Tareas
En esta práctica, crearemos una aplicación de línea de comandos para gestionar tareas pendientes. Los usuarios pueden agregar, ver y eliminar tareas.

Paso 1: Crea un archivo llamado "gestor_de_tareas.py".

Paso 2: Escribe el código para el gestor de tareas:

python
Copy code
tareas = []

def agregar_tarea():
    tarea = input("Ingresa una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def ver_tareas():
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

def eliminar_tarea():
    ver_tareas()
    indice = int(input("Selecciona el número de la tarea que deseas eliminar: ")) - 1

    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea eliminada: {tarea_eliminada}")
    else:
        print("Índice fuera de rango. No se eliminó ninguna tarea.")

while True:
    print("\nGestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        ver_tareas()
    elif opcion == '3':
        eliminar_tarea()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
Paso 3: Ejecuta el archivo y gestiona tus tareas utilizando el gestor de tareas.

Este código crea un gestor de tareas que permite al usuario agregar, ver y eliminar tareas pendientes. Utiliza una lista para almacenar las tareas y funciones para realizar las operaciones de gestión de tareas. El programa se ejecuta en un bucle hasta que el usuario elige salir.