import { restaurant } from "../data/restaurant.js";

export default function About() {
  return (
    <section className="wrap">
      <p className="kicker">Since {restaurant.founded}</p>
      <h1 className="section-title">About Us</h1>
      <p style={{ maxWidth: "40rem", fontSize: "1.15rem" }}>{restaurant.history}</p>
      <p>{restaurant.commitment}</p>
      <div className="grid-2" style={{ marginTop: "2rem" }}>
        {restaurant.owners.map((owner) => (
          <article className="owner-card" key={owner.name}>
            <h2>{owner.name}</h2>
            <p className="muted">{owner.role}</p>
            <p>{owner.bio}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
