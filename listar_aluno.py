from cadastrar_aluno import alunos

def listar_aluno():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("\nnome:", aluno["nome"])
            print("sobrenome:", aluno["sobrenome"])
            print("turma:", aluno["turma"])
            print("idade:", aluno["idade"])