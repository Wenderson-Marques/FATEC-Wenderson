import express from "express"
const router = express.Router()
import PedidoService from "../services/PedidoService.js"

// ROTA PEDIDOS
router.get("/pedidos", function(req, res){
    PedidoService.SelectAll().then((pedidos) =>{
        res.render("pedidos", {
            pedidos : pedidos
        })
    })
})

export default router

