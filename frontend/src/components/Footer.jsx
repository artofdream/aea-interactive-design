import { Link } from "react-router-dom";
import { restaurant } from "../data/restaurant.js";
import NewsletterForm from "./NewsletterForm.jsx";

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-inner">
        <div>
          <h2>{restaurant.name}</h2>
          <p>{restaurant.address.line}</p>
          <p>
            <a href={restaurant.phoneHref}>{restaurant.phone}</a>
          </p>
          <p className="muted">{restaurant.hoursLine}</p>
        </div>
        <div>
          <h2>Visit</h2>
          <p>
            <Link to="/menu">Menu</Link>
          </p>
          <p>
            <Link to="/reservations">Reservations</Link>
          </p>
          <p>
            <Link to="/about">About Us</Link>
          </p>
          <p>
            <Link to="/gallery">Gallery</Link>
          </p>
          <p>
            <Link to="/contact">Contact</Link>
          </p>
        </div>
        <div>
          <h2>Newsletter</h2>
          <p>Occasional notes from the dining room. Email only; we store it on our backend.</p>
          <NewsletterForm compact />
        </div>
      </div>
    </footer>
  );
}
