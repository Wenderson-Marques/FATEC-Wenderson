tab=int(input("Digite qual tabuada irá querer ver : \n"))
start=int(input("Digite o valor inicial:\n"))
end=int(input("Digite o valor final:\n"))
i=start-1
if (start<end):
    while (i<end):
        i+=1
        print(f"{tab} x {i} = {tab*i}")
else:
     i=start
     while (i>=end):
        print(f"{tab} x {i} = {tab*i}")
        i-=1