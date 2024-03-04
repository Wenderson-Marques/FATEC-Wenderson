import os 
os.system('cls')
num1=int(input("Digite um numero:\n"))
num2=int(input("Digite um segundo número:\n"))
num3=int(input("Digite um terceiro numero:\n"))

if num1>num2 and num1>num3:
    print(f"{num1} é o maior numero")
elif num2>num1 and num2>num3:
    print(f"{num2} é o maior numero")
elif num3>num1 and num3>num2:
    print(f"{num3} é o maior numero")
if num1==num2:
    print(f"{num1} e {num2} são iguais") 
if num2==num3:
    print(f"{num2} e {num3} são iguais")  
if num1==num3:
    print(f"{num1} e {num3} são iguais") 