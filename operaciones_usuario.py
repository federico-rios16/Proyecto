import mysql.connector
import csv
from validacion import validar_datos_usuario
from logger import log_error
from mysql.connector import Error

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
        cursor = conexion.cursor()
        query = """
        INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni))
        conexion.commit()
        return True
    except Error as error:
        print(f"Error al crear usuario: {error}")
        return False

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
        usuarios = cursor.fetchall()
        return usuarios if usuarios else []
    except Error as error:
        print(f"Error al leer usuarios: {error}")
        return []

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
        for tabla in tablas:
            print(tabla)
    except Error as error:
        print(f"Error al mostrar tablas: {error}")

def actualizar_usuario(conexion, id, nombre, apellido, email, telefono, direccion, fecha_nacimiento, dni):
    """
    Actualiza la información de un usuario existente en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        usuario_id (int): ID del usuario a actualizar.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        email (str): Email del usuario.
        telefono (str): Teléfono del usuario.
        direccion (str): Dirección del usuario.
        fecha_nacimiento (str): Fecha de nacimiento del usuario.
        dni (str): DNI del usuario.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        query = """
        UPDATE usuarios
        SET nombre = %s, apellido = %s, email = %s, telefono = %s, direccion = %s, fecha_nacimiento = %s, dni = %s
        WHERE id_usuario = %s
        """
        cursor.execute(query, (nombre, apellido, email, telefono, direccion, fecha_nacimiento, dni, id))
        conexion.commit()
        return True
    except mysql.connector.Error as error:
        print(f"Error al actualizar usuario: {error}")
        return False

def eliminar_usuario(conexion, id):
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
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        return True
    except mysql.connector.Error as error:
        print(f"Error al eliminar usuario: {error}")
        return False

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
        cursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (nombre,))
        usuario = cursor.fetchone()
        if usuario:
            print(usuario)
        else:
            print("Usuario no encontrado")
    except Error as error:
        print(f"Error al buscar usuario: {error}")

def listar_usuarios_paginados(conexion, page_num, page_size):
    """
    Lista usuarios con paginación.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): Conexión a la base de datos.
        pagina (int): Número de la página.
        cantidad (int): Tamaño de la página.

    Raises:
        mysql.connector.Error: Si ocurre un error al interactuar con la base de datos.
    """
    try:
        cursor = conexion.cursor()
        offset = (page_num - 1) * page_size
        query = "SELECT * FROM usuarios LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        usuarios = cursor.fetchall()
        return usuarios
    except Error as error:
        print(f"Error al listar usuarios paginados: {error}")
        return []

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
        with open(archivo_csv, 'w') as file:
            for usuario in usuarios:
                file.write(','.join(map(str, usuario)) + '\n')
        print(f"Usuarios exportados a {archivo_csv}")
    except Error as error:
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
        with open(archivo_csv, 'r') as file:
            for linea in file:
                datos = linea.strip().split(',')
                crear_usuario(conexion, *datos)
        print(f"Usuarios importados desde {archivo_csv}")
    except Error as error:
        print(f"Error al importar usuarios: {error}")
    except IOError as io_error:
        log_error(f"Error al leer el archivo CSV: {io_error}")
        print(f"Error al leer el archivo CSV: {io_error}")

def encriptar_contrasena(contrasena):
    import bcrypt
    salt = bcrypt.gensalt()
    contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return contrasena_encriptada