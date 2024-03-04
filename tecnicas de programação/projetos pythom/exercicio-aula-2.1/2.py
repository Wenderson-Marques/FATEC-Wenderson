import os 
os.system("cls")
indicePolicao=int(input("Digite o indice de poluição do meio ambiente entre 1 a 10:\n"))
match indicePolicao:
    case 0|1|2:
        print("Aceitável!")
    case 3|4|5:
        print("Suspender Atividades Grupo 1 !!\n")
    case 6|7:
        print("Suspender Atividades dos Grupos 1 e 2 !!!\n")
    case 8|9|10:
        print("Suspender ativdades de todos os grupos !!!!!!!!!!\n")
    case default: 
        print("Digite um numero inteiro de 1  A 10 ")