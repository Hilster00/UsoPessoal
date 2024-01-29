def ordenar_nomes_no_mesmo_arquivo(arquivo,separador=","):
    with open(arquivo, 'r+') as file:
        # Lê os nomes do arquivo e os divide pela vírgula
        nomes = file.read().split(separador)

        # Remove espaços em branco ao redor de cada nome
        nomes = [nome.strip() for nome in nomes]

        # Ordena os nomes em ordem alfabética
        nomes_ordenados = sorted(nomes)

        # Move para o início do arquivo
        file.seek(0)

        # Limpa o conteúdo do arquivo
        file.truncate()

        # Escreve os nomes ordenados de volta no arquivo
        file.write(','.join(nomes_ordenados))

# Substitua 'nome_arquivo.txt' pelo nome do seu arquivo
ordenar_nomes_no_mesmo_arquivo('nome_arquivo.txt')
