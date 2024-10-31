import threading  # Para permitir a execução simultânea de threads
import time  # Para funções de pausa
import random  # Para gerar seleções aleatórias

class Processo:
    def __init__(self, id, processos):
        self.id = id  # Identificador único do processo
        self.coordenador = None  # Coordenador atual, inicialmente indefinido
        self.processos = processos  # Lista de processos na rede
        self.ativo = True  # Estado do processo, ativo ou inativo

    def iniciar_eleicao(self):
        # Método para iniciar uma nova eleição de coordenador
        print(f"Processo {self.id} iniciou uma eleição")
        
        # Filtra processos com ID maior que o atual e que estão ativos
        candidatos = [p for p in self.processos if p.id > self.id and p.ativo]

        # Se não houver candidatos, este processo se torna o coordenador
        if not candidatos:
            self.coordenador = self.id
            print(f"Processo {self.id} é o novo coordenador")
            self.anunciar_coordenador()  # Anuncia o novo coordenador para todos os processos
        else:
            # Envia uma mensagem de eleição para os candidatos
            for p in candidatos:
                p.receber_eleicao(self)

    def receber_eleicao(self, solicitante):
        # Método chamado quando um processo recebe uma mensagem de eleição
        print(f"Processo {self.id} recebeu mensagem de eleição de Processo {solicitante.id}")
        if self.ativo:
            self.iniciar_eleicao()  # Inicia uma nova eleição se o processo estiver ativo

    def anunciar_coordenador(self):
        # Anuncia o novo coordenador para todos os processos ativos
        for p in self.processos:
            if p.id != self.id and p.ativo:  # Ignora o próprio processo
                p.coordenador = self.id  # Define o coordenador no processo
                print(f"Processo {self.id} anunciou que é o novo coordenador para Processo {p.id}")

    def verificar_coordenador_continuamente(self):
        # Verifica continuamente se o coordenador atual está ativo
        while self.ativo:
            # Se o coordenador não estiver definido ou não estiver ativo, inicia uma nova eleição
            if self.coordenador is None or not any(p.id == self.coordenador and p.ativo for p in self.processos):
                print(f"Processo {self.id} detectou que o coordenador falhou")
                self.iniciar_eleicao()  # Inicia a eleição
            time.sleep(2)  # Aguarda um intervalo antes de verificar novamente

    def parar(self):
        # Método para parar o processo
        self.ativo = False  # Define o estado do processo como inativo

def simular_falha(processos, tempo_falha):
    # Simula a falha de um processo após um determinado tempo
    time.sleep(tempo_falha)  # Aguarda um tempo antes de simular a falha
    falha = random.choice(processos)  # Escolhe um processo aleatoriamente
    falha.ativo = False  # Define o processo como inativo
    print(f"Processo {falha.id} falhou")  # Notifica que o processo falhou

def teste_robustez(processos):
    # Testes de robustez para o algoritmo de eleição
    # Teste 1: Simular falhas em diferentes momentos
    for i in range(3):
        time.sleep(random.randint(1, 5))  # Espera um intervalo aleatório entre 1 e 5 segundos
        threading.Thread(target=simular_falha, args=(processos, 0)).start()  # Inicia uma nova thread para simular a falha

    # Teste 2: Medir tempo para eleição após falha
    time.sleep(6)  # Espera para garantir que algumas falhas tenham ocorrido
    print("\nTeste 2: Medindo tempo para nova eleição...")
    inicio = time.time()  # Registra o tempo de início da eleição
    coordenador_atual = next((p for p in processos if p.ativo and p.coordenador is not None), None)  # Encontra o coordenador atual ativo
    if coordenador_atual:
        coordenador_atual.ativo = False  # Simula a falha do coordenador
        print(f"Processo {coordenador_atual.id} falhou como coordenador.")
    else:
        print("Nenhum coordenador ativo.")

    time.sleep(5)  # Espera para permitir que a nova eleição ocorra
    fim = time.time()  # Registra o tempo de término da eleição
    print(f"Tempo para nova eleição: {fim - inicio:.2f} segundos\n")  # Exibe o tempo total para a nova eleição

# Exemplo de uso:
processos = [Processo(i, []) for i in range(5)]  # Cria 5 processos
for p in processos:
    p.processos = processos  # Atribui a lista de processos a cada processo

# Threads para verificar continuamente o coordenador
for p in processos:
    threading.Thread(target=p.verificar_coordenador_continuamente).start()  # Inicia uma thread para cada processo

# Executa o teste de robustez
teste_robustez(processos)

# Aguardar alguns segundos antes de encerrar o programa
time.sleep(10)  # Ajuste conforme necessário para observar a simulação

# Parar todos os processos
for p in processos:
    p.parar()  # Chama o método para parar cada processo

print("Todos os processos foram parados.")  # Mensagem final para indicar que todos os processos foram encerrados
