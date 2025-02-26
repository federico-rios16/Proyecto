import mysql.connector
from mysql.connector import Error

def conectar_bd():
    try:
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

def cerrar_conexion(conexion):
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada correctamente")
    except Error as error:
        print(f"Error al cerrar la conexión a la base de datos: {error}")

