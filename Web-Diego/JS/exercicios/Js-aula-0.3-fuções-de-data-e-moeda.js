//Manipulando datas no javascript c
//criando uma instancia de Date () parautilizar seus métodos 
const dataAtual=new Date()
console.log(typeof(dataAtual))

//pegar o dia atual 
const dia = dataAtual.getDate()
console.log(`Hoje é dia ${dia}`)
//pegar o mes atual 
const mes = dataAtual.getMonth()
console.log(`Estamos no mês  ${mes+1}`)
//pegar o ano atual 
const ano = dataAtual.getFullYear()
console.log(`Ano atual  ${ano}`)
//mostrando data completa 
console.log(`A data de hoje é ${dia}/${mes}/${ano}`)

//-----------------------------------------------------------------------------
//manipulando moedas no jacvascript 
let salario = 2500.30
console.log(salario)
console.log(salario.toFixed(2))
console.log(salario.toFixed(0))
console.log(salario.toFixed(2).replace('.',','))
console.log(salario.toLocaleString('pt-br',{style:'currency',currency:'BRL'}))
let dolar = salario * 0.20

console.log(dolar.toLocaleString('en-us',{style:'currency',currency:'USD'}))
let euro = salario * 0.18

console.log(euro.toLocaleString('pt-br',{style:'currency',currency:'EUR'}))

//-----------------------------------------------------------------------------------
//Formatando Strings
const nome = "Wenderson Marques"
console.log(nome.toUpperCase())
console.log(nome.toLowerCase())
console.log(nome.length)

//Podemos usar length tbm para arrays
const lista = ['maça','banana','pera']
console.log(lista.length)