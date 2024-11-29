class Cuenta:
    def __init__(self, titular="", cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    # Getters y Setters
    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    # Métodos para mostrar, ingresar y retirar dinero
    def mostrar(self):
        print(f"Titular: {self.__titular}, Cantidad: {self.__cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("No se pueden ingresar cantidades negativas.")

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Ejemplo de uso
cuenta = Cuenta("Juan", 100.0)
cuenta.mostrar()  # Muestra: Titular: Juan, Cantidad: 100.00

cuenta.ingresar(50)
cuenta.mostrar()  # Muestra: Titular: Juan, Cantidad: 150.00

cuenta.retirar(200)
cuenta.mostrar()  # Muestra: Titular: Juan, Cantidad: -50.00

cuenta.ingresar(-30)  # Muestra: No se pueden ingresar cantidades negativas.
