import React from 'react'
import cl from './MyModal.module.css'


const MyModal = ({children, visible, setVisible}) => {

  const rootingClass = [cl.myModal]
  
  if (visible) {
    rootingClass.push(cl.active)
  }

  return (
    <div className={rootingClass.join(' ')} onClick={() => setVisible(false)}>
        <div className={cl.myModalContent}>
            {children}
            Привет
        </div>
    </div>
  )
}

export default MyModal