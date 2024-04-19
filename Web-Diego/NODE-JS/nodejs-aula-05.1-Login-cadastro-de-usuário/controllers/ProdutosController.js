import express from "express"
const router = express.Router()
import ProdutoService from "../services/ProdutoService.js"

// ROTA PRODUTOS
router.get("/produtos", function(req, res){
    ProdutoService.SelectAll().then((produtos) =>{
        res.render("produtos", {
            produtos : produtos
        })
    })
})

export default router