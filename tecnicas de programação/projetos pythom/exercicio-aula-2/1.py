import os 
os.system('cls')
num1=int(input("Digite um numero :\n"))
num2=int(input("Digite um segundo numero:\n"))
if num1 ==num2:
    print("Os numeros não iguais .")
elif num1>num2:
    div=num1/num2
    print(f"o resultado da divisão é: {div}")
elif num2>num1:
    div=num2/num1
    print(f"o resultado da divisão é: {div}")
