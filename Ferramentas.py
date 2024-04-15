import random
import string
import hashlib
import requests
import json

# Função para gerar uma senha aleatória
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Função para calcular o hash SHA-256 de uma string
def calcular_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

# Função para buscar informações de um CEP usando uma API
def buscar_informacoes_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Erro ao buscar informações do CEP: {e}")
        return None

# Função para formatar e exibir as informações de um CEP
def exibir_informacoes_cep(cep_info):
    if cep_info:
        print("Informações do CEP:")
        print(f"CEP: {cep_info['cep']}")
        print(f"Logradouro: {cep_info['logradouro']}")
        print(f"Complemento: {cep_info['complemento']}")
        print(f"Bairro: {cep_info['bairro']}")
        print(f"Cidade: {cep_info['localidade']}")
        print(f"Estado: {cep_info['uf']}")
    else:
        print("CEP não encontrado ou inválido.")

# Função para buscar informações sobre um filme usando uma API
def buscar_informacoes_filme(titulo):
    try:
        url = f"http://www.omdbapi.com/?apikey=your_api_key&t={titulo}"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Erro ao buscar informações do filme: {e}")
        return None

# Função para exibir as informações de um filme
def exibir_informacoes_filme(filme_info):
    if filme_info and filme_info.get('Response') == 'True':
        print("Informações do filme:")
        print(f"Título: {filme_info['Title']}")
        print(f"Ano: {filme_info['Year']}")
        print(f"Gênero: {filme_info['Genre']}")
        print(f"Diretor: {filme_info['Director']}")
        print(f"Atores: {filme_info['Actors']}")
        print(f"Sinopse: {filme_info['Plot']}")
    else:
        print("Filme não encontrado.")

# Exemplo de utilização das funções
if __name__ == "__main__":
    # Gerar uma senha aleatória
    senha = gerar_senha()
    print("Senha aleatória:", senha)

    # Calcular o hash SHA-256 de uma senha
    hash_senha = calcular_hash(senha)
    print("Hash da senha:", hash_senha)

    # Buscar informações de um CEP
    cep = "01001000"  # CEP da Av. Paulista, São Paulo
    cep_info = buscar_informacoes_cep(cep)
    exibir_informacoes_cep(cep_info)

    # Buscar informações de um filme
    titulo_filme = "Inception"
    filme_info = buscar_informacoes_filme(titulo_filme)
    exibir_informacoes_filme(filme_info)
