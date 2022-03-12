import React from 'react'
import cl from './MyModal.module.css'
import close from '../../../images/close.png'


const MyModal = ({children, visible, setVisible}) => {

  const rootingClass = [cl.myModal]
  
  if (visible) {
    rootingClass.push(cl.active)
  }

  return (
    <div className={rootingClass.join(' ')}>
        <div className={cl.myModalContent}>
          <img src={close} onClick={() => setVisible(false)} style={{'cursor': 'pointer'}} />
          {children}
        </div>
    </div>
  )
}

export default MyModal