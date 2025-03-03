import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [formData, setFormData] = useState({
    email: '',
    contrasena: ''
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
    // Aquí iría la lógica para iniciar sesión
    // Simulamos un inicio de sesión exitoso
    const isLoginSuccessful = true; // Cambia esto por la lógica real de inicio de sesión

    if (isLoginSuccessful) {
      navigate('/dashboard');
    } else {
      alert('Error al iniciar sesión');
    }
  };

  return (
    <Container className="mt-5">
      <h1>Iniciar Sesión</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Ingrese el email"
            required
          />
        </Form.Group>
        <Form.Group controlId="formContrasena">
          <Form.Label>Contraseña</Form.Label>
          <Form.Control
            type="password"
            name="contrasena"
            value={formData.contrasena}
            onChange={handleChange}
            placeholder="Ingrese la contraseña"
            required
          />
        </Form.Group>
        <Button variant="info" type="submit">
          Iniciar Sesión
        </Button>
      </Form>
    </Container>
  );
}

export default Login;