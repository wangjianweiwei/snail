import axios from "axios";


const request = axios.create({
    baseURL: "http://me-api.ifmatch.top"
})

export default request
