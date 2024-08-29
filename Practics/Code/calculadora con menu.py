import time

while True:
    print("Menú de Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    if opcion == '5':
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
        elif opcion == '2':
            resultado = num1 - num2
        elif opcion == '3':
            resultado = num1 * num2
        elif opcion == '4':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 / num2
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

        print("Resultado:", resultado , "\n")

        time.sleep(0.5)

    except ValueError:
        print("Error: Debes ingresar números válidos.")
    except ZeroDivisionError as e:
        print("Error:", e)
