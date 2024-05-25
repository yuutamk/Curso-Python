**Blog Creativo: Introducción a Bases de Datos en SQLite**

¡Bienvenidos, jóvenes programadores de 12 años, a un nuevo y emocionante viaje en el mundo de la programación! Hoy, vamos a explorar un tema fundamental que te ayudará a gestionar datos de una manera asombrosa: ¡las bases de datos en SQLite! No te preocupes si no entiendes qué es una base de datos o SQLite, ¡estoy aquí para explicártelo de una manera sencilla y creativa!

**¿Qué son las Bases de Datos?**

Imagina que eres el bibliotecario de una gran biblioteca. Tienes miles de libros, y cada uno tiene su propio lugar. Organizas estos libros en estantes, y cuando alguien busca un libro en particular, puedes encontrarlo rápidamente gracias a la organización. Las bases de datos son como esos estantes y carpetas virtuales para guardar información de manera ordenada.

SQLite es una pequeña pero potente biblioteca que te permite crear, gestionar y acceder a bases de datos en tus programas de Python. ¡Vamos a explorar cómo funciona de una manera divertida!

**Creando una Base de Datos con SQLite:**

En el mundo de la programación, una base de datos es como un cajón secreto lleno de información útil. Para empezar, primero necesitamos crear ese cajón. En SQLite, puedes hacerlo con solo unas pocas líneas de código:

```python
import sqlite3

# Conectémonos a una base de datos o créala si no existe
conn = sqlite3.connect('mi_base_de_datos.db')

# Creamos una "tabla" en la base de datos para almacenar datos
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')
```

En el código anterior, estamos conectándonos a una base de datos llamada 'mi_base_de_datos.db' y creando una tabla llamada 'estudiantes' con tres columnas: 'id', 'nombre' y 'edad'. La tabla es como una hoja de registro donde podemos guardar información sobre estudiantes.

**Añadir Datos a la Base de Datos:**

Ahora que tenemos nuestra tabla, es hora de llenarla con información. Imagina que eres un maestro y quieres registrar a tus estudiantes en la base de datos. Podemos hacerlo así:

```python
# Insertamos datos en la tabla
cursor.execute('INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)', ('Juan', 12))
cursor.execute('INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)', ('Maria', 11))

# Guardamos los cambios
conn.commit()
```

Hemos añadido dos estudiantes, Juan y Maria, a nuestra tabla. Puedes agregar tantos estudiantes como quieras, y SQLite los mantendrá organizados en tu base de datos.

**Consultar Datos en la Base de Datos:**

Ahora que hemos guardado datos, ¿cómo podemos encontrarlos cuando los necesitemos? SQLite nos permite hacer consultas para buscar información específica. Imagina que deseas encontrar la edad de Juan:

```python
# Consultamos la base de datos para encontrar la edad de Juan
cursor.execute('SELECT edad FROM estudiantes WHERE nombre = ?', ('Juan',))
edad_juan = cursor.fetchone()[0]
print(f'La edad de Juan es {edad_juan} años.')
```

Con esta consulta, estamos buscando la edad de un estudiante cuyo nombre es 'Juan'. SQLite nos devuelve el resultado y podemos imprimirlo en pantalla.

**Cerrando el Cajón:**

Cuando termines de trabajar con tu base de datos, asegúrate de cerrarla correctamente:

```python
# Cerramos la conexión a la base de datos
conn.close()
```

Esto es como cerrar un cajón después de usarlo. ¡Asegúrate de hacerlo para mantener tus datos seguros y ordenados!

¡Espero que esta introducción a las bases de datos en SQLite haya sido emocionante y comprensible para ti! Con SQLite, puedes almacenar y acceder a información de manera eficiente en tus proyectos de programación. ¿Por qué no intentas crear tu propia base de datos y explorar más? ¡Diviértete programando!