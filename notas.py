notas = []

def cadastrar_notas():
    while True:
        print("\nMatérias:")
        print("1 - Desenvolvimento de Sistemas")
        print("2 - Banco de Dados")
        print("3 - Requisitos")

        materia = input("Escolha a matéria: ").strip()

        if materia == "1":
            materia = "Desenvolvimento de Sistemas"
            break
        elif materia == "2":
            materia = "Banco de Dados"
            break
        elif materia == "3":
            materia = "Requisitos"
            break
        else:
            print("Matéria inválida.")

    while True:
        nota1 = input("Digite a nota 1: ").strip()

        try:
            nota1 = float(nota1)

            if 0 <= nota1 <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite apenas números.")

    while True:
        nota2 = input("Digite a nota 2: ").strip()

        try:
            nota2 = float(nota2)

            if 0 <= nota2 <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite apenas números.")

    notas.append({
        "materia": materia,
        "nota1": nota1,
        "nota2": nota2
    })

    print("\nNota cadastrada com sucesso!")
