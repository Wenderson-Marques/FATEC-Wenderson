import mongoose from "mongoose"
import produto from "../models/Produto.js"

const Produto = mongoose.model("Produto", produto)

class ProdutoService {

}

export default new ProdutoService()