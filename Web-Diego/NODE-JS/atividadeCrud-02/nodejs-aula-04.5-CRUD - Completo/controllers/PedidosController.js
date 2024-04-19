import express from "express"
const router = express.Router()
import PedidoService from "../services/PedidoService.js"
import Pedido from "../models/Pedido.js"

// ROTA pedidoS
router.get("/pedidos", function(req, res){
    PedidoService.SelectAll().then((pedidos) =>{
        res.render("pedidos", {
            pedidos : pedidos
        })
    })
})

// ROTA DE CADASTRO DE pedidoS
router.post("/pedidos/new", (req, res) => {
    PedidoService.Create(
        req.body.numero,
        req.body.valor
    )
    res.redirect("/pedidos")
})

// ROTA DE EXCLUSÃO DE pedido
router.get("/pedidos/delete/:id", (req, res) => {
    const id = req.params.id
    PedidoService.Delete(id)
    res.redirect("/pedidos")
})

// ROTA DE EDIÇÃO DE pedido
router.get("/pedidos/edit/:id", (req, res) => {
    const id = req.params.id
    PedidoService.SelectOne(id).then((pedido) => {
        res.render("pedidoEdit", {
            pedido : pedido
        })
    })
})

// ROTA DE ALTERAÇÃO DE pedido
router.post("/pedidos/update/:id", (req, res) => {
    PedidoService.Update(
        req.body.id,
        req.body.numero,
        req.body.valor
    )
    res.redirect("/pedidos")
})
//rota para busca do ultimo numero 
router.post("/pedidos/selectLast/:numero", (req, res) => {
    PedidoService.selectLast(
        req.body.numero,
    )
    res.redirect("/pedidos")
})



export default router //exportando o módulo "router"