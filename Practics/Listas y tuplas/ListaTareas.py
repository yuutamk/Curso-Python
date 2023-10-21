# Inicializa una lista para almacenar las tareas.
tareas = []
# Inicializa un diccionario para rastrear el estado de las tareas (completadas o no).
estado_tareas = {}

# Función para agregar una tarea.
def agregar_tarea():
    tarea = input("Escribe la tarea que deseas agregar: ")
    tareas.append(tarea)
    estado_tareas[tarea] = False  # Inicialmente, la tarea no está completada.

# Función para marcar una tarea como completada.
def marcar_completada():
    tarea = input("Ingresa la tarea completada: ")
    if tarea in estado_tareas:
        estado_tareas[tarea] = True
        print("Tarea marcada como completada.")
    else:
        print("Tarea no encontrada en la lista.")

# Función para eliminar una tarea.
def eliminar_tarea():
    tarea = input("Ingresa la tarea a eliminar: ")
    if tarea in estado_tareas:
        tareas.remove(tarea)
        del estado_tareas[tarea]
        print("Tarea eliminada.")
    else:
        print("Tarea no encontrada en la lista.")

# Función para listar todas las tareas.
def listar_tareas():
    if len(tareas) == 0:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas):
            estado = "Completada" if estado_tareas[tarea] else "Pendiente"
            print(f"{i + 1}. {tarea} ({estado})")

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

