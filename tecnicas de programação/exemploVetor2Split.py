# Exemplo vetor sem definição de tamanho usando função Split (só números ou só letras)

import os
os.system('cls')

entrada_dados = input("Digite os elementos do vetor separados por espaço: ") 
vetor = [int(x) for x in entrada_dados.split()] 

print(vetor)