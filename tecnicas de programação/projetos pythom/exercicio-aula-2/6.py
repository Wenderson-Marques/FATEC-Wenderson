import os 
os.system('cls')
num1=float(input("Digite um primeiro numero : \n"))
num2=float(input("Digite um segundo numero : \n"))

media=(num1*2+num2*3)/5
q=(num1+num2)**2
print(f"A média ponderada é = {media:.2f}")
print(f"O quadrado da soma dos dois numero é = {q}")

if num1<num2:
    cubo=num1**3
    print(f"O cubo do menor numero é ={cubo}")
else:
    cubo=num2**3
    print(f"O cubo do menor numero é = {cubo}")

