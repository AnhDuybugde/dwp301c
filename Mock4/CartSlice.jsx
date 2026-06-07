import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  items: []
};

const findCartItem = (items, id) => items.find((item) => item.id === id);

const cartSlice = createSlice({
  name: "cart",
  initialState,
  reducers: {
    addItem: (state, action) => {
      const product = action.payload;
      const existingItem = findCartItem(state.items, product.id);

      if (existingItem) {
        existingItem.quantity += 1;
      } else {
        state.items.push({ ...product, quantity: 1 });
      }
    },

    removeItem: (state, action) => {
      state.items = state.items.filter((item) => item.id !== action.payload);
    },

    updateQuantity: (state, action) => {
      const { id, quantity } = action.payload;
      const existingItem = findCartItem(state.items, id);

      if (!existingItem) {
        return;
      }

      if (quantity <= 0) {
        state.items = state.items.filter((item) => item.id !== id);
      } else {
        existingItem.quantity = quantity;
      }
    },

    addltem: (state, action) => {
      cartSlice.caseReducers.addItem(state, action);
    },

    removeltem: (state, action) => {
      cartSlice.caseReducers.removeItem(state, action);
    },

    updaleQuantity: (state, action) => {
      cartSlice.caseReducers.updateQuantity(state, action);
    }
  }
});

export const {
  addItem,
  removeItem,
  updateQuantity,
  addltem,
  removeltem,
  updaleQuantity
} = cartSlice.actions;

export const selectCartItems = (state) => state.cart.items;

export const selectCartCount = (state) =>
  state.cart.items.reduce((total, item) => total + item.quantity, 0);

export const selectCartTotal = (state) =>
  state.cart.items.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

export default cartSlice.reducer;
