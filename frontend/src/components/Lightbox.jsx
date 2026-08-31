import React, { useEffect } from "react";

export default function Lightbox({ image, onClose }) {
  useEffect(() => {
    if (!image) {
      return undefined;
    }
    function onKey(event) {
      if (event.key === "Escape") {
        onClose();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [image, onClose]);

  if (!image) {
    return null;
  }

  return (
    <div className="lightbox" role="dialog" aria-modal="true" aria-label={image.alt} onClick={onClose}>
      <button type="button" className="lightbox-close" onClick={onClose}>
        Close
      </button>
      <img src={`/images/${image.file}`} alt={image.alt} onClick={(event) => event.stopPropagation()} />
    </div>
  );
}
