# Proyecto de Alquileres

Este es un proyecto de gestión de alquileres desarrollado con Flask para el backend y React para el frontend. La aplicación permite registrar, actualizar, eliminar y listar usuarios, así como gestionar propiedades.

## Características

- Registro de usuarios
- Inicio de sesión de usuarios
- Actualización de información de usuarios
- Eliminación de usuarios
- Listado paginado de usuarios
- Gestión de propiedades

## Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Framework web para el backend
- [React](https://reactjs.org/) - Biblioteca de JavaScript para el frontend
- [MySQL](https://www.mysql.com/) - Sistema de gestión de bases de datos
- [Bootstrap](https://getbootstrap.com/) - Framework CSS para el diseño

## Instalación

### Requisitos Previos

- Python 3
- Node.js y npm
- MySQL

### Backend

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/proyecto-alquileres.git
    cd proyecto-alquileres
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura la base de datos MySQL:
    - Crea una base de datos llamada `alquileres`.
    - Actualiza las credenciales de la base de datos en [conexion_bd.py](http://_vscodecontentref_/0).

5. Ejecuta las migraciones de la base de datos (si las tienes):
    ```bash
    flask db upgrade
    ```

6. Inicia el servidor Flask:
    ```bash
    flask run
    ```

### Frontend

1. Navega al directorio del frontend:
    ```bash
    cd alquileres-frontend
    ```

2. Instala las dependencias:
    ```bash
    npm install
    ```

3. Inicia el servidor de desarrollo de React:
    ```bash
    npm start
    ```

## Uso

1. Abre tu navegador web y navega a `http://localhost:3000` para acceder a la aplicación frontend.
2. Utiliza las funcionalidades de registro, inicio de sesión, y gestión de usuarios y propiedades.

## Contribución

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.


## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto:

- **Nombre:** Federico Rios
- **Correo Electrónico:** federicoalfredorios@gmail.com
- **GitHub:** [federico-rios16](https://github.com/federico-rios16)
