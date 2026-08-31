import React from "react";
import { Link } from "react-router-dom";
import freeze from "@shared/freeze.json";

export default function Home() {
  const hero = freeze.officialImages.find((img) => img.kind === "home");
  return (
    <article>
      <section className="hero">
        <div>
          <h1>{freeze.name}</h1>
          <p className="lede">{freeze.history}</p>
          <p>
            <Link to="/reservations">Reserve a table</Link>
            {" · "}
            <Link to="/menu">View the menu</Link>
          </p>
        </div>
        <img src={`/images/${hero.file}`} alt={hero.alt} width="800" height="560" />
      </section>
      <section className="card-grid">
        <div className="card">
          <h2>Visit</h2>
          <p>{freeze.address}</p>
          <p>{freeze.phone}</p>
        </div>
        <div className="card">
          <h2>Hours</h2>
          <p>{freeze.hoursDisplay}</p>
        </div>
        <div className="card">
          <h2>Explore</h2>
          <p>
            <Link to="/about">About Us</Link>
            {" · "}
            <Link to="/gallery">Gallery</Link>
          </p>
        </div>
      </section>
    </article>
  );
}
