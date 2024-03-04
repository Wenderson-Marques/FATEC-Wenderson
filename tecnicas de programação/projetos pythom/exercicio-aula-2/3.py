import os 
os.system('cls')
altura=float(input("Digite sua altura :\n"))
sexo=int(input("Digite\n1-para masculino\n2-para feminino\n"))
imch=(72.7*altura)-58
imcm=(62.1*altura)-44.7
if sexo==1:
    print(f"Seu peso ideal seria {imch:.2f}\n\n")
else:
    print(f"Seu peso ideal seria {imcm:.2f}\n\n")
