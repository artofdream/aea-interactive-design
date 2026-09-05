import React, { useEffect, useState } from "react";
import { Link, NavLink, Outlet, useLocation } from "react-router-dom";
import freeze from "@shared/freeze.json";
import NewsletterForm from "./NewsletterForm.jsx";
import NavIcon from "./NavIcon.jsx";

const LINKS = [
  { to: "/", label: "Home", icon: "home", end: true },
  { to: "/menu", label: "Menu", icon: "menu" },
  { to: "/reservations", label: "Reservations", icon: "reservations" },
  { to: "/about", label: "About Us", icon: "about" },
  { to: "/gallery", label: "Gallery", icon: "gallery" },
];

export default function Layout() {
  const location = useLocation();
  const [navOpen, setNavOpen] = useState(false);

  useEffect(() => {
    document.documentElement.classList.add("js-nav");
    return () => document.documentElement.classList.remove("js-nav");
  }, []);

  useEffect(() => {
    setNavOpen(false);
  }, [location.pathname]);

  return (
    <>
      <header className="site-header">
        <Link className="wordmark" to="/">
          {freeze.name}
        </Link>
        <button
          type="button"
          className="nav-toggle"
          aria-expanded={navOpen}
          aria-controls="primary-nav"
          onClick={() => setNavOpen((open) => !open)}
        >
          <span className="nav-toggle-bars" aria-hidden="true">
            <span />
            <span />
            <span />
          </span>
          {navOpen ? "Close" : "Site menu"}
        </button>
        <nav
          id="primary-nav"
          className={navOpen ? "site-nav is-open" : "site-nav"}
          aria-label="Primary"
        >
          {LINKS.map((link) => (
            <NavLink key={link.to} to={link.to} end={link.end}>
              <NavIcon name={link.icon} />
              <span>{link.label}</span>
            </NavLink>
          ))}
        </nav>
      </header>
      <main className="site-main">
        <Outlet />
      </main>
      <footer className="site-footer">
        <div className="footer-grid">
          <section>
            <h2>{freeze.name}</h2>
            <p>{freeze.address}</p>
            <p>{freeze.phone}</p>
            <p>{freeze.hoursDisplay}</p>
          </section>
          <section>
            <h2>Newsletter</h2>
            <p>Email signup is stored only when PostgreSQL accepts the write.</p>
            <NewsletterForm />
          </section>
        </div>
        <p className="footer-operator">
          <Link to="/operator">Operator</Link>
        </p>
      </footer>
    </>
  );
}
