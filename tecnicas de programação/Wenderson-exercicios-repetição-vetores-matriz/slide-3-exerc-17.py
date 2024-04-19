linguagens = ["python", "SQL", "c", "c++", "js", "cobol"]

total_caracteres = 0

print("Linguagens com mais de 3 caracteres:")
for linguagem in linguagens:
    if len(linguagem) > 3:
        print(linguagem)
        total_caracteres += len(linguagem)

print(f"\nQuantidade total de caracteres: {total_caracteres}")
