import webbrowser
from flask import Flask, render_template
from flask_login import login_user, logout_user, login_required, current_user
from flask_cors import CORS
from flask_login import LoginManager
from gestion_usuarios import usuarios_bp


# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la aplicación
app.secret_key = 'supersecretkey'
CORS(app)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'usuarios.login'

# Registrar el Blueprint de usuarios
app.register_blueprint(usuarios_bp)

# Ruta principal
@app.route('/')
def index():
    """
    Renderiza el archivo index.html como la página principal.
    Returns:
        Response: Renderiza la plantilla index.html.
    """
    return render_template('index.html')

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)