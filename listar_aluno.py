def listar_aluno(dados):

    if len(dados["alunos"]) == 0:
        print("\nNenhum aluno cadastrado.")
    else:
        for aluno in dados["alunos"]:
            print("\nnome:", aluno["nome"])
            print("sobrenome:", aluno["sobrenome"])
            print("turma:", aluno["turma"])
            print("idade:", aluno["idade"])