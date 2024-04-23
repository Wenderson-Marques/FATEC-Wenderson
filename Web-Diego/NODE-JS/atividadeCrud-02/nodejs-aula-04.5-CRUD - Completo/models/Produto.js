import mongoose from "mongoose"

const produto = new mongoose.Schema({
    nome: String,
    valor: String,
    descricao: String
})

export default produto