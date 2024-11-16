class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()

    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni) != 9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""

    def mostrar(self):
        return "Nombre: " + self.nombre + " - Edad: " + str(self.edad) + " - DNI: " + self.dni

    def esMayorDeEdad(self):
        return self.edad >= 18
