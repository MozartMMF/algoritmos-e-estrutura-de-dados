from collections import defaultdict, deque

def validar_arvore_binaria(arestas):

    if not arestas:
        return True
    
    adjacencia = defaultdict(list)
    filhos_set = set()
    todos_nos = set()

    for pai, filho in arestas:
        if pai == filho:
            return False
        
        if filho in filhos_set:
            return False
        
        adjacencia[pai].append(filho)
        filhos_set.add(filho)
        todos_nos.add(pai)
        todos_nos.add(filho)

        if len(adjacencia[pai]) > 2:
            return False
        
    possiveis_raizes = todos_nos - filhos_set

    if len(possiveis_raizes) != 1:
        return False
    
    raiz = possiveis_raizes.pop() 

    fila = deque([raiz])
    visitados = {raiz}

    while fila:
        no_atual = fila.popleft()

        for vizinho in adjacencia[no_atual]:
            if vizinho in visitados:
                return False
            
            visitados.add(vizinho)
            fila.append(vizinho)
    
    return len(visitados) == len(todos_nos)



arestas_validas = [(1, 2), (1, 3)]
print(f"Caso 1 (Válido): {validar_arvore_binaria(arestas_validas)}") 


arestas_tres_filhos = [(1, 2), (1, 3), (1, 4)]
print(f"Caso 2 (3 Filhos): {validar_arvore_binaria(arestas_tres_filhos)}")


arestas_ciclo = [(1, 2), (2, 3), (3, 1)]
print(f"Caso 3 (Ciclo): {validar_arvore_binaria(arestas_ciclo)}")


arestas_desconexas = [(1, 2), (3, 4)]
print(f"Caso 4 (Desconexo): {validar_arvore_binaria(arestas_desconexas)}")