from cadastrar_aluno import alunos

def remover_aluno():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno que deseja remover: ").lower()

    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return

    print("Aluno não encontrado.")