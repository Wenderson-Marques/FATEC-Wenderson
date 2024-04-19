import express from "express"
import bcrypt from "bcrypt"
const router = express.Router()
import UserService from "../services/UserService.js"

// ROTA DE LOGIN
router.get("/login", (req, res) => {
    res.render("login")
})

// ROTA DE CADASTRO
router.get("/cadastro", (req, res) => {
    res.render("cadastro")
})

// ROTA DE CRIAÇÃO DE USUÁRIO NO BANCO
router.post("/createUser", (req, res) => {
    // Coletando as informações do corpo da requisição
    const email = req.body.email
    const password = req.body.password
    UserService.Create(email, password)
    res.redirect("/login")
})

export default router