import os 
os.system("cls")
n=int(input("Digite um valor para lhe mostrar a tabuada : \n"))
i=-1
while (i<10):
    i+=1
    print(f"{n} x {i} = {n*i}")