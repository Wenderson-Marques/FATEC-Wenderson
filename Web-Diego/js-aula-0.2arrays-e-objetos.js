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
    console.log(`${c} - ${produtos[c]}`)
}