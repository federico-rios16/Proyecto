import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos
def conectar_bd():
    try:
        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Asegúrate de que este usuario tenga permisos
            password="1234",  # Asegúrate de que esta contraseña sea correcta
            database="alquileres"
        )
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa")
        return conexion
    except Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
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

