import heapq

def dijkstra_com_restricoes(grafo, inicio, fim, proibidos=None):
    if proibidos is None:
        proibidos = set()
    else:
        proibidos = set(proibidos)

    if inicio in proibidos or fim in proibidos:
        return float('inf'), []
    
    fila =[(0, inicio)]

    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0

    predecessores = {no: None for no in grafo}

    while fila:
        custo_atual, no_atual = heapq.heappop(fila)

        if no_atual == fim:
            break

        if custo_atual > distancias[no_atual]:
            continue

        for vizinho, peso in grafo[no_atual].items():
            if vizinho in proibidos:
                continue

            nova_distancia = custo_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (nova_distancia, vizinho))

    caminho = []
    passo = fim

    if distancias[fim] == float('inf'):
        return float('inf'), []
    
    while passo is not None:
        caminho.insert(0, passo)
        passo = predecessores[passo]

    return distancias[fim], caminho

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 3, 'D': 7, 'E': 5},
    'C': {'A': 2, 'B': 3, 'E': 6},
    'D': {'B': 7, 'E': 4, 'F': 8}, 
    'E': {'B': 5, 'C': 6, 'D': 4, 'G': 3},
    'F': {'D': 2, 'G': 4},
    'G': {'E': 3, 'F': 4}
}

custo1, caminho1 = dijkstra_com_restricoes(grafo, 'A', 'F')
print(f"1. Rota Padrão (A -> F):")
print(f"   Custo: {custo1}")
print(f"   Caminho: {caminho1}")
print("-" * 30)


nos_bloqueados = ['E']
custo2, caminho2 = dijkstra_com_restricoes(grafo, 'A', 'F', nos_bloqueados)
print(f"2. Rota evitando {nos_bloqueados} (A -> F):")
print(f"   Custo: {custo2}")
print(f"   Caminho: {caminho2}")
print("-" * 30)


nos_bloqueados_criticos = ['B', 'C']
custo3, caminho3 = dijkstra_com_restricoes(grafo, 'A', 'F', nos_bloqueados_criticos)
print(f"3. Rota evitando {nos_bloqueados_criticos} (A -> F):")
print(f"   Custo: {custo3} (infinito significa inalcançável)")
print(f"   Caminho: {caminho3}")