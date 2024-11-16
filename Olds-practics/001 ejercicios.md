1. **Operaciones Matemáticas:**

   - Paso 1: Abre un nuevo archivo llamado "operaciones.py".
   - Paso 2: Escribe el código siguiente para realizar operaciones matemáticas:
     ```python
     num1 = 10
     num2 = 5
     suma = num1 + num2
     resta = num1 - num2
     multiplicacion = num1 * num2
     division = num1 / num2

     print("Suma:", suma)
     print("Resta:", resta)
     print("Multiplicación:", multiplicacion)
     print("División:", division)
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías ver los resultados de las operaciones matemáticas en la pantalla.

2. **Verificar Paridad de Números:**

   - Paso 1: Crea un nuevo archivo llamado "paridad.py".
   - Paso 2: Escribe el código siguiente para verificar si un número es par o impar:
     ```python
     numero = 7

     if numero % 2 == 0:
         print("El número es par.")
     else:
         print("El número es impar.")
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías ver un mensaje que indica si el número es par o impar.

3. **Saludo Personalizado con Función:**

   - Paso 1: Crea un nuevo archivo llamado "saludo_personalizado.py".
   - Paso 2: Escribe una función para saludar con un nombre personalizado:
     ```python
     def saludar(nombre):
         mensaje = "¡Hola, " + nombre + "!"
         return mensaje

     nombre_usuario = "Alice"
     saludo = saludar(nombre_usuario)
     print(saludo)
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías ver un saludo personalizado para el nombre especificado.

4. **Calculadora de Cuadrados con Función:**

   - Paso 1: Crea un nuevo archivo llamado "calcular_cuadrado.py".
   - Paso 2: Escribe una función para calcular el cuadrado de un número:
     ```python
     def calcular_cuadrado(numero):
         cuadrado = numero * numero
         return cuadrado

     numero_ingresado = 5
     resultado = calcular_cuadrado(numero_ingresado)
     print("El cuadrado de", numero_ingresado, "es", resultado)
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías obtener el cuadrado del número especificado.

5. **Bucle For para Contar:**

   - Paso 1: Crea un nuevo archivo llamado "bucle_for.py".
   - Paso 2: Escribe un bucle for para contar del 1 al 5:
     ```python
     for numero in range(1, 6):
         print("Número:", numero)
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías ver los números del 1 al 5 impresos en la pantalla.

6. **Bucle While para Adivinar un Número:**

   - Paso 1: Crea un nuevo archivo llamado "adivina_numero.py".
   - Paso 2: Escribe un bucle while para adivinar un número secreto:
     ```python
     numero_secreto = 7
     intentos = 0

     while True:
         intento = int(input("Adivina el número secreto: "))
         intentos += 1

         if intento == numero_secreto:
             print("¡Correcto! ¡Lo adivinaste en", intentos, "intentos!")
             break
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías poder adivinar el número secreto.

7. **Importar y Usar el Módulo "math":**

   - Paso 1: Crea un nuevo archivo llamado "usar_math.py".
   - Paso 2: Escribe el código siguiente para utilizar funciones del módulo "math":
     ```python
     import math

     numero = 25
     raiz = math.sqrt(numero)
     print("La raíz cuadrada de", numero, "es", raiz)

     angulo = 45
     seno = math.sin(math.radians(angulo))
     print("El seno de", angulo, "grados es", seno)
     ```
   - Paso 3: Guarda el archivo y ejecútalo. Deberías ver los cálculos realizados utilizando el módulo "math".

8. **Crear un Módulo Personalizado:**

   - Paso 1: Crea un archivo llamado "mi_modulo.py" con el contenido del módulo personalizado mencionado en el texto.
   - Paso 2: Crea un nuevo archivo llamado "usar_mi_modulo.py".
   - Paso 3: Escribe el código siguiente para importar y utilizar funciones del módulo personalizado:
     ```python
     import mi_modulo

     nombre = "Alice"
     saludo = mi_modulo.saludar(nombre)
     print(saludo)

     numero = 5
     resultado = mi_modulo.doble(numero)
     print("El doble de", numero, "es", resultado)
     ```


   - Paso 4: Guarda ambos archivos y ejecuta "usar_mi_modulo.py". Deberías ver los resultados de las funciones del módulo personalizado.

9. **Manejo de Excepciones:**

    - Paso 1: Crea un nuevo archivo llamado "manejo_excepciones.py".
    - Paso 2: Escribe el código siguiente para manejar una excepción:
      ```python
      try:
          numero = int(input("Ingresa un número: "))
          resultado = 10 / numero
          print("El resultado es:", resultado)
      except ZeroDivisionError:
          print("Error: No puedes dividir por cero.")
      except ValueError:
          print("Error: Debes ingresar un número válido.")
      ```
    - Paso 3: Guarda el archivo y ejecútalo. Prueba ingresar diferentes valores para ver cómo se manejan las excepciones.

Estas prácticas te ayudarán a comenzar a programar en Python y a comprender los conceptos fundamentales mencionados en el texto principal.