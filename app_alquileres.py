import json
from conexion_bd import conectar_bd
from operaciones_usuario import (crear_usuario, leer_usuarios, mostrar_tablas, 
                                 actualizar_usuario, eliminar_usuario, 
                                 buscar_usuario_por_nombre, listar_usuarios_paginados, 
                                 exportar_usuarios_a_csv, importar_usuarios_desde_csv)

# Leer usuarios desde el archivo de configuración
with open('config.json', 'r') as file:
    config = json.load(file)
    usuarios = config['usuarios']

# Ejemplo de uso
conexion = conectar_bd()

if conexion:
    for usuario in usuarios:
        crear_usuario(conexion, usuario['nombre'], usuario['apellido'], usuario['email'], usuario['contrasena'], usuario['telefono'], usuario['direccion'], usuario['fecha_nacimiento'], usuario['dni'])

    leer_usuarios(conexion)
    mostrar_tablas(conexion)
    buscar_usuario_por_nombre(conexion, "Ana")
    listar_usuarios_paginados(conexion, 1, 2)
    exportar_usuarios_a_csv(conexion, "usuarios.csv")
    importar_usuarios_desde_csv(conexion, "usuarios.csv")
    conexion.close()

