import React from "react";

const ICONS = {
  home: (
    <path d="M4.5 11.2 12 4.8l7.5 6.4v8.5h-5.2v-5.1H9.7v5.1H4.5v-8.5z" />
  ),
  menu: (
    <path d="M6 4.8h12v1.7H6V4.8zm0 3.3h12v11.1H6V8.1zm2.1 2.2v1.5h7.8v-1.5H8.1zm0 3.2v1.5h5.6v-1.5H8.1z" />
  ),
  reservations: (
    <path d="M7.2 4.5h1.7v1.6h6.2V4.5h1.7v1.6H19v13.4H5V6.1h2.2V4.5zm10.1 5.1H6.7v7.2h10.6V9.6z" />
  ),
  about: (
    <path d="M12 5.2a2.4 2.4 0 1 1 0 4.8 2.4 2.4 0 0 1 0-4.8zm0 5.8c3.1 0 5.6 1.6 5.6 3.6v1.7H6.4V14.6c0-2 2.5-3.6 5.6-3.6z" />
  ),
  gallery: (
    <path d="M4.8 6.2h10.4v8.8H4.8V6.2zm1.7 6.5 2.2-2.8 1.7 2 1.4-1.2 2.5 2H6.5zm10.1-3.3H19v10.4H8.4v-1.7h8.2V9.4z" />
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
