def listar_notas(dados):

    if len(dados["notas"]) == 0:
        print("\nNenhuma nota cadastrada.")
    else:
        print("\n=== LISTA DE NOTAS ===")

        for nota in dados["notas"]:
            print("\nAluno:", nota["nome"])
            print("Matéria:", nota["materia"])
            print("Nota 1:", nota["nota1"])
            print("Nota 2:", nota["nota2"])