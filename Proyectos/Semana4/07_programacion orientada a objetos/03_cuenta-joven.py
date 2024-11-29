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

# Clase derivada CuentaJoven
class CuentaJoven(Cuenta):
    def __init__(self, titular="", cantidad=0.0, bonificacion=0.0, edad_titular=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        self.__edad_titular = edad_titular

    # Getters y Setters
    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_edad_titular(self):
        return self.__edad_titular

    def set_edad_titular(self, edad):
        self.__edad_titular = edad

    # Método para verificar si el titular es válido
    def es_titular_valido(self):
        return 18 <= self.__edad_titular < 25

    # Redefinición del método mostrar
    def mostrar(self):
        print(f"Cuenta Joven")
        print(f"Titular: {self.get_titular()}, Cantidad: {self.get_cantidad():.2f}, Bonificación: {self.__bonificacion:.2f}%")

    # Redefinición del método retirar
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero: El titular no es válido para una Cuenta Joven.")

# Ejemplo de uso
cuenta_joven = CuentaJoven("Ana", 200.0, 10.0, 22)
cuenta_joven.mostrar()  # Muestra: Cuenta Joven con la bonificación
# Muestra: Titular: Ana, Cantidad: 200.00, Bonificación: 10.00%

cuenta_joven.ingresar(100)
cuenta_joven.mostrar()  # Muestra: Titular: Ana, Cantidad: 300.00, Bonificación: 10.00%

cuenta_joven.retirar(50)
cuenta_joven.mostrar()  # Muestra: Titular: Ana, Cantidad: 250.00, Bonificación: 10.00%

cuenta_joven.set_edad_titular(26)
cuenta_joven.retirar(50)  # Muestra: No se puede retirar dinero: El titular no es válido para una Cuenta Joven.
