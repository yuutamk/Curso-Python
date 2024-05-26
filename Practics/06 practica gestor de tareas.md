## Gestor de tareas
#### Paso 1: Creación del archivo "gestor_de_tareas.py".

#### Paso 2: Definición de funciones para el gestor de tareas:

- Se crea una lista vacía llamada `tareas` para almacenar las tareas pendientes.

```python
tareas = []
```

- Se define la función `agregar_tarea()` para permitir al usuario agregar una nueva tarea.

```python
def agregar_tarea():
    tarea = input("Ingresa una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")
```

- Se define la función `ver_tareas()` para mostrar las tareas pendientes.

```python
def ver_tareas():
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")
```

- Se define la función `eliminar_tarea()` para permitir al usuario eliminar una tarea específica.

```python
def eliminar_tarea():
    ver_tareas()
    indice = int(input("Selecciona el número de la tarea que deseas eliminar: ")) - 1

    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea eliminada: {tarea_eliminada}")
    else:
        print("Índice fuera de rango. No se eliminó ninguna tarea.")
```

#### Paso 2 (continuación): Bucle principal del gestor de tareas:

- Se inicia un bucle `while` que continúa hasta que el usuario elija salir (`opcion == '4'`).

```python
while True:
```

- Se muestra el menú principal del gestor de tareas con opciones para agregar, ver, eliminar tareas y salir.

```python
    print("\nGestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")
```

#### Paso 2 (continuación): Manejo de las opciones del usuario:

- Si el usuario elige la opción '1', se llama a la función `agregar_tarea()`.

```python
    if opcion == '1':
        agregar_tarea()
```

- Si el usuario elige la opción '2', se llama a la función `ver_tareas()` para mostrar las tareas pendientes.

```python
    elif opcion == '2':
        ver_tareas()
```

- Si el usuario elige la opción '3', se llama a la función `eliminar_tarea()` para permitir al usuario eliminar una tarea específica.

```python
    elif opcion == '3':
        eliminar_tarea()
```

- Si el usuario elige la opción '4', se rompe el bucle `while` para salir del programa.

```python
    elif opcion == '4':
        break
```

- Si el usuario ingresa una opción no válida, se muestra un mensaje de error.

```python
    else:
        print("Opción no válida. Inténtalo de nuevo.")
```

#### Paso 3: Ejecuta el archivo y gestiona tus tareas utilizando el gestor de tareas.

Este código crea un gestor de tareas que permite al usuario agregar, ver y eliminar tareas pendientes. Utiliza una lista para almacenar las tareas y funciones para realizar las operaciones de gestión de tareas. El programa se ejecuta en un bucle hasta que el usuario elija salir.