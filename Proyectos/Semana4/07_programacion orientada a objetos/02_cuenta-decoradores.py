class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Cuenta\nTitular: {self.titular} - Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("No se pueden ingresar cantidades negativas.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("No se pueden retirar cantidades negativas.")

# Ejemplo de uso
cuenta = Cuenta("Juan", 100.0)
cuenta.mostrar()  # Muestra: Titular: Juan - Cantidad: 100.00

cuenta.ingresar(50)
cuenta.mostrar()  # Muestra: Titular: Juan - Cantidad: 150.00

cuenta.retirar(200)
cuenta.mostrar()  # Muestra: Titular: Juan - Cantidad: -50.00

cuenta.ingresar(-30)  # Muestra: No se pueden ingresar cantidades negativas.
