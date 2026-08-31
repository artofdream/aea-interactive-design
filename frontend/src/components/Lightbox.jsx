import { useEffect } from "react";

export default function Lightbox({ item, onClose }) {
  useEffect(() => {
    if (!item) return undefined;
    function onKey(event) {
      if (event.key === "Escape") onClose();
    }
    document.addEventListener("keydown", onKey);
    const previous = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = previous;
    };
  }, [item, onClose]);

  if (!item) return null;

  return (
    <div className="lightbox" role="dialog" aria-modal="true" aria-label={item.caption} onClick={onClose}>
      <button type="button" className="lightbox-close" onClick={onClose}>
        Close
      </button>
      <figure onClick={(event) => event.stopPropagation()}>
        <img src={item.src} alt={item.alt} />
        <figcaption>
          {item.caption}
          {item.official ? "" : " — Not official (student-recovered image)"}
        </figcaption>
      </figure>
    </div>
  );
}
