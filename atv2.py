with open("notas.txt", "r", encoding="utf-8") as arquivo:
    with open("aprovados.txt", "w", encoding="utf-8") as aprovados:
        with open("exame.txt", "w", encoding="utf-8") as exame:
            with open("reprovados.txt", "w", encoding="utf-8") as reprovados:

                for linha in arquivo:
                    dados = linha.strip().split(";")

                    aluno = dados[0]
                    nota1 = float(dados[1])
                    nota2 = float(dados[2])
                    nota3 = float(dados[3])

                    media = (nota1 + nota2 + nota3) / 3

                    if media >= 7:
                        aprovados.write(f"{aluno};{media:.2f};Aprovado\n")
                    elif media >= 5:
                        exame.write(f"{aluno};{media:.2f}\n")
                    else:
                        reprovados.write( f"{aluno};{media:.2f};Reprovado\n")

print("Alunos separados com sucesso!")
