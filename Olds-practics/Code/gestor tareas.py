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
