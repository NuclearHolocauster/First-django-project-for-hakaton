import React, { useEffect, useState } from 'react'
import ClassService from './API/ClassService'
import ModalContentInfo from './ModalContentInfo'

const ModalContentReserv = ({room, roomInfo}) => {	
  return (
    <ModalContentInfo room={room} roomInfo={roomInfo} />
  )
}

export default ModalContentReserv