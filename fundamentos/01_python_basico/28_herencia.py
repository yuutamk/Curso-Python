class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} no está disponible.")

    def estado(self):
        return self.disponible

    def get_price(self):
        return self.precio

class Auto(Vehículo):
    def start(self):
        if self.disponible:
            return f"El motor del coche {self.marca} está en marcha."
        else:
            return f"El coche {self.marca} no está disponible."

    def stop(self):
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido."
        else:
            return f"El coche {self.marca} no está disponible."


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos = []

    def comprar_auto(self, auto):
        if auto.estado():
            self.autos.append(auto)
            auto.vender()
        else:
            print(f"El auto {auto.marca} no está disponible.")

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_auto(self, auto):
        self.inventario.append(auto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_disponibles(self):
        for auto in self.inventario:
            if auto.estado():
                print(f"{auto.marca} {auto.modelo} está disponible por {auto.get_price()}.")


# Crear autos
auto1 = Auto("Toyota", "Corolla", 20000)
auto2 = Auto("Honda", "Civic", 22000)
auto3 = Auto("Ford", "Mustang", 30000)

# Crear cliente
cliente = Cliente("Carlos")

# Crear concesionaria
concesionaria = Concesionaria()
concesionaria.añadir_auto(auto1)
concesionaria.añadir_auto(auto2)
concesionaria.añadir_auto(auto3)
concesionaria.registrar_cliente(cliente)

# Mostrar autos disponibles
concesionaria.mostrar_disponibles()

# Comprar auto
cliente.comprar_auto(auto1)

# Mostrar autos disponibles después de la compra
concesionaria.mostrar_disponibles()  

