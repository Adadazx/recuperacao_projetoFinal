def listar_aluno(dados):

    if len(dados["alunos"]) == 0:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n=== LISTA DE ALUNOS ===")

    for aluno in dados["alunos"]:

        print("\nNome:", aluno["nome"])
        print("Sobrenome:", aluno["sobrenome"])
        print("Idade:", aluno["idade"])
        print("Turma:", aluno["turma"])

        encontrou_nota = False

        for nota in dados["notas"]:

            if nota["nome"] == aluno["nome"]:

                media = (nota["nota1"] + nota["nota2"]) / 2

                if media >= 7:
                    situacao = "Aprovado"

                elif media >= 5:
                    situacao = "Recuperação"

                else:
                    situacao = "Reprovado"

                print("\nMatéria:", nota["materia"])
                print(f"Média: {media:.1f}")
                print("Situação:", situacao)

                encontrou_nota = True

        if not encontrou_nota:
            print("\nNenhuma nota cadastrada.")