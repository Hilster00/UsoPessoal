def sao_anagramas(*palavras):
    if len(palavras)<2:
        return False
    quantidades=[{} for i in range(len(palavras))]
    lista_caracteres=set()
    # Contagem de caracteres em cada palavra
    for i,palavra in enumerate(palavras):
        for caractere in palavra:
            quantidades[i][caractere]=quantidades[i].get(caractere,0)+1
            lista_caracteres.add(caractere)

    # Contagem de caracteres em cada palavra       
    for caractere in lista_caracteres:

    
        q = quantidades[0].get(caractere, 0)  # Obtém a contagem do primeiro conjunto
        
        # Verifica se as contagens são iguais em todas as palavras
        if any(quantidade.get(caractere, 0) != q for quantidade in quantidades):
            return False
        
    return True
def sao_anagramas2(*palavras):
    if len(palavras)<2:
        return False
    palavras = [sorted(palavra) for palavra in palavras]
    
    # Verifica se todas as palavras ordenadas são iguais à primeira
    return all(palavra == palavras_ordenadas[0] for palavra in palavras_ordenadas)

# Testes
print(sao_anagramas("listen", "silent"))  # Deve imprimir True
print(sao_anagramas("hello", "world"))    # Deve imprimir False
print(sao_anagramas("ana", "naa"))         # Deve imprimir True
    
