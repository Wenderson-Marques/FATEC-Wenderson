import os 
os.system('cls')
print("Programa Empréstimo")
print("Responda \n1-Sim\n0-Não\n")
negativado=int(input("possui nome negativado?\n"))
if negativado == 1 : 
    print("Você não pode realizar empréstimo\n")
else:
    carteiraassinada=int(input("Possui carteira assinada?\n"))
    if carteiraassinada==0:
        print("Você não pode realizar empréstimo\n")
    else:
        casaPropria=int(input("Possui casa própria?\n"))
        if casaPropria==0:
            print("Você não pode realizar empréstimo\n")
        else:
            print("Você pode realizar o empréstimo\n")