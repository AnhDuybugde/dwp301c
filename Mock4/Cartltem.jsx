import React from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  removeItem,
  selectCartCount,
  selectCartItems,
  selectCartTotal,
  updateQuantity
} from "./CartSlice";

function Cartltem() {
  const dispatch = useDispatch();
  const cartItems = useSelector(selectCartItems);
  const totalItems = useSelector(selectCartCount);
  const totalCost = useSelector(selectCartTotal);

  const handleCheckout = () => {
    alert("Thank you for shopping with Paradise Nursery!");
  };

  return (
    <section className="cart-page">
      <h1>Shopping Cart</h1>
      <p>Total items: {totalItems}</p>
      <p>Total cost: ${totalCost.toFixed(2)}</p>

      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <div className="cart-items">
          {cartItems.map((item) => (
            <article className="cart-item" key={item.id}>
              <img src={item.image} alt={item.name} />
              <div>
                <h2>{item.name}</h2>
                <p>Unit cost: ${item.price.toFixed(2)}</p>
                <p>Subtotal: ${(item.price * item.quantity).toFixed(2)}</p>
              </div>
              <div className="quantity-controls">
                <button
                  type="button"
                  onClick={() =>
                    dispatch(
                      updateQuantity({
                        id: item.id,
                        quantity: item.quantity - 1
                      })
                    )
                  }
                >
                  -
                </button>
                <span>{item.quantity}</span>
                <button
                  type="button"
                  onClick={() =>
                    dispatch(
                      updateQuantity({
                        id: item.id,
                        quantity: item.quantity + 1
                      })
                    )
                  }
                >
                  +
                </button>
              </div>
              <button type="button" onClick={() => dispatch(removeItem(item.id))}>
                Delete
              </button>
            </article>
          ))}
        </div>
      )}

      <div className="cart-actions">
        <button type="button" onClick={() => (window.location.hash = "#products")}>
          Continue Shopping
        </button>
        <button type="button" onClick={handleCheckout}>
          Checkout
        </button>
      </div>
    </section>
  );
}

export default Cartltem;
