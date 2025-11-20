import React from 'react';
import { Button, Card } from 'react-bootstrap';
import { backend } from '../api/api';

export default function ProductCard({ product, onShowDetails, onCartUpdated }) {
  const handleAddToCart = async () => {
    try {
      await backend.post('/cart', {
        productId: product.id,
        title: product.title,
        price: product.price,
        image: product.image,
        category: product.category,
        quantity: 1
      });
      // inform parent to refresh totals
      onCartUpdated && onCartUpdated();
    } catch (err) {
      console.error(err);
      alert('Failed to add to cart');
    }
  };

  return (
    <Card className="h-100">
      <div style={{height:200,display:'flex',alignItems:'center',justifyContent:'center'}}>
        <Card.Img variant="top" src={product.image} style={{maxHeight:180, width:'auto', objectFit:'contain'}}/>
      </div>
      <Card.Body className="d-flex flex-column">
        <Card.Title style={{fontSize: '0.95rem'}}>{product.title}</Card.Title>
        <Card.Text className="mt-auto">
          <strong>₹{product.price.toFixed(2)}</strong>
        </Card.Text>
        <div className="d-flex gap-2">
          <Button variant="primary" onClick={() => onShowDetails(product)}>Details</Button>
          <Button variant="outline-success" onClick={handleAddToCart}>Add to Cart</Button>
        </div>
      </Card.Body>
    </Card>
  );
}
