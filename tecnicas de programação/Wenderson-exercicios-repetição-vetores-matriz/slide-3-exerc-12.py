nomes = []

for i in range(7):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)

print("Nomes armazenados e suas posições na lista:")
for i, nome in enumerate(nomes):
    print(f"Posição {i+1}: {nome}")
