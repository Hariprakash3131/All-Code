import React from 'react';
import { Navbar, Container, Nav, Badge } from 'react-bootstrap';
import { backend } from '../api/api';

export default function AppNavbar({ cartSignal }) {
  const [totals, setTotals] = React.useState({ totalItems:0, totalAmount:0 });

  const loadCart = async () => {
    const res = await backend.get('/cart');
    setTotals({ totalItems: res.data.totalItems, totalAmount: res.data.totalAmount });
  };

  React.useEffect(() => {
    loadCart();
  }, [cartSignal]); // parent increments cartSignal to force refresh

  return (
    <Navbar bg="light" expand="lg" className="mb-4">
      <Container>
        <Navbar.Brand>Mini Store</Navbar.Brand>
        <Nav className="ms-auto">
          <Nav.Item className="me-3">
            Items <Badge bg="secondary">{totals.totalItems}</Badge>
          </Nav.Item>
          <Nav.Item>
            Total <Badge bg="success">₹{totals.totalAmount.toFixed(2)}</Badge>
          </Nav.Item>
        </Nav>
      </Container>
    </Navbar>
  );
}
