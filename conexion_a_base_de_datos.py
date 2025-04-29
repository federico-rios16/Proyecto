from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from tabulate import tabulate

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/Alquileres')
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    contrasena = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(String)
    dni = Column(String)
    telefono = Column(String)
    fecha_registro = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

# Realizar una consulta para obtener todos los usuarios
usuarios = session.query(Usuario).all()

# Crear una lista con los resultados
resultados = []
for usuario in usuarios:
    fila = [
        usuario.id_usuario,
        usuario.nombre,
        usuario.apellido,
        usuario.email,
        usuario.contrasena,
        usuario.direccion,
        usuario.fecha_nacimiento,
        usuario.dni,
        usuario.telefono,
        usuario.fecha_registro
    ]
    fila = [valor if valor is not None else 'N/A' for valor in fila]
    resultados.append(fila)

# Imprimir los resultados en una tabla
maxcolwidths = [10, 20, 20, 30, 20, 30, 20, 15, 15, 25]
print(tabulate(resultados, headers=['ID', 'Nombre', 'Apellido', 'Email', 'Contraseña', 'Direccion', 'Fecha Nacimiento', 'DNI', 'Telefono', 'Fecha Registro'], tablefmt='fancy_grid', maxcolwidths=maxcolwidths, missingval='N/A'))

session.close()