from extensiones import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
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
    
    def get_id(self):
        return str(self.id_usuario)

class Propiedad(db.Model):
    __tablename__ = 'propiedades'

    id_propiedad = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    direccion = db.Column(db.String(255))
    tipo = db.Column(db.String(50))
    habitaciones = db.Column(db.Integer)
    baños = db.Column(db.Integer)
    precio = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    imagenes = db.Column(db.Text)
    caracteristicas = db.Column(db.Text)