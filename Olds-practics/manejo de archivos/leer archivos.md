### Paso 1: Leer un Archivo Línea por Línea

El primer bloque de código muestra cómo leer un archivo línea por línea en Python. Usamos la declaración `with` para abrir el archivo `caperucita.txt` en modo lectura (`'r'`). La declaración `with` garantiza que el archivo se cierre automáticamente después de que se haya completado el bloque de código.

```python
# Leer un archivo línea por línea
with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
```

**Explicación**:
- **`with open('caperucita.txt', 'r') as file`**: Abre el archivo `caperucita.txt` en modo lectura. `open()` devuelve un objeto de archivo que se asigna a la variable `file`.
- **`for lineas in file`**: Itera sobre cada línea del archivo. Cada línea se trata como una cadena de texto.
- **`print(lineas.strip())`**: Imprime cada línea eliminando los caracteres de espacio en blanco al principio y al final de la línea con `strip()`. Esto ayuda a limpiar el texto al mostrarlo en la consola.


### Paso 2: Leer Todas las Líneas en una Lista

En este paso, se leen todas las líneas del archivo y se almacenan en una lista utilizando el método `readlines()`.

```python
# Leer todas las líneas en una lista
with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```

**Explicación**:
- **`with open('caperucita.txt', 'r') as file`**: Abre el archivo en modo lectura.
- **`file.readlines()`**: Lee todas las líneas del archivo y las almacena en una lista. Cada elemento de la lista es una línea del archivo, incluyendo los caracteres de nueva línea (`\n`).
- **`print(lines)`**: Muestra la lista completa de líneas en la consola.

### Paso 3: Añadir Texto al Final del Archivo

Este bloque de código muestra cómo añadir texto al final de un archivo sin sobrescribir el contenido existente, usando el modo de apertura `'a'` (apéndice).

```python
# Añadir texto
with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")
```

**Explicación**:
- **`with open('caperucita.txt', 'a') as file`**: Abre el archivo en modo apéndice (`'a'`), lo que significa que el texto se añadirá al final del archivo sin borrar el contenido existente.
- **`file.write("\n\nBy:ChatGPT")`**: Escribe `"\n\nBy:ChatGPT"` al final del archivo. El `\n\n` agrega dos líneas en blanco antes del texto, facilitando la separación visual.

### Paso 4: Sobreescribir el Contenido del Archivo

Finalmente, este bloque de código muestra cómo sobrescribir todo el contenido de un archivo, usando el modo `'w'`.

```python
# Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")
```

**Explicación**:
- **`with open('caperucita.txt', 'w') as file`**: Abre el archivo en modo escritura (`'w'`). Este modo borra todo el contenido existente del archivo y luego escribe el nuevo contenido.
- **`file.write("\n\nBy:ChatGPT")`**: Escribe el texto `"\n\nBy:ChatGPT"` en el archivo. Debido al modo `'w'`, esto reemplaza todo el contenido anterior del archivo con este nuevo texto.

### Resumen

- **Modo `'r'` (lectura)**: Abre el archivo para leer. Si el archivo no existe, se genera un error.
- **Modo `'a'` (apéndice)**: Abre el archivo para añadir contenido al final. Si el archivo no existe, se crea uno nuevo.
- **Modo `'w'` (escritura)**: Abre el archivo para escribir. Si el archivo existe, se borra su contenido previo; si no existe, se crea uno nuevo.

Estos modos permiten una gran flexibilidad al trabajar con archivos en Python, desde la simple lectura hasta la manipulación avanzada de contenido, ya sea añadiendo o sobrescribiendo texto.