import express from "express"
const router = express.Router()
import ProdutoService from "../services/ProdutoService.js"

// ROTA 
router.get("/produtos", function(req, res){
    ProdutoService.SelectAll().then((produtos) =>{
        res.render("produtos", {
            produtos : produtos
        })
    })
})

// ROTA DE CADASTRO DE produtos
router.post("/produtos/new", (req, res) => {
    ProdutoService.Create(
        req.body.nome,
        req.body.cpf,
        req.body.endereco
    )
    res.redirect("/produtos")
})

// ROTA DE EXCLUSÃO DE produto
router.get("/produtos/delete/:id", (req, res) => {
    const id = req.params.id
    ProdutoService.Delete(id)
    res.redirect("/produtos")
})

// ROTA DE EDIÇÃO DE 
router.get("/produtos/edit/:id", (req, res) => {
    const id = req.params.id
    ProdutoService.SelectOne(id).then((produto) => {
        res.render("produtoEdit", {
            produto : produto
        })
    })
})

// ROTA DE ALTERAÇÃO DE 
router.post("/produto/update/:id", (req, res) => {
    ProdutoService.Update(
        req.body.id,
        req.body.nome,
        req.body.cpf,
        req.body.endereco
    )
    res.redirect("/produtos")
})

export default router //exportando o módulo "router"