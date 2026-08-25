import json

# Lendo o arquivo de texto
with open("dados.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()

lista_alunos = []

for linha in linhas:
    # Remove quebras de linha e trata separadores (; ou ,)
    linha_limpa = linha.strip().replace(",", ";")
    partes = [p.strip() for p in linha_limpa.split(";") if p.strip()]

    if partes:
        # Monta o dicionário dinamicamente
        aluno = {
            "nome": partes[0] if len(partes) > 0 else None,
            "idade": partes[1] if len(partes) > 1 else None,
            "cep": partes[2] if len(partes) > 2 else None,
            "RestMatr": partes[3] if len(partes) == 5 else None,
            "email": partes[-1] if len(partes) > 3 else None,
        }
        lista_alunos.append(aluno)

# Salvando no arquivo JSON
with open("alunos.json", "w", encoding="utf-8") as json_file:
    json.dump(lista_alunos, json_file, ensure_ascii=False, indent=2)

print("Conversão concluída com sucesso!")
