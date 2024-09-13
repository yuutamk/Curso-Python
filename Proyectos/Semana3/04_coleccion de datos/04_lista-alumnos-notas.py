# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas.
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos
# y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá
# pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

# Diccionario para almacenar los nombres de los alumnos y sus notas.
alumnos = {}

# Pedir la cantidad de alumnos que vamos a introducir.
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar: "))

# Bucle para introducir los datos de cada alumno.
for _ in range(cantidad):
    # Pedir el nombre del alumno y comprobar si ya existe en el diccionario.
    while True:
        alumno = input("Nombre del alumno: ")
        if alumno in alumnos:
            print("Alumno ya existe. Introduce un nombre diferente.")
        else:
            break
    
    # Lista para almacenar las notas del alumno.
    notas = []
    
    # Pedir las notas del alumno hasta que se introduzca un número negativo.
    while True:
        nota = float(input("Dame una nota del alumno (negativo para terminar): "))
        if nota < 0:
            break
        notas.append(nota)
    
    # Guardar las notas en el diccionario.
    alumnos[alumno] = notas

# Mostrar la lista de alumnos y la nota media obtenida por cada uno.
for alumno, notas in alumnos.items():
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"{alumno} ha sacado de nota media {media:.2f}")
    else:
        print(f"{alumno} no tiene notas registradas.")
