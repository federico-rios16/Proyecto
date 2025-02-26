import mysql.connector
import csv
from validacion import validar_datos_usuario
from logger import log_error

def crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        email (str): Email del usuario.
        contrasena (str): Contraseña del usuario.
        telefono (str): Teléfono del usuario.
        direccion (str): Dirección del usuario.
        fecha_nacimiento (str): Fecha de nacimiento del usuario.
        dni (str): DNI del usuario.

    Raises:
        ValueError: Si los datos del usuario no son válidos.
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        validar_datos_usuario(nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni)
        cursor = conexion.cursor()
        sql = """
        INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni)
        cursor.execute(sql, values)
        conexion.commit()
        print("Usuario creado exitosamente")
    except mysql.connector.Error as error:
        log_error(f"Error al crear usuario: {error}")
        print(f"Error al crear usuario: {error}")
    except ValueError as ve:
        log_error(f"Error de validación: {ve}")
        print(f"Error de validación: {ve}")

def leer_usuarios(conexion):
    """
    Lee y muestra todos los usuarios de la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)
    except mysql.connector.Error as error:
        log_error(f"Error al leer usuarios: {error}")
        print(f"Error al leer usuarios: {error}")

def mostrar_tablas(conexion):
    """
    Muestra todas las tablas en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
    except mysql.connector.Error as error:
        log_error(f"Error al mostrar tablas: {error}")
        print(f"Error al mostrar tablas: {error}")

def actualizar_usuario(conexion, usuario_id, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
    """
    Actualiza la información de un usuario existente en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        usuario_id (int): ID del usuario a actualizar.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        email (str): Email del usuario.
        contrasena (str): Contraseña del usuario.
        telefono (str): Teléfono del usuario.
        direccion (str): Dirección del usuario.
        fecha_nacimiento (str): Fecha de nacimiento del usuario.
        dni (str): DNI del usuario.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        sql = """
        UPDATE usuarios
        SET nombre = %s, apellido = %s, email = %s, contrasena = %s, telefono = %s, direccion = %s, fecha_nacimiento = %s, dni = %s
        WHERE id = %s
        """
        values = (nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni, usuario_id)
        cursor.execute(sql, values)
        conexion.commit()
        print("Usuario actualizado exitosamente")
    except mysql.connector.Error as error:
        log_error(f"Error al actualizar usuario: {error}")
        print(f"Error al actualizar usuario: {error}")

def eliminar_usuario(conexion, usuario_id):
    """
    Elimina un usuario de la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        usuario_id (int): ID del usuario a eliminar.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuario_id,))
        conexion.commit()
        print("Usuario eliminado exitosamente")
    except mysql.connector.Error as error:
        log_error(f"Error al eliminar usuario: {error}")
        print(f"Error al eliminar usuario: {error}")

def buscar_usuario_por_nombre(conexion, nombre):
    """
    Busca usuarios por nombre en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        nombre (str): Nombre del usuario a buscar.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        usuarios = cursor.fetchall()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print("No se encontraron usuarios con ese nombre")
    except mysql.connector.Error as error:
        log_error(f"Error al buscar usuario: {error}")
        print(f"Error al buscar usuario: {error}")

def listar_usuarios_paginados(conexion, pagina, tamano_pagina):
    """
    Lista usuarios con paginación.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        pagina (int): Número de la página.
        tamano_pagina (int): Tamaño de la página.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        offset = (pagina - 1) * tamano_pagina
        sql = "SELECT * FROM usuarios LIMIT %s OFFSET %s"
        cursor.execute(sql, (tamano_pagina, offset))
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
    except mysql.connector.Error as error:
        log_error(f"Error al listar usuarios: {error}")
        print(f"Error al listar usuarios: {error}")

def exportar_usuarios_a_csv(conexion, archivo_csv):
    """
    Exporta usuarios a un archivo CSV.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        archivo_csv (str): Ruta del archivo CSV.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
        IOError: Si ocurre un error al escribir el archivo CSV.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cursor.description])  # Escribir encabezados
            writer.writerows(usuarios)
        print(f"Usuarios exportados exitosamente a {archivo_csv}")
    except mysql.connector.Error as error:
        log_error(f"Error al exportar usuarios: {error}")
        print(f"Error al exportar usuarios: {error}")
    except IOError as io_error:
        log_error(f"Error al escribir el archivo CSV: {io_error}")
        print(f"Error al escribir el archivo CSV: {io_error}")

def importar_usuarios_desde_csv(conexion, archivo_csv):
    """
    Importa usuarios desde un archivo CSV.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        archivo_csv (str): Ruta del archivo CSV.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
        IOError: Si ocurre un error al leer el archivo CSV.
    """
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar encabezados
            for row in reader:
                crear_usuario(conexion, *row)
        print(f"Usuarios importados exitosamente desde {archivo_csv}")
    except mysql.connector.Error as error:
        log_error(f"Error al importar usuarios: {error}")
        print(f"Error al importar usuarios: {error}")
    except IOError as io_error:
        log_error(f"Error al leer el archivo CSV: {io_error}")
        print(f"Error al leer el archivo CSV: {io_error}")