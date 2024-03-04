import os 
os.system('cls')
num1=int(input("Digite um numero inteiro positivo:\n"))
if num1%2==0:
    pot=num1**2
    print(f"O numero é par ,elevado ao quadrado  {pot}")
else:
    pot=num1**3
    print(f"O numero é ímpar ,elevado ao cubo = {pot}")

