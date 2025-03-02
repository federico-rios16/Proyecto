import React from 'react';
import { Container, Row, Col, Button, Form } from 'react-bootstrap';
import { useHistory } from 'react-router-dom';

function Student() {
  const history = useHistory();

  const handleRegisterClick = () => {
    history.push('/register');
  };

  const handleLoginClick = () => {
    history.push('/login');
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