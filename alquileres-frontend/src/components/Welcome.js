import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { useHistory } from 'react-router-dom';

function Welcome() {
  const history = useHistory();

  const handleStudentClick = () => {
    history.push('/student');
  };

  const handleLandlordClick = () => {
    history.push('/landlord');
  };

  return (
    <Container className="text-center mt-5">
      <h1>Bienvenido a Alquileres</h1>
      <p>¿Eres estudiante o tienes un alquiler?</p>
      <Row className="mt-4">
        <Col>
          <Button variant="primary" size="lg" onClick={handleStudentClick}>
            Soy Estudiante
          </Button>
        </Col>
        <Col>
          <Button variant="secondary" size="lg" onClick={handleLandlordClick}>
            Tengo un Alquiler
          </Button>
        </Col>
      </Row>
    </Container>
  );
}

export default Welcome;