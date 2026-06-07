import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { addItem, selectCartItems } from "./CartSlice";

const products = [
  {
    id: 1,
    name: "Snake Plant",
    category: "Air Purifying Plants",
    price: 18,
    image: "https://images.unsplash.com/photo-1593482892290-f54927ae2b51?auto=format&fit=crop&w=500&q=80"
  },
  {
    id: 2,
    name: "Peace Lily",
    category: "Air Purifying Plants",
    price: 24,
    image: "https://images.unsplash.com/photo-1593691509543-c55fb32e5cee?auto=format&fit=crop&w=500&q=80"
  },
  {
    id: 3,
    name: "Monstera",
    category: "Tropical Plants",
    price: 32,
    image: "https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=500&q=80"
  },
  {
    id: 4,
    name: "Aloe Vera",
    category: "Succulents",
    price: 14,
    image: "https://images.unsplash.com/photo-1509423350716-97f9360b4e09?auto=format&fit=crop&w=500&q=80"
  },
  {
    id: 5,
    name: "Lavender",
    category: "Flowering Plants",
    price: 16,
    image: "https://images.unsplash.com/photo-1499002238440-d264edd596ec?auto=format&fit=crop&w=500&q=80"
  },
  {
    id: 6,
    name: "Basil",
    category: "Herbs",
    price: 10,
    image: "https://images.unsplash.com/photo-1618375569909-3c8616cf7733?auto=format&fit=crop&w=500&q=80"
  }
];

function Productist() {
  const dispatch = useDispatch();
  const cartItems = useSelector(selectCartItems);
  const cartIds = cartItems.map((item) => item.id);
  const categories = [...new Set(products.map((product) => product.category))];

  return (
    <section className="product-listing" id="products">
      <header className="product-header">
        <h1>Paradise Nursery Plant Shop</h1>
        <p>Choose from our favorite plants and add them to your cart.</p>
      </header>

      {categories.map((category) => (
        <div className="product-category" key={category}>
          <h2>{category}</h2>
          <div className="product-grid">
            {products
              .filter((product) => product.category === category)
              .map((product) => {
                const isAdded = cartIds.includes(product.id);

                return (
                  <article className="product-card" key={product.id}>
                    <img src={product.image} alt={product.name} />
                    <h3>{product.name}</h3>
                    <p>${product.price.toFixed(2)}</p>
                    <button
                      type="button"
                      disabled={isAdded}
                      onClick={() => dispatch(addItem(product))}
                    >
                      {isAdded ? "Added to Cart" : "Add to Cart"}
                    </button>
                  </article>
                );
              })}
          </div>
        </div>
      ))}
    </section>
  );
}

export default Productist;
