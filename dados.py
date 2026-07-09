import json

arquivo = "dados.json"


def salvar(dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar():
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return {
            "alunos": [],
            "notas": [],
            "medias": [],
            "situacoes": []
        }
    