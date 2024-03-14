//arrays (vetor ou lista )
let produto = []
console.log(typeof(produto))
let produtos=['computador','notebook','celular','tablet']
console.log(produtos)
console.log(produtos[0])
console.log(produtos[2])
console.log()
//exibindo o array com for (com o s indices)
for (let c in produtos )
{
    console.log(`${Number(c)+1} - ${produtos[c]}`)
}
console.log()
//exibindo o array com forEach
produtos.forEach((produto,i)=>
{
    console.log(produto)
})
console.log()
//////////////////////////////////////////////////////////////////////
// OBJETOS LITERAIS
const porduct = {}
console.log(typeof(porduct))

const Product = 
{
    nome: 'computador',
    MARCA : 'Positivo',
    preco: 3000,
    descricao : 'PC moderno com bom desempenho'
}
console.log(Product)
console.log()
console.log(`O ${Product.nome},da marca ${Product.MARCA},custa R$${Product.preco},${Product.descricao}`)