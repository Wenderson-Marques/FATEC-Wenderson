import os 
os.system('cls')
nome=input("Digite o nome do aluno:\n")
nota1=float(input("Digite a primeira nota :\n"))
nota2=float(input("Digite a segunda nota :\n "))

media = (nota1+nota2)/2

if media > 6:
    print(f"O aluno {nome} , está aprovado,média ={media:.2f}")
elif media >=2 and media < 6:
    print(f"O aluno {nome},está de exame , media = {media:.2f}")
else:
    print(f"O aluno {nome}, está reprovado , média ={media:.2f}")