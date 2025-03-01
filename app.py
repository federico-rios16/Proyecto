from flask import Flask, render_template, request, redirect, url_for
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios

app = Flask(__name__)

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
        crear_usuario(conexion, nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni)
        cerrar_conexion(conexion)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)