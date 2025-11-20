const CartItem = require('../models/CartItem');

exports.getCart = async (req, res) => {
  const items = await CartItem.find();
  const totalItems = items.reduce((s, it) => s + it.quantity, 0);
  const totalAmount = items.reduce((s, it) => s + it.price * it.quantity, 0);
  res.json({ items, totalItems, totalAmount });
};

exports.addToCart = async (req, res) => {
  const { productId, title, price, image, category, quantity = 1 } = req.body;
  // check if product already in cart -> increment qty
  const existing = await CartItem.findOne({ productId });
  if (existing) {
    existing.quantity += quantity;
    await existing.save();
    return res.status(200).json(existing);
  }
  const item = new CartItem({ productId, title, price, image, category, quantity });
  await item.save();
  res.status(201).json(item);
};

exports.removeFromCart = async (req, res) => {
  const id = req.params.id;
  await CartItem.findByIdAndDelete(id);
  res.json({ success: true });
};
