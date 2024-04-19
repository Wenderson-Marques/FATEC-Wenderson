
pontos= 0
respostas = 0

while respostas < 4:
    resposta = input(f"Digite a resposta {respostas + 1} para a questão: ")

    
    if respostas == 0 and resposta == 'a':
        pontos += 1
    elif respostas == 1 and resposta == 'c':
        pontos += 1
    elif respostas == 2 and resposta == 'd':
        pontos += 1

   
    respostas += 1

print(f"A pontuação total é: {pontos}")
