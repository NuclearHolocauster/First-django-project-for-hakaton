import React, { useState } from 'react'
import people from '../images/people.png'
import MyModal from './UI/MyModal/MyModal'
import ModalContentReserv from './ModalContentReserv'
import ClassService from './API/ClassService'

const DefClassCard = ({room}) => {

  let [modalVisible, setModalVisible] = useState(false)
  let [roomInfo, setRoomInfo] = useState([])

  async function fetchRoomInfo(audience_number) {
    const response = await ClassService.getRoomInfo(audience_number)
    setRoomInfo(response)
  }

  return (
    <div>
        <div className='defClassCardContent'>
          <img src={people} alt="" width='80' height='70' />
          {room.audience_number}<br/>Вметимость: {room.capacity} человек
        </div>
        <div className='toBook' onClick={() => {setModalVisible(true); fetchRoomInfo(room.audience_number)}}>Подробнее</div>
        <MyModal visible={modalVisible} setVisible={setModalVisible}>
          <ModalContentReserv room={room} roomInfo={roomInfo}/>
        </MyModal>
    </div>
  )
}

export default DefClassCard