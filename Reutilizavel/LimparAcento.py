from unidecode import unidecode

def remover_acentos(texto):
    return unidecode(texto)

# Exemplo de uso
entrada = "Olá, como está você hoje?"
saida = remover_acentos(entrada)
print(saida)
