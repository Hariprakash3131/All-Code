const mongoose = require('mongoose');

const CartItemSchema = new mongoose.Schema({
  productId: { type: Number, required: true }, // fakestore product id
  title: { type: String, required: true },
  price: { type: Number, required: true },
  image: { type: String },
  quantity: { type: Number, default: 1 },
  category: { type: String },
  // optionally: userId if implementing auth
}, { timestamps: true });

module.exports = mongoose.model('CartItem', CartItemSchema);
