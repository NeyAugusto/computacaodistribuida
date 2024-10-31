import socket
import threading

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP local
PORT = 12345        # Porta de escuta

# Criando o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # Vinculando o socket ao endereço IP e porta
server.listen()  # Colocando o servidor no modo de escuta para conexões

clients = []  # Lista para armazenar os clientes conectados

# Função para enviar mensagens para todos os clientes conectados, exceto o remetente
def broadcast(message, sender):
    for client in clients:
        if client != sender:  # Não enviar para o remetente
            client.send(message)

# Função para lidar com a comunicação de um cliente específico
def handle_client(client):
    while True:
        try:
            # Recebe mensagem do cliente
            message = client.recv(1024)
            # Envia a mensagem para todos os outros clientes
            broadcast(message, client)
        except:
            # Remove o cliente da lista e fecha a conexão em caso de erro
            clients.remove(client)
            client.close()
            break

# Função para aceitar novas conexões de clientes
def receive_connections():
    while True:
        # Aceita uma nova conexão de cliente
        client, address = server.accept()
        print(f"Conectado com {str(address)}")
        clients.append(client)  # Adiciona o novo cliente à lista
        # Inicia uma nova thread para lidar com a comunicação do cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Iniciando o servidor
print("Servidor está escutando...")
receive_connections()