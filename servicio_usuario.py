from conexion_bd import cerrar_conexion, conectar_bd
from modelo_usuario import Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ServicioUsuario:
    def __init__(self, sesion):
        self.sesion = sesion

    def crear_usuario(self, nombre, apellido, correo_electronico, contraseña):
        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, correo_electronico=correo_electronico, contraseña=contraseña)
        self.sesion.add(nuevo_usuario)
        self.sesion.commit()
        return nuevo_usuario

    def leer_usuarios(self):
        return self.sesion.query(Usuario).all()

    def actualizar_usuario(self, id, nombre, apellido, correo_electronico, contraseña):
        usuario = self.sesion.query(Usuario).get(id)
        if usuario:
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo_electronico = correo_electronico
            usuario.contraseña = contraseña
            self.sesion.commit()
            return usuario
        return None

    def eliminar_usuario(self, id):
        usuario = self.sesion.query(Usuario).get(id)
        if usuario:
            self.sesion.delete(usuario)
            self.sesion.commit()
            return True
        return False

    def obtener_usuario_por_email(self, email):
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
            cerrar_conexion(conexion)
            return usuario
        return None