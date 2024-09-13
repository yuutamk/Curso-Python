# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
# hasta que seleccionamos la opción de "Salir".

while True:
    # Mostrar menú
    print("Menú de recomendaciones")
    print(" 1. Literatura")
    print(" 2. Cine")
    print(" 3. Música")
    print(" 4. Videojuegos")
    print(" 5. Salir")
    
    # Ingresar una opción
    opcion = input("Elija una opción (1-5): ")
    
    # Verificar que la opción ingresada sea un número
    if opcion.isdigit():
        opcion = int(opcion)
        
        # Procesar esa opción
        if opcion == 1:
            print("Lecturas recomendables:")
            print(" + Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)")
            print(" + El juego de Ender (Orson Scott Card)")
            print(" + El sueño de los héroes (Adolfo Bioy Casares)")
        elif opcion == 2:
            print("Películas recomendables:")
            print(" + Matrix (1999)")
            print(" + El último samuray (2003)")
            print(" + Cars (2006)")
        elif opcion == 3:
            print("Discos recomendables:")
            print(" + Despedazado por mil partes (La Renga, 1996)")
            print(" + Búfalo (La Mississippi, 2008)")
            print(" + Gaia (Mago de Oz, 2003)")
        elif opcion == 4:
            print("Videojuegos clásicos recomendables:")
            print(" + Día del tentáculo (LucasArts, 1993)")
            print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
            print(" + Death Rally (Remedy/Apogee, 1996)")
        elif opcion == 5:
            print("Gracias, vuelva pronto")
            break
        else:
            print("Opción no válida, por favor elija una opción del 1 al 5.")
    else:
        print("Entrada inválida, por favor ingrese un número entre 1 y 5.")

print("FIN")
    