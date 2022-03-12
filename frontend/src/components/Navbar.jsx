import React from 'react'
import { Link } from "react-router-dom";
import logo from '../images/logo.png'

const Navbar = () => {
  return (
    <div>
        <nav>
            <ul className='navbarLeft'>
                <li><Link to="/"><img src={logo}/></Link></li>
                <li className='navLink'><Link to="/">ГЛАВНАЯ</Link></li>
                <li className='navLink'><Link to="#">САЙТ СИБГУ ИМ. М.Ф. РЕШЕТНЕВА</Link></li>
                <li className='navLink'><Link to="#">СВЕДЕНИЯ ОБ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ</Link></li>
            </ul>
            <ul className='navbarRight'>
                <li><Link to="">Вход</Link></li>
            </ul>
        </nav>
    </div>
  )
}

export default Navbar