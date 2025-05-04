from app import app
from modelos import db, Usuario

with app.app_context():
    # Crear un usuario de prueba
    nuevo_usuario = Usuario(
        nombre="Test",
        apellido="User",
        email="test@example.com",
        contrasena="hashed_password"
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    print("Usuario creado:", nuevo_usuario)