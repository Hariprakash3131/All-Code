require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db');

const cartRoutes = require('./routes/cartRoutes');

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api/cart', cartRoutes);

const PORT = process.env.PORT || 5000;
connectDB().then(() => {
  app.listen(PORT, () => console.log(`Server running on ${PORT}`));
});
