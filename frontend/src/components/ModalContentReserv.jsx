import React from 'react'
import ModalContentInfo from './ModalContentInfo'
import ModalContResForm from './ModalContResForm'

const ModalContentReserv = ({room, roomInfo}) => {	
  return (
    <div>
      <ModalContentInfo room={room} roomInfo={roomInfo} />
      <ModalContResForm room={room}/>
    </div> 
  )
}

export default ModalContentReserv