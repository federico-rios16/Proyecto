import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Asegúrate de que este usuario tenga permisos
            password="1234",  # Asegúrate de que esta contraseña sea correcta
            database="alquileres"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None
    
