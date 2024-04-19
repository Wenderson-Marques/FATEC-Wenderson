valores = []

for i in range(5):
    valor = int(input(f"Digite o valor {i + 1}: "))
    valores.append(valor)

print("Valores digitados:")
for valor in valores:
    print(valor)

print("\nValores pares:")
for valor in valores:
    if valor % 2 == 0:
        print(valor)
