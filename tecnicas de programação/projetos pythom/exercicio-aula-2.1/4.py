ptotal=float(input("Digite o valor total a compra:\nR$"))
op= int(input("Digite:\n1-À vísta(em espécie)\n2-Cartão de débito\n3-cartão de crédito\n"))
match op :
    case 1: 
        d = ptotal+(ptotal*0.15)
    case 2:
        d = ptotal+(ptotal*0.10)
    case 3:
        d = ptotal+(ptotal*0.5)
    case default:
        print("Opção inexistente")
print(f"O valor total da compra juntamente\ncom o desconto pela forma de pagamento é R${d} ")