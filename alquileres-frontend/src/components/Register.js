import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

function Register() {
  const [formData, setFormData] = useState({
    nombre: '',
    apellido: '',
    email: '',
    contrasena: '',
    telefono: '',
    direccion: '',
    fecha_nacimiento: '',
    dni: ''
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/api/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'Usuario registrado con éxito') {
          alert('Usuario registrado con éxito');
          navigate('/login');
        } else {
          alert('Error al registrar usuario');
        }
      });
  };

  return (
    <Container className="mt-5">
      <h1>Registro de Estudiante</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formNombre">
          <Form.Label>Nombre</Form.Label>
          <Form.Control type="text" name="nombre" value={formData.nombre} onChange={handleChange} placeholder="Ingrese el nombre" required />
        </Form.Group>
        <Form.Group controlId="formApellido">
          <Form.Label>Apellido</Form.Label>
          <Form.Control type="text" name="apellido" value={formData.apellido} onChange={handleChange} placeholder="Ingrese el apellido" required />
        </Form.Group>
        <Form.Group controlId="formEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Ingrese el email" required />
        </Form.Group>
        <Form.Group controlId="formContrasena">
          <Form.Label>Contraseña</Form.Label>
          <Form.Control type="password" name="contrasena" value={formData.contrasena} onChange={handleChange} placeholder="Ingrese la contraseña" required />
        </Form.Group>
        <Form.Group controlId="formTelefono">
          <Form.Label>Teléfono</Form.Label>
          <Form.Control type="text" name="telefono" value={formData.telefono} onChange={handleChange} placeholder="Ingrese el teléfono" />
        </Form.Group>
        <Form.Group controlId="formDireccion">
          <Form.Label>Dirección</Form.Label>
          <Form.Control type="text" name="direccion" value={formData.direccion} onChange={handleChange} placeholder="Ingrese la dirección" />
        </Form.Group>
        <Form.Group controlId="formFechaNacimiento">
          <Form.Label>Fecha de Nacimiento</Form.Label>
          <Form.Control type="date" name="fecha_nacimiento" value={formData.fecha_nacimiento} onChange={handleChange} />
        </Form.Group>
        <Form.Group controlId="formDNI">
          <Form.Label>DNI</Form.Label>
          <Form.Control type="text" name="dni" value={formData.dni} onChange={handleChange} placeholder="Ingrese el DNI" />
        </Form.Group>
        <Button variant="success" type="submit">
          Registrarse
        </Button>
      </Form>
    </Container>
  );
}

export default Register;