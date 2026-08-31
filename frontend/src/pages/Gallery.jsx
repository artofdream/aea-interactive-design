import { useState } from "react";
import Lightbox from "../components/Lightbox.jsx";
import { galleryItems } from "../data/gallery.js";
import { restaurant } from "../data/restaurant.js";

export default function Gallery() {
  const [active, setActive] = useState(null);

  return (
    <section className="wrap">
      <p className="kicker">The room and the plate</p>
      <h1 className="section-title">Gallery</h1>
      <p className="muted">
        Official course images first. Extra photos are labeled{" "}
        <strong>not official</strong>.
      </p>
      <div className="gallery-grid" style={{ marginTop: "1.5rem" }}>
        {galleryItems.map((item) => (
          <button
            type="button"
            className="gallery-tile"
            key={item.src}
            onClick={() => setActive(item)}
          >
            <img src={item.src} alt={item.alt} />
            {item.official ? null : <span className="badge">Not official</span>}
            <span className="tile-caption">{item.caption}</span>
          </button>
        ))}
      </div>

      <h2 className="section-title" style={{ marginTop: "2.5rem" }}>
        Awards
      </h2>
      <div className="award-grid">
        {restaurant.awards.map((award) => (
          <article className="award-card" key={award.title}>
            <h3>{award.title}</h3>
            <p className="muted">{award.year}</p>
          </article>
        ))}
      </div>

      <h2 className="section-title" style={{ marginTop: "2.5rem" }}>
        Guest reviews
      </h2>
      <div className="grid-2">
        {restaurant.reviews.map((review) => (
          <blockquote className="review" key={review.source}>
            <p>“{review.quote}”</p>
            <footer className="muted">— {review.source}</footer>
          </blockquote>
        ))}
      </div>

      <Lightbox item={active} onClose={() => setActive(null)} />
    </section>
  );
}
