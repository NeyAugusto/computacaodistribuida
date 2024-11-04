# SISTEMAS DISTRIBUÍDOS E COMPUTAÇÃO PARALELA

Projeto: Práticas em Sistemas Distribuídos e Computação Paralela

Este repositório contém implementações práticas de tópicos avançados em sistemas distribuídos e computação paralela, com foco em paradigmas de comunicação, coordenação, sincronização e automação com Kubernetes.

1. Paradigmas de Comunicação

Objetivo.: Implementar e comparar diferentes paradigmas de comunicação em sistemas distribuídos, abordando protocolos TCP e UDP.

Descrição.: Desenvolvimento de uma aplicação de chat distribuído onde múltiplos clientes podem enviar e receber mensagens por meio de um servidor central. Esta prática inclui:

Implementação com sockets TCP: Comunicação confiável com controle de conexão.
Implementação com sockets UDP: Comunicação sem conexão, explorando o desempenho e a simplicidade do protocolo.

Comparação.: Comparação entre TCP e UDP em termos de desempenho e confiabilidade.

Ferramentas.:

Linguagem: Python
Bibliotecas: Módulos de comunicação de rede (socket)

2. Coordenação, Tempo, Relógios Lógicos e Sincronização

Objetivo.: Implementar mecanismos de coordenação e sincronização de tempo em sistemas distribuídos, abordando algoritmos de eleição para coordenação de processos.

Descrição.: Implementação de um algoritmo de eleição, como o Algoritmo de Bully, para eleger um coordenador em um ambiente distribuído. As principais tarefas incluem:

Algoritmo de eleição: Implementação de uma aplicação onde múltiplos processos participam de uma eleição.
Testes de robustez: Avaliar a robustez do algoritmo em cenários de falha de processos.

Ferramentas.:

Linguagem: Python

3. Automação da Implantação, Escalonamento e Gerenciamento com Kubernetes

Objetivo.: Configurar e gerenciar aplicações distribuídas utilizando Kubernetes, focando na automação da implantação, escalonamento e monitoramento de aplicações.

Descrição.: Configuração de um cluster Kubernetes local com Minikube e gerenciamento de uma aplicação de microserviços simples, composta por frontend e backend.

Tarefas.:

1. Instalação do Minikube: Configurar um cluster Kubernetes local.
2. Configuração YAML: Definir pods, serviços e deployments.
3. Implantação de aplicação de microserviços: Configurar uma aplicação web com frontend e backend.
4. Escalonamento automático: Configurar o Horizontal Pod Autoscaler para ajuste automático de recursos.
5. Monitoramento: Monitorar a aplicação utilizando o Kubernetes Dashboard.

Ferramentas.:

Minikube
kubectl
Kubernetes Dashboard


Pré-requisitos.:

Python 3.x para implementações de comunicação e coordenação
Minikube ekubectl para automação com Kubernetes
Kubernetes Dashboard para monitoramento das aplicações

Instruções de Uso

1.Configuração do Ambiente: Certifiquese de que Python, Minikube e kubectl estão instalados no sistema.
2.Execução dos Códigos: Acesse os diretórios correspondentes para cada prática e siga as instruções nos arquivos README específicos.
3.Monitoramento: Após a implantação no Kubernetes, acesse o Kubernetes Dashboard para monitorar os recursos e o escalonamento automático da aplicação.



Este projeto é parte de estudos avançados em computação distribuída e paralela, visando entender e aplicar conceitos de comunicação, coordenação e gerenciamento de aplicações em ambientes distribuídos.
