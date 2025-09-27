import json

alunos = [
    {"nome": "João", "idade": 20},
    {"nome": "Maria", "idade": 22},
]

# Salvar no arquivo
with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump(alunos, f, indent=4, ensure_ascii=False)

# Ler do arquivo
with open("alunos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print("Alunos cadastrados:", dados)