from flask import Flask, render_template
from conexion_bd import conectar_bd, cerrar_conexion
import webbrowser



# Crear la aplicación
app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para la página de contacto
if __name__ == "__main__":
    # Abrir el navegador al iniciar la aplicación
    webbrowser.open_new_tab('http://127.0.0.1:5000')
    app.run()