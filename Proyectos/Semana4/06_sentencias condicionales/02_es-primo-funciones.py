def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Solicitar al usuario la cantidad de números primos a mostrar
cantidad = int(input("Ingrese la cantidad de números primos que desea mostrar: "))

# Mostrar los N primeros números primos
primos = primeros_n_primos(cantidad)
print(f"Los primeros {cantidad} números primos son: {primos}")
