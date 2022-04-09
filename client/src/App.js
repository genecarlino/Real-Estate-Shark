import React from "react";
import Home from "./containers/Home";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Payments from "./containers/Payments";
import Maintanence from "./containers/Maintanence";
import Apartments from "./containers/Apartments";
import Account from "./containers/Account";
import About from "./containers/About";
import Contact from "./containers/Contact";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/Account" element={<Account />} />
        <Route exact path="/Payments" element={<Payments />} />
        <Route exact path="/About" element={<About />} />
        <Route exact path="/Contact" element={<Contact />} />
        <Route exact path="/Apartments" element={<Apartments />} />
        <Route exact path="/Maintanence" element={<Maintanence />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
