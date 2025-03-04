from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario, listar_usuarios_paginados

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave secreta segura
CORS(app)  # Permitir solicitudes CORS desde el frontend

# Simulación de base de datos
usuarios = []

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    usuarios.append(data)
    return jsonify({"message": "Usuario registrado con éxito"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    for usuario in usuarios:
        if usuario['email'] == data['email'] and usuario['contrasena'] == data['contrasena']:
            return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"message": "Credenciales incorrectas"}), 401

@app.route('/')
def index():
    return redirect(url_for('paginated_index', page_num=1))

@app.route('/page/<int:page_num>')
def paginated_index(page_num):
    conexion = conectar_bd()
    usuarios = []
    if conexion:
        usuarios = listar_usuarios_paginados(conexion, page_num, 10)  # 10 usuarios por página
        cerrar_conexion(conexion)
    return render_template('index.html', usuarios=usuarios, page_num=page_num)

@app.route('/add', methods=['POST'])
def add_user():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    contrasena = request.form['contrasena']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dni = request.form['dni']
    
    conexion = conectar_bd()
    if conexion:
        if crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
            flash('Usuario agregado correctamente', 'success')
        else:
            flash('Error al agregar usuario', 'danger')
        cerrar_conexion(conexion)
    return redirect(url_for('paginated_index', page_num=1))

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dni = request.form['dni']
    
    conexion = conectar_bd()
    if conexion:
        if actualizar_usuario(conexion, id, nombre, apellido, email, telefono, direccion, fecha_nacimiento, dni):
            flash('Usuario actualizado correctamente', 'success')
        else:
            flash('Error al actualizar usuario', 'danger')
        cerrar_conexion(conexion)
    return redirect(url_for('paginated_index', page_num=1))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    conexion = conectar_bd()
    if conexion:
        if eliminar_usuario(conexion, id):
            flash('Usuario eliminado correctamente', 'success')
        else:
            flash('Error al eliminar usuario', 'danger')
        cerrar_conexion(conexion)
    return redirect(url_for('paginated_index', page_num=1))

if __name__ == '__main__':
    app.run(debug=True)