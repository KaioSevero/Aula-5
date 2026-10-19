with open("exame.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:
        dados = linha.strip().split(";")

        aluno = dados[0]
        media_anterior = float(dados[1])

        nota_exame = float(input(f"Digite a nota do exame de {aluno}: "))

        media_final = (media_anterior + nota_exame) / 2

        if media_final >= 5:
            with open("aprovados.txt", "a", encoding="utf-8") as aprovados:
                aprovados.write(f"{aluno};{media_final:.2f};Aprovado após exame\n")

            print(f"{aluno}: Aprovado após exame")

        else:
            with open("reprovados.txt", "a", encoding="utf-8") as reprovados:
                reprovados.write(f"{aluno};{media_final:.2f};Reprovado após exame\n")
       
            print(f"{aluno}: Reprovado após exame")

print("Resultados dos exames registrados!")
