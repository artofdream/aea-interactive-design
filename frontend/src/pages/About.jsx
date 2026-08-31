import React from "react";
import freeze from "@shared/freeze.json";

export default function About() {
  return (
    <article>
      <h1>About Us</h1>
      <p>{freeze.history}</p>
      <p>{freeze.locallySourced}</p>
      <h2>Founders</h2>
      <div className="founders">
        {freeze.founders.map((person) => (
          <section className="card" key={person.name}>
            <h3>{person.name}</h3>
            <p className="hours-note">{person.role}</p>
            <p>{person.bio}</p>
          </section>
        ))}
      </div>
    </article>
  );
}
