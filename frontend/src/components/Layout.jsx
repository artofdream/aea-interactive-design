import React from "react";
import { Link, NavLink, Outlet } from "react-router-dom";
import freeze from "@shared/freeze.json";
import NewsletterForm from "./NewsletterForm.jsx";

const LINKS = [
  { to: "/menu", label: "Menu" },
  { to: "/reservations", label: "Reservations" },
  { to: "/about", label: "About Us" },
  { to: "/gallery", label: "Gallery" },
];

export default function Layout() {
  return (
    <>
      <header className="site-header">
        <Link className="wordmark" to="/">
          {freeze.name}
        </Link>
        <nav className="site-nav" aria-label="Primary">
          {LINKS.map((link) => (
            <NavLink key={link.to} to={link.to}>
              {link.label}
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
      </footer>
    </>
  );
}
