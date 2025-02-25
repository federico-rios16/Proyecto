from conexion_bd import conectar_bd

import mysql.connector

def crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
    try:
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
        print(f"Error al crear usuario: {error}")

def leer_usuarios(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)
    except mysql.connector.Error as error:
        print(f"Error al leer usuarios: {error}")

def mostrar_tablas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
    except mysql.connector.Error as error:
        print(f"Error al mostrar tablas: {error}")

# Ejemplo de uso
conexion = conectar_bd()

if conexion:
    # Cargar varios usuarios
    usuarios = [
        ("Ana", "García", "ana@ejemplo.com", "secreto123", "123456789", "Calle Falsa 123", "1990-01-01", "12345678A"),
        ("Luis", "Pérez", "luis@ejemplo.com", "contrasena456", "987654321", "Avenida Siempre Viva 742", "1985-05-15", "87654321B"),
        ("María", "López", "maria@ejemplo.com", "clave789", "555555555", "Plaza Mayor 1", "1992-07-20", "11223344C"),
        ("Carlos", "Martínez", "carlos@ejemplo.com", "password101", "444444444", "Calle Luna 45", "1988-11-30", "22334455D")
    ]

    for usuario in usuarios:
        crear_usuario(conexion, *usuario)

    leer_usuarios(conexion)
    mostrar_tablas(conexion)
    conexion.close()