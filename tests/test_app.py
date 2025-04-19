import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Configurar el cliente de prueba
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        # Prueba para la ruta principal
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Gestión de Alquileres Dinasty8'.encode('utf-8'), response.data)

    def test_registro_get(self):
        # Prueba para la página de registro (GET)
        response = self.app.get('/registro')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registro', response.data)
        self.assertIn(b'Nombre', response.data)

    def test_login_get(self):
        # Prueba para la página de login (GET)
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Iniciar sesión'.encode('utf-8'), response.data)

    def test_login_post_invalid(self):
        # Prueba para un inicio de sesión con credenciales inválidas
        response = self.app.post('/login', data={
            'correo_electronico': 'usuario@invalido.com',
            'contraseña': 'incorrecta'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Credenciales inválidas'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()