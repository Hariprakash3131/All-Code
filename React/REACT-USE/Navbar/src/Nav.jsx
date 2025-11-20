import './App.css';

function Nav() {
  return (
    <div className="navbar">
      <nav>
        <input type="checkbox" id="nav-toggle" />
        <label htmlFor="nav-toggle" className="hamburger">☰</label>

        <div className="nav-menu">
          <ul>
            <li><a href="#" className="navbar-link">Home</a></li>
            <li><a href="#" className="navbar-link">About</a></li>
            <li><a href="#" className="navbar-link">Address</a></li>
            <li><a href="#" className="navbar-link">Contact</a></li>
            <li><a href="#" className="navbar-link">Book</a></li>
          </ul>
          <div className="nav-buttons">
            <button className="button">Login</button>
            <button className="button">Signup</button>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Nav;
