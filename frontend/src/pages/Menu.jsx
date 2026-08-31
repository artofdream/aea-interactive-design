import React from "react";
import freeze from "@shared/freeze.json";

function formatPrice(price) {
  return `$${price}`;
}

export default function Menu() {
  return (
    <article className="menu-page">
      <h1>Menu</h1>
      {freeze.menu.map((category) => (
        <section className="menu-category" key={category.category}>
          <h2>{category.category}</h2>
          <ul className="menu-list">
            {category.items.map((item) => (
              <li className="menu-item" key={item.name}>
                <strong>{item.name}</strong>
                <span className="price">{formatPrice(item.price)}</span>
                <p>{item.description}</p>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </article>
  );
}
