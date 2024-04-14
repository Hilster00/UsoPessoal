import os
import shutil
import subprocess
import platform

# Função para renomear arquivos em um diretório
def renomear_arquivos(diretorio):
    try:
        for nome_arquivo in os.listdir(diretorio):
            novo_nome = nome_arquivo.replace(' ', '_')
            os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome))
        print("Arquivos renomeados com sucesso.")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")

# Função para compactar arquivos em um diretório
def compactar_arquivos(diretorio_origem, diretorio_destino):
    try:
        shutil.make_archive(diretorio_destino, 'zip', diretorio_origem)
        print("Arquivos compactados com sucesso.")
    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")

# Função para executar um comando no terminal
def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print("Saída do comando:")
        print(resultado.stdout)
    except Exception as e:
        print(f"Erro ao executar comando: {e}")

# Função para exibir informações do sistema
def informacoes_sistema():
    try:
        sistema = platform.system()
        arquitetura = platform.architecture()[0]
        versao = platform.version()
        print(f"Sistema operacional: {sistema}")
        print(f"Arquitetura do sistema: {arquitetura}")
        print(f"Versão do sistema: {versao}")
    except Exception as e:
        print(f"Erro ao obter informações do sistema: {e}")

# Função para criar um diretório
def criar_diretorio(caminho):
    try:
        os.makedirs(caminho, exist_ok=True)
        print("Diretório criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar diretório: {e}")

# Função para remover um diretório
def remover_diretorio(caminho):
    try:
        shutil.rmtree(caminho)
        print("Diretório removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover diretório: {e}")

# Exemplo de utilização das funções
if __name__ == "__main__":
    diretorio_origem = '/caminho/para/arquivos'
    diretorio_destino = '/caminho/para/backup'
    diretorio_novo = '/caminho/novo/diretorio'
    
    renomear_arquivos(diretorio_origem)
    compactar_arquivos(diretorio_origem, diretorio_destino)
    executar_comando('ls -l')
    informacoes_sistema()
    criar_diretorio(diretorio_novo)
    remover_diretorio(diretorio_novo)
