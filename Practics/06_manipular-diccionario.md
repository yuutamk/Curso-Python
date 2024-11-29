### **Manipulando Diccionarios en Python: Coding Playground**

¡Bienvenido/a al Coding Playground! Hoy aprenderás a trabajar con diccionarios en Python mediante operaciones básicas como agregar, actualizar, eliminar elementos, y listar llaves y valores. 🚀

---

#### **Paso 1: Configura tu entorno**
Antes de empezar, asegúrate de tener lo siguiente:

1. **Python**: Descárgalo desde [python.org](https://www.python.org/). Durante la instalación, marca la opción **"Add Python to PATH"**.
2. **Visual Studio Code (VS Code)**: Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/) y sigue las instrucciones.

---

#### **Paso 2: Crea el archivo del ejercicio**

1. **Abre VS Code**.
2. Crea una carpeta nueva llamada `person_dict`.
3. Abre la carpeta en VS Code desde **Archivo > Abrir Carpeta**.
4. Crea un archivo llamado `manipula_diccionario.py`:
   - Haz clic en **Archivo > Nuevo Archivo**.
   - Guárdalo como `manipula_diccionario.py`.

---

#### **Paso 3: Escribe el código base**

Copia el siguiente código en tu archivo `manipula_diccionario.py`:

```python
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
```

Este será el punto de partida para tu ejercicio.

---

#### **Paso 4: Resuelve el ejercicio**

En este desafío, se te proporcionará un diccionario llamado `person` que contiene información sobre una persona. Tu reto es realizar las siguientes operaciones en orden:

1. Agregar un nuevo elemento al diccionario con la llave `"twitter"` y el valor `"@nicobytes"`.
2. Actualizar el valor del elemento con la llave `"name"` con el valor `"Felipe"`.
3. Eliminar el elemento del diccionario con la llave `"age"`.
4. Imprimir una lista con las llaves del diccionario.
5. Imprimir una lista con los valores del diccionario.

A continuación se muestran ejemplos de cómo debería funcionar tu solución:

Ejemplo:

```python
Input:
person = {
    "name": "Nicolas",
    "lastName": "Molina",
    "age": 29
}

Output:
["name", "lastName", "twitter"]
["Felipe", "Molina", "@nicobytes"]
```

Recuerda prestar atención al orden de las operaciones y utilizar las funciones y métodos adecuados para cada tarea.

---

#### **¡Felicidades! 🎉**

Has completado tu ejercicio de manipulación de diccionarios en Python. Ahora puedes personalizar los valores en el diccionario `person` para probar con otros datos. ¡Sigue practicando y aprendiendo en tu Coding Playground! 🎈

---

<details value="code">
<summary>Solución propuesta</summary>

```python
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇

person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
del person["age"]

print(list(person.keys()))
print(list(person.values()))
```

</details>