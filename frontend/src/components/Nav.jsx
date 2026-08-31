import { useState } from "react";
import { NavLink } from "react-router-dom";
import { restaurant } from "../data/restaurant.js";

const LINKS = [
  { to: "/menu", label: "Menu" },
  { to: "/reservations", label: "Reservations" },
  { to: "/about", label: "About Us" },
  { to: "/gallery", label: "Gallery" },
  { to: "/contact", label: "Contact" },
];

export default function Nav() {
  const [open, setOpen] = useState(false);

  return (
    <header className="site-header">
      <div className="header-inner">
        <NavLink className="brand" to="/" onClick={() => setOpen(false)}>
          {restaurant.name}
        </NavLink>
        <button
          type="button"
          className="nav-toggle"
          aria-expanded={open}
          aria-controls="site-nav"
          onClick={() => setOpen((v) => !v)}
        >
          Menu
        </button>
        <nav id="site-nav" aria-label="Primary">
          <ul className={open ? "nav-list open" : "nav-list"}>
            {LINKS.map((link) => (
              <li key={link.to}>
                <NavLink to={link.to} onClick={() => setOpen(false)}>
                  {link.label}
                </NavLink>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </header>
  );
}
