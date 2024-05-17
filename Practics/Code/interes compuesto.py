def calcular_interes_compuesto(capital, tasa, años):
    monto_final = capital * (1 + tasa / 100) ** años
    return monto_final

try:
    capital_inicial = float(input("Ingresa el capital inicial: "))
    tasa_anual = float(input("Ingresa la tasa de interés anual (%): "))
    años = int(input("Ingresa el período de inversión en años: "))

    if capital_inicial < 0 or tasa_anual < 0 or años < 0:
        raise ValueError("Los valores no pueden ser negativos.")

    monto_total = calcular_interes_compuesto(capital_inicial, tasa_anual, años)
    print("El monto total después de", años, "años será de:", round(monto_total, 2))

except ValueError as e:
    print("Error:", e)
