import express from "express"
const router = express.Router()
import ClienteService from "../services/ClienteService.js"

// ROTA CLIENTES
router.get("/clientes", function(req, res){
    ClienteService.SelectAll()
    res.render("clientes")
})

export default router //exportando o módulo "router"