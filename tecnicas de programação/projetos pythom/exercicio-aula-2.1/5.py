s=float(input("Digite o salario do funcionario : \nR$"))
op = input("Digite a categoria do funcionario \n A , B ou C\n")
match op : 
    case "A"|"a":
        acresc= s+(s*0.10)
    case "B"|"b":
        acresc= s+(s*0.15)
    case "C"|"c":
        acresc= s+(s*0.25)
    
print(f"O salario atual do funcionario é R${s} , porém acrescentado de acordo com a categoria resulta em R${acresc}")
