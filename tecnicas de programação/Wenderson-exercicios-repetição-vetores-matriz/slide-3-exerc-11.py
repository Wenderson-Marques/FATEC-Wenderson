nomes = ["Wenderson", "Eder", "Luiz", "fernanda", "alice", "joão"]

while True:
    escolha = input("Digite 1 para buscar  ou 0 para sair: ")
    
    if escolha == '0':
        print("Saindo...")
        break
    elif escolha == '1':
        nome_busca = input("Digite um nome: ")
        encontrado = False
        
        for nome in nomes:
            if nome == nome_busca:
                print(f"Nome encontrado: {nome}")
                encontrado = True
                break
        
        if not encontrado:
            print("Nome não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")
