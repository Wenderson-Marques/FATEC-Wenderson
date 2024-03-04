import os
os.system('cls')
rg=input("Digite o rg do empregado \n")
dtnasc=int(input("Digite o ano  de nascimento :\n"))
anoDeIngresso=int(input("Digite o ano de ingresso na impresa :\n" ))
anoAtual=int(input("Digite o ano atual\n"))

idade = anoAtual-dtnasc
tempoTrabalho=anoAtual-anoDeIngresso
print(f"Idade : {idade}" )
print(f"Tempo de trabalho : {tempoTrabalho}")
if idade>=65 or tempoTrabalho>=30 :
    print("Requer aposentadoria")
elif idade>=60 and tempoTrabalho>=25:
    print("Requerer aposentadoria")
else :
    print("Não requerer aposentadoria")
    
