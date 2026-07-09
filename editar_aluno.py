def editar_aluno(dados):
    while True:
        if len(dados["alunos"]) == 0:
            print("Nenhum aluno cadastrado.")
            continue

        nome = input("Digite o nome do aluno que deseja editar: ").lower()

        for aluno in dados["alunos"]:
            if aluno["nome"] == nome:

                aluno["sobrenome"] = input("Novo sobrenome: ").lower()
                aluno["idade"] = input("Nova idade: ")
                aluno["turma"] = input("Nova turma: ")

                print("Aluno editado com sucesso!")
                return

        print("Aluno não encontrado.")