/*comentário no java script
*/
//variáveis no javascript
//const x var x let
//const nome = "Wenderson"
//const idade 
//let nome ="Wenderson"
//nome="Nego"
//console.log(nome)
//var nome ="Wenderson"
//nome="Nego"
//console.log(nome)
// let idade = 18 
// let cidade="PariqueraAçu"
// console.log(typeof(idade))
// console.log(typeof(cidade))
// function minhaFuncao(){

// }
// //função simples 
// function simples(){
//     console.log("Olá , bem vindo ")
// }
// simples()

// //função com parâmetro / argumento
// function saudacao(nome){
//     console.log(`Olá bem-vindo, ${nome}!` )
//     console.log("olá , bem-vindo "+nome)
// }
// nome="Wenderson"
// saudacao(nome)

// //FUNÇÃO COM  MAIS DE UM PARÂMETRO 
// function soma (num1,num2)
// {
//     let res= num1+num2
//     console.log(`A soma dos dois numeros foi ${res}`)
// }
// soma(5,7)

// //FUNÇÃO COM RETORNO 
// function Soma(n1,n2)
// {
//     return n1+n2
// }
// console.log(`A soma dos dois numeros foi ${Soma(2,6)}.`)

// //FUNÇÃO COM MAIS DE UM RETORNO 
// function parImpar(n){
//     if (n%2==0){
//         return 'Par'
//     }
//     else{
//         return 'Ímpar'
//     }
// }

// let num = 4
// console.log(parImpar(num))
// console.log(`O número ${num} é ${parImpar(num)}.`)

// //FUNÇÃO ANÔNIMA
// let dobro = function(x)
// {
//     return x*2
// }
// console.log(dobro(15))

// //ARROW FUNCTION( COM UM UNICO PARÂMETRO)
// const Dobro=x=>{
//     return x*2
// }
// console.log(`O dobro do numero é ${Dobro(20)}.`)
// //ARROW FUNCTION (COM MAIS DE UM PARÂMETRO)
// const Calc = (num1,operador,num2)=>
// {
//     return eval(`${num1}${operador}${num2}`)//função eval lê string e interpreta para fazer calculos 
// }
// console.log(`O resultado da operação é ${Calc(8,"/",2)}`)

//FUNÇÃO IMEDIATA - IIFE(imediately invoked function expression)
const iife = (function()
{
    console.log("Executando automaticamente!!")
})()
const start = (function(app)
{
    console.log(`Executando imediatamente ${app}.`)
})("Whatsapp")