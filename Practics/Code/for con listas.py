# Lista para almacenar las ventas y nombres de los vendedores
ventas_diarias = []
nombres_vendedores = []

# Solicitar la cantidad de días a registrar
dias = int(input("Ingrese el número de días a registrar ventas: "))

# Recolectar datos del usuario
for dia in range(dias):
    nombre = input(f"Ingrese el nombre del vendedor para el día {dia + 1}: ")
    venta = float(input(f"Ingrese la venta del día {dia + 1}: "))
    nombres_vendedores.append(nombre)
    ventas_diarias.append(venta)

# Mostrar las ventas diarias y calcular el total de ventas
total_ventas = 0
print("\nVentas diarias:")
for i in range(len(ventas_diarias)):
    print(f"Día {i + 1} - Vendedor: {nombres_vendedores[i]}, Venta: ${ventas_diarias[i]:.2f}")
    total_ventas += ventas_diarias[i]
print("Total de ventas:", total_ventas)

# Determinar el vendedor con mayores ventas
max_venta = ventas_diarias[0]
mejor_vendedor = nombres_vendedores[0]
for i in range(1, len(ventas_diarias)):
    if ventas_diarias[i] > max_venta:
        max_venta = ventas_diarias[i]
        mejor_vendedor = nombres_vendedores[i]
print(f"El vendedor con mayores ventas es {mejor_vendedor} con una venta de ${max_venta:.2f}")

# Contar los días con ventas superiores a $1000
dias_ventas_altas = 0
for venta in ventas_diarias:
    if venta > 1000:
        dias_ventas_altas += 1
print("Días con ventas superiores a $1000:", dias_ventas_altas)

# Crear una lista con las ventas incrementadas en un 10%
ventas_incrementadas = []
for venta in ventas_diarias:
    ventas_incrementadas.append((venta * 10 / 100) + venta)
print("Ventas incrementadas en un 10%:", ventas_incrementadas)

# Filtrar las ventas menores a $500
ventas_bajas = []
for venta in ventas_diarias:
    if venta < 500:
        ventas_bajas.append(venta)
print("Ventas menores a $500:", ventas_bajas)
