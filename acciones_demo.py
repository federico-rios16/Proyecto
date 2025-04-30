from flask import Flask
from extensiones import db
from modelos import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/alquileres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Crear un nuevo usuario
def crear_usuario_demo():
    nuevo_usuario = Usuario(
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@email.com",
        contrasena="123456",
        telefono="123456789",
        direccion="Calle Falsa 123",
        fecha_nacimiento="1990-01-01",
        dni="12345678"
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    print("Usuario insertado con ID:", nuevo_usuario.id_usuario)

#Actualizar un usuario existente
def actualizar_usuario_demo(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if usuario:
        usuario.nombre = "Nombre Nuevo"
        usuario.direccion = "Nueva Dirección"
        db.session.commit()
        print("Usuario actualizado")
    else:
        print("Usuario no encontrado")

#Consultar todos los usuarios
def listar_usuarios_demo():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        print(f"ID: {usuario.id_usuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")

#Buscar un usuario por email
def buscar_usuario_por_email_demo(email):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        print(f"Usuario encontrado: ID: {usuario.id_usuario}, Nombre: {usuario.nombre}")
    else:
        print("Usuario no encontrado")

#Eliminar un usuario por ID
def eliminar_usuario_demo(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")

if __name__ == "__main__":
    with app.app_context():
        # Descomenta SOLO la acción que quieras probar
        # crear_usuario_demo()
        # actualizar_usuario_demo(1)
        listar_usuarios_demo()
        # buscar_usuario_por_email_demo("juan.perez@email.com")
        # eliminar_usuario_demo(1)