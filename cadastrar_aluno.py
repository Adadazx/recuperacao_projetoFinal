alunos = []

def cadastrar_aluno():
    while True:
        nome = input("Nome do aluno: ").strip().lower()
        sobrenome = input("Sobrenome: ").strip().lower()

        if nome == "" or sobrenome == "":
            print("Campo vazio.")
            continue

        if not nome.isalpha() or not sobrenome.isalpha():
            print("Nome inválido.")
            continue

        break

    while True:
        idade = input("Idade: ").strip()

        if idade == "":
            print("Campo vazio.")
            continue

        if not idade.isdigit():
            print("Digite apenas números.")
            continue

        idade = int(idade)

        if idade <= 0:
            print("Idade inválida.")
            continue

        break

    while True:
        print("Opções de turma:")
        print("1 a 9")

        turma = input("Turma: ").strip()

        if turma in ["1","2","3","4","5","6","7","8","9"]:
            print("Turma cadastrada!")
            break
        else:
            print("Turma inválida.")

    alunos.append({
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "turma": turma
    })