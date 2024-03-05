peso = float(input("Digite o peso de uma pessoa :\n"))
op = int(input("Selecione o planeta no qual você deseja ver o peso dessa pessoa :\n1-Mercúrio\n2-Vênus\n3-Marte\n4-Júpiter\n5-Saturno\n"))
match op : 
    case 1 : 
        pesor= peso*0.37
        print(f"O Peso dessa pessoa em Mercúrio é : {pesor}")
    case 2 : 
        pesor= peso*0.88
        print(f"O Peso dessa pessoa em Vênus é : {pesor}")
    case 3 : 
        pesor= peso*0.38
        print(f"O Peso dessa pessoa em Marte é : {pesor}")
    case 4 : 
        pesor= peso*2.64
        print(f"O Peso dessa pessoa em Jupiter é : {pesor}")
    case 5 : 
        pesor= peso*1.15
        print(f"O Peso dessa pessoa em Saturno é : {pesor}")