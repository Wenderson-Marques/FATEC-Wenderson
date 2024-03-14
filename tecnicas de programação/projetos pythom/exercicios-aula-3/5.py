# Função para verificar se a resposta é válida
def resposta_valida(resposta):
    return resposta.lower() in ['a', 'b', 'c', 'd']

# Questões e respostas
questoes = [
    "1. Qual é a capital do Brasil?\n\
    a) Rio de Janeiro\n\
    b) São Paulo\n\
    c) Brasília\n\
    d) Belo Horizonte\n",

    "2. Qual é o maior animal terrestre?\n\
    a) Elefante Africano\n\
    b) Girafa\n\
    c) Tubarão Branco\n\
    d) Baleia Azul\n",

    "3. Qual é a capital da França?\n\
    a) Londres\n\
    b) Berlim\n\
    c) Paris\n\
    d) Roma\n",

    "4. Quem escreveu 'Dom Quixote'?\n\
    a) William Shakespeare\n\
    b) Miguel de Cervantes\n\
    c) Dante Alighieri\n\
    d) Johann Wolfgang von Goethe\n"
]

# Respostas corretas
respostas_corretas = ['c', 'd', 'c', 'b']

# Inicializar contador de pontuação
pontuacao = 0

# Loop para perguntar as questões até que todas sejam respondidas corretamente
i = 0
while i < len(questoes):
    print(questoes[i])
    resposta = input("Escolha a opção correta (a, b, c ou d): ")
    if resposta_valida(resposta):
        if resposta.lower() == respostas_corretas[i]:
            print("Resposta correta!\n")
            pontuacao += 1
            i += 1
        else:
            print("Resposta incorreta. Tente novamente.\n")
    else:
        print("Por favor, insira uma resposta válida.\n")

# Exibir pontuação final
print(f"Sua pontuação final é: {pontuacao}/{len(questoes)}")
