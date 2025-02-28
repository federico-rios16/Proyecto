CREATE DATABASE IF NOT EXISTS Alquileres;

#USE Alquileres;

#DROP DATABASE Alquleres;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    fecha_nacimiento DATE,
    dni VARCHAR(20) UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS propiedades (
    id_propiedad INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    direccion VARCHAR(255),
    tipo VARCHAR(50),
    habitaciones INT,
    baños INT,
    precio DECIMAL(10, 2),
    disponible BOOLEAN,
    imagenes TEXT,
    caracteristicas TEXT
);

CREATE TABLE IF NOT EXISTS alquileres (
    id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_propiedad INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    precio_alquiler DECIMAL(10, 2),
    estado VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_propiedad) REFERENCES propiedades(id_propiedad)
);

CREATE TABLE IF NOT EXISTS pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_alquiler INT,
    fecha_pago DATE,
    monto DECIMAL(10, 2),
    metodo_pago VARCHAR(50),
    numero_transaccion VARCHAR(255),
    FOREIGN KEY (id_alquiler) REFERENCES alquileres(id_alquiler)
);

-- Inserción de datos de ejemplo
INSERT INTO usuarios (nombre, apellido, email, contrasena) VALUES (
    'Juan', 
    'Pérez', 
    'juan@ejemplo.com', 
    'contraseña123'
);

INSERT INTO propiedades (titulo, precio, disponible) VALUES (
    'Apartamento en la playa', 
    1500.00, 
    true
);

-- Consultas de ejemplo
SELECT * FROM usuarios;
SELECT titulo, precio FROM propiedades WHERE disponible = true;













