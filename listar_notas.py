from notas import notas

def listar_notas():
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.")
    else:
        print("\n=== LISTA DE NOTAS ===")

        for nota in notas:
            print("Matéria:", nota["materia"])
            print("Nota 1:", nota["nota1"])
            print("Nota 2:", nota["nota2"])
            print()

    