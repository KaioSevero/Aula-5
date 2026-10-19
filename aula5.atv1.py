with open("notas.txt", "w", encoding="utf-8") as pontuacao:

    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        aluno = input("Digite o nome do aluno: ")

        notas = []

        for j in range(1, 4):
            nota = float(input(f"Digite a nota {j}: "))
            notas.append(nota)

        pontuacao.write(f"{aluno};{notas[0]};{notas[1]};{notas[2]}\n")

print("Notas salvas com sucesso!")
