u=float(input("Digite o valor da tensão:\n"))
r=float(input("Digite o valor da Resistência:\n"))
i=float(input("Digite o valor da Corrente:\n"))
op= int(input("Digite ...\n1-Tensão(em Volt)\n2-Resistência(em Ohm)\n3-Corrente(em Ampére)"))
match op:
        case 1:
            u=r*i
            print(f"Tensão = {u}")
        case 2:
            r=u/i
            print(f"Resistência= {r}")
        case 3:
            i=u/r
            print(f"Corrente= {i}")
    