matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz 4x4:")
for linha in matriz:
    print(linha)

contagem = 0

for linha in matriz:
    for valor in linha:
        if valor > 10:
            contagem += 1

print(f"\nA matriz possui {contagem} valores maiores que 10.")
