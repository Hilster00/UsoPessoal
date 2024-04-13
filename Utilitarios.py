import os
import shutil
import psutil
import subprocess
import getpass

# Função para realizar backup de arquivos importantes
def fazer_backup(diretorio_origem, diretorio_destino):
    try:
        shutil.make_archive(diretorio_destino, 'zip', diretorio_origem)
        print("Backup concluído com sucesso.")
    except Exception as e:
        print(f"Erro ao fazer backup: {e}")

# Função para monitorar os recursos do sistema
def monitorar_recursos():
    try:
        with open('system_status.txt', 'w') as f:
            subprocess.call(['top', '-n', '1'], stdout=f)
        print("Monitoramento de recursos do sistema concluído.")
    except Exception as e:
        print(f"Erro ao monitorar recursos do sistema: {e}")

# Função para instalar pacotes usando o gerenciador de pacotes do sistema
def instalar_pacotes(pacotes):
    try:
        subprocess.call(['sudo', 'apt-get', 'update'])
        subprocess.call(['sudo', 'apt-get', 'install', '-y'] + pacotes)
        print("Pacotes instalados com sucesso.")
    except Exception as e:
        print(f"Erro ao instalar pacotes: {e}")

# Função para verificar a segurança de senhas
def verificar_seguranca_senhas():
    try:
        subprocess.call(['pwqcheck', '-r', 'rules.txt'])
        print("Verificação de segurança de senhas concluída.")
    except Exception as e:
        print(f"Erro ao verificar segurança de senhas: {e}")

# Função para criar um relatório de utilização de disco
def criar_relatorio_disco():
    try:
        with open('disk_usage_report.txt', 'w') as f:
            subprocess.call(['df', '-h'], stdout=f)
        print("Relatório de utilização de disco gerado.")
    except Exception as e:
        print(f"Erro ao criar relatório de utilização de disco: {e}")

# Função para executar um teste de conectividade de rede
def teste_conectividade():
    try:
        with open('connectivity_test.txt', 'w') as f:
            subprocess.call(['ping', '-c', '5', 'google.com'], stdout=f)
        print("Teste de conectividade concluído.")
    except Exception as e:
        print(f"Erro ao executar teste de conectividade: {e}")

# Função para limpar logs antigos
def limpar_logs_antigos(diretorio_logs, dias=7):
    try:
        for arquivo in os.listdir(diretorio_logs):
            if arquivo.endswith('.log'):
                caminho_arquivo = os.path.join(diretorio_logs, arquivo)
                if os.stat(caminho_arquivo).st_mtime < (time.time() - dias * 86400):
                    os.remove(caminho_arquivo)
        print("Logs antigos removidos.")
    except Exception as e:
        print(f"Erro ao limpar logs antigos: {e}")

# Exemplo de utilização das funções
if __name__ == "__main__":
    diretorio_origem = '/caminho/para/arquivos'
    diretorio_destino = '/caminho/para/backup.zip'
    fazer_backup(diretorio_origem, diretorio_destino)

    monitorar_recursos()

    pacotes = ['htop', 'vim', 'git']
    instalar_pacotes(pacotes)

    verificar_seguranca_senhas()

    criar_relatorio_disco()

    teste_conectividade()

    diretorio_logs = '/var/log'
    limpar_logs_antigos(diretorio_logs)
