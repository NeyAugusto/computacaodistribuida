import threading  # Biblioteca para manipular threads
import time       # Biblioteca para pausas de tempo
import random     # Biblioteca para operações aleatórias

# Classe que representa um processo no sistema distribuído
class Processo:
    def __init__(self, id, processos):
        self.id = id                   # Identificador único do processo
        self.coordenador = None         # Coordenador atual (pode ser o próprio ou outro processo)
        self.processos = processos      # Lista de todos os processos no sistema
        self.ativo = True               # Estado do processo (ativo ou falho)

    # Método para iniciar uma eleição caso o coordenador falhe
    def iniciar_eleicao(self):
        print(f"Processo {self.id} iniciou uma eleição")
        # Lista de processos candidatos (processos com IDs maiores e ativos)
        candidatos = [p for p in self.processos if p.id > self.id and p.ativo]
        
        # Se não houver candidatos, o processo atual se torna o coordenador
        if not candidatos:
            self.coordenador = self.id
            print(f"Processo {self.id} é o novo coordenador")
            self.anunciar_coordenador()  # Anuncia aos outros que é o coordenador
        else:
            # Envia mensagem de eleição para cada candidato
            for p in candidatos:
                p.receber_eleicao(self)

    # Método para receber uma mensagem de eleição de outro processo
    def receber_eleicao(self, solicitante):
        print(f"Processo {self.id} recebeu mensagem de eleição de Processo {solicitante.id}")
        # Se o processo está ativo, ele inicia sua própria eleição
        if self.ativo:
            self.iniciar_eleicao()

    # Método para anunciar a todos que este processo é o novo coordenador
    def anunciar_coordenador(self):
        for p in self.processos:
            if p.id != self.id and p.ativo:  # Só envia para processos diferentes e ativos
                p.coordenador = self.id
                print(f"Processo {self.id} anunciou que é o novo coordenador para Processo {p.id}")

    # Método para verificar periodicamente se o coordenador atual ainda está ativo
    def verificar_coordenador(self):
        # Se o coordenador não está definido ou não está ativo, inicia uma eleição
        if self.coordenador is None or not any(p.id == self.coordenador and p.ativo for p in self.processos):
            print(f"Processo {self.id} detectou que o coordenador falhou")
            self.iniciar_eleicao()

# Função para simular uma falha aleatória em um processo após um tempo específico
def simular_falha(processos, tempo_falha):
    time.sleep(tempo_falha)  # Pausa antes de iniciar a falha
    falha = random.choice(processos)  # Escolhe um processo aleatório
    falha.ativo = False               # Define o processo como inativo (falho)
    print(f"Processo {falha.id} falhou")

# Exemplo de uso:

# Criação de uma lista de processos com IDs de 0 a 4
processos = [Processo(i, []) for i in range(5)]
for p in processos:
    p.processos = processos  # Cada processo recebe a lista completa de processos

# Criação de uma thread para simular falhas após um tempo
threading.Thread(target=simular_falha, args=(processos, 3)).start()

# Cada processo inicia uma thread para verificar periodicamente o coordenador
for p in processos:
    threading.Thread(target=lambda: [time.sleep(2), p.verificar_coordenador()]).start()
