import React from 'react'
import cl from '../styles/DefClassCard.module.css'
import people from '../images/people.png'

const DefClassCard = ({room}) => {
  return (
    <div>
        <div className='defClassCardContent'>
          <img src={people} alt="" width='80' height='70' />
          {room.audience_number}<br/>Вметимость: {room.capacity} человек
        </div>
        <div className='toBook'>Забронировать</div>
    </div>
  )
}

export default DefClassCard