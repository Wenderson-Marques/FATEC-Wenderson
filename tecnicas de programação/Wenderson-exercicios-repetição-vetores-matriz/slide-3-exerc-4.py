
numero = int(input("Digite um número para a tabuada: "))

inicio = int(input("Digite o inicio: "))
final = int(input("Digite o fim: "))


while inicio <= final:
    resultado = numero * inicio
    print(f"{numero} x {inicio} = {resultado}")
    inicio += 1
