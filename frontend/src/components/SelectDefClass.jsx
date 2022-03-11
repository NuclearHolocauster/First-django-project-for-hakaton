import React from 'react'
import { Link } from 'react-router-dom'
import cl from '../styles/SelectDefClass.module.css'
import img2 from '../images/img2.png'

const SelectDefClass = () => {
  return (
    <div className={cl.selectDefClass}>
        <div className={cl.selectDefClassDesc}>
            <div>
                <h2>Знаешь какая аудитория тебе нужна?</h2>
                <p>Полный список аудиторий со всеми харатеристами  Подходит для препожователей нашего вуза, которые знают какая имеено аудитория им нужна</p>
            </div>
            <div>
                <Link to="">Выбрать</Link>
            </div>
        </div>
        <div className={cl.selectDefClassImg}>
            <img src={img2} alt="" />
        </div>
    </div>
  )
}

export default SelectDefClass