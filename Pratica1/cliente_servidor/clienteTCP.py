import socket
import threading
from datetime import datetime

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta de conexão do servidor

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Função para obter o timestamp atual formatado
def get_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Receber mensagens do servidor
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # Move o cursor para uma nova linha para exibir a mensagem do servidor corretamente
            print(f"\r[Servidor] {get_timestamp()} {message}\n[Você] ", end="") 
        except:
            print("\nErro ao receber mensagem.")
            client.close()
            break

# Enviar mensagens ao servidor
def send_messages():
    while True:
        message = input("[Você] ")  # Prefixo para mensagens do usuário
        client.send(message.encode('utf-8'))

# Iniciar thread para receber mensagens
thread_receive = threading.Thread(target=receive_messages, args=(client,))
thread_receive.start()

# Iniciar thread para enviar mensagens
thread_send = threading.Thread(target=send_messages)
thread_send.start()







