import unittest
from unittest.mock import MagicMock, patch
from operaciones_usuario import (crear_usuario, leer_usuarios, mostrar_tablas, 
                                 actualizar_usuario, eliminar_usuario, 
                                 buscar_usuario_por_nombre, listar_usuarios_paginados, 
                                 exportar_usuarios_a_csv, importar_usuarios_desde_csv)

class TestOperacionesUsuario(unittest.TestCase):

    def setUp(self):
        self.conexion = MagicMock()

    @patch('operaciones_usuario.validar_datos_usuario')
    def test_crear_usuario(self, mock_validar):
        crear_usuario(self.conexion, "Test", "User", "test@user.com", "password", "123456789", "Test Address", "2000-01-01", "12345678A")
        self.conexion.cursor().execute.assert_called()
        mock_validar.assert_called()

    def test_leer_usuarios(self):
        leer_usuarios(self.conexion)
        self.conexion.cursor().execute.assert_called_with("SELECT * FROM usuarios")

    def test_mostrar_tablas(self):
        mostrar_tablas(self.conexion)
        self.conexion.cursor().execute.assert_called_with("SHOW TABLES")

    def test_actualizar_usuario(self):
        actualizar_usuario(self.conexion, 1, "Test", "User", "test@user.com", "password", "123456789", "Test Address", "2000-01-01", "12345678A")
        self.conexion.cursor().execute.assert_called()

    def test_eliminar_usuario(self):
        eliminar_usuario(self.conexion, 1)
        self.conexion.cursor().execute.assert_called_with("DELETE FROM usuarios WHERE id = %s", (1,))

    def test_buscar_usuario_por_nombre(self):
        buscar_usuario_por_nombre(self.conexion, "Test")
        self.conexion.cursor().execute.assert_called_with("SELECT * FROM usuarios WHERE nombre = %s", ("Test",))

    def test_listar_usuarios_paginados(self):
        listar_usuarios_paginados(self.conexion, 1, 2)
        self.conexion.cursor().execute.assert_called_with("SELECT * FROM usuarios LIMIT %s OFFSET %s", (2, 0))

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="nombre,apellido,email,contrasena,telefono,direccion,fecha_nacimiento,dni\nTest,User,test@user.com,password,123456789,Test Address,2000-01-01,12345678A")
    def test_exportar_usuarios_a_csv(self, mock_open):
        exportar_usuarios_a_csv(self.conexion, "usuarios.csv")
        self.conexion.cursor().execute.assert_called_with("SELECT * FROM usuarios")
        mock_open.assert_called_with("usuarios.csv", mode='w', newline='')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="nombre,apellido,email,contrasena,telefono,direccion,fecha_nacimiento,dni\nTest,User,test@user.com,password,123456789,Test Address,2000-01-01,12345678A")
    def test_importar_usuarios_desde_csv(self, mock_open):
        importar_usuarios_desde_csv(self.conexion, "usuarios.csv")
        self.conexion.cursor().execute.assert_called()

if __name__ == '__main__':
    unittest.main()