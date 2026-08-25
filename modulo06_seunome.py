'''
Arquivos do tipo
txt -> arquivo em bloco de notas, texto simples;
csv -> arquivo em excel e google planilhas, texto simples, separado por vírgula;
json -> arquivo em formato de dicionário, texto simples, separado por vírgula;

# 1. Abre o arquivo para leitura ('r')
arquivo_read = open('arquivo_leitura.txt', 'r', encoding='utf-8')

# 2. Lê todo o conteúdo do arquivo
conteudo_arquivo = arquivo_read.read()

# 3. Exibe o conteúdo na tela
print(conteudo_arquivo)

# 4. Fecha o arquivo
arquivo_read.close()

'''



# 1. Abre o arquivo para leitura ('r')
arquivo_read = open('arquivo_leitura.txt', 'r', encoding='utf-8')

# 2. Lê todo o conteúdo do arquivo
conteudo_arquivo = arquivo_read.readlines()

# 3. Exibe o conteúdo na tela
# print(conteudo_arquivo)
print(conteudo_arquivo[4].strip())

# 4. Fecha o arquivo
arquivo_read.close()
