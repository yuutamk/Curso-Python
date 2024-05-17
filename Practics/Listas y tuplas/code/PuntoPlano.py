import math

# Inicializa una lista para almacenar los puntos como tuplas (x, y).
puntos = []

def agregar_punto():
    x = float(input("Ingresa la coordenada x: "))
    y = float(input("Ingresa la coordenada y: "))
    punto = (x, y)
    puntos.append(punto)
    print("Punto agregado a la lista de puntos.")

def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

def encontrar_punto_cercano_o_alejado(alejado=True):
    if len(puntos) < 2:
        print("Se necesitan al menos dos puntos para realizar esta operación.")
        return

    punto_referencia = puntos[int(input("Ingresa el número del punto de referencia: "))]
    punto_resultado = None
    distancia_resultado = 0 if alejado else float("inf")

    for punto in puntos:
        if punto != punto_referencia:
            distancia = calcular_distancia(punto_referencia, punto)
            if (alejado and distancia > distancia_resultado) or (not alejado and distancia < distancia_resultado):
                distancia_resultado = distancia
                punto_resultado = punto

    tipo_operacion = "alejado" if alejado else "cercano"
    print(f"El punto más {tipo_operacion} al punto de referencia es {punto_resultado} con una distancia de {distancia_resultado:.2f} unidades.")

# Menú de opciones
while True:
    print("\nMenú:")
    print("1. Agregar un punto")
    print("2. Calcular distancia entre puntos")
    print("3. Encontrar punto más cercano al punto de referencia")
    print("4. Encontrar punto más alejado al punto de referencia")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        agregar_punto()
    elif opcion == "2":
        if len(puntos) < 2:
            print("Se necesitan al menos dos puntos para calcular la distancia.")
        else:
            punto1 = puntos[int(input("Ingresa el número del primer punto: "))]
            punto2 = puntos[int(input("Ingresa el número del segundo punto: "))]
            distancia = calcular_distancia(punto1, punto2)
            print(f"La distancia entre los puntos es {distancia:.2f} unidades.")
    elif opcion == "3":
        encontrar_punto_cercano_o_alejado(alejado=False)
    elif opcion == "4":
        encontrar_punto_cercano_o_alejado(alejado=True)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida del menú.")
