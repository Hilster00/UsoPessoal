import socket
import threading

# Variável de controle para encerrar o servidor
servidor_ativo = True

# Variável global para o socket do servidor
socket_servidor = None

# Porta inicial (o valor real será definido dinamicamente pelo sistema)
porta_servidor = 0

# Lista para armazenar conexões dos clientes
conexoes = []

#lista usuários
usuarios={}

def enviar_mensagem(socket_cliente, mensagem):
    socket_cliente.sendall(mensagem.encode('utf-8'))
        
# Função para lidar com as mensagens dos clientes
def lidar_com_cliente(socket_cliente, endereco):
    print(f"Nova conexão estabelecida: {endereco}")

    # Adiciona o socket do cliente à lista de conexões
    conexoes.append(socket_cliente)

    # Recebe mensagem do cliente
    login = socket_cliente.recv(1024).decode("utf-8")
   
    if usuarios.get(login) == None:
        usuarios[login] = socket_cliente
        while True:
                    try:
                        # Recebe mensagem do cliente
                        mensagem = socket_cliente.recv(1024).decode("utf-8")

                        if not mensagem:
                            break
                        else:
                            print(mensagem)
                            retorno=comandos_cliente(mensagem)
                            if retorno == "fechar":
                                usuarios.pop(login)
                                break
                        # Envia a mensagem para todos os clientes conectados
                        #difundir(mensagem)

                    except Exception as e:
                        print(f"Erro ao lidar com o cliente {endereco}: {e}")
                        break

        # Remove o cliente da lista de conexões e fecha o socket
        conexoes.remove(socket_cliente)
        socket_cliente.close()
        print(f"Conexão encerrada: {endereco}")
    else:
        enviar_mensagem(socket_cliente, "Usuário já está em uso")
    

# Função para enviar uma mensagem a todos os clientes
def difundir(mensagem):
    for conexao in conexoes:
        try:
            conexao.send(mensagem.encode("utf-8"))
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

# Função para aceitar novas conexões
def aceitar_conexoes():
    global servidor_ativo
    global socket_servidor

    while servidor_ativo:
        try:
            socket_cliente, endereco = socket_servidor.accept()
            thread_cliente = threading.Thread(target=lidar_com_cliente, args=(socket_cliente, endereco))
            thread_cliente.start()
        except Exception as e:
            if servidor_ativo:
                print(f"Erro ao aceitar nova conexão: {e}")
                

# Função para redirecionar conexões para outro servidor
def redirecionar_conexoes(novo_host, novo_porta):
    global servidor_ativo
    global socket_servidor
    global porta_servidor

    print(f"Redirecionando conexões para o novo servidor: {novo_host}:{novo_porta}")

    # Fecha todos os sockets dos clientes
    for conexao in conexoes:
        conexao.close()

    # Fecha o socket do servidor atual
    socket_servidor.close()

    # Cria e inicia o socket para o novo servidor
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind(('', novo_porta))  # Porta definida manualmente
    socket_servidor.listen(5)
    print(f"Novo servidor ouvindo em {novo_host}:{novo_porta}")

    # Atualiza a variável de controle e a porta do servidor
    servidor_ativo = True
    porta_servidor = novo_porta

    # Reinicia a thread para aceitar conexões
    thread_aceitar_conexoes = threading.Thread(target=aceitar_conexoes)
    thread_aceitar_conexoes.start()

# Configurações do servidor
host_servidor = '127.0.0.1'

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(('', 0))  # Porta definida automaticamente pelo sistema
porta_servidor = socket_servidor.getsockname()[1]
socket_servidor.listen(5)
print(f"Servidor ouvindo em {host_servidor}:{porta_servidor}")

# Inicia uma thread para aceitar conexões
thread_aceitar_conexoes = threading.Thread(target=aceitar_conexoes)
thread_aceitar_conexoes.start()

def comandos(comando):
    comando=comando.split(":")
    if comando[0] == "msg":
        mensagem=""
        if comando[1] != "":
            mensagem+=comando[1]
            mensagem+=":"
        else:
            #mensagem+="Servidor"
            ...
        if comando[2] != "":
            if usuarios.get(comando[2]) != None:
                mensagem+=comando[3]
                enviar_mensagem(usuarios[comando[2]], mensagem)
            else:
                print("Usuário inexistente")
        else:
            mensagem+=comando[3]
            difundir(mensagem)
    if comando[0] == "ban":
        if usuarios.get(comando[1]) != None:
            cliente=usuarios[comando[1]]
            enviar_mensagem(cliente, "Você foi Banido!")
            cliente.close()
            usuarios.pop(comando[1])
            
def comandos_cliente(comando):
    comando=comando.split(":")
    if comando[0] == "fechar":
        return 'fechar'
    if comando[1] == "msg":
        if usuarios.get(comando[2]) != None:
            mensagem=f'{comando[0]}:{comando[3]}'
            enviar_mensagem(usuarios[comando[2]], mensagem)
# Loop principal do servidor
while True:
    comando = input("Comando do Servidor: ")

    comandos(comando)
    # Encerra o servidor e redireciona para outro se o comando for "fechar:redirecionar"
    if comando == "fechar:redirecionar":
        nova_porta = input("Informe a porta do novo servidor:")
        if nova_porta.lower() != "fechar":
            redirecionar_conexoes('127.0.0.1', int(nova_porta))
            servidor_ativo = False
            socket_servidor.close()
            break
    if comando == "fechar":
        print("Fechando o Servidor...")
        servidor_ativo = False  # Define a variável de controle para encerrar a thread de aceitação
        socket_servidor.close()  # Fecha o socket do servidor
        break
    elif comando == "port":
        print(f"O servidor está ouvindo na porta: {porta_servidor}")
