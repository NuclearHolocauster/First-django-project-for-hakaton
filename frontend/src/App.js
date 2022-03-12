import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Booking from "./pages/Booking";
import DefClass from "./pages/DefClass";
import './styles/App.css'


function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Booking/>}/>
        <Route path="/def-classes" element={<DefClass />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
