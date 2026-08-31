import { formatPrice, menuCategories } from "../data/menu.js";

export default function Menu() {
  return (
    <section className="wrap">
      <p className="kicker">The card</p>
      <h1 className="section-title">Menu</h1>
      <p className="muted">Prices from the official Café Fausse specification.</p>
      <div className="menu-grid" style={{ marginTop: "1.5rem" }}>
        {menuCategories.map((category) => (
          <article className="menu-card" key={category.id}>
            <h2>{category.name}</h2>
            {category.items.map((item) => (
              <div className="menu-item" key={item.name}>
                <div>
                  <h3>{item.name}</h3>
                  <p className="muted">{item.description}</p>
                </div>
                <p className="price">{formatPrice(item.price)}</p>
              </div>
            ))}
          </article>
        ))}
      </div>
    </section>
  );
}
