from extensiones import db
from modelos import Usuario

class ServicioUsuario:
    def __init__(self):
        pass  # Ya no necesitamos sesión externa, usamos db.session

    def crear_usuario(self, nombre, apellido, correo_electronico, contrasena, telefono=None, direccion=None, fecha_nacimiento=None, dni=None):
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=correo_electronico,
            contrasena=contrasena,
            telefono=telefono,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            dni=dni
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    def leer_usuarios(self):
        return Usuario.query.all()

    def actualizar_usuario(self, id_usuario, nombre=None, apellido=None, correo_electronico=None, contrasena=None, telefono=None, direccion=None, fecha_nacimiento=None, dni=None):
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            if nombre is not None:
                usuario.nombre = nombre
            if apellido is not None:
                usuario.apellido = apellido
            if correo_electronico is not None:
                usuario.email = correo_electronico
            if contrasena is not None:
                usuario.contrasena = contrasena
            if telefono is not None:
                usuario.telefono = telefono
            if direccion is not None:
                usuario.direccion = direccion
            if fecha_nacimiento is not None:
                usuario.fecha_nacimiento = fecha_nacimiento
            if dni is not None:
                usuario.dni = dni
            db.session.commit()
            return usuario
        return None

    def eliminar_usuario(self, id_usuario):
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return True
        return False

    def obtener_usuario_por_email(self, correo_electronico):
        return Usuario.query.filter_by(email=correo_electronico).first()
