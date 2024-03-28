import mongoose from "mongoose"
import pedido from "../models/Pedido.js"

const Pedido = mongoose.model("Pedido", pedido)

class PedidoService {

}

export default new PedidoService()