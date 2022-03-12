import React, { useEffect, useState } from 'react'
import ClassService from '../components/API/ClassService'
import DefClassCard from '../components/DefClassCard'

const DefClass = () => {
  let [classes, setClasses] = useState([])

  async function fetchClass() {
    const response = await ClassService.getAll()
    setClasses(response)
  }

  useEffect(() => {
    fetchClass()
  }, [])

  return (
    <div >
      <h1 style={{'textAlign': 'center'}}>Все аудитории</h1>
      <div className='defClass'>
        {
          classes.map(room => 
            <DefClassCard room={room} key={room.audience_number}/>
          )
        }
      </div>
    </div>
  )
}

export default DefClass