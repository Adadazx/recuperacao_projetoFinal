def remover_aluno(dados):

    if len(dados["alunos"]) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno que deseja remover: ").strip().lower()

    for aluno in dados["alunos"]:
        if aluno["nome"] == nome:
            dados["alunos"].remove(aluno)

            dados["notas"] = [
                nota for nota in dados["notas"]
                if nota["nome"] != nome
            ]

            print("Aluno removido com sucesso!")
            return

    print("Aluno não encontrado.")