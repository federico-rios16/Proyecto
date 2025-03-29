from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario, listar_usuarios_paginados
import re

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Establecer una clave secreta para la aplicación (necesaria para manejar sesiones y cookies)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave secreta segura

# Permitir solicitudes CORS desde el frontend
CORS(app)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simulación de base de datos (lista de usuarios en memoria)
usuarios = []

# Clase User para Flask-Login
class User(UserMixin):
    def __init__(self, id, email, contrasena):
        self.id = id
        self.email = email
        self.contrasena = contrasena

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == int(user_id):
            return User(usuario['id'], usuario['email'], usuario['contrasena'])
    return None

# Función para validar datos de usuario
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
@app.route('/api/register', methods=['POST'])
def register():
    """
    Registra un nuevo usuario.
    Returns:
        Response: Respuesta JSON con un mensaje de éxito o error.
    """
    data = request.json  # Obtener los datos del usuario desde la solicitud JSON
    valido, mensaje = validar_datos_usuario(data)
    if not valido:
        return jsonify({"message": mensaje}), 400  # Devolver un mensaje de error si los datos no son válidos
    data['id'] = len(usuarios) + 1  # Asignar un ID único al usuario
    usuarios.append(data)  # Agregar el nuevo usuario a la lista de usuarios
    return jsonify({"message": "Usuario registrado con éxito"}), 201  # Devolver una respuesta JSON con un mensaje de éxito

# Ruta para iniciar sesión
@app.route('/api/login', methods=['POST'])
def login():
    """
    Inicia sesión de un usuario.
    Returns:
        Response: Respuesta JSON con un mensaje de éxito o error.
    """
    data = request.json  # Obtener los datos de inicio de sesión desde la solicitud JSON
    for usuario in usuarios:  # Recorrer la lista de usuarios
        if usuario['email'] == data['email'] and usuario['contrasena'] == data['contrasena']:  # Verificar las credenciales
            user = User(usuario['id'], usuario['email'], usuario['contrasena'])
            login_user(user)  # Iniciar sesión del usuario
            return jsonify({"message": "Inicio de sesión exitoso"}), 200  # Devolver una respuesta JSON con un mensaje de éxito
    return jsonify({"message": "Credenciales incorrectas"}), 401  # Devolver una respuesta JSON con un mensaje de error

# Ruta para cerrar sesión
@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    """
    Cierra la sesión del usuario.
    Returns:
        Response: Redirección a la página de inicio.
    """
    logout_user()  # Cerrar sesión del usuario
    return jsonify({"message": "Sesión cerrada exitosamente"}), 200  # Devolver una respuesta JSON con un mensaje de éxito

# Ruta principal que renderiza el archivo index.html como la página principal
@app.route('/')
def index():
    """
    Renderiza el archivo index.html como la página principal.
    Returns:
        Response: Renderiza la plantilla index.html.
    """
    return render_template('index.html')  # Renderiza tu archivo index.html directamente

# Ruta para mostrar una página paginada de usuarios
@app.route('/page/<int:page_num>')
def paginated_index(page_num):
    """
    Muestra una página paginada de usuarios.
    Args:
        page_num (int): Número de la página.
    Returns:
        Response: Renderiza la plantilla HTML con la lista de usuarios y el número de página.
    """
    conexion = conectar_bd()  # Conectar a la base de datos
    usuarios = []
    if conexion:
        usuarios = listar_usuarios_paginados(conexion, page_num, 10)  # Obtener una lista paginada de usuarios (10 usuarios por página)
        cerrar_conexion(conexion)  # Cerrar la conexión a la base de datos
    return render_template('index.html', usuarios=usuarios, page_num=page_num)  # Renderizar la plantilla HTML con la lista de usuarios y el número de página

# Ruta para agregar un nuevo usuario
@app.route('/add', methods=['POST'])
@login_required
def add_user():
    """
    Agrega un nuevo usuario.
    Returns:
        Response: Redirección a la primera página de usuarios.
    """
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    contrasena = request.form['contrasena']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dni = request.form['dni']
    
    # Validar los datos del formulario
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contrasena": contrasena,
        "telefono": telefono,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nacimiento,
        "dni": dni
    }
    valido, mensaje = validar_datos_usuario(data)
    if not valido:
        flash(mensaje, 'danger')  # Mostrar un mensaje de error si los datos no son válidos
        return redirect(url_for('paginated_index', page_num=1))  # Redirigir a la primera página de usuarios

    conexion = conectar_bd()  # Conectar a la base de datos
    if conexion:
        # Intentar crear un nuevo usuario en la base de datos
        if crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
            flash('Usuario agregado correctamente', 'success')  # Mostrar un mensaje de éxito
        else:
            flash('Error al agregar usuario', 'danger')  # Mostrar un mensaje de error
        cerrar_conexion(conexion)  # Cerrar la conexión a la base de datos
    return redirect(url_for('paginated_index', page_num=1))  # Redirigir a la primera página de usuarios

# Ruta para actualizar un usuario existente
@app.route('/update/<int:id>', methods=['POST'])
@login_required
def update_user(id):
    """
    Actualiza un usuario existente.
    Args:
        id (int): ID del usuario.
    Returns:
        Response: Redirección a la primera página de usuarios.
    """
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dni = request.form['dni']
    
    # Validar los datos del formulario
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contrasena": request.form.get('contrasena', ''),  # La contraseña puede no estar presente en la actualización
        "telefono": telefono,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nacimiento,
        "dni": dni
    }
    valido, mensaje = validar_datos_usuario(data)
    if not valido:
        flash(mensaje, 'danger')  # Mostrar un mensaje de error si los datos no son válidos
        return redirect(url_for('paginated_index', page_num=1))  # Redirigir a la primera página de usuarios

    conexion = conectar_bd()  # Conectar a la base de datos
    if conexion:
        # Intentar actualizar el usuario en la base de datos
        if actualizar_usuario(conexion, id, nombre, apellido, email, telefono, direccion, fecha_nacimiento, dni):
            flash('Usuario actualizado correctamente', 'success')  # Mostrar un mensaje de éxito
        else:
            flash('Error al actualizar usuario', 'danger')  # Mostrar un mensaje de error
        cerrar_conexion(conexion)  # Cerrar la conexión a la base de datos
    return redirect(url_for('paginated_index', page_num=1))  # Redirigir a la primera página de usuarios

# Ruta para eliminar un usuario existente
@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    """
    Elimina un usuario existente.
    Args:
        id (int): ID del usuario.
    Returns:
        Response: Redirección a la primera página de usuarios.
    """
    conexion = conectar_bd()  # Conectar a la base de datos
    if conexion:
        # Intentar eliminar el usuario de la base de datos
        if eliminar_usuario(conexion, id):
            flash('Usuario eliminado correctamente', 'success')  # Mostrar un mensaje de éxito
        else:
            flash('Error al eliminar usuario', 'danger')  # Mostrar un mensaje de error
        cerrar_conexion(conexion)  # Cerrar la conexión a la base de datos
    return redirect(url_for('paginated_index', page_num=1))  # Redirigir a la primera página de usuarios

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo de depuración