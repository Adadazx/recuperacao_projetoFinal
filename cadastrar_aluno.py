def cadastrar_aluno(dados):
    while True:
        nome = input("nome do aluno: ").strip().lower()
        sobrenome = input("sobrenome: ").strip().lower()

        if nome == "" or sobrenome == "":
            print("campo vazio")
            continue

        if not nome.isalpha() or not sobrenome.isalpha():
            print("nome inválido")
            continue

        break

    while True:
        idade = input("idade: ").strip()

        if idade == "":
            print("campo vazio")
            continue

        if not idade.isdigit():
            print("digite apenas números")
            continue

        break

    while True:
        turma = input("turma: ")

        if turma in ["1","2","3","4","5","6","7","8","9"]:
            break
        else:
            print("turma inválida")

    dados["alunos"].append({
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "turma": turma
    })

    print("Aluno cadastrado!")