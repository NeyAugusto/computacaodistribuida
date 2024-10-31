import socket
import logging

# Configuração do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP local
PORT = 12345        # Porta de escuta

# Criando o socket UDP do servidora
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))  # Vinculando o socket ao endereço IP e porta

clients = set()  # Conjunto para armazenar os clientes conectados

# Loop principal para receber e distribuir mensagens
logging.info("Servidor UDP está escutando...")  # Mensagem inicial
while True:
    try:
        # Recebendo mensagem e endereço do cliente
        message, address = server.recvfrom(1024)
        logging.info(f"Mensagem de {address}: {message.decode('utf-8')}")

        # Adicionando o cliente à lista de clientes conhecidos
        clients.add(address)

        # Distribuindo a mensagem para todos os outros clientes
        for client in clients:
            if client != address:  # Não enviar a mensagem de volta ao remetente
                server.sendto(message, client)

    except ConnectionResetError as e:
        logging.warning(f"Conexão resetada: {e}")
    except Exception as e:
        logging.error(f"Erro ao receber ou enviar mensagem: {e}")