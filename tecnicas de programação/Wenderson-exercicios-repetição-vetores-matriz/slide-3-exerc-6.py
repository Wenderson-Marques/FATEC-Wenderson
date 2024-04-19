t_precos = []

for num_produtos in range(1, 51):
    preco = num_produtos * 1.99
    
    t_precos.append((num_produtos, preco))

print("Tabela de Preços da Loja \"Quase Dois\":")
print("Número de Produtos | Preço\n")

for item in t_precos:
    print(f"{item[0]:<18} | R$ {item[1]:.2f}")
