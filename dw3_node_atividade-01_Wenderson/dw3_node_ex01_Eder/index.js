const express = require('express')
const app = express()

app.set("view engine","ejs")
// Middleware para servir arquivos estáticos
app.use(express.static('public'))

// Definir as rotas
app.get('/', (req, res) => {
  res.render('index')
})

app.get('/clientes', (req, res) => {
  const clientes = [
    { nome: 'Jimmy Neutron', cpf: '123.456.789-00', endereco: 'Rua A, 123' },
    { nome: 'Gilmar Ggi', cpf: '987.654.321-00', endereco: 'Rua B, 456' },
    { nome: 'Lucas Lider', cpf: '789.456.123-00', endereco: 'Rua C, 987' },
    { nome: 'Victor Von Dun', cpf: '567.890.432-00', endereco: 'Rua D, 4321' },
    
  ]
  res.render('clientes', { clientes })
})

app.get('/produtos', (req, res) => {
  const produtos = [
    { nome: 'NoteBook', preco: 3500, categoria: 'Computadores' },
    { nome: 'Gabinete', preco: 1500, categoria: 'Equipamentos' },
    { nome: 'Cadeira Gamer', preco: 2000, categoria: 'Acessórios' },
    { nome: 'Mouse Pad', preco: 80, categoria: 'Acessórios' },
    { nome: 'Mouse Gamer', preco: 150, categoria: 'Acessórios' },
    { nome: 'Monitor', preco: 2500, categoria: 'Periféricos' },
  ]
  res.render('produtos', { produtos })
})

app.get('/pedidos', (req, res) => {
  const pedidos = [
    { Pedido: 1, valor: 50.00 },
    { Pedido: 2, valor: 75.00 },
    { Pedido: 3, valor: 35.00 },
    { Pedido: 4, valor: 1200.00 },
    { Pedido: 5, valor: 880.00 },
  ]
  res.render('pedidos', { pedidos })
})

// Iniciar o servidor
app.listen(8080, (erro) => {
    if(erro){
        console.log("Ocorreu um erro")
    }else{
  console.log(`Servidor iniciado com sucesso`);
    }
})
