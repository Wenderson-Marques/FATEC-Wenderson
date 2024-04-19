import mongoose from "mongoose"
import produto from "../models/Produto.js"

const Produto = mongoose.model("Produto", produto)

class ProdutoService {
    // Método para SELECIONAR TODOS os Clientes no banco
    SelectAll() {
        const produtos = Produto.find()
        return produtos
    }

    // Método para CADASTRAR um Cliente
    Create(nome, cpf, endereco) {
        const novoProduto = new Produto({
            nome : nome,
            cpf : cpf,
            endereco : endereco
        })
        novoProduto.save()
    }
    

    // Método para EXCLUIR um Cliente
    Delete(id) {
        Produto.findByIdAndDelete(id).then(() => {
            console.log(`Produto com a id: ${id} foi deletado com sucesso.`)
        }).catch(err => {
            console.log(err)
        })
    }

    // Método para SELECIONAR um cliente ÚNICO
    SelectOne(id){
        const produto = Produto.findOne({_id : id})
        return produto
    }

    // Método para ALTERAR um cliente
    Update(id, nome, cpf, endereco) {
        Produto.findByIdAndUpdate(id, {
            nome : nome,
            cpf : cpf,
            endereco : endereco
        }).then(() => {
            console.log(`Dados do produto com id: ${id} alterados com sucesso!`)
        }).catch(err => {
            console.log(err)
        })
    }
}

export default new ProdutoService()