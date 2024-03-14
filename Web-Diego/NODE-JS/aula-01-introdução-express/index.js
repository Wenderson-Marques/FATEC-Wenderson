// importando o express
const express = require("express")
// iniciando o express dentro da variavel app
const app = express()

//criando a primeira rota do site (rota principal )
app.get("/",(req, res )=>{
    res.send("<h1>Seja bem vindo</h1>")
})

//rota de Prefil 
app.get("/perfil/:nome",(req,res)=>{
    res.send(req.params.nome)
})

// Rota videos 
//rota de Prefil 
app.get("/video",(req,res)=>{
    res.send("<h1>Essa é a pagoma de videos </h1>")
})
app.listen(8080, erro =>{
    if(erro){
        console.log("Ocorreu um erro")
    }
    else{
        console.log("O servidor foi iniciado com sucesso !!!!!!!!")
    }
})