vb=int(input("Digite a quantidade de votos brancos :\n"))
vn=int(input("Digite a quantidade de votos nulos :\n"))
vv=int(input("Digite a quantidade de votos validos :\n"))
total=vb+vn+vv
percb=(vb*100)/total
percn=(vn*100)/total
percv=(vv*100)/total

print(f"percentual de votos brancos:{percb}%\npercentual de votos nulos :{percn}%\npercentual de votos validos : {percv}%\ntotal de votos  : {total} ")