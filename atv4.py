
print("===== APROVADOS =====")

with open("aprovados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")
      
        aluno = dados[0]
        media = dados[1]
        situacao = dados[2]

        print(f"Aluno: {aluno} | Média: {media} | Situação: {situacao}")

print("\n===== REPROVADOS =====")

with open("reprovados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")

        aluno = dados[0]
        media = dados[1]
        situacao = dados[2]

        print(f"Aluno: {aluno} | Média: {media} | Situação: {situacao}")
