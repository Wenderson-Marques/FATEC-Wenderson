import os 
os.system('cls')
nome1=input("Digite um nome:\n")
peso1=float(input("Digite seu peso :"))
nome2=input("Digite um outro nome:\n")
peso2=float(input("Digite seu peso :"))

if peso1>peso2:
    print(f"{nome1} é o/a mais pesado/a")
elif peso2>peso1 :
    print(f"{nome2} é o/a mais pesado/a")
if peso1==peso2:
    print(f"{nome1} e {nome2} possuem o mesmo peso")