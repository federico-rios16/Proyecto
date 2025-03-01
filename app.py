from flask import Flask, render_template, request, redirect, url_for, flash
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave secreta segura

@app.route('/')
def index():
    conexion = conectar_bd()
    usuarios = []
    if conexion:
        usuarios = leer_usuarios(conexion)
        cerrar_conexion(conexion)
    return render_template('index.html', usuarios=usuarios)

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
    return redirect(url_for('index'))

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
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    conexion = conectar_bd()
    if conexion:
        if eliminar_usuario(conexion, id):
            flash('Usuario eliminado correctamente', 'success')
        else:
            flash('Error al eliminar usuario', 'danger')
        cerrar_conexion(conexion)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)