
import './App.css'
import './card.css'
  import React from "react";


function App() {
  



  return (
  <div className="card">
      <div className="card-image">
        <img 
          src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80" 
          alt="Swiss Alps Retreat"
        />
        <div className="card-overlay">
          <div className="card-content">
            <h2 className="card-title">Swiss Alps Retreat</h2>
            <div className="card-price">$7.100</div>
            <div className="card-details">
              <span className="card-tag">Luxury Stay</span>
              <span className="card-duration">2 Day stay</span>
            </div>
            <button className="card-button">Reserve</button>
          </div>
        </div>
      </div>
    </div>
      
  );
};
 


export default App
