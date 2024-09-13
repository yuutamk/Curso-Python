# Solicitar al usuario la cantidad de números primos a mostrar
cantidad = int(input("Ingrese la cantidad de números primos que desea mostrar: "))

primos = []
numero = 2  # Comenzamos a buscar primos desde el número 2

while len(primos) < cantidad:
    es_primo = True
    
    # Verificar si el número actual es primo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        primos.append(numero)
    
    numero += 1

# Mostrar los N primeros números primos
print(f"Los primeros {cantidad} números primos son: {primos}")
