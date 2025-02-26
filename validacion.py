import re

def validar_datos_usuario(nombre, apellido, email, contrasena, telefono, direccion, fecha_nacimiento, dni):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Email no válido")
    if len(contrasena) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres")
    # Agrega más validaciones según sea necesario
    return True