import React from "react";
import freeze from "@shared/freeze.json";
import presentation from "@shared/menu-presentation.json";

function formatPrice(price) {
  return `$${price}`;
}

function MenuPhoto({ item }) {
  const visual = presentation.items[item.name];
  if (!visual || visual.kind === "placeholder" || !visual.file) {
    return (
      <div className="menu-item-placeholder" role="img" aria-label={`${item.name}: no matching photo`}>
        <span>No matching photo</span>
      </div>
    );
  }
  return (
    <img
      className="menu-item-photo"
      src={`/images/${visual.file}`}
      alt={visual.alt || item.name}
      width="240"
      height="240"
    />
  );
}

function MenuCaption({ item }) {
  const visual = presentation.items[item.name];
  if (!visual) {
    return null;
  }
  return <p className="menu-item-caption">{visual.caption}</p>;
}

export default function Menu() {
  return (
    <article className="menu-page">
      <h1>Menu</h1>
      <p className="menu-honesty">
        Names, descriptions, and prices are the official SRS freeze (FR-5). Photos are
        presentation aids only. Ribeye reuses the Quantic-official gallery dish. Other
        photos are student-recovered extras and are <strong>not Quantic-official</strong>.
        Bruschetta has no matching photo.
      </p>
      {freeze.menu.map((category) => (
        <section className="menu-category" key={category.category}>
          <h2>{category.category}</h2>
          <ul className="menu-list">
            {category.items.map((item) => (
              <li className="menu-item" key={item.name}>
                <MenuPhoto item={item} />
                <strong>{item.name}</strong>
                <span className="price">{formatPrice(item.price)}</span>
                <p>{item.description}</p>
                <MenuCaption item={item} />
              </li>
            ))}
          </ul>
        </section>
      ))}
    </article>
  );
}
