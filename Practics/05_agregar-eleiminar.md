### **Manipulando listas en Python: Coding Playground**

¡Bienvenido/a al Coding Playground! En este ejercicio aprenderás a manipular listas en Python siguiendo una serie de pasos. 🚀

---

#### **Paso 1: Configura tu entorno**

Antes de comenzar, asegúrate de tener lo siguiente:  

1. **Python**: Descárgalo desde [python.org](https://www.python.org/). Durante la instalación, marca la opción **"Add Python to PATH"**.  
2. **Visual Studio Code (VS Code)**: Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/) y sigue las instrucciones.  

---

#### **Paso 2: Crea el archivo del ejercicio**

1. **Abre VS Code**.  
2. Crea una carpeta nueva llamada `ListManipulator`.  
3. Abre la carpeta en VS Code desde **Archivo > Abrir Carpeta**.  
4. Crea un archivo llamado `list_manipulation.py`:  
   - Haz clic en **Archivo > Nuevo Archivo**.  
   - Guárdalo como `list_manipulation.py`.  

---

#### **Paso 3: Escribe el código base**

Copia el siguiente código en tu archivo `list_manipulation.py`:

```python
# Código base para manipular listas
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

print(letters)
```

Este será el punto de partida para tu ejercicio.

---

#### **Paso 4: Resuelve el desafío**

Ahora, tu reto es realizar las siguientes operaciones en orden:

1. **Agregar la letra G al final de la lista.**  
   Usa un método adecuado para agregar elementos al final de una lista.  
2. **Reemplazar la letra en la posición 0 con la letra Z.**  
   Recuerda que los índices comienzan desde 0.  
3. **Eliminar la letra C de la lista.**  
   Elimina la primera aparición de un elemento específico.  
4. **Imprimir la lista resultante al revés.**  
   Utiliza un método para invertir el orden de los elementos.

#### **Ejemplo**

    Input: ["A", "B", "C", "D", "E", "F"]
    Output: ["G", "F", "E", "D", "B", "Z"]

---

#### **¡Felicidades! 🎉**

Has aprendido a manipular listas en Python utilizando métodos clave. Ahora puedes experimentar con otros valores en la lista para seguir practicando. ¡Sigue explorando y creando en tu Coding Playground! 🎈


<details value="code">  
<summary>Abrir despues de 4 intentos</summary>  

```python
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

letters.append('G')  # Agrega la letra G al final
letters[0] = 'Z'     # Reemplaza la letra en la posición 0 con Z
letters.remove('C')  # Elimina la letra C de la lista
letters.reverse()    # Invierte el orden de los elementos
print(letters)       # Salida: ['G', 'F', 'E', 'D', 'B', 'Z']

```

</details>