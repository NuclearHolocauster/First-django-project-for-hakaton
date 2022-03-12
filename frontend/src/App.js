import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Booking from "./pages/Booking";
import Catalog from "./pages/Catalog";
import './styles/App.css'


function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        {/* <Route path="/" element={<Catalog/>}/> */}
        <Route path="/booking-class" element={<Booking/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
