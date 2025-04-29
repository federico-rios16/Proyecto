from flask import Flask, render_template, request, redirect, url_for, jsonify
import webbrowser
import bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from extensiones import db
from modelos import Usuario, Propiedad
from servicio_usuario import ServicioUsuario

# Configurar la aplicación
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/alquileres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la app
db.init_app(app)

# Crear una instancia del servicio de usuario
servicio_usuario = ServicioUsuario()

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    return usuario

# Ruta principal
@app.route("/")
def index():
    propiedades = Propiedad.query.filter_by(disponible=True).all()
    return render_template("index.html", propiedades=propiedades)

# Ruta para la página de registro
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo_electronico = request.form["correo_electronico"]
        contraseña = request.form["contraseña"]

        if not nombre or not apellido or not correo_electronico or not contraseña:
            return render_template("registro.html", error="Todos los campos son obligatorios.")
        if len(contraseña) < 6:
            return render_template("registro.html", error="La contraseña debe tener al menos 6 caracteres.")
        if "@" not in correo_electronico:
            return render_template("registro.html", error="Correo electrónico no válido.")

        hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            servicio_usuario.crear_usuario(
                nombre=nombre,
                apellido=apellido,
                correo_electronico=correo_electronico,
                contrasena=hashed_password
            )
        except Exception as e:
            return render_template("registro.html", error="Error al registrar el usuario: " + str(e))
        return redirect(url_for("index"))
    return render_template("registro.html")

# Ruta para la página de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo_electronico = request.form["correo_electronico"]
        contraseña = request.form["contraseña"]

        usuario = servicio_usuario.obtener_usuario_por_email(correo_electronico)
        if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            login_user(usuario)
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Credenciales inválidas")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# Ruta para la página de perfil
@app.route("/perfil")
@login_required
def perfil():
    return render_template("perfil.html")

# Ruta para la página de contacto
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    correo_electronico = data.get('correo_electronico')
    contrasena = data.get('contrasena')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    fecha_nacimiento = data.get('fecha_nacimiento')
    dni = data.get('dni')

    if not all([nombre, apellido, correo_electronico, contrasena, dni]):
        return jsonify({'message': 'Todos los campos son obligatorios'}), 400

    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
    try:
        servicio_usuario.crear_usuario(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            contrasena=hashed_password,
            telefono=telefono,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            dni=dni
        )
    except Exception as e:
        return jsonify({'message': 'Error al registrar el usuario', 'error': str(e)}), 500
    return jsonify({'message': 'Usuario registrado con éxito'}), 201

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.json
    correo_electronico = data.get('correo_electronico')
    contrasena = data.get('contrasena')

    usuario = servicio_usuario.obtener_usuario_por_email(correo_electronico)
    if usuario and bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    return jsonify({'message': 'Credenciales incorrectas'}), 401

if __name__ == "__main__":
    webbrowser.open_new_tab('http://127.0.0.1:5000')
    with app.app_context():
        db.create_all()
    app.run(debug=True)
