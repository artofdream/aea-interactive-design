import Footer from "./Footer.jsx";
import Nav from "./Nav.jsx";

export default function Layout({ children }) {
  return (
    <>
      <a className="skip-link" href="#main">
        Skip to content
      </a>
      <Nav />
      <main id="main" className="site-main">
        {children}
      </main>
      <Footer />
    </>
  );
}
