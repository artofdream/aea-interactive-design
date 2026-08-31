import { Link } from "react-router-dom";
import { officialImages } from "../data/gallery.js";
import { restaurant } from "../data/restaurant.js";
import Hours from "../components/Hours.jsx";

export default function Home() {
  return (
    <>
      <section className="hero">
        <img src={officialImages.home} alt="Café Fausse" />
        <div className="hero-shade" />
        <div className="hero-copy">
          <p className="kicker">Washington, DC · Est. {restaurant.founded}</p>
          <h1>{restaurant.name}</h1>
          <p className="lede">
            Traditional Italian flavors with modern culinary innovation. An unforgettable
            dining experience that reflects both quality and creativity.
          </p>
          <div className="btn-row">
            <Link className="btn" to="/reservations">
              Reserve a table
            </Link>
            <Link className="btn secondary" to="/menu">
              View the menu
            </Link>
          </div>
        </div>
      </section>

      <section className="wrap">
        <div className="grid-2">
          <article className="card contact-card">
            <h2 className="section-title">Visit us</h2>
            <p>{restaurant.address.street}</p>
            <p>{restaurant.address.suite}</p>
            <p>
              {restaurant.address.city} {restaurant.address.zip}
            </p>
            <p>
              <a href={restaurant.phoneHref}>{restaurant.phone}</a>
            </p>
            <Hours />
          </article>
          <article className="card">
            <h2 className="section-title">Tonight at the café</h2>
            <p>
              Thirty tables. Half-hour seatings from 5:00 PM. Sunday service ends at 9:00 PM;
              Monday through Saturday we welcome guests until 11:00 PM.
            </p>
            <p>
              <Link to="/gallery">See the dining room</Link> ·{" "}
              <Link to="/about">Meet the owners</Link> ·{" "}
              <Link to="/contact">Contact</Link>
            </p>
          </article>
        </div>
      </section>
    </>
  );
}
