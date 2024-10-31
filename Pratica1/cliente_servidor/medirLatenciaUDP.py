import socket
import time

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta de conexão do servidor

# Criando o socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    start_time = time.time()  # Início da medição de tempo
    s.sendto(b'Hello, server', (HOST, PORT))  # Envia mensagem ao servidor
    data, addr = s.recvfrom(1024)  # Recebe a resposta do servidor
    end_time = time.time()  # Fim da medição de tempo

# Calculando e exibindo a latência em milissegundos
latency = end_time - start_time
print(f'Latência (UDP): {latency * 1000:.2f} ms')  # Exibindo a latência em milissegundos
