import socket
import time

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta de conexão do servidor

# Função para medir a latência
def measure_latency():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        start_time = time.time()  # Início da medição
        s.sendall(b'Hello, server')  # Envia uma mensagem simples ao servidor
        data = s.recv(1024)  # Recebe a resposta do servidor
        end_time = time.time()  # Fim da medição

    # Calcula e exibe a latência em milissegundos
    latency = end_time - start_time
    print(f'Latência (TCP): {latency * 1000:.2f} ms')

if __name__ == "__main__":
    measure_latency()
