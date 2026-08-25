import csv
import json

# 1. Carrega os dados do arquivo JSON
with open('alunos.json', 'r', encoding='utf-8') as json_file:
    lista_alunos = json.load(json_file)

# 2. Abre (ou cria) o arquivo CSV para escrita
with open('alunos.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    # ADICIONADO 'RestMatr' NA LISTA DE COLUNAS:
    colunas = ['nome', 'idade', 'cep', 'RestMatr', 'email']

    writer = csv.DictWriter(csv_file, fieldnames=colunas, delimiter=';')

    # Escreve o cabeçalho
    writer.writeheader()

    # Escreve as linhas (agora aceita 'telefone' sem erros)
    writer.writerows(lista_alunos)

print('Conversão realizada com sucesso!')