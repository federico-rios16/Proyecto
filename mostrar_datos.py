from conexion_bd import conectar_bd
from operaciones_usuario import leer_usuarios

def mostrar_usuarios():
    conexion = conectar_bd()
    if conexion:
        leer_usuarios(conexion)
        conexion.close()

if __name__ == '__main__':
    mostrar_usuarios()