from cadastrar_aluno import cadastrar_aluno
from listar_aluno import listar_aluno
from notas import cadastrar_notas

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - cadastrar notas")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_aluno()

    elif opcao == "3":
        cadastrar_notas()

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")


    print("\nDeseja voltar?")
    print("1 - Sim")
    print("2 - Não")

    opcao = input("Escolha: ").strip()

    if opcao == "":
        print("Campo vazio.")
        continue

    if not opcao.isdigit():
        print("Digite apenas números.")
        continue

    if opcao == "1":
        
        continue

    elif opcao == "2":
        
        break 

    else:
        print("Escolha apenas 1 ou 2.")


