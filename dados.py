import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "ativo": True,
    "habilidades": ["python", "java"]
}

with open ('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados,arquivo, ensure_ascii=False, indent=4)

def ler_dados():
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)

    print(dados_lidos["idade"])


ler_dados()