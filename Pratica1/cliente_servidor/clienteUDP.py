import socket
import threading

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta de conexão do servidor

# Criando o socket do cliente UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Função para receber mensagens do servidor
def receive_messages():
    while True:
        try:
            message, _ = client.recvfrom(1024)  # Recebendo mensagens
            print(message.decode('utf-8'))      # Exibindo a mensagem no terminal
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

# Função para enviar mensagens ao servidor
def send_messages():
    while True:
        message = input("")  # Coletando mensagem do usuário
        try:
            client.sendto(message.encode('utf-8'), (HOST, PORT))  # Enviando mensagem para o servidor
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            break

# Criando e iniciando threads para enviar e receber mensagens
thread_receive = threading.Thread(target=receive_messages)
thread_receive.start()

thread_send = threading.Thread(target=send_messages)
thread_send.start()


