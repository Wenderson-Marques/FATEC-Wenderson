# Exemplo vetor com definição de tamanho

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(0,5):
    elemento = int(input(f"Digite o {i + 1}º valor do vetor: "))
    vetor.append(elemento)

print(vetor)