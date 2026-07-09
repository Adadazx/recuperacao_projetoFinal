def calcular_situacao(dados):

    if len(dados["notas"]) == 0:
        print("Nenhuma nota cadastrada.")
        return

    dados["medias"] = []
    dados["situacoes"] = []

    print("\n=== MÉDIA E SITUAÇÃO ===")

    for nota in dados["notas"]:

        media = (nota["nota1"] + nota["nota2"]) / 2

        if media >= 7.0:
            situacao = "Aprovado"

        elif media >= 5.0:
            situacao = "Recuperação"

        else:
            situacao = "Reprovado"

        dados["medias"].append({
            "nome": nota["nome"],
            "materia": nota["materia"],
            "media": media
        })

        dados["situacoes"].append({
            "nome": nota["nome"],
            "materia": nota["materia"],
            "situacao": situacao
        })

        print(f"\nAluno: {nota['nome']}")
        print(f"Matéria: {nota['materia']}")
        print(f"Média: {media:.1f}")
        print(f"Situação: {situacao}")