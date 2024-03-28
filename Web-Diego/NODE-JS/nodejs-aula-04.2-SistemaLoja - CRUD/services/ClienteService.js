import mongoose from "mongoose"
import cliente from "../models/Cliente.js"

const Cliente = mongoose.model("Cliente", cliente)

class ClienteService {
    //método para selecionar todos os clientes no banco 
    SelectAll(){
        const clientes = Cliente.find()
        return clientes
    }

}

export default new ClienteService()