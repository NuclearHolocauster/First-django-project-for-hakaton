import axios from 'axios'

const baseUrl = 'http://127.0.0.1:8000/api'

export default class ClassService{
    static async getAll(){
        const responce = await axios.get(`${baseUrl}/room/all`);
        return responce.data
    }

    static async getRoomInfo(roomId){
        const responce = await axios.get(`${baseUrl}/equipment/all?audience_number=${roomId}`);
        return responce.data
    }

    static async postReservRoom(body) {
        axios.post(`${baseUrl}/reservation/create`, 
            body
        )
        .then(function (response) {
            return response;
        })
        .catch(function (error) {
            return error;
        });
    }
}