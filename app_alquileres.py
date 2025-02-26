from conexion_bd import conectar_bd

import mysql.connector
import re

def validar_datos_usuario(nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Email no válido")
    if len(contrasena) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres")
    # Agrega más validaciones según sea necesario
    return True

def crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
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
        print(f"Error al crear usuario: {error}")
    except ValueError as ve:
        print(f"Error de validación: {ve}")

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

def actualizar_usuario(conexion, usuario_id, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
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
        print(f"Error al actualizar usuario: {error}")

def eliminar_usuario(conexion, usuario_id):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuario_id,))
        conexion.commit()
        print("Usuario eliminado exitosamente")
    except mysql.connector.Error as error:
        print(f"Error al eliminar usuario: {error}")

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

