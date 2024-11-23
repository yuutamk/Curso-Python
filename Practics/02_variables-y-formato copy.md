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
2. Crea una carpeta nueva llamada `AgeCalculator`.  
3. Abre la carpeta en VS Code desde **Archivo > Abrir Carpeta**.  
4. Crea un archivo llamado `age_calculator.py`:  
   - Haz clic en **Archivo > Nuevo Archivo**.  
   - Guárdalo como `age_calculator.py`.  

---

#### **Paso 3: Escribe el código base**  

Copia el siguiente código en tu archivo `age_calculator.py`:  

```python
# Código base para calcular tu edad futura
name = 'Juana'
print(name)  # Muestra el nombre en la consola

age = '10'
print(age)  # Muestra la edad actual en la consola

# Aquí completaremos el código 👇
template = f"---"
print(template)
```

Este será el punto de partida para tu ejercicio.  

---

#### **Paso 4: Resuelve el ejercicio**  

Ahora, tu desafío es completar el código para:  
1. **Convertir la edad (age) de texto a número.**  
2. **Calcular la edad dentro de 10 años.**  
3. **Crear un mensaje con un formato específico.**  
4. **Imprimir el mensaje en la consola.**  

El mensaje deberá tener este formato:  
```plaintext
Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años
```
Aquí tienes otros ejemplos:

Ejemplo 1:


    Input:
    name: 'Juan'
    age: '10'

    Output:
    Hola mi nombre es Juan, tengo 10 años y en 10 años tendré 20 años

Ejemplo 2:

    Input:
    name: Andrea
    age: 22

    Output:
    Hola mi nombre es Andreaasas, tengo 22 años y en 10 años tendré 32 años

Recuerda prestar atención a los espacios y mayúsculas, ya que son importantes para que tu respuesta sea correcta.

---



#### **Ejemplo de salida**  

Cuando ejecutes el código, deberías ver lo siguiente en la consola:  
```plaintext
Juana  
10  
Hola mi nombre es Juana, tengo 10 años y en 10 años tendré 20 años  
```

---

#### **¡Felicidades! 🎉**  

Has completado tu ejercicio en Python. Ahora puedes personalizar las variables `name` y `age` para probar con otros valores. ¡Sigue practicando y aprendiendo en tu Coding Playground! 🎈  

---

<details value="code">  
<summary>Abrir despues de 4 intentos</summary>  

```python
# Código para calcular tu edad futura
name = 'Juana'
print(name)  # Muestra el nombre en la consola

age = '10'
print(age)  # Muestra la edad actual en la consola

# Conversión de edad y cálculo
age_number = int(age)  # Convierte 'age' a un número
future_age = age_number + 10  # Calcula la edad en 10 años

# Mensaje dinámico
template = f"Hola mi nombre es {name}, tengo {age_number} años y en 10 años tendré {future_age} años"
print(template)  # Muestra el mensaje en la consola
```

</details>