import socket
import threading

def receber_mensagens(sock):
    while True:
        try:
            mensagem = sock.recv(1024).decode('utf-8')
            print(f"{mensagem}")
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

def enviar_mensagens(sock, nome):
    while True:
        mensagem = input("Digite a mensagem para enviar (ou 'fechar' para encerrar): ")
        sock.sendall(f"{nome}:{mensagem}".encode('utf-8'))
        if mensagem.lower() == 'fechar':
            break

# Configurações do cliente
host = '127.0.0.1'
porta_servidor = int(input("Digite a porta do servidor: "))
nome_cliente = input("Digite seu nome: ")

# Conecta-se ao servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, porta_servidor))

    # Envia o nome do cliente para o servidor
    s.sendall(nome_cliente.encode('utf-8'))

    # Inicia threads para receber e enviar mensagens
    thread_receber = threading.Thread(target=receber_mensagens, args=(s,))
    thread_enviar = threading.Thread(target=enviar_mensagens, args=(s, nome_cliente))

    thread_receber.start()
    thread_enviar.start()

    # Aguarda até que a thread de envio termine (quando o usuário digitar 'fechar')
    thread_enviar.join()

print("Conexão encerrada.")
