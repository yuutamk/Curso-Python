class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getters y Setters para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.isalpha():
            self._nombre = nombre
        else:
            print("Error: El nombre debe contener solo letras.")

    # Getters y Setters para edad
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:
            self._edad = edad
        else:
            print("Error: La edad debe ser un número entero entre 0 y 120.")

    # Getters y Setters para DNI
    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        if isinstance(dni, str) and dni.isdigit() and len(dni) == 8:
            self._dni = dni
        else:
            print("Error: El DNI debe ser un número de 8 dígitos.")

    # Método para mostrar la información de la persona
    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    # Método para verificar si la persona es mayor de edad
    def esMayorDeEdad(self):
        return self._edad >= 18


# Ejemplo de uso de la clase
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(25)
persona1.set_dni("12345678")

persona1.mostrar()

if persona1.esMayorDeEdad():
    print("La persona es mayor de edad.")
else:
    print("La persona no es mayor de edad.")
