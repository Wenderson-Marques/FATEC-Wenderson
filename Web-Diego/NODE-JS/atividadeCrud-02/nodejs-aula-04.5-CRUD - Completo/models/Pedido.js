import mongoose from "mongoose"

const pedido = new mongoose.Schema({
    id: String,
    numero: String,
    valor: String
})

export default pedido