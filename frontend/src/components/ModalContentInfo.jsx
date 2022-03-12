import React from 'react'
import cl from '../styles/ModalContentInfo.module.css'
import imgModal from '../images/imgModal.png'

const ModalContentInfo = ({room, roomInfo}) => {
  return (
    <div className={cl.modalContentInfo}>
        <div>
            <img src={imgModal} alt="" />
        </div>
        <div>
            <h3>Аудитория {room.audience_number}</h3>
            <ul>
                <li>
                    <h4>Вместительность:</h4>
                    <p>Данная аудитория обладает вместительностью до {room.capacity} человек</p>
                </li>
                <li>
                    <h4>Что имеется в аудитории:</h4>
                    <ul>
                        {roomInfo.map(info => <li key={info.id}>{info.equipment_name}: {info.number}</li>)}
                    </ul>
                </li>
                <li style={{'marginTop': '50px'}}>
                    <h4>Оставьте заявку на бронь</h4>
                </li>
            </ul>
        </div>
    </div>
  )
}

export default ModalContentInfo