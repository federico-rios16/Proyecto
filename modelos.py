from extensiones import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    dni = db.Column(db.String(20), unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    activo = db.Column(db.Boolean, default=True)
    rol = db.Column(db.String(20), default='usuario')
    
    # Relaciones
    alquileres = db.relationship('Alquiler', back_populates='usuario', cascade="all, delete-orphan")
    
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

    id_propiedad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    direccion = db.Column(db.String(255))
    tipo = db.Column(db.String(50))
    habitaciones = db.Column(db.Integer)
    banos = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    imagenes = db.Column(db.Text)
    caracteristicas = db.Column(db.Text)
    
    # Relaciones
    alquileres = db.relationship('Alquiler', back_populates='propiedad')
    
    def __repr__(self):
        return f"Propiedad(id_propiedad={self.id_propiedad}, titulo='{self.titulo}', precio={self.precio})"
    
    def to_dict(self):
        return {
            'id': self.id_propiedad,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'direccion': self.direccion,
            'tipo': self.tipo,
            'habitaciones': self.habitaciones,
            'banos': self.banos,
            'precio': float(self.precio) if self.precio else None,
            'disponible': self.disponible,
            'imagenes': self.imagenes,
            'caracteristicas': self.caracteristicas
        }

class Alquiler(db.Model):
    __tablename__ = 'alquileres'

    id_alquiler = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'))
    id_propiedad = db.Column(db.Integer, db.ForeignKey('propiedades.id_propiedad'))
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    precio_alquiler = db.Column(db.Numeric(10, 2))
    estado = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    # Relaciones
    usuario = db.relationship('Usuario', back_populates='alquileres')
    propiedad = db.relationship('Propiedad', back_populates='alquileres')
    pagos = db.relationship('Pago', back_populates='alquiler', cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Alquiler(id_alquiler={self.id_alquiler}, id_usuario={self.id_usuario}, id_propiedad={self.id_propiedad})"
    
    def to_dict(self):
        return {
            'id': self.id_alquiler,
            'id_usuario': self.id_usuario,
            'id_propiedad': self.id_propiedad,
            'fecha_inicio': self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            'fecha_fin': self.fecha_fin.isoformat() if self.fecha_fin else None,
            'precio_alquiler': float(self.precio_alquiler) if self.precio_alquiler else None,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None
        }

class Pago(db.Model):
    __tablename__ = 'pagos'

    id_pago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_alquiler = db.Column(db.Integer, db.ForeignKey('alquileres.id_alquiler', ondelete='CASCADE'))
    fecha_pago = db.Column(db.Date)
    monto = db.Column(db.Numeric(10, 2))
    metodo_pago = db.Column(db.String(50))
    numero_transaccion = db.Column(db.String(255))
    
    # Relaciones
    alquiler = db.relationship('Alquiler', back_populates='pagos')
    
    def __repr__(self):
        return f"Pago(id_pago={self.id_pago}, id_alquiler={self.id_alquiler}, monto={self.monto})"
    
    def to_dict(self):
        return {
            'id': self.id_pago,
            'id_alquiler': self.id_alquiler,
            'fecha_pago': self.fecha_pago.isoformat() if self.fecha_pago else None,
            'monto': float(self.monto) if self.monto else None,
            'metodo_pago': self.metodo_pago,
            'numero_transaccion': self.numero_transaccion
        }
