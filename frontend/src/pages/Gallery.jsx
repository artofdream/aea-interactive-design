import React, { useState } from "react";
import freeze from "@shared/freeze.json";
import Lightbox from "../components/Lightbox.jsx";

export default function Gallery() {
  const [active, setActive] = useState(null);
  const images = freeze.officialImages;

  return (
    <article>
      <h1>Gallery</h1>
      <p>Official course images only (four webps). Click an image to enlarge.</p>
      <div className="gallery-grid">
        {images.map((image) => (
          <figure key={image.file}>
            <button type="button" onClick={() => setActive(image)} aria-label={`Enlarge ${image.alt}`}>
              <img src={`/images/${image.file}`} alt={image.alt} width="480" height="320" />
            </button>
            <figcaption className="caption">{image.caption}</figcaption>
          </figure>
        ))}
      </div>
      <Lightbox image={active} onClose={() => setActive(null)} />

      <h2>Awards</h2>
      <ul className="awards">
        {freeze.awards.map((award) => (
          <li key={award}>{award}</li>
        ))}
      </ul>

      <h2>Customer reviews</h2>
      {freeze.reviews.map((review) => (
        <blockquote key={review.attribution}>
          “{review.quote}” — {review.attribution}
        </blockquote>
      ))}
    </article>
  );
}
