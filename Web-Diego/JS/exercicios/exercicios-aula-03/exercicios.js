const dataAtual=new Date()
console.log(typeof(dataAtual))
dia = dataAtual.getDate()
mes = dataAtual.getMonth()
ano = dataAtual.getFullYear()
console.log(`${dia+7}/${mes}/${ano}`)
console.log(`${dia}/${mes+5}/${ano}`)
console.log(`${dia}/${mes}/${ano+2}`)

nome='Wenderson Marques'
function Name(nome)
{
    console.log(`nome com letas maiúsculas: ${nome.toUpperCase()}`)
    console.log(`Nome com letras minuculas: ${nome.toLowerCase()}`)
    console.log(`Quantidade de letras :${nome.length-1}`)
}
Name(nome)
