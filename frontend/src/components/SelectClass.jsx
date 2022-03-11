import Select from 'react-select'
import CreatableSelect from 'react-select//creatable'
import React from 'react'
import cl from '../styles/selectClass.module.css'
import { Link } from 'react-router-dom'

const SelectClass = () => {

    const options1 = [
        { value: '10', label: '10' },
        { value: '20', label: '20' },
        { value: '30', label: '30' }
    ]

    const options2 = [
        { value: '10', label: 'Столы' },
        { value: '20', label: 'Стулья' },
        { value: '30', label: 'Компьютеры' }
    ]

    const options3 = [
        { value: '10', label: 'Музыкальная репетиция' },
        { value: '20', label: 'Мероприятие' },
        { value: '30', label: 'Театральная репитиция' }
    ]

    return (
        <div className={cl.selectClassContent}>
            <h2 className={cl.firstTitle}>Подобрать аудиторию</h2>
            <p className={cl.selectClassDesc}>На этом сайте вы можете выбрат необходимую аудиторию для вашего сайта</p>
            <form action="">
                <Select 
                    options={options1}
                    placeholder=''
                    defaultInputValue='10'
                />
                <CreatableSelect 
                    isMulti
                    options={options2}/>
                <Select options={options3} />
                <Link to="">Подобрать</Link>
            </form>
        </div>
    )
}

export default SelectClass