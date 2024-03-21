// importando o express
const express = require("express")
// iniciando o express dentro da variavel app
const app = express()
app.set('view engine','ejs')

//criando a primeira rota do site (rota principal )
app.get("/",(req, res )=>{
    res.render("<h1>Seja bem vindo</h1>")
})

//rota de Prefil 
app.get("/perfil/:nome?",(req,res)=>{
    let nome=req.params.nome
    if (nome){//verificando se o parametro nome existe 
        res.send(`<h2> Olá ${nome} <br>Seja bem vindo ao seu perfil ! </h2> `)
    }
    else
    {
        res.render('perfil')
    }
    res.render('perfil',{
        nome: nome
    })
})

// Rota videos 
//rota de Prefil 
app.get("/video:playlist/:video",(req,res)=>{
    let playlist=req.params.playlist
    res.render('videos')
})

app.get("/produtos/:produto?",(req,res)=>
{
    let produtos=['computador','celular','tablet','notebook']
    let produto=req.params.produto
    res.render('produtos',
    {
        //enviando variaveis para a pagina 
        produto:produto,
        produtos : produto
    })
})


app.listen(8080, erro =>{
    if(erro){
        console.log("Ocorreu um erro")
    }
    else{
        console.log("O servidor foi iniciado com sucesso !!!!!!!!")
    }
})

//rota pedidos 
app.get('/pedidos',(req, res)=>{
    //array de objetos com os pedidos 
    const pedidos = [
        {produto:'Celular',preco:3000},{produto:'Computador',preco:4000},{produto:'tablet' , preco:2000},{produto:'notebook ', preco:3800}
    ]
    
    res.render('pedidos',
    {
        pedidos:pedidos
    })
})