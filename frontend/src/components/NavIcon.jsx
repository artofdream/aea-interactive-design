import React from "react";

const ICONS = {
  home: (
    <path d="M4.5 11.2 12 4.8l7.5 6.4v8.5h-5.2v-5.1H9.7v5.1H4.5v-8.5z" />
  ),
  menu: (
    <path d="M5 7h14v1.8H5V7zm0 4.1h14v1.8H5v-1.8zm0 4.1h10v1.8H5V15.2z" />
  ),
  reservations: (
    <path d="M7.2 4.5h1.7v1.6h6.2V4.5h1.7v1.6H19v13.4H5V6.1h2.2V4.5zm10.1 5.1H6.7v7.2h10.6V9.6z" />
  ),
  about: (
    <path d="M12 5.2a2.4 2.4 0 1 1 0 4.8 2.4 2.4 0 0 1 0-4.8zm0 5.8c3.1 0 5.6 1.6 5.6 3.6v1.7H6.4V14.6c0-2 2.5-3.6 5.6-3.6z" />
  ),
  gallery: (
    <path d="M5 7.2h9.4v9.6H5V7.2zm10.2 2.2H19v9.6h-8.6v-1.8h4.8V9.4z" />
  ),
};

export default function NavIcon({ name }) {
  return (
    <svg
      className="nav-icon"
      viewBox="0 0 24 24"
      width="20"
      height="20"
      fill="currentColor"
      aria-hidden="true"
      focusable="false"
    >
      {ICONS[name]}
    </svg>
  );
}
