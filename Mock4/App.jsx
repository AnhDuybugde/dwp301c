import React from "react";
import "./App.css";

function App() {
  const handleGetStarted = () => {
    window.location.hash = "#products";
  };

  return (
    <main className="landing-page">
      <div className="landing-content">
        <h1 className="company-name">Paradise Nursery</h1>
        <p className="company-tagline">
          Discover beautiful plants that make every room feel calmer, fresher,
          and closer to nature.
        </p>
        <button className="get-started-button" onClick={handleGetStarted}>
          Get Started
        </button>
      </div>
    </main>
  );
}

export default App;
