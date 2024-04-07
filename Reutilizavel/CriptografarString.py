import secrets

# Função para gerar uma chave de criptografia
def gerar_chave():
    chave = secrets.token_hex(16)  # Gera uma chave hexadecimal de 16 bytes
    return chave

# Função para criptografar uma mensagem
def criptografar_mensagem(mensagem, chave):
    mensagem_criptografada = ""
    for caractere, caractere_chave in zip(mensagem, chave):
        caractere_criptografado = chr(ord(caractere) ^ ord(caractere_chave))  # Aplica operação XOR
        mensagem_criptografada += caractere_criptografado
    return mensagem_criptografada

# Função para descriptografar uma mensagem
def descriptografar_mensagem(mensagem_criptografada, chave):
    mensagem_descriptografada = ""
    for caractere, caractere_chave in zip(mensagem_criptografada, chave):
        caractere_descriptografado = chr(ord(caractere) ^ ord(caractere_chave))  # Aplica operação XOR
        mensagem_descriptografada += caractere_descriptografado
    return mensagem_descriptografada

# Função principal para criptografar ou descriptografar uma mensagem
def cripto_mensagem(mensagem, chave=None):
    if chave is None:
        chave = gerar_chave()
        return (criptografar_mensagem(mensagem, chave), chave)
    else:
        return descriptografar_mensagem(mensagem, chave)

# Exemplo de uso
mensagem = "Olá, mundo!"
mensagem_criptografada, chave = cripto_mensagem(mensagem)
print("Mensagem criptografada:", mensagem_criptografada)
print("Chave:", chave)

mensagem_descriptografada = cripto_mensagem(mensagem_criptografada, chave)
print("Mensagem descriptografada:", mensagem_descriptografada)
