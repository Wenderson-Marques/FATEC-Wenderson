import os 
os.system('cls')
alt1=float(input("Digite a altura da pessoa 1\n"))
alt2=float(input("Digite a altura da pessoa 2\n"))
alt3=float(input("Digite a altura da pessoa 3\n"))

if alt1<alt2 and alt2<alt3:
    print(f"\n\n{alt3}\n{alt2}\n{alt1}")

elif alt2<alt1 and alt1<alt3:
    print(f"\n\n{alt3}\n{alt1}\n{alt2}")

elif alt3<alt1 and alt1<alt2:
    print(f"\n\n{alt2}\n{alt1}\n{alt3}")

elif alt1<alt3 and alt3<alt2:
    print(f"\n\n{alt2}\n{alt3}\n{alt1}")

elif alt2<alt3 and alt3<alt1:
    print(f"\n\n\n{alt1}\n{alt3}\n{alt2}")

elif alt3<alt2 and alt2<alt1:
    print(f"\n\n\n{alt1}\n{alt2}\n{alt3}")
if alt1==alt2 or alt2==alt3 or alt1==alt3:
    print("Alguns dos  valores são iguais, por favor seja mais especifico")








