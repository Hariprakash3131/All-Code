const express = require('express');
const router = express.Router();
const ctrl = require('../controllers/cartController');

router.get('/', ctrl.getCart);
router.post('/', ctrl.addToCart);
router.delete('/:id', ctrl.removeFromCart);
// optionally router.put('/:id', ctrl.updateQuantity);

module.exports = router;
