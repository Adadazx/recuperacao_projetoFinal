from dados import carregar, salvar
from cadastrar_aluno import cadastrar_aluno
from listar_aluno import listar_aluno
from editar_aluno import editar_aluno
from remover_aluno import remover_aluno
from notas import cadastrar_notas
from listar_notas import listar_notas
from situacao_aluno import calcular_situacao

dados = carregar()

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Cadastrar notas")
    print("4 - listar notas")
    print("5 - editar aluno")
    print("6 - remover aluno")
    print("7 - média e situação")
    print("8 - apagar todos os dados")
    print("9 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno(dados)
        salvar(dados)

    elif opcao == "2":
        listar_aluno(dados)
        salvar(dados)

    elif opcao == "3":
        cadastrar_notas(dados)
        salvar(dados)

    elif opcao == "4":
        listar_notas(dados)
        salvar(dados)

    elif opcao =="5":
        editar_aluno(dados)
        salvar(dados)

    elif opcao == "6":
        remover_aluno(dados)
        salvar(dados)


    elif opcao == "7":
        calcular_situacao(dados)
        salvar(dados)

    elif opcao == "8":
        dados["alunos"] = []
        dados["notas"] = []
        dados["medias"] = []
        dados["situacoes"] = []
        salvar(dados)

        print("Todos os dados foram apagados!")

    elif opcao == "9":
        salvar(dados)
        print("Dados salvos!")
        break


    else:
        print("Opção inválida.")
        continue

    while True:
        print("\nDeseja voltar?")
        print("1 - Sim")
        print("2 - Não")

        voltar = input("Escolha: ").strip()

        if voltar == "":
            print("Campo vazio.")
            continue

        if not voltar.isdigit():
            print("Digite apenas números.")
            continue

        if voltar == "1":
            break  

        elif voltar == "2":
            salvar(dados)
            print("dados salvos")
            exit()  

        else:
            print("Escolha apenas 1 ou 2.")

