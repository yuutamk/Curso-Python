try:
    monto = float(input("Ingrese monto: "))
    interes = float(input("Ingrese interés mensual (%): "))
    
    # Verificar si el interés es mayor al 30%
    if interes > 30:
        print("El interés ingresado es incorrecto. Debe ser 30% o menos.")
    else:
        # Calcular el monto final con el interés aplicado
        monto_final = monto * (1 + interes / 100)
        print("Monto final: %08.2f" % monto_final)
        
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número válido.")

print("FIN")
