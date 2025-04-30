from extensiones import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)
    rol = db.Column(db.String(20), default='usuario')
    
    # Relaciones (pueden agregarse según necesidad)
    # propiedades = db.relationship('Propiedad', backref='propietario', lazy=True)
    
    def __repr__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
    
    def get_id(self):
        return str(self.id_usuario)
    
    def set_password(self, password):
        self.contrasena = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
    
    def to_dict(self):
        return {
            'id': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'fecha_registro': self.fecha_registro.isoformat() if self.fecha_registro else None,
            'rol': self.rol
        }

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
