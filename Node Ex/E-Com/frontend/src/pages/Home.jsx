import React from 'react';
import axios from 'axios';

export default function Home() {
  const [products, setProducts] = React.useState([]);
  const [categories, setCategories] = React.useState([]);
  const [selectedCat, setSelectedCat] = React.useState('all');
  const [sort, setSort] = React.useState('none'); // 'asc' | 'desc' | 'none'
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    async function load() {
      setLoading(true);
      const res = await axios.get('https://fakestoreapi.com/products');
      setProducts(res.data);
      const cats = Array.from(new Set(res.data.map(p => p.category)));
      setCategories(cats);
      setLoading(false);
    }
    load();
  }, []);

  // filtering and sorting derived array
  const visible = React.useMemo(() => {
    let arr = products.slice();
    if (selectedCat !== 'all') arr = arr.filter(p => p.category === selectedCat);
    if (sort === 'asc') arr.sort((a,b) => a.price - b.price);
    if (sort === 'desc') arr.sort((a,b) => b.price - a.price);
    return arr;
  }, [products, selectedCat, sort]);

  return (
    <div className="container py-4">
      {/* controls: category filter + sort */}
      {/* product grid: map visible -> ProductCard */}
    </div>
  );
}
