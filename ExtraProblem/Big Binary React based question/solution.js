import React, { useState, useEffect } from "react";

// Assume fetchData() is available and returns a Promise resolving to JSON data

function PopularProducts() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPopularProducts = async () => {
      try {
        setLoading(true);
        setError(null);

        const data = await fetchData(); // API call

        // Sort by popularityScore (descending) and take top 5
        const topProducts = data
          .sort((a, b) => b.popularityScore - a.popularityScore)
          .slice(0, 5);

        setProducts(topProducts);
      } catch (err) {
        setError("Failed to load popular products.");
      } finally {
        setLoading(false);
      }
    };

    fetchPopularProducts();
  }, []); // Runs when component mounts (homepage navigation)

  if (loading) {
    return <p>Loading popular products...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
    <div>
      <h2>🔥 Top 5 Popular Products</h2>
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            <strong>{product.productName}</strong> <br />
            Price: ₹{product.price} <br />
            Popularity Score: {product.popularityScore}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PopularProducts;
