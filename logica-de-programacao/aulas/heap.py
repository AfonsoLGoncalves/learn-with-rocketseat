from heapq import *

fila_prioridade = []
heappush(fila_prioridade, (2, 'Atender cliente VIP'))
heappush(fila_prioridade, (1, 'Atender cliente VIP'))
heappush(fila_prioridade, (3, 'Ler e-mails'))
heappush(fila_prioridade, (1, 'Apagar Incêndio'))
print(fila_prioridade)


# Retira as tarefas de acordo com a prioridade, por mais que a lista esteja fora de ordem
while fila_prioridade:
    prioridade, tarefa = heappop(fila_prioridade)
    print(f'Executando: {tarefa} - Prioridade: {prioridade}')