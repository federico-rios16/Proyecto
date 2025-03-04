import React from 'react';
import { Container, Row, Col, Button, Form } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import Map from './Map';

function Dashboard() {
  const navigate = useNavigate();

  const handleSupportClick = () => {
    navigate('/support');
  };

  const handleWalletClick = () => {
    navigate('/wallet');
  };

  return (
    <Container className="mt-5">
      <h1>Bienvenido al Dashboard</h1>
      <Row className="mt-4">
        <Col md={8}>
          <h2>Últimos Alquileres Cargados</h2>
          {/* Aquí iría el código para mostrar los últimos alquileres */}
        </Col>
        <Col md={4}>
          <h2>Opciones</h2>
          <Button variant="primary" className="mb-2" onClick={handleSupportClick}>
            Soporte Técnico
          </Button>
          <Button variant="secondary" onClick={handleWalletClick}>
            Billetera
          </Button>
        </Col>
      </Row>
      <Row className="mt-4">
        <Col>
          <h2>Buscar Alquileres</h2>
          <Form>
            <Row>
              <Col>
                <Form.Control placeholder="Precio Mínimo" />
              </Col>
              <Col>
                <Form.Control placeholder="Precio Máximo" />
              </Col>
              <Col>
                <Form.Control placeholder="Tipo de Departamento" />
              </Col>
              <Col>
                <Button variant="success">Buscar</Button>
              </Col>
            </Row>
          </Form>
        </Col>
      </Row>
      <Row className="mt-4">
        <Col>
          <h2>Mapa de Alquileres</h2>
          <Map />
        </Col>
      </Row>
    </Container>
  );
}

export default Dashboard;