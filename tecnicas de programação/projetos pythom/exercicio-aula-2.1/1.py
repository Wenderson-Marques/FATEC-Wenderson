import os 
os.system("cls")
letra = input("Digite uma letra\n")
match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print("É uma vogal!!!")
    case defaut:
        print("É uma consoante!!!")
    