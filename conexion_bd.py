import mysql.connector
from mysql.connector import Error
import json

# Función para conectar a la base de datos
def conectar_bd():
    """
    Establece la conexión a la base de datos.
    Returns:
        conexion: Objeto de conexión a la base de datos o None si hay un error.
    """
    try:
        # Leer la configuración de la base de datos desde un archivo config.json
        with open('config.json') as f:
            config = json.load(f)
        database_config = config['database']

        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host=database_config['host'],
            user=database_config['user'],
            password=database_config['password'],
            database=database_config['database']
        )
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa")
        return conexion
    except Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    """
    Cierra la conexión a la base de datos.
    Args:
        conexion: Objeto de conexión a la base de datos.
    """
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada correctamente")
    except Error as error:
        print(f"Error al cerrar la conexión a la base de datos: {error}")

# Código de prueba para verificar la conexión a la base de datos
if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SHOW DATABASES;")
        for db in cursor:
            print(db)
        cerrar_conexion(conexion)

