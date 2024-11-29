### **Calculando tu edad futura en Python: Coding Playground**  

¡Bienvenido/a al Coding Playground! Hoy aprenderás a trabajar con variables, realizar cálculos básicos y crear un mensaje dinámico que incluye tu edad futura. 🚀  

---

#### **Paso 1: Configura tu entorno**  
Antes de empezar, asegúrate de tener lo siguiente:  

1. **Python**: Descárgalo desde [python.org](https://www.python.org/). Durante la instalación, marca la opción **"Add Python to PATH"**.  
2. **Visual Studio Code (VS Code)**: Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/) y sigue las instrucciones.  

---

#### **Paso 2: Crea el archivo del ejercicio**  

1. **Abre VS Code**.  
2. Crea una carpeta nueva llamada `numPar`.  
3. Abre la carpeta en VS Code desde **Archivo > Abrir Carpeta**.  
4. Crea un archivo llamado `numero_par.py`:  
   - Haz clic en **Archivo > Nuevo Archivo**.  
   - Guárdalo como `numero_par.py`.  

---

#### **Paso 3: Escribe el código base**  

Copia el siguiente código en tu archivo `nuemro_par.py`:  

```python
number = '10'
print(number)

# Escribe tu solución 👇
```

Este será el punto de partida para tu ejercicio.  

---

#### **Paso 4: Resuelve el ejercicio**  

En este desafío, tienes una variable llamada number como string, tu reto es determinar si ese string es un número par o impar. Para hacer esta validación, debes transformar el string a number y luego realizar una condicional que compruebe si el número es divisible por dos. Si lo es, significa que el número es par y debes imprimir el mensaje Es par. Si no lo es, significa que el número es impar y debes imprimir el mensaje Es impar.

A continuación se muestran ejemplos de cómo debería funcionar tu solución:

Ejemplo 1:

    Input: '2'
    Output: "Es par"

Ejemplo 2:

    Input: '3'
    Output: "Es impar"

Recuerda prestar atención a los espacios y mayúsculas del string como respuesta, ya que son importantes para que tu respuesta sea correcta.


---

#### **¡Felicidades! 🎉**  

Has completado tu ejercicio en Python. Ahora puedes personalizar las variables `name` y `age` para probar con otros valores. ¡Sigue practicando y aprendiendo en tu Coding Playground! 🎈  

---

<details value="code">  
<summary>Abrir despues de 4 intentos</summary>  

```python
number = '10'
print(number)

# Escribe tu solución 👇

if int(number) % 2 == 0:
    print('Es par')
else:
    print('Es impar')
```

</details>