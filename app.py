from flask import Flask, render_template, request, redirect, url_for, jsonify
from conexion_bd import conectar_bd, cerrar_conexion
from servicio_usuario import ServicioUsuario
import webbrowser
import bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
import os




# Configurar la aplicación
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Cambia esto a una clave secreta más segura en producción
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost/alquileres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email

@login_manager.user_loader
def load_user(email):
    usuario = servicio_usuario.obtener_usuario_por_email(email)
    if usuario:
        return User(usuario["email"], usuario["email"])
    return None

# Crear una instancia del servicio de usuario
servicio_usuario = ServicioUsuario(conectar_bd())

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    dni = db.Column(db.String(20), unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())

class Propiedad(db.Model):
    __tablename__ = 'propiedades'

    id_propiedad = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)  # Cambio de 'nombre' a 'titulo'
    descripcion = db.Column(db.Text)
    direccion = db.Column(db.String(255))
    tipo = db.Column(db.String(50))
    habitaciones = db.Column(db.Integer)
    baños = db.Column(db.Integer)
    precio = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    imagenes = db.Column(db.Text)  # Si guardas URLs de imágenes
    caracteristicas = db.Column(db.Text)  # Detalles adicionales

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

        # Validaciones
        if not nombre or not apellido or not correo_electronico or not contraseña:
            return render_template("registro.html", error="Todos los campos son obligatorios.")
        if len(contraseña) < 6:
            return render_template("registro.html", error="La contraseña debe tener al menos 6 caracteres.")
        if "@" not in correo_electronico:
            return render_template("registro.html", error="Correo electrónico no válido.")

        # Encriptar la contraseña
        hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

        # Crear el usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=correo_electronico,
            contrasena=hashed_password.decode('utf-8')
        )
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return render_template("registro.html", error="Error al registrar el usuario: " + str(e))
        return redirect(url_for("index"))
    return render_template("registro.html")

# Ruta para la página de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo_electronico = request.form["correo_electronico"]
        contraseña = request.form["contraseña"]

        usuario = Usuario.query.filter_by(email=correo_electronico).first()
        if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            user = User(usuario.id_usuario, usuario.email)
            login_user(user)
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
    email = data.get('email')
    contrasena = data.get('contrasena')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    fecha_nacimiento = data.get('fecha_nacimiento')
    dni = data.get('dni')

    # Validaciones básicas
    if not all([nombre, apellido, email, contrasena, dni]):
        return jsonify({'message': 'Todos los campos son obligatorios'}), 400

    # Crear el usuario
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        email=email,
        contrasena=hashed_password.decode('utf-8'),
        telefono=telefono,
        direccion=direccion,
        fecha_nacimiento=fecha_nacimiento,
        dni=dni
    )
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al registrar el usuario', 'error': str(e)}), 500
    return jsonify({'message': 'Usuario registrado con éxito'}), 201

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.json
    email = data.get('email')
    contrasena = data.get('contrasena')

    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    return jsonify({'message': 'Credenciales incorrectas'}), 401

if __name__ == "__main__":
    # Abrir el navegador al iniciar la aplicación
    webbrowser.open_new_tab('http://127.0.0.1:5000')
    with app.app_context():
        db.create_all()
    app.run()
    