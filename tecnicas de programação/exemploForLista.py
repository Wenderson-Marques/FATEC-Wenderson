import os 
os.system("cls")
frutas = ["abacate","laranja","maça","pera"]
for lista in frutas :
    print(lista)

#buscar  o nome da fruta
busca =input("Digite o nome da fruta:\n")
for i in frutas :
    if i == busca :
        print(i)
        break
    else:
        print(f"{busca} , está fruta não foi encontrada")