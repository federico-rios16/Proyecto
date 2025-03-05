import unittest
from app import app, validar_datos_usuario
from flask_login import login_user, logout_user
from conexion_bd import conectar_bd, cerrar_conexion
from operaciones_usuario import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario, listar_usuarios_paginados

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app.testing = True

    def test_validar_datos_usuario(self):
        # Prueba de validación de datos de usuario
        data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "contrasena": "123456"
        }
        valido, mensaje = validar_datos_usuario(data)
        self.assertTrue(valido)
        self.assertEqual(mensaje, "")

        data_invalido = {
            "nombre": "",
            "apellido": "Pérez",
            "email": "juan.perez@example",
            "contrasena": "123"
        }
        valido, mensaje = validar_datos_usuario(data_invalido)
        self.assertFalse(valido)
        self.assertNotEqual(mensaje, "")

    def test_register(self):
        # Prueba de registro de usuario
        data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "contrasena": "123456"
        }
        response = self.app.post('/api/register', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], "Usuario registrado con éxito")

    def test_login(self):
        # Prueba de inicio de sesión de usuario
        data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "contrasena": "123456"
        }
        # Registrar el usuario antes de intentar iniciar sesión
        self.app.post('/api/register', json=data)
        
        # Intentar iniciar sesión con las credenciales correctas
        response = self.app.post('/api/login', json={"email": "juan.perez@example.com", "contrasena": "123456"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Inicio de sesión exitoso")

        # Intentar iniciar sesión con una contraseña incorrecta
        response = self.app.post('/api/login', json={"email": "juan.perez@example.com", "contrasena": "incorrecta"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], "Credenciales incorrectas")

    def test_logout(self):
        # Prueba de cierre de sesión de usuario
        data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@example.com",
            "contrasena": "123456"
        }
        # Registrar e iniciar sesión del usuario
        self.app.post('/api/register', json=data)
        self.app.post('/api/login', json={"email": "juan.perez@example.com", "contrasena": "123456"})
        
        # Cerrar sesión del usuario
        response = self.app.post('/api/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Sesión cerrada exitosamente")

    def test_paginated_index(self):
        # Prueba de listado paginado de usuarios
        response = self.app.get('/page/1')
        self.assertEqual(response.status_code, 302)  # Redirección a la página de inicio de sesión

if __name__ == '__main__':
    unittest.main()