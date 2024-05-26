import pandas as pd

class ManejadorDatos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.dataframe = pd.DataFrame()

    def cargar_datos(self):
        self.dataframe = pd.read_csv(self.nombre_archivo)

    def mostrar_datos(self):
        print(self.dataframe)

def main():
    nombre_archivo = 'datos.csv'  # Nombre del archivo de datos
    manejador = ManejadorDatos(nombre_archivo)
    manejador.cargar_datos()

    while True:
        print("\nOpciones:")
        print("1. Mostrar datos")
        print("2. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            manejador.mostrar_datos()
        elif opcion == 2:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
