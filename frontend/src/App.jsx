import React from "react";
import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout.jsx";
import Home from "./pages/Home.jsx";
import Menu from "./pages/Menu.jsx";
import Reservations from "./pages/Reservations.jsx";
import About from "./pages/About.jsx";
import Gallery from "./pages/Gallery.jsx";
import Operator from "./pages/Operator.jsx";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/reservations" element={<Reservations />} />
        <Route path="/about" element={<About />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="/operator" element={<Operator />} />
      </Route>
    </Routes>
  );
}
