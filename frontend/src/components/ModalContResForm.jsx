import React, { useState } from 'react'
import ClassService from './API/ClassService'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'

const ModalContResForm = ({room}) => {

	const [startDate, setStartDate] = useState()
  	const [endDate, setEndDate] = useState()

	async function fetchResRoom(e) {
		e.preventDefault()

		const body = {
			'user': 1,
			'audience_number': room.audience_number,
			'reservation_start': new Date(startDate).toISOString(),
			'reservation_end': new Date(endDate).toISOString()
		}

    const response = await ClassService.postReservRoom(body)
		console.log(response)
  }

	return (
		<div>
			<form action="" className='formReserv'>
				{/* <FullCalendar
					plugins={[ dayGridPlugin ]}
					initialView="dayGridMonth"
					locale={'ru'}
				/> */}
				<input 
					type="text"
					placeholder='Какое мероприятие будет'
				/>
				<input 
					type="date"
					placeholder='Начальное время'
					value={startDate}
					onChange={e => setStartDate(e.target.value)}
				/>
				<input 
					type="date"
					placeholder='Конечное время'
					value={endDate}
					onChange={e => setEndDate(e.target.value)}
				/>
				<button onClick={fetchResRoom}>Забронировать</button>
			</form>
		</div>
	)
}

export default ModalContResForm