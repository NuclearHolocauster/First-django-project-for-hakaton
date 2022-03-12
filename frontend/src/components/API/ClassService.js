import axios from 'axios'

export default class ClassService{
    static async getAll(){
        const responce = await axios.get("http://127.0.0.1:8000/api/room/all");
        return responce.data
    }

    static async getRoomInfo(roomId){
        const responce = await axios.get(`http://127.0.0.1:8000/api/equipment/all?audience_number=${roomId}`);
        return responce.data
    }
}