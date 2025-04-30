from extensiones import db
from modelos import Usuario
from sqlalchemy.exc import IntegrityError

class ServicioUsuario:
    """
    Servicio para operaciones CRUD sobre usuarios.
    """

    def crear_usuario(self, nombre, apellido, correo_electronico, contrasena, telefono=None, direccion=None, fecha_nacimiento=None, dni=None):
        """
        Crea un nuevo usuario si el email y el dni no existen.
        Retorna el usuario creado o None si ya existe.
        """
        # Verificar si ya existe un usuario con el mismo email
        if Usuario.query.filter_by(email=correo_electronico).first():
            return None
            
        # Verificar si ya existe un usuario con el mismo DNI (si se proporciona)
        if dni and Usuario.query.filter_by(dni=dni).first():
            return None

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
        try:
            db.session.commit()
            return nuevo_usuario
        except IntegrityError:
            db.session.rollback()
            return None

    def leer_usuarios(self):
        """
        Retorna una lista de todos los usuarios.
        """
        return Usuario.query.all()

    def actualizar_usuario(self, id_usuario, nombre=None, apellido=None, correo_electronico=None, contrasena=None, telefono=None, direccion=None, fecha_nacimiento=None, dni=None):
        """
        Actualiza los datos de un usuario existente.
        Retorna el usuario actualizado o None si no existe o hay duplicados.
        """
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return None

        # Validar email/dni duplicados si se cambian
        if correo_electronico and correo_electronico != usuario.email:
            if Usuario.query.filter_by(email=correo_electronico).first():
                return None
            usuario.email = correo_electronico
            
        if dni and dni != usuario.dni:
            if Usuario.query.filter_by(dni=dni).first():
                return None
            usuario.dni = dni

        if nombre is not None:
            usuario.nombre = nombre
        if apellido is not None:
            usuario.apellido = apellido
        if contrasena is not None:
            usuario.contrasena = contrasena
        if telefono is not None:
            usuario.telefono = telefono
        if direccion is not None:
            usuario.direccion = direccion
        if fecha_nacimiento is not None:
            usuario.fecha_nacimiento = fecha_nacimiento

        try:
            db.session.commit()
            return usuario
        except IntegrityError:
            db.session.rollback()
            return None

    def eliminar_usuario(self, id_usuario):
        """
        Elimina un usuario por su ID.
        Retorna True si se eliminó, False si no existe.
        """
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False
            
        try:
            db.session.delete(usuario)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def obtener_usuario_por_email(self, correo_electronico):
        """
        Retorna el usuario con el email dado, o None si no existe.
        """
        return Usuario.query.filter_by(email=correo_electronico).first()
