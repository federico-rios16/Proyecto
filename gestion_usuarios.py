from flask import Blueprint, request, jsonify, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from modelo_usuario import User  # Ensure 'modelo_usuario.py' is in the same directory as this file
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario
import re
from flask import url_for, redirect
from gestion_usuarios import usuarios

# Crear un Blueprint para la gestión de usuarios
@usuarios_bp.route('/usuarios')
def usuarios():
    return redirect(url_for('usuarios'))

@usuarios_bp.route('/usuarios/<int:user_id>')
def usuario(user_id):
    return redirect(url_for('usuario', user_id=user_id))

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    return redirect(url_for('crear_usuario'))

@usuarios_bp.route('/usuarios/editar/<int:user_id>', methods=['GET', 'POST'])
def editar_usuario(user_id):
    return redirect(url_for('editar_usuario', user_id=user_id))

@usuarios_bp.route('/usuarios/eliminar/<int:user_id>')
def eliminar_usuario(user_id):
    return redirect(url_for('eliminar_usuario', user_id=user_id))

# Crear un Blueprint para la gestión de usuarios
usuarios_bp = Blueprint('usuarios', __name__)

# Validar datos de usuario
def validar_datos_usuario(data):
    """
    Valida los datos del usuario.
    Args:
        data (dict): Diccionario con los datos del usuario.
    Returns:
        tuple: (bool, str) Indica si los datos son válidos y un mensaje de error si no lo son.
    """
    if not data.get('nombre') or not data.get('apellido'):
        return False, "Nombre y apellido son obligatorios."
    if not data.get('email') or not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return False, "Correo electrónico no válido."
    if not data.get('contrasena') or len(data['contrasena']) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    return True, ""

# Ruta para registrar un nuevo usuario
@usuarios_bp.route('/api/register', methods=['POST'])
def register():
    """
    Registra un nuevo usuario.
    Returns:
        Response: Respuesta JSON con un mensaje de éxito o error.
    """
    data = request.json
    valido, mensaje = validar_datos_usuario(data)
    if not valido:
        return jsonify({"message": mensaje}), 400
    conexion = conectar_bd()
    if conexion:
        if crear_usuario(conexion, **data):
            cerrar_conexion(conexion)
            return jsonify({"message": "Usuario registrado con éxito"}), 201
        cerrar_conexion(conexion)
    return jsonify({"message": "Error al registrar usuario"}), 500

# Ruta para iniciar sesión
@usuarios_bp.route('/api/login', methods=['POST'])
def login():
    """
    Inicia sesión de un usuario.
    Returns:
        Response: Respuesta JSON con un mensaje de éxito o error.
    """
    data = request.json
    conexion = conectar_bd()
    if conexion:
        usuarios = leer_usuarios(conexion)
        cerrar_conexion(conexion)
        for usuario in usuarios:
            if usuario['email'] == data['email'] and usuario['contrasena'] == data['contrasena']:
                user = User(usuario['id'], usuario['email'], usuario['contrasena'])
                login_user(user)
                return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"message": "Credenciales incorrectas"}), 401

# Ruta para cerrar sesión
@usuarios_bp.route('/api/logout', methods=['POST'])
@login_required
def logout():
    """
    Cierra la sesión del usuario.
    Returns:
        Response: Respuesta JSON con un mensaje de éxito.
    """
    logout_user()
    return jsonify({"message": "Sesión cerrada exitosamente"}), 200