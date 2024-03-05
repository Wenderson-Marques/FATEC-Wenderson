nomes=["josé","maria julia","luiz","ana","Fernanda"]
for i in nomes :
    if len(i)!=3:
        continue
    print(f"ola {i}")
    if i == "luiz":
        break
