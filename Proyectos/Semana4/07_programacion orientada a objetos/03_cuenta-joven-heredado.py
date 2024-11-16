# Para heredar renombra el archivo 02_cuenta-decoradores.py a cuenta_decoradores.py
from cuenta_decoradores import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        return (f"Cuenta Joven\nTitular: {self.titular} - "
                f"Cantidad: {self.cantidad} - Bonificación: {self.bonificacion}%")

    def esTitularValido(self):
        # Asumiendo que titular tiene los métodos 'edad' y 'esMayorDeEdad()'
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()

    def retirar(self, cantidad):
        if not self.esTitularValido():
            print("No puedes retirar el dinero. Titular no válido.")
        elif cantidad > 0:
            super().retirar(cantidad)
