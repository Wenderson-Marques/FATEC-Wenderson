import mongoose from "mongoose"

const  pedido= new mongoose.Schema({
    nome: String,
    cpf: String,
    endereco: String
})

export default pedido