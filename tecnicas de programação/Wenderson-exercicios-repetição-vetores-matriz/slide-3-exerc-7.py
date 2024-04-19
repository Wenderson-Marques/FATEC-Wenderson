preco_por_pao = 0.54

t_precos = []

for num_paes in range(2, 51, 2):
    preco_total = num_paes * preco_por_pao
    t_precos.append((num_paes, preco_total))

print("Tabela de Preços da Panificadora \"Pão de Ontem\":")
print("Quantidade de Pães | Preço Total")
print("-------------------|-------------")
for item in t_precos:
    print(f"{item[0]:<19} | R$ {item[1]:.2f}")
