import mongoose from "mongoose"
import pedido from "../models/Pedido.js"

const Pedido = mongoose.model("Pedido", pedido)

class PedidoService {
    // Método para SELECIONAR TODOS os pedidos no banco
    SelectAll() {
        const pedidos = Pedido.find()
        return pedidos
    }
    // ROTA PARA OBTENÇÃO DO ÚLTIMO NÚMERO DE PEDIDO
   selectLast() {
        try {
            // Encontra o último pedido  ordenado por data de criação decrescente
            const ultimoPedido =  Pedido.findOne({}, {}, { sort: { 'created_at': -1 } });
    
            if (ultimoPedido) {
                // Se encontrou o último pedido, imprime o número do pedido
                return("Último número de pedido:", ultimoPedido.numero);
            } else {
                console.log("Nenhum pedido encontrado.");
            }
        } catch (error) {
            console.error("Erro ao obter o último pedido:", error);
        }
    }
    
    // Método para CADASTRAR um pedido
    Create(numero,valor) {
        const novoPedido = new Pedido({
            numero : numero,
            valor : valor
        })
        novoPedido.save()
    }

    // Método para EXCLUIR um pedido
    Delete(id) {
        Pedido.findByIdAndDelete(id).then(() => {
            console.log(`Pedido com a id: ${id} foi deletado com sucesso.`)
        }).catch(err => {
            console.log(err)
        })
    }

    // Método para SELECIONAR um pedido ÚNICO
    SelectOne(id){
        const pedido = pedido.findOne({_id : id})
        return pedido
    }

    // Método para ALTERAR um pedido
    Update(id, numero, valor) {
        Pedido.findByIdAndUpdate(id, {
            numero : numero,
            valor : valor,
           
        }).then(() => {
            console.log(`Dados do pedido com id: ${id} alterados com sucesso!`)
        }).catch(err => {
            console.log(err)
        })
    }
}

// router.get("/pedidos", function(req, res) {
//     Pedido.findOne({}, {}, { sort: { 'created_at' : -1 } }, function(err, pedido) {
//         if (err) {
//             console.log(err);
//             res.status(500).send("Erro ao obter o último pedido.");
//         } else {
//             if (pedido) {
//                 res.json({ ultimoNumero: pedido.numero });
//             } else {
//                 res.json({ ultimoNumero: 0 }); 
//             }
//         }
//     });
// });

export default new PedidoService()