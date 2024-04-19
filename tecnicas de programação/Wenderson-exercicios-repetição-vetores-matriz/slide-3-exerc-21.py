num_funcionarios_masculinos = 0

contador = 0

while contador < 15:
    nome = input("Digite o nome do funcionário: ")
    sexo = input("Digite o sexo do funcionário (M/F): ")

    if sexo.upper() == 'M':
        num_funcionarios_masculinos += 1
        print(f"{nome} precisa fazer o exame.")
    
    elif sexo.upper() == 'F':
        print(f"{nome} não precisa fazer o exame.")
    else:
        print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
    
    contador += 1
print(f"\nNúmero total de funcionários do sexo masculino: {num_funcionarios_masculinos}")
