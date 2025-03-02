import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

function Student() {
  const navigate = useNavigate();

  const handleRegisterClick = () => {
    navigate('/register');
  };

  const handleLoginClick = () => {
    navigate('/login');
  };

  return (
    <Container className="text-center mt-5">
      <h1>Bienvenido Estudiante</h1>
      <p>Por favor, regístrate o inicia sesión para continuar.</p>
      <Row className="mt-4">
        <Col>
          <Button variant="success" size="lg" onClick={handleRegisterClick}>
            Registrarse
          </Button>
        </Col>
        <Col>
          <Button variant="info" size="lg" onClick={handleLoginClick}>
            Iniciar Sesión
          </Button>
        </Col>
      </Row>
    </Container>
  );
}

export default Student;