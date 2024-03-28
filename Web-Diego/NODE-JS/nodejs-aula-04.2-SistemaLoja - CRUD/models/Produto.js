import mongoose from "mongoose"

const produto = new mongoose.Schema({
    nome: String,
    cpf: String,
    endereco: String
})

export default produto