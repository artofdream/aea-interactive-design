import { Link } from "react-router-dom";
import Hours from "../components/Hours.jsx";
import NewsletterForm from "../components/NewsletterForm.jsx";
import { restaurant } from "../data/restaurant.js";

export default function Contact() {
  return (
    <section className="wrap">
      <p className="kicker">Find us</p>
      <h1 className="section-title">Contact</h1>
      <div className="grid-2">
        <article className="card contact-card">
          <h2>{restaurant.name}</h2>
          <p>{restaurant.address.street}</p>
          <p>{restaurant.address.suite}</p>
          <p>
            {restaurant.address.city} {restaurant.address.zip}
          </p>
          <p>
            Phone: <a href={restaurant.phoneHref}>{restaurant.phone}</a>
          </p>
          <Hours />
          <p style={{ marginTop: "1rem" }}>
            <Link className="btn" to="/reservations">
              Reserve a table
            </Link>
          </p>
        </article>
        <article className="card">
          <h2>Newsletter</h2>
          <p className="muted">
            Leave an email. We validate the format and store it for future notes from the
            café.
          </p>
          <NewsletterForm />
        </article>
      </div>
    </section>
  );
}
